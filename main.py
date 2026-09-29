import json
import os
from src.transformers import process_data
from src.report_builder import generate_pdf
# from src.mailer import send_email (заглушка для импорта)

def load_config():
    with open('config/settings.json', 'r') as f:
        return json.load(f)

def main():
    print("Starting daily aggregation pipeline...")
    config = load_config()
    
    # 1. Трансформация данных
    summary_df = process_data(config['csv_input_path'])
    
    # 2. Генерация отчета
    generate_pdf(summary_df, config['pdf_output_path'])
    
    # 3. Отправка email (заглушенная логика)
    # send_email(config['pdf_output_path'], config['email'])
    print("Pipeline finished successfully.")

if __name__ == "__main__":
    # Создание тестовых данных при первом запуске
    if not os.path.exists("./data/raw/sales.csv"):
        os.makedirs("./data/raw", exist_ok=True)
        with open("./data/raw/sales.csv", "w") as f:
            f.write("date,revenue,sales_count\n2023-10-01,1500,34\n2023-10-02,2300,56")
            
    main()
