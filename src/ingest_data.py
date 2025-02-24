import pandas as pd
import chardet
from google.cloud import bigquery
import time

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(1024))  # Read only the first 1024 bytes
        return result['encoding']

def load_data(csv_path, dataset_id, table_id):
    client = bigquery.Client(project="tribal-logic-451821-q3")
    
    # Detect encoding of CSV file
    encoding = detect_encoding(csv_path)
    if encoding == 'ascii':
        encoding = 'ISO-8859-1'  # fallback encoding

    print(f'The detected encoding is: {encoding}')
    
    df = pd.read_csv(csv_path, encoding=encoding)
    df_top_20 = df.head(20)

    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    retry_attempts = 5
    for attempt in range(retry_attempts):
        try:
            load_job = client.load_table_from_dataframe(df_top_20, table_ref, job_config=job_config)
            load_job.result()  # Wait for completion
            print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
            return
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < retry_attempts - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise

if __name__ == "__main__":
    load_data("data/data.csv", "retail_transactions", "raw_transactions")
