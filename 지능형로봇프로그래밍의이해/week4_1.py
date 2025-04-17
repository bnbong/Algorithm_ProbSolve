print("## 택배를 보내기 위한 정보를 입력하세요. ##")
people = input("받는 사람 : ")
address = input("주소 : ")
weight = int(input("무게(g) : "))

print(f"** 받는 사람 ==> {people}")
print(f"** 주소 ==> {address}")
print(f"** 배송비 ==> {weight*5} 원")
