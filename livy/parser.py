from pprint import pprint


def get_sql_tables(json):
    return get_output_data_fields(json, 'tableName')


def get_sql_databases(json):
    return get_output_data_fields(json, 'databaseName')


def get_output_data_fields(json, field_name):
    schema = get_schema(json)
    data = get_data(json)

    field_data = []
    for index, element in enumerate(schema['fields']):
        if element['name'] == field_name:
            for data_element in data:
                field_data.append(data_element[index])

    return field_data


def get_data(json):
    return json['output']['data']['application/json']['data']


def get_schema(json):
    return json['output']['data']['application/json']['schema']


def get_response(json):
    return json['output']['data']['application/json']
