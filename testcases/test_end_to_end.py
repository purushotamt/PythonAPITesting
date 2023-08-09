import requests
import json
import jsonpath

def test_addnewstudent():
    API_URL ="https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/Purushotam/Desktop/RequestJson.json', 'r')
    request_json=json.loads(f.read())
    response = requests.post(API_URL,request_json)
    #print(response)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])


    tech_api_url ="https://thetestingworldapi.com/api/technicalskills"
    f =open('C:/Users/Purushotam/Desktop/Techskilljson.json', 'r')
    request_json = json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    address_api_url = "https://thetestingworldapi.com/api/addresses"
    f = open('C:/Users/Purushotam/Desktop/address.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(address_api_url, request_json)


    final_deatils ="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_deatils)
    print(response.text)

#so everytime a new student is added I want to add address and techskill for same student
#tech = request_json['id']=int(id[0])
   # request_json['st_id'] = id[0]