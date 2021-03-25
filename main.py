import collections

my_str = input().strip()
answer = collections.Counter(my_str)
a = answer.most_common(3)
print(a)