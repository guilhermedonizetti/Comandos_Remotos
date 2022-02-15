import paho.mqtt.subscribe as subscribe
import funcoes as fc
from webbrowser import open
from os import execl, system

x = True
while x == True:

    msg = subscribe.simple(["remotoTeste/Gui", "remotoTeste/Gui/Desligar"], hostname="test.mosquitto.org", port=1883)
    comando = msg.payload.decode("utf8")

    # Verifica se foi informado um link para abrir no navegador
    link = fc.verificarLink(comando)
    if link:
        open(comando)
    
    # Verifica se foi informado um programa para ser iniciado
    status, caminho = fc.verificarPrograma(comando)
    if status:
        execl(caminho, "code")

    # Verifica se deve desligar o computador
    if comando == "Desligar":
        system("shutdown /s /t 1")
    
    # Verifica se deve encerrar o programa
    try:
        if int(comando) == 0:
            x = False
    except:
        pass
