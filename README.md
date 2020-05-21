# user-preferences
Microserviço responsável por gerenciar as preferências dos usuários, i.e. os likes e dislikes.

### Construindo Imagem
Execute o comando:
```shell script
docker build -t user-preferences .
```
Isso irá gerar uma imagem docker (_user-preferences:latest_) localmente.

### Testando Local
Execute o comando:
```shell script
docker-compose up
```
Isso irá subir um banco de dados Mongodb na porta 27017. Rode a aplicação.
Caso seja necessário, altera as propriedades de execução da aplicação em [application.ini](application.ini).

### Documentação da API
Acesse [/swagger](src/web/serverconfig/static/swagger.json) para visualizar a documentação de API da aplicação.