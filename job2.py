import pandas as pd # type: ignore
from sqlalchemy import create_engine # type: ignore
import os

data = pd.read_csv(f'{os.getcwd()}/forbes_2000_empresas.csv')


engine = create_engine('postgresql://postgres:root@localhost:5432/forbes2000')

data.to_sql('forbes', engine, if_exists='replace', index=False)
