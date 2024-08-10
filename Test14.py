import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#print(type(response.json()))
#print(type(response))
#print((response.json()))

complete_detail = response.json()

#print(complete_detail[0]["id"])

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])

