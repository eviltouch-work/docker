def adult():
    print("you are mature")
def non_adult():
    print("you are not 18+")
    
def validate():
    age=int(input("your age: "))
    if age >=18:
        adult()
    else:
        non_adult()

validate()
