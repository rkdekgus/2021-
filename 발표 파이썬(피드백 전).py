
메뉴 = ['상명김밥','참치김밥','라면','떡볶이','라볶이'] 
가격 = [2500,3000,3000,3500,4000]  
menu = dict()

print('안녕하세요 상명천국입니다.\n============================')  
print('메뉴판\n============================')
print('상명김밥')
print('참치김밥')
print('라면')
print('떡볶이')
print('라볶이\n============================')
print('메뉴를 골라주세요!')



for i,j in zip(메뉴,가격):  
  menu[i] = j 



while True:
  orders = input('주문하고자 하는 음식 : ').split()
  error = 0

  for order in orders: 
    if order not in menu.keys():
      print('주문하신 {}는(은) 메뉴판에 없습니다.\n다시 주문해주세요!'.format(order)) 
      
      error +=1 
      break
    else:
      continue 

  if error == 0: 
    break
  

price = [] 
for order in orders: 
  price.append(menu[order]) 

for order,cost in zip(orders, price):
  print('{}는(은) {}원입니다'.format(order,cost))
print('음식의 총가격은 {}입니다!'.format(sum(price))) 
