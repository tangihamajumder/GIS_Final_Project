# Methodology

## Environmental Risk Screening Model

### Indicator Variables

| Variable | Source | Unit | Role |
|----------|--------|------|------|
| Population Density | ACS 2022 | persons/km² | Exposure population |
| GHSL Built-up Intensity | GEE / GHSL 2020 | dimensionless (0–1) | Settlement indicator |
| PM2.5 Mean | EPA/CDC | µg/m³ | Air quality burden |

### Normalization

All three variables are min-max normalized to a 0–1 scale:

```
X_std = (X - X_min) / (X_max - X_min)
```

### Composite Score

The screening score is the equal-weighted mean of the three standardized variables:

```
Risk Score = (PopDen_std + GHSL_std + PM25_std) / 3
```

### Classification

Tracts are classified into 5 quintile-based risk classes using `pd.qcut()`:

| Class | Description |
|-------|-------------|
| Very Low | Bottom 20% of scores |
| Low | 20th–40th percentile |
| Moderate | 40th–60th percentile |
| High | 60th–80th percentile |
| Very High | Top 20% of scores |

### Limitations

- Equal weighting assumes all three variables contribute equally to risk — this is a simplification
- Min-max normalization is sensitive to outliers
- Temporal mismatch: ACS (2018–2022), GHSL (2020), PM2.5 (varies)
- Missing PM2.5 values for some tracts result in missing composite scores
