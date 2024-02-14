from operator import length_hint
from os import system
import random
import string
from time import sleep
import requests
import re
import os
import platform
from banner import imprimir_banner
import time
from credits import creditos
from info import info_sobre
from info import infomacoes_uso
from errors import erro_cpf
from errors import erro_nome
from errors import erro_pai
from errors import erro_mae
from errors import erro_rg
from errors import erro_cns
from errors import erro_morar_cep
from errors import erro_telefone
from errors import erro_fixo
from errors import erro_email
from errors import erro_cnpj
from errors import erro_placa
from errors import erro_operadora
from errors import erro_cep
from errors import erro_bin
from errors import erro_ip
from errors import erro_gerar_pessoa
from errors import erro_gerar_cartao

R = "\033[0;91m"
B = "\033[1;36m"
C = "\033[1;37m"
Y = "\033[1;33m"
G = "\033[1;32m"
L = "\033[1;35m"
P = "\033[30m"
RT = "\033[40m"


nome_usuario = os.getlogin()


os.system('cls' if os.name == 'nt' else 'clear')



def animacao_carregando():
    tempo_inicial = time.time()
    while True:
        tempo_atual = time.time()
        if tempo_atual - tempo_inicial >= 5:
            break
        print(f"{L}\n\n\n\n\n\n\n\n————————————————————————————————————————————————————————\n", end="", flush=False)
        print(f"{L}    Verificando atualizações, por favor, aguarde", end="", flush=True)
        for _ in range(3):  
            for _ in range(3):  
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("\b\b\b   \b\b\b", end="", flush=True)
            time.sleep(0.5)

animacao_carregando()






def tchau():
    print("Aguarde, saindo em:")
    print("3...")
    sleep(1)
    print("2..")
    sleep(1)
    print("1.")
    sleep(1)

    print(f"\n{L}====================================================")
    print(f"                   {C}Até breve {B}{nome_usuario}               ")
    print(f"{L}====================================================\n\n\n\n")




print("\n\n")

os.system('cls' if os.name == 'nt' else 'clear')


