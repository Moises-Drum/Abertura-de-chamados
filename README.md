# Projeto Abertura de Chamados

Neste repositório, trato da troca de informações entre usuários utilizando a linguagem Python, especialmente quando ocorre em máquinas diferentes. Emprego pacotes como Threading e Socket para criar um servidor que facilita essa comunicação.

## Preparação

- Para iniciar, execute primeiro o arquivo **servidor.py** para garantir o funcionamento adequado dos demais arquivos.
- Após, incie os arquivos **cliente.py** e **tecnico.py** e teste a aplicação.

## Observação

É possível realizar a conexão em diferentes máquinas. <br>

<img src="/ImagemTutorial/host.jpeg" width="550"/> <br><br>

Para garantir o correto funcionamento, certifique-se de que a variável host em todos os arquivos esteja configurada com o mesmo IP utilizado no arquivo servidor.py. Se os arquivos estiverem distribuídos em máquinas distintas, mas compartilharem o mesmo IP do servidor.py, o código operará sem problemas.<br>
OBS. o código `socket.gethostbyname(socket.gethostbyname())` pega automaticamente o IP da máquina local.

## Finalização

Este repositório reflete parte dos meus estudos sobre a conexão e troca de informações entre diferentes máquinas ou usuários.
