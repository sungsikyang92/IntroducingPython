# def dec_to_bin(n):
#     for num in n:
#         if num % 2 !=0:
#             print (num % 2)


def dec_to_bin(n):
    if n < 2:
        return f'{n}'
    return dec_to_bin(n // 2) + f'{n % 2}'

print(dec_to_bin(10))
# => '1010'
print(dec_to_bin(5))
# => '101'
print(dec_to_bin(50))
# => '110010'