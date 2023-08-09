import jsonpath
import requests
import json

# Add new student using POST
def test_add_student_data():
    API_URl="https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Purushotam/Desktop/RequestJson.json','r')
    json_request = json.loads(f.read())
    response = requests.post(API_URl,json_request)
    print(response.text)

def test_Update_student_data():
    API_URl="https://thetestingworldapi.com/api/studentsDetails/7759858"
    f = open('C:/Users/Purushotam/Desktop/RequestJson.json','r')
    json_request = json.loads(f.read())
    response = requests.put(API_URl,json_request)
    print(response.text)


def test_delete_student_data():
    API_URl = "https://thetestingworldapi.com/api/studentsDetails/7759858"
    response = requests.delete(API_URl)
    print(response.text)

def test_get_student_data():
    API_URl = "https://thetestingworldapi.com/api/studentsDetails/7759858"
    response = requests.get(API_URl)
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    #print(id)
    assert id[0]==7759858






