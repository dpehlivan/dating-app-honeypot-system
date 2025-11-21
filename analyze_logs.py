df = pd.read_csv("logs.csv")
df['count'] = 1
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.groupby(df.timestamp.dt.hour)['count'].sum().plot()
