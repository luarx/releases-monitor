FROM python:3.7.0-alpine3.8

# Force stdin, stdout and stderr to be totally unbuffered
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt ./

# Signal handling for PID1 https://github.com/krallin/tini
RUN apk add --update --no-cache tini && \
    apk add --no-cache --virtual .build-dependencies alpine-sdk libffi-dev autoconf automake libtool && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-dependencies && \
    find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' +

RUN addgroup -g 1001 appuser && \
    adduser -S -u 1001 -G appuser appuser
USER 1001

COPY . .

ENTRYPOINT ["/sbin/tini", "--"]
