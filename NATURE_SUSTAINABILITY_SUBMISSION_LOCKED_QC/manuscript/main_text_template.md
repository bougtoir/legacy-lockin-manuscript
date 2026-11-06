# When does inherited structure become adaptation lock-in?

**Onishi Tatsuki**
Data Science and AI Innovation Research Promotion Center, Shiga University, Hikone, Shiga, Japan

## Abstract

Climate adaptation unfolds within inherited systems — crop portfolios, irrigation networks, built environments and institutions — widely treated as potential sources of lock-in. Whether inherited structure itself generates rigidity is rarely tested falsifiably across distinct systems. We subjected this intuition to four tests in which each primary design was frozen, outcome-blind, before its headline estimate was computed: national crop specialization, subnational irrigation dependence, urban built capital under flood exposure, and institutionalized departure of flood-prone settlements. Neither agricultural test provided confirmatory evidence of legacy-associated rigidity under climatic mismatch. Built capital produced a small, context-dependent negative interaction concentrated inland. At transition margins the legacy interaction was negative but uncertain, and prior programme capacity did not amplify transition initiation. Inherited specialization, capital and institutional legacy were insufficient to produce a stable general rigidity pattern. Legacy should be treated as a hypothesis about constraint, not evidence of constraint.

## Introduction

Climate adaptation and sustainability transitions do not begin from a blank slate. Food production runs on inherited crop portfolios and irrigation works; cities are fixed quantities of buildings and networks laid down under past conditions; institutions accumulate programmes, rules and capabilities that channel every subsequent response. These inherited systems are assets: they embody accumulated knowledge, embodied capital and network value that make incremental adaptation cheaper and more reliable{1,2}. The economics of increasing returns formalized why: once a technology, crop or urban form is adopted, learning effects, coordination benefits and adaptive expectations raise the cost of every alternative{3,4}.

The same inheritances are frequently described in the adaptation and transitions literatures as sources of rigidity — path dependence{3–6}, infrastructure and carbon lock-in{1,2}, adaptation lock-in, stranded assets{7–9}. Underlying these labels is an influential intuition: that accumulated specialization and fixed capital themselves generate resistance to transformation{10–15}. The claim is consequential. If inherited structure is the binding constraint on adaptation, then transformation may appear to require structural replacement rather than adjustment, and incremental adaptation policy may look futile in legacy-heavy systems. Yet persistence and constraint are not logically identical. A system can persist because alternatives are inferior, because change is not yet demanded, or because substitution is genuinely blocked; only the last of these is lock-in, and observing accumulated structure does not distinguish among them. Persistence is often discussed through the language of path dependence and lock-in, although persistence alone does not identify the mechanism that constrains alternatives.

This distinction yields a falsifiable prediction. If accumulated legacy is itself a general source of adaptation rigidity, then systems carrying greater pre-existing specialization, fixed capital or institutional commitment should show systematically attenuated transformation when environmental demand for change intensifies{16,17}. The prediction is cross-domain: it should hold in agricultural portfolios, in urban spatial structure and in discrete institutional transitions alike. It is also sequential in strength. If the interaction fails under the weakest conditions — continuous, marginal reallocation — there is little reason to expect it at harder margins; if it appears only at the hardest margin — initiation of transformational departure — the boundary itself is informative.

We tested it sequentially in four locked empirical designs (Fig. 1). The first examines whether national crop specialization conditioned long-run crop-mix transformation under growing climatic mismatch across {{nat.N}} countries{18–21}. The second asks the same question at the scale where adaptation is implemented — {{subnat.N}} first-level administrative units in {{subnat.countries}} countries — replacing specialization with baseline irrigation dependence, a physically fixed form of agricultural capital{22,23}. The third turns to the most capital-intensive human system: whether pre-existing built volume conditioned spatial reconfiguration of {{urban.N|,}} urban centres across baseline riverine flood-exposure gradients between 2000 and 2020{24–26}. The fourth addresses the discrete, transformational margin: whether the age of county housing stock and prior programme experience conditioned the initiation of FEMA-supported transformational-departure (property acquisition and relocation) programmes in US counties after flood disasters between 2000 and 2020{27–29}. For each branch, the primary sample, exposures, outcome, estimator and inference procedure were frozen before the corresponding headline outcome was estimated; each primary test was executed exactly once, and null and uncertain results were preserved rather than explored into alternatives{30,31} (Extended Data Fig. 1, Extended Data Table 1). This design converts a familiar rhetorical claim into a set of separate, examinable tests whose failures are as informative as its successes, and it removes the researcher's largest degree of freedom — the freedom to keep searching until the hypothesis is confirmed.

