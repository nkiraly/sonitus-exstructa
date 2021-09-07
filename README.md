# Sonitus Exstructa

'Structured Noise' log generator for container orchestration log testing

## Usage

Usage example for various container orchestration and execution solutions.

## Development

Changes and improvements are ideally built and tested in a python virtual environment based on the repository Pipfile which installs the repository package as editable.

```sh
cd ~/src/sonitus-exstructa
pipenv install --dev --python python3.8
pipenv shell
```

Where you can do an editable install and execute the program as desired to test output:

```sh
(sonitus-exstructa) nkiraly@helios:~/src/sonitus-exstructa$ SONITUS_EXSTRUCTA_ACTOR="PowerManager PowerLord" \
SONITUS_EXSTRUCTA_TARGET="regulators accumulators" \
SONITUS_EXSTRUCTA_STATE="charged online dry" \
sonitus-exstructa generate

{"message": "PowerLord ensuring regulators online", "actor": "PowerLord", "action": "ensuring", "target": "regulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:48:02.480646"}
{"message": "PowerLord ensuring regulators online", "actor": "PowerLord", "action": "ensuring", "target": "regulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:48:30.509398"}
{"message": "PowerLord ensuring accumulators online", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:48:54.530558"}
{"message": "PowerManager ensuring regulators dry", "actor": "PowerManager", "action": "ensuring", "target": "regulators", "state": "dry", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:49:12.549721"}
{"message": "PowerLord ensuring regulators charged", "actor": "PowerLord", "action": "ensuring", "target": "regulators", "state": "charged", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:49:35.573644"}
{"message": "PowerLord ensuring accumulators online", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:49:51.590405"}
{"message": "PowerLord ensuring accumulators charged", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "charged", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:50:16.616450"}
{"message": "PowerLord ensuring accumulators dry", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "dry", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:50:46.646828"}
{"message": "PowerLord ensuring regulators online", "actor": "PowerLord", "action": "ensuring", "target": "regulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:51:11.659593"}
```

When upgrading core dependencies, it may be necessary to rebuild the Pipfile and lock, derived from requirements files a la

```sh
cd ~/src/sonitus-exstructa
pipenv install --dev --python python3.8
pipenv shell
pipenv install --requirements requirements.txt
pipenv install --dev --requirements requirements-testing.txt
pipenv install --dev --requirements requirements-build.txt
pipenv install --editable .
```

## Testing

When satisfied with changes, you should also test an updated container image behaves as exeptected

```sh
$ DOCKER_BUILDKIT=1 docker build .
[+] Building 25.4s (21/21) FINISHED
.....
  => => writing image sha256:31ad9bf80200e93f90ce6b53433aaff89fa2323bbdc7f69cb98f2c6d7871daec                                                                                                                  0.0s

$ docker run -it --env SONITUS_EXSTRUCTA_TARGET="regulators accumulators" --env SONITUS_EXSTRUCTA_STATE="charged online dry" 31ad9bf80200e93f90ce6b53433aaff89fa2323bbdc7f69cb98f2c6d7871daec generate
{"message": "PowerLord ensuring accumulators online", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:55:38.531466"}
{"message": "PowerLord failed ensuring accumulators charged", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "charged", "result": "FAILURE", "level": "error", "timestamp": "2021-09-07T02:55:54.546809"}
{"message": "PowerLord ensuring regulators charged", "actor": "PowerLord", "action": "ensuring", "target": "regulators", "state": "charged", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:56:13.551927"}
{"message": "PowerManager ensuring regulators dry", "actor": "PowerManager", "action": "ensuring", "target": "regulators", "state": "dry", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:56:18.558007"}
{"message": "PowerManager ensuring regulators charged", "actor": "PowerManager", "action": "ensuring", "target": "regulators", "state": "charged", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:56:36.574668"}
{"message": "PowerManager ensuring accumulators online", "actor": "PowerManager", "action": "ensuring", "target": "accumulators", "state": "online", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:56:59.599014"}
{"message": "PowerLord ensuring accumulators charged", "actor": "PowerLord", "action": "ensuring", "target": "accumulators", "state": "charged", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:57:22.623623"}
{"message": "PowerLord ensuring regulators dry", "actor": "PowerLord", "action": "ensuring", "target": "regulators", "state": "dry", "result": "SUCCESS", "level": "info", "timestamp": "2021-09-07T02:57:41.643901"}
```
