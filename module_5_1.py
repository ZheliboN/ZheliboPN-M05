# Создайте класс House.
class House:
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
    def __init__(self, name, number_of_floor):
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
        self.name = name
        self.number_of_floor = number_of_floor
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print(f'Такого этажа не существует. В доме c названием "{self.name}" количество этажей: {self.number_of_floor}')
        else:
            for i in range(1,new_floor+1):
                print(i)
    def house_name_info(self):
        print(f'Информация по дому с названием "{self.name}":')


# Создайте объект класса House с произвольным названием и количеством этажей.
house_1 = House('ЖК Солнечная Башня',15)
house_1.house_name_info()
# Вызовите метод go_to у этого объекта с произвольным числом.
house_1.go_to(5)
house_2 = House('Домик Пуха',2)
house_2.house_name_info()
house_2.go_to(3)
