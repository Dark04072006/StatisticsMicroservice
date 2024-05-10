FROM python:3.11.9

WORKDIR /src

COPY pyproject.toml /src/pyproject.toml
COPY StatisticsMicroservice /src/StatisticsMicroservice
COPY scripts/start.sh /src/scripts/start.sh
COPY yoyo.ini /src/yoyo.ini

RUN chmod +x /src/scripts/start.sh
RUN pip install -U pip
RUN pip install -e .
RUN cd /src/
