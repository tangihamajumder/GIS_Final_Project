# data/

This folder holds input data files used by the analysis notebook.

Large files (`.gdb`, `.gpkg`, large CSVs) are excluded from git via `.gitignore`.  
See `docs/data_guide.md` for download instructions and expected file placement.

## Expected contents (not tracked by git)

```
data/
├── ACS_2022_5YR_TRACT_05_ARKANSAS.gdb/   ← ACS tract GDB (Census Bureau)
├── Arkansas_Tract_GHSL_Stats_2020.csv     ← GEE GHSL export
└── PM2.5_AR/
    └── data_144231.csv                    ← EPA PM2.5 tract data
```
