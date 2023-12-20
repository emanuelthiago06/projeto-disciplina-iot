Nesse projeto a conexão com o proxy é feito no main.py, o restante do projeto está no servidor django que está na mesma raiz do main.py
o código para se estabelecer a comunicação com o proxy e o servidor está em main.py
Para rodar o servidor execute o comando python3 manage.py runserver
Com o servidor funcionando navegue para /api/initial-page, lá é preciso colocar o id do sensor a ser visualizado, feito isso clicar no botão e então será feito um redirecionamento para a página de vi
sualização do gráfico

