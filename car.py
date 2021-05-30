class Car(object):
    def __init__(self,model,color,company,mileage,speed_limit):
        self.model=model,
        self.color=color,
        self.company=company,
        self.mileage=int(mileage),
        self.speed_limit=int(speed_limit)
    
    def start(self):
        print("Started")

    def cars(self,mileage,speed_limit):
        return int(self.mileage)/int(self.speed_limit)

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerated")


SUV=Car('model_500','white','hyundai',300,100)
print(SUV.start())
print(SUV.stop())
print(SUV.accelerate())
print(SUV.color)
print(SUV.cars(300,100))
