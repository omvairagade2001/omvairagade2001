import pandas as pd

# Load recruiters
def load_recruiters(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f"✅ Loaded {len(df)} recruiters from {file_path}")
        return df
    except Exception as e:
        print(f"❌ Error loading recruiters data: {e}")
        return None

# Preprocess recruiters
def preprocess_recruiters(df):
    df['Required Skills'] = df['Required Skills'].fillna('').str.lower()
    df['Custom Requirements'] = df['Custom Requirements'].fillna('')
    return df

# Load job seekers
def load_job_seekers(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f"✅ Loaded {len(df)} job seekers from {file_path}")
        return df
    except Exception as e:
        print(f"❌ Error loading job seekers data: {e}")
        return None

# Preprocess job seekers
def preprocess_job_seekers(df):
    df['Skills'] = df['Skills'].fillna('').str.lower()
    df['Preferred Job Type'] = df['Preferred Job Type'].fillna('').str.lower()
    df['Education Level'] = df['Education Level'].fillna('').str.upper()
    df['Resume Summary'] = df['Resume Summary'].fillna('')
    df['Contact Email'] = df['Contact Email'].fillna('')
    return df

if __name__ == "__main__":
    recruiters_path = "recruiters.xlsx"
    seekers_path = "job_seekers.xlsx"

    recruiters_df = load_recruiters(recruiters_path)
    seekers_df = load_job_seekers(seekers_path)

    if recruiters_df is not None:
        recruiters_df = preprocess_recruiters(recruiters_df)
        print(recruiters_df.head())

    if seekers_df is not None:
        seekers_df = preprocess_job_seekers(seekers_df)
        print(seekers_df.head())


