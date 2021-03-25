# #6.1 반복하기:while
# count = 1
# while count <=5:
#     print(count)
#     count +=1

# #6.1.1 중단하기: break
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

# #6.1.2 건너뛰기: continue
# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == 'q': #종료
#         break
#     number = int(value)
#     if number % 2 == 0: #짝수
#         continue
#     print(number, "squared is", number * number)

# #6.1.3 break 확인하기: else
# numbers = [1, 3, 5]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 ==0:
#         print('Found even number', number)
#         break
#     position +=1
# else: #break문이 호출되지 않은 경우
#     print('No even number found')

# #6.2 순회하기: for와 in
# word = 'thud'
# offset = 0
# while offset < len(word):
#     print(word[offset])
#     offset +=1
#
# for letter in word:
#     print(letter)

# #6.2.1 중단하기: break
# word = 'thud'
# for letter in word:
#     if letter == 'u':
#         break
#     print(letter)

# #6.2.3 break 확인하기: else
# word = 'thud'
# for letter in word:
#     if letter == 'x':
#         print("Eek! An 'x'!")
#         break
#     print(letter)
# else:
#     print("No 'x' in there.")

# #6.2.4 숫자 시퀀스 생성하기: range()
# for x in range(0,3):
#     print(x)
# print(list(range(0,3)))
#
# for x in range(2,-1,-1):
#     print(x)
# print(list(range(2,-1,-1)))
#
# for x in range(0,11,2):
#     print(x)
# print(list(range(0,11,2)))

# #6.5 연습문제
#     #6.1
# for x in range(3,-1,-1):
#     print(x)
# print(list(range(3,-1,-1)))
# #해설
# for value in [3,2,1,0]:
#     print(value)

#     #6.2
# guess_me = 7
# number = 1
# while True:
#     if number < guess_me:
#         print('too low')
#     elif number == guess_me:
#         print('found it!')
#         break
#     elif number > guess_me:
#         print('oops')
#         break
#     number += 1

#     #6.3
# guess_me = 5
# for number in range(10):
#     if number < guess_me:
#         print("too low")
#     elif number == guess_me:
#         print("found it!")
#     elif number > guess_me:
#         print("oops")
#         break

