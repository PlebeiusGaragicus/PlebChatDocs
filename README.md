```sh
# DEVELOPMENT
# docker-compose up -f docker-compose-dev.yml --env-file .env
docker compose -f docker-compose-dev.yml --env-file .env up -d

# PRODUCTION
# docker-compose up -f docker-compose.yml --env-file .env
docker compose -f docker-compose.yml --env-file .env up -d
```


```sh
docker logs watchtower

```




https://containrrr.dev/watchtower/arguments/


```sh
mv template.env .env
```