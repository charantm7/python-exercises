dictionary = {}
dictionary1 = {
    "name":"Charan",
    "age":18,
    "College":"SVCE",
    "address":{
       "Lives in":"bengaluru"
    }
}
dictionary1["name"]="shamanth"
dictionary_added = dictionary.update(dictionary1)
print(dictionary.get("age"))