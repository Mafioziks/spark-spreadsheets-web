from pprint import pprint


def get_sql_tables(json):
    return get_output_data_fields(json, 'tableName')


def get_sql_databases(json):
    return get_output_data_fields(json, 'databaseName')


def get_output_data_fields(json, field_name):
    schema = json['output']['data']['application/json']['schema']
    data = json['output']['data']['application/json']['data']

    field_data = []
    for index, element in enumerate(schema['fields']):
        if element['name'] == field_name:
            for data_element in data:
                field_data.append(data_element[index])

    return field_data
