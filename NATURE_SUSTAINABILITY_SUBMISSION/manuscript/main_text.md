# When does inherited structure become adaptation lock-in?

**Onishi Tatsuki**
Data Science and AI Innovation Research Promotion Center, Shiga University, Hikone, Shiga, Japan

## Abstract

Climate adaptation unfolds within inherited systems — crop portfolios, irrigation networks, built environments and institutions — widely treated as potential sources of lock-in. Whether inherited structure itself generates rigidity is rarely tested falsifiably across distinct systems. We subjected this intuition to four tests in which each primary design was frozen, outcome-blind, before its headline estimate was computed: national crop specialization, subnational irrigation dependence, urban built capital under flood exposure, and institutionalized departure of flood-prone settlements. Crop specialization and irrigation dependence showed no detectable conditioning of transformation under climatic mismatch. Built capital produced a small, context-dependent negative interaction concentrated inland. At transition margins the legacy interaction was negative but uncertain, and prior programme capacity did not amplify transition initiation. Inherited specialization, capital and institutional legacy were insufficient to produce a stable general rigidity pattern. Legacy should be treated as a hypothesis about constraint, not evidence of constraint.

## Introduction

Climate adaptation and sustainability transitions do not begin from a blank slate. Food production runs on inherited crop portfolios and irrigation works; cities are fixed quantities of buildings and networks laid down under past conditions; institutions accumulate programmes, rules and capabilities that channel every subsequent response. These inherited systems are assets: they embody accumulated knowledge, embodied capital and network value that make incremental adaptation cheaper and more reliable{1,2}. The economics of increasing returns formalized why: once a technology, crop or urban form is adopted, learning effects, coordination benefits and adaptive expectations raise the cost of every alternative{3,4}.

The same inheritances are frequently described in the adaptation and transitions literatures as sources of rigidity — path dependence{3–6}, infrastructure and carbon lock-in{1,2}, adaptation lock-in, stranded assets{7–9}. Underlying these labels is an influential intuition: that accumulated specialization and fixed capital themselves generate resistance to transformation{10–15}. The claim is consequential. If inherited structure is the binding constraint on adaptation, then transformation requires either catastrophe-level forcing or costly structural demolition, and incremental adaptation policy is largely futile in legacy-heavy systems. Yet persistence and constraint are not logically identical. A system can persist because alternatives are inferior, because change is not yet demanded, or because substitution is genuinely blocked; only the last of these is lock-in, and observing accumulated structure does not distinguish among them. Empirical work has nevertheless proceeded largely by attributing observed persistence to lock-in, or by documenting that adaptation is insufficient and inferring that structure must be at fault.

This distinction yields a falsifiable prediction. If accumulated legacy is itself a general source of adaptation rigidity, then systems carrying greater pre-existing specialization, fixed capital or institutional commitment should show systematically attenuated transformation when environmental demand for change intensifies{16,17}. The prediction is cross-domain: it should hold in agricultural portfolios, in urban spatial structure and in discrete institutional transitions alike. It is also sequential in strength. If the interaction fails under the weakest conditions — continuous, marginal reallocation — there is little reason to expect it at harder margins; if it appears only at the hardest margin — initiation of transformational departure — the boundary itself is informative.

We tested it sequentially in four locked empirical designs (Fig. 1). The first examines whether national crop specialization conditioned long-run crop-mix transformation under growing climatic mismatch across 147 countries{18–21}. The second asks the same question at the scale where adaptation is implemented — 340 first-level administrative units in 23 countries — replacing specialization with baseline irrigation dependence, a physically fixed form of agricultural capital{22,23}. The third turns to the most capital-intensive human system: whether pre-existing built volume conditioned spatial reconfiguration of 4,598 urban centres across baseline riverine flood-exposure gradients between 2000 and 2020{24–26}. The fourth addresses the discrete, transformational margin: whether the age of county housing stock and prior programme experience conditioned the initiation of FEMA-supported transformational-departure (property acquisition and relocation) programmes in US counties after flood disasters between 2000 and 2020{27–29}. For each branch, the primary sample, exposures, outcome, estimator and inference procedure were frozen before the corresponding headline outcome was estimated; each primary test was executed exactly once, and null and uncertain results were preserved rather than explored into alternatives{30,31}. This design converts a familiar rhetorical claim into a set of separate, examinable tests whose failures are as informative as its successes, and it removes the researcher's largest degree of freedom — the freedom to keep searching until the hypothesis is confirmed.

