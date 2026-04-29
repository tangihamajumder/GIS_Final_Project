# Arkansas Environmental Risk Screening

**Course:** GIS Programming — Western Michigan University  
**Semester:** Spring 2026  
**Author:** Tangiha Majumder

---

## Project Overview

This project develops a **tract-level environmental risk screening model** for Arkansas using three ecological indicator variables:

1. **Population Density** — 2022 ACS 5-Year Estimates (US Census Bureau)
2. **GHSL Built-up Intensity** — Global Human Settlement Layer via Google Earth Engine
3. **PM2.5 Air Quality** — Tract-level ambient particulate matter (EPA / CDC PLACES)

Each variable is min-max normalized and combined into an equal-weighted composite screening score. Census tracts are then classified into five risk quintiles: *Very Low, Low, Moderate, High, Very High*.

---

## Repository Structure

```
arkansas_env_risk/
├── assets/             # Output maps, charts, and figures
├── data/               # Input data files (CSVs, GDB references)
├── docs/               # Project documentation and data dictionary
├── notebooks/          # Main Jupyter analysis notebook
├── src/                # Helper Python modules (scoring, mapping)
├── tests/              # Unit tests for helper functions
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Data Sources

| Dataset | Source | Geography |
|---------|--------|-----------|
| ACS 2022 5-Year Estimates | US Census Bureau | Census Tract |
| GHSL 2020 Built-up Surface | Google Earth Engine | ~10m raster → Tract |
| PM2.5 Concentrations | EPA / CDC PLACES | Census Tract |

> **Note:** Raw data files (`.gdb`, large CSVs) are excluded from this repository via `.gitignore`. See `docs/data_guide.md` for download instructions.

---

## Setup & Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/arkansas_env_risk.git
cd arkansas_env_risk

# Install dependencies
pip install -r requirements.txt
```

---

## Running the Analysis

Open and run the main notebook:

```bash
jupyter notebook notebooks/Final_Project_v4_improved.ipynb
```

Update the file paths in the **Environment Setup** cell to point to your local copies of the input data files.

---

## Key Results

- Arkansas census tracts are scored on a 0–1 environmental risk scale
- Tracts classified as **High** or **Very High** risk are concentrated in urban cores and river-valley communities
- Approximately **[X]%** of the Arkansas population lives in High or Very High risk tracts *(fill in after running)*

---

## Rubric Coverage

| Rubric Item | Where Addressed |
|-------------|----------------|
| Initial Plan, Problem Statement, LOE, Budget | Notebook Section 1 |
| Data Sources & Conceptual Analysis | Notebook Section 2 |
| GEE Layer + 3 Eco/Enviro Indicators | Sections 5, 6, 7 |
| Charts, Maps, Data Analysis | Section 9 |
| Code Quality & Python Knowledge | All code cells |
| Conclusion, Insights, Next Steps | Section 11 |

---


