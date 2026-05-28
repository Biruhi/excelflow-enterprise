# =========================
# NEW PROFESSIONAL FILE:
# app/analytics.py
#
# IMPROVEMENTS:
# ✅ Business analytics
# ✅ KPI generation
# =========================

def generate_analytics(df):

    analytics = {

        "total_sales":
        float(df["Sales"].sum()),

        "average_sales":
        float(df["Sales"].mean()),

        "highest_sales":
        float(df["Sales"].max()),

        "top_country":
        str(df["Country"].mode()[0]),

        "top_department":
        str(df["Department"].mode()[0])
    }

    return analytics