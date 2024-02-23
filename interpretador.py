import os
import json
import random

def criar_diretorio(diretorio):
    # Verifica se o diretório existe, se não, cria
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def obter_caminho_completo(diretorio, nome_arquivo):
    return os.path.join(diretorio, nome_arquivo)

def obter_nome_cliente(caminho_json):
    try:
        with open(caminho_json, 'r') as file:
            dados_json = json.load(file)
            nome_cliente = dados_json.get("nome_cliente")
            nome_cliente_formatado = str(nome_cliente).ljust(60)
            return nome_cliente_formatado
            
    except Exception as e:
        print(f"Erro ao obter o nome do cliente do JSON {caminho_json}: {e}")
        return None

def cadastrar_cliente(caminho_completo, prefixo, prefixo2):
    contador = 1
    diretorio_json = 'C:\\Users\\auxiliar.contabil\\Magno Martins\\CONTABILIDADE - Documentos\\TRIBUTOS\\DECLARAÇÔES\\DIMOB 2024\\MAGNO ENG\\repositorio_clientes'  # Substitua pelo caminho do diretório com os arquivos JSON

    while True:
        
        caminho_json = os.path.join(diretorio_json, f'cliente{contador}.json')

        cnpj_cpf_cliente = cadastro_cnpj_cpf_cliente(caminho_json)
        nome_cliente = obter_nome_cliente(caminho_json)
        contrato = numero_contrato(caminho_json)
        
        data_formatada = cadastro_data_contrato()
        renda_janeiro = valores_janeiro()

        # Formata o contador para 7 caracteres preenchidos com zeros à esquerda
        contador_formatado = f'{contador:07}'

        with open(caminho_completo, 'a') as arquivo:
            arquivo.write(prefixo + contador_formatado + prefixo2 + cnpj_cpf_cliente + nome_cliente + contrato + data_formatada + renda_janeiro + '\n')

        contador += 1

        os.system('cls')
        print('Cliente Cadastrado com SUCESSO!\n')
        continuar = input("Deseja cadastrar outro cliente? (s/n) ")
        if continuar.lower() != 's':
            print('\nPrograma Finalizado!\n')
            break

def limpar_cpf(cpf):
    # Remove pontos, barras e hífens do CPF
    cpf_sem_formatacao = cpf.replace('.', '').replace('/', '').replace('-', '')
    return cpf_sem_formatacao

def cadastro_cnpj_cpf_cliente(caminho_json):
    while True:
        try:
            with open(caminho_json, 'r') as file:
                dados_json = json.load(file)
                cpf_cnpj = dados_json.get("cpf_cnpj_cliente")

                # Limpa a formatação do CPF
                cpf_cnpj_sem_formatacao = limpar_cpf(str(cpf_cnpj))

                # Ljust para 14 caracteres
                cpf_cnpj_sem_formatacao = cpf_cnpj_sem_formatacao.ljust(14)
                return cpf_cnpj_sem_formatacao

        except Exception as e:
            print(f"Erro ao obter o CPF/CNPJ do JSON {caminho_json}: {e}")
            return None

def numero_contrato(caminho_json):
    try:
        with open(caminho_json, 'r') as file:
            dados_json = json.load(file)
            numero_contrato = dados_json.get("numero_contrato")

            if not numero_contrato or len(numero_contrato) > 6:
                # Se o número do contrato for vazio ou maior que 6, gera um número aleatório
                numero_contrato = str(random.randint(10, 9999)).ljust(6)
            else:
                # Se o número do contrato tiver 6 ou menos caracteres, ajusta para 6
                numero_contrato = str(numero_contrato).ljust(6)

            return numero_contrato
    except Exception as e:
        print(f"Erro ao obter o número do contrato do JSON {caminho_json}: {e}")
        return None

def formatar_data_contatro(input_data):
    # Remove as barras e retorna apenas os números
    return input_data.replace('/', '')

def cadastro_data_contrato():
    while True:
        data_input = input("Digite a data no formato DD/MM/AAAA: ")

        # Verifica se a entrada tem o formato correto (DD/MM/AAAA) e componentes numéricos
        if len(data_input) == 10 and data_input[2] == '/' and data_input[5] == '/':
            try:
                # Tenta converter os componentes em números
                dia, mes, ano = map(int, data_input.split('/'))
                
                # Verifica se os componentes estão dentro de intervalos aceitáveis
                if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 9999:
                    # Chama a função para formatar a data
                    data_formatada = formatar_data_contatro(data_input)
                    return data_formatada
                else:
                    print("Data inválida. Componentes fora do intervalo aceitável.")
            except ValueError:
                print("Data inválida. Certifique-se de que os componentes são numéricos.")
        else:
            print("Formato de data inválido. Tente novamente.")

def valores_janeiro():
    while True:
        bruto = input("Digite o valor bruto de Janeiro: ")
        comissao = input("Digite o valor da comissão de Janeiro: ")

        try:
            # Substitui vírgula por ponto e converte para float
            valor_bruto_float = float(bruto.replace(',', '.'))
            valor_comissao_float = float(comissao.replace(',', '.'))


            # Remove o ponto decimal e formata o valor com 14 posições
            valor_bruto_sem_ponto = '{:014}'.format(int(valor_bruto_float * 100))
            valor_comissao_sem_ponto = '{:014}'.format(int(valor_comissao_float * 100))

            return valor_bruto_sem_ponto + valor_comissao_sem_ponto + prefixo3

        except ValueError:
            print("Valor inválido. Certifique-se de digitar um número. Tente novamente.")


diretorio_do_arquivo = r'C:\\Users\\auxiliar.contabil\\Magno Martins\\CONTABILIDADE - Documentos\\TRIBUTOS\DECLARAÇÔES\DIMOB 2024\\MAGNO ENG'
nome_do_arquivo = 'arquivo.txt'

criar_diretorio(diretorio_do_arquivo)
caminho_completo = obter_caminho_completo(diretorio_do_arquivo, nome_do_arquivo)

prefixo = "R02807183310001092023"
prefixo2 = "80718331000109MAGNO MARTINS ENGENHARIA LTDA                               "
prefixo3 = "00000000000000"
cadastrar_cliente(caminho_completo, prefixo, prefixo2)


#testando o upload no githup