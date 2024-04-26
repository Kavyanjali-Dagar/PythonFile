tpl = ('F', 'l', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')
# addition of ! is not possible as tuple is an immutable
# so to add ! we need to create a new tuple and then make tpl refer to it
tpl = tpl + ('!',)
print(tpl)
# convert tuple to string
s = ''.join(tpl)
print(s)
# extract ('b', 'b') from the tuple
t = tpl[3:5]
print(t)
# count number of 'e' in the tuple
count = tpl.count('e')
print('count = ', count)
# check whether 'r' existsin the tuple
print('r' in tpl)
# Convert the tuple to a list
lst = list(tpl)
print(lst)
# tuples are immutable, so we cannot remove elements from it
# we need to split the tuple, eliminate the unwanted element and then merge the tuples
tpl = tpl[:3] + tpl[7:]
print(tpl)