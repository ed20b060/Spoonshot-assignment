ingredients = ['Ambrette Seed', 'Apple Cinnamon Granola', 'Arizona Seasoning', 'Americano Coffee',
               'Baby Abalone',
               'Cadbury Double Decker Chocolate Bar',
               'Campari Tomato',
               'Celery Soup',
               'Chia Meal',
               'Crunch Bars',
               'Cardamom',
               'Giardiniera',
               'Hog Maw',
               'Mccormick Montreal Steak Seasoning',
               'Muesli',
               'Mulberry',
               'Munch Chocolate',
               'Murukku Packet',
               'Mango',
               'Organic Maize',
               'Organic Peruvian Groundcherry',
               'Organic Tartar Cream',
               'Orange Extract',
               'Pickled Cauliflower',
               'Pork Chump Chops',
               'Pork Lungs',
               'Pork Tripe',
               'Peanut Butter',
               'Smokies Sausage',
               'Snickers Spread',
               'Strawberry Gelatin',
               'Salmon',
               'Tomato',
               'Tamarind',
               'Vegan Carob Chips',
               'Vegan Chicken Strips',
               'Vegan Chorizo',
               'Vegan Marshmallow',
               'Vegan Puff Pastry Sheet',
               'Vegan Semisweet Chocolate Chips',
               'Vegan White Cake',
               'Vegetable Stock',
               'Vinegar']
for i in range(len(ingredients)):
    ingredients[i] = str.lower(ingredients[i])

freq = {}
while True:
    sent = input()
    if len(sent) != 0:
        sent = sent.split()
        for words in sent:
            try:
                freq[words] = freq[words] + 1
            except:
                freq[words] = 1
        print(sent)
    else:
        break

rank = {}
print(freq)
for ing in ingredients:
    temp = ing.split(' ')
    count = 0
    for word in temp:
        try:
            count = count + freq[word]
        except:
            continue
    print(count)
    if count > 0:
        rank[ing] = count
print(rank)
