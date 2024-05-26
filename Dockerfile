ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim as build

#RUN apt-get update \
#    && apt-get install gcc -y \
#    && apt-get clean

WORKDIR /app

COPY . .

RUN pip install -r /backend/requirements.txt \
    && rm -rf /root/.cache/pip \

EXPOSE 5000

CMD ["python", "__init__.py"]
