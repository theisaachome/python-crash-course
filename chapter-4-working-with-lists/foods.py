foods=["pizza","falafel","carror cake"];


friend_foods = foods[:];

foods.append("cannoli")
friend_foods.append("ice cream");

print("My favorite foods:")
for food in foods:
    print(food.title());

print("\nMy Friend's favorite foods:")
for food in friend_foods:
    print(food.title());