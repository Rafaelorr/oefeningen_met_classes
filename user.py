class User():
    """Een simpele voorstelling van een gebruiker."""

    def __init__(self, first_name :str, last_name :str):
        self.first_name = first_name
        self.last_name = last_name
    
    def greet_user(self):
        print(f"Dag {self.first_name.title()} {self.last_name.title()}.")
    
    def describe_user(self):
        print(f"""Gegevens van de gebruiker:
              Voornaam: {self.first_name.title()}
              Achternaam: {self.last_name.title()}""")