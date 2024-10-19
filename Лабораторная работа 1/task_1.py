numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
count_of_elements = len(numbers)
summa=0
iter = 0
for i in range(count_of_elements):
    if type(numbers[i]) != int: i = iter
    else:  summa += numbers[i]
average = summa/count_of_elements

for j in range(count_of_elements):
    if type(numbers[j])!= int: numbers[j] = average


print("Измененный список:", numbers)
