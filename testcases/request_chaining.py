import json
import requests
import jsonpath


def test_add_new_student():
    global id
    Api_url="https://thetestingworldapi.com/api/studentsDetails"
    f=open('C:/Users/Purushotam/Desktop/add_student.json', 'r')
    json_request=json.loads(f.read())
    response=requests.post(Api_url,json_request)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])


def test_get_details():
    api_url="https://thetestingworldapi.com/api/studentsDetails/" +str(id[0])
    response = requests.get(api_url)
    print(response.text)


# create a Report Directory
#In terminal - pytest --alluredir C:\Users\Purushotam\PycharmProjects\Automation1\Report testcases
# In CMD to create HTML report -allure serve C:\Users\Purushotam\PycharmProjects\Automation1\Report