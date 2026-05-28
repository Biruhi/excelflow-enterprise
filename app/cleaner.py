# =========================
# IMPROVED FILE:
# app/cleaner.py
#
# IMPROVEMENTS:
# ✅ Configurable cleaning
# ✅ Remove missing Sales
# ✅ Remove missing Country
# ✅ Better enterprise cleaning
# =========================

import pandas as pd


def clean_data(
    df,
    remove_duplicates=True,
    remove_missing_sales=True,
    remove_missing_country=True
):

    # Remove duplicates
    if remove_duplicates:
        df = df.drop_duplicates()

    # Remove fully empty rows
    df = df.dropna(how="all")

    # Remove missing Sales
    if remove_missing_sales:
        df = df.dropna(subset=["Sales"])

    # Remove missing Country
    if remove_missing_country:
        df = df.dropna(subset=["Country"])

    # Clean column names
    df.columns = df.columns.str.strip()

    # Remove extra spaces
    df = df.apply(
        lambda col: col.str.strip()
        if col.dtype == "object"
        else col
    )

    return df