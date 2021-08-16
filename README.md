 - Link para o notebook através do nbviewer (Recomendado para uma melhor visualização): https://nbviewer.jupyter.org/github/Leonardodsch/house-rocket-insights/blob/main/house_rocket_insights.ipynb
 
# House Rocket Insights


Disclaimer: O Contexto a seguir, é completamente fictício, a empresa, o contexto, o CEO, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam no projeto do site https://sejaumdatascientist.com/.

<p align="center">
  <img width="1100" height="450" src="https://user-images.githubusercontent.com/76128123/111823321-93868900-88c3-11eb-9bf2-d52afd1ca128.png" />
</p>


## Contexto de negócio

A House Rocket é uma empresa focada na compra e venda de imóveis, buscando avaliar e encontrar bons negócios para constituir seu portfólio e oferecer também bons negocios para seus clientes. O CEO da House Rocket gostaria de maximizar a receita da empresa encontrando boas oportunidades de negócio.

A principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita. Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores e a localização e o período do ano também podem influenciar os preços.

Diante disso foi realizada uma análise onde diversos imóveis foram explorados e avaliados buscando o que poderia se tornar uma boa oportunidade para a empresa e alguns insights interessantes foram descobertos, algo que se tornará de extremo valor caso seja bem utilizado. Nenhum algoritimo de machine learning foi utilizado, os insights e recomendações forma feitas utilizando apenas a análise e exploração dos dados. Nesse processo buscou-se responder as perguntas abaixo. 

 1. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?
 2. Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

## Dados
O conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. Esse é o link: https://www.kaggle.com/harlfoxem/housesalesprediction.
Esse conjunto de dados contém casas vendidas entre Maio de 2014 e Maio de 2015. o dataset contém os seguintes atributos :

**id** - Numeração única de identificação de cada imóvel

**date** - Data da venda do imóvel

**price** - Preço da venda do imóvel

**bedrooms** - Numero de quartos 

**bathrooms** - Número de banheiros. 0.5 indica um banheiro sem chuveiro

**sqft_living** - Medida (em pés quadrado) do espaço interior dos imóveis

**sqft_lot** - Medida (em pés quadrado) do espaço total do terreno

**floors** - Numero de andares

**waterfront** - Variável que indica a presença ou não de vista para água (0 = não e 1 = sim)

**view** - Um índice de 0 a 4 que indica a qualidade da vista do imóvel. Onde: 0 = baixa 4 = alta

**condition** - Um índice de 1 a 5 que indica a condição do imóvel. Onde: 1 = baixo, 5 = alta

**grade** - Um índice de 1 a 13 que indica a construção e o design do imóvel. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta

**sqft_above** - Medida (em pés quadrado) do espaço interior dos comodos que estão acima do nível do solo

**sqft_basement** - Medida (em pés quadrado) do espaço interior dos comodos que estão abaixo do nível do solo

**yr_built** - Ano de construção do imóvel

**yr_renovated** - Ano de reforma do imóvel

**zipcode** - Região onde cada imóvel se encontra

**lat** - Latitude

**long** - Longitude

**sqft_living15** - Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo

**sqft_lot15** - Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo

## Premissas
Para execução do projeto foram assumidas algumas premissas, tais como:
1. Os outliers encontrados na variável 'price' foram analisados e como se encontravam em pequena quantidade não se mostraram um fator que atrapalhasse o valor das médias e medianas calculadas e por acabaram sendo incluidos nos calculos;
2. A culuna 'price' foi considerada como o valor atual do imóvel, como se ele estivesse disponivel a venda.
3. As colunas sqft_livining15 e sqft_lot15 não foram consideradas duranta a analise e exploração dos dados.

