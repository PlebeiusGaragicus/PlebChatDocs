# PlebChat

🚨 Work in progress 🚨

---


## setup

```sh
# setup .env vars first
cp .env.example .env

mkdir ./volumes/openwebui_backend_data
mkdir ./volumes/pipelines
```

```sh
docker compose -f docker-compose.yml --env-file .env up -d
```


```sh
# check logs
# https://containrrr.dev/watchtower/arguments/
docker logs watchtower
```


![PlebChat avatar](./static/plebchat.png)