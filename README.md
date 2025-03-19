# 📦 Emprestaii - Backend API

Este projeto faz parte da aplicação **Emprestaii**, um sistema para **controle e organização de itens pessoais emprestados**, com autenticação segura, histórico de empréstimos, CRUDs e permissões por usuário.

---

## ✅ Funcionalidades Implementadas

### 🔐 Módulo `users/` – Autenticação e gerenciamento de usuários
- Modelo de usuário customizado (`CustomUser`)
  - `email` (obrigatório, único – usado como login)
  - `username` (opcional)
  - `name`, `phone`, `address` (model separada)
- Autenticação JWT com `djangorestframework-simplejwt`
- Funcionalidades:
  - Registro de usuários: `/api/users/register/`
  - Login via email e senha: `/api/users/login/`
  - Refresh token: `/api/users/token/refresh/`
  - Logout com blacklist: `/api/users/logout/`
  - Perfil do usuário logado: `/api/users/profile/`
- Integração com Django Admin personalizada

### 📦 Módulo `items/` – Cadastro e gerenciamento de itens
- CRUD completo de itens
  - Campos: `name`, `description`, `category`, `status`, `owner`
- Filtro por `status` e `category`
- Busca por `name` e `description`
- Permissão por usuário: cada usuário vê apenas seus próprios itens
- Integração com Django Admin

---

## 🔐 Autenticação JWT
- Login via `/api/users/login/` retorna `access` e `refresh` tokens
- `access_token` tem duração curta (ex: 5 minutos)
- `refresh_token` dura mais (ex: 7 dias) e pode ser revogado no logout
- Logout com blacklist de `refresh_token` impede novas sessões com token antigo
- Após logout, o frontend deve remover o access token localmente

---

## 🚀 Como iniciar o projeto com Docker

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/emprestaii.git
```

### 2. Acesse a pasta do projeto
```bash
cd emprestaii
```

### 3. Suba os containers com Docker Compose
```bash
docker-compose up --build
```

### 4. Acesse a aplicação:
- API: [http://localhost:8000/api/](http://localhost:8000/api/)
- Django Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### 5. Criar superusuário (opcional)
```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 📂 Estrutura de diretórios relevante
```
emprestaii/
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── items/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── emprestaii/         ← config (settings, urls)
├── requirements.txt
└── docker-compose.yml
```

---

## 📌 Observações técnicas
- API protegida por JWT (via `Authorization: Bearer <token>`)
- Uso de `DefaultRouter` do DRF para organização de rotas
- Itens são automaticamente vinculados ao usuário autenticado
- Endpoints bem definidos para facilitar integração com frontend (ex: React)

---

## ✍️ Desenvolvimento Futuro
- Módulo `loans/` – controle de empréstimos (próxima etapa)
- Módulo `contacts/` – agenda pessoal de contatos (opcional)
- Testes automatizados com `pytest`
- Documentação com Swagger/OpenAPI
- Notificações e dashboard (funcionalidades extra para portfólio)

---

**Desenvolvido por:** Projeto Emprestaii Backend – Django + Django REST Framework
