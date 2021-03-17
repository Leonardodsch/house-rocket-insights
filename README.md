# House Rocket Insights


Disclaimer: O Contexto a seguir, é completamente fictício, a empresa, o contexto, o CEO, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam no projeto do site https://sejaumdatascientist.com/.

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
7. Conclusão

## Melhores insights
Os insights podem ajudar o time de negócios na tomada de decisão, insights valiosos podem fazer a diferença entre fazer um bom negócio ou não. Diante disso alguns insights econtrados a partir da analise e exploração dos dados foram:
1. Imóveis com vista para a água são 200% mais caros na média
2. Imóveis com data de construção menor do que 1955 são aproximadamente 1,6% mais baratos
3. Imóveis com 3 ou mais banheiros são 100% mais caros na média
4. Imóveis com condition igual ou maior do que 4 são 0,5% mais caros, na média
5. Imóveis sem porão possuem uma area total 23% maior

## Resultados







