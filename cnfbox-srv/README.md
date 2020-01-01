# CnfBox SRV

REST APIが動く．Google App Engineでの動作を確認している．

## development

```
FLASK_APP=main.py python3 -m flask run
```

## deployment

```
gcloud components install app-engine-python
gcloud app deploy
```
