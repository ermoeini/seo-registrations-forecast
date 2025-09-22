📊 # SEO Registrations Forecast (Shamsi Calendar)
📖 ## Description

This project is a Streamlit app for visualizing and forecasting user registrations from SEO (non-branded traffic) on a platform using the Shamsi (Solar Hijri) calendar.

It compares:

Year 1403 registrations (full year)

Year 1404 registrations (first 6 months of actual data)

Forecasted registrations for months 7–12 of 1404

The app allows you to upload a CSV file with registration data, view year-over-year comparisons, and forecast the next 6 months using different forecasting methods (linear regression, polynomial regression, exponential regression).

🚀 Usage
1. Clone the repository
git clone https://github.com/USERNAME/seo-registrations-forecast.git
cd seo-registrations-forecast

2. Create and activate a Conda environment
conda create -n seo_forecast python=3.11 -y
conda activate seo_forecast

3. Install dependencies
pip install -r requirements.txt

4. Run the app
streamlit run app.py

📂 CSV Format

Upload a CSV file in the following format:

year,month,registrations
1403,1,120
1403,2,135
1403,3,200
1403,4,180
1403,5,220
1403,6,210
1403,7,250
1403,8,270
1403,9,260
1403,10,280
1403,11,300
1403,12,290
1404,1,180
1404,2,195
1404,3,210
1404,4,205
1404,5,215
1404,6,225


year → Shamsi year (e.g., 1403, 1404)

month → Month number (1–12)

registrations → Number of SEO non-branded registrations

📈 Features

Compare full year 1403 vs. 1404

Forecast next 6 months of 1404 with multiple methods

Continuous line chart (no gaps between actual and forecast)

Trendline for 1403