The expected general rigidity pattern did not emerge. The two agricultural tests yield estimates centred on zero, with no evidence of conditioning; the urban test yields a small, context-dependent interaction; the transition test yields a directional but uncertain barrier and an unsupported enablement mechanism. What the programme produces instead is an empirical boundary: accumulated legacy alone is insufficient evidence of adaptation lock-in. Constraint, where it exists, must be demonstrated against measurable barriers — substitution costs, network dependence, coordination thresholds, institutional exit — rather than inferred from the depth of accumulated structure.

## Results

### Specialization and fixed capital do not produce detectable agricultural rigidity

We first tested whether national crop specialization conditions crop-system transformation under climatic mismatch. Legacy was measured as the Herfindahl concentration of the production portfolio in 1981–2001; environmental demand as a crop-calendar mismatch index — the Mahalanobis displacement of each country's dominant crop's agro-climatic window between 1984–2001 and 2002–2020; transformation as the Jensen–Shannon divergence (JSD) between early and late crop-mix distributions{32–36}. In the frozen fractional-logit specification on {{nat.N}} countries, the specialization-by-mismatch interaction was {{eq:β3}} = {{nat.beta3|+.3f}} (95% CI [{{nat.beta3_ci_lo|+.3f}}, {{nat.beta3_ci_hi|+.3f}}], M49-subregion cluster bootstrap, B = {{nat.boot_B}}; Fig. 2). The interval is centred almost exactly on zero and provides no evidence of conditioning in either direction (Extended Data Fig. 2).

We then repeated the test at first-level administrative units, where irrigation infrastructure — a physically sunk capital stock — replaces portfolio concentration as the legacy construct. On the locked sample of {{subnat.N}} admin-1 units in {{subnat.countries}} countries, the irrigation-by-mismatch interaction was {{eq:β3}} = {{subnat.beta3|+.3f}} (95% CI [{{subnat.beta3_ci_lo|+.3f}}, {{subnat.beta3_ci_hi|+.3f}}], 10-degree geographic-block bootstrap, B = {{subnat.boot_B}}, p = {{subnat.beta3_p|.3f}}; Fig. 2). {{subnat.n_robustness_variants}} prespecified robustness variants and a falsification suite were consistent with the null (Extended Data Fig. 3); a positive falsification at pre-treatment exposure (conditional result) is retained in the record as a caution against strong causal reading of any small residual association. The agricultural branches were then permanently closed: both nulls are prospectively locked and were not reopened.

### Built capital weakly conditions urban reconfiguration

The third test moved to built capital — the longest-lived and most network-entangled form of inherited structure — using the Global Human Settlement Layer Urban Centre Database, which fixes settlement footprints and reports epoch-specific built volume, population and modelled riverine flood exposure for {{urban.total_centres_ucdb|,}} urban centres{37,38}. On the locked sample of {{urban.N|,}} urban centres in {{urban.countries}} countries observed in 2000 and 2020, we regressed a net hazard-avoidance reallocation index on standardized log built volume in 2000 (legacy), the baseline ten-year-return-period flood-exposed share (exposure), their interaction and controls, with country fixed effects. The legacy-by-exposure interaction was {{eq:β3}} = {{urban.beta3|+.4f}} (95% CI [{{urban.beta3_ci_lo|+.4f}}, {{urban.beta3_ci_hi|+.4f}}], 1,000-km geographic-block bootstrap, B = {{nat.boot_B}}, p = {{urban.beta3_p|.3f}}), equivalent to an original-scale marginal contrast of {{urban.delta_me|+.3f}} on the reallocation index — approximately {{urban.delta_me_frac_sd|pct1}} of its standard deviation (Fig. 3).

The primary estimate was negative and precise, but small and strongly context-dependent. It is concentrated in inland settlements (inland >50 km: {{eq:β3}} ≈ {{urban.het_inland.b3|+.3f}}) while coastal-proximity strata are near zero (≤10 km: ≈ {{urban.het_coastal10.b3|+.4f}}). A longer-return-period (RP100) hazard definition reverses the sign; per-capita and per-area capital intensity attenuate it; nonlinear strata show the legacy effect strongest at low, not high, hazard; and the sea-level-rise subset ({{urban.slr.N}} urban centres with altimetry coverage) does not reproduce the pattern (Extended Data Figs. 4 and 5). We therefore classify this branch as weak and context-dependent conditioning, not general urban lock-in.

### Legacy signals strengthen near transformational margins but remain uncertain

