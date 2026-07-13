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


class IceCreamStand(Restaurant):
    """Een simpele voorstelling van een ijscoman"""

    def __init__(self, restaurant_name :str, cuisine_type :str, flavors :list[str]) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors    

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} heeft deze smaken ijs: ")

        for flavor in self.flavors:
            print(f"    - {flavor}")
    
    def add_flavor(self, flavor :str):
        if flavor.lower() in self.flavors:
            print(f"{flavor.title()} is al een smaak in {self.restaurant_name.title()}.")
        else:
            self.flavors.append(flavor.lower())
            print(f"{flavor.title()} is nu een smaak in {self.restaurant_name.title()}.")
    
    def remove_flavor(self, flavor :str):
        if not flavor.lower() in self.flavors:
            print(f"{flavor} is geen smaak in {self.restaurant_name.title()}.")
        else:
            print(f"{flavor} is nu geen smaak meer in {self.restaurant_name.title()}.")
            self.flavors.remove(flavor.lower())