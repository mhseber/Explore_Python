nid_list = [
    {"nid_number":1010101010,"name":"seber","fathers name":"a khalak","mothers name":"mahamuda bagum","age":22,"permanent address":"44 no s k dash road gandaria"},
    {"nid_number":2020202020,"name":"tusar","fathers name":"bunu","mothers name":"sara","age":30,"permanent address":"10/1 vattikana sutrapur"},
    {"nid_number":3030303030,"name":"ahanaf","fathers name":"h raju","mothers name":"munmun","age":35,"permanent address":"42 notun rasta sutrapur"},
    {"nid_number":4040404040,"name":"free fire","fathers name":"garina","mothers name":"susa","age":50,"permanent address":"new town hogkog"},
    
]

total_list = int(input("enter nid number:"))
for info in nid_list:
    if total_list == info["nid_number"]:
        print(f"{info['nid_number']} \nname:{info['name']} \nfathers name: {info['fathers name']} \nmothers name:{info['mothers name']} \npermanent address:{info['permanent address']} .") 
    
    # DONE