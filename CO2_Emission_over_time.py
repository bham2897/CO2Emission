import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a pandas DataFrame
df = pd.read_excel('/Users/divya/Downloads/owidco2data_2.xlsx', sheet_name='Sheet1')

# Select specific countries and years
selected_countries = ['India', 'China', 'United Kingdom', 'United States', 'United Arab Emirates']
selected_years = range(1900, 2022)

# Filter the dataset for selected countries and years
co2_trends_data = df[(df['country'].isin(selected_countries)) & (df['year'].isin(selected_years))]

# Plotting the line chart
plt.figure(figsize=(12, 8))

# Iterate through selected countries and plot a line for each
for country in selected_countries:
    country_data = co2_trends_data[co2_trends_data['country'] == country]
    plt.plot(country_data['year'], country_data['co2'], label=country)

# Adding title and labels
plt.title("CO2 Emissions Trends Over Time")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")

# Adjust legend parameters
plt.legend(loc='upper left', bbox_to_anchor=(0, 1), title='Countries', title_fontsize='12')

# Display the plot
plt.show()
