from random import randint
from typing import Callable
from csv import writer, reader, QUOTE_NONNUMERIC
from json import dumps

# Нахождение корней квадратного уравнения

def quadratic_equation(a: int, b: int, c: int):
    pass


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def get_random_numbers_to_csv() -> None:
    lenght: int = randint(100, 1000)
    nums: list[int] = []
    temp: list[int] = []
    
    for i in range(lenght):
        nums.append(randint(-1000, 1000))
    
    with open("nums.csv", "+w", newline='') as f:
        write = writer(f, quoting=QUOTE_NONNUMERIC)
        
        for i in range(len(nums)):
            if i % 3 == 0 and i != 0:
                write.writerow(temp)
                temp = []
            temp.append(nums[i])
            
    

if __name__ == "__main__":
    print(get_random_numbers_to_csv())
    