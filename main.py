from random import randint
from typing import Callable
from csv import writer, reader, QUOTE_NONNUMERIC
from json import dump


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def get_random_numbers_to_csv() -> None:
    lenght: int = randint(100, 1000)
    nums: list[int] = []
    temp: list[int] = []
    
    for _ in range(lenght):
        nums.append(randint(-1000, 1000))
    
    with open("nums.csv", "+w", newline='') as f:
        write = writer(f, quoting=QUOTE_NONNUMERIC)
        
        for i in range(len(nums)):
            if i % 3 == 0 and i != 0:
                write.writerow(temp)
                temp = []
            temp.append(nums[i])


# Декоратор, запускающий функцию нахождения корней 
# квадратного уравнения с каждой тройкой чисел из csv файла.
def get_parametrs_from_csv(func: Callable):
    result = {}
    def wrapper(*args, **kwargs):
        nonlocal result
        temp = []
        with open("nums.csv", '+r') as f:
            nums = reader(f)
            for i, lines in enumerate(nums):  
                for j in lines:
                    temp.append(j)
                
                temp = list(map(int, temp))
                result[*func(*temp)] = [*temp]
                temp = []
        return result  
    return wrapper()


# Декоратор, сохраняющий переданные параметры 
# и результаты работы функции в json файл.
def save_to_json(func: Callable):
    file_name = "result.json"
    def save(*args, **kwargs):
        nonlocal file_name
        to_save = {}
        for result, params in (func.items()):
            to_save[f"{result}"] = [f"{params}"]
        with open(file_name, '+w') as f:
            dump(to_save, indent=2, separators=(',', ':'), fp=f)
    return save


# Нахождение корней квадратного уравнения
@save_to_json
@get_parametrs_from_csv
def quadratic_equation(a: int, b: int, c: int) -> list:
    x = []
    discremenant = b**2 - 4*a*c
    x.append((-b + (discremenant)**(1/2))/(2*a))
    x.append((-b - (discremenant)**(1/2))/(2*a))
    return x


if __name__ == "__main__":
    # print(get_random_numbers_to_csv())
    quadratic_equation()
