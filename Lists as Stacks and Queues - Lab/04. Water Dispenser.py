from collections import deque


class Water_despenser:
    quantity = 0
    water_line = deque()

    def add_person(self, name: str):
        self.water_line.append(name)

    def refill(self, liters: int):
        self.quantity += liters

    def get_water(self, liters: int):
        if liters <= self.quantity:
            self.quantity -= liters
            return f"{self.water_line.popleft()} got water"
        return f"{self.water_line.popleft()} must wait"


dispenser = Water_despenser()
dispenser.quantity = int(input())
person = input()

while person != 'Start':
    dispenser.add_person(person)
    person = input()

command = input()
while command != 'End':
    if command.isdigit():
        print(dispenser.get_water((int(command))))
    else:
        _, liter_to_refill = command.split()
        dispenser.refill(int(liter_to_refill))
    command = input()

print(f'{dispenser.quantity} liters left')