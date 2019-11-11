from car import car
from collection import collectionCar
class functionsdealer():
    def saleyear(self,year,listcar):
        total=0
        for i in listcar:
            if str(i.get_sold_date())==year:
                total=total+int(i.get_sold_price())
        return total
    def benefityear(self,year,listcar):
        total=0
        for i in listcar:
            if str(i.get_sold_date())==year:
                benefit=int(i.get_sold_price())-int(i.get_purchase_price())
                total=total+benefit
        return total
    def soldmake(self,make,listcar):
        total=0
        for i in listcar:
            if str(i.get_make())==make:
                total=total+int(i.get_sold_price())
        return total 
    def purchase(self,make,listcar):
        total=0
        for i in listcar:
            if str(i.get_make())==make:
                total=total+int(i.get_purchase_price())
        return total    
    def displaysale(self,total):
        print("toatal of sale:"+str(total))
    def displaybenefitsale(self,total):
        print("toatal of benefitsale:"+str(total))
    def displaysoldmakesale(self,total):
        print("toatal of soldmakesale:"+str(total))
    def displaysoldpurchase(self,total):
        print("toatal of purchase:"+str(total))