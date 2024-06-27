# Todo List App

## Descrição

Esta é uma aplicação web simples de lista de tarefas (to-do list) desenvolvida com Flask, dockerizada usando Docker e Docker Compose.

## Pré-requisitos

- Docker
- Docker Compose

## Construção e Execução dos Contêineres

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/todo-list-app.git
    cd todo-list-app
    ```

2. Construa e inicie os contêineres:
    ```bash
    docker-compose up --build
    ```

3. A aplicação estará disponível em `http://localhost:5000`.

## Endpoints

- `GET /tasks` - Retorna todas as tarefas
- `POST /tasks` - Adiciona uma nova tarefa
- `DELETE /tasks/<id>` - Remove uma tarefa pelo ID

## Persistência de Dados

Os dados do banco de dados são persistidos utilizando volumes do Docker. Mesmo que os contêineres sejam destruídos, os dados permanecerão no volume `postgres_data`.
