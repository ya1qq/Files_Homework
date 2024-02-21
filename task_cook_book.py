def create_cook_book(file_name):
  cook_book = {}
  with open(file_name, encoding='utf-8') as f:
      lines = f.readlines()

  i = 0
  while i < len(lines):
      dish_name = lines[i].strip()
      i += 1
      ingredients_count = int(lines[i].strip())
      i += 1
      ingredients = []
      while i < len(lines) and lines[i].strip():
          ingredient_info = lines[i].strip().split('|')
          ingredient_name = ingredient_info[0].strip()
          quantity = int(ingredient_info[1].strip())
          measure = ingredient_info[2].strip()
          ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
          ingredients.append(ingredient)
          i += 1
      cook_book[dish_name] = ingredients
      i += 1

  return cook_book

cook_book = create_cook_book('recipes.txt')

print(cook_book)
print()

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
      if dish not in cook_book:
          print(f'Блюдо "{dish}" отсутствует в книге рецептов.')
          continue
      for ingredient in cook_book[dish]:
          ingredient_name = ingredient['ingredient_name']
          measure = ingredient['measure']
          quantity = ingredient['quantity'] * person_count
          if ingredient_name not in shop_list:
              shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
          else:
              shop_list[ingredient_name]['quantity'] += quantity
  return shop_list

print(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 3))
