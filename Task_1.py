numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

num1 = numbers[0:4:]
num2 = numbers[5::]
average = (sum(num1)+sum(num2))/len(numbers)
numbers[4] = average

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
