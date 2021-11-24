import pandas as pd
import geopandas as gpd


def load_map():
    gdf = gpd.read_file('ukraine.json')
    gdf['region'] = gdf['NAME_1']
    return gdf.loc[:, ['region', 'geometry']]


def load_data():
    df = pd.read_csv('population_trends.csv')
    df['rate'] = df['rate'].apply(lambda x: float(x))
    df['year'] = df['year'].apply(lambda x: float(x))
    return df


if __name__ == '__main__':
    print(load_data())
