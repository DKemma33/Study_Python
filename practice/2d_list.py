
# fruits = ["apple","orange","banana","coconut"]
# vagetables = ["celery","carrots","potatoes"]
# meat = ["chicken","fish","turkey"]
#
# groceries = [fruits,vagetables,meat]



# fruits[0] = "pineapple"
# #['pineapple', 'orange', 'banana', 'coconut']
# print(fruits)
# #[['pineapple', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]
# print(groceries)
# #['pineapple', 'orange', 'banana', 'coconut']
# print(groceries[0])
# #pineapple
# print(groceries[0][0])

groceries = [
    ["apple","orange","banana","coconut"],
    ["celery","carrots","potatoes"],
    ["chicken","fish","turkey"]
]
# 위 같은 식은 다음 칸으로 갈때 마다 , 가 필요하다
for collection in groceries:
    print(collection)
# ['apple', 'orange', 'banana', 'coconut']
# ['celery', 'carrots', 'potatoes']
# ['chicken', 'fish', 'turkey']

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
# apple orange banana coconut
# celery carrots potatoes
# chicken fish turkey

#-------------------------------------------------------------------
# NUMBER PAD

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #