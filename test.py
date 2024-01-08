
# inventory = [
#     {"title":  "pencil", "price": 5},
#     {"title": "pen", "price": 10},
#     {"title": "eraser","price":8},
#     {"title": "marker","price":50},
#     {"title": "paper", "price":15},
# ]

# total = 0
# while True :
#     pd_title = input("ki lagbe?: ")
#     msg = ""
    
#     if pd_title == "":
#         break
#     msg = f"{pd_title} nai"
    
#     for pd in inventory:
#         if pd["title"] == pd_title:
#             msg = f"{pd_title} ache"
#             pd_quint = int(input("koita dimu: "))
#             sub_total = pd["price"] * pd_quint
#             total += sub_total
    

#     print(msg)
    
# print(f"{total} taka hoicha")



# pcexasorise =[
#     { "title":"mouse","price": 500},
#     {"title":"kebored","price":1000},
#     {"title":"monitor","price":10000},
#     {"title":"headphon","price":1500},
# ]

# total = 0 
# while True:
#     pd_title = input("ki lagbe?: ")
#     msg = ""
    
#     if pd_title == "":
#         break
#     msg = f"{pd_title} nai"
    
#     for pd in pcexasorise:
#         if pd["title"] == pd_title:
#             msg = f"{pd_title} ache"
#             pd_quint = int(input("koita dimu: "))
#             sub_total = pd["price"] * pd_quint
#             total += sub_total
            
            
#     print(msg)
    
# print(f"{total} taka hoiche")
            





gudam = [
    {"title": "colom", "price": 5}, 
    {"title": "pencil", "price": 2}, 
    {"title": "scale", "price": 15}
]

input_title = str(input("ki lagbe: "))
for item in gudam:
    if input_title == item["title"]:
        print(f"{item['title']} er dam {item['price']} taka")

