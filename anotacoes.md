# comandos principais do django
Para criar um ambiente virtual -> python -m venv venv
No Windows, para ativar o ambiente virtual utilizamos . Ex: venv\Scripts\activate
Para instalar o django no projeto -> pip install django
Para criar um projeto Django -> django-admin startproject project .
Para subir o servidor, utilizamos -> python manage.py runserver
Para criar um novo APP -> python manage.py startapp home
Para realizar a coleta dos arquivos estáticos -> python manage.py collectstatic
Para desativar a venv no projeto django -> deactivate

# Ações das migrações

Para preparar as migrações -> python manage.py makemigrations
Para realizar as migrações -> python manage.py migrate
Criando e modificando a senha do super usuário Django
Para criar o superuser -> python manage.py createsuperuser
Para alterar a senha, caso você esqueça -> python manage.py changepassword nomedousuario