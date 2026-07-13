class Restaurant():
    """Een simpele voorstelling van een restaurant"""

    def __init__(self, restaurant_name :str, cuisine_type :str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serveert uit de {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is nu open")