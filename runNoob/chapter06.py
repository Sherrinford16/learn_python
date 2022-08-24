# dict 动态结构可随时添加键值对
# attention！Python3.7之后的版本，字典中元素的排列顺序与定义时相同。如果遍历其元素，将发现元素的排列顺序与添加顺序相同。
#
# 创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)  # {'color': 'green', 'points': 5}

# 修改字典中的值
print(f"The original alien color is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The changed alien color is {alien_0['color']} now.")

# 对一个能够以不同速度移动的外星人进行位置跟踪。
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_1['x_position']}")
# 向右移动外星人，根据当前速度确定将外星人向右移动多远。
# alien_1['speed'] = 'fast'
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的的移动速度肯定很快。
    x_increment = 3
# 新位置为旧位置加上移动距离。
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position']}\n")

# 删除键值对 del语句将相应的键值对彻底删除。使用时必须指明字典名和要删除的键。
alien_2 = {'color': 'green', 'points': 5}
print(alien_2)

del alien_2['points']
print(alien_2, '\n')

# 由类似对象组成的字典，前面是一个对象的多个信息。下面是字典来存储众多对象的同一种信息。
favorite_language = {
    'personA': 'python',
    'personB': 'c',
    'personC': 'java',
    'personD': 'js',
}

language = favorite_language['personA'].title()
print(f"PersonA's favorite language is {language}")

# 使用get()来访问值
# []访问不存在的值将导致KeyError错误 chapter10会介绍处理类似错误，
# 但就字典来说，可以用get()方法在指定的键不存在时返回一个默认值来避免错误。
# 未指定默认值将返回None

# 6.3 遍历字典  虽然test06的6-3实现了相似的功能，但还是要多看下区别
user_0 = {
    'username': 'xiafu',
    'first_name': 'fu',
    'last_name': 'xia'
}
for key, value in user_0.items():  # 方法items()返回一个键值对列表
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# 采用6.2的例子
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# 遍历字典中的所有键, keys()方法
for name in favorite_language.keys():  # keys()方法返回一个列表，其中包含字典中的所有键。
    print(name)

for name in favorite_language:  # 遍历字典时会默认遍历所有的键，但显式地使用key()方法更易理解。
    print(name)

# 通过当前的键访问与之关联的值。
friends = ['personA', 'personB']
for name in favorite_language.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you like {language}")

# 使用keys()方法确定某个人是否接受了调查。
if 'personX' not in favorite_language.keys():
    print("PersonD, please take our poll!")

# 6.3.3 按特定顺序遍历字典中的所有键
# 可以用sorted()函数来获得按特定顺序排列的键列表的副本：
favorite_number = {
    'Spike': 27,
    'Faye': 23,
    'Jet': 36,
    'Ed': 13,
    'Ein': 1011,
}

for name in sorted(favorite_number.keys()):
    print(f"{name.title()}, thanks for taking the poll!")

# 遍历字典中的所有值 values()方法
print("The following numbers have been mentioned:")
for number in favorite_number.values():
    print(number)

# 可以用集合(set)剔除重复项。集合中的每个元素都必须是独一无二的。
favorite_number['pardon'] = 13  # 引入重复value
print("favorite_number:", favorite_number)
for number in set(favorite_number.values()):
    print(number)

# 可以用一对{}直接创建集合，用逗号分隔其中元素。集合不会以特定的顺序存储元素。

# 6.4嵌套 将一系列字典存储在列表中，或将列表作为值存储在字典中balabala
print("\n6.4")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# range()自动生成一些ET
print("\n自动生成：")
new_aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    new_aliens.append(new_alien)

for alien in new_aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in new_aliens[:5]:
    print(alien)
print("...")
print(f"---Total number of aliens: {len(new_aliens)}---")

# 6.4.2 在字典中存储列表 在这个节点上的时候想了想list和dict嵌套使用过程中不同的场景应用。
print("\n6.4.2")

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(topping)

# 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:  # 在这里进行了错误的缩进，导致最后输出language.title()时只拿到了最后的list['python', 'haskell']
        print(f"\t{language.title()}")

# 列表和字典的嵌套层级不应太多，可能有更简单的方法解决多级嵌套-0-


# 6.4.3 在字典中存储字典
print("\n6.4.3")
users = {
       'aeinstein': {
           'first': 'albert',
           'last': 'einstein',
           'location': 'princeton',
        },
       'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
        },
}
for username, userInfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userInfo['first']} {userInfo['last']}"
    location = userInfo['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# 表示每位用户的字典都具有相同的结构，虽然python并没有这样要求，但这样做使得嵌套的字典处理起来更容易。