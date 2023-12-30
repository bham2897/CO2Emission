# CO2Emission
CO2 Emissions Trends Visualization Script

This Python script is designed to analyze and visualize CO2 emissions trends over time for selected countries. Using data from an Excel file, it generates line charts that depict the changes in CO2 emissions for each country across a specified time range. This script is particularly useful for environmental researchers, policy analysts, and educators interested in studying and presenting historical emissions data.

**Key Features**
1. Data Loading: The script loads CO2 emissions data from an Excel file into a pandas DataFrame.
2. Country and Year Selection:
Allows for the selection of specific countries for analysis. The default countries include India, China, the United Kingdom, the United States, and the United Arab Emirates.
Enables the selection of a specific range of years for analysis. The current setting ranges from 1900 to 2021.
3. Data Filtering: Filters the dataset to include only the selected countries and years.
4. Visualization:
Generates a line chart for each selected country, showing CO2 emissions trends over the selected years.
Customizes the plot with a title, axis labels, and a legend to enhance readability.
5. Customizable Plot Parameters:
The plot size, legend positioning, and other aesthetic parameters can be adjusted as needed.

**Usage**
Input: Replace the file path in the script with the path to your Excel file containing CO2 emissions data.
Output: The script outputs a line chart visualizing the CO2 emissions trends of the selected countries over the chosen time period.

**Requirements**
To run this script, the following Python libraries are required:
pandas: For data manipulation and analysis.
matplotlib: For creating visualizations.
