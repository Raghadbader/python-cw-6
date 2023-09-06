# write your code here
person = { 
    "name": "raghad" ,
    "age" : 18 ,

    "hobbies" : ["sleep","watching movies"]

}       

print(person["name"])
print(person["age"])

person["age"] = 19
person["country"] = "kuwait"

print(person)
person.items()
print(person.items())

person["hobbies"].append("sport") 

def check_hobbies(person) :
    if len(person["hobbies"])>=3 :
        print("wow you are amazing")
    else :
        False
check_hobbies(person)



