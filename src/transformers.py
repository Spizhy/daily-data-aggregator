import pandas as pd

def process_data(csv_path: str) -> pd.DataFrame:
    """Очищает и агрегирует сырые данные по дням."""
    try:
        df = pd.read_csv(csv_path)
        df['date'] = pd.to_datetime(df['date'])
        
        # Агрегация выручки и количества продаж по дням
        daily_summary = df.groupby(df['date'].dt.date).agg({
            'revenue': 'sum',
            'sales_count': 'sum'
        }).reset_index()
        
        return daily_summary
    except FileNotFoundError:
        print(f"Error: File {csv_path} not found.")
        return pd.DataFrame()
