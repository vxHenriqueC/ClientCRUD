# ClientCRUD

Sistema CRUD de gerenciamento de clientes desenvolvido em Python com SQLite.

## Funcionalidades

- Cadastro de clientes
- Listagem de clientes
- Busca por ID
- Atualização de dados
- Exclusão de clientes

## Tecnologias utilizadas

- Python
- SQLite

## Estrutura do projeto

```bash
ClientCRUD/
│
├── main.py
├── clients.py
├── db.py
└── clientflow.db
```

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/clientcrud.git
```

### 2. Acesse a pasta do projeto

```bash
cd clientcrud
```

### 3. Execute o projeto

```bash
python main.py
```

## Banco de dados

O banco de dados é criado automaticamente utilizando SQLite.

Arquivo gerado automaticamente:

```bash
clientflow.db
```

Tabela criada:

```sql
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    company TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Operações disponíveis

### Criar cliente

```text
1 - Create client
```

### Listar clientes

```text
2 - List clients
```

### Buscar cliente

```text
3 - Search client
```

### Atualizar cliente

```text
4 - Update client
```

### Deletar cliente

```text
5 - Delete client
```

## Exemplo de execução

```text
=== CLIENTFLOW ===
1 - Create client
2 - List clients
3 - Search client
4 - Update client
5 - Delete client
0 - Exit
```

## Objetivo do projeto

Projeto desenvolvido com foco em aprendizado e prática de:

- CRUD
- Integração Python + Banco de Dados
- SQLite
- SQL
- Estruturação de aplicações backend
- Manipulação de dados

## Autor

Henrique Conton Chiaretti
