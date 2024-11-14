print("Witaj w kalkulatorze bmi")


weight_value = True
while weight_value:

    weight = input('Podaj swoją wagę (kg): ')

    try:
        weight = float(weight)
        weight_value = False
    except ValueError:
        print('Błąd wartości dziesiętnej - podaj wartość dziesiątną użuwając kropki, np. 90.5')


height_value = True
while height_value:

    height = input('Podaj swój wzrost (m): ')

    try:
        height = float(height)
        height_value = False
    except ValueError:
        print('Błąd wartości dziesiętnej - podaj wartość dziesiątną użuwając kropki, np. 1.9')


bmi = round(weight / height ** 2, 2)


if bmi < 18.5:
    print('Twój wskaźnik bmi wynosi ', str(bmi) + ' - ', 'Niedowaga!')

elif bmi > 25:
    print('Twój wskaźnik bmi wynosi ', str(bmi) + ' - ', 'Nadwaga!')

else:
    print('Twój wskaźnik bmi wynosi ', str(bmi) + ' - ', 'Waga prawidłowa! Brawo')