import os
import json
import random
import glob

def criar_diretorio(diretorio):
    # Verifica se o diretório existe, se não, cria
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def obter_caminho_completo(diretorio, nome_arquivo):
    return os.path.join(diretorio, nome_arquivo)

def criando_header(caminho_completo):
    header = 'DIMOB' + (369 * ' ')
    with open(caminho_completo, 'a') as arquivo:
            arquivo.write(header + '\n')

def criando_ficha_dados_iniciais(caminho_completo):
    tipo = 'R01'
    
    # definir variaveis globais 
    global nome_empresa
    global cnpj_declarante

    cnpj_declarante = input('Digite o CNPJ do declarante: ')
    
    ano = '2023'
    retificadora = 22 * '0'

    nome_empresa = input('Digite o nome da empresa: ')
    nome_empresa = nome_empresa.ljust(60)
    cpf_responsavel = '02972859987'
    endereco = 'AV. RIO BRANCO, 333 - SALAS 202 A 208 - ED. COM. MIRAGE TOWER - CENTRO                                                  SC8105                              '
    with open(caminho_completo, 'a') as arquivo:
            arquivo.write(tipo + cnpj_declarante + ano + retificadora + nome_empresa + cpf_responsavel + endereco + '\n')

def cadastrar_cliente(caminho_completo):
    contador = 1
    registros = 0
    diretorio_json = 'C:\\Users\\auxiliar.contabil\\Magno Martins\\CONTABILIDADE - Documentos\\TRIBUTOS\\DECLARAÇÔES\\DIMOB 2024\\MAGNO ENG\\repositorio_clientes'  # Substitua pelo caminho do diretório com os arquivos JSON
    finalizar_programa = False

    while finalizar_programa == False:
        
        # Lista todos os arquivos JSON no diretório
        arquivos_json = glob.glob(os.path.join(diretorio_json, 'cliente*.json'))

        if not arquivos_json:
            print('Nenhum arquivo JSON encontrado no diretório. Programa encerrado.')
            return

        for caminho_json in arquivos_json:
            
            tipo = 'R02'
            ano = '2023'
            
            cnpj_cpf_cliente = cadastro_cnpj_cpf_cliente(caminho_json)
            nome_cliente = obter_nome_cliente(caminho_json)
            contrato = numero_contrato(caminho_json)
            data_formatada = cadastro_data_contrato(caminho_json)
            
            janeiro = extraindo_valores_mes(caminho_json,"jan")
            fevereiro = extraindo_valores_mes(caminho_json,"fev")
            março = extraindo_valores_mes(caminho_json,"mar")
            abril = extraindo_valores_mes(caminho_json,"abr")
            maio = extraindo_valores_mes(caminho_json,"maio")
            junho = extraindo_valores_mes(caminho_json,"jun")
            julho = extraindo_valores_mes(caminho_json,"jul")
            agosto = extraindo_valores_mes(caminho_json,"ago")
            setembro= extraindo_valores_mes(caminho_json,"set")
            outubro = extraindo_valores_mes(caminho_json,"out")
            novembro = extraindo_valores_mes(caminho_json,"nov")
            dezembro= extraindo_valores_mes(caminho_json,"dez")
            
            tipo_imovel = 'U'
            endereco_imovel = extraindo_endereco_imovel(caminho_json)
            cep = extraindo_cep(caminho_json)
            codido_municipio = '8105'
            reservado_20 = 20 * ' '
            uf = 'SC'
            reservado_10 = 10 * ' '

            # Formata o contador para 7 caracteres preenchidos com zeros à esquerda
            contador_formatado = f'{contador:07}'

            with open(caminho_completo, 'a') as arquivo:
                arquivo.write(tipo + cnpj_declarante + ano + contador_formatado + cnpj_declarante + nome_empresa + cnpj_cpf_cliente + nome_cliente + contrato + data_formatada + janeiro + fevereiro + março + abril + maio + junho + julho + agosto + setembro + outubro + novembro + dezembro + tipo_imovel + endereco_imovel + cep + codido_municipio + reservado_20 + uf + reservado_10 + '\n')

            contador += 1
            registros += 1

            os.system('cls')
            print('Clientes Cadastrados com SUCESSO!\n')
        
            #Finalizar o programa quando acabar os arquivos
            if len(arquivos_json) <= registros:
                print(f'{registros} registro foram adicionado')
                print('\nPrograma Finalizado!\n')
                finalizar_programa = True
                break

def obter_nome_cliente(caminho_json):
    try:
        with open(caminho_json, 'r', encoding='utf-8') as file:
            dados_json = json.load(file)
            nome_cliente = dados_json.get('nome_cliente')
            
            # Garantindo que o nome seja uma string antes de realizar o ljust
            nome_cliente_str = str(nome_cliente) if nome_cliente is not None else ''
            
            # Preenche à esquerda com espaços para garantir o comprimento desejado
            nome_cliente_formatado = nome_cliente_str.ljust(60)
            
            return nome_cliente_formatado
            
    except Exception as e:
        print(f'Erro ao obter o nome do cliente do JSON {caminho_json}: {e}')
        return None

def limpar_cpf(cpf):
    # Remove pontos, barras e hífens do CPF
    cpf_sem_formatacao = cpf.replace('.', '').replace('/', '').replace('-', '')
    return cpf_sem_formatacao

