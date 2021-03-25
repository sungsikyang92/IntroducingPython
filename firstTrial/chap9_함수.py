# #9.1 함수 정의하기: def
# def do_nothing():
#     pass
# print('**')
# #9.2 함수 호출하기: ()
# print(do_nothing())
# def make_a_sound():
#     print('quack')
#
# make_a_sound()
# #9.3 인수와 매개변수
#
# def echo(anything):
#     return anything+' '+anything
#
# print(echo('Rumplestiltskin'))
#
# def commentary(color):
#     if color == 'red':
#         return "It's a tomato."
#     elif color == "green":
#         return "It's a green pepper."
#     elif color == 'bee purple':
#         return "I don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color " + color + "."
#
# comment = commentary('blue')
#
# print(comment)
# print(commentary('red'))
# print(do_nothing())
#
# #9.3.1 유용한 None
# thing = None
# if thing:
#     print("It's some thing")
# else:
#     print("It's no thing")
#
# if thing is None:
#     print("It's nothing")
# else:
#     print("It's something")
#
# def whatis(thing):
#     if thing is None:
#         print(thing, 'is None')
#     elif thing:
#         print(thing, 'is True')
#     else:
#         print(thing, 'is False')
#
# whatis(None)
# whatis(True)
# whatis(False)
# whatis('abc')
# whatis(0)
#
# whatis(0.0)
# whatis('')
# whatis("")
# whatis('''''')
# whatis(())
# whatis([])
# whatis({})
# whatis(set())
# whatis(0.00001)
# whatis([0])
# whatis([''])
# whatis(' ')

# #9.3.2 위치인수
# def menu(wine,entree,dessert):
#     return {'wine':wine, 'entree':entree, 'dessert':dessert}
# print(menu('chardonnay','chicken','cake'))
#
# print(menu('beef','bagel','bordeaux'))
#

# #9.3.3 키워드 인수
# print(menu(entree='beef',dessert='bagle',wine='bordeaux'))
#
# print(menu('frontenac',dessert='flan',entree='fish'))

# #9.3.4 기본 매개변수 값 지정하기
# def menu(wine, entree, dessert = 'pudding'):
#     return {'wine':wine, 'entree':entree, 'dessert':dessert}
#
# print(menu('chardonnay','chicken'))
#
# print(menu('dunkelfelder','duck','doughnut'))
#
# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)
#
# buggy('a')
# buggy('b')
# buggy('c')
# print('**')
# def works(arg):
#     result = []
#     result.append(arg)
#     return result
#
# print(works('a'))
# print(works('b'))
# print(works('c'))
#
# def nonbuggy(arg, result=None):
#     if result is None:
#         result =[]
#     result.append(arg)
#     print(result)
# print('**')
# nonbuggy('a')
# nonbuggy('b')
# nonbuggy('c')
#
# #9.3.5 위치 인수 분해하기/모으기:*
#
# def print_args (*args):
#     print("Positional tuple:",args)
#
# print_args()
#
# print_args(3,2,1, 'wait!','uh...')
#
# def print_more(required1, required2, *args):
#     print('Need this one:', required1)
#     print('Need this one. too:', required2)
#     print('All the rest:',args)
#
# print_more('cap','gloves','scarf','monocle','mustache wax')
#
# print_args(2,5,7,'x')
# args = (2,5,7,'x')
# print_args(args)
# print_args(*args)

# #9.3.6 키워드 인수 분해하기/모으기:*
#
# def print_kwargs(**kwargs):
#     print('Keyword arguments:',kwargs)
#
# print_kwargs()
# print_kwargs(wine='merlot',entree='mutton',dessert='macaroon')

# #9.3.7 키워드 전용 인수
#
# def print_data(data, *, start=0, end=100):
#     for value in (data[start:end]):
#         print(value)
#
# data = ['a','b','c','d','e','f']
# data = [1,2,3,4,5,6,7,8,9]
# print_data(data)
# print('**')
# print_data(data, start=4)
# print('**')
# print_data(data, end=2)

# #9.3.8 가변/불변 인수
#
# outside = ['one','fine','day']
# def mangle(arg):
#     arg[1] = 'terrible!'
#
# print(outside)
# mangle(outside)
# print(outside)

# #9.4 독스트링
#
# def echo(anything):
#     'echo returns its input argument'
#     return anything
#
# def print_if_true(thing,check):
#     '''
#     Prints the first argument if a second argument is true.
#     The operation is:
#         1. Check whether the *second* argument is true.
#         2. If it is, print the *first* argument.
#     '''
#     if check:
#         print(thing)
#
# help(echo)
# print('**')
# print(echo.__doc__)
# print('**')
# help(print_if_true)
# print('**')
# print(print_if_true.__doc__)

# #9.5 일등 시민: 함수
#
# def answer():
#     print(42)
#
# answer()
#
# def run_something(func):
#     func()
# print("**")
# run_something(answer)
#
# print(type(run_something))
# print(type(answer))
#
# def add_args(arg1,arg2):
#     print(arg1+arg2)
#
# print(type(add_args))
#
# add_args(1,2)
#
# def run_something_with_args(func,arg1,arg2):
#     func(arg1,arg2)
#
# run_something_with_args(add_args,5,9)
#
# def sum_args(*args):
#     return sum(args)
#
# def run_with_positional_args(func,*args):
#     return func(*args)
#
# print(run_with_positional_args(sum_args,1,2,3,4))

# #9.6 내부 함수
#
# def outer(a,b):
#     def inner(c,d):
#         return c+d
#     return inner(a,b)
#
# print(outer(4,7))
#
# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" %quote
#     return inner(saying)
#
# print(knights('Ni!'))

