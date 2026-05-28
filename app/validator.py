# =========================
# IMPROVED FILE:
# app/validator.py
#
# IMPROVEMENTS:
# ✅ Email validation
# ✅ Invalid email detection
# ✅ Better reporting
# =========================

import re


def validate_emails(df):

    invalid_emails = 0

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    for email in df["Email"]:

        if not re.match(pattern, str(email)):
            invalid_emails += 1

    return invalid_emails


def validate_data(df):

    report = {

        "missing_values":
        df.isnull().sum().to_dict(),

        "duplicate_rows":
        int(df.duplicated().sum()),

        "total_rows":
        len(df),

        "invalid_emails":
        validate_emails(df)
    }

    return report