import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

# get data
path='data/df_sugestions01.csv'
path2 = 'data/df_sugestions02.csv'

data = get_data(path)
df = get_data(path2)

f_zipcode = st.sidebar.multiselect('Select Zipcode', data['zipcode'].unique())
f_condition = st.sidebar.multiselect('Select Condition', data['condition'].sort_values(ascending=True).unique())
f_buy = st.sidebar.multiselect('Select buy option', data['buy'].unique())
f_season = st.sidebar.multiselect('Select season', df['season'].unique())

min_price = df['price'].min()
max_price = df['price'].max()
#sorted_unique_price = sorted(twsdata.Price.unique())
selected_price_range = st.sidebar.slider('Select the price range', min_price, max_price, 1.0)
st.write('Range Values', selected_price_range)

st.title('Buy suggestions')

if (f_zipcode != []) & (f_condition == []) & (f_buy == []) & (f_season == []):
    st.write(data.loc[data['zipcode'].isin(f_zipcode)])
    st.write(df.loc[(df['zipcode'].isin(f_zipcode))])

elif (f_condition != []) & (f_zipcode != []) & (f_buy != []) & (f_season != []):
    st.write(data.loc[(data['condition'].isin(f_condition)) & (data['zipcode'].isin(f_zipcode)) & (data['buy'].isin(f_buy))])
    st.write(df.loc[(df['season'].isin(f_season)) & (df['zipcode'].isin(f_zipcode))])

elif (f_condition != []) & (f_zipcode == []) & (f_buy == []) & (f_season == []):
    st.write(data.loc[data['condition'].isin(f_condition)])
    st.dataframe(df)

elif (f_buy != []) & (f_zipcode == []) & (f_condition == []) & (f_season == []):
    st.write(data.loc[data['buy'].isin(f_buy)])
    st.dataframe(df)

elif (f_condition != []) & (f_zipcode != []) & (f_buy == []) & (f_season != []):
    st.write(data.loc[(data['condition'].isin(f_condition)) & (data['zipcode'].isin(f_zipcode))])
    st.write(df.loc[(df['season'].isin(f_season)) & (df['zipcode'].isin(f_zipcode))])

elif (f_condition == []) & (f_zipcode != []) & (f_buy != []) & (f_season == []):
    st.write(data.loc[(data['zipcode'].isin(f_zipcode)) & (data['buy'].isin(f_buy))])
    st.write(df.loc[(df['zipcode'].isin(f_zipcode))])

elif (f_season != []) & (f_zipcode == []) & (f_buy == []) & (f_condition == []):
    st.dataframe(data, height=400, width=700)
    st.write(df.loc[(df['season'].isin(f_season))])

elif (f_season != []) & (f_zipcode == []) & (f_buy != []) & (f_condition == []):
    st.write(data.loc[data['buy'].isin(f_buy)])
    st.write(df.loc[df['season'].isin(f_season)])

elif (f_season != []) & (f_zipcode == []) & (f_buy == []) & (f_condition != []):
    st.write(data.loc[data['condition'].isin(f_condition)])
    st.write(df.loc[df['season'].isin(f_season)])

elif (f_season != []) & (f_zipcode == []) & (f_buy != []) & (f_condition != []):
    st.write(data.loc[data['condition'].isin(f_condition) & (data['buy'].isin(f_buy))])
    st.write(df.loc[df['season'].isin(f_season)])

elif (f_zipcode != []) & (f_condition == []) & (f_buy == []) & (f_season != []):
    st.write(data.loc[data['zipcode'].isin(f_zipcode)])
    st.write(df.loc[(df['season'].isin(f_season)) & (df['zipcode'].isin(f_zipcode))])

elif (f_condition == []) & (f_zipcode != []) & (f_buy != []) & (f_season != []):
    st.write(data.loc[(data['zipcode'].isin(f_zipcode)) & (data['buy'].isin(f_buy))])
    st.write(df.loc[(df['season'].isin(f_season)) & (df['zipcode'].isin(f_zipcode))])

elif (f_condition != []) & (f_zipcode != []) & (f_buy == []) & (f_season == []):
    st.write(data.loc[(data['condition'].isin(f_condition)) & (data['zipcode'].isin(f_zipcode))])
    st.write(df.loc[(df['zipcode'].isin(f_zipcode))])

elif (f_condition != []) & (f_zipcode != []) & (f_buy != []) & (f_season == []):
    st.write(data.loc[(data['condition'].isin(f_condition)) & (data['zipcode'].isin(f_zipcode)) & (data['buy'].isin(f_buy))])
    st.write(df.loc[(df['zipcode'].isin(f_zipcode))])

else:
    data = data.copy()
    df = df.copy()
    st.dataframe(data, height=400, width=700)
    st.dataframe(df)
