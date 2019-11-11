from car import car
from collection import collectionCar
from main import functionsdealer
car1=car('test1','wood','100','120','1991','1991')
car2=car('test2','ev','100','130','1991','1991')
car3=car('test3','wood','100','140','1991','1991')
coll=collectionCar()
coll.addCar(car1)
coll.addCar(car2)
coll.addCar(car3)

m=functionsdealer()
total=m.saleyear('1991',coll.get_list())
total1=m.benefityear('1991',coll.get_list())
total2=m.soldmake('wood',coll.get_list())
total3=m.purchase('wood',coll.get_list())
m.displaybenefitsale(total1)
m.displaysale(total)
m.displaysoldmakesale(total2)
m.displaysoldpurchase(total3)
