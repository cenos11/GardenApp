import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patheffects as pe

# SETTING DIRECTORIES FOR DATA TO BE PULLED AND STORED
directory_in = 'GardenData.csv'
directory_out = 'GardenDatabase.csv'

# SET SPRING AND FALL FROST DATES
last_frost = '2023-05-15'
first_frost = '2023-10-15'

# READING IN CSV FILE
df = pd.read_csv(directory_in)

# CONVERT FROST DATES TO DATETIME FORMAT
df['Last Frost'] = pd.to_datetime(last_frost)
df['First Frost'] = pd.to_datetime(first_frost)

# FORECASTING DATES FOR PLANTING WINDOW
df['Transplant Start'] = df['Last Frost'] - pd.to_timedelta(df['Weeks from Frost'], unit = 'W')
df['Seeding Start'] = df['Transplant Start'] - pd.to_timedelta(df['Starter Weeks'], unit = 'W')
df['First Harvest'] = df['Transplant Start'] + pd.to_timedelta(df['Maturity'], unit = 'D')
df['Last Harvest'] = df['First Frost'] + pd.to_timedelta(df['Weeks from Frost'], unit = 'W')
df['Last Transplant'] = df['Last Harvest'] - pd.to_timedelta(8, unit = 'W')
df['Last Seed'] = df['Last Transplant'] - pd.to_timedelta(df['Starter Weeks'], unit = 'W')

# CALCULATING HARVESTABLE WEEKS
df['Harvest Weeks'] = df['Last Harvest'] - df['First Harvest']
df['Harvest Weeks'] = df['Harvest Weeks']/np.timedelta64(1, 'W')
df['Harvest Weeks'] = df['Harvest Weeks'].astype(int)

# CREATING GANTT CHART PLOTS
fig, ax = plt.subplots(figsize = (12, 4))
ax.vlines(df['Last Frost'], -1, (len(df['Last Frost'])+1), \
    color = 'c', linestyles = 'dashed', linewidth = 2)
ax.vlines(df['First Frost'], -1, (len(df['Last Frost'])+1), \
    color = 'c', linestyles = 'dashed', linewidth = 2)
ax.hlines(df.index, df['Seeding Start'], df['Last Seed'], \
    color = 'red', lw = 3, capstyle = 'round', path_effects=[pe.Stroke(linewidth=5, foreground='black'), pe.Normal()])
ax.hlines(df.index, df['Transplant Start'], df['Last Transplant'], \
    color = 'yellow', lw = 3, capstyle = 'round', path_effects=[pe.Stroke(linewidth=5, foreground='black'), pe.Normal()])
ax.hlines(df['Variety'], df['First Harvest'], df['Last Harvest'], \
    color = 'green', linestyles = 'dotted', lw = 3, capstyle = 'round', path_effects=[pe.Stroke(linewidth=5, foreground='black'), pe.Normal()])


# FORMATTING AXES
ax.set_xlim([dt.date(2023, 1, 1), dt.date(2024, 1, 1)])
ax.set_ylim(-0.5, (len(df['Variety'])-0.5))
ax.set_ylabel('Crops', fontsize = 'large', fontweight = 'bold')
ax.set_xlabel('Date', fontsize = 'large', fontweight = 'bold')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.tick_params(axis='x', which='minor', bottom=False)

plt.grid(axis = 'x')

# SHOW PLOT
plt.show()

# OUTPUTS
df.to_csv(directory_out)
print(df)