import requests
import json
url=requests.get("https://api.merakilearn.org/courses")
api_data=url.json()
with open("folder.json","w")as file_data:
    file=json.dump(api_data,file_data,indent=4)
serial_number=1
for i in api_data:
    print(serial_number,".",i["name"],":",i["id"])
    serial_number+=1
course_no=int(input("choose your course number:"))
print(api_data[course_no-1]["name"])
idd=api_data[course_no-1]["id"]
N_url=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
data=N_url.json()
with open("topic.json","w")as k:
    json.dump(data,k,indent=4)
    serial_number2=1
    list1=[]
    list2=[]
for j in data["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial_number2,j["name"])
        print("   ",serial_number2,j["slug"])
        serial_number2+=1
        new_no=1
        list1.append(j)
        list2.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial_number2,j["name"])
        serial_number2+=1
        new_no=1
        list1.append(j)
    for l in data["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print("     ",new_no,j["name"])
            new_no+=1
            list2.append(j)
            break
nevigation=input("what you want previous or next(n/p):")
if nevigation=="p":
    serial_number=1
    for i in api_data:
        print(serial_number,".",i["name"],":",i["id"])
        serial_number+=1
    course_no=int(input("enter ur number do u want:"))
    print(api_data[course_no-1]["name"])
    idd=api_data[course_no-1]["id"]
    url=requests.get("http://api.merakilearn.org/courses/"+str(idd)+"/exercises")
    var=url.json()
    with open("topic.json","w")as k:
        json.dump(var,k,indent=4)
        serial_number2=1
        list1=[]
        list2=[]
    for j in var["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(serial_number2,j["name"])
            print("   ",serial_number2,j["slug"])
            serial_number2+=1
            new_no=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial_number2,j["name"])
            serial_number2+=1
            new_no=1
            list1.append(j)
        for l in var["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("     ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
        parent=int(input("enter the parent exercise do want:"))
        for k in list1:
            if k["parent_exercise_id"]==k["id"]:
                print(list1[parent-1]["name"])
                num=(list1[parent-1]["id"])
                var=[]
                var3=[]
                new_no1=1
                for n in list2:
                    if n["parent_exercise_id"]==num:
                        print("  ",new_no1,n["name"])
                        var.append(n["name"])
                        var3.append(n["content"])
                        new_no1+=1
                child=int(input("enter the child exercise do u want :"))
                new_no2=1
                for s in range(0,len(var)):
                    if child==new_no2:
                        print(var[s])
                        print(var3[s])
                    new_no2+=1
elif nevigation=="n":
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
        parent=int(input("enter the parent exercise do want:"))
        for k in list1:
            if k["parent_exercise_id"]==k["id"]:
                print(list1[parent-1]["name"])
                num=(list1[parent-1]["id"])
                var=[]
                var3=[]
                new_no1=1
                for n in list2:
                    if n["parent_exercise_id"]==num:
                        print("  ",new_no1,n["name"])
                        var.append(n["name"])
                        var3.append(n["content"])
                        new_no1+=1
                child=int(input("enter the child exercise do u want:"))
                new_no2=1
                for s in range(0,len(var)):
                    if child==new_no2:
                        print(var[s])
                        print(var3[s])
                    new_no2+=1