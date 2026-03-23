import os

ambiente = os.environ['MMEU_AMBIENTE']

def exibirLog(mensagem):
    print("Log para monitoramento:", mensagem)
    print("AMBIENTE:", ambiente)

