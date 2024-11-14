#!/bin/bash

docker compose -f searxng.yml --env-file searxng.env up -d
