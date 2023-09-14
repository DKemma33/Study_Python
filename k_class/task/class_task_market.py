# 마켓은 손님 한 명에게 한 개의 상품을 판매한다.
# 손님마다 할인율이 다르다
# 마켓에서 판매 시 손님의 할인율을 적용하여 판매한다.


class Market:
    # 상품명, 상품가격, 상품 재고
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, customer):
        discount_price = self.price - (self.price * customer.discount * 0.01)
        customer.money -= int(discount_price)
        self.stock -= 1


class Customer:
    # 이름, 나이, 할인율(10%)
    def __init__(self, name, age, discount, money):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money


customer = Customer('한동석', 20, 30, 40000)
market = Market('감자', 1500, 50)

market.sell(customer)
print(customer.money)










