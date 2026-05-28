# =========================
# IMPROVED FILE:
# app/charts.py
#
# IMPROVEMENTS:
# ✅ Plotly charts
# ✅ Interactive visualizations
# =========================

import plotly.express as px


def sales_by_country_chart(df):

    grouped = (
        df.groupby("Country")["Sales"]
        .sum()
        .reset_index()
    )

    chart = px.bar(
        grouped,
        x="Country",
        y="Sales",
        title="Sales by Country"
    )

    return chart


def department_chart(df):

    grouped = (
        df.groupby("Department")["Sales"]
        .sum()
        .reset_index()
    )

    chart = px.pie(
        grouped,
        names="Department",
        values="Sales",
        title="Department Sales Distribution"
    )

    return chart