import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf(df: pd.DataFrame, output_path: str):
    """Строит график и встраивает его в PDF отчет."""
    if df.empty:
        print("No data to generate report.")
        return

    # Генерация графика
    chart_path = "temp_chart.png"
    plt.figure(figsize=(8, 4))
    plt.plot(df['date'], df['revenue'], marker='o', color='b', label='Revenue')
    plt.title('Daily Revenue')
    plt.xlabel('Date')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    # Сборка PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Automated Daily Performance Report")
    
    # Вставка графика
    c.drawImage(chart_path, 50, 400, width=500, height=250)
    
    # Текстовая сводка
    c.setFont("Helvetica", 12)
    total_revenue = df['revenue'].sum()
    c.drawString(50, 350, f"Total Revenue for period: ${total_revenue:,.2f}")
    c.drawString(50, 330, f"Total Sales Count: {df['sales_count'].sum()}")
    
    c.save()
    os.remove(chart_path)
    print(f"Report saved to {output_path}")
