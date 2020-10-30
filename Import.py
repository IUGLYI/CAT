from script import Cat

cat1 = Cat('Sam', 'Boy', 2)
cat2 = Cat('Baron', 'Boy', 2)

cats =[cat1, cat2]

for cat in cats:
    print('Name:', cat.get_name(),
          'Gender:', cat.get_gender(),
          'Age:', cat.get_age())
