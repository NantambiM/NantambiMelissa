""" a=5
if not a:
    print("there is no 'a'")
else:
    print("a has a value")

b=5
print(a and b)

if a or not b:
    print('only a')
else:
    print('both of them')

print('a is greater') if a>b else print('b is greater'+ str(b))

while a>0:
    print(f"a is now {a}")
    a=a-1
else:
    print("a is now 0") """

###########LISTS##########
mylist=list(['cow','goat','banana','cricket','mantis'])
print(mylist[1])
mylist[0]='cockroach'
print(mylist)
mylist.append('buffalo')
print(mylist)
mylist[2]='Bathel'
print(mylist)
del mylist[3]
print(mylist)
print(mylist[-1])

new_list=list(['mango','guava','pawpaw','watermelon','orange','pineapple','pear'])
print(new_list[2:5])

countries=['Uganda','Kenya','Tanzania']
countries1=countries.copy()
print(countries1)

for country in countries1:
    print(country)


animals=['cow','dog','cat','goat','buffalo','rhino','tiger','lion','monkey']
print(sorted(animals))
print(sorted(animals,reverse=True))

for animal in animals:
    if 'a' in animal:
        print(animal)

first_names=list(['Nantambi'])
second_names=list(['Melissa'])

full_names=first_names+second_names
print(full_names)



##########TUPLES################
x=('samsung','iphone','tecno','redmi')
favorite,*rest=x
print(favorite)
print(x[0])
print(x[-2])
x1=list(x)
x1[1]='itel'
x1.append('Huawei')
x1.remove('samsung')
x=tuple(x1)
print(x)

for phone in x:
    print(phone)

uganda_cities=tuple(('Kampala','Mbarara','Mbale','Gulu','Fort Portal'))
central,western,eastern,northern,south_western=uganda_cities
print(central)
print(western)
print(eastern)
print(northern)
print(south_western)

c1=list(uganda_cities)
print(c1[1:4])

firstnames=tuple(['Nantambi'])
secondnames=tuple(['Melissa'])

fullname=tuple(firstnames+secondnames)
print(fullname)

colours=('pink','yellow','gold')
colours_multiplied=colours*3
print(colours_multiplied)

thistuple=(1,3,7,8,7,5,4,6,8,5)
count8=0
for item in thistuple:
    if item==8:
        count8=count8+1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
print(f"8 appears {count8} times in thistuple")
# thistuple.count(8)


##############SETS##############
myfavouritebeverages=set({'mirinda orange','mirinda pineapple','minute maid'})
print(myfavouritebeverages)
myfavouritebeverages.update(['water','milk'])
fav1=myfavouritebeverages.pop()
print(fav1)
print(myfavouritebeverages)

mySet={'oven','microwave','kettle','refrigerator'}
print(True) if 'microwave' in mySet else print(False)
mySet.remove('kettle')#or dicard
print(mySet)
    
for item in mySet:
    print(item)


##############STRINGS##############
m=12
n='What is going on?'
print(f"{str(m)+n}")

txt="    Hello,    Uganda!    "
print(txt.strip())
print(txt.replace(" ",""))
print(txt.upper())
print(txt.replace("U","V"))

y="I am proudly Ugandan"
print(y[1:5])

x="All 'Data Scientists' are cool!"


############DICTIONARIES############
Shoes={
    "brand":"Nick",
    "color":"black",
    "size":40
}
print(Shoes['size'])
Shoes['brand']="Adidas"
print(Shoes)
Shoes['type']="Sneakers"
print(Shoes)
print(Shoes.keys())
print(Shoes.values())

if 'size' in Shoes.keys():
    print("Yes, it is there")
else:
    print("No, it isn't there")

for key,value in Shoes.items():
    print(f"{key}: {value}")

del Shoes['color']
print(Shoes)
Shoes.clear()
print(Shoes)

myChoice={
    "drink":"Minute maid",
    "sweet":"Chocolate",
    "snack":"scone"
}
myChoice1=myChoice.copy()
print(myChoice1)

myChoice2={
    'drinks':{
        'softdrinks':'Mirinda Orange',
        'fruitdrinks':'Minute maid'
    },
    'snacks':{
        'flour':'scones',
        'meat':'sausages'
    }
}