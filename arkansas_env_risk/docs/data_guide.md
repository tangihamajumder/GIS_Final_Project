# Data Guide

This document describes each dataset used in the project, where to download it, and how to place it in the `data/` folder.

---

## 1. ACS 2022 5-Year Census Tract Data (Arkansas)

**Source:** US Census Bureau — TIGER/Line with Selected Demographic and Economic Data  
**URL:** https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-data.html  
**File:** `ACS_2022_5YR_TRACT_05_ARKANSAS.gdb`  
**Layers used:**
- `ACS_2022_5YR_TRACT_05_ARKANSAS` — tract geometry + GEOIDFQ
- `X01_AGE_AND_SEX` — total population (`B01003_E001`)

**Place in:** `data/ACS_2022_5YR_TRACT_05_ARKANSAS.gdb/`

---

## 2. GHSL Built-up Intensity — Google Earth Engine Export

**Source:** European Commission — Global Human Settlement Layer (GHS-BUILT-S 2020)  
**Accessed via:** Google Earth Engine  
**GEE Dataset ID:** `JRC/GHSL/P2023A/GHS_BUILT_S`  
**Export:** Tract-level summary statistics computed with `reduceRegions()` (mean, sum)  
**File:** `Arkansas_Tract_GHSL_Stats_2020.csv`

**Columns used:**
- `GEOID` — 11-digit census tract identifier
- `ghsl_built_mean` — mean built-up intensity per tract
- `ghsl_built_sum` — total built-up area per tract
- `ghsl_pop_density` — GHSL population density
- `ghsl_pop_sum` — GHSL total population

**Place in:** `data/Arkansas_Tract_GHSL_Stats_2020.csv`

---

## 3. PM2.5 Tract-Level Concentrations

**Source:** EPA / CDC PLACES (Environmental Justice datasets)  
**URL:** https://www.epa.gov/ejscreen  
**File:** `data_144231.csv`  
**Columns used:**
- `CensusTract` — tract GEOID (converted to 11-digit zero-padded)
- `Value` — daily PM2.5 concentration (µg/m³)

**Place in:** `data/PM2.5_AR/data_144231.csv`

---

## File Path Configuration

Update the paths in the **Environment Setup** cell of the notebook:

```python
gdb_path    = "data/ACS_2022_5YR_TRACT_05_ARKANSAS.gdb/ACS_2022_5YR_TRACT_05_ARKANSAS.gdb"
ghsl_csv    = "data/Arkansas_Tract_GHSL_Stats_2020.csv"
pm25_path   = "data/PM2.5_AR/data_144231.csv"
output_folder = "assets/"
```