# #9.6.1 클로저
#
# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" %saying
#     return inner2
#
# a = knights2('Duck')
# b = knights2('Hasenpfeffer')
#
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a())
# print(b())

# #9.7 익명 함수: lambda
#
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
# stairs = ['thud','meow','thud','hiss']
#
# def enliven(word):
#     return word.capitalize() + "!"
#
# edit_story(stairs,enliven)
# print("**")
# edit_story(stairs, lambda word:word.capitalize()+"!")

# #9.8 제너레이터
#
# print(sum(range(1,101)))
#
# #9.8.1 제너레이터 함수
#
# def my_range(first=0, last=10,step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# print(my_range())
#
# ranger = my_range(1,5)
#
# print(ranger)
#
# for x in ranger:
#     print(x)
# print("**")
# for y in ranger:
#     print(y)

# #9.8.2 제너레이터 컴프리헨션
#
# genobj = (pair for pair in zip(['a','b'], ['1','2']))
# print(genobj)
# for thing in genobj:
#     print(thing)

# #9.9 데커레이터
#
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function
#
# def add_ints(a,b):
#     return a+b
#
# print(add_ints(3,5))
# #수동으로 데커레이터 적용
# cooler_add_ints = document_it(add_ints)
# cooler_add_ints(3,5)
#
# print("**")
# @document_it
# def add_ints(a,b):
#     return a + b
#
# add_ints(3,5)
#
# #result를 제곱하는 square_it() 데커레이터
# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function
#
# @document_it
# @square_it
# def add_ints(a,b):
#     return a+b
# print(add_ints(3,5))
#
# @square_it
# @document_it
# def add_ints(a,b):
#     return a+b
# print(add_ints(4,4))

#9.10 네임스페이스와 스코프

#     #전역 변수 값 예시
# animal = 'fruibat'
# def print_global():
#     print('inside print_global:', animal)
#
# print('at the top level:', animal)
#
# print_global()
#
#     #함수에서 전역 변수의 값을 얻어서 바꾸려 할 때 에러 발생 예시
# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the chnage:', animal)
#
# change_and_print_global()
#
#     #함수 내에서 전역 변수와 이름이 같은 변수 animal을 변경할 때, 함수 내 animal 변수를 변경한다.
# def change_local():
#     animal = 'wombat'
#     print('inside change_local:', animal, id(animal))
#
# change_local()
#
# print(animal)
# print(id(animal))

#     #함수 내의 지역 변수가 아닌 전역 변수를 접근하기 위해 global 키워드를 사용해서 전역 변수의 접근을 명시해야 한다.
# animal = 'fruitbat'
# def change_and_print_global():
#     global animal
#     animal = 'wombat'
#     print('after the change:', animal)
#
# print(animal)
# change_and_print_global()
# print(animal)

# animal = 'fruitbat' #전역 변수
# def change_local():
#     animal = 'wombat' #지역 변수
#     print('locals:', locals())
#
# print(animal)
# change_local()
# print('globals:',globals())
# print(animal)

# #9.11 이름에 _와 __사용하기
# def amazing():
#     '''This is the amazing function.
#     Want to see it again?'''
#     print('This function is named:', amazing.__name__)
#     print('And its docstring is:', amazing.__doc__)
#
# amazing()

# #9.12 재귀 함수
#
#     #파이썬에서 재귀가 깊다면(자기 자신을 너무 많이 호출하면) 예외가 발생한다.
# def dive():
#     return dive()
#
# dive()

#     #모든 하위 리스트를 '평평하게'만들때, 다음과 같이 재귀 함수를 작성할 수 있다.
# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             for subitem in flatten(item):
#                 yield subitem
#         else:
#             yield item
# lol = [1,2,[3,4,5],[6,[7,8,9],[]]]
# print(flatten(lol))
# print(list(flatten(lol)))
#
#     #위에서 yield from 표현식을 추가하여 제너레이터의 일부를 전달할 수 있다.
# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item
# lol = [1,2,[3,4,5,6],[7,[8,9],[]]]
# print(flatten(lol))
# print(list(flatten(lol)))

# #9.13 비동기 함수
#
# #9.14 예외
# short_list = [1,2,3]
# position = 5
# print(short_list[position])

# #9.14.1 에러 처리하기: try, except
# #첫번쨰 예시
# short_list = [1,2,3]
# position = 5
# try:
#     print(short_list[position])
# except:
#     print('Need a position between 0 and', len(short_list)-1, ' but got', position)
# #두번쨰 예시
# short_list = [1,2,3]
# while True:
#     value = input('Position [q to quit]? ')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else broke:,', other)

# #9.14.2 예외 만들기
#
# #words 문자열에 대문자가 있을 때 예외를 발생하는 UppercaseException 예외를 만들어보자.
#
# class UppercaseException(Exception):
#     pass
#
# words = ['eenie','meenie','miny','MO']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)
#     try:
#         raise UppercaseException('panic')
#     except UppercaseException as exc:
#         print(exc)

# #9.16 연습문제
#
# #9,1
# # a = ['Harry','Ron','Hermione']
# # def good():
# #     print(a)
# #
# # good()
#
# def good():
#     return ['Harry,','Ron','Hermione']
# print(good())

# #9.2
# def get_odds():
#     for number in range(1,10,2):
#         yield number
#
# count = 1
# for number in get_odds():
#     if count == 3:
#         print("The third odd number id", number)
#         break
#     count += 1
#
# #9.3
# def test(func):
#     def new_func(*args,**kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return new_func
#
# @test
# def greeting():
#     print("Greetings, Earthling")
#
# greeting()
#
# #9.4
# class OopsException(Exception):
#     pass
# try:
#     raise OopsException
# except OopsException:
#     print('Caught an oops')
#
# raise OopsException()

