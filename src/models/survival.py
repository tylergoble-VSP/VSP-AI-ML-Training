"""
Used in: 09_Survival_Analysis
Purpose:
    Provide utilities for survival analysis including Kaplan-Meier and Cox models.
"""

import pandas as pd  # Pandas for DataFrame operations
from lifelines import KaplanMeierFitter, CoxPHFitter  # Lifelines survival analysis library
from lifelines.statistics import logrank_test  # Log-rank test for comparing survival curves
from typing import Optional  # Type hints


def fit_kaplan_meier(durations: pd.Series, events: pd.Series, label: Optional[str] = None) -> KaplanMeierFitter:
    """
    Fit a Kaplan-Meier survival curve.

    Args:
        durations: Time until event or censoring.
        events: Binary indicator (1 = event occurred, 0 = censored).
        label: Optional label for the survival curve.

    Returns:
        Fitted KaplanMeierFitter object.
    """
    # Create Kaplan-Meier fitter
    kmf = KaplanMeierFitter(label=label)

    # Fit the model to the data
    kmf.fit(durations, event_observed=events)

    return kmf


def compare_survival_curves(durations_1: pd.Series, events_1: pd.Series,
                           durations_2: pd.Series, events_2: pd.Series) -> dict:
    """
    Compare two survival curves using the log-rank test.

    Args:
        durations_1: Time data for group 1.
        events_1: Event indicators for group 1.
        durations_2: Time data for group 2.
        events_2: Event indicators for group 2.

    Returns:
        Dictionary with test results including p-value.
    """
    # Perform log-rank test
    results = logrank_test(durations_1, durations_2, events_1, events_2)

    return {
        "p_value": results.p_value,
        "test_statistic": results.test_statistic,
        "is_significant": results.p_value < 0.05
    }


def fit_cox_model(df: pd.DataFrame, duration_col: str, event_col: str, 
                  formula: Optional[str] = None) -> CoxPHFitter:
    """
    Fit a Cox Proportional Hazards model.

    Args:
        df: DataFrame with survival data and covariates.
        duration_col: Name of column containing time durations.
        event_col: Name of column containing event indicators.
        formula: Optional formula string (e.g., "age + sex"). If None, uses all columns except duration/event.

    Returns:
        Fitted CoxPHFitter object.
    """
    # Create Cox model fitter
    cph = CoxPHFitter()

    # Fit the model
    if formula:
        cph.fit(df, duration_col=duration_col, event_col=event_col, formula=formula)
    else:
        cph.fit(df, duration_col=duration_col, event_col=event_col)

    return cph

