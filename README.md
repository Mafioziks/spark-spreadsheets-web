Spreadsheet based UI for Apache Spark
=====================================

Project created as final year project for MSc level studies.

## Setup

### Apache Spark + Livy

Build docker image:
```bash
$ docker build .
```

Possible build arguments:
- openjdk_version
- scala_version
- spark_version
- hadoop_version
- livy_version

Default build argument values are:
- openjdk_version=8
- scala_version=2.11.12
- spark_version=3.0.1
- hadoop_version=2.7
- livy_version=0.7.0

Run container from image:
```bash
$ docker run -p 8888:8888 -p 8998:8998 [docker_image_hash]
```

Start up Livy:
```bash
$ docker exec -it [docker_container_hash] bash
$ ./livy0.7.0/apache-livy-0.7.0-incubating-bin/bin/livy-server start
```

### Spark Spreadsheets

Create virtual environment for python
```bash
$ python3.8 -m venv fyp
```

Switch to virtual environment:
```bash
$ . ./fyp/bin/activate
```

Install python packages:
```bash
$ pip install -r requirements.txt
```

Run API:
```bash
$ python app.py
```

### Setup Result

After this Swagger API documentation is located on: `http://localhost:5000/api/ui`

Page will be located on: `http://localhost:5000`