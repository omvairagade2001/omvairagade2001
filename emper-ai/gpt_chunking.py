# gpt_chunking.py

"""
Splits job seeker dataset into smaller chunks for GPT processing.

Handles token constraints by limiting number of candidates per GPT call.

Author: Om Vairagade
"""

import pandas as pd


def chunk_job_seekers(job_seeker_df, chunk_size=15):
    """
    Splits job seeker dataframe into chunks.

    Parameters:
    - job_seeker_df: pandas DataFrame with all job seekers
    - chunk_size: max number of records per GPT input (default = 15)

    Returns:
    - List of DataFrame chunks
    """
    chunks = []
    total_rows = job_seeker_df.shape[0]

    for i in range(0, total_rows, chunk_size):
        chunk = job_seeker_df.iloc[i:i + chunk_size]
        chunks.append(chunk)

    print(f"📦 Split job seekers into {len(chunks)} chunks of ~{chunk_size} each.")
    return chunks


def chunk_to_json(chunk_df):
    """
    Converts a DataFrame chunk to JSON-friendly dict (for GPT input).

    Parameters:
    - chunk_df: a chunk of job_seeker_df

    Returns:
    - List of dicts (one per job seeker)
    """
    return chunk_df.to_dict(orient="records")


# Optional: quick test
if __name__ == "__main__":
    df = pd.read_excel("job_seekers.xlsx")
    chunks = chunk_job_seekers(df, chunk_size=15)
    print("✅ Sample chunk as JSON:")
    print(chunk_to_json(chunks[0]))
