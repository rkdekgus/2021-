print('안녕하세요 상명천국입니다.')
print()
print('메뉴판')
print('=============================')
print('상명김밥 : 2500원')
print('참치김밥 : 3000원')
print('라면 : 3000원')
print('떡볶이 : 3500원')
print('라볶이 : 4000원')
print('=============================')
total = 0
food_list=['상명김밥', '참치김밥', '라면', '떡볶이', '라볶이']

while True :

    
    a=input("메뉴를 선택하세요. \n(메뉴를 멈추고 싶으면 -> 엔터를 누르세요):")

    if a == '':
      break

    b=int(input("몇인분 주문할까요? \n(메뉴를 멈추고 싶으면 -> 0을 입력하세요):"))
    print('-------------------------------------------')

    

    if a in food_list:
        
        
        if'상명김밥' in a:
            total=total+b*2500

        if'참치김밥' in a:
            total=total+b*3000

        if'라면' in a:
            total=total+b*3000

        if'떡볶이' in a:
            total=total+b*3500

        if'라볶이' in a:
            total=total+b*4000
    
        print('주문하신 메뉴의 총 가격은', total,'원 입니다')
        print('-------------------------------------------')
            
    else:
        print("메뉴가 없습니다. 다시 메뉴를 넣어주세요")
