# src/report.py

import pandas as pd
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Paths (assumes running from project root)
forecast_csv = "data/forecast_results.csv"
load_csv = "data/load_data.csv"
forecast_plot = "outputs/forecast_plot.png"
usage_plot = "outputs/usage_plot.png"
output_pdf = "outputs/load_summary_report.pdf"

# === Load and Clean Forecast Data ===
df_forecast = pd.read_csv(forecast_csv)
df_forecast = df_forecast[['timestamp', 'usage_kwh', 'forecast', 'anomaly', 'load_factor']]  # pick key columns
df_forecast = df_forecast.round(2)

# === Load and Clean Raw Data ===
df_load = pd.read_csv(load_csv)
df_load = df_load.round(2)

# === Build tables (first 10 rows) ===
forecast_table_data = [df_forecast.columns.tolist()] + df_forecast.head(10).values.tolist()
load_table_data = [df_load.columns.tolist()] + df_load.head(10).values.tolist()

# === PDF Setup ===
doc = SimpleDocTemplate(output_pdf, pagesize=LETTER)
styles = getSampleStyleSheet()
elements = []

# === Forecast Section ===
elements.append(Paragraph("Energy Load Forecasting and Anomaly Detection Report", styles['Title']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("Forecast Results (First 10 rows)", styles['Heading2']))
forecast_table = Table(forecast_table_data)
forecast_table._argW = [90] * len(forecast_table_data[0])  # adjust width to fit on page
forecast_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
    ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
]))
elements.append(forecast_table)
elements.append(Spacer(1, 10))

elements.append(Paragraph(
    "This table summarizes the forecasted energy usage based on a 24-hour moving average. "
    "It includes calculated anomalies and load factor, which help identify risk patterns in load behavior.",
    styles['BodyText']
))
elements.append(Spacer(1, 12))

elements.append(Paragraph("Forecast Plot", styles['Heading3']))
elements.append(Image(forecast_plot, width=400, height=200))
elements.append(Spacer(1, 24))

# === Raw Load Data Section ===
elements.append(Paragraph("Raw Load Data (First 10 rows)", styles['Heading2']))
load_table = Table(load_table_data)
load_table._argW = [90] * len(load_table_data[0])
load_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 7),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
    ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
]))
elements.append(load_table)
elements.append(Spacer(1, 10))

elements.append(Paragraph(
    "This table shows the original simulated energy usage and temperature data that feeds the forecasting model. "
    "It reflects hourly values across a 72-hour period, representing real-time utility monitoring.",
    styles['BodyText']
))
elements.append(Spacer(1, 12))

elements.append(Paragraph("Usage Plot", styles['Heading3']))
elements.append(Image(usage_plot, width=400, height=200))
elements.append(Spacer(1, 24))

# === Build PDF ===
doc.build(elements)
print(f"✅ PDF generated at: {output_pdf}")

