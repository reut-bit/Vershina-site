#!/usr/bin/env bash
# Загружает содержимое site/ на хостинг Timeweb (основной сайт, ~/public_html).
# Нужен SSH-ключ, добавленный в ~/.ssh/authorized_keys на хостинге.
# Пробный запуск без изменений: ./deploy.sh --dry-run
set -euo pipefail
cd "$(dirname "$0")"

HOST="cj110251@vh460.timeweb.ru"

rsync -rltvz --delete --exclude='.DS_Store' --exclude='cgi-bin/' "$@" site/ "$HOST:public_html/"
