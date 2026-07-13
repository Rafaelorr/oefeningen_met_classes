from restaurant import IceCreamStand

ijskraam = IceCreamStand("'s coupe", "ijsjes", ["chocolade", "vanille", "aardbei", "smurf"])
ijskraam.describe_restaurant()

ijskraam.add_flavor("mokka")

ijskraam.describe_restaurant()

ijskraam.remove_flavor("aardbei")

ijskraam.describe_restaurant()