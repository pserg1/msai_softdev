from item import ItemHolder
from shelf import ClassicShelf
from vending import Vending

# initialize first vending machine
items1 = [[('Candy', 5), ('Chips', 3), ('Coke', 2)],
              [('Juice', 2), ('Snack', 3), ('Apple', 4)],
              [('Muffin', 6), ('Water', 4), ('Coffee', 7)]]

vending_machine = Vending.FromItemNames(ItemHolder, ClassicShelf, items1)

# initialize second vending machine
items2 = [[('Candy',5), ('Chips', 3), ('Coke', 2)],
            [('Apple', 4), ('Orange', 5), ('Waffles', 7)]]

vending_machine2 = Vending.FromItemNames(ItemHolder, ClassicShelf, items2)

print(f"\nTotal item cost ov vending machine 1 = {vending_machine.cost}")
print(f"Total item cost ov vending machine 2 = {vending_machine2.cost}\n")

# check union, intersection, and difference between two vending machines
print(Vending.ContentUnion(vending_machine, vending_machine2))
print(Vending.ContentDifference(vending_machine, vending_machine2))
print(Vending.ContentIntersection(vending_machine, vending_machine2))

# both vendings start with the same amount of cash
print(vending_machine == vending_machine2)

item_name, Vending = vending_machine.TakeItem(1,2)

print(f"Purchased {item_name} that costs {Vending}")
print(f"New balance of the vending machine = {vending_machine.money}")

# vending 1 now has more cash
print(vending_machine == vending_machine2)