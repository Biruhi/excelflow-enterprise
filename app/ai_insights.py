# =========================
# NEW PROFESSIONAL FILE:
# app/ai_insights.py
#
# IMPROVEMENTS:
# ✅ AI-style business insights
# ✅ Smart reporting
# =========================

def generate_ai_insights(df):

    insights = []

    # Top country
    top_country = (
        df.groupby("Country")["Sales"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"{top_country} generated the highest sales."
    )

    # Top department
    top_department = (
        df.groupby("Department")["Sales"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"{top_department} department has the best performance."
    )

    # Missing sales
    missing_sales = df["Sales"].isnull().sum()

    insights.append(
        f"{missing_sales} rows contain missing sales values."
    )

    return insights