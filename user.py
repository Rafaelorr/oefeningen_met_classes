class User():
    """Een simpele voorstelling van een gebruiker."""

    def __init__(self, first_name :str, last_name :str):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0
    
    def greet_user(self):
        print(f"Dag {self.first_name.title()} {self.last_name.title()}.")
    
    def describe_user(self):
        print(f"""Gegevens van de gebruiker:
              Voornaam: {self.first_name.title()}
              Achternaam: {self.last_name.title()}""")
    
    def increase_login_attemps(self):
        self.login_attemps += 1
    
    def reset_login_attemps(self):
        self.login_attemps = 0