The fourth test isolated the discrete margin where lock-in claims bite hardest: initiation of transformational-departure programmes — FEMA-funded property acquisition and relocation{39,40} — rather than continuous adjustment. The outcome is the first observed FEMA-supported transformational-departure programme entry in a county, measured in programme fiscal years; the risk set keeps all {{trans.counties|,}} at-risk counties, including {{trans.never_transition|,}} that never transition, contributing {{trans.N|,}} county-years and {{trans.events|,}} first events during 2000–2020 (Extended Data Fig. 6). Demand is the strictly lagged three-year burden of unique county-level major flood declarations; legacy is the median construction year of the 2000 housing stock; capacity — measured after an audit re-scoped it to departure-type projects only — is cumulative prior obligations on acquisition and relocation projects. The frozen estimator is a discrete-time complementary log–log first-entry hazard with year baseline hazards, state effects and county-clustered inference.

Flood demand strongly predicts first programme entry (main effect {{trans.demand.coef|+.2f}}, {{trans.demand.p|sci}}). The primary legacy interaction, however, is directional but uncertain: {{eq:β}} = {{trans.H1.coef|+.3f}} (95% CI [{{trans.H1.ci_lo|+.3f}}, {{trans.H1.ci_hi|+.3f}}], p = {{trans.H1.p|.3f}}; Fig. 4a) — consistent with a legacy barrier but not distinguishable from zero, and the interval is wide enough to contain substantively large barriers. The capacity interaction is unsupported: {{eq:β}} = {{trans.H2.coef|+.3f}} (95% CI [{{trans.H2.ci_lo|+.3f}}, {{trans.H2.ci_hi|+.3f}}], p = {{trans.H2.p|.3f}}; Fig. 4b). Prior departure-programme experience predicts higher baseline programme activity but does not amplify the demand-triggered transition initiation it was theorized to enable.

Prespecified secondary analyses are consistent with — but cannot confirm — the primary reading. In the lag-1 demand window the extensive-margin interaction strengthened to {{eq:β}} = {{trans.sec_lag1.H1|+.3f}} (p = {{trans.sec_lag1.H1_p|.3f}}), and on the secondary intensive margin (entry volumes, PPML with county and year fixed effects) the legacy interaction was {{eq:β}} = {{trans.intensive.H1|+.3f}} (95% CI [{{trans.intensive.H1_ci_lo|+.3f}}, {{trans.intensive.H1_ci_hi|+.3f}}], p = {{trans.intensive.H1_p|.3f}}; Fig. 4c, Extended Data Table 2). Because the primary estimand remains uncertain, these strengthen the hypothesis rather than the finding: the strongest remaining legacy signature appeared at transformational-departure margins, but it did not meet the confirmatory threshold for transition initiation.

### Legacy effects do not generalize across adaptation systems

Read together, the four frozen tests trace a coherent boundary rather than a coherent law (Fig. 5, Supplementary Table 1). The two agricultural tests provided no stable evidence that legacy conditioned transformation. The one system where a primary interaction reached precision — urban built capital — produced an original-scale contrast of approximately {{urban.delta_me|+.3f}} — about {{urban.delta_me_frac_sd|pct1}} of the outcome standard deviation — that was not stable across prespecified alternative hazard and capital definitions. At the institutional transition margin the legacy direction is systematically negative — a negative H1 estimate retained across all prespecified numeric variants (Extended Data Fig. 7) — but the confirmatory first-entry estimate remained uncertain, and the capacity-enablement leg of the mechanism failed outright. Across domains, accumulated specialization, capital and institutional experience predict where adaptation activity occurs (large main effects of demand and prior capacity) far better than whether inherited structure blocks it.

## Discussion

Accumulated legacy did not operate as a general predictor of adaptation rigidity. Across national and subnational agriculture, urban built capital and institutionalized transformational departure, the interaction between inherited structure and environmental demand was either absent, small and context-dependent, or directional but uncertain. The umbrella intuition — legacy implies lock-in — did not survive four outcome-blind locked tests.

This negative generalization result matters because lock-in terminology is doing double work in adaptation science. It conflates the observation that systems persist with the demonstration that alternatives are foreclosed{3,6,41,42}. Our tests operationalize the second, stronger claim and find it unsupported as a blanket proposition. The contribution is not that inherited systems are adaptable — we did not measure realized welfare, livelihood continuity or ecological outcomes — but that inherited structure alone is not evidence that they are not. This is a stronger statement than the familiar complaint that lock-in is 'overused'. It says that at the scales and on the margins we tested, the observable implication of general lock-in — an attenuation of transformation that grows with both legacy and demand — is not where the data sit.

