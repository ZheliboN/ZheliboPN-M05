class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

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
print(House.houses_history)
house_2 = House('ЖК Акация', 20)
print(House.houses_history)
house_3 = House('ЖК Матрешки', 20)
print(House.houses_history)
del house_2
del house_3
print(House.houses_history)
