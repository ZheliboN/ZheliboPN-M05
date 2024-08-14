class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print(f'Такого этажа не существует. '
                  f'В доме c названием "{self.name}" количество этажей: {self.number_of_floor}')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        s = f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'
        return s

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


house_1 = House('ЖК Эльбрус', 10)
house_2 = House('ЖК Акация', 20)
print(house_1)
print(house_2)
print(house_1 == house_2)
house_1 = house_1 + 10
print(house_1)
print(house_1 == house_2)
house_1 += 10
print(house_1)
house_2 = 10 + house_2
print(house_2)
print(house_1 > house_2)
print(house_1 >= house_2)
print(house_1 < house_2)
print(house_1 <= house_2)
print(house_1 != house_2)