## Planejamento da solução
1. Coleta dos dados
2. Entendimento do negócio e problemas e serem resolvidos
3. Limpeza e tratamento dos dados
4. Exploração dos dados buscando responder as perguntas de negócio

   -- Agrupar os imóveis por região ( zipcode ).
   
   -- Dentro de cada região, eu vou encontrar a mediana do preço do imóvel.
   
   -- Sugerir os imóveis que estão abaixo do preço mediano da região e que estejam e boas condições.
   
   -- Agrupar os imóveis por região ( zipcode ) e por sazonalidade ( Summer, Winter ).
   
   -- Dentro de cada região e sazonalidade, calcular a mediana do preco.
   
   -- Condições de venda:
   
     	- Se o preço da compra for maior que a mediana da região + sazonalidade.
            O preço da venda será igual ao preço da compra + 10%
	    
      	- Se o preço da compra for menor que a mediana da região + sazonalidade.
	    O preço da venda será igual ao preço da compra + 30%
            
5. Criação de hipóteses para geração de insights
6. Resultados obtidos
7. Criação do web app usando streamlit com o demonstrativo dos resultados
8. Conclusão

## Melhores insights
Os insights podem ajudar o time de negócios na tomada de decisão, insights valiosos podem fazer a diferença entre fazer um bom negócio ou não. Diante disso alguns insights econtrados a partir da analise e exploração dos dados foram:

**1. Imóveis com vista para a água são 200% mais caros na média**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129404439-71465834-7bb4-4e8d-9ae4-f7ae44b1a6d3.png" />
</p>


**2. Imóveis com data de construção menor do que 1955 são aproximadamente 1,6% mais baratos**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129404634-5a9904b8-7d70-427b-be45-6e5d695fae77.png" />
</p>

**3. Imóveis com 3 ou mais banheiros são 100% mais caros na média**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129404834-1fb89c8d-1e05-4d19-bca0-5ffacf8e5a89.png" />
</p>

**4. Imóveis com condition igual ou maior do que 4 são 0,5% mais caros, na média**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129404973-06c96bcf-273f-4b8c-b955-ab3c7eedd624.png" />
</p>

**5. Imóveis sem porão possuem uma area total 23% maior**

<p align="center">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/129405079-fb696338-f693-4467-a5ee-3c1509c1b2ff.png" />
</p>


## Resultados

Após toda a exploração e análise feita e seguindo as regra de negócio de venda definidas, os resultados finaceiros foram os seguintes:

O lucro total com a venda dos imóveis que foram recomendados para compra a partir do mediana de preço de cada região e de condoção foi de $ 376.310.918.5

Os resultdos considerando a variavel mediana por região e a estação do ano foram os seguintes:

A soma do lucro por estação do ano foi de:

![image](https://user-images.githubusercontent.com/76128123/111724241-a9ed0000-8843-11eb-9fda-497b12c5f9eb.png)

<p align="left">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/76128123/111724105-6b574580-8843-11eb-8655-7e6bfdaab104.png"/>
</p>


Considerando a soma total para todas as estações temos o valor de $ 1.976.821.731.6

# Conclusões

Após buscar um entedimento do negócio, explorar e analisar os dados e partindo das perguntas feitas pelo CEO, foi possivel buscar as soluções a partir das premissas criadas e
obter insights, através de uma analise exploratória, que podem ajudar o time de negócios a tomar melhores decisões sobre quais imóveis comprar. Os resultados financeiros encontrados são decorrencia do estudo e entendimento dos dados e podem ser maximizados caso esse estudo seja aplicado em todas as tomadas de decisão da empresa. 

Como próximos passos, seria possivel explorar ainda mais o conjunto de dados para obtenção de outros insights que pudessem ser relevantes de alguma forma. Outra abordagem seria trabalhar esses dados para serem utilizados em algoritimos de machine learning que possam prever por qual valor cada imóvel deveria ser vendido, garantindo assim um resultado mais acertivo e que possa trazer um retorno positivo ainda maior para a empresa.

De uma forma geral as perguntas feitas pelo CEO puderam ser respondidas e diversos insights foram descobertos que podem se tornar algo de valor em futuras decisões tomadas pela House Rocket. 

