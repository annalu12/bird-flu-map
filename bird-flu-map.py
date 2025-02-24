from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

# export county data with FIPS codes
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# original map and data from 
# https://www.cdc.gov/bird-flu/situation-summary/data-map-wild-birds.html
data_file = "data-table.csv"
df = pd.read_csv(data_file, dtype={"FIPS": str})
df.head()

# display as choropleth map
fig = px.choropleth(df, geojson=counties, locations='FIPS', color='Totals',
                           color_continuous_scale="Viridis",
                           range_color=(0, 30),
                           scope="usa",
                           labels={'Totals':'Totals'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()