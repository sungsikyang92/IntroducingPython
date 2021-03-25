# #11.3.1 누락된 키 처리하기: setdefault()와 defaultdict()
#
# periodic_table = {'Hydrogen':1, 'Helium':2}
# print(periodic_table)
#
# carbon = periodic_table.setdefault('Carbon',12)
# print(carbon)
# print(periodic_table)
#
# helium = periodic_table.setdefault("Helium", 947)
# print(helium)
# print(periodic_table)

# #11.3.6 깔끔하게 출력하기: pprint()
# from collections import OrderedDict
# from pprint import pprint
# quotes = OrderedDict([
#     ('Moe', 'A wise guy, huh?'),
#     ('Larry','Ow!'),
#     ('Curly','Nyuk nyuk!'),
# ])
# print(quotes)
# pprint(quotes)