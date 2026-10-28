"""Build MAIN_MANUSCRIPT_NS_inline_LOCKED.docx and _clean_LOCKED.docx
from manuscript/main_text.md + analysis/canonical_results.json.

All analysis numbers come from the canonical registry (no literals).
{{eq:...}} markers -> inline OMML oMath runs.
{{display_eq:...}} markers -> OMML oMathPara display equations.
"""
import json
import re
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "manuscript", "main_text.md")
FIGDIR = os.path.join(ROOT, "figures")
REG = {k: v["value"] for k, v in json.load(open(os.path.join(ROOT, "analysis", "canonical_results.json"))).items()}

MINUS = "−"


def v(key):
    return float(REG[key])


def s3(x, dec=3):
    s = f"{x:+.{dec}f}"
    return s.replace("-", MINUS)


def p3(x):
    return f"{x:.3f}"


def ci(lo, hi, dec=3):
    return f"[{s3(lo, dec)}, {s3(hi, dec)}]"


# ---------------- OMML emitters ----------------
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"


def _m(tag):
    el = OxmlElement("m:" + tag)
    return el


def _mrun(text, sty="p"):
    r = _m("r")
    rPr = _m("rPr")
    st = _m("sty")
    st.set(qn("m:val"), sty)
    rPr.append(st)
    r.append(rPr)
    t = _m("t")
    t.text = text
    r.append(t)
    return r


# symbol table: minimal OMML composer for our small formula vocabulary.
# Tokens: identifiers, greek (β γ α ε μ), subscripts "_x", superscripts "^x",
# sqrt(...), fraction via '/', operators + - = × ( ) , . ′ digits spaces.

GREEK = {"β": "β", "γ": "γ", "α": "α", "ε": "ε", "μ": "μ", "Δ": "Δ",
         "θ": "θ", "σ": "σ", "δ": "δ", "λ": "λ", "π": "π", "ρ": "ρ"}


def _parse_seq(tokens):
    """tokens -> list of OMML elements, handling _ ^ sqrt( and ( ) fractions."""
    els = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok == "sqrt(":
            # find matching close: tokens marked ")sqrt"
            inner = []
            i += 1
            depth = 0
            while i < len(tokens) and (tokens[i] != ")sqrt" or depth):
                if tokens[i] == "sqrt(":
                    depth += 1
                elif tokens[i] == ")sqrt":
                    depth -= 1
                inner.append(tokens[i]); i += 1
            i += 1  # skip ")sqrt"
            rad = _m("rad")
            radPr = _m("radPr")
            degHide = _m("degHide"); degHide.set(qn("m:val"), "on")
            radPr.append(degHide); rad.append(radPr)
            deg = _m("deg"); rad.append(deg)
            e = _m("e")
            for el in _parse_seq(inner):
                e.append(el)
            rad.append(e)
            els.append(rad)
        elif tok.startswith("_"):
            # subscript: attach to previous element as sSub
            base = els.pop()
            ssub = _m("sSub")
            e = _m("e"); e.append(base); ssub.append(e)
            sub = _m("sub"); sub.append(_mrun(tok[1:])); ssub.append(sub)
            els.append(ssub)
        elif tok.startswith("^"):
            base = els.pop()
            ssup = _m("sSup")
            e = _m("e"); e.append(base); ssup.append(e)
            sup = _m("sup"); sup.append(_mrun(tok[1:])); ssup.append(sup)
            els.append(ssup)
        elif tok == "/":
            # build fraction from surrounding operand groups
            num_els = els
            den_tokens = []
            j = i + 1
            while j < len(tokens):
                den_tokens.append(tokens[j]); j += 1
            i = j
            f = _m("f")
            num = _m("num")
            for el in num_els:
                num.append(el)
            den = _m("den")
            for el in _parse_seq(den_tokens):
                den.append(el)
            f.append(num); f.append(den)
            els = [f]
        else:
            els.append(_mrun(tok))
        i += 1
    return els


