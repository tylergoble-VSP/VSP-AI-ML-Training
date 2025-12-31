"""
Used in: 09_Survival_Analysis
Purpose:
    Provide utilities for survival analysis including Kaplan-Meier and Cox models.
    
Educational Context:
    Survival analysis studies time until an event occurs.
    
    Key Concepts:
    1. Survival Time: Time until event (death, failure, etc.)
    2. Censoring: Event hasn't occurred yet (still alive, still working)
    3. Survival Function: Probability of surviving past time t
    4. Hazard Function: Instantaneous risk of event at time t
    
    Methods:
    1. Kaplan-Meier: Non-parametric (no assumptions about distribution)
       - Estimates survival curve from data
       - Handles censoring naturally
    
    2. Cox Proportional Hazards: Semi-parametric regression
       - Models how covariates affect survival
       - Assumes proportional hazards (risks scale multiplicatively)
    
    Applications:
    - Medical: Patient survival, disease progression
    - Engineering: Equipment failure, reliability
    - Business: Customer churn, employee retention
"""

# Import Pandas: For DataFrame operations
import pandas as pd

# Import lifelines: Specialized library for survival analysis
# KaplanMeierFitter: Estimates survival curves non-parametrically
# CoxPHFitter: Fits Cox proportional hazards regression model
from lifelines import KaplanMeierFitter, CoxPHFitter

# Import logrank_test: Statistical test for comparing survival curves
# Tests if two groups have different survival distributions
from lifelines.statistics import logrank_test

# Import type hints
from typing import Optional


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

