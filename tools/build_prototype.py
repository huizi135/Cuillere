"""Build the standalone Cuillere design preview using only Python's standard library."""
from html import escape
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "prototype" / "source.html"
template = root / "tools" / "prototype-shell.html"
destination = root / "prototype" / "index.html"
fragment = source.read_text(encoding="utf-8")
shell = template.read_text(encoding="utf-8")
marker = "__CUILLERE_FRAGMENT__"
if shell.count(marker) != 1:
    raise SystemExit("Expected exactly one fragment placeholder in the runtime shell.")
with destination.open("w", encoding="utf-8", newline="\n") as output:
    output.write(shell.replace(marker, escape(fragment)))
print("Built prototype/index.html")
