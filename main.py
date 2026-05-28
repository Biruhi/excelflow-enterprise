# =========================
# FILE: main.py
# =========================

import pandas as pd

from app.cleaner import clean_data
from app.validator import validate_data
from app.formatter import format_excel
from app.analytics import generate_analytics

INPUT_FILE = "uploads/enterprise_sales_data.xlsx"

OUTPUT_FILE = "outputs/cleaned_sales_data.xlsx"

# Read Excel
df = pd.read_excel(INPUT_FILE)

# Validation
report = validate_data(df)

print("\n===== VALIDATION REPORT =====")
print(report)

# Cleaning
df_cleaned = clean_data(df)

# Analytics
analytics = generate_analytics(df_cleaned)

print("\n===== ANALYTICS =====")
print(analytics)

# Save
df_cleaned.to_excel(
    OUTPUT_FILE,
    index=False
)

# Format
format_excel(OUTPUT_FILE)

print("\n✅ ExcelFlow Enterprise completed!")
print(f"📁 Output saved to: {OUTPUT_FILE}")