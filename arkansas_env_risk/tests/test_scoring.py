"""
test_scoring.py
---------------
Unit tests for src/scoring.py helper functions.

Run with:
    pytest tests/test_scoring.py -v
"""

import numpy as np
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.scoring import minmax, compute_risk_score, classify_risk


# ------------------------------------------------------------------
# minmax tests
# ------------------------------------------------------------------

def test_minmax_basic():
    """Output should be in [0, 1] range."""
    s = pd.Series([10, 20, 30, 40, 50])
    result = minmax(s)
    assert result.min() == 0.0
    assert result.max() == 1.0


def test_minmax_zero_variance():
    """All-same values should return a zero Series (no division by zero)."""
    s = pd.Series([5, 5, 5, 5])
    result = minmax(s)
    assert (result == 0).all()


def test_minmax_with_nan():
    """NaN values should remain NaN after normalization."""
    s = pd.Series([0, 10, np.nan, 20])
    result = minmax(s)
    assert result.isna().sum() == 1


def test_minmax_non_numeric_coerced():
    """Non-numeric strings should be coerced to NaN."""
    s = pd.Series(["a", "b", 10, 20])
    result = minmax(s)
    assert result.isna().sum() == 2


# ------------------------------------------------------------------
# compute_risk_score tests
# ------------------------------------------------------------------

def test_compute_risk_score_columns():
    """Output DataFrame should contain all expected columns."""
    df = pd.DataFrame({
        "pop_density": [100, 200, 300],
        "ghsl_built_mean": [0.1, 0.5, 0.9],
        "pm25_2026_mean": [8.0, 10.0, 12.0],
    })
    result = compute_risk_score(df)
    for col in ["popden_std", "built_std", "pm25_std", "risk_score_3var"]:
        assert col in result.columns, f"Missing column: {col}"


def test_compute_risk_score_range():
    """Risk score should be in [0, 1]."""
    df = pd.DataFrame({
        "pop_density": [50, 150, 250, 350],
        "ghsl_built_mean": [0.1, 0.3, 0.6, 0.9],
        "pm25_2026_mean": [7.0, 9.0, 11.0, 13.0],
    })
    result = compute_risk_score(df)
    assert result["risk_score_3var"].min() >= 0.0
    assert result["risk_score_3var"].max() <= 1.0


# ------------------------------------------------------------------
# classify_risk tests
# ------------------------------------------------------------------

def test_classify_risk_labels():
    """Risk classes should use the expected label set."""
    df = pd.DataFrame({
        "risk_score_3var": [0.1, 0.3, 0.5, 0.7, 0.9,
                            0.15, 0.35, 0.55, 0.75, 0.95]
    })
    result = classify_risk(df)
    expected = {"Very Low", "Low", "Moderate", "High", "Very High"}
    actual = set(result["risk_class_3var"].dropna().astype(str).unique())
    assert actual.issubset(expected)


def test_classify_risk_column_exists():
    """Output should contain 'risk_class_3var' column."""
    df = pd.DataFrame({"risk_score_3var": list(range(10))})
    result = classify_risk(df)
    assert "risk_class_3var" in result.columns
