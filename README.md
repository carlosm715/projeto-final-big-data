# projeto-final-big-data
Projeto Final Big Data FIA

Esse projeto tem como objetivo realizar as pré tratativas dos dados para poder gerar os três domínios de dados
para o projeto: clima, calendário e vôos.

Nele também temos o compilado de hql que utilizamos para realizar as tratativas necessárias para conseguir gerar as tabelas
únicas para podermos aplicar a parte de datascience de forma mais fácil.

Nos pacotes de tratamento de dados, temos código do tratamento de dados dividido por domínio.

No pacote tratamentodedados/scripts, temos os hql utilizados.

No pacote datascience, temo as duas tentativas principais de treinamento de modelo, uma sem a parte de seleção de features
E sem utilizar algumas dummies, a segunda, a que usamos no trabalho como case para a apresentação.

Também no pacote vôos, temos a antiga base que estava sendo utilizada, recuperada pelo kaggle e que fizemos algumas poucas
análises em cima, quando decidimos buscar as bases oficiais da ANAC. E também a análise de cidades com aeroportos que
utilizamos para realizar as chamadas na API de feriados.