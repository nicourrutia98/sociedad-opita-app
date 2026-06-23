#!/usr/bin/env node
/**
 * check-lexicon.mjs — Linter de léxico para monumento-cultural-v1
 * Bloquea 21 palabras blacklist (R3 decisión) y verifica 7 frases whitelist.
 *
 * Uso:
 *   node scripts/check-lexicon.mjs                     # scan bundle completo
 *   node scripts/check-lexicon.mjs path/to/file        # scan un archivo (test fixture)
 *   STRICT=1 node scripts/check-lexicon.mjs            # exit 2 si falta whitelist
 *
 * Exit codes:
 *   0  clean
 *   1  blacklist hit (con file:line:col)
 *   2  whitelist missing (solo en modo --strict o single-file sin whitelist)
 *
 * Whitelist phrases (7) — ver spec/lexicon-guard
 * Blacklist words (21) — ver R3 decisión confirmada
 *
 * Excepciones inline: <!-- lex:allow [palabra] --> permite la palabra en ESE archivo.
 * Cada uso de lex:allow se imprime a stderr para auditoría.
 */

import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, relative, extname, resolve } from "node:path";

const ROOT = process.cwd();

const BLACKLIST = [
  "engagement",
  "usuarios",
  "data",
  "contenido",
  "métricas",
  "KPI",
  "growth",
  "funnel",
  "cliente",
  "consumidor",
  "viral",
  "growth hack",
  "changelog",
  "release notes",
  "SaaS",
  "dark pattern",
  "FOMO",
  "streak",
  "daily login bonus",
  "leaderboard",
  "tier",
];

const WHITELIST = [
  "monumento digital vivo",
  "memoria que también es Tello",
  "herida que se honra",
  "pueblo",
  "para que Tello no se muera cuando los pelaos se vayan pa' Bogotá",
  "Te estamos dejando asomarte",
  "Hecho por un nativo huilense, en el Huila, con IA",
];

const EXTS = new Set([".html", ".md", ".astro"]);
const SKIP_DIRS = new Set([
  "node_modules",
  ".git",
  "dist",
  ".astro",
  "_astro",
  ".githooks",
  "scripts",
  ".github",
  "tests",
]);

function walk(dir, files = []) {
  for (const entry of readdirSync(dir)) {
    if (SKIP_DIRS.has(entry)) continue;
    const full = join(dir, entry);
    let s;
    try {
      s = statSync(full);
    } catch {
      continue;
    }
    if (s.isDirectory()) walk(full, files);
    else if (EXTS.has(extname(entry))) files.push(full);
  }
  return files;
}

function escapeRe(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

const ALLOW_RE = /<!--\s*lex:allow\s+(\S+?)\s*-->/g;

function findBlacklistHits(text, relFile) {
  const hits = [];
  const allowed = new Set();
  let m;
  ALLOW_RE.lastIndex = 0;
  while ((m = ALLOW_RE.exec(text)) !== null) {
    const word = m[1].toLowerCase();
    allowed.add(word);
    process.stderr.write(`[allow] ${relFile}: lex:allow ${m[1]}\n`);
  }

  const lines = text.split("\n");
  for (const word of BLACKLIST) {
    if (allowed.has(word.toLowerCase())) continue;
    const wordRe = new RegExp(`\\b${escapeRe(word)}\\b`, "gi");
    for (let i = 0; i < lines.length; i++) {
      const stripped = lines[i].replace(
        /<!--\s*lex:allow\s+\S+?\s*-->/g,
        ""
      );
      const lineRe = new RegExp(`\\b${escapeRe(word)}\\b`, "gi");
      let lm;
      while ((lm = lineRe.exec(stripped)) !== null) {
        hits.push({
          file: relFile,
          line: i + 1,
          col: lm.index + 1,
          word,
          match: lm[0],
          context: stripped.trim().slice(0, 100),
        });
      }
    }
  }
  return hits;
}

function main() {
  const args = process.argv.slice(2);
  const strict = process.env.STRICT === "1" || args.includes("--strict");
  const filtered = args.filter((a) => a !== "--strict");
  const single = filtered.length > 0;

  let files;
  if (single) {
    files = filtered.map((a) => resolve(a));
  } else {
    files = walk(ROOT);
  }

  let allHits = [];
  const fileText = {};
  for (const f of files) {
    let text;
    try {
      text = readFileSync(f, "utf8");
    } catch (e) {
      process.stderr.write(`[error] cannot read ${f}: ${e.message}\n`);
      continue;
    }
    fileText[f] = text;
    const hits = findBlacklistHits(text, relative(ROOT, f));
    allHits = allHits.concat(hits);
  }

  for (const h of allHits) {
    process.stderr.write(
      `[blacklist] ${h.file}:${h.line}:${h.col}  ${h.word}  →  ${h.context}\n`
    );
  }

  const missing = [];
  if (single) {
    for (const f of files) {
      if (!fileText[f]) continue;
      const t = fileText[f].toLowerCase();
      for (const phrase of WHITELIST) {
        if (!t.includes(phrase.toLowerCase())) {
          missing.push({ file: relative(ROOT, f), phrase });
        }
      }
    }
  } else {
    const allText = Object.values(fileText).join("\n").toLowerCase();
    for (const phrase of WHITELIST) {
      if (!allText.includes(phrase.toLowerCase())) {
        missing.push({ file: "<bundle>", phrase });
      }
    }
  }

  if (allHits.length > 0) {
    process.stderr.write(
      `\n✗ Blacklist hits: ${allHits.length} across ${files.length} file(s)\n`
    );
    process.exit(1);
  }

  if (missing.length > 0) {
    if (strict) {
      process.stderr.write(
        `\n✗ Whitelist missing (STRICT): ${missing.length} occurrence(s)\n`
      );
      for (const m of missing) {
        process.stderr.write(`  - [${m.file}] "${m.phrase}"\n`);
      }
      process.exit(2);
    }
    process.stderr.write(
      `\n⚠ Whitelist missing (soft, STRICT=1 to enforce): ${missing.length} occurrence(s)\n`
    );
    for (const m of missing) {
      process.stderr.write(`  - [${m.file}] "${m.phrase}"\n`);
    }
    process.stderr.write(
      `  Las 7 frases whitelist se agregan progresivamente en PR 2-4. Después de PR 4, ejecutar con STRICT=1.\n`
    );
    process.exit(0);
  }

  process.stdout.write(
    `✓ ${files.length} file(s) scanned, ${WHITELIST.length}/${WHITELIST.length} whitelist present, 0/${BLACKLIST.length} blacklist hits\n`
  );
  process.exit(0);
}

main();
