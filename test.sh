#!/bin/bash
docker compose -f docker-compose.yml --env-file openwebui.env up

# docker logs -f open-webui pipelines cloudflared_tunnel watchtower
# docker logs -f cloudflared_tunnel

# for i in {1..10}; do docker logs -f open-webui pipelines cloudflared_tunnel watchtower; sleep 1; done