def _tokenize(formula):
    """Split formula into tokens: words, greek, _sub, ^sup, sqrt( ... )."""
    tokens = []
    i = 0
    n = len(formula)
    while i < n:
        c = formula[i]
        if c == "_":
            j = i + 1
            while j < n and (formula[j].isalnum() or formula[j] in "()"):
                j += 1
            tokens.append("_" + formula[i + 1:j]); i = j
        elif c == "^":
            j = i + 1
            while j < n and formula[j].isalnum():
                j += 1
            tokens.append("^" + formula[i + 1:j]); i = j
        elif formula.startswith("√(", i):
            depth = 0
            j = i + 1
            inner = ""
            # chars from after '('
            while j < n:
                if formula[j] == "(":
                    depth += 1
                elif formula[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                inner += formula[j]; j += 1
            tokens.append("sqrt(")
            tokens.extend(_tokenize(inner))
            tokens.append(")sqrt")
            i = j + 1
        elif c == "√":
            # bare radical without parens -> treat following token-group as radicand
            tokens.append("√glyph"); i += 1
        elif c == " ":
            tokens.append(" "); i += 1
        else:
            # accumulate a word (letters/digits/operators) until _ ^ √ or space
            j = i
            buf = ""
            while j < n and formula[j] not in " _^√":
                buf += formula[j]; j += 1
            # split buf into runs of letters vs single operators for subscript attach
            tokens.extend(_split_word(buf))
            i = j
    return tokens


def _split_word(buf):
    """Split 'L_iM_i' style already handled by tokenizer; split mixed like 'DJS(p_early,p_late)'
    conservatively: emit each char-group so _ can attach to preceding element."""
    out = []
    cur = ""
    for ch in buf:
        if ch.isalnum() or ch in ".′":
            cur += ch
        else:
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
    if cur:
        out.append(cur)
    return out


def add_omml(paragraph, formula, display=False):
    if display:
        omath = _m("oMathPara")
        inner = _m("oMath")
        for el in _parse_seq(_tokenize(formula)):
            inner.append(el)
        omath.append(inner)
        paragraph._p.append(omath)
    else:
        omath = _m("oMath")
        for el in _parse_seq(_tokenize(formula)):
            omath.append(el)
        paragraph._p.append(omath)


# ---------------- registry-driven tables ----------------
TABLE1 = [
    ["study", "legacy", "outcome", "primary estimate (95% CI)", "classification"],
    [f"national agriculture (N={int(v('nat.N'))})", "crop portfolio HHI", "crop-mix JSD",
     f"{s3(v('nat.beta3'))} {ci(v('nat.beta3_ci_lo'), v('nat.beta3_ci_hi'))}, p={p3(v('nat.beta3_p'))}", "NULL"],
    [f"subnational agriculture (N={int(v('subnat.N'))})", "irrigation share 2000", "crop-mix JSD",
     f"{s3(v('subnat.beta3'))} {ci(v('subnat.beta3_ci_lo'), v('subnat.beta3_ci_hi'))}, p={p3(v('subnat.beta3_p'))}", "NULL"],
    [f"urban settlements (N={int(v('urban.N')):,})", "ln built volume 2000", "net hazard-avoidance reallocation",
     f"{s3(v('urban.beta3'),4)} {ci(v('urban.beta3_ci_lo'), v('urban.beta3_ci_hi'),4)}, p={p3(v('urban.beta3_p'))}", "WEAK / CONTEXT DEPENDENT"],
    [f"transition H1 legacy (N={int(v('trans.N')):,})", "housing-stock age", "first programme entry",
     f"{s3(v('trans.H1.coef'))} {ci(v('trans.H1.ci_lo'), v('trans.H1.ci_hi'))}, p={p3(v('trans.H1.p'))}", "DIRECTIONAL BUT UNCERTAIN"],
    [f"transition H2 capacity (N={int(v('trans.N')):,})", "prior departure obligations", "first programme entry",
     f"{s3(v('trans.H2.coef'))} {ci(v('trans.H2.ci_lo'), v('trans.H2.ci_hi'))}, p={p3(v('trans.H2.p'))}", "NULL"],
    ["transition H1 lag-1 (secondary)", "housing-stock age", "first programme entry",
     f"{s3(v('trans.sec_lag1.H1'))} {ci(v('trans.sec_lag1.H1_ci_lo'), v('trans.sec_lag1.H1_ci_hi'))}, p={p3(v('trans.sec_lag1.H1_p'))}", "SECONDARY"],
    ["transition H1 intensive (secondary)", "housing-stock age", "entry volume",
     f"{s3(v('trans.intensive.H1'))} {ci(v('trans.intensive.H1_ci_lo'), v('trans.intensive.H1_ci_hi'))}, p={p3(v('trans.intensive.H1_p'))}", "SECONDARY"],
]


def write_ed_table3():
    import csv as _csv
    rows = [
        ["study", "unit", "N", "legacy", "demand", "outcome", "estimand", "estimate", "95% CI", "p", "classification"],
        ["national agriculture", "country", str(int(v('nat.N'))), "crop portfolio HHI", "crop-calendar mismatch", "crop-mix JSD",
         "legacy x mismatch (fractional logit)", s3(v('nat.beta3')), ci(v('nat.beta3_ci_lo'), v('nat.beta3_ci_hi')), p3(v('nat.beta3_p')), "NULL"],
        ["subnational agriculture", "admin-1", str(int(v('subnat.N'))), "irrigation share 2000", "crop-calendar mismatch", "crop-mix JSD",
         "legacy x mismatch (OLS + country FE)", s3(v('subnat.beta3')), ci(v('subnat.beta3_ci_lo'), v('subnat.beta3_ci_hi')), p3(v('subnat.beta3_p')), "NULL"],
        ["urban settlements", "urban centre", f"{int(v('urban.N')):,}", "ln built volume 2000", "baseline RP10 flood share",
         "net hazard-avoidance reallocation", "legacy x exposure (OLS + country FE)", s3(v('urban.beta3'), 4),
         ci(v('urban.beta3_ci_lo'), v('urban.beta3_ci_hi'), 4), p3(v('urban.beta3_p')), "WEAK / CONTEXT DEPENDENT"],
        ["transition H1 (legacy)", "county-year", f"{int(v('trans.N')):,}", "housing-stock age", "3-yr lag flood declarations",
         "first programme entry", "demand x legacy (cloglog)", s3(v('trans.H1.coef')),
         ci(v('trans.H1.ci_lo'), v('trans.H1.ci_hi')), p3(v('trans.H1.p')), "DIRECTIONAL BUT UNCERTAIN"],
        ["transition H2 (capacity)", "county-year", f"{int(v('trans.N')):,}", "prior departure obligations", "3-yr lag flood declarations",
         "first programme entry", "demand x capacity (cloglog)", s3(v('trans.H2.coef')),
         ci(v('trans.H2.ci_lo'), v('trans.H2.ci_hi')), p3(v('trans.H2.p')), "NULL"],
        ["transition H1 lag-1 (secondary)", "county-year", f"{int(v('trans.N')):,}", "housing-stock age", "1-yr lag declarations",
         "first programme entry", "demand x legacy (cloglog)", s3(v('trans.sec_lag1.H1')),
         ci(v('trans.sec_lag1.H1_ci_lo'), v('trans.sec_lag1.H1_ci_hi')), p3(v('trans.sec_lag1.H1_p')), "SECONDARY"],
        ["transition H1 intensive (secondary)", "county-year", f"{int(v('trans.intensive.N')):,}", "housing-stock age", "1-yr lag declarations",
         "entry volume", "demand x legacy (PPML)", s3(v('trans.intensive.H1')),
         ci(v('trans.intensive.H1_ci_lo'), v('trans.intensive.H1_ci_hi')), p3(v('trans.intensive.H1_p')), "SECONDARY"]]
    with open(os.path.join(ROOT, "supplementary", "SI_Table_1.csv"), "w", newline="") as f:
        _csv.writer(f).writerows(rows)


# ---------------- docx helpers ----------------
def style_doc(doc):
    st = doc.styles["Normal"]
    st.font.name = "Times New Roman"; st.font.size = Pt(12)
    st.font.color.rgb = RGBColor(0, 0, 0)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    for h in ("Heading 1", "Heading 2", "Heading 3"):
        s = doc.styles[h]; s.font.name = "Times New Roman"; s.font.color.rgb = RGBColor(0, 0, 0)
        s.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")


def _emit(doc_p, text, size, bold, italic):
    # math markers inside a segment are split first
    for piece in re.split(r"(\{\{eq:[^}]*\}\})", text):
        if not piece:
            continue
        m = re.fullmatch(r"\{\{eq:(.*)\}\}", piece)
        if m:
            add_omml(doc_p, m.group(1), display=False)
            continue
        for seg in re.split(r"(\*\*.+?\*\*|\*.+?\*)", piece):
            if not seg:
                continue
            b, it, s = bold, italic, seg
            if s.startswith("**") and s.endswith("**") and len(s) > 4:
                b, s = True, s[2:-2]
            elif s.startswith("*") and s.endswith("*") and len(s) > 2:
                it, s = True, s[1:-1]
            r = doc_p.add_run(s)
            r.bold = b; r.italic = it
            r.font.size = Pt(size); r.font.name = "Times New Roman"
            r.font.color.rgb = RGBColor(0, 0, 0)


def add_para(doc, text, size=12, bold=False, italic=False):
    p = doc.add_paragraph()
    parts = re.split(r"(\{[0-9,–\s]+\})", text)
    for part in parts:
        m = re.fullmatch(r"\{([0-9,–\s]+)\}", part)
        if m:
            r = p.add_run("[" + m.group(1).strip() + "]")
            r.font.superscript = True
            r.font.size = Pt(size); r.font.name = "Times New Roman"
            r.font.color.rgb = RGBColor(0, 0, 0)
        else:
            _emit(p, part, size, bold, italic)
    return p


def add_caption(doc, text):
    p = add_para(doc, text, size=10)
    p.paragraph_format.space_before = Pt(14)
    return p


def add_table1(doc):
    t = doc.add_table(rows=len(TABLE1), cols=len(TABLE1[0]))
    t.style = "Table Grid"
    for i, row in enumerate(TABLE1):
        for j, val in enumerate(row):
            cell = t.cell(i, j); cell.text = ""
            r = cell.paragraphs[0].add_run(val)
            r.font.size = Pt(9); r.font.name = "Times New Roman"
            r.font.color.rgb = RGBColor(0, 0, 0)
            if i == 0:
                r.bold = True


def build(inline: bool, out: str):
    doc = Document(); style_doc(doc)
    sec = doc.sections[0]
    sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Inches(1)
    lines = open(MD, encoding="utf8").read().split("\n")
    fig_caption = {}
    for ln in lines:
        if ln.startswith("**Figure "):
            num = re.match(r"\*\*Figure (\d)", ln).group(1)
            fig_caption[num] = ln.replace("**", "").strip()
    inserted_figs = set(); ed3_done = False
    i = 0
    while i < len(lines):
        ln = lines[i]; i += 1
        if ln.startswith("## References"):
            doc.add_heading("References", level=1)
            while i < len(lines):
                rl = lines[i]; i += 1
                if rl.startswith("## "):
                    i -= 1; break
                if rl.strip():
                    add_para(doc, rl, size=10)
            continue
        if ln.startswith("## Figure legends"):
            doc.add_heading("Figure legends", level=1)
            while i < len(lines):
                rl = lines[i]; i += 1
                if rl.startswith("## Extended Data"):
                    i -= 1; break
                if rl.strip():
                    add_para(doc, rl, size=10)
            continue
        if ln.startswith("## Extended Data"):
            doc.add_heading("Extended Data", level=1)
            while i < len(lines):
                rl = lines[i]; i += 1
                if rl.startswith("## "):
                    i -= 1; break
                if rl.strip():
                    add_para(doc, rl, size=10)
            continue
        if ln.startswith("## "):
            doc.add_heading(ln[3:].strip(), level=1); continue
        if ln.startswith("### "):
            doc.add_heading(ln[4:].strip(), level=2); continue
        if ln.startswith("# "):
            doc.add_heading(ln[2:].strip(), level=0); continue
        if not ln.strip():
            continue
        if ln.startswith("**Supplementary Table 1") and not ed3_done:
            ed3_done = True
            add_para(doc, ln, size=10)
            if inline:
                add_table1(doc)
            continue
        # display equations -> standalone paragraph with oMathPara
        for m in re.finditer(r"\{\{display_eq:([^}]*)\}\}", ln):
            dp = doc.add_paragraph()
            dp.paragraph_format.space_before = Pt(4)
            dp.paragraph_format.space_after = Pt(4)
            add_omml(dp, m.group(1), display=True)
            ln = ln.replace(m.group(0), "")
        if ln.strip():
            add_para(doc, ln)
        if inline:
            for num in re.findall(r"Fig\.\s*(\d)", ln):
                if num not in inserted_figs and os.path.exists(f"{FIGDIR}/Figure_{num}.png"):
                    doc.add_picture(f"{FIGDIR}/Figure_{num}.png", width=Inches(6.3))
                    if num in fig_caption:
                        add_caption(doc, fig_caption[num])
                    inserted_figs.add(num)
    doc.save(out)
    print("saved", out, "figs:", sorted(inserted_figs))


write_ed_table3()
build(True, os.path.join(ROOT, "MAIN_MANUSCRIPT_NS_inline_LOCKED.docx"))
build(False, os.path.join(ROOT, "MAIN_MANUSCRIPT_NS_clean_LOCKED.docx"))
