For microcontroller client-side part of this project a.k.a data acquisition,
see [noise-monitor-mcu](https://github.com/mwicat/noise-monitor-mcu)

## Configuration

Create file `~/.noise-monitor.env` and set the contents for your configuration:

```ini
DOCKER_INFLUXDB_INIT_MODE=setup
DOCKER_INFLUXDB_INIT_RETENTION=12w
DOCKER_INFLUXDB_INIT_USERNAME=<YOUR USERNAME HERE>
DOCKER_INFLUXDB_INIT_PASSWORD=<YOUR PASSWORD HERE>
DOCKER_INFLUXDB_INIT_ORG=<YOUR ORGANIZATION NAME HERE>
DOCKER_INFLUXDB_INIT_BUCKET=<YOUR BUCKET NAME HERE>
DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=<YOUR ADMIN TOKEN HERE>
DOCKER_INFLUXDB_URL=http://localhost:8086
DOCKER_INFLUXDB_MEASUREMENT=noise_level
```

Start services:

```sh
docker-compose up
```

## Testing

### Browser

1. Visit [http://localhost:8086/](http://localhost:8086/)
2. Locate and open dashboard `Noise level`

### CLI

Initialize environment

```sh
cd test_client
pipenv install
```

Pull data from InfluxDB:

```sh
pipenv run ./recv_data.py
```

Send some random data to InfluxDB:

```sh
pipenv run ./send_data.py
```
