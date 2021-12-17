#!/bin/sh

influx apply --file /docker-entrypoint-initdb.d/dashboards --force true
