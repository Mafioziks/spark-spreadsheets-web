import requests, textwrap, json
import session


def listing():
    # TODO: session need to be started from one connection and shared if there will be users
    session_response = session.start()

    if session_response is None:
        return {'error': 'Failed to start a session'}

    url = session.link + ':' + str(session.port) + session_response.headers['location']

    data = {
        'code': textwrap.dedent("""
         from pyspark.sql import SparkSession
         spark = SparkSession.builder \
              .appName("Spark Spreadsheets") \
              .getOrCreate()
        
          result spark.sql('show databases').show()
        """)
    }

    r = requests.post(url, data=json.dumps(data), headers=session.headers)

    return r.text