The expected general rigidity pattern did not emerge. The two agricultural tests yield tightly centred nulls; the urban test yields a small, context-dependent interaction; the transition test yields a directional but uncertain barrier and an unsupported enablement mechanism. What the programme produces instead is an empirical boundary: accumulated legacy alone is insufficient evidence of adaptation lock-in. Constraint, where it exists, must be demonstrated against measurable barriers — substitution costs, network dependence, coordination thresholds, institutional exit — rather than inferred from the depth of accumulated structure.

## Results

### Specialization and fixed capital do not produce detectable agricultural rigidity

We first tested whether national crop specialization conditions crop-system transformation under climatic mismatch. Legacy was measured as the Herfindahl concentration of the production portfolio in 1981–2001; environmental demand as a crop-calendar mismatch index — the Mahalanobis displacement of each country's dominant crop's agro-climatic window between 1984–2001 and 2002–2020; transformation as the Jensen–Shannon divergence (JSD) between early and late crop-mix distributions{32–36}. In the frozen fractional-logit specification on 147 countries, the specialization-by-mismatch interaction was β3 = +0.005 (95% CI [−0.131, +0.143], M49-subregion cluster bootstrap, B = 999; Fig. 2). The interval is centred almost exactly on zero and excludes meaningful conditioning in either direction at the observed scale (Extended Data Fig. 2).

We then repeated the test at first-level administrative units, where irrigation infrastructure — a physically sunk capital stock — replaces portfolio concentration as the legacy construct. On the locked sample of 340 admin-1 units in 23 countries, the irrigation-by-mismatch interaction was β3 = −0.038 (95% CI [−0.251, +0.077], 10-degree geographic-block bootstrap, B = 999, p = 0.384; Fig. 2). Nine prespecified robustness variants and a falsification suite were consistent with the null (Extended Data Fig. 3); a positive falsification at pre-treatment exposure (conditional result) is retained in the record as a caution against strong causal reading of any small residual association. The agricultural branches were then permanently closed: both nulls are prospectively locked and were not reopened.

### Built capital weakly conditions urban reconfiguration

The third test moved to built capital — the longest-lived and most network-entangled form of inherited structure — using the Global Human Settlement Layer Urban Centre Database, which fixes settlement footprints and reports epoch-specific built volume, population and modelled riverine flood exposure for 11,422 urban centres{37,38}. On the locked sample of 4,598 urban centres in 143 countries observed in 2000 and 2020, we regressed a net hazard-avoidance reallocation index on standardized log built volume in 2000 (legacy), the baseline ten-year-return-period flood-exposed share (exposure), their interaction and controls, with country fixed effects. The legacy-by-exposure interaction was β3 = −0.0083 (95% CI [−0.0166, −0.0033], 1,000-km geographic-block bootstrap, B = 999, p = 0.002), equivalent to an original-scale marginal contrast of −0.010 on the reallocation index — approximately 4% of its standard deviation (Fig. 3).

The association is real but small and sharply context-dependent. It is concentrated in inland settlements (inland >50 km: β3 ≈ −0.019) while coastal-proximity strata are near zero (≤10 km: ≈ −0.0004). A longer-return-period (RP100) hazard definition reverses the sign; per-capita and per-area capital intensity attenuate it; nonlinear strata show the legacy effect strongest at low, not high, hazard; and the sea-level-rise subset (1,334 urban centres with altimetry coverage) does not reproduce the pattern (Extended Data Figs. 4 and 5). We therefore classify this branch as weak and context-dependent conditioning, not general urban lock-in.

### Legacy signals strengthen near transformational margins but remain uncertain