def cadastro_cnpj_cpf_cliente(caminho_json):
    while True:
        try:
            with open(caminho_json, 'r') as file:
                dados_json = json.load(file)
                cpf_cnpj = dados_json.get('cpf_cnpj_cliente')

                # Limpa a formatação do CPF
                cpf_cnpj_sem_formatacao = limpar_cpf(str(cpf_cnpj))

                # Ljust para 14 caracteres
                cpf_cnpj_sem_formatacao = cpf_cnpj_sem_formatacao.ljust(14)
                return cpf_cnpj_sem_formatacao

        except Exception as e:
            print(f'Erro ao obter o CPF/CNPJ do JSON {caminho_json}: {e}')
            return None

def numero_contrato(caminho_json):
    try:
        with open(caminho_json, 'r') as file:
            dados_json = json.load(file)
            numero_contrato = dados_json.get('numero_contrato')

            if not numero_contrato or len(numero_contrato) > 6:
                # Se o número do contrato for vazio ou maior que 6, gera um número aleatório
                numero_contrato = str(random.randint(10, 9999)).ljust(6)
            else:
                # Se o número do contrato tiver 6 ou menos caracteres, ajusta para 6
                numero_contrato = str(numero_contrato).ljust(6)

            return numero_contrato
    except Exception as e:
        print(f'Erro ao obter o número do contrato do JSON {caminho_json}: {e}')
        return None

def formatar_data_contatro(input_data):
    # Remove as barras e retorna apenas os números
    return input_data.replace('/', '')

def cadastro_data_contrato(caminho_json):
    try: 
        with open(caminho_json, 'r') as file:
            dados_json = json.load(file)
            dada_extraida = dados_json.get("data_contrato")
            
        # Verifica se a entrada tem o formato correto (DD/MM/AAAA) e componentes numéricos
        if len(dada_extraida) == 10 and dada_extraida[2] == '/' and dada_extraida[5] == '/':
            try:
                # Tenta converter os componentes em números
                dia, mes, ano = map(int, dada_extraida.split('/'))
                    
                # Verifica se os componentes estão dentro de intervalos aceitáveis
                if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 9999:
                    # Chama a função para formatar a data
                    data_formatada = formatar_data_contatro(dada_extraida)
                    return data_formatada
                else:
                    print('Data inválida. Componentes fora do intervalo aceitável.')
            except ValueError:
                print('Data inválida. Certifique-se de que os componentes são numéricos.')
            
        else:
            print('Formato de data inválido. Tente novamente.')
        
    except:
        pass

def extraindo_valores_mes(caminho_json, nome_mes):
    with open(caminho_json, 'r') as file:
        dados_json = json.load(file)
        bruto = dados_json.get(f'valor_aluguel_{nome_mes.lower()}')
        comissao = dados_json.get(f'valor_comissao_{nome_mes.lower()}')


    try:
        # verifica se teve movimentação no mês
        # se o bruto for zero, a comissao é zero
        if bruto == '':
            sem_valor = '0' * 42
            return sem_valor
        
        # Substitui vírgula por ponto e converte para float
        valor_bruto_float = float(bruto)
        valor_comissao_float = float(comissao)

        # Remove o ponto decimal e formata o valor com 14 posições
        valor_bruto_sem_separador = '{:014}'.format(int(valor_bruto_float * 100))
        valor_comissao_sem_separador = '{:014}'.format(int(valor_comissao_float * 100))

        # converter os valores para strings
        valor_bruto_sem_separador = str(valor_bruto_sem_separador)
        valor_comissao_sem_separador = str(valor_comissao_sem_separador)

        return valor_bruto_sem_separador + valor_comissao_sem_separador + prefixo3

    except ValueError:
        print(f'Valor inválido para o mês de {nome_mes}. Certifique-se de digitar um número. Tente novamente.')
        return None

def extraindo_endereco_imovel(caminho_json):
    with open(caminho_json, 'r', encoding='utf-8') as file:
            dados_json = json.load(file)
            endereco_imovel = dados_json.get('endereco_imovel')
            endereco_imovel = endereco_imovel.ljust(60)
            return endereco_imovel

def extraindo_cep(caminho_json):
    with open(caminho_json, 'r', encoding='utf-8') as file:
            dados_json = json.load(file)
            cep = dados_json.get('cep')
            cep = cep.replace('-','')
            
            return cep

def finalizar_registro(caminho_completo):
    trailler_da_declaração = 'T9'+ (' ' * 100)
    with open(caminho_completo, 'a') as arquivo:
            arquivo.write(trailler_da_declaração)

diretorio_do_arquivo = r'C:\\Users\\auxiliar.contabil\\Magno Martins\\CONTABILIDADE - Documentos\\TRIBUTOS\DECLARAÇÔES\DIMOB 2024\\MAGNO ENG'
nome_do_arquivo = 'arquivo.txt'

criar_diretorio(diretorio_do_arquivo)
caminho_completo = obter_caminho_completo(diretorio_do_arquivo, nome_do_arquivo)

#prefixo = 'R02807183310001092023'
#prefixo2 = '80718331000109MAGNO MARTINS ENGENHARIA LTDA                               '
prefixo3 = '00000000000000'

criando_header(caminho_completo)
criando_ficha_dados_iniciais(caminho_completo)
cadastrar_cliente(caminho_completo)
finalizar_registro(caminho_completo)
