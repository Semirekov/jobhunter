from terminaltables import SingleTable

def create_head(headers):
    return [headers]

def create_table(header, rows, title):
    TABLE_DATA = header + rows
    return SingleTable(TABLE_DATA, title)

def print_report(table_instance):
    print()
    print(table_instance.table)
    print()

def justify_right(table_instance, columns):
    for column in columns:
        table_instance.justify_columns[column] = 'right'
    
