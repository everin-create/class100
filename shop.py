class Shop(object):
    def __init__(self,shop_name,no_items,money):
        self.shop_name=shop_name,
        self.no_items=no_items,
        self.money=money
    def price(self,no_items,money):
        return(self.no_items/self.money)
    def shop(self,shop_name):
        print(self.shop_name)
    

Nice=Shop('nandini',18,180)
print(Nice.price(18,180))
print(Nice.shop('nandini'))