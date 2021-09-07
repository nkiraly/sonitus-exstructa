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
sonitus-exstructa generate
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
 => => writing image sha256:ab8566b1122ebb0869f327dab505c4cb91201545b175fc60f35a1e698a719878                                                                                                                  0.0s

$ docker run -it ab8566b1122ebb0869f327dab505c4cb91201545b175fc60f35a1e698a719878 generate
{"message": "Generate Message", "level": "info", "timestamp": "2021-09-07T01:10:45.350580"}
```
