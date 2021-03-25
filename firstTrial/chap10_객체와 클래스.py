# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
# hydrogen = Element('Hydrogen', 'H', 1)
#
# print(hydrogen.name)
#
# el_dict={'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
#
# hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
#
# # print(hydrogen.name)
#
# class Element:
#     def __init__(self,name,symbol,number):
#         self.name=name
#         self.symbol=symbol
#         self.number=number
#     def dump(self):
#         print('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
# print("**")
# hydrogen = Element(**el_dict)
# print(hydrogen.dump())
# print(hydrogen)
# class Element:
#     def __init__(self,name,symbol,number):
#         self.name=name
#         self.symbol=symbol
#         self.number=number
#     def __str__(self):
#         return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
# print("**")
# print(hydrogen.dump())
# class Element:
#     def __init__(self,name,symbol,number):
#         self.__name=name
#         self.__symbol=symbol
#         self.__number=number
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def symbol(self):
#         return self.__symbol
#     @property
#     def number(self):
#         return self.__number
#
# hydrogen=Element('Hydrogen','H',1)
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)
#
# class Bear:
#     def eats(self):
#         return "berries"
#
# class Rabbit:
#     def eats(self):
#         return "clover"
#
# class Octothorpe:
#     def eats(self):
#         return "campers"
#
# bear = Bear()
# rabbit = Rabbit()
# octothorpe = Octothorpe()
#
# print(bear.eats())
# print(rabbit.eats())
# print(octothorpe.eats())

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return '''I have many attachments:
            My laser, to %s.
            My claw, to %s.
            My smartphone, to %s.
            ''' %(self.laser.does(), self.claw.does(), self.smartphone.does())

robbie = Robot()
print(robbie.does())