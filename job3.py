import psycopg2 # type: ignore

conn = psycopg2.connect(
    dbname='forbes2000',
    user='postgres',
    password='root',
    host='localhost'
)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Industry (industry_id SERIAL PRIMARY KEY, industry_name VARCHAR(255) NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS Country (country_id SERIAL PRIMARY KEY, country_name VARCHAR(255) NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS Year (year_id SERIAL PRIMARY KEY, year_founded INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS Revenue (revenue_id SERIAL PRIMARY KEY, revenue_amount FLOAT NOT NULL)")

cur.execute("SELECT \"Industry\" FROM forbes")
industries_data = cur.fetchall()

cur.execute("SELECT \"Country\" FROM forbes")
countries_data = cur.fetchall()

industries = [industry[0] for industry in industries_data if industry[0] is not None]
countries = [country[0] for country in countries_data if country[0] is not None]

cur.execute("SELECT \"Year Founded\" FROM forbes")
years_data = cur.fetchall()

years_int = [int(year[0]) for year in years_data if year[0] is not None]

cur.execute("SELECT \"Revenue (Billions)\" FROM forbes")
revenues_data = cur.fetchall()

revenues_float = [float(revenue[0]) for revenue in revenues_data if revenue[0] is not None]

for industry in industries:
    cur.execute("INSERT INTO Industry (industry_name) VALUES (%s)", (industry,))

for country in countries:
    cur.execute("INSERT INTO Country (country_name) VALUES (%s)", (country,))

for year_founded in years_int:
    cur.execute("INSERT INTO Year (year_founded) VALUES (%s)", (year_founded,))

for revenue_amount in revenues_float:
    cur.execute("INSERT INTO Revenue (revenue_amount) VALUES (%s)", (revenue_amount,))

conn.commit()
cur.close()
conn.close()
