"""
scoring.py
----------
Helper functions for normalizing environmental indicator variables
and computing the composite risk screening score.

Usage:
    from src.scoring import minmax, compute_risk_score, classify_risk
"""

import numpy as np
import pandas as pd


def minmax(series: pd.Series) -> pd.Series:
    """
    Apply min-max normalization to a pandas Series.

    Values are scaled to the range [0, 1]. Non-numeric values are coerced
    to NaN. If all values are identical (zero variance), returns a zero Series.

    Parameters
    ----------
    series : pd.Series
        Input data to normalize.

    Returns
    -------
    pd.Series
        Normalized series in range [0, 1].
    """
    s = pd.to_numeric(series, errors="coerce")
    smin = s.min(skipna=True)
    smax = s.max(skipna=True)
    if pd.isna(smin) or pd.isna(smax) or smax == smin:
        return pd.Series(np.zeros(len(s)), index=s.index)
    return (s - smin) / (smax - smin)


def compute_risk_score(df: pd.DataFrame,
                       pop_col: str = "pop_density",
                       built_col: str = "ghsl_built_mean",
                       pm25_col: str = "pm25_2026_mean") -> pd.DataFrame:
    """
    Normalize three indicator variables and compute an equal-weighted
    composite environmental risk screening score.

    Parameters
    ----------
    df : pd.DataFrame
        Input GeoDataFrame or DataFrame with indicator columns.
    pop_col : str
        Column name for population density.
    built_col : str
        Column name for GHSL built-up intensity.
    pm25_col : str
        Column name for PM2.5 mean concentration.

    Returns
    -------
    pd.DataFrame
        Input DataFrame with added columns:
        - popden_std, built_std, pm25_std (normalized 0–1)
        - risk_score_3var (composite score 0–1)
    """
    result = df.copy()
    result["popden_std"] = minmax(result[pop_col])
    result["built_std"] = minmax(result[built_col])
    result["pm25_std"] = minmax(result[pm25_col])
    result["risk_score_3var"] = result[
        ["popden_std", "built_std", "pm25_std"]
    ].mean(axis=1)
    return result


def classify_risk(df: pd.DataFrame,
                  score_col: str = "risk_score_3var",
                  n_classes: int = 5) -> pd.DataFrame:
    """
    Classify risk scores into quintile-based risk categories.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the composite risk score column.
    score_col : str
        Name of the score column to classify.
    n_classes : int
        Number of quantile classes (default: 5).

    Returns
    -------
    pd.DataFrame
        Input DataFrame with added 'risk_class_3var' column.
    """
    labels = ["Very Low", "Low", "Moderate", "High", "Very High"][:n_classes]
    result = df.copy()
    result["risk_class_3var"] = pd.qcut(
        result[score_col],
        q=n_classes,
        labels=labels,
        duplicates="drop"
    )
    return result
