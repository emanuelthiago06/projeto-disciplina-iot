# Projeto de Conexão com Proxy e Servidor Django

## Primeiros passos

Antes de instalar as bibliotecas é recomendado criar uma venv para separar as versões e bibliotecas do projeto do python do seu sistema, ela é instalada com o seguinte comando:

```bash
python3 -m venv venv
```

Uma vez ela instalada é preciso ativa-la para isso digite o comando:

Linux/MacOs:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Feito isso agora será falta a instalação das bibliotecas, se voce decidiu pular os passos para fazer a venv a instalação das bibliotecas será feita no python do seu sistema, não nos responsabilizamos por problemas.

```bash
pip install -r requirements.txt
```

## Executando a conexão com o proxy

O código responsável por estabelecer a comunicação com o proxy e o servidor está contido no arquivo `main.py`.

Para executar ele basta rodar ele, e se for o desejo mudar os valores de "value" e "id" para os valores e id o sensor a ser enviado

```bash
python3 main.py
```

## Executando o servidor

Para rodar o servidor execute o comando python3 manage.py runserver

Com o servidor funcionando navegue para /api/initial-page, lá é preciso colocar o id do sensor a ser visualizado, feito isso clicar no botão e então será feito um redirecionamento para a página de vi
sualização do gráfico

O servidor só recebe o dado via requisição, não existe forma de colocar os dados na página web, para fazer a requisição é preciso fazer um POST para o endereço /api/add-point com o payload contendo a valor do sensor "value" e o identificador do sensor "id", como mostrado a seguir:

```json
{
"value": "valor do sensor",
"id": "id do sensor",
}
```

Para iniciar o servidor, utilize o seguinte comando:

```bash
python3 manage.py runserver
