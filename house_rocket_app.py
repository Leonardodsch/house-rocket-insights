import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import fixed
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

def barplot(a,b, aux):
    plot = sns.barplot(x=a, y=b, data=aux, edgecolor='k', palette='Blues')
    sns.despine()
    return plot

# get data
path = 'data/df_sugestions01.csv'
path2 = 'data/df_sugestions02.csv'
path3 = 'data/df_full.csv'

data = get_data(path)
df = get_data(path2)
df1 = get_data(path3)

st.sidebar.write()
f_zipcode = st.sidebar.multiselect('Select Zipcode', data['zipcode'].unique())
f_condition = st.sidebar.multiselect('Select Condition', data['condition'].sort_values(ascending=True).unique())
f_buy = st.sidebar.multiselect('Select buy option', data['buy'].unique())
f_season = st.sidebar.multiselect('Select season', df['season'].unique())

min_price = int(df['price'].min())
max_price = int(df['price'].max())
median_price = int(df['price'].median())



st.title('House Rocket')
st.write('A House Rocket é uma empresa focada na compra e venda de imóveis, buscando avaliar e encontrar bons negócios para constituir seu portfólio e oferecer também bons'
         ' negocios para seus clientes. Diante disso foi realizada uma análise onde diversos imóveis foram explorados e avaliados buscando o que poderia se tornar uma boa oportunidade para a empresa'
        ' e alguns insights interessantes foram descobertos, algo que se tornará de extremo valor caso seja bem utilizado.'
         'Para detalhes mais técnicos e visualização do projeto completo acessar:' ' [GitHub](https://github.com/Leonardodsch/house-rocket-insights)')

st.title('Business Questions')
st.write('As tabelas são interativas e podem ser filtradas a partir das opções na barra lateral, permitindo assim que os imóveis'
         ' possam ser exibidos de acordo com a preferência.')
st.header(' Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?')
st.write(' Na primeita tabela estão os imóveis agrupados por região (zipcode), com os preços médios de cada região. Estes são avaliados juntamente com o valor'
         ' da coluna condition de cada imóvel, para assim ser feita uma sugestão de compra ou não')
st.header(' Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?')
st.write('Na segunda tabela é possivel filtrar os imóveis pela região mas também pela sazonalidade, o que permite ver as melhores opções de compra em cada estação do ano'
         ' e o valor da venda baseado nas premissas de assumidas no começo do projeto')



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

st.header('Mapa com as indicações de compra')
is_check = st.checkbox('Show Map')


if is_check:

    selected_price_range = st.slider('Select the price range', min_price, max_price, median_price)
    buy_select = st.multiselect('Buy option', df1['buy'].unique())

    if (buy_select != []):
        # select rows
        houses = df1[(df1['price'] < selected_price_range) & (df1['buy'].isin(buy_select))][['id','zipcode','price','median_price','condition', 'lat', 'long']]
        # draw map
        fig = px.scatter_mapbox(
            houses,
            lat='lat',
            lon='long',
            color="condition",
            size="price",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=10 )

        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)

    else:
        # select rows
        houses = df1[['id','zipcode','price','median_price','condition', 'lat', 'long']].copy()
        # draw map
        fig = px.scatter_mapbox(
            houses,
            lat='lat',
            lon='long',
            color="condition",
            size="price",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=10 )

        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)

st.title('Business Hypothesis')

# H1
st.header('H1: Imóveis que possuem vista para água, são 30% mais caros, na média')
st.text('Falsa! Imóveis com vista para a agua são 200% mais caros na mádia')
aux = df1[['price','waterfront']].groupby('waterfront').mean().reset_index()
fig = plt.figure(figsize=(9,3))
barplot('waterfront','price',aux)
st.pyplot(fig)

#H2
st.header('H2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média')
st.text('Falsa! Imóveis com data de construção menot do que 1955 são aproximadamente 1,6% mais baratos')
aux2 = df1[['price','yr_built']].copy()
aux2['yr_built'] = aux2['yr_built'].apply(lambda x: '<= 1955' if x <= 1955 else '> 1955')
aux = aux2[['price','yr_built']].groupby('yr_built').mean().reset_index()
fig2 = plt.figure(figsize=(9,3))
barplot('yr_built','price',aux)
st.pyplot(fig2)

# Evolution over the year
st.header('Evolution over the years')
aux = df1[['price','yr_built']].loc[df1['yr_built'] <= 1955].groupby('yr_built').mean().reset_index()
aux2 = df1[['price','yr_built']].loc[df1['yr_built'] > 1955].groupby('yr_built').mean().reset_index()

fig_ = plt.figure(figsize=(15,7))
plt.subplot(2,1,1)
barplot('yr_built','price', aux)
plt.xticks(rotation=60);
plt.title('Yr_built <= 1955')

plt.subplot(2,1,2)
barplot('yr_built','price',aux2)
plt.xticks(rotation=60);
plt.title('Yr_built > 1955')
plt.tight_layout()
st.pyplot(fig_)

