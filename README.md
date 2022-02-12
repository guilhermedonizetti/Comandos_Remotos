<h1 align="center">Comandos_Remotos</h1>
<p align="center">
Interagir remotamento com o computador através do Python e protocolo MQTT. :computer:<br>
<i>Status: em desenvolvimento :vertical_traffic_light:</i>
</p>

<b>Objetivo:</b> Interagir com o computador usando o celular, o envio dos comandos acontecem através do protocolo MQTT (<i>Message Queuing Telemetry Transport</i>). Assim, pode-se executar tarefas báscias no computador sem a necessidade de estar próximo a ele.

<b>Funcionamento:</b> Conforme as regras de uso do MQTT, o programa se conecta como subscriber em um tópico específico do broker e aguarda que chegue mensagens telemétricas. Ao receber qualquer mensagem executa as etapas abaixo:<br>
<br>
:arrow_right: <b>Verifica se é link:</b> se a mensagem recebida possuir característica de link, o programa irá iniciar esse conteúdo no navegador padrão.<br>
:arrow_right: <b>Verifica se é um programa:</b> se a mensagem transmitida para o computador for o nome de um software (ex.: Postman), o programa vai iniciar esse software.<br>

<b>Comunicação:</b> Para transmitir os comandos do celular para o notebook, foi usado o aplicativo MQTT Dash que permite conectar a brokers e publicar ou receber cargas úteis. No caso, foi usado unicamente para publicar mensagens. Foi usado o broker remoto de teste TestMosquitto. O celular transmite as mensagens para esse destino e o programa que executa no computador se conecta a esse broker para receber as mensagens, ou seja, o celular pode estar em qualquer distância do computador, pois a conexão é realmente remota.

<p align="center">
<b>MQTT, Python, Telemetria</b><br>Guilherme Donizetti - 2022
</p>
