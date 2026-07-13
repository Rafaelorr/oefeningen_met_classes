class Restaurant():
    """Een simpele voorstelling van een restaurant"""

    def __init__(self, restaurant_name :str, cuisine_type :str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serveert uit de {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is nu open")
    
    def set_number_served(self, number_served :int):
        self.number_served = number_served
    
    def increment_number_served(self, number_served :int):
        self.number_served += number_served