#H3
st.header('H3: Imóveis sem porão possuem area total (sqrt_lot), são 50% maiores do que com porão')
st.text('Falsa! Imóveis sem porão possuem uma area total 23% maior')
aux = df1[['sqft_basement','sqft_lot']].copy()
aux['sqft_basement'] = aux['sqft_basement'].apply(lambda x: 'yes' if x != 0 else 'no')
aux1 = aux[['sqft_basement','sqft_lot']].groupby('sqft_basement').mean().reset_index()
aux1.sort_values(by='sqft_lot', ascending=True, inplace=True)
fig3 = plt.figure(figsize=(9,3))
barplot('sqft_basement','sqft_lot',aux1)
st.pyplot(fig3)

#4
st.header('H4: O crescimento do preço dos imóveis YoY ( Year over Year ) é de 10%')
st.text('Falsa O crescimento do preço dos imoveis YoY é de 2%')
aux = df1[['price','year']].loc[df1['month'] == 5].copy()
aux1 = aux[['price','year']].groupby('year').mean().reset_index()
fig4 = plt.figure(figsize=(9,3))
barplot('year','price',aux1)
st.pyplot(fig4)

#5
st.header('H5: Imóveis com 3 banheiros tem um crescimento MoM ( Month over Month ) de 15%')
st.text('Falsa! Imóveis com 3 banheiros não possuem um crescimento MoM de 15%')
aux = df1[['price','month']].loc[df1['bathrooms'] == 3].groupby(['month']).mean().reset_index()
aux['growth'] = aux['price'].pct_change()
fig5 = plt.figure(figsize=(9,3))
plt.subplot(2,1,1)
plt.plot('month','price', data=aux)
plt.ylabel('Price')
plt.subplot(2,1,2)
barplot('month','growth',aux)
st.pyplot(fig5)

#6
st.header('H6: Imóveis com 3 ou mais banheiros são 30% mais caros, na média')
st.text('Falsa! Impoveis com 3 ou mais banheiros são 100% mais caros na média')
aux = df1[['bathrooms','price']].copy()
aux['bathrooms'] = aux['bathrooms'].apply(lambda x: '>= 3' if x >=3 else '< 3')
aux1 = aux[['price','bathrooms']].groupby('bathrooms').mean().reset_index()
fig6 = plt.figure(figsize=(9,3))
barplot('bathrooms','price',aux1)
st.pyplot(fig6)

#7
st.header('H7: Imóveis com condition igual ou maior do que 4 são 40% mais caros, na média')
st.text('Falsa! Imóveis com condition igual ou maior do que 4 são 0,5% mais caros, na média')
aux = df1[['price','condition']].copy()
aux['condition'] = aux['condition'].apply(lambda x: '< 4' if x < 4 else '>= 4')
aux1 = aux[['price','condition']].groupby('condition').mean().reset_index()
fig7 = plt.figure(figsize=(9,3))
barplot('condition','price',aux1)
st.pyplot(fig7)

#8
st.header('H8: Imóveis vendidos no inverno são 30% mais baratos na média do que imóveis vendidos no verão')
st.text('Falsa! Imóveis vendidos no inverno são 4% mais baratos na média do que imóveis vendidos no verão')
aux = df1[['price','season']].loc[(df1['season'] == 'winter') | (df1['season'] == 'summer') ].copy()
aux1 = aux[['price','season']].groupby('season').mean().reset_index()
aux1.sort_values(by='price', ascending=True, inplace=True)
fig8 = plt.figure(figsize=(9,3))
barplot('season','price',aux1)
st.pyplot(fig8)

#9
st.header('H9: Imóveis com mais de 400m2 (m2_living) são 50% mais caros na media')
st.text('Falsa! Imóveis com mais de 400m2 são 230% mais caros na média')
aux = df1[['price','m2_living']].copy()
aux['m2_living'] = aux['m2_living'].apply(lambda x: '< 400' if x < 400 else '> 400')
aux1= aux[['price','m2_living']].groupby('m2_living').mean().reset_index()
fig9 = plt.figure(figsize=(9,3))
barplot('m2_living','price',aux1)
st.pyplot(fig9)

#10
st.header('H10: Imóveis com menos de 100m2 tem um crescimento Mom ( Month over Month ) de 20%')
st.text('Falsa! Imóveis com menos de 100m2 não possuem um crescimento MoM de 20%')
aux = df1[['price','month']].loc[df1['m2_living'] < 100 ].groupby('month').mean().reset_index()
aux['growth'] = aux['price'].pct_change()
fig10 = plt.figure(figsize=(9,3))
plt.subplot(2,1,1)
plt.plot('month','price', data=aux)
plt.ylabel('Price')
plt.subplot(2,1,2)
barplot('month','growth',aux)
st.pyplot(fig10)

#11
st.header('H11: Imóveis com 4 ou mais quartos são 50% mais caros, na média')
st.text('Verdadeira! Imóveis com 4 ou mais quartos são 50% mais caros, na média')
aux = df1[['bedrooms','price']].copy()
aux['bedrooms'] = aux['bedrooms'].apply(lambda x: '< 4' if x < 4 else '>= 4')
aux1= aux[['price','bedrooms']].groupby('bedrooms').mean().reset_index()
fig11 = plt.figure(figsize=(9,3))
barplot('bedrooms','price',aux1)
st.pyplot(fig11)

