from restaurant import Restaurant

aziatisch_restaurant = Restaurant("Asian take-away","Aziatische keuken")
aziatisch_restaurant.describe_restaurant()
aziatisch_restaurant.open_restaurant()

print(aziatisch_restaurant.number_served)

aziatisch_restaurant.set_number_served(54)

print(aziatisch_restaurant.number_served)

aziatisch_restaurant.increment_number_served(30)

print(aziatisch_restaurant.number_served)
