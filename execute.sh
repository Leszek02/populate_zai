#!/bin/bash

docker cp ./csv opev-postgres:/csv
docker cp ./populate.sql opev-postgres:/populate.sql

docker exec -it opev-postgres psql -U open_event_user -d open_event -f /populate.sql