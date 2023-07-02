if __name__ == '__main__':
    # Завдання 1
    numbers1 = int(input("Введіть першу цифру: "))
    numbers2 = int(input("Введіть другу цифру: "))
    numbers3 = int(input("Введіть третю цифру: "))

    number = int(str(numbers1) + str(numbers2) + str(numbers3))

    print("Створене число:", number)

    # Завдання 2
    number = int(input("Введіть число з чотирьох цифр: "))

    # Розділити число на окремі цифри
    numbers1 = number // 1000
    numbers2 = (number // 100) % 10
    numbers3 = (number // 10) % 10
    numbers4 = number % 10

    # Обчислити добуток цифр
    product = numbers1 * numbers2 * numbers3 * numbers4

    print("Добуток цифр:", product)

    # Завдання 3
    meters = float(input("Введіть кількість метрів: "))

    centimeters = meters * 100
    decimeters = meters * 10
    millimeters = meters * 1000
    miles = meters / 1609.34

    print("У сантиметрах:", centimeters)
    print("У дециметрах:", decimeters)
    print("У міліметрах:", millimeters)
    print("У милях:", miles)

    base = float(input("Введіть розмір основи трикутника: "))
    height = float(input("Введіть розмір висоти трикутника: "))

    area = 0.5 * base * height

    print("Площа трикутника:", area)

    # Завдання 4
    base = float(input("Введіть розмір основи трикутника: "))
    height = float(input("Введіть розмір висоти трикутника: "))

    area = 0.5 * base * height

    print("Площа трикутника:", area)

    # Завдання 5
    number = int(input("Введіть чотиризначне число: "))

    reversed_number = int(str(number)[::-1])

    print("Перевернуте число:", reversed_number)

