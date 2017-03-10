#when we create any dictionary it is object or instances of dict()
fruit = dict()
print type(fruit)
#print dictionary in sorted order
fruit = {'mango':40,'banana':30,'orange':20,'cherry':10}
print fruit.keys()
print fruit.values()
for i in sorted(fruit):
    print i,':', fruit[i]
#to print values in dictionary in sorted order
for s in sorted(fruit.values()):
    print s
#to print keys in sorted order
for k in sorted(fruit.keys()):
    print k
#to print dictionary in reverse order
#
#

