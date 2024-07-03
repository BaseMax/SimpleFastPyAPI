FROM jenkins/inbound-agent:3256.v88a_f6e922152-1-jdk17

USER root

RUN apt update && apt install --no-install-recommends -y python3 python3-venv pipenv

USER jenkins
