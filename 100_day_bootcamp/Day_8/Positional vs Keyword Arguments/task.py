# Functions with input

#def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")

def greet_with(name: str, location: str):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
#greet_with("Piers", "Ely")
greet_with(location="Ely", name="Piers")