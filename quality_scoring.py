import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",      
    host="localhost",              
    port="5432"
)

query = "SELECT * FROM weather_air_quality"
df = pd.read_sql(query, conn)
conn.close()

print(df.head())
print("\nSchema Info:")
df.info()

dq_results = {}
columns_to_check = [
    "ts", "temp", "pressure", "humidity",
    "wind_speed", "wind_dir", "icon",
    "aqi_us", "main_pollutant_us", "aqi_cn", "main_pollutant_cn"
]

print("\n📊 Data Completeness Report:")
for col in columns_to_check:
    not_null_ratio = df[col].notnull().sum() / len(df)
    dq_results[col] = not_null_ratio
    print(f"✔️ {col:20}: {not_null_ratio:.2%}")

overall_completeness = sum(dq_results.values()) / len(dq_results)
print(f"\n Overall Completeness Score: {overall_completeness:.2%}")
