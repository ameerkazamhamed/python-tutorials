
mylist = [
    '_private',
    'spam',
    '_anotherprivate',
    'eggs'
]

print(mylist)
print(['my:'+each for each in mylist])
print([{'my':each} for each in mylist])

print(mylist)
print([each for each in mylist if not each.startswith('_')])