The fourth test isolated the discrete margin where lock-in claims bite hardest: initiation of transformational-departure programmes — FEMA-funded property acquisition and relocation{39,40} — rather than continuous adjustment. The outcome is the first observed FEMA-supported transformational-departure programme entry in a county, measured in programme fiscal years; the risk set keeps all 3,062 at-risk counties, including 2,041 that never transition, contributing 51,686 county-years and 1,021 first events during 2000–2020 (Extended Data Fig. 6). Demand is the strictly lagged three-year burden of unique county-level major flood declarations; legacy is the median construction year of the 2000 housing stock; capacity — measured after an audit re-scoped it to departure-type projects only — is cumulative prior obligations on acquisition and relocation projects. The frozen estimator is a discrete-time complementary log–log first-entry hazard with year baseline hazards, state effects and county-clustered inference.

Flood demand strongly predicts first programme entry (main effect +1.10, p ≈ 2×10⁻¹¹). The primary legacy interaction, however, is directional but uncertain: β = −0.192 (95% CI [−0.454, +0.069], p = 0.149; Fig. 4a) — consistent with a legacy barrier but not distinguishable from zero, and the interval is wide enough to contain substantively large barriers. The capacity interaction is unsupported: β = +0.034 (95% CI [−0.097, +0.166], p = 0.610; Fig. 4b). Prior departure-programme experience predicts higher baseline programme activity but does not amplify the demand-triggered transition initiation it was theorized to enable.

Prespecified secondary analyses are consistent with — but cannot confirm — the primary reading. In the lag-1 demand window the extensive-margin interaction strengthened to β = −0.380 (p = 0.012), and on the secondary intensive margin (entry volumes, PPML with county and year fixed effects) the legacy interaction was β = −0.548 (95% CI [−0.910, −0.187], p = 0.003; Fig. 4c, Extended Data Table 2). Because the primary estimand remains uncertain, these strengthen the hypothesis rather than the finding: the strongest remaining legacy signature appeared at transformational-departure margins, but it did not meet the confirmatory threshold for transition initiation.

### Legacy effects do not generalize across adaptation systems

Read together, the four frozen tests trace a coherent boundary rather than a coherent law (Fig. 5, Table 1). Two independent agricultural scales show tightly-centred nulls. The one system where a primary interaction reached precision — urban built capital — produced an effect an order of magnitude smaller than a threshold of practical consequence and that vanished or reversed under prespecified respecifications. At the institutional transition margin the legacy direction is systematically negative — nine of nine numeric fits across extensive and intensive estimands (Extended Data Fig. 7) — but the confirmatory opening remained uncertain, and the capacity-enablement leg of the mechanism failed outright. Across domains, accumulated specialization, capital and institutional experience predict where adaptation activity occurs (large main effects of demand and prior capacity) far better than whether inherited structure blocks it.

## Discussion

Accumulated legacy did not operate as a general predictor of adaptation rigidity. Across national and subnational agriculture, urban built capital and institutionalized transformational departure, the interaction between inherited structure and environmental demand was either absent, small and context-dependent, or directional but uncertain. The umbrella intuition — legacy implies lock-in — did not survive four outcome-blind locked tests.

This negative generalization result matters because lock-in terminology is doing double work in adaptation science. It conflates the observation that systems persist with the demonstration that alternatives are foreclosed{3,6,41,42}. Our tests operationalize the second, stronger claim and find it unsupported as a blanket proposition. The contribution is not that inherited systems are adaptable — we did not measure realized welfare, livelihood continuity or ecological outcomes — but that inherited structure alone is not evidence that they are not. This is a stronger statement than the familiar complaint that lock-in is 'overused'. It says that at the scales and on the margins we tested, the observable implication of general lock-in — an attenuation of transformation that grows with both legacy and demand — is not where the data sit.

The agricultural nulls are the clearest boundary. If specialization and sunk irrigation capital do not measurably condition crop-system transformation under growing climatic mismatch at either the national or first-administrative scale, then portfolio and infrastructure legacy cannot be invoked as stand-alone explanations for agricultural rigidity; where rigidity appears, something else must carry it — market access, coordination, price incentives, land tenure or substitution opportunities our legacy measures do not capture. This is consistent with evidence that crop switching and comparative-advantage reallocation remain substantial{35,36} and that measured adaptation shortfalls concentrate in output outcomes rather than in the transformation margin itself{34}.

