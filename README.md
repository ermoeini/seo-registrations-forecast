# seo-registrations-forecast
This project is a Streamlit app for visualizing and forecasting user registrations from SEO (non-branded traffic) on a platform using the Shamsi (Solar Hijri) calendar.

It compares:

Year 1403 registrations (full year)

Year 1404 registrations (first 6 months of actual data)

Forecasted registrations for months 7–12 of 1404

The app allows you to upload a CSV file with registration data, view year-over-year comparisons, and forecast the next 6 months using different forecasting methods (linear regression, polynomial regression, exponential regression).

🚀 Usage

Clone the repository:

git clone https://github.com/USERNAME/seo-registrations-forecast.git
cd seo-registrations-forecast


Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Upload a CSV file with the following format:

year,month,registrations
1403,1,120
1403,2,135
...
1404,1,180
1404,2,195


year: Shamsi year (e.g., 1403, 1404)

month: Month number (1–12)

registrations: Number of SEO non-branded registrations

View:

Line chart comparing 1403 vs 1404

Forecast for months 7–12 of 1404 based on the selected forecasting method
