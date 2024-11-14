#!/bin/bash

docker compose -f tunnel.yml --env-file tunnel.env up -d
