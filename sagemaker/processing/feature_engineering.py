from datetime import datetime

def feature_engineering(df):

    print("\nApplying Feature Engineering...")

    df["employee_id"] = range(1, len(df) + 1)

    df["event_time"] = datetime.utcnow().strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    return df
