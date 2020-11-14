# Library imported

# This is a sample Python script.


import json
import requests




# if __name__ == '__main__':
#     print_hi('PyCharm')

call_api = requests.get('http://127.0.0.1:8080/api/permitteds')

json_data = json.loads(call_api.content)
for data in json_data:
    print(data['imageId'])



# login()


# em_dbh.insert()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
