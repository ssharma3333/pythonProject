student_infor= {

"name" : "pramod",
"age"  : 65,
"address" : "KA"

}

print(student_infor)
print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])



student_infor["age"]=100
print(student_infor)



student_infor1={

 "name" : "pramod",
 "age"  :  20,
"address" : {

"home_address" : "ND",
"office_address": "KA"
}

}

student_infor2={
"name":"AMit",
"age" : 67,
"address":{
    "home address":"goa",
    "office_address": "KA"
}

}

student_list=[student_infor1,student_infor2]
print(student_list)