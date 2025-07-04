# 🚀 Tech Blog - Portfólio Django

![Screenshot da página inicial do Blog Tech](docs/images/screenshot-blog.png)

Este é um projeto de blog de notícias de tecnologia construído com Django desenvolvi para aprimorar minhas habilidades, focado em boas práticas de desenvolvimento, performance e otimização para motores de busca (SEO). Nele, foquei em implementar um sistema seguro, com boas práticas de SEO e um layout responsivo, demonstrando os principais conceitos do framework.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

### ✨ Funcionalidades Principais

* **Sistema de Posts e Categorias:** Criação de conteúdo dinâmico através do painel de administração do Django.
* **SEO Técnico:** Meta tags (`<title>`, `description`, `keywords`) geradas dinamicamente para cada post e URLs amigáveis (slugs).
* **Otimização de Performance:** Uso de `select_related` nas queries para reduzir o número de acessos ao banco de dados.
* **Gerenciamento de Mídia:** Sistema de upload de imagens para os posts.
* **Design Responsivo:** Layout construído com Bootstrap 5, adaptável a desktops e dispositivos móveis.
* **Segurança:** Chaves secretas e configurações sensíveis gerenciadas com variáveis de ambiente (`.env` e `python-decouple`), garantindo que nenhum dado sensível seja exposto no repositório.

---

### 🛠️ Como Executar o Projeto Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/blog-django-portfolio.git](https://github.com/SEU-USUARIO/blog-django-portfolio.git)
    cd blog-django-portfolio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt 
    ```

4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione as seguintes variáveis:
        ```env
        SECRET_KEY=sua_propria_chave_secreta_aqui
        DEBUG=True
        ```

5.  **Aplique as migrações e inicie o servidor:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser # Opcional, para criar um admin
    python manage.py runserver
    ```

6.  Acesse `http://127.0.0.1:8000/` no seu navegador.