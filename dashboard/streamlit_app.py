# =========================
# IMPROVED FILE:
# dashboard/streamlit_app.py
#
# IMPROVEMENTS:
# ✅ Multi-file upload
# ✅ Sidebar settings
# ✅ KPI cards
# ✅ Tabs UI
# ✅ AI insights
# ✅ Analytics
# ✅ Interactive charts
# ✅ Better UX
# =========================

import sys
import os




sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

os.makedirs("outputs", exist_ok=True)

import streamlit as st
import pandas as pd

from app.cleaner import clean_data
from app.validator import validate_data
from app.analytics import generate_analytics
from app.ai_insights import generate_ai_insights

from app.charts import (
    sales_by_country_chart,
    department_chart
)

from app.formatter import format_excel
from app.logger import log_message


# PAGE CONFIG
st.set_page_config(
    page_title="ExcelFlow Enterprise",
    layout="wide"
)

st.title("📊 ExcelFlow Enterprise")


# SIDEBAR
st.sidebar.title("⚙ Settings")

uploaded_files = st.sidebar.file_uploader(
    "Upload Excel Files",
    type=["xlsx"],
    accept_multiple_files=True
)

remove_duplicates = st.sidebar.checkbox(
    "Remove Duplicates",
    value=True
)

remove_missing_sales = st.sidebar.checkbox(
    "Remove Missing Sales",
    value=True
)

remove_missing_country = st.sidebar.checkbox(
    "Remove Missing Country",
    value=True
)


# MAIN APP
if uploaded_files:

    for uploaded_file in uploaded_files:

        try:

            st.header(f"📁 {uploaded_file.name}")

            df = pd.read_excel(uploaded_file)

            report = validate_data(df)

            df_cleaned = clean_data(
                df,
                remove_duplicates,
                remove_missing_sales,
                remove_missing_country
            )

            analytics = generate_analytics(
                df_cleaned
            )

            insights = generate_ai_insights(
                df_cleaned
            )

            output_file = (
                f"outputs/cleaned_{uploaded_file.name}"
            )

            df_cleaned.to_excel(
                output_file,
                index=False
            )

            format_excel(output_file)

            # KPI METRICS
            st.subheader("📌 KPI Metrics")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Rows",
                report["total_rows"]
            )

            col2.metric(
                "Duplicate Rows",
                report["duplicate_rows"]
            )

            col3.metric(
                "Missing Sales",
                report["missing_values"]["Sales"]
            )

            col4.metric(
                "Invalid Emails",
                report["invalid_emails"]
            )

            # TABS
            tab1, tab2, tab3, tab4 = st.tabs([
                "📄 Original Data",
                "🧹 Cleaned Data",
                "📊 Analytics",
                "⬇ Downloads"
            ])

            # ORIGINAL DATA
            with tab1:

                st.dataframe(df)

                st.subheader(
                    "✅ Validation Report"
                )

                st.json(report)

            # CLEANED DATA
            with tab2:

                st.dataframe(df_cleaned)

            # ANALYTICS
            with tab3:

                st.subheader("📈 Analytics")

                st.write(analytics)

                st.subheader("🤖 AI Insights")

                for insight in insights:

                    st.success(insight)

                chart1 = sales_by_country_chart(
                    df_cleaned
                )

                st.plotly_chart(
                    chart1,
                    use_container_width=True
                )

                chart2 = department_chart(
                    df_cleaned
                )

                st.plotly_chart(
                    chart2,
                    use_container_width=True
                )

            # DOWNLOADS
            with tab4:

                with open(
                    output_file,
                    "rb"
                ) as file:

                    st.download_button(
                        label="⬇ Download Cleaned Excel",
                        data=file,
                        file_name=f"cleaned_{uploaded_file.name}"
                    )

        except Exception as e:

            st.error(f"Error: {e}")