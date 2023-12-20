# Projeto de Conexão com Proxy e Servidor Django

## Executando a conexão com o proxy

O código responsável por estabelecer a comunicação com o proxy e o servidor está contido no arquivo `main.py`.

Para executar ele basta rodar ele, e se for o desejo mudar os valores de "value" e "id" para os valores e id o sensor a ser enviado


## Executando o servidor

Para rodar o servidor execute o comando python3 manage.py runserver

Com o servidor funcionando navegue para /api/initial-page, lá é preciso colocar o id do sensor a ser visualizado, feito isso clicar no botão e então será feito um redirecionamento para a página de vi
sualização do gráfico

O servidor só recebe o dado via requisição, não existe forma de colocar os dados na página web, para fazer a requisição é só fazer um POST para o endereço /api/add-point com o payload contendo a valor do sensor "value" e o identificador do sensor "id"

```bash
python3 manage.py runserver