Urban built capital is the branch that comes closest to the hypothesized pattern: the interaction is detectable and correctly signed. Its weakness is as informative as its existence. An interaction of roughly 4% of the outcome's standard deviation, concentrated inland, reversing at longer hazard return periods and not reproducing under the sea-level-rise subset is conditioning at the margin, not lock-in. For the catastrophic visions of stranded coastal cities{43} the test provides no support; for the more modest claim that older, denser built stock modestly dampens hazard-avoidant reconfiguration, it provides qualified support.

The transition study holds the programme's most interesting residue. The primary evidence for a legacy barrier to initiating departure programmes is directional but uncertain; the secondary, pre-specified signatures — stronger at shorter demand lags and on the transition-intensity margin — point the same way. That gradient is consistent with a real barrier that binds at transition depth rather than at initiation, and it is a concrete, falsifiable target for a powered independent study with a pre-specified transition-intensity estimand. Equally informative is the failure of enablement: counties' accumulated FEMA departure-programme experience did not condition their demand-triggered transitions, so prior institutional practice cannot be assumed to unlock transformation either.

We propose — without claiming to have demonstrated — the boundary conditions these results suggest. Legacy becomes lock-in only where at least one measurable constraint binds: low substitutability between current and transformed configurations; network dependence that makes piecemeal change non-viable; coordination thresholds that no actor can cross alone; absent exit mechanisms; or institutional barriers that block rather than merely channel transition. Each is observable and distinguishable from accumulated capital per se, and each is a better target for policy diagnosis than investment history. A research agenda follows directly: measure substitutability and switching costs where transformation is demanded; test the transition-depth margin the secondary signatures point to; and treat each candidate constraint as a separate estimand rather than a synonym for lock-in. This also separates two objects the literature often merges: persistence of system form and persistence of system function. Reconfiguration may preserve function while abandoning form; our urban and transition outcomes measured movement of the form margin, and functional sustainability remains unmeasured. A system may abandon form extensively while preserving function — a city that relocates its flood-exposed fringe is still a city — so rigidity of form does not entail loss of function, and flexibility of form does not guarantee it.

The policy implication is narrow. Adaptation assessment should measure actual transition constraints — availability of substitutes, switching costs, network dependence, institutional exit mechanisms, transition-support capacity and whether function can be preserved through reconfiguration — rather than inferring them from the depth of past investment. Where communities and treasuries are asked to finance structural change on the argument that inherited systems cannot adapt, our tests show the premise has not been demonstrated: diagnosis must precede the demolition order.

Several limitations bound the claim. The four domains are heterogeneous and deliberately so; there is no common causal estimand, and we report no pooled effect. Identification is observational: frozen designs prevent specification fishing but cannot eliminate confounding. Outcome-blind locking is not external preregistration. The urban exposure is baseline modelled riverine flood exposure, not observed worsening hazard. The transition study is US-specific and institutionally mediated through FEMA programmes; its capacity measure is programme experience, not general social capacity; and no household destination or arrival outcome exists in this record. The transition-intensity signal is secondary and awaits confirmatory design. A companion ecological branch of the programme found no universal law and is outside the scope of this paper. Finally, our tests measure whether transformation happens, not whether it is timely, just or sufficient — systems may transform and still adapt badly.

Legacy should be treated as a hypothesis about constraint, not evidence of constraint.

## Methods

### Study architecture

The programme tested one falsifiable prediction in four sequential branches: systems with greater inherited specialization, fixed capital or institutional commitment should show attenuated transformation under stronger environmental demand. For each branch the primary sample, exposures, outcome, estimator and inference procedure were frozen in a versioned analysis lock (YAML + SHA-256) before the headline outcome was estimated; the headline model was executed exactly once and its output recorded immutably with checksums. Outcome-blind simulations on the frozen design matrix calibrated inference before each opening. No primary estimate was refit to strengthen results; locked agricultural nulls were not reopened.

### National agriculture

