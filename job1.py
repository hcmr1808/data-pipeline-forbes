import pandas as pd # type: ignore
import os

url = "https://raw.githubusercontent.com/hcmr1808/data-pipeline-forbes/master/Forbes_2000_top_company_CLNQ11.csv"

df = pd.read_csv(url)

df.to_csv(f'{os.getcwd()}/staging/forbes_2000_empresas.csv', index=False)