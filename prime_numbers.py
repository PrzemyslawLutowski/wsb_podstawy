print('Witaj w programie zwracającym liczby pierwsze')
user_value = input('Podaj ostatnią liczbę zakresu do sprawdzenia liczb pierwszych: ')
user_value = int(user_value)


prime_numbers_list = []
for value in range(2, user_value + 1):
    prime_numbers_list.append(value)

for value in range(1, user_value + 1):
    for less_value in range(2, value):
        if value % less_value == 0:
            prime_numbers_list.remove(value)
            break


print('Oto lista liczb pierwszych z zakresu liczb od 1 do ' + str(user_value) + ':', prime_numbers_list)

