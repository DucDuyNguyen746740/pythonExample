from car import car
class collectionCar:
    def __init__(self):
        self.collectionCar = []
    def get_list(self):
        return self.collectionCar
    def addCar(self,car):
        self.collectionCar.append(car)
    def removeCar(self,car):
        self.collectionCar.remove(car)
