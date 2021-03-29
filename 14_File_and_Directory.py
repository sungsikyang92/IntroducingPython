# fout = open('oops.txt', 'wt')
# fout.close()

# fout = open('oops.txt', 'wt')
# print('Oops, I created a file.', file=fout)
# fout.close()

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
# print(len(poem))
#
# fout = open('relativity', 'wt')
# fout.write(poem)
# fout.close()

# fout = open('relativity', 'wt')
# print(poem, file=fout, sep='', end='')
# fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset= 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()