Spreadsheet based UI for Apache Spark
=====================================

Project created as final year project for MSc level studies.

## Setup

### Apache Spark + Livy

Build docker image:
```bash
$ cd docker
$ docker build -t livy:latest .
$ cd ..
```

Run container from image:
```bash
$ docker run -p 8998:8998 -d livy:latest
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