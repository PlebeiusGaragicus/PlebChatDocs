# Open WebUI setup

```sh
# https://docs.openwebui.com/getting-started/env-configuration/

docker run -d \
    -p 3000:8080 \
    --add-host=host.docker.internal:host-gateway \
    -v open-webui:/app/backend/data \
    --name open-webui \
    --restart always ghcr.io/open-webui/open-webui:main \
    -e ENABLE_MESSAGE_RATING=false \
    -e WEBUI_NAME=PlebChat

    # -e STATIC_DIR=

    #-e TASK_MODEL=
    #-e TITLE_GENERATION_PROMPT_TEMPLATE=

    #-e DOCS_DIR=


```

### watchtower auto-updating

```sh
docker run -d --name watchtower --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower open-webui
```