def tipos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        C + f"""
    {C}██████╗  █████╗ ██████╗  {L}██████╗ ██╗████████╗ ██████╗██╗  ██╗
    {C}██╔══██╗██╔══██╗██╔══██╗ {L}██╔══██╗██║╚══██╔══╝██╔════╝██║  ██║
    {C}██████╔╝███████║██║  ██║ {L}██████╔╝██║   ██║   ██║     ███████║
    {C}██╔══██╗██╔══██║██║  ██║ {L}██╔══██╗██║   ██║   ██║     ██╔══██║
    {C}██████╔╝██║  ██║██████╔╝ {L}██████╔╝██║   ██║   ╚██████╗██║  ██║
    {C}╚═════╝ ╚═╝  ╚═╝╚═════╝  {L}╚═════╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝ {C}v1.0 (BETA)       
                                              {L}Created By {C}offalien\n"""                                                   
    )

    print(f"""
  {C}[{L}OPÇÕES{C}]                                   {C}[{L}STATUS{C}]           

    {C}[{L}1{C}]  Consulta de CPF                       {C}[{B}ON{C}]           {C}[{L}13{C}] Informações de Operadora             {C}[{B}ON{C}]
    {C}[{L}2{C}]  Consulta de Nome                      {C}[{B}ON{C}]           {C}[{L}14{C}] Consultar CEP                        {C}[{B}ON{C}]
    {C}[{L}3{C}]  Consulta por nome do pai              {C}[{B}ON{C}]           {C}[{L}15{C}] Consulta de BIN (Cartão)             {C}[{B}ON{C}]
    {C}[{L}4{C}]  Consulta por nome da mãe              {C}[{B}ON{C}]           {C}[{L}16{C}] Consulta de IP/Site                  {C}[{B}ON{C}]
    {C}[{L}5{C}]  Consulta de RG                       [BETA]          {C}[{L}17{C}] Gerador de Pessoa                    {C}[{B}ON{C}]
    {C}[{L}6{C}]  Consulta de CNS                       {C}[{B}ON{C}]           {C}[{L}18{C}] Gerador de Cartão de Crédito         {C}[{B}ON{C}]                                                         
    {C}[{L}7{C}]  Consulta Moradores por CEP            {C}[{B}ON{C}]           
    {C}[{L}8{C}]  Consulta de dados por Telefone        {C}[{B}ON{C}]           {C}[{L}99{C}] Sair
    {C}[{L}9{C}]  Consulta de Telefone Fixo             {C}[{B}ON{C}]           
    {C}[{L}10{C}] Consulta por E-mail                   {C}[{B}ON{C}]           
    {C}[{L}11{C}] Consulta de CNPJ                      {C}[{B}ON{C}]           {C}[{L}i{C}] Informações de uso                   {C}[{B}INFO{C}]
    {C}[{L}12{C}] Consulta de Placa                   [OFFLINE]        {C}[{L}?{C}] Créditos Finais                      {C}[{B}INFO{C}]
            \n
    {C}╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
         {B}Discord: {L}offalien    {C}||      {L}Bad Bitch {C}© All Rights Reserved      {C}||    {B}Usuário: {L}{nome_usuario}
    {C}╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝
            
            """
    )











    tool = input(C + f"[{L}*{C}] SELECIONE A OPÇÃO DESEJADA: " + C)

    if tool == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"      {C}Mais de 180 milhões de dados disponíveis para consulta          ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        cpf = input(C + f"[{L}*{C}] DIGITE O CPF: " + C)
        cpf = re.sub("[^0-9]+", "", cpf)
        consulta(cpf)
        

    elif tool == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"            {C}CONSULTANDO TODA A POPULAÇÃO DO BRASIL!   ")
        print(f"     MAIS DE 224 MILHÕES DE DADOS DISPONÍVEIS PARA CONSULTA            ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝")
        nome = input(C + f"\n[{L}*{C}] DIGITE O NOME COMPLETO: " + C)
        consulta_nome(nome)


    elif tool == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"                {C}Consultando Filhos pelo nome do Pai                    ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        pai = input(C + f"[{L}*{C}] DIGITE O NOME DO PAI COMPLETO: " + C)
        consulta_pai(pai)

    elif tool == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"               {C}Consultando Filhos pelo nome da Mãe                    ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        mae = input(C + f"[{L}*{C}] DIGITE O NOME DA MÃE COMPLETO: " + C)
        consulta_mae(mae)

    elif tool == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"           {C}Consultando Dados das Pessoas pelo RG [BETA]                   ")
        print(f"       Algumas consultas podem não funcionar ou não encontrar!")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        rg = input(C + f"[{L}*{C}] DIGITE O RG: " + C)
        rg = re.sub("[^0-9]+", "", rg)
        consulta_rg(rg)

    elif tool == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"                  {C}Consultando Dados Pessoais Pelo CNS                   ")
        print(f"                         Cartão Nacional do SUS                            ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        cns = input(C + f"[{L}*{C}] DIGITE O CNS: " + C)
        rg = re.sub("[^0-9]+", "", cns)
        consulta_cns(cns)

    elif tool == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"                   {C}Consultando Dados de Moradores                  ")
        print(f"                         De um determinado CEP                            ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        cep_pessoas = input(C + f"[{L}*{C}] DIGITE O CEP QUE DESEJA CONSULTAR OS MORADORES: " + C)
        cep_pessoas = re.sub("[^0-9]+", "", cep_pessoas)
        consulta_cep(cep_pessoas)

    elif tool == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"     {C}Mais de 100 milhões de Números disponíveis para consulta          ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        print("OBS: Evite usar espaços e pontos, use o apenas o DDD e o número. Exemplo: 11987654321")        
        telefone = input(C + f"[{L}*{C}] DIGITE O TELEFONE A CONSULTAR: " + C)
        telefone = re.sub("[^0-9]+", "", telefone)
        consulta_telefone(telefone)

    elif tool == "9":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"     {C}Mais de 100 milhões de Números disponíveis para consulta          ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        print("OBS: Evite usar espaços e pontos, use o apenas o DDD e o número. Exemplo: 1135128012")        
        fixo = input(C + f"[{L}*{C}] DIGITE O TELEFONE A CONSULTAR: " + C)
        fixo = re.sub("[^0-9]+", "", fixo)
        consulta_fixo(fixo)

    elif tool == "10":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"     {C}Mais de 10 milhões de E-mails disponíveis para consulta          ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        email = input(C + f"[{L}*{C}] DIGITE O E-MAIL DESEJADO: " + C)
        consulta_email(email)

    elif tool == "11":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"        {C}Consulta de CNPJ Mostrando Sócios Proprietários          ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        cnpj = input(C + f"[{L}*{C}] DIGITE O CNPJ DA EMPRESA A CONSULTAR: " + C)
        cnpj = re.sub("[^0-9]+", "", cnpj)
        consulta_cnpj(cnpj)

    elif tool == "12":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"         {C}ESTE ITEM ESTARÁ DISPONÍVEL EM BREVE!          ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        placa = re.sub("[^0-9]+", "", placa)
        info_sobre(placa)

    elif tool == "13":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"       {C}Verificação de Operadora Pelo Número de celular               ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        print("OBS: Insira o número no formato internacional. Exemplo: +551191234567")
        operadora = input(C + f"[{L}*{C}] DIGITE O NÚMERO DE TELEFONE A SER CONSULTADO: " + C)
        consulta_operadora(operadora)

    elif tool == "14":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"                       {C}Consultar Rua pelo CEP               ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        print("Não use pontos e hífens, use apenas números.")
        banco = input(C + f"[{L}*{C}] DIGITE O CEP ABAIXO: " + C)
        viacep(banco)

    elif tool == "15":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"              {C}Consultar de Nível de Cartão de Crédito               ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        print("\nInsira apenas os 6 primeiros dígitos do cartão")
        banco = input(C + f"[{L}*{C}] DIGITE A BIN: " + C)
        bin_cc(banco)

    elif tool == "16":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        print(f"\n{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"                         {C}Consultar de IP                            ")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        busca_ip()


    elif tool == "17":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        gerarpessoa()

    elif tool == "18":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        gerarcartao()

    elif tool == "99":
        os.system('cls' if os.name == 'nt' else 'clear')
        tchau()

    elif tool == "i":
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_banner()
        infomacoes_uso()
        input(C + f"[{L}:){C}] Aperte qualquer tecla para retornar ao menu: " + C)
        print("\n")
        tipos()

    elif tool == "?":
        os.system('cls' if os.name == 'nt' else 'clear')
        info_sobre()
        input(C + f"[{L}:){C}] Aperte qualquer tecla para retornar ao menu: " + C)
        tipos()


    else:
        print(C + f"[{L}!{C}] Seleção inválida.")
        sleep(1)
        tipos()

def consulta(cpf):

    url = f"http://18.228.166.136:8000/api/v1/database/datasus/search?cpf={cpf}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf2_info = data[0]  

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                         {C}CONSULTA DE CPF                           {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " NOME:", (cpf2_info.get('nome') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " CPF:", cpf2_info.get('cpf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DA MÃE:", cpf2_info.get('mae') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DO PAI:", cpf2_info.get('pai') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", cpf2_info.get('logradouro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", cpf2_info.get('numero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " BAIRRO:", cpf2_info.get('bairro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " COMPLEMENTO: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " CIDADE:", cpf2_info.get('municipio') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CEP:", cpf2_info.get('cep') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CIDADE DE NASCIMENTO:", cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TÍTULO ELEITORAL:", cpf2_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " PIS:", cpf2_info.get('pis') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CNS:", cpf2_info.get('cns') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG:", cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG DATA DE EMISSÃO:", cpf2_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG ORGÃO EMISSOR:", cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " UF DO RG:", cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " E-MAIL: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " TELEFONE:", cpf2_info.get('telefone') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TELEFONE SECUNDÁRIO:", cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO')

                print("")
                creditos()


                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

                if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                    
                    cpf_arquivo = f"CPF_{cpf}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), cpf_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"\n\nResultados da Consulta do CPF {cpf}\n\n")
                        arquivo.write("_________________________________________________________\n\n")
                        arquivo.write(f"- Nome: {(cpf2_info.get('nome') or 'SEM INFORMAÇÃO').upper()}\n")
                        arquivo.write(f"- CPF: {cpf2_info.get('cpf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Data de Nascimento: {cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome da Mãe: {cpf2_info.get('mae') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome do Pai: {cpf2_info.get('pai') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Rua/Logradouro: {cpf2_info.get('logradouro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Número da Casa: {cpf2_info.get('numero') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Bairro: {cpf2_info.get('bairro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                        arquivo.write(f"- Cidade: {cpf2_info.get('municipio') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CEP: {cpf2_info.get('cep') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Cidade de Nascimento: {cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Título Eleitoral: {cpf2_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- PIS: {cpf2_info.get('pis') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CNS: {cpf2_info.get('cns') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG: {cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG Data de Emissão: {cpf2_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG Órgão Emissor: {cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- UF do RG: {cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("- E-mail: SEM INFORMAÇÃO\n")
                        arquivo.write(f"- Telefone: {cpf2_info.get('telefone') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Telefone Secundário: {cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO'}\n\n")
                        arquivo.write("_________________________________________________________\n")
                        arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {cpf_arquivo}\n")

                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()
        else:
            erro_cpf()
            sleep(2)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_nome(nome):
    url = f"http://18.228.166.136:8000/api/v1/database/serasa/search?nome={nome}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                         {C}CONSULTA DE NOME                        {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                for pessoa in data:
                    print(f"{C}[{L}+{C}]" " NOME:", pessoa.get('nome', 'SEM INFORMAÇÃO').upper())
                    print(f"{C}[{L}+{C}]" " CPF:", pessoa.get('cpf', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " SEXO:", pessoa.get('sexo', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", pessoa.get('data_nascimento', 'SEM INFORMAÇÃO\n'))
                    print(f"{L}\n---------------------------------------------------\n")

                print(f"{C}[{B}+{C}] {len(data)} DADOS ENCONTRADOS NO NOME DE {B}{nome}\n")
                creditos()

                salvar = input(C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: ").lower()

                if salvar == "s" or salvar == "sim" or salvar == "y" or salvar == "yes":

                    nome_arquivo = f"{nome}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"Resultados da consulta para o nome '{nome}':\n\n")
                        for pessoa in data:
                            arquivo.write("________________________________________________________________\n")
                            arquivo.write("\n- Nome: {}\n".format(pessoa.get('nome', 'SEM INFORMAÇÃO').upper()))
                            arquivo.write("- CPF: {}\n".format(pessoa.get('cpf', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Sexo: {}\n".format(pessoa.get('sexo', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Data de Nascimento: {}\n".format(pessoa.get('data_nascimento', 'SEM INFORMAÇÃO\n')))
                        arquivo.write("________________________________________________________________\n")
                        arquivo.write("\n                  Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO '{nome_arquivo}'!\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()
                   
        else:
            print ("")
            erro_nome()
            sleep(2)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_pai(pai):
    url = f"http://18.228.166.136:8000/api/v1/database/datasus/search?pai={pai}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                     {C}CONSULTA POR NOME DO PAI                    {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                for pessoa in data:
                    print(f"{C}[{L}+{C}]" " NOME:", pessoa.get('nome', 'SEM INFORMAÇÃO').upper())
                    print(f"{C}[{L}+{C}]" " CPF:", pessoa.get('cpf', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", pessoa.get('nascimento', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " NOME DO PAI:", pessoa.get('pai', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " NOME DA MÃE:", pessoa.get('mae', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", pessoa.get('logradouro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", pessoa.get('numero') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " BAIRRO:", pessoa.get('bairro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " COMPLEMENTO: SEM INFORMAÇÃO")
                    print(f"{C}[{L}+{C}]" " CIDADE:", pessoa.get('municipio') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CEP:", pessoa.get('cep') or 'SEM INFORMAÇÃO')
                    print(f"{L}\n---------------------------------------------------\n")
                
                print(f"{C}[{B}+{C}] {len(data)} FILHOS FORAM ENCONTRADOS PELO NOME DO PAI {B}{pai}\n")
                creditos()

                salvar = input(C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: ").lower()

                if salvar == "s" or salvar == "sim" or salvar == "y" or salvar == "yes":
                    pai_arquivo = f"FILHOS_{pai}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), pai_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"Resultados da consulta para os filhos do Sr. {pai}\n\n")
                        for pessoa in data:
                            arquivo.write("________________________________________________________________\n")
                            arquivo.write("\n- Nome: {}\n".format(pessoa.get('nome', 'SEM INFORMAÇÃO').upper()))
                            arquivo.write("- CPF: {}\n".format(pessoa.get('cpf', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Data de nascimento: {}\n".format(pessoa.get('nascimento', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Nome do pai: {}\n".format(pessoa.get('pai', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Nome da mãe: {}\n".format(pessoa.get('mae', 'SEM INFORMAÇÃO')))           
                            arquivo.write("- Rua/Logradouro: {}\n".format(pessoa.get('logradouro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Número da casa: {}\n".format(pessoa.get('numero', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Bairro: {}\n".format(pessoa.get('bairro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                            arquivo.write("- Cidade: {}\n".format(pessoa.get('municipio', 'SEM INFORMAÇÃO')))
                            arquivo.write("- CEP: {}\n".format(pessoa.get('cep', 'SEM INFORMAÇÃO\n')))
                        arquivo.write("________________________________________________________________\n")
                        arquivo.write("\n                  Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO '{pai_arquivo}'!\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA> [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()
                
        else:
            print ("")
            erro_pai()
            sleep(2)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_mae(mae):
    url = f"http://18.228.166.136:8000/api/v1/database/datasus/search?mae={mae}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                      {C}CONSULTA POR NOME DA MÃE                   {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                for pessoa in data:
                    print(f"{C}[{L}+{C}]" " NOME:", pessoa.get('nome', 'SEM INFORMAÇÃO').upper())
                    print(f"{C}[{L}+{C}]" " CPF:", pessoa.get('cpf', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", pessoa.get('nascimento', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " NOME DA PAI:", pessoa.get('pai', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " NOME DA MÃE:", pessoa.get('mae', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", pessoa.get('logradouro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", pessoa.get('numero') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " BAIRRO:", pessoa.get('bairro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " COMPLEMENTO: SEM INFORMAÇÃO")
                    print(f"{C}[{L}+{C}]" " CIDADE:", pessoa.get('municipio') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CEP:", pessoa.get('cep') or 'SEM INFORMAÇÃO')
                    print(f"{L}\n---------------------------------------------------\n")
                
                print(f"{C}[{B}+{C}] {len(data)} FILHOS FORAM ENCONTRADOS PELO NOME DA MÃE {B}{mae}\n")
                creditos()
                salvar = input(C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: ").lower()

                if salvar == "s" or salvar == "sim" or salvar == "y" or salvar == "yes":
                    mae_arquivo = f"FILHOS_{mae}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), mae_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"Resultados da consulta para os filhos do Sra. {mae}\n\n")
                        for pessoa in data:
                            arquivo.write("________________________________________________________________\n")
                            arquivo.write("\n- Nome: {}\n".format(pessoa.get('nome', 'SEM INFORMAÇÃO').upper()))
                            arquivo.write("- CPF: {}\n".format(pessoa.get('cpf', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Data de nascimento: {}\n".format(pessoa.get('nascimento', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Nome do pai: {}\n".format(pessoa.get('pai', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Nome da mãe: {}\n".format(pessoa.get('mae', 'SEM INFORMAÇÃO')))           
                            arquivo.write("- Rua/Logradouro: {}\n".format(pessoa.get('logradouro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Número da casa: {}\n".format(pessoa.get('numero', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Bairro: {}\n".format(pessoa.get('bairro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                            arquivo.write("- Cidade: {}\n".format(pessoa.get('municipio', 'SEM INFORMAÇÃO')))
                            arquivo.write("- CEP: {}\n".format(pessoa.get('cep', 'SEM INFORMAÇÃO\n')))
                        arquivo.write("________________________________________________________________\n")
                        arquivo.write("\n                  Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO '{mae_arquivo}'!\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA> [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                   tchau()

        else:
            print ("")
            erro_mae()
            sleep(2)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_rg(rg):

    url = f"http://18.228.166.136:8000/api/v1/database/datasus/search?rg={rg}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf2_info = data[0]  

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                           {C}CONSULTA DE RG                       {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " NOME:", (cpf2_info.get('nome') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " CPF:", cpf2_info.get('cpf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DA MÃE:", cpf2_info.get('mae') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DO PAI:", cpf2_info.get('pai') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", cpf2_info.get('logradouro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", cpf2_info.get('numero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " BAIRRO:", cpf2_info.get('bairro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " COMPLEMENTO: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " CIDADE:", cpf2_info.get('municipio') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CEP:", cpf2_info.get('cep') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CIDADE DE NASCIMENTO:", cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TÍTULO ELEITORAL:", cpf2_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " PIS:", cpf2_info.get('pis') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CNS:", cpf2_info.get('cns') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG:", cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG DATA DE EMISSÃO:", cpf2_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG ORGÃO EMISSOR:", cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " UF DO RG:", cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " E-MAIL: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " TELEFONE:", cpf2_info.get('telefone') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TELEFONE SECUNDÁRIO:", cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO')

                print("")
                creditos()

                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

                if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                    rg_arquivo = f"RG_{rg}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), rg_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"\n\nResultados da Consulta no RG {rg}\n\n")
                        arquivo.write("_________________________________________________________\n\n")
                        arquivo.write(f"- Nome: {cpf2_info.get('nome') or 'SEM INFORMAÇÃO'}\n".upper())
                        arquivo.write(f"- CPF: {cpf2_info.get('cpf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Data de Nascimento: {cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome da Mãe: {cpf2_info.get('mae') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome do Pai: {cpf2_info.get('pai') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Rua/Logradouro: {cpf2_info.get('logradouro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Número da Casa: {cpf2_info.get('numero') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Bairro: {cpf2_info.get('bairro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                        arquivo.write(f"- Cidade: {cpf2_info.get('municipio') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CEP: {cpf2_info.get('cep') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Cidade de Nascimento: {cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Título Eleitoral: {cpf2_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- PIS: {cpf2_info.get('pis') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CNS: {cpf2_info.get('cns') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG: {cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG Data de Emissão: {cpf2_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG Órgão Emissor: {cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- UF do RG: {cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("- E-mail: SEM INFORMAÇÃO\n")
                        arquivo.write(f"- Telefone: {cpf2_info.get('telefone') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Telefone Secundário: {cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO'}\n\n")
                        arquivo.write("_________________________________________________________\n")
                        arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {rg_arquivo}.txt\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                tchau()

        else:
            print ("")
            erro_rg()
            sleep(2)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_cns(cns):

    url = f"http://18.228.166.136:8000/api/v1/database/datasus/search?cns={cns}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf2_info = data[0]  

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                         {C}CONSULTA DE CNS                          {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " NOME:", (cpf2_info.get('nome') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " CPF:", cpf2_info.get('cpf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DA MÃE:", cpf2_info.get('mae') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DO PAI:", cpf2_info.get('pai') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", cpf2_info.get('logradouro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", cpf2_info.get('numero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " BAIRRO:", cpf2_info.get('bairro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " COMPLEMENTO: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " CIDADE:", cpf2_info.get('municipio') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CEP:", cpf2_info.get('cep') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CIDADE DE NASCIMENTO:", cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TÍTULO ELEITORAL:", cpf2_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " PIS:", cpf2_info.get('pis') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CNS:", cpf2_info.get('cns') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG:", cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG DATA DE EMISSÃO:", cpf2_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG ORGÃO EMISSOR:", cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " UF DO RG:", cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " E-MAIL: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " TELEFONE:", cpf2_info.get('telefone') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TELEFONE SECUNDÁRIO:", cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO')

                print("")
                creditos()

                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

                if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":

                    cns_arquivo = f"CNS_{cns}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), cns_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"\n\nResultados da Consulta no CNS (Cartão Nacional do Sus) {cns}\n\n")
                        arquivo.write("_________________________________________________________\n\n")
                        arquivo.write(f"- Nome: {cpf2_info.get('nome') or 'SEM INFORMAÇÃO'}\n".upper())
                        arquivo.write(f"- CPF: {cpf2_info.get('cpf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Data de Nascimento: {cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome da Mãe: {cpf2_info.get('mae') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome do Pai: {cpf2_info.get('pai') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Rua/Logradouro: {cpf2_info.get('logradouro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Número da Casa: {cpf2_info.get('numero') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Bairro: {cpf2_info.get('bairro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                        arquivo.write(f"- Cidade: {cpf2_info.get('municipio') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CEP: {cpf2_info.get('cep') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Cidade de Nascimento: {cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Título Eleitoral: {cpf2_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- PIS: {cpf2_info.get('pis') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CNS: {cpf2_info.get('cns') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG: {cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG Data de Emissão: {cpf2_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- RG Órgão Emissor: {cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- UF do RG: {cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("- E-mail: SEM INFORMAÇÃO\n")
                        arquivo.write(f"- Telefone: {cpf2_info.get('telefone') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Telefone Secundário: {cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO'}\n\n")
                        arquivo.write("_________________________________________________________\n")
                        arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {cns_arquivo}\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_cns()
            sleep(2)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_cep(cep):
    url = f"http://18.228.166.136:8000/api/v1/database/datasus/search?cep={cep}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                    {C}CONSULTA DE MORADORES POR CEP                 {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                for pessoa in data:
                    print(f"{C}[{L}+{C}]" " NOME:", pessoa.get('nome', 'SEM INFORMAÇÃO').upper())
                    print(f"{C}[{L}+{C}]" " CPF:", pessoa.get('cpf', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", pessoa.get('nascimento', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " NOME DA MÃE:", pessoa.get('mae', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", pessoa.get('logradouro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", pessoa.get('numero') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " BAIRRO:", pessoa.get('bairro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CIDADE:", pessoa.get('municipio') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CEP:", pessoa.get('cep') or 'SEM INFORMAÇÃO')
                    print(f"{L}\n---------------------------------------------------\n")
                
                print(f"{C}[{B}+{C}] {len(data)} MORADORES DO CEP {B}{cep} {C}FORAM ENCONTRADOS")
                print(f"{C}[{B}+{C}] OBS: ALGUNS DADOS SERÃO REPETIDOS, É NORMAL!\n")
                creditos()

                salvar = input(C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: ").lower()

                if salvar == "s" or salvar == "sim" or salvar == "y" or salvar == "yes":
                    cep_arquivo = f"PESSOAS_CEP_{cep}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), cep_arquivo)

                    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                        arquivo.write(f"Resultados da consulta para os Moradores do CEP {cep}\n\n")
                        for pessoa in data:
                            arquivo.write("________________________________________________________________\n")
                            arquivo.write("\n- Nome: {}\n".format(pessoa.get('nome', 'SEM INFORMAÇÃO').upper()))
                            arquivo.write("- CPF: {}\n".format(pessoa.get('cpf', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Sexo: {}\n".format(pessoa.get('nascimento', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Nome do pai: {}\n".format(pessoa.get('pai', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Nome da mãe: {}\n".format(pessoa.get('mae', 'SEM INFORMAÇÃO')))           
                            arquivo.write("- Rua/Logradouro: {}\n".format(pessoa.get('logradouro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Número da casa: {}\n".format(pessoa.get('numero', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Bairro: {}\n".format(pessoa.get('bairro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                            arquivo.write("- Cidade: {}\n".format(pessoa.get('municipio', 'SEM INFORMAÇÃO')))
                            arquivo.write("- CEP: {}\n".format(pessoa.get('cep', 'SEM INFORMAÇÃO\n')))
                        arquivo.write("________________________________________________________________\n")
                        arquivo.write("\n                  Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO '{cep_arquivo}'!\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA> [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_morar_cep()
            sleep(5)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_telefone(telefone):
    url = f"http://18.228.166.136:8000/api/v1/database/telefone/search?telefone={telefone}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                   {C}CONSULTA DE DADOS POR TELEFONE                 {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                for pessoa in data:
                    print(f"{C}[{L}+{C}]" " NOME:", pessoa.get('nome', 'SEM INFORMAÇÃO').upper())
                    print(f"{C}[{L}+{C}]" " CPF:", pessoa.get('cpf', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", pessoa.get('rua') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", pessoa.get('numero') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " BAIRRO:", pessoa.get('bairro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " COMPLEMENTO:", pessoa.get('complemento') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CIDADE:", pessoa.get('cidade') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CEP:", pessoa.get('cep') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " UF:", pessoa.get('uf') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " TELEFONE:", pessoa.get('telefone') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " OPERADORA:", pessoa.get('operadora') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " TELEFONE FIXO:", pessoa.get('fixo') or 'SEM INFORMAÇÃO')

                    print(f"{L}\n---------------------------------------------------\n")
                
                print(f"{C}[{B}+{C}] {len(data)} DADOS DE PROPRIETÁRIOS FORAM ENCONTRADOS PARA O TELEFONE {B}{telefone}\n")
                creditos()

                salvar = input(C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: ").lower()

                if salvar == "s" or salvar == "sim" or salvar == "y" or salvar == "yes":
                    telefone_arquivo = f"TELEFONE_{telefone}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), telefone_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"Resultados dos proprietários do telefone {telefone}\n\n")
                        for pessoa in data:
                            arquivo.write("________________________________________________________________\n")
                            arquivo.write("\n- Nome: {}\n".format(pessoa.get('nome', 'SEM INFORMAÇÃO').upper()))
                            arquivo.write("- CPF: {}\n".format(pessoa.get('cpf', 'SEM INFORMAÇÃO')))         
                            arquivo.write("- Rua/Logradouro: {}\n".format(pessoa.get('rua', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Número da casa: {}\n".format(pessoa.get('numero', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Bairro: {}\n".format(pessoa.get('bairro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Complemento: {}\n".format(pessoa.get('complemento', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Cidade: {}\n".format(pessoa.get('cidade', 'SEM INFORMAÇÃO')))
                            arquivo.write("- CEP: {}\n".format(pessoa.get('cep', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- UF: {}\n".format(pessoa.get('uf', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- TELEFONE: {}\n".format(pessoa.get('telefone', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- OPERADORA: {}\n".format(pessoa.get('operadora', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- TELEFONE FIXO: {}\n".format(pessoa.get('fixo', 'SEM INFORMAÇÃO\n')))
                        arquivo.write("________________________________________________________________\n")
                        arquivo.write("\n                  Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO '{telefone_arquivo}'!\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA> [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_telefone()
            sleep(5)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_fixo(fixo):
    url = f"http://18.228.166.136:8000/api/v1/database/telefone/search?fixo={fixo}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                 {C}CONSULTA DE DADOS POR TELEFONE                  {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                for pessoa in data:
                    print(f"{C}[{L}+{C}]" " NOME:", pessoa.get('nome', 'SEM INFORMAÇÃO').upper())
                    print(f"{C}[{L}+{C}]" " CPF:", pessoa.get('cpf', 'SEM INFORMAÇÃO'))
                    print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", pessoa.get('rua') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", pessoa.get('numero') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " BAIRRO:", pessoa.get('bairro') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " COMPLEMENTO:", pessoa.get('complemento') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CIDADE:", pessoa.get('cidade') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " CEP:", pessoa.get('cep') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " UF:", pessoa.get('uf') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " TELEFONE:", pessoa.get('telefone') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " OPERADORA:", pessoa.get('operadora') or 'SEM INFORMAÇÃO')
                    print(f"{C}[{L}+{C}]" " TELEFONE FIXO:", pessoa.get('fixo') or 'SEM INFORMAÇÃO')

                    print(f"{L}\n---------------------------------------------------\n")
                
                print(f"{C}[{B}+{C}] {len(data)} DADOS DE PROPRIETÁRIOS FORAM ENCONTRADOS PARA O TELEFONE {B}{fixo}\n")
                creditos()

                salvar = input(C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: ").lower()

                if salvar == "s" or salvar == "sim" or salvar == "y" or salvar == "yes":
                    fixo_arquivo = f"TELEFONE_FIXO_{fixo}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), fixo_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"Resultados dos proprietários do telefone {fixo}\n\n")
                        for pessoa in data:
                            arquivo.write("________________________________________________________________\n")
                            arquivo.write("\n- Nome: {}\n".format(pessoa.get('nome', 'SEM INFORMAÇÃO').upper()))
                            arquivo.write("- CPF: {}\n".format(pessoa.get('cpf', 'SEM INFORMAÇÃO')))         
                            arquivo.write("- Rua/Logradouro: {}\n".format(pessoa.get('rua', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Número da casa: {}\n".format(pessoa.get('numero', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Bairro: {}\n".format(pessoa.get('bairro', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Complemento: {}\n".format(pessoa.get('complemento', 'SEM INFORMAÇÃO')))
                            arquivo.write("- Cidade: {}\n".format(pessoa.get('cidade', 'SEM INFORMAÇÃO')))
                            arquivo.write("- CEP: {}\n".format(pessoa.get('cep', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- UF: {}\n".format(pessoa.get('uf', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- TELEFONE: {}\n".format(pessoa.get('telefone', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- OPERADORA: {}\n".format(pessoa.get('operadora', 'SEM INFORMAÇÃO\n')))
                            arquivo.write("- TELEFONE FIXO: {}\n".format(pessoa.get('fixo', 'SEM INFORMAÇÃO\n')))
                        arquivo.write("________________________________________________________________\n")
                        arquivo.write("\n                  Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO '{fixo_arquivo}'!\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA> [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_fixo()
            sleep(5)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_email(email):

    url = f"http://18.228.166.136:8000/api/v1/datasus_emails/search?email={email}"
    headers = {'apikey': 'b08a14ec7cdbf0d7470c7d751dbf0733'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                email_info = data[0] 

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                        {C}CONSULTA DE E-MAIL                        {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " NOME:", (email_info.get('nome') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " CPF:", email_info.get('cpf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", email_info.get('nascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " E-MAILS:", email_info.get('emails') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DA MÃE:", email_info.get('mae') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DO PAI:", email_info.get('pai') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RUA/LOGRADOURO:", email_info.get('logradouro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NÚMERO DA CASA:", email_info.get('numero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " BAIRRO:", email_info.get('bairro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " COMPLEMENTO: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " CIDADE:", email_info.get('municipio') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CEP:", email_info.get('cep') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CIDADE DE NASCIMENTO:", email_info.get('municipioNascimento') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TÍTULO ELEITORAL:", email_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " PIS:", email_info.get('pis') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CNS:", email_info.get('cns') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG:", email_info.get('rgNumero') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG DATA DE EMISSÃO:", email_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " RG ORGÃO EMISSOR:", email_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " UF DO RG:", email_info.get('rgUf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " E-MAIL: SEM INFORMAÇÃO")
                print(f"{C}[{L}+{C}]" " TELEFONE:", email_info.get('telefone') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TELEFONE SECUNDÁRIO:", email_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO')

                print("")
                creditos()

                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

            if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                email_arquivo = f"EMAIL_{email}.txt"
                caminho_arquivo = os.path.join(os.getcwd(), email_arquivo)

                with open(caminho_arquivo, 'w') as arquivo:
                    arquivo.write(f"\n\nResultados da Consulta: {email}\n\n")
                    arquivo.write("_________________________________________________________\n\n")
                    arquivo.write(f"- Nome: {email_info.get('nome') or 'SEM INFORMAÇÃO'}\n".upper())
                    arquivo.write(f"- CPF: {email_info.get('cpf') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Data de Nascimento: {email_info.get('nascimento') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- E-mail: {email_info.get('emails') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Nome da Mãe: {email_info.get('mae') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Nome do Pai: {email_info.get('pai') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Rua/Logradouro: {email_info.get('logradouro') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Número da Casa: {email_info.get('numero') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Bairro: {email_info.get('bairro') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write("- Complemento: SEM INFORMAÇÃO\n")
                    arquivo.write(f"- Cidade: {email_info.get('municipio') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- CEP: {email_info.get('cep') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Cidade de Nascimento: {email_info.get('municipioNascimento') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Título Eleitoral: {email_info.get('tituloEleitoral') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- PIS: {email_info.get('pis') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- CNS: {email_info.get('cns') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- RG: {email_info.get('rgNumero') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- RG Data de Emissão: {email_info.get('rgDataEmissao') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- RG Órgão Emissor: {email_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- UF do RG: {email_info.get('rgUf') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write("- E-mail: SEM INFORMAÇÃO\n")
                    arquivo.write(f"- Telefone: {email_info.get('telefone') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Telefone Secundário: {email_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO'}\n\n")
                    arquivo.write("_________________________________________________________\n")
                    arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                    arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {email_arquivo}\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_email()
            sleep(3)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def consulta_cnpj(cnpj):

    url = f"https://hyb.com.br/curl_cnpj.php?action=acessa_curl&cnpj={cnpj}"
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            data = response.json()

            if data.get('cnpj') is None:
                print("")
                print(f"{L}+------------------------------------------------+")
                print(f"{L}+              {C}CNPJ NÃO ENCONTRADO!              {L}+")
                print(f"{L}+------------------------------------------------+")
                sleep(1.5)
                tipos()
            
            else:
                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                         {C}CONSULTA DE CNPJ                     {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")


                print(f"{C}[{L}+{C}] CNPJ: {data.get('cnpj') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] NOME FANTASIA: {data.get('nome_fantasia') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] RAZÃO SOCIAL: {data.get('razao_social') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] MATRIZ FILIAL: {data.get('matriz_filial') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] MOTIVO DA ABERTURA: {data.get('motivo_situacao') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] ENDEREÇO: {data.get('tipo_logradouro', 'SEM INFORMAÇÃO')} {data.get('logradouro', 'SEM INFORMAÇÃO')}, {data.get('numero', 'SEM INFORMAÇÃO')} - {data.get('bairro', 'SEM INFORMAÇÃO')}")
                print(f"{C}[{L}+{C}] CEP: {data.get('cep') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] MUNICÍPIO: {data.get('municipio', 'SEM INFORMAÇÃO')} - {data.get('uf', 'SEM INFORMAÇÃO')}")
                print(f"{C}[{L}+{C}] COMPLEMENTO: {data.get('complemento') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] TELEFONE: {data.get('telefone_1') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] TELEFONE 2: {data.get('telefone_2') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] DATA DE ABERTURA: {data.get('data_inicio_ativ') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] E-MAIL: {data.get('email') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] SÓCIOS PROPRIETÁRIOS: {', '.join(data.get('socios', 'SEM INFORMAÇÃO'))}")
                print(f"{C}[{L}+{C}] DATA DE ATUALIZAÇÃO: {data.get('data_situacao') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] QUALIFICAÇÃO DO RESPONSÁVEL: {data.get('qualif_resp') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] CIDADE NO EXTERIOR: {data.get('nm_cidade_exterior') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] CÓDIGO DO PAÍS EXTERIOR: {data.get('cod_pais') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] CAPITAL SOCIAL: {data.get('capital_social') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] OPÇÃO PELO SIMPLES: {data.get('opc_simples') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] DATA OPÇÃO PELO SIMPLES: {data.get('data_opc_simples') or 'SEM INFORMAÇÃO'}")
                print(f"{C}[{L}+{C}] CNAE FISCAL: {data.get('cnae_fiscal') or 'SEM INFORMAÇÃO'}")

                print("")
                creditos()

                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

            if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                cnpj_arquivo = f"CNPJ_{cnpj}.txt"
                caminho_arquivo = os.path.join(os.getcwd(), cnpj_arquivo)

                with open(caminho_arquivo, 'w') as arquivo:
                    arquivo.write(f"\n\nResultados da Consulta: {cnpj}\n\n")
                    arquivo.write("_________________________________________________________\n\n")
                    arquivo.write(f"- CNPJ: {data.get('cnpj') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- NOME FANTASIA: {data.get('nome_fantasia') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- RAZÃO SOCIAL: {data.get('razao_social') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- MATRIZ FILIAL: {data.get('matriz_filial') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- MOTIVO DA ABERTURA: {data.get('motivo_situacao') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- ENDEREÇO: {data.get('tipo_logradouro', 'SEM INFORMAÇÃO')}, {data.get('logradouro', 'SEM INFORMAÇÃO')}, {data.get('numero', 'SEM INFORMAÇÃO')} - {data.get('bairro', 'SEM INFORMAÇÃO')}\n")
                    arquivo.write(f"- CEP: {data.get('cep') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- MUNICÍPIO: {data.get('municipio', 'SEM INFORMAÇÃO')} - {data.get('uf', 'SEM INFORMAÇÃO')}\n")
                    arquivo.write(f"- COMPLEMENTO: {data.get('complemento') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- TELEFONE: {data.get('telefone_1') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- TELEFONE 2: {data.get('telefone_2') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- DATA DE ABERTURA: {data.get('data_inicio_ativ') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- E-MAIL: {data.get('email') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- SÓCIOS PROPRIETÁRIOS: {', '.join(data.get('socios', 'SEM INFORMAÇÃO'))}\n")
                    arquivo.write(f"- DATA DE ATUALIZAÇÃO: {data.get('data_situacao') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- QUALIFICAÇÃO DO RESPONSÁVEL: {data.get('qualif_resp') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- CIDADE NO EXTERIOR: {data.get('nm_cidade_exterior') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- CÓDIGO DO PAÍS EXTERIOR: {data.get('cod_pais') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- CAPITAL SOCIAL: {data.get('capital_social') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- OPÇÃO PELO SIMPLES: {data.get('opc_simples') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- DATA OPÇÃO PELO SIMPLES: {data.get('data_opc_simples') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- CNAE FISCAL: {data.get('cnae_fiscal') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write("_________________________________________________________\n")
                    arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                    arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {cnpj_arquivo}\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

            else:
                print ("")
                erro_cnpj()
                sleep(3)
                tipos()


    except Exception as e:
        print(R + "Erro:", e)
        tipos()


def consulta_operadora(operadora):

    url = f"http://apilayer.net/api/validate?access_key=317fca6d1dc194d6c5e5d16898b63ddf&number={operadora}&country_code=&format=1"

    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                operadora_info = data  

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                        {C}CHECKAR OPERADORA                         {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " CELULAR CONSULTADO:", (operadora_info.get('number') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " FORMATO INTERNACIONAL:", operadora_info.get('international_format') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " PAÍS DE ORIGEM:", operadora_info.get('country_name') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " REGIÃO:", operadora_info.get('location') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " PREFIXO DO PAÍS:", operadora_info.get('country_code') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " OPERADORA:", operadora_info.get('carrier') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TIPO DE OPERADORA:", operadora_info.get('line_type') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " VALIDADE DO NÚMERO:", operadora_info.get('valid') or 'SEM INFORMAÇÃO')

                print("")
                creditos()

                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

                if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                    
                    operadora_arquivo = f"OPERADORA_{operadora}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), operadora_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"\n\nResultados da Consulta de Operadora no número {operadora}\n\n")
                        arquivo.write("_________________________________________________________\n\n")
                        arquivo.write(f"- Celular consultado: {(operadora_info.get('number') or 'SEM INFORMAÇÃO').upper()}\n")
                        arquivo.write(f"- Formato Internacional: {operadora_info.get('international_format') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- País de origem: {operadora_info.get('country_name') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Região: {operadora_info.get('location') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Prefixo do País: {operadora_info.get('country_code') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Operadora: {operadora_info.get('carrier') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Tipo de operadora: {operadora_info.get('line_type') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Validade do número: {operadora_info.get('valid') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("_________________________________________________________\n")
                        arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {operadora_arquivo}\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_operadora()
            sleep(3)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def viacep(cep):

    url = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cep_viacep = data  

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                         {C}CONSULTA DE CEP                          {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " CEP:", (cep_viacep.get('cep') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " NOME DA RUA:", cep_viacep.get('logradouro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " BAIRRO:", cep_viacep.get('bairro') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CIDADE:", cep_viacep.get('localidade') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " ESTADO:", cep_viacep.get('uf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CÓDIGO IBGE:", cep_viacep.get('ibge') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " DDD:", cep_viacep.get('ddd') or 'SEM INFORMAÇÃO')
                print("")
                creditos()

                
                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

                if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                    
                    cep_arquivo = f"CEP_{cep}.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), cep_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"\n\nResultados da Consulta do CEP {cep}\n\n")
                        arquivo.write("_________________________________________________________\n\n")
                        arquivo.write(f"- CEP: {(cep_viacep.get('cep') or 'SEM INFORMAÇÃO').upper()}\n")
                        arquivo.write(f"- Nome da rua: {cep_viacep.get('logradouro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Bairro: {cep_viacep.get('bairro') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Cidade: {cep_viacep.get('localidade') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Estado: {cep_viacep.get('uf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Código IBGE: {cep_viacep.get('ibge') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- DDD: {cep_viacep.get('ddd') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("_________________________________________________________\n")
                        arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {cep_arquivo}\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_cep()
            sleep(3)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()

def bin_cc(bin):

    url = f"https://lookup.binlist.net/{bin}"

    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                bin_lookup = data  

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                        {C}CONSULTA DE BIN                           {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " BIN:", bin_lookup.get("{bin}") or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " MODELO:", (bin_lookup.get('type') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " BANDEIRA:", (bin_lookup.get('scheme') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " NÍVEL:", (bin_lookup.get('brand') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " PAÍS:", (bin_lookup.get("country", {}).get("name") or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " SIGLA DO PAÍS:", bin_lookup.get("country", {}).get("alpha2") or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " MOEDA USADA NO PAÍS:", bin_lookup.get("country", {}).get("currency") or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " BANCO:", (bin_lookup.get("bank", {}).get("name") or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " SITE DO BANCO:", bin_lookup.get("bank", {}).get("url") or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " TELEFONE:", bin_lookup.get("bank", {}).get("phone") or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CIDADE:", (bin_lookup.get("bank", {}).get("city") or 'SEM INFORMAÇÃO').upper())
                print("")
                creditos()

                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_bin()
            sleep(3)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()









def gerarpessoa():

    url = f"https://api.invertexto.com/v1/faker?token=4616%7CdEehBVzCGLelV7ORmXhmRxgdROmglDok&locale=pt_BR"

    response = requests.get(url)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                gerador = data 

                print("")
                print(f"{L}╔════════════════════════════════════════════════════════════════╗")
                print(f"{L}                         {C}GERADOR DE PESSOA                          {L}")
                print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
                
                print(f"{C}[{L}+{C}]" " NOME:", (gerador.get('name') or 'SEM INFORMAÇÃO').upper())
                print(f"{C}[{L}+{C}]" " CPF:", gerador.get('cpf') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " DATA DE NASCIMENTO:", gerador.get('birth_date') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " EMAIL:", gerador.get('email') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DE USUÁRIO:", gerador.get('username') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NÚMERO DE TELEFONE:", gerador.get('phone_number') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " SITE HOSPEDADO:", gerador.get('domain_name') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " CNPJ:", gerador.get('cnpj') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NOME DA EMPRESA:", gerador.get('company') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " IP REVERSO DE HOSPEDAGEM:", gerador.get('ipv4') or 'SEM INFORMAÇÃO')
                print(f"{C}[{L}+{C}]" " NAVEGADOR:", gerador.get('user_agent') or 'SEM INFORMAÇÃO')
                print("")
                creditos()

                salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

                if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                    
                    gerador_arquivo = f"PESSOA_GERADA.txt"
                    caminho_arquivo = os.path.join(os.getcwd(), gerador_arquivo)

                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.write(f"\n\nResultados do Gerador\n\n")
                        arquivo.write("_________________________________________________________\n\n")
                        arquivo.write(f"- Nome: {(gerador.get('name') or 'SEM INFORMAÇÃO').upper()}\n")
                        arquivo.write(f"- CPF: {gerador.get('cpf') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Data de nascimento: {gerador.get('birth_date') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- E-mail: {gerador.get('email') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome de usuário: {gerador.get('username') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Número de telefone: {gerador.get('phone_number') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Site hospedado: {gerador.get('domain_name') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- CNPJ: {gerador.get('cnpj') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Nome da Empresa: {gerador.get('company') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- IP Reverso de hospedagem: {gerador.get('ipv4') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write(f"- Navegador: {gerador.get('user_agent') or 'SEM INFORMAÇÃO'}\n")
                        arquivo.write("_________________________________________________________\n")
                        arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                        arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {gerador_arquivo}\n")
                
                nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
                os.system('cls' if os.name == 'nt' else 'clear')

                if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
                    tipos()
                else:
                    tchau()

        else:
            print ("")
            erro_gerar_pessoa()
            sleep(3)
            tipos()

    except Exception as e:
        print(R + "Erro:", e)
        tipos()






def gerarcartao():


    url = requests.get(f"https://api.invertexto.com/v1/faker?token=4616%7CdEehBVzCGLelV7ORmXhmRxgdROmglDok&locale=pt_BR").json()

    random_numbers = [random.randint(100, 999) for _ in range(1)]
                
    for i, num in enumerate(random_numbers, start=1):


        print("")
        print(f"{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"{L}                  {C}GERADOR DE CARTÃO DE CRÉDITO                    {L}")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        
        print(f"{C}[{L}+{C}]" " NÚMERO DO CARTÃO:", (url.get("credit_card", {}).get("number") or 'SEM INFORMAÇÃO').upper())
        print(f"{C}[{L}+{C}]" " DATA DE EXPIRAÇÃO:", url.get("credit_card", {}).get("expiration") or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " BANDEIRA DO CARTÃO:", url.get("credit_card", {}).get("type") or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " CVV DO CARTÃO:", num or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " NOME IMPRESSO NO CARTÃO:", url.get("credit_card", {}).get("name") or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " CPF DO TITULAR:", url.get("cpf") or 'SEM INFORMAÇÃO\n\n')
        print(f"\n[{B}!{C}] OBS: OS DADOS GERADOS SÃO FICTÍCIOS, QUALQUER SEMELHANÇA É MERA COINCIDÊNCIA!")

        print("")
        creditos()

        salvar_arquivo = input(
            C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
        ).lower()

        if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
            
            cartao_arquivo = f"CC_GERADO.txt"
            caminho_arquivo = os.path.join(os.getcwd(), cartao_arquivo)

            with open(caminho_arquivo, 'w') as arquivo:
                arquivo.write(f"\n\nResultados do Gerador\n\n")
                arquivo.write("_________________________________________________________\n\n")
                arquivo.write(f"- Numero do Cartão: {url.get('credit_card', {}).get('number') or 'SEM INFORMAÇÃO'}\n")
                arquivo.write(f"- Data de Expiração: {url.get('credit_card', {}).get('expiration') or 'SEM INFORMAÇÃO'}\n")
                arquivo.write(f"- Bandeira do cartão: {url.get('credit_card', {}).get('type') or 'SEM INFORMAÇÃO'}\n")
                arquivo.write(f"- CVV do cartão: {num}\n")
                arquivo.write(f"- Nome impresso no cartão: {url.get('credit_card', {}).get('name') or 'SEM INFORMAÇÃO'}\n")
                arquivo.write(f"- CPF do titular: {url.get('cpf') or 'SEM INFORMAÇÃO'}\n\n\n")
                arquivo.write("OBS: Os dados gerados são fictícios, qualquer semelhança é mera coincidência!\n")
                arquivo.write("_________________________________________________________\n")
                arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                arquivo.write("                       Created By offalien                      \n")


            print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {cartao_arquivo}\n")
        
        nova = input(
            C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
        ).lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
            tipos()
        else:
            tchau()


def busca_ip():

    ip = input(C + f"[{L}*{C}] DIGITE A NÚMERO DE IP A SER CONSULTADO: " + C)

    url = requests.get(f'http://ipwhois.app/json/{ip}')

    json = url.json()

    if url.status_code == 200:

        print("")
        print(f"{L}╔════════════════════════════════════════════════════════════════╗")
        print(f"{L}                        {C}CONSULTA DE IP                            {L}")
        print(f"{L}╚════════════════════════════════════════════════════════════════╝\n")
        
        print(f"{C}[{L}+{C}]" " IP:", json.get('ip') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " ATIVO:", json.get('success') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " TIPO:", json.get('type') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " CIDADE:", json.get('city') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " ESTADO:", json.get('region') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " PAÍS:", json.get('country') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " SIGLA DO PAÍS:", json.get('country_code') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " DDI DO PAÍS:", json.get('country_phone') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " CONTINENTE:", json.get('continent') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " LATITUDE:", json.get('latitude') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " LONGITUDE:", json.get('longitude') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " PROVEDOR:", json.get('isp') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " ORGANIZAÇÃO:", json.get('org') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " ASN:", json.get('asn') or 'SEM INFORMAÇÃO')
        print(f"{C}[{L}+{C}]" " EMPRESA RESPONSÁVEL:", json.get('org') or 'SEM INFORMAÇÃO\n\n')
        print("")
        creditos()


        salvar_arquivo = input(
                    C + f"[{L}?{C}] DESEJA SALVAR OS RESULTADOS EM UM ARQUIVO? [{G}S{C}/{R}N{C}]: "
                ).lower()

        if salvar_arquivo == "s" or salvar_arquivo == "sim" or salvar_arquivo == "y" or salvar_arquivo == "yes":
                ip_caminho = f"RG_{ip}.txt"
                caminho_arquivo = os.path.join(os.getcwd(), ip_caminho)

                with open(caminho_arquivo, 'w') as arquivo:

                    arquivo.write(f"\n\nResultados da Busca pelo IP {ip}\n\n")
                    arquivo.write("_________________________________________________________\n\n")
                    arquivo.write(f"- IP: {(json.get('ip') or 'SEM INFORMAÇÃO')}\n")
                    arquivo.write(f"- Ativo: {json.get('success') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Tipo de conexão: {json.get('type') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Cidade: {json.get('city') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Estado: {json.get('region') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- País: {json.get('country') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Sigla do País: {json.get('country_code') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- DDI Do País: {json.get('country_phone') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Continente: {json.get('continent') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Latitude: {json.get('latitude') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Longitude: {json.get('longitude') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Provedor: {json.get('isp') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Organização: {json.get('org') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- ASN: {json.get('asn') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write(f"- Empresa Responsável: {json.get('org') or 'SEM INFORMAÇÃO'}\n")
                    arquivo.write("_________________________________________________________\n")
                    arquivo.write("\n                 Bad Bitch © All Rights Reserved               \n")
                    arquivo.write("                       Created By offalien                      \n")

                    print(f"{G}[{C}+{G}] OS RESULTADOS FORAM SALVOS COM SUCESSO NO ARQUIVO {ip_caminho}\n")
            
        nova = input(
                    C + f"[{L}?{C}] DESEJA REALIZAR UMA NOVA CONSULTA? [{G}S{C}/{R}N{C}]: "
                ).lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        if nova == "s" or nova == "sim" or nova == "y" or nova == "yes":
            tipos()
        else:
            tchau()

    else:
        print ("")
        erro_ip()
        sleep(3)
        tipos()


















if __name__ == '__main__':
    try:
        tipos()

    except Exception as e:
        print(C + f"Erro: {R}{e}" + RT)

    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        