def validate_data(df):


    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicates:")
    print(df.duplicated().sum())

    print("\nColumns:")
    print(df.columns.tolist())

    return True