The agricultural nulls are the clearest boundary. If specialization and sunk irrigation capital do not measurably condition crop-system transformation under growing climatic mismatch at either the national or first-administrative scale, then portfolio and infrastructure legacy cannot be invoked as stand-alone explanations for agricultural rigidity; where rigidity appears, something else must carry it — market access, coordination, price incentives, land tenure or substitution opportunities our legacy measures do not capture. This is consistent with evidence that crop switching and comparative-advantage reallocation remain substantial{35,36} and that measured adaptation shortfalls concentrate in output outcomes rather than in the transformation margin itself{34}.

Urban built capital is the branch that comes closest to the hypothesized pattern: the primary estimate is negative and precise. Its weakness is as informative as its existence. An interaction of roughly {{urban.delta_me_frac_sd|pct1}} of the outcome's standard deviation, concentrated inland, reversing at longer hazard return periods and not reproducing under the sea-level-rise subset is conditioning at the margin, not lock-in. For strong claims of wholesale stranding of coastal cities{43} the test provides no support; for the more modest claim that older, denser built stock modestly dampens hazard-avoidant reconfiguration, it provides qualified support.

The transition study holds the programme's most interesting residue. The primary evidence for a legacy barrier to initiating departure programmes is directional but uncertain; the secondary, pre-specified signatures — stronger at shorter demand lags and on the transition-intensity margin — point the same way. That gradient is consistent with a real barrier that binds at transition depth rather than at initiation, and it is a concrete, falsifiable target for a powered independent study with a pre-specified transition-intensity estimand. Equally informative is the failure of enablement: counties' accumulated FEMA departure-programme experience did not condition their demand-triggered transitions, so prior institutional practice cannot be assumed to unlock transformation either.

We propose — without claiming to have demonstrated — the boundary conditions these results suggest. Legacy becomes lock-in only where at least one measurable constraint binds: low substitutability between current and transformed configurations; network dependence that makes piecemeal change non-viable; coordination thresholds that no actor can cross alone; absent exit mechanisms; or institutional barriers that block rather than merely channel transition. Each is observable and distinguishable from accumulated capital per se, and each is a better target for policy diagnosis than investment history. A research agenda follows directly: measure substitutability and switching costs where transformation is demanded; test the transition-depth margin the secondary signatures point to; and treat each candidate constraint as a separate estimand rather than a synonym for lock-in. This also separates two objects the literature often merges: persistence of system form and persistence of system function. Reconfiguration may preserve function while abandoning form; our urban and transition outcomes measured movement of the form margin, and functional sustainability remains unmeasured. A system may abandon form extensively while preserving function — a city that relocates its flood-exposed fringe is still a city — so rigidity of form does not entail loss of function, and flexibility of form does not guarantee it.

The policy implication is narrow. Adaptation assessment should measure actual transition constraints — availability of substitutes, switching costs, network dependence, institutional exit mechanisms, transition-support capacity and whether function can be preserved through reconfiguration — rather than inferring them from the depth of past investment. Where policies assume structural replacement is necessary because inherited systems cannot adapt, our tests show the premise has not been demonstrated: diagnosis of actual transition constraints should come first.

Several limitations bound the claim. The four domains are heterogeneous and deliberately so; there is no common causal estimand, and we report no pooled effect. Identification is observational: frozen designs prevent specification fishing but cannot eliminate confounding. Outcome-blind locking is not external preregistration. The urban exposure is baseline modelled riverine flood exposure, not observed worsening hazard. The transition study is US-specific and institutionally mediated through FEMA programmes; its capacity measure is programme experience, not general social capacity; and no household destination or arrival outcome exists in this record. The transition-intensity signal is secondary and awaits confirmatory design. Finally, our tests measure whether transformation happens, not whether it is timely, just or sufficient — systems may transform and still adapt badly.

Legacy should be treated as a hypothesis about constraint, not evidence of constraint.

## Methods

### Study architecture

The programme tested one falsifiable prediction in four sequential branches: systems with greater inherited specialization, fixed capital or institutional commitment should show attenuated transformation under stronger environmental demand. For each branch the primary sample, exposures, outcome, estimator and inference procedure were frozen in a versioned analysis lock (YAML + SHA-256) before the headline outcome was estimated; the headline model was executed exactly once and its output recorded immutably with checksums. Outcome-blind simulations on the frozen design matrix calibrated inference before each opening. No primary estimate was refit to strengthen results; locked agricultural nulls were not reopened.

### National agriculture

Countries were the unit (N = {{nat.N}} with sufficient data). Legacy: Herfindahl index of the 1981–2001 production portfolio (FAOSTAT{44}/SPAM2000{45} basis). Demand: dominant-crop crop-calendar mismatch, a Mahalanobis displacement between the crop's 1984–2001 and 2002–2020 agro-climatic windows (MIRCA2000{46} crop calendar; ERA5{47}-derived fields). Outcome: the Jensen–Shannon divergence between early (1981–2001) and late (2002–2020) crop-mix distributions, scaled by {{eq:√(ln 2)}}:

