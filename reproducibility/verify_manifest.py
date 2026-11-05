#!/usr/bin/env python3
"""Verify published notebook and Excel files listed in manifest_sha256.txt.
Uses only Python standard library; no notebook execution is required.
"""
from pathlib import Path
import hashlib, sys

root = Path(__file__).resolve().parent.parent
manifest = root / "manifest_sha256.txt"
errors = []
count = 0
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    if len(line) < 67 or line[64:66] != "  ":
        errors.append("Invalid manifest entry: " + line[:90])
        continue
    expected, relative = line[:64].lower(), line[66:]
    if not all(c in "0123456789abcdef" for c in expected):
        errors.append("Invalid hash: " + relative)
        continue
    path = root / Path(relative)
    if not path.is_file():
        errors.append("MISSING " + relative)
        continue
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(2**20), b""):
            sha.update(block)
    if sha.hexdigest() != expected:
        errors.append("MISMATCH " + relative)
    else:
        count += 1
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"SHA-256 OK: {count} notebook/output files verified.")