Countries were the unit (N = 147 with sufficient data). Legacy: Herfindahl index of the 1981–2001 production portfolio (FAOSTAT/MapSPAM basis). Demand: dominant-crop crop-calendar mismatch, a Mahalanobis displacement between the crop's 1984–2001 and 2002–2020 agro-climatic windows (MIRCA2000 crop calendar; ERA5-derived fields). Outcome: JSD between early (1981–2001) and late (2002–2020) crop-mix distributions, scaled by √ln 2. Estimator: fractional logit with standardized predictors. Inference: M49-subregion cluster bootstrap, B = 999, two-sided percentile 95% CI — selected after spatial-inference simulation rejected five-cluster CRVE (anti-conservative). Primary estimate: β3 = +0.0046 [−0.131, +0.143].

### Subnational agriculture

First-level administrative units (N = 340 units, 23 countries, four regions after strict first-order-division audit). Legacy: baseline irrigation dependence, zonal irrigated harvest-area share from SPAM2000 (~2000, pre-transition). Demand: unit-level crop-calendar mismatch on each unit's observed agricultural window. Outcome: JSD of crop-mix between early and late vintages (median gap 17 years). Estimator: OLS with country fixed effects. Inference: 10-degree geographic-block bootstrap, B = 999 (calibrated by bounded-outcome simulation; country-cluster CRVE rejected as anti-conservative). Primary estimate: β3 = −0.0377 [−0.2513, +0.0773], p = 0.384.

### Flood-exposed urban settlements

Urban centres from the GHS Urban Centre Database R2024A (N = 4,598 centres in 143 countries present in 2000 and 2020). Legacy: standardized log built-up volume in 2000. Exposure: baseline share of centre area exposed to modelled riverine flooding at ten-year return period (CEMS-GLOFAS/Baugh-derived static field). Outcome: net hazard-avoidance reallocation index 2000→2020 (net shift of built volume out of exposed zones; not a gross-addition share). Estimator: OLS with country fixed effects and controls (log population, elevation, port distance, within-50 km urban-centre cover). Inference: 1,000-km Mollweide block bootstrap, B = 999. Primary estimate: β3 = −0.008275 [−0.0166, −0.0033], p = 0.002; original-scale marginal contrast ΔME = −0.0102 [−0.0205, −0.0041]. Prespecified heterogeneity by coastal proximity, return period, capital-intensity scaling, hazard stratum and sea-level-rise subset.

### Settlement-transition initiation

US counties (3,062 at risk; 51,686 county-years 2000–2020; 1,021 first events; 2,041 never-transition counties retained). Outcome: first observed FEMA-supported transformational-departure programme entry (programme fiscal year). Demand: strictly lagged three-year burden of unique county-level major flood disaster declarations (OpenFEMA DisasterDeclarationsSummaries). Legacy: standardized negative median construction year of the 2000 housing stock (Census 2000 SF3 H035). Capacity: strictly lagged cumulative obligations on departure-type HMA projects only (200.x acquisition excluding vacant land, 201.x relocation; OpenFEMA HMA Projects, component-level action-type audit). Estimator: discrete-time complementary log–log hazard with year dummies, state fixed effects, log housing units and Mundlak county means. Inference: county-cluster CRV1 selected by null-simulation calibration (type-I 8.2%, warning band; state clustering exceeded 0.10; Extended Data Fig. 8). Primary estimates: H1 demand×legacy −0.1923 [−0.4537, +0.0692], p = 0.149; H2 demand×capacity +0.0342 [−0.0975, +0.1660], p = 0.610. Secondary intensive margin: PPML, county and year fixed effects, offset log housing units.

### Statistical reporting and robustness

All primary results are reported with effect estimates, 95% CIs and p-values. Prespecified robustness suites (9–11 variants per branch), falsification tests, leave-one-unit-out grids and information/power simulations are reported in full in the reproducibility bundle and Extended Data (Figs. 1–8, Tables 1–2). No pooled meta-analytic effect is reported because estimands are not comparable.

### Reproducibility

Every lock file, frozen sample, checksum, simulation and script is in the reproducibility bundle (REPRODUCIBILITY_BUNDLE_NS.zip) and the public repository mirrors listed in Data and Code Availability. Primary-opening JSON files are write-once artifacts with SHA-256 sidecars.

## Data availability

