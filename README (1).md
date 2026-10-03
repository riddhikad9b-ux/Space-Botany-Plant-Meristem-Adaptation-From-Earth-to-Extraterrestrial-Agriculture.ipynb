# 🌿 Space-Botany-Meristem-Dynamics
> **Plant Stem Cell Resilience & Transcriptomics in Extraterrestrial Microgravity**

[![Domain](https://img.shields.io/badge/Domain-Space%20Botany%20%26%20Bioinformatics-green.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](#)

---

## 📌 Executive Summary & Scientific Hypothesis

Under Earth’s constant $1\text{-g}$ environment, plant growth orientation and structural integrity are governed by gravity vectors. Gravitropic perception in root columella statocytes drives polar auxin transport via PIN efflux carriers, coordinating asymmetric elongation and cell wall assembly. In extraterrestrial microgravity ($g \approx 0$), the loss of this directional mechanical cue induces severe physiological disruptions:
* **Hormonal Disorientation:** Loss of amyloplast sedimentation breaks gravitropic integral control, randomizing auxin distribution and unmasking default helical growth tendencies (exaggerated root skewing).
* **Primary Cell Wall Disorganization:** Transmission electron microscopy reveals that nascent primary vessel walls suffer from scattered, non-parallel cellulose microfibril deposition and reduced wall thickness.
* **Meristematic Vulnerability:** Shoot Apical Meristem (SAM) and Root Apical Meristem (RAM) stem cell niches ($WUS\text{-}CLV3$ and $WOX4\text{-}PXY$ circuits) experience oxidative stress and mechanical instability under cosmic radiation and microgravity.

### Core Hypothesis
> *"Integrating climate-resilient molecular pathways—specifically stabilizing PABA-mediated auxin-ethylene crosstalk, activating vacuolar acid invertase ($Ivr2$) hexose sugar metabolism, and upregulating cell wall remodeling enzymes ($XTH1$, $EXPA1$)—restores mechanical anisotropy and stem cell niche maintenance, programming a 'space-resilient' plant model capable of stable growth in closed-loop extraterrestrial agricultural systems."*

---

## 📂 Repository Architecture

```text
Space-Botany-Meristem-Dynamics/
│
├── README.md                      # Master executive summary & research portfolio documentation
├── requirements.txt               # Dependencies: pandas, numpy, scipy, matplotlib, seaborn
│
├── docs/                          # Theoretical framework & literature synthesis
│   ├── phase1_literature_synthesis.md
│   └── phase2_scientific_hypothesis.md
│
├── src/                           # Reproducible bioinformatic pipelines
│   └── space_botany_transcriptomics.py
│
├── data/                          # Expression counts & DEG tables
│   └── space_botany_deg_results.csv
│
└── outputs/                       # Publication-quality visualization dashboard
    └── space_botany_expression_dashboard.png
```

---

## 🔬 Key Mechanistic Pillars

### 1. Statocyte Sensing & LAZY-RLD Machinery
In $1\text{-g}$, gravity perception occurs in root cap statocytes via amyloplast settling. This recruits **LAZY family proteins** and **RLD regulators** to polarize **PIN3** and **PIN7** to the lower membrane. Auxin flows via **PIN2** and **AUX1** into the Elongation Zone (EZ), where high auxin activates $CNGC14$ $\text{Ca}^{2+}$ channels to inhibit cell elongation on the lower flank while lower flank acidification via expansins drives downward curvature. Under microgravity, this polarization breaks down.

### 2. Pulvinar Metabolic Commitment
In cereal shoot pulvini, gravistimulation triggers a rapid 4-hour free-IAA gradient peak (Phase I). This commitments Phase II: transcriptional activation of vacuolar acid invertase (**$Ivr2$**). $Ivr2$ cleaves sucrose into D-glucose and D-fructose, driving localized water uptake, turgor pressure accumulation, and differential tissue elongation.

### 3. Quantitative Tipping Point Modeling
Based on empirical stress diagnostics, plant structural stability obeys a **55/45 weighted stress model**:
$$\text{Structural Vulnerability} = 0.55 \times (\text{Heatwave/Radiation Intensity}) + 0.45 \times (\text{Lodging Risk Index})$$

When environmental stress crosses the **$82.0 - 85.0$ tipping point threshold**, physical buckling risk eclipses biological resilience, dropping Meristemic Resilience Scores below $50.0$ unless protective cell-wall remodeling networks are activated.

---

## 💻 Bioinformatic Pipeline Usage (`space_botany_transcriptomics.py`)

The repository includes a modular Python pipeline for ingesting RNA-seq count matrices (spaceflight vs. ground controls), calculating $\text{Log}_2\text{ Fold Change}$ ($\text{Log}_2\text{FC}$), computing Student's t-test $p$-values, and generating visualization outputs.

### Installation
```bash
git clone https://github.com/Riddhika/Space-Botany-Meristem-Dynamics.git
cd Space-Botany-Meristem-Dynamics
pip install -r requirements.txt
```

### Execution
```bash
python src/space_botany_transcriptomics.py
```

### Transcriptomic Results Summary

| Gene Symbol | Functional Pathway | Target Tissue | Log2 Fold Change | $p$-value | Biological Impact in Microgravity |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **`LAZY1`** | Statocyte Perception | RAM | `-2.30` | `0.0004` | Loss of gravitropic orientation vector |
| **`PIN2`** | Polar Auxin Transport | RAM | `-2.15` | `0.0008` | Disrupted shootward auxin reflux |
| **`PIN3`** | Lateral Auxin Flow | Statocytes | `-1.85` | `0.0021` | Impaired asymmetric gradient formation |
| **`WUS`** | Stem Cell Pluripotency | SAM | `-1.72` | `0.0035` | Suppression of organizing center stem cells |
| **`WOX4`** | Cambial Maintenance | Meristem | `-1.68` | `0.0041` | Reduced vascular stem cell division |
| **`XTH1`** | Cell Wall Remodeling | Elongation Zone | `+2.45` | `0.0002` | Compensatory wall loosening & microfibril alignment |
| **`EXPA1`** | Cell Wall Extensibility | Elongation Zone | `+2.18` | `0.0006` | Acid-driven wall polymer loosening |
| **`PABA (TAA1)`** | Hormonal Crosstalk | Root Cap | `+2.10` | `0.0009` | Restores local asymmetric auxin synthesis |
| **`GST1`** | Oxidative Stress | SAM / RAM | `+2.60` | `0.0001` | Systemic ROS detoxification |

---

## 📊 Output Visualization Dashboard

The pipeline automatically outputs a publication-ready dual-panel figure (`outputs/space_botany_expression_dashboard.png`):
1. **Volcano Plot:** Plots $\text{Log}_2\text{FC}$ against $-\log_{10}(p\text{-value})$, highlighting significantly upregulated and downregulated genes in microgravity.
2. **Tissue Heatmap:** Profiles spatial expression shifts across the Shoot Apical Meristem (SAM), Root Apical Meristem (RAM), and Elongation Zone (EZ).

---

## 📜 Citation & License

This project is developed as part of the **Space Botany & Extraterrestrial Agriculture Portfolio**.
Licensed under the **MIT License**.
