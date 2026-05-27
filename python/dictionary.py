# data in the form og key and value 
info={
    "key": "value",
    "name": "Archana",
    "learning": "coding",
    "subject":["pyton","c","java"],
    "topics":("dict","set"),
    "age": 20,
    "is_adult": True
}
#print(info)
#del info["key"]
#print(info.pop("key"))
#print(info.popitem())

#info.clear()
"""print(info.keys())
print(info.values())
print(info.items())"""


"""print(info["age"])
print(info["is_adult"])
print(info["subject"])"""

"""info['name']='Archa'               #overwrite
info['surname']='Sharma'
print(info)"""

"""null_dict={}
null_dict["name"]="Archu"
#print(null_dict)
print(null_dict.get("name"))
print(null_dict.get("Name"))
"""

names={
    'name1' : 'Archana',
    'name2' : 'Archu',
    'name3' : 'Archa'
}

for i in names:
    print(i)
    print(names[i])

for i in names.items():
    print(i)

"""print(names)
print(len(names))
names2=names.copy()
print(names2)"""