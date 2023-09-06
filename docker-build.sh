#!/bin/sh

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -e|--env) env="$2"; shift ;;
        *) echo "Неизвестный параметр: $1"; sleep 5s; exit 1 ;;
    esac
    shift
done

docker compose -f ./config/docker-compose.$env.yml --env-file ./config/.env.$env up -d --build

sleep 25s