MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit =0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def coins_operations():
        print("please insert coins ")
        total  =int(input("how many quarters ?")) *0.25
        total+= int(input("how many dimes ?")) * 0.10
        total+= int(input("how many nickles  ?"))* 0.05
        total+= int(input("how many pennies  ?"))*0.01
        return total

def is_transaction_successfull(money_recieved,drink_cost):
     if money_recieved > drink_cost:
          change = round(money_recieved - drink_cost,2)
          print(f"here is your change {change}")
          global profit
          profit+= drink_cost
          return True
     else:
          print("sorry thats enough money . money refunded")
          return False

def make_coffee(drink_name,order_ingredients):
     for item in order_ingredients:
          resources[item] -= order_ingredients[item]
     print(f"here your {drink_name}")
          

is_on = True
user_guess = input("What would you like? (espresso/latte/cappuccino):")
if user_guess == "off":
    is_on = False
elif user_guess == "report":
    print(f"Water: {resources["water"]}")
    print(f"Milk:{resources["milk"]}") 
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money:{profit}")
else:
    drink = MENU[user_guess]
    if resource_sufficient(drink["ingredients"]):
         payment =coins_operations()
         if is_transaction_successfull(payment,drink["cost"]):
              make_coffee(user_guess,drink["ingredients"])
              