All derived analysis datasets used here (frozen estimation samples, robustness ledgers, bootstrap replicates, simulation outputs) are included in the reproducibility bundle accompanying this submission and are mirrored in the public repository at https://github.com/bougtoir/settlement-transition-feasibility and companion branch mirrors. Third-party raw data were obtained from public sources: FAOSTAT crop production (https://www.fao.org/faostat/), MapSPAM/SPAM2000 and SPAM2010 (https://mapspam.info/), MIRCA2000 crop calendars (University of Frankfurt dataset), ERA5-derived agro-climatic fields, FAO GAUL/GADM administrative boundaries, the GHS Urban Centre Database R2024A (European Commission JRC, https://ghsl.jrc.ec.europa.eu/), OpenFEMA HMA Mitigated Properties, HMA Projects, Disaster Declarations Summaries and NFIP datasets (https://www.fema.gov/about/openfema/api), US Census Bureau SF3 2000 and population/housing-unit estimates, and HarvestStat/FAO subnational, Eurostat apro_cpshr, USDA Census of Agriculture, StatCan and IBGE PAM subnational agricultural series. Licence restrictions on raw third-party records prevent redistribution of some source tables; acquisition scripts and retrieval metadata (URLs, access dates, byte counts, SHA-256 hashes) are provided in the data-source ledgers so that all analyses can be regenerated from source. No proprietary or restricted-access data were used.

## Code availability

All analysis code — capacity audits, risk-set construction, information simulations, the single-opening analysis scripts, robustness suites and validators — is included in the reproducibility bundle and mirrored at the public repository above. A permanent archive DOI will be minted at publication stage [PLACEHOLDER: Zenodo DOI to be added upon deposit].

## Acknowledgements

[To be completed by the author.]

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
38. Florczyk, A. J. et al. *GHSL Data Package 2019* (Publications Office of the European Union, 2019).
39. Siders, A. R. Social justice implications of U.S. managed retreat buyout programs. *Clim. Change* 152, 239–257 (2019).
40. Mach, K. J. et al. Managed retreat through voluntary buyouts of flood-prone properties. *Sci. Adv.* 5, eaax8995 (2019).
41. Davis, D. R. & Weinstein, D. E. Bones, bombs, and break points: the geography of economic activity. *Am. Econ. Rev.* 92, 1269–1289 (2002).
42. Miguel, E. & Roland, G. The long-run impact of bombing Vietnam. *J. Dev. Econ.* 96, 1–15 (2011).
43. Caldecott, B., Howarth, N. & McSharry, P. *Stranded Assets in Agriculture: Protecting Value from Environment-Related Risks* (Smith School of Enterprise and the Environment, Univ. of Oxford, 2013).

## Figure legends

**Figure 1 | Theory and empirical architecture.** The inherited-structure intuition predicts that legacy attenuates transformation under environmental demand. Four locked tests evaluate the interaction at distinct scales and on distinct margins, with continuous adjustment (crop mix, built reconfiguration) separated from discrete transition (first programme entry). All designs, samples and estimators were frozen before headline estimation.

**Figure 2 | Agricultural tests.** Interaction estimates (95% CI) for national crop specialization (fractional logit, N = 147, subregion bootstrap) and subnational irrigation dependence (OLS + country FE, N = 340, geographic-block bootstrap). Both are null.

**Figure 3 | Urban built-capital test.** Primary interaction estimate and prespecified coastal-proximity subgroups; a detectable but small and context-dependent association concentrated inland.

**Figure 4 | Settlement-transition test.** (a) Primary demand×legacy interaction, first-entry hazard. (b) Primary demand×capacity interaction. (c) Secondary estimates (lag-1 extensive; intensive-margin volume), visually separated from primary. (d) Primary vs secondary classification.

**Figure 5 | Cross-study synthesis.** Evidence map of the four primary tests: legacy construct, transformation margin, effect, precision and classification. No pooled effect is estimated; estimands are deliberately not comparable.

**Table 1 | Integrated evidence table.** Unit, sample, legacy construct, environmental demand, transformation outcome, primary estimand, estimate, 95% CI, p-value and classification for each locked primary test.

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
