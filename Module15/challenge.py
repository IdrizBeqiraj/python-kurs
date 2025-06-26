import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('archive/weather_tokyo_data.csv')

df['date'] = pd.to_datetime(df['date'])

average_temp = df['temperature'].mean()
print("\nTask 1a: Average Temperature for Entire Dataset")
print(f"{average_temp:.2f}°C")

df['month'] = df['date'].dt.month
monthly_avg = df.groupby('month')['temperature'].mean()

print("\nTask 2a: Monthly Average Temperatures")
print(monthly_avg.round(2))

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title('Monthly Average Temperature in Tokyo')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


hottest_day = df.loc[df['temperature'].idxmax()]
coldest_day = df.loc[df['temperature'].idxmin()]

print("\nTask 3a: Hottest Day")
print(hottest_day)
print("\nColdest Day")
print(coldest_day)

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['temperature'], color='royalblue', alpha=0.7)
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['season'] = df['month'].apply(get_season)
seasonal_avg = df.groupby('season')['temperature'].mean().reindex(['Winter', 'Spring', 'Summer', 'Fall'])

print("\nTask 4b: Seasonal Average Temperatures")
print(seasonal_avg.round(2))

plt.figure(figsize=(8, 5))
seasonal_avg.plot(kind='bar', color=['lightblue', 'lightgreen', 'salmon', 'gold'])
plt.title('Seasonal Average Temperature in Tokyo')
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()