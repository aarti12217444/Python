info={
    "key":"value",
    "name":"aarti",
    "learning":"coding",
    "age":19,
    "marks":87
}
print(info["name"])
print(info["age"])
print(info["marks"])

info["name"]="miss kashyap"
print(info)

student={
    "name":"Aarti",
    "subject":{
        "phy":90,
        "che":80,
        "maths":100
    }
}
print(student["subject"]["che"])
print(len(list(student.keys())))
print(list(student.values()))
pair=list(student.items())
print(pair[0])
print(student.get("name2"))#it will give none instead of error
student.update({"city":"patna"})
print(student)