{{display_eq:JSD = DJS(p_early, p_late) / √(ln 2)}}

Estimator: fractional logit with standardized predictors,{{display_eq:JSD_i = β0 + β1 L_i + β2 M_i + β3 L_i M_i + ε_i}}

where L is portfolio concentration and M the crop-calendar mismatch. Inference: M49-subregion cluster bootstrap, B = {{nat.boot_B}}, two-sided percentile 95% CI — selected after spatial-inference simulation rejected five-cluster CRVE (anti-conservative). Primary estimate: {{eq:β3}} = {{nat.beta3|+.4f}} [{{nat.beta3_ci_lo|+.3f}}, {{nat.beta3_ci_hi|+.3f}}], p = {{nat.beta3_p|.3f}}.

### Subnational agriculture

First-level administrative units (N = {{subnat.N}} units, {{subnat.countries}} countries, {{subnat.regions}} regions after strict first-order-division audit). Legacy: baseline irrigation dependence, zonal irrigated harvest-area share from SPAM2000 (~2000, pre-transition). Demand: unit-level crop-calendar mismatch on each unit's observed agricultural window. Outcome: JSD of crop-mix between early and late vintages (median gap {{subnat.median_gap_years|.0f}} years). Estimator: OLS with country fixed effects,{{display_eq:JSD_u = β0 + β1 I_u + β2 M_u + β3 I_u M_u + α_c(u) + ε_u}}

where I is baseline irrigation share and α_c country fixed effects. Inference: 10-degree geographic-block bootstrap, B = {{subnat.boot_B}} (calibrated by bounded-outcome simulation; country-cluster CRVE rejected as anti-conservative). Primary estimate: {{eq:β3}} = {{subnat.beta3|+.4f}} [{{subnat.beta3_ci_lo|+.4f}}, {{subnat.beta3_ci_hi|+.4f}}], p = {{subnat.beta3_p|.3f}}.

### Flood-exposed urban settlements

Urban centres from the GHS Urban Centre Database R2024A (N = {{urban.N|,}} centres in {{urban.countries}} countries present in 2000 and 2020). Legacy: standardized log built-up volume in 2000. Exposure: baseline share of centre area exposed to modelled riverine flooding at ten-year return period (CEMS-GloFAS global river flood hazard maps{48} as integrated in GHS-UCDB). Outcome: net hazard-avoidance reallocation index 2000→2020 (net shift of built volume out of exposed zones; not a gross-addition share). Estimator: OLS with country fixed effects and controls (log population, elevation, port distance, within-50 km urban-centre cover),{{display_eq:R_c = β0 + β1 B_c + β2 F_c + β3 B_c F_c + γ′X_c + α_c + ε_c}}

where B is standardized log built volume, F the baseline RP10 flood-exposed share and R the net hazard-avoidance reallocation index. Inference: 1,000-km Mollweide block bootstrap, B = {{nat.boot_B}}. Primary estimate: {{eq:β3}} = {{urban.beta3|+.6f}} [{{urban.beta3_ci_lo|+.4f}}, {{urban.beta3_ci_hi|+.4f}}], p = {{urban.beta3_p|.3f}}; original-scale marginal contrast {{eq:ΔME}} = {{urban.delta_me|+.4f}} [{{urban.delta_me_ci_lo|+.4f}}, {{urban.delta_me_ci_hi|+.4f}}]. Prespecified heterogeneity by coastal proximity, return period, capital-intensity scaling, hazard stratum and sea-level-rise subset.

### Settlement-transition initiation

US counties ({{trans.counties|,}} at risk; {{trans.N|,}} county-years 2000–2020; {{trans.events|,}} first events; {{trans.never_transition|,}} never-transition counties retained). Outcome: first observed FEMA-supported transformational-departure programme entry (programme fiscal year). Demand: strictly lagged three-year burden of unique county-level major flood disaster declarations (OpenFEMA DisasterDeclarationsSummaries). Legacy: standardized negative median construction year of the 2000 housing stock (Census 2000 SF3 H035). Capacity: strictly lagged cumulative obligations on departure-type HMA projects only (200.x acquisition excluding vacant land, 201.x relocation; OpenFEMA HMA Projects, component-level action-type audit). Estimator: discrete-time complementary log–log hazard with year dummies, state fixed effects, log housing units and Mundlak county means,{{display_eq:cloglog(h_ct) = α_t + β1 D_ct + β2 L_c + β3 D_ct L_c + β4 D_ct C_c + γ′X_ct + μ_s(c)}}

