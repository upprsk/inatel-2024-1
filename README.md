# Trabalho 1

Crie um programa cliente servidor que envia duas questões em sequência de
múltipla escolha para um cliente após este se conectar, o cliente deve responder
às questões e o servidor retornar com quantas questões acertou, mostrando em uma
lista o acerto/erro de cada. Criar um banco de dados para as questões no servidor.
O banco de dados deve estar dockerizado. A escolha do banco é livre. Exemplo de questão:

Qual é a capital da Itália?

- a) Roma;
- b) Paris;
- c) Lisboa;
- d) Londres

Enviar um link do github do trabalho onde deve estar documentado e com todos os
arquivos utilizados. Pode ser feito em grupos de até duas pessoas.

## Uso (linux)

O banco de dados usado é o [rqlite](https://github.com/rqlite/rqlite), e pode ser
usado no docker:

```bash
docker run -p4001:4001 rqlite/rqlite
```

Deve-se criar um `venv` para a biblioteca do banco de dados.

```bash
python -m .venv venv
source .venv/bin/activate
pip install -r requirements.txt
```

Depois é possível rodar o servidor:

```bash
python server.py "" 6969
```

E o cliente (em outro terminal):

```bash
python client.py localhost 6969
```

Pode-se também usar qualquer cliente TCP:

```bash
netcat localhost 6969
```
