"""Builds Figures 1-5 and Extended Data figures for the NS submission."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import pandas as pd, numpy as np, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD = os.path.join(ROOT, "source_data")
FIG = os.path.join(ROOT, "figures")
ED = os.path.join(ROOT, "extended_data")
os.makedirs(FIG, exist_ok=True); os.makedirs(ED, exist_ok=True)
plt.rcParams.update({"font.size": 8, "font.family": "DejaVu Sans",
                     "axes.spines.top": False, "axes.spines.right": False})
C_NULL, C_WEAK, C_UNC, C_SEC = "#4C72B0", "#DD8452", "#55A868", "#8172B3"

def forest(ax, rows, ylab):
    ys = np.arange(len(rows))[::-1]
    for (lab, est, lo, hi, col), y in zip(rows, ys):
        ax.plot([lo, hi], [y, y], color=col, lw=1.8, zorder=2)
        ax.plot([est], [y], "o", color=col, ms=5, zorder=3)
        xmin = min(lo for _, _, lo, _, _ in rows)
        ax.text(xmin, y + 0.28, lab, va="center", ha="left", fontsize=6.8)
    ax.axvline(0, color="k", lw=0.7, ls="--")
    ax.set_yticks([]); ax.set_ylabel(ylab, fontsize=8)

# ---------- Figure 1: theory + architecture ----------
fig, ax = plt.subplots(figsize=(7.0, 4.6)); ax.axis("off")
ax.text(0.5, 0.97, "Inherited-structure intuition", ha="center", fontsize=10, weight="bold")
boxes = [
    (0.05, 0.80, 0.28, "SPECIALIZATION\n(crop portfolio HHI)"),
    (0.37, 0.80, 0.28, "FIXED CAPITAL\n(irrigation, built volume)"),
    (0.68, 0.80, 0.31, "INSTITUTIONAL LEGACY\n(programme history, stock age)")]
for x, y, w, t in boxes:
    ax.add_patch(mp.FancyBboxPatch((x, y), w, 0.10, boxstyle="round,pad=0.008",
                                 fc="#EAEAF2", ec="#666"))
    ax.text(x+w/2, y+0.05, t, ha="center", va="center", fontsize=7.5)
ax.add_patch(mp.FancyBboxPatch((0.24, 0.62), 0.52, 0.10, boxstyle="round,pad=0.008",
                               fc="#F5D7C5", ec="#B35C2A"))
ax.text(0.5, 0.67, "prediction: greater legacy → attenuated transformation\nunder stronger environmental demand", ha="center", va="center", fontsize=8)
for xc in (0.19, 0.51, 0.83):
    ax.annotate("", xy=(xc if xc!=0.51 else 0.5, 0.73), xytext=(xc, 0.80),
                arrowprops=dict(arrowstyle="-", color="#666"))
tests = [
    (0.02, "T1 national agriculture\n147 countries · frac. logit\nNULL"),
    (0.27, "T2 subnational agriculture\n340 admin-1 · OLS+FE\nNULL"),
    (0.52, "T3 urban built capital\n4,598 centres · OLS+FE\nWEAK / CONTEXT"),
    (0.77, "T4 transition initiation\n3,062 counties · cloglog\nUNCERTAIN + NULL")]
for x, t in tests:
    ax.add_patch(mp.FancyBboxPatch((x, 0.36), 0.21, 0.16, boxstyle="round,pad=0.008",
                                 fc="white", ec="#444"))
    ax.text(x+0.105, 0.44, t, ha="center", va="center", fontsize=6.6)
    ax.annotate("", xy=(x+0.105, 0.54), xytext=(0.5, 0.61),
                arrowprops=dict(arrowstyle="->", color="#888", lw=0.8))
ax.add_patch(mp.FancyBboxPatch((0.13, 0.05), 0.74, 0.20, boxstyle="round,pad=0.010",
                               fc="#DCE8DA", ec="#3C6E47"))
ax.text(0.5, 0.19, "observed: no stable general rigidity pattern", ha="center", fontsize=8.5, weight="bold")
ax.text(0.5, 0.11, "continuous adjustment (T1–T3: crop mix, built reconfiguration)\nvs discrete transition (T4: first programme entry)",
        ha="center", fontsize=7, style="italic")
ax.text(0.5, 0.055, "boundary: legacy is a hypothesis about constraint, not evidence of it",
        ha="center", fontsize=7.5)
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
fig.savefig(f"{FIG}/Figure_1.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ---------- Figure 2: agricultural ----------
nat = (0.00459, -0.131, 0.143)
sub = (-0.0377, -0.2513, 0.0773)
fig, ax = plt.subplots(figsize=(5.6, 2.6))
rows = [("national specialization × mismatch\n(fractional logit, N=147)", *nat, C_NULL),
        ("subnational irrigation × mismatch\n(OLS + country FE, N=340)", *sub, C_NULL)]
forest(ax, rows, "")
ax.set_xlim(-0.45, 0.35)
ax.set_xlabel("interaction estimate (standardized scale), 95% CI")
ax.set_title("Agricultural tests: legacy × climatic-mismatch interactions", fontsize=9)
fig.savefig(f"{FIG}/Figure_2.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ---------- Figure 3: urban ----------
het = pd.read_csv(f"{SD}/urban_COASTAL_HETEROGENEITY.csv")
fig, ax = plt.subplots(figsize=(5.8, 3.0))
labels = {"coastal_le10km": "coastal ≤10 km (N=782)",
          "coastal_le25km": "coastal ≤25 km (N=1,077)",
          "coastal_le50km": "coastal ≤50 km (N=1,417)",
          "inland_gt50km": "inland >50 km (N=3,181)",
          "full": "full sample (N=4,598)"}
order = ["full", "coastal_le10km", "coastal_le25km", "coastal_le50km", "inland_gt50km"]
ys = np.arange(len(order))[::-1]
for lab, y in zip(order, ys):
    row = het[het.subgroup == lab].iloc[0]
    col = C_WEAK if lab == "inland_gt50km" else (C_NULL if lab == "full" else "#999")
    ax.plot(row.b3, y, "o", color=col, ms=6)
    if lab == "full":
        ax.text(row.b3, y - 0.32, f"{row.b3:+.4f}", va="center", ha="center", fontsize=7)
    elif row.b3 > -0.006:
        ax.text(row.b3 - 0.0012, y, f"{row.b3:+.4f}", va="center", ha="right", fontsize=7)
    else:
        ax.text(row.b3 + 0.0012, y, f"{row.b3:+.4f}", va="center", fontsize=7)
    ax.text(-0.0335, y, labels[lab], va="center", fontsize=7.5)
ax.plot([-0.0166, -0.0033], [ys[0], ys[0]], color=C_NULL, lw=2)
ax.axvline(0, color="k", lw=0.7, ls="--"); ax.set_yticks([])
ax.set_xlim(-0.034, 0.012)
ax.set_xlabel("legacy × baseline flood-exposure interaction (β3)")
ax.set_title("Urban built capital: small, inland-concentrated conditioning", fontsize=9)
fig.savefig(f"{FIG}/Figure_3.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ---------- Figure 4: transition ----------
fig, axes = plt.subplots(1, 3, figsize=(8.2, 2.9), gridspec_kw={"width_ratios": [1.15, 1.15, 1.3]})
prim = [("H1 demand × legacy", -0.1923, -0.4537, 0.0692, C_UNC),
        ("H2 demand × capacity", 0.0342, -0.0975, 0.1660, C_NULL)]
forest(axes[0], prim, "PRIMARY (first-entry hazard)")
axes[0].set_xlim(-0.6, 0.35); axes[0].set_xlabel("cloglog coefficient, 95% CI")
axes[0].set_title("a  Primary interactions", fontsize=9, loc="left")
sec = [("lag-1 demand, extensive H1", -0.380, -0.678, -0.082, C_SEC),
       ("intensive-margin H1 (volume)", -0.548, -0.910, -0.187, C_SEC)]
forest(axes[1], sec, "SECONDARY (non-confirmatory)")
axes[1].set_xlim(-1.05, 0.25); axes[1].set_xlabel("coefficient, 95% CI")
axes[1].set_title("c  Secondary estimates", fontsize=9, loc="left")
ax = axes[2]; ax.axis("off")
txt = ("Classification\n\n"
       "H1: DIRECTIONAL BUT\nUNCERTAIN (p=0.149)\n\n"
       "H2: NOT SUPPORTED\n(p=0.610)\n\n"
       "secondary signals strengthen\nthe hypothesis, not the finding\n"
       "— independent confirmation\nrequired")
ax.text(0.02, 0.95, txt, va="top", fontsize=8, family="DejaVu Sans")
ax.set_title("d  Primary vs secondary", fontsize=9, loc="left")
fig.tight_layout()
fig.savefig(f"{FIG}/Figure_4.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ---------- Figure 5: synthesis (primary evidence only) ----------
fig, (axL, axF, axR) = plt.subplots(
    1, 3, figsize=(8.8, 3.7), gridspec_kw={"width_ratios": [2.9, 4.0, 1.55], "wspace": 0.05})
rows = [
    ("T1  national agriculture",      "portfolio HHI → crop-mix JSD",            +0.0046, -0.131, +0.143, "NULL",       C_NULL),
    ("T2  subnational agriculture",   "irrigation share → crop-mix JSD",          -0.0377, -0.2513,+0.0773,"NULL",       C_NULL),
    ("T3  urban built capital",       "built volume 2000 → hazard-avoidance",     -0.008275,-0.0166,-0.0033,"WEAK /\nCONTEXT", C_WEAK),
    ("T4  transition H1 (legacy)",    "housing-stock age → first entry",          -0.1923, -0.4537,+0.0692,"UNCERTAIN",  C_UNC),
    ("T4  transition H2 (capacity)",  "prior departures → first entry",           +0.0342, -0.0975,+0.1660,"NULL",       C_NULL)]
ys = list(range(len(rows)-1, -1, -1))
axL.axis("off"); axL.set_xlim(0, 1); axL.set_ylim(-0.7, len(rows)-0.1)
axR.axis("off"); axR.set_xlim(0, 1); axR.set_ylim(-0.7, len(rows)-0.1)
for (name, detail, est, lo, hi, cls, col), y in zip(rows, ys):
    axL.text(0.0, y+0.10, name, fontsize=9, weight="bold", va="center")
    axL.text(0.0, y-0.22, detail, fontsize=8, color="#444", va="center")
    axF.plot([lo, hi], [y, y], color=col, lw=2.2, solid_capstyle="butt")
    axF.scatter([est], [y], color=col, s=42, zorder=3)
    axF.text(hi+0.02 if hi+0.02 < 0.34 else lo-0.02, y,
             f"{est:+.3f}", fontsize=8, va="center",
             ha="left" if hi+0.02 < 0.34 else "right", color="#222")
    axR.text(0.0, y-0.06, cls, fontsize=8.5, weight="bold", color=col, va="center")
axF.axvline(0, color="#999", lw=0.8, ls="--")
axF.set_xlim(-0.62, 0.42); axF.set_ylim(-0.7, len(rows)-0.1)
axF.set_yticks([]); axF.set_xlabel("interaction coefficient (95% CI)", fontsize=9)
for s in ["top","right","left"]: axF.spines[s].set_visible(False)
axR.text(0.0, len(rows)-0.35, "classification", fontsize=8.5, weight="bold", color="#333")
axF.text(0.0, -0.26,
         "Primary estimates only; secondary transition estimates are reported separately (Fig. 4).\n"
         "Estimands are deliberately not comparable: no pooled meta-analytic effect is reported.",
         fontsize=7.2, style="italic", va="top", transform=axF.transAxes)
fig.savefig(f"{FIG}/Figure_5.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ---------- Extended Data figures ----------
# ED Fig 2: national robustness
rl = pd.read_csv(f"{SD}/nat_robustness_specification_ledger.csv")
fig, ax = plt.subplots(figsize=(6.4, 3.4))
rows = [("PRIMARY (subregion bootstrap)", *nat, C_NULL)] + \
       [(r.spec, r.beta3, r.ci_lo, r.ci_hi, "#888") for r in rl.itertuples()]
forest(ax, rows, "")
ax.set_xlim(-0.6, 0.6); ax.set_xlabel("β3 estimate, 95% CI")
ax.set_title("ED Fig. 2 — National agricultural robustness", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_2.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 3: subnational robustness
sl = pd.read_csv(f"{SD}/subnat_ROBUSTNESS_LEDGER.csv")
fig, ax = plt.subplots(figsize=(6.6, 3.8))
keep = sl[sl.interaction_estimate.notna() & sl.CI_low.notna()]
rows = [(r.analysis_id, r.interaction_estimate, r.CI_low, r.CI_high,
         C_NULL if r.interaction_estimate < 0 else "#999") for r in keep.itertuples()]
forest(ax, rows, "")
ax.set_xlim(-0.8, 0.9); ax.set_xlabel("β3 estimate, 95% CI")
ax.set_title("ED Fig. 3 — Subnational agricultural robustness", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_3.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 4: urban robustness
ul = pd.read_csv(f"{SD}/urban_ROBUSTNESS_LEDGER.csv")
keep = ul[ul.interaction_est.notna() & ul.ci_low.notna()].head(14)
fig, ax = plt.subplots(figsize=(6.8, 4.6))
rows = [(r.analysis_id, r.interaction_est, r.ci_low, r.ci_high,
         C_WEAK if r.interaction_est < 0 else "#999") for r in keep.itertuples()]
forest(ax, rows, "")
ax.set_xlim(-0.45, 0.75); ax.set_xlabel("interaction estimate, 95% CI")
ax.set_title("ED Fig. 4 — Urban robustness and prespecified heterogeneity", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_4.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 5: urban negative controls
nc = pd.read_csv(f"{SD}/urban_NEGATIVE_CONTROL_LEDGER.csv")
fig, ax = plt.subplots(figsize=(6.4, 3.2))
vals = [("primary", -0.008275), ("low-hazard matched control", 0.000838),
        ("future-exposure placebo", -0.00807), ("top10 BUV excl.", -0.0104),
        ("port<25km excl.", -0.0118), ("capitals excl.", -0.0081)]
ys = np.arange(len(vals))[::-1]
for (lab, est), y in zip(vals, ys):
    ax.plot(est, y, "o", color="#4C72B0" if lab == "primary" else "#999", ms=6)
    ax.text(est + 0.0005, y, f"{est:+.4f}", va="center", fontsize=7)
    ax.text(-0.0155, y, lab, va="center", fontsize=7.5)
ax.axvline(0, color="k", lw=0.7, ls="--"); ax.set_yticks([])
ax.set_xlim(-0.016, 0.004); ax.set_xlabel("β3 / control estimate")
ax.set_title("ED Fig. 5 — Urban negative controls and exclusions", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_5.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 6: transition risk-set construction
fig, ax = plt.subplots(figsize=(5.8, 3.0)); ax.axis("off")
steps = [("3,062 counties at risk\n(2000, flood-eligible)", 0.88),
         ("51,686 county-years\nrisk set, 2000–2020", 0.64),
         ("1,021 first events\n(≤1 per county)", 0.40),
         ("2,041 never-transition\nretained at risk", 0.16)]
for t, y in steps:
    ax.add_patch(mp.FancyBboxPatch((0.12, y - 0.07), 0.76, 0.13,
                                   boxstyle="round,pad=0.008", fc="#EAEAF2", ec="#555"))
    ax.text(0.5, y, t, ha="center", va="center", fontsize=8)
for y1, y2 in [(0.80, 0.72), (0.56, 0.48), (0.32, 0.24)]:
    ax.annotate("", xy=(0.5, y2), xytext=(0.5, y1), arrowprops=dict(arrowstyle="->", color="#777"))
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_title("ED Fig. 6 — Transition risk-set construction", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_6.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 7: transition robustness
tr = pd.read_csv(f"{SD}/trans_ROBUSTNESS_LEDGER.csv")
keep = tr[tr.H1.notna() & tr.H1_ci.notna()]
fig, ax = plt.subplots(figsize=(6.6, 4.0))
import ast
rows = [(r.variant, r.H1, ast.literal_eval(r.H1_ci)[0], ast.literal_eval(r.H1_ci)[1],
         C_UNC if r.H1 < 0 else "#999") for r in keep.itertuples()]
forest(ax, rows, "")
ax.set_xlim(-0.75, 0.45); ax.set_xlabel("H1 (demand × legacy) estimate, 95% CI")
ax.set_title("ED Fig. 7 — Transition robustness (H1 across variants)", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_7.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 8: simulation calibration
sim = pd.read_csv(f"{SD}/trans_information_simulation_v4.csv")
null = sim[(sim.true_effect == 0) & (sim.inference == "fips")]
fig, ax = plt.subplots(figsize=(5.4, 2.6))
labs = null.hypothesis + " county CRV1"
ax.bar(labs, null["reject"], color=[C_UNC, C_NULL], width=0.45)
ax.axhline(0.07, color="orange", ls="--", lw=1); ax.axhline(0.10, color="red", ls="--", lw=1)
ax.axhline(0.03, color="green", ls="--", lw=1)
ax.set_ylabel("null rejection rate")
for i, v in enumerate(null["reject"]):
    ax.text(i, v + 0.003, f"{v:.3f}", ha="center", fontsize=8)
ax.set_ylim(0, 0.12)
ax.set_title("ED Fig. 8 — Inference calibration on null draws", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_8.png", dpi=300, bbox_inches="tight"); plt.close(fig)

# ED Fig 1: lock chronology
fig, ax = plt.subplots(figsize=(6.6, 3.2))
events = [("feasibility + design freeze", 0, "#999"),
          ("LOCK V2 → V3 estimand split", 1, "#999"),
          ("V4 capacity repair + lock", 2, "#999"),
          ("info simulation gate", 3, "#999"),
          ("SINGLE opening (immutable)", 4, "#B35C2A"),
          ("robustness + classification", 5, "#3C6E47")]
ax.plot([0, 5], [0, 0], color="#BBB", lw=1.5)
for lab, x, c in events:
    ax.plot(x, 0, "o", color=c, ms=8)
    ax.text(x, 0.07 if x % 2 == 0 else -0.10, lab, ha="center", fontsize=6.6,
            va="bottom" if x % 2 == 0 else "top", rotation=0)
ax.set_ylim(-0.35, 0.45); ax.set_yticks([])
ax.set_xticks(range(6)); ax.set_xticklabels([f"step {i+1}" for i in range(6)], fontsize=7)
ax.set_title("ED Fig. 1 — Lock chronology (transition branch; same pattern per branch)", fontsize=9)
fig.savefig(f"{ED}/ED_Fig_1.png", dpi=300, bbox_inches="tight"); plt.close(fig)

print("figures done")
