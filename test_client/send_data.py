#!/usr/bin/env python3

import os
import random
import time

from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point

load_dotenv(os.path.expanduser('~/.noise-monitor.env'))

url = os.environ['DOCKER_INFLUXDB_URL']
bucket = os.environ['DOCKER_INFLUXDB_INIT_BUCKET']
token = os.environ['DOCKER_INFLUXDB_INIT_ADMIN_TOKEN']
org = os.environ['DOCKER_INFLUXDB_INIT_ORG']
measurement = os.environ['DOCKER_INFLUXDB_MEASUREMENT']

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api()

while True:
    volume = random.randrange(-60, 0)
    p = Point(measurement).field("volume", volume)
    write_api.write(bucket=bucket, record=p)
    print(f'Sending me {volume} dB')
    time.sleep(0.1)
