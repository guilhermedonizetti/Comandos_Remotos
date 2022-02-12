import paho.mqtt.subscribe as subscribe
import funcoes as fc
from webbrowser import open
from os import execl, sync

x = True
while x == True:

    msg = subscribe.simple("remotoTeste/Gui", hostname="test.mosquitto.org", port=1883)
    comando = msg.payload.decode("utf8")

    # Verifica se foi informado um link para abrir no navegador
    link = fc.verificarLink(comando)
    if link:
        open(comando)
    
    # Verifica se foi informado um programa para ser iniciado
    status, caminho = fc.verificarPrograma(comando)
    if status:
        sync()
        execl(caminho, "code")
    
    # Verifica se deve encerrar o programa
    try:
        if int(comando) == 0:
            x = False
    except:
        pass