where D is the lagged flood-declaration burden, L housing-stock age (legacy) and C prior departure-programme capacity. Inference: county-cluster CRV1 selected by null-simulation calibration (type-I {{trans.sim.typeI_fips|pct1}}, warning band; state clustering exceeded 0.10; Extended Data Fig. 8). Primary estimates: H1 demand×legacy {{trans.H1.coef|+.4f}} [{{trans.H1.ci_lo|+.4f}}, {{trans.H1.ci_hi|+.4f}}], p = {{trans.H1.p|.3f}}; H2 demand×capacity {{trans.H2.coef|+.4f}} [{{trans.H2.ci_lo|+.4f}}, {{trans.H2.ci_hi|+.4f}}], p = {{trans.H2.p|.3f}}. Secondary intensive margin: PPML, county and year fixed effects, offset log housing units (N = {{trans.intensive.N|,}} county-years).

### Statistical reporting and robustness

All primary results are reported with effect estimates, 95% CIs and p-values. Prespecified robustness suites (9–11 variants per branch), falsification tests, leave-one-unit-out grids and information/power simulations are reported in full in the reproducibility bundle and Extended Data (Figs. 1–8, Tables 1–2). No pooled meta-analytic effect is reported because estimands are not comparable.

### Reproducibility

Every lock file, frozen sample, checksum, simulation and script is in the reproducibility bundle (REPRODUCIBILITY_BUNDLE_NS_FINAL.zip) and the public repository listed in Data and Code Availability. Primary-opening JSON files are write-once artifacts with SHA-256 sidecars.

## Data availability

All derived analysis datasets used here (frozen estimation samples, robustness ledgers, bootstrap replicates, simulation outputs) are included in the reproducibility bundle accompanying this submission and in the integrated public repository at https://github.com/bougtoir/legacy-lockin-manuscript. Third-party raw data were obtained from public sources: FAOSTAT crop production (https://www.fao.org/faostat/), MapSPAM/SPAM2000 and SPAM2010 (https://mapspam.info/), MIRCA2000 crop calendars (University of Frankfurt dataset), ERA5-derived agro-climatic fields, FAO GAUL/GADM administrative boundaries, the GHS Urban Centre Database R2024A (European Commission JRC, https://ghsl.jrc.ec.europa.eu/), OpenFEMA HMA Mitigated Properties, HMA Projects, Disaster Declarations Summaries and NFIP datasets (https://www.fema.gov/about/openfema/api), US Census Bureau SF3 2000 and population/housing-unit estimates, and HarvestStat/FAO subnational, Eurostat apro_cpshr, USDA Census of Agriculture, StatCan and IBGE PAM subnational agricultural series. Licence restrictions on raw third-party records prevent redistribution of some source tables; acquisition scripts and retrieval metadata (URLs, access dates, byte counts, SHA-256 hashes) are provided in the data-source ledgers so that all analyses can be regenerated from source. No proprietary or restricted-access data were used.

## Code availability

All analysis code — capacity audits, risk-set construction, information simulations, the single-opening analysis scripts, robustness suites and validators — is included in the reproducibility bundle and in the public repository at https://github.com/bougtoir/legacy-lockin-manuscript. A versioned archival release will be deposited in a persistent repository upon acceptance.

## Acknowledgements

None.

## Author contributions

O.T. conceived the study, designed the locked-test architecture, performed the analyses, and wrote the manuscript.

## Competing interests

The author declares no competing interests.

## References

