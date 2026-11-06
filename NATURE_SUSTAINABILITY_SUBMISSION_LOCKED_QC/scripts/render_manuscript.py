#!/usr/bin/env python3
"""Render manuscript/main_text.md from main_text_template.md + canonical registry.

Placeholder syntax in the template:
  {{key|fmt}}       registry lookup + formatting
  {{eq:...}}        inline math marker (kept verbatim; build_docx converts to OMML)
  {{display_eq:...}} display-equation marker (kept verbatim; -> OMML oMathPara)

Format codes:
  +.3f / .4f / .6f / .0f   signed or plain fixed-point (minus -> U+2212)
  ,                       integer with thousands separators
  pct1                    fraction -> one-decimal percent (0.0351 -> 3.5%)
  sci                     small p -> 'p ≈ M×10^-E' with unicode superscripts
  raw                     str(value)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = json.load(open(os.path.join(ROOT, "analysis", "canonical_results.json")))
TPL = os.path.join(ROOT, "manuscript", "main_text_template.md")
OUT = os.path.join(ROOT, "manuscript", "main_text.md")

SUP = {"-": "⁻", "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
       "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}


def sup(s):
    return "".join(SUP.get(c, c) for c in s)


def fmt_value(v, spec):
    if spec == "raw":
        return str(v)
    if spec == ",":
        return f"{int(round(v)):,}"
    if spec == "pct1":
        return f"{v * 100:.1f}%"
    if spec == "sci":
        # scientific notation with integer mantissa: 1.987e-11 -> p ≈ 2×10⁻¹¹
        m, e = f"{v:.0e}".split("e")
        return f"p ≈ {m}×10{sup(str(int(e)))}"
    m = re.fullmatch(r"(\+?)\.(\d+)f", spec)
    if m:
        s = f"{v:{'+' if m.group(1) else ''}.{m.group(2)}f}"
        return s.replace("-", "−")
    raise ValueError(f"unknown fmt {spec!r}")


def render(text):
    def sub(m):
        key, spec = m.group(1), m.group(2) or "raw"
        if key not in REG:
            raise KeyError(f"no canonical entry for '{key}'")
        return fmt_value(REG[key]["value"], spec)

    # numeric placeholders only; {{eq:}}/{{display_eq:}} survive to docx stage
    return re.sub(r"\{\{(?!eq:|display_eq:)([^{}|]+?)(?:\|([^{}]+))?\}\}", sub, text)


def main():
    src = open(TPL, encoding="utf8").read()
    out = render(src)
    leftover = re.findall(r"\{\{(?!eq:|display_eq:)([^}]+)\}\}", out)
    if leftover:
        sys.exit(f"unresolved placeholders: {leftover[:10]}")
    open(OUT, "w", encoding="utf8").write(out)
    print("rendered", OUT)


if __name__ == "__main__":
    main()
