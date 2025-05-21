import pandas as pd

def load_data():
    benin = pd.read_csv('data/Benin_clean.csv')
    togo = pd.read_csv('Togo_clean.csv')
    sierra_leone = pd.read_csv('data/sierraleone_clean.csv')

    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sierra_leone['Country'] = 'Sierra Leone'

    return pd.concat([benin, togo, sierra_leone], ignore_index=True)

def summary_table(df):
    return df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
