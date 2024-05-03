# PROJETO EM DESENVOLVIMENTO

## 1. Descrição geral do problema 
 A Dimob é uma Declaração de Informações sobre Atividades Imobiliárias obrigatória, que deve ser entregue anualmente à Receita Federal. Ela deve ser declarada através de um programa próprio da Receita Federal, disponibilizado no portal do GOV, podendo as informações serem preenchidas manualmente ou através de um arquivo no formato txt, com um layout pré-determinado pelo programa. 
Dentro da empresa que trabalho a locação dos imóveis fica sobre responsabilidade, atualmente, de 5 imobiliárias, que juntas administram um total de 16 dos nossos empreendimentos, em que cada um conta com uma variedade de apartamentos. 
Objetivo: utilizar a linguagem python, para criar o arquivo txt no formato estabelecido pela Receita Federal e, fazer a importação dele.

## 2. Obtendo os dados
Como os dados vem de imobiliárias diferentes, foi desenvolvido duas maneiras de coletar as informações necessárias de acordo com o que é fornecido pelas imobiliárias: em PDF ou em formato txt. Visando a padronização de entrada no código python, fiz a conversão dos arquivos pra o formato JSON. E para converter os PDF's recebidos em arquivos JSON, foi utilizado o Google Document IA. Já para a padronização dos arquivos txt, estes foram importados no excel e utilizado VBA para a extração dos dados e gerar os arquivos JSON.
## 3. Layout exigido pelo programa da Dimob.
Dentro do programa da Dimob existe uma seção de ajuda destinada utilização do 
programa bem como uma descrição completa do layout exigido para fazer a importação, 
vou abordar apenas os principais tópicos para a demonstração de como o código 
funciona.

CONVENÇÕES DE FORMATO E TAMANHO DOS CAMPOS
Organização: Sequencial ASCII de Hex 20 a Hex 7E;
Delimitadores de registro (EOL): Hex 0D + Hex 0A.
Tamanho de registro: variável.

Características dos registros: conforme leiaute.
Nome do arquivo: nome válido de arquivo conforme definição MS-DOS, com extensão 
TXT.
Declarações gravadas para a RFB pela Dimob, também são importadas pelo programa.
Branco(s) - Caractere ou sequência de caracteres Hexadecimal 20, ASCII 32.
Zero(s) - caractere ou sequência de caracteres Hexadecimal 30, ASCII 48.
R$ - Campo numérico de 14 posições, onde as 12 primeiras posições são a parte inteira 
com zeros à esquerda; e as 2 últimas posições são a parte decimal com zeros à direita. Se 
vazio, preencher com zeros. Somente aceita valor maior ou igual a zero
DATA - Campo do tipo Data, com o formato DDMMAAAA. Período válido para Ficha 
Locação: entre 1950 e ano-calendário declarado. Período válido para Ficha Incorporação 
e Ficha Intermediação: ano-calendário declarado.
ANO - Campo numérico, com 4 posições. Válidos 2005 a 2010.
X - Campo alfanumérico com tamanho especificado na Descrição, alinhado à esquerda 
com brancos à direita.
N - Campo numérico com tamanho especificado na Descrição, alinhado à direita, com 
zeros à esquerda. Se vazio, preencher com zeros.
CPF - Campo numérico com 11 posições. CPF válido.
CNPJ - Campo numérico com 14 posições.
CPF/CNPJ - Campo numérico com 14 posições, se CNPJ. Com 11 posições, alinhado à 
esquerda com brancos à direita, se CPF.
CPF/CNPJ 2 - Campo alfanumérico com 14 posições, se CNPJ. Com 11 posições, alinhado 
à esquerda com brancos à direita, se CPF. Aceita NDP - Não Domiciliado no País
EOL - Sequência de caracteres Hexadecimais 0D0A, delimitador de registro



### continua
