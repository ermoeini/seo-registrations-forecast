<h1>📊 SEO Registrations Forecast (Shamsi Calendar)</h1>

<h2>📖 Description</h2>
<p>
This project is a <b>Streamlit app</b> for visualizing and forecasting user registrations from SEO (non-branded traffic) on a platform using the <b>Shamsi (Solar Hijri) calendar</b>.
</p>

<p>It compares:</p>
<ul>
  <li><b>Year 1403 registrations (full year)</b></li>
  <li><b>Year 1404 registrations (first 6 months of actual data)</b></li>
  <li><b>Forecasted registrations for months 7–12 of 1404</b></li>
</ul>

<p>
The app allows you to upload a CSV file with registration data, view year-over-year comparisons, and forecast the next 6 months using different forecasting methods (linear regression, polynomial regression, exponential regression).
</p>

<hr>

<h2>🚀 Usage</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/USERNAME/seo-registrations-forecast.git
cd seo-registrations-forecast
</code></pre>

<h3>2. Create and activate a Conda environment</h3>
<pre><code>conda create -n seo_forecast python=3.11 -y
conda activate seo_forecast
</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. Run the app</h3>
<pre><code>streamlit run app.py
</code></pre>

<hr>

<h2>📂 CSV Format</h2>
<p>Upload a CSV file in the following format:</p>

<pre><code>year,month,registrations
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
</code></pre>

<ul>
  <li><b>year</b> → Shamsi year (e.g., 1403, 1404)</li>
  <li><b>month</b> → Month number (1–12)</li>
  <li><b>registrations</b> → Number of SEO non-branded registrations</li>
</ul>

<hr>

<h2>📈 Features</h2>
<ul>
  <li>Compare full year <b>1403 vs. 1404</b></li>
  <li>Forecast <b>next 6 months of 1404</b> with multiple methods</li>
</ul>