1. Unruh, G. C. Understanding carbon lock-in. *Energy Policy* 28, 817–830 (2000).
2. Seto, K. C. et al. Carbon lock-in: types, causes, and policy implications. *Annu. Rev. Environ. Resour.* 41, 425–452 (2016).
3. David, P. A. Clio and the economics of QWERTY: the necessity of history. *Am. Econ. Rev.* 75, 332–337 (1985).
4. Arthur, W. B. Competing technologies, increasing returns, and lock-in by historical events. *Econ. J.* 99, 116–131 (1989).
5. North, D. C. *Institutions, Institutional Change and Economic Performance* (Cambridge Univ. Press, 1990).
6. Page, S. E. Path dependence. *Q. J. Polit. Sci.* 1, 87–115 (2006).
7. Geels, F. W. Technological transitions as evolutionary reconfiguration processes: a multi-level perspective and a case-study. *Res. Policy* 31, 1257–1274 (2002).
8. Markard, J., Raven, R. & Truffer, B. Sustainability transitions: an emerging field of research and its prospects. *Res. Policy* 41, 955–967 (2012).
9. Köhler, J. et al. An agenda for sustainability transitions research: state of the art and future directions. *Environ. Innov. Soc. Transit.* 31, 1–32 (2019).
10. Barnett, J. & O'Neill, S. Maladaptation. *Glob. Environ. Change* 20, 211–213 (2010).
11. Magnan, A. K. et al. Addressing the risk of maladaptation to climate change. *WIREs Clim. Change* 7, 646–665 (2016).
12. Juhola, S., Glaas, E., Linnér, B.-O. & Neset, T.-S. Redefining maladaptation. *Environ. Sci. Policy* 55, 135–140 (2016).
13. Eriksen, S. et al. Adaptation interventions and their effect on vulnerability in developing countries: help, hindrance or irrelevance? *World Dev.* 141, 105383 (2021).
14. Dow, K. et al. Limits to adaptation. *Nat. Clim. Change* 3, 305–307 (2013).
15. Schipper, E. L. F. Maladaptation: when adaptation to climate change goes very wrong. *One Earth* 3, 409–414 (2020).
16. Moser, S. C. & Ekstrom, J. A. A framework to diagnose barriers to climate change adaptation. *Proc. Natl Acad. Sci. USA* 107, 22026–22031 (2010).
17. Biesbroek, G. R. et al. On the nature of barriers to climate change adaptation. *Reg. Environ. Change* 13, 1119–1129 (2013).
18. Kates, R. W., Travis, W. R. & Wilbanks, T. J. Transformational adaptation when incremental adaptations to climate change are insufficient. *Proc. Natl Acad. Sci. USA* 109, 7156–7161 (2012).
19. Fedele, G., Donatti, C. I., Harvey, C. A., Hannah, L. & Hole, D. G. Transformative adaptation to climate change for sustainable social-ecological systems. *Environ. Sci. Policy* 101, 116–125 (2019).
20. Gajjar, S. P., Singh, C. & Deshpande, T. Tracing back to move ahead: a review of development pathways that constrain adaptation futures. *Clim. Dev.* 11, 223–237 (2019).
21. Adger, W. N. et al. Adaptation to climate change in the developing world. *Prog. Dev. Stud.* 3, 179–195 (2003).
22. Mendelsohn, R., Nordhaus, W. D. & Shaw, D. The impact of global warming on agriculture: a Ricardian analysis. *Am. Econ. Rev.* 84, 753–771 (1994).
23. Deschênes, O. & Greenstone, M. The economic impacts of climate change: evidence from agricultural output and random fluctuations in weather. *Am. Econ. Rev.* 97, 354–385 (2007).
24. Hornbeck, R. The enduring impact of the American Dust Bowl: short- and long-run adjustments to environmental catastrophe. *Am. Econ. Rev.* 102, 1477–1507 (2012).
25. Hornbeck, R. & Keniston, D. Creative destruction: barriers to urban growth and the Great Boston Fire of 1872. *Am. Econ. Rev.* 107, 1365–1398 (2017).
26. Vigdor, J. The economic aftermath of Hurricane Katrina. *J. Econ. Perspect.* 22, 135–154 (2008).
27. Hino, M., Field, C. B. & Mach, K. J. Managed retreat as a response to natural hazard risk. *Nat. Clim. Change* 7, 364–370 (2017).
28. Boustan, L. P., Kahn, M. E. & Rhode, P. W. Moving to higher ground: migration response to natural disasters in the early twentieth century. *Am. Econ. Rev.* 102, 238–242 (2012).
29. Marino, E. Adaptation privilege and voluntary buyouts: perspectives on ethnocentrism in sea level rise relocation and retreat policies in the US. *Glob. Environ. Change* 49, 10–13 (2018).
30. Franco, A., Malhotra, N. & Simonovits, G. Publication bias in the social sciences: unlocking the file drawer. *Science* 345, 1502–1505 (2014).
31. Fanelli, D. Do pressures to publish increase scientists' bias? An empirical support from US states data. *PLoS ONE* 5, e10271 (2010).
32. Schlenker, W. & Roberts, M. J. Nonlinear temperature effects indicate severe damages to U.S. crop yields under climate change. *Proc. Natl Acad. Sci. USA* 106, 15594–15598 (2009).
33. Lobell, D. B., Schlenker, W. & Costa-Roberts, J. Climate trends and global crop production since 1980. *Science* 333, 616–620 (2011).
34. Burke, M. & Emerick, K. Adaptation to climate change: evidence from US agriculture. *Am. Econ. J. Econ. Policy* 8, 106–140 (2016).
35. Costinot, A., Donaldson, D. & Smith, C. Evolving comparative advantage and the impact of climate change in agricultural markets: evidence from 1.7 million fields around the world. *J. Polit. Econ.* 124, 205–248 (2016).
36. Rising, J. & Devineni, N. Crop switching reduces agricultural losses from climate change in the United States by half under RCP 8.5. *Nat. Commun.* 11, 4991 (2020).
37. Melchiorri, M. et al. Unveiling 25 years of planetary urbanization with remote sensing: perspectives from the global human settlement layer. *Remote Sens.* 10, 768 (2018).
38. Melchiorri, M. et al. *Stats in the City — the GHSL Urban Centre Database 2025 (GHS-UCDB R2024A)* JRC139768 (Publications Office of the European Union, 2024), doi:10.2760/3046391.
39. Siders, A. R. Social justice implications of U.S. managed retreat buyout programs. *Clim. Change* 152, 239–257 (2019).
40. Mach, K. J. et al. Managed retreat through voluntary buyouts of flood-prone properties. *Sci. Adv.* 5, eaax8995 (2019).
41. Davis, D. R. & Weinstein, D. E. Bones, bombs, and break points: the geography of economic activity. *Am. Econ. Rev.* 92, 1269–1289 (2002).
42. Miguel, E. & Roland, G. The long-run impact of bombing Vietnam. *J. Dev. Econ.* 96, 1–15 (2011).
43. Caldecott, B., Howarth, N. & McSharry, P. *Stranded Assets in Agriculture: Protecting Value from Environment-Related Risks* (Smith School of Enterprise and the Environment, Univ. of Oxford, 2013).
44. FAO. *FAOSTAT Statistical Database* (Food and Agriculture Organization of the United Nations, Rome; accessed 2025).
45. You, L. et al. *Spatial Production Allocation Model (SPAM) 2000* (International Food Policy Research Institute; https://mapspam.info).
46. Portmann, F. T., Siebert, S. & Döll, P. MIRCA2000 — Global monthly irrigated and rainfed crop areas around the year 2000: a new high-resolution data set for agricultural and hydrological modeling. *Global Biogeochem. Cycles* 24, GB1011 (2010).
47. Hersbach, H. et al. The ERA5 global reanalysis. *Q. J. R. Meteorol. Soc.* 146, 1999–2049 (2020).
48. Baugh, C. et al. *Global River Flood Hazard Maps* (European Commission, Joint Research Centre, 2024), doi:10.2905/JRC.VD32YWG.

## Figure legends

**Figure 1 | Theory and empirical architecture.** The inherited-structure intuition predicts that legacy attenuates transformation under environmental demand. Four locked tests evaluate the interaction at distinct scales and on distinct margins, with continuous adjustment (crop mix, built reconfiguration) separated from discrete transition (first programme entry). All designs, samples and estimators were frozen before headline estimation.

**Figure 2 | Agricultural tests.** Interaction estimates (95% CI) for national crop specialization (fractional logit, N = 147, subregion bootstrap) and subnational irrigation dependence (OLS + country FE, N = 340, geographic-block bootstrap). Both are null.

**Figure 3 | Urban built-capital test.** Primary interaction estimate and prespecified coastal-proximity subgroups; a detectable but small and context-dependent association concentrated inland.

**Figure 4 | Settlement-transition test.** (a) Primary demand×legacy interaction, first-entry hazard. (b) Primary demand×capacity interaction. (c) Secondary estimates (lag-1 extensive; intensive-margin volume), visually separated from primary. (d) Primary vs secondary classification.

**Figure 5 | Cross-study synthesis.** Forest plot of the five primary interaction estimates: legacy construct, transformation margin, 95% confidence interval and classification for each locked primary test. No pooled effect is estimated; estimands are deliberately not comparable.


## Extended Data

**Extended Data Fig. 1 | Lock chronology and study architecture.**
**Extended Data Fig. 2 | National agricultural robustness.**
**Extended Data Fig. 3 | Subnational agricultural robustness.**
**Extended Data Fig. 4 | Urban robustness and heterogeneity.**
**Extended Data Fig. 5 | Urban negative controls.**
**Extended Data Fig. 6 | Transition risk-set construction.**
**Extended Data Fig. 7 | Transition robustness.**
**Extended Data Fig. 8 | Simulation and inference calibration.**
**Extended Data Table 1 | Complete design matrix.**
**Extended Data Table 2 | All primary estimands.**

## Supplementary Information

**Supplementary Table 1 | Integrated evidence table.** Unit, sample, legacy construct, environmental demand, transformation outcome, primary estimand, estimate, 95% CI, p-value and classification for each locked primary test. Provided as supplementary/SI_Table_1.csv in the submission package.
