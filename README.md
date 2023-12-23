
# Documentação do Projeto Disciplina IoT

## Descrição do Projeto

O projeto foi desenvolvido como projeto final para a disciplina de Internet das Coisas (IoT) do mestrado em Engenharia Elétrica do IFPB. O onjetivo era implementar um sistema funcional de ponta a ponta de comunicação de dispositivos LoRa.

## Estrutura do Projeto

Este repositorio conta apenas com a parte Web do projeto, nela foram desenvolvidas dois módulos: um proxy que lê uma fila rabbitMQ e envia os dados via post para o servidor web; e um servidor django que armazena as informações recebidas em um banco de dados para posterior visualização através por usuários.

### Como utilizar:

Para o uso correto você deve criar um arquivo ``.env`` na raiz do projeto com as seguintes váriaveis de ambiente:

- ``RMQ_HOT`` que indica o host da fila RabbitMQ;
- ``WEB_HOST`` que indica o host do servidor web, ou seja, o ip da maquina que você está subindo o projeto;
- ``WEB_PORT`` que é a porta em que o servidor web está utilizando. 

Após definir o arquivo ``.env``, para executar o projeto você deve utilizar ``sudo docker compose up --build`` na raiz do repositório. 

Para mais detalhes de como se comunicar o servidor web, leia o readme do diretório ``web-server``.
