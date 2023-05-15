import json


def main(json_obj):
    data = json.loads(json_obj)
    print(type(data))
    print(data)


if __name__ == "__main__":
    
    json_obj = '''
    {
        "RELEASE_VERSION": "22.1.3",
        "ALL_ARCHIVES": ["22.1.3", "22.1.45", "22.1.354"],
        "22.1.3": [
            {
                "path": ["1", "2"],
                "0": {
                    'install': "Установка скрипто в для банков",
                    'scripts': ["1", "2", "3", "4", "5"]
                },
                "1": {
                    'install': "Установка скрипто в для банков",
                    'scripts': ["1", "2", "3", "4", "5"]
                }
            },
            {
                "0": {
                    "№": "data[0]",
                    "type": "data[1]",
                    "Direction": "data[2]",
                    "Description": "data[5]",
                    "Scripts": "data[6]",
                    "BBR": "data[7]",
                    "Configure": "data[8]",
                    "Modules": "data[9]",
                    "DDL": "data[10]",
                    "Documents": "data[11]"
                },
                "1": {
                    "№": "data[0]",
                    "type": "data[1]",
                    "Direction": "data[2]",
                    "Description": "data[5]",
                    "Scripts": "data[6]",
                    "BBR": "data[7]",
                    "Configure": "data[8]",
                    "Modules": "data[9]",
                    "DDL": "data[10]",
                    "Documents": "data[11]"
                }
            },
            {
                "AllFiles": [1, 2, 3, 4, 5]
            }
        ]
    }
    '''.replace(" ", "").replace("'", '"')
    
#     json_obj = '''
#     {
#     "employees" : [
#        {
#            "first_name": "Michael", 
#            "last_name": "Rodgers", 
#            "department": "Marketing"
#         },
#        {
#            "first_name": "Michelle", 
#            "last_name": "Williams", 
#            "department": "Engineering"
#         }
#     ]
# }
#     '''


    main(json_obj)