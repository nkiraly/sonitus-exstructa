# syntax=docker/dockerfile:1.0-experimental

FROM python:3.8-slim-buster as build

RUN apt-get update && apt-get install --no-install-recommends -y \
  pipenv \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /sonitus-exstructa
COPY . .

RUN pip install --requirement requirements-build.txt && python setup.py bdist_wheel


FROM python:3.8-slim as base

ENV SERVICE_NAME=sonitus-exstructa
ENV WORKDIR=/$SERVICE_NAME
ENV SERVICE_USER=$SERVICE_NAME
ARG SERVICE_USER_ID=999

WORKDIR $WORKDIR
RUN apt-get update && apt-get install --no-install-recommends -y \
  dumb-init \
  && rm -rf /var/lib/apt/lists/* \
  && update-ca-certificates

COPY --from=build ${WORKDIR}/dist/*.whl .

#RUN --mount=type=secret,id=pipConf export PIP_CONFIG_FILE="/run/secrets/pipConf" \
RUN pip install --no-cache-dir *.whl \
    && rm *.whl

COPY docker/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN addgroup --system --gid $SERVICE_USER_ID $SERVICE_USER \
  && adduser --system --uid $SERVICE_USER_ID --ingroup $SERVICE_USER $SERVICE_USER \
  && chown -R "$SERVICE_USER:$SERVICE_USER" "$WORKDIR" \
  && chmod +x /usr/local/bin/docker-entrypoint.sh

USER $SERVICE_USER
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
CMD [ "--help" ]
