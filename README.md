# fatech

É recomendado o uso de um [ambiente virtual do python](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/development_environment#usando_django_em_um_ambiente_virtual_python) para evitar conflitos de pacotes pip, mas é possivel rodar sem ele.

Instalando o Django:
```
python3 -m pip install django
```
Na pasta do repositório, faça as migrações das tabelas:
```
python3 manage.py makemigrations
python3 manage.py migrate
````
Crie um super usuário Django:
```
python3 manage.py createsuperuser
```
rode o rodar.bat
ou
lan.bat

