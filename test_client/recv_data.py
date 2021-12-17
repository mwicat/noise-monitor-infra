#!/usr/bin/env python3

import datetime
import os
import time

from dotenv import load_dotenv
from influxdb_client import InfluxDBClient


load_dotenv(os.path.expanduser('~/.noise-monitor.env'))

url = os.environ['DOCKER_INFLUXDB_URL']
bucket = os.environ['DOCKER_INFLUXDB_INIT_BUCKET']
token = os.environ['DOCKER_INFLUXDB_INIT_ADMIN_TOKEN']
org = os.environ['DOCKER_INFLUXDB_INIT_ORG']
measurement = os.environ['DOCKER_INFLUXDB_MEASUREMENT']

client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

params = {
    "_measurement": measurement,
    "_bucket": bucket,
    "_start": datetime.timedelta(minutes=-15),
    "_desc": True,
    "_every": datetime.timedelta(seconds=10)
}

query = '''
from(bucket: _bucket)
  |> range(start: _start)
  |> filter(fn: (r) => r["_measurement"] == _measurement)
  |> filter(fn: (r) => r["_field"] == "volume")
  |> aggregateWindow(every: _every, fn: mean, createEmpty: false)
  |> sort(columns: ["_time"], desc: _desc)
'''.strip()


last_ts = None

while True:
  records = query_api.query_stream(query=query, params=params)
  fresh_records = []

  for pos, record in enumerate(records):
    if last_ts is None or record["_time"] > last_ts:
      fresh_records.append(record)
    else:
      break
  
  fresh_records.reverse()
  for record in fresh_records:
    print(f'{record["_time"]}\t{record["_value"]}')

  if fresh_records:
    last_ts = record["_time"]

  time.sleep(1)

