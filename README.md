# fatech - Python3
```
Bruno Silva de Araujo      | bruno.araujo37@fatec.sp.gov.br
Daniel Gomes Dias          | daniel.dias19@fatec.sp.gov.br
Gustavo Henrique Santos    | gustavo.santos173@fatec.sp.gov.br
Renan Andrade de Morais    | renan.morais5@fatec.sp.gov.br
Thainá Cristina Peres Cota | thaina.cota@fatec.sp.gov.br
```

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

