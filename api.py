import requests
# print(requests)
# api=("https://fakestoreapi.com/products/")
# res=requests.get(api)
# print(res.json())


import json
mob={"id":2,"name":"oppo","price":50000,"color":"black"}
res=requests.post("http://localhost:3001/mob",json=mob)
print(res)

mob={"id":3,"name":"iphone","price":100000,"color":"orange"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":4,"name":"1+","price":30000,"color":"white"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":5,"name":"moto","price":20000,"color":"black"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":6,"name":"poco","price":50000,"color":"pink"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":7,"name":"vivo","price":40000,"color":"black"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":8,"name":"redmi","price":15000,"color":"black"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":9,"name":"realme","price":18000,"color":"light blue"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)

mob={"id":10,"name":"nokiya","price":8000,"color":"red"}
res=requests.post("http://localhost:3001/books",json=books)
print(res)




# LAPTOP

laptop={"id":2,"name":"lenovo ideapad slim 3","price":48000,"ram":"8GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":3,"name":"acer aspire 5","price":51000,"ram":"8GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":4,"name":"asus vivobook 15","price":58000,"ram":"16GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":5,"name":"msi modern 14","price":65000,"ram":"16GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":6,"name":"samsung galaxy book4","price":65000,"ram":"16GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":7,"name":"dell vostro 15","price":53000,"ram":"8GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":8,"name":"lenovo","price":76000,"ram":"8GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":9,"name":"apple macbook air m2","price":76000,"ram":"8GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)

laptop={"id":10,"name":"dell inspiration 15","price":55000,"ram":"16GB"}
res=requests.post("http://localhost:3000/laptop",json=laptop)
print(res)



#  TV
tv={"id":2,"name":"LG smart tv","price":42000,"size":"50 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":3,"name":"sony bravia","price":55000,"size":"55 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":4,"name":"mi smart tv x","price":28000,"size":"43 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":5,"name":"oneplus y series","price":26000,"size":"43 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":6,"name":"tcl qled tv","price":39000,"size":"55 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":7,"name":"hisense smart tv","price":30000,"size":"50 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":8,"name":"panasonic led tv","price":34000,"size":"43 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":9,"name":"vu premium tv","price":31000,"size":"50 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)


tv={"id":10,"name":"acer advanced i series","price":37000,"size":"55 inches"}
res=requests.post("http://localhost:3001/tv",json=tv)
print(res)




# WATCH
watch={"id":2,"name":"fastrack reflex","price":3500,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":3,"name":"noise colorfitpro","price":3500,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":4,"name":"boat wave call","price":2800,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":5,"name":"fire-boltt ninja","price":3200,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":6,"name":"apple watch se","price":29900,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":7,"name":"casio g-shock","price":8500,"type":"digital"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":8,"name":"samsung galaxy watch 6","price":24900,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)


watch={"id":9,"name":"timex expedition","price":4500,"type":"analog"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)

watch={"id":10,"name":"fossil gen 6","price":18999,"type":"smartwatch"}
res=requests.post("http://localhost:3001/watch",json=watch)
print(res)



# BOOKS
books={"id":2,"name":"java basics","price":400}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":3,"name":"c programming","price":350}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":4,"name":"data science","price":550}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":5,"name":"dbms concepts","price":500}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":6,"name":"os","price":600}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":7,"name":"computer network","price":520}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":8,"name":"machine learning","price":750}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":9,"name":"artifical intelligence","price":800}
res=requests.post("http://localhost:3001/books",json=books)
print(res)


books={"id":10,"name":"clean code","price":650}
res=requests.post("http://localhost:3001/books",json=books)
print(res)






