#!/usr/bin/env bash
set -e

echo 1231231213
# TODO для создания баз прописать свой вариант
export VARIANT="v2"
export SCRIPT_PATH=/docker-entrypoint-initdb.d/
export PGPASSWORD=postgres
psql -f "$SCRIPT_PATH/scripts/db-$VARIANT.sql"
