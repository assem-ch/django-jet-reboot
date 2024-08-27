FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /startup
COPY gulp_build_scripts/entrypoint.sh .

VOLUME /django-jet-reboot

ENTRYPOINT [ "/bin/bash", "entrypoint.sh" ]