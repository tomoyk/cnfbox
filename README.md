## CLI

```
python -m venv env
. env/bin/activate
pip install -r requirements.txt
python -i example.py
```

## SRV

```
python -m venv env
. env/bin/activate
pip install -r requirements.txt

DB_HOST='xx.xx.xx.xx' \
DB_USER='root' \
DB_PASSWD='skjfff' \
DB_NAME='dev' \
FLASK_APP=main.py python3 -m flask run
```

### DB

```
mysql> desc config;
+---------+---------+------+-----+---------+----------------+
| Field   | Type    | Null | Key | Default | Extra          |
+---------+---------+------+-----+---------+----------------+
| id      | int(11) | NO   | PRI | NULL    | auto_increment |
| content | json    | YES  |     | NULL    |                |
+---------+---------+------+-----+---------+----------------+
2 rows in set (0.14 sec)
```

### Deploy app to GAE

write app.yaml below.

```
# [START gae_python37_custom_runtime]
runtime: python37
env_variables:
  DB_HOST: "x.x.x.x"
  DB_USER: "xxxx"
  DB_PASSWD: "yyyyyyyyyyyyyyyyy"
  DB_NAME: "zzz"
  UNIX_SOCKET: "/cloudsql/project-id:us-central1:project-store"
entrypoint: uwsgi --http-socket :8080 --wsgi-file main.py --callable app --master --processes 1 --threads 2
```

deploy to gae by using gcloud command.

```
gcloud components install app-engine-python
gcloud app deploy
```

