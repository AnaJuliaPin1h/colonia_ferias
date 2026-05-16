# 🏖️ Sistema de Reservas — Colônia de Férias

Sistema web para gerenciamento de reservas de apartamentos em colônia de férias corporativa, desenvolvido com Django, Django REST Framework e JavaScript puro.

---

## 📋 Funcionalidades

- Cadastro de reservas com nome do responsável, tipo de apartamento, número de pessoas e dias
- Cálculo automático do valor total com base na tabela de preços
- API REST completa (criar, listar, editar, excluir reservas)
- Geração de comprovante em PDF
- Interface web responsiva

---

## 🛠️ Tecnologias utilizadas

| Camada | Tecnologia |
|---|---|
| Backend | Python 3 + Django 4+ |
| API | Django REST Framework |
| Banco de dados | SQLite (dev) / MySQL (prod) |
| PDF | ReportLab |
| Frontend | HTML, CSS, JavaScript puro |
| CORS | django-cors-headers |

---

## 📁 Estrutura do projeto

```
colonia_ferias/
├── reservas/              # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/                   # App principal
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── manage.py
└── requirements.txt
```

---

## 💰 Tabela de preços

| Pessoas | Tipo 1 (diária) | Tipo 2 (diária) |
|:---:|:---:|:---:|
| 1 | R$ 20,00 | R$ 25,00 |
| 2 | R$ 28,00 | R$ 34,00 |
| 3 | R$ 35,00 | R$ 42,00 |
| 4 | R$ 42,00 | R$ 50,00 |
| 5 | R$ 48,00 | R$ 57,00 |
| 6 | R$ 53,00 | R$ 63,00 |

---

## 🚀 Como rodar o projeto localmente

### Pré-requisitos

- Python 3.10+
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/colonia-ferias.git
cd colonia-ferias
```

### 2. Crie e ative o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as migrations

```bash
python manage.py makemigrations app
python manage.py migrate
```

### 5. Rode o servidor

```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔌 Endpoints da API

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/reservas/` | Lista todas as reservas |
| POST | `/api/reservas/` | Cria uma nova reserva |
| GET | `/api/reservas/{id}/` | Detalha uma reserva |
| PUT | `/api/reservas/{id}/` | Atualiza uma reserva |
| DELETE | `/api/reservas/{id}/` | Remove uma reserva |
| GET | `/pdf/{id}/` | Gera comprovante em PDF |

### Exemplo de requisição POST

```json
{
  "nome": "Ana Julia",
  "tipo": 1,
  "pessoas": 2,
  "dias": 5
}
```

### Exemplo de resposta

```json
{
  "id": 1,
  "nome": "Ana Julia",
  "tipo": 1,
  "pessoas": 2,
  "dias": 5,
  "valor_total": "140.00",
  "total": "140.00",
  "criado_em": "2025-01-01T12:00:00Z"
}
```

---

## 📦 requirements.txt

```
django
djangorestframework
django-cors-headers
reportlab
```

Gere o seu com:

```bash
pip freeze > requirements.txt
```

---

## 👩‍💻 Autora

Desenvolvido por **Ana Julia Pinheiro**
