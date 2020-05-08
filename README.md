# blog_python
Aplicativo de blog simples do Django

 ! [blog] (https://github.com/glaubermarcelino/blog_python/blob/master/pics/main.png)

Para mais fotos, consulte o diretório `pics`.

Recursos
--------
1. Autorização e registro do usuário
2. Permissões básicas do usuário: administrador, editor, normal.
- Os editores podem adicionar postagens, atualizar / excluir os existentes para os quais eles são adequados
permissões / propriedade.
- admin é superusuário como de costume.
3. Comentários no Facebook
4. Tags
5. Pesquise, arquivos ano / mês, classifique por autor do post, categoria, tags.
6. API REST básica fornecida pela estrutura REST do Django (disponível em `/ api`)

Principais requisitos
------------

1. `python` 3.5, 3.6, 3.7
2. `Django` 2.1.8
3. `PostreSQL` 11.1

Este projeto também usa alguns pacotes externos (consulte o arquivo `requirements.txt` para obter detalhes).
Por exemplo, o suporte a tags é fornecido pelo [django-taggit] (https://github.com/alex/django-taggit).


## Como configurar

### Configurar usando o Docker

A maneira mais fácil de colocar esse projeto em funcionamento é via [Docker] (https://www.docker.com/). Consulte [docs] (https://docs.docker.com/get-started/) para começar. Depois de configurado, execute o seguinte comando:

`docker-compor up`

Pode demorar um pouco para que o processo seja concluído, pois o Docker precisa obter as dependências necessárias. Uma vez feito, o aplicativo deve estar acessível em `0.0.0.0:8000`.

### Configuração manual

Primeiro, crie um novo diretório e mude para ele:

`mkdir blog_django && cd blog_django`

Em seguida, clone este repositório no diretório atual:

`git clone https://github.com/glaubermarcelino/blog_python.git .`


Em seguida, é necessário configurar o banco de dados como SQLite ou PostgreSQL em uma máquina local. Este projeto usa o PostgreSQL por padrão (veja [documentação do Django] (https://docs.djangoproject.com/en/2.1/ref/settings/#databases) para configurações diferentes). Esse processo pode variar de um sistema operacional para outro, por exemplo. no Arch Linux, pode-se seguir um guia direto [aqui] (https://wiki.archlinux.org/index.php/PostgreSQL).

As configurações do banco de dados são especificadas em `website/settings/local.py`. Em particular, o nome padrão do banco de dados é `BlogDjango`, que pode ser criado a partir do shell do PostgreSQL executando` createdb BlogDjango`.


Em seguida, configure um ambiente virtual e ative-o:

`python -m venv env && fonte env/bin/enable`

Instale os pacotes necessários:

`pip install -r requirements.txt`

Em seguida, execute a migração:

`python manage.py migrate --settings = website.settings.local`

A instalação está completa. Execute um servidor local com

`python manage.py runserver --settings = website.settings.local`

O blog deve estar disponível em `localhost: 8000`.

## Qual é o próximo?

Nesse ponto, convém criar uma conta de superusuário, criar o grupo Editores e adicionar alguns usuários a esse grupo.
