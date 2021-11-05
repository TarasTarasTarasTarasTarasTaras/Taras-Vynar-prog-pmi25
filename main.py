'''
Варіант 1 
Створити клас FlightBooking, який містить такі поля
 1. AviaCompany (enum: Wizzair, Ryanair, SkyUp, QatarAirlines)
 2. NoOfPeople (1-300)
 3. StartTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)).
 4. EndTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)). Min: StartTime. 
 5. Date
 6. FlightNumber (XX YYYY, X - літера, Y - цифра) 
Створити такі методи:
 1. Зчитати масив (клас для роботи з масивом екземплярів класу FlightBooking) FlightBooking з файла (1)
 2. Додати новий FlightBooking. На один рейс і на одну дату може бути заброньовано одночасно не більше 300 місць. 
 Ну і звісно, що один і той самий рейс не може здійснюватись практично одночасно. 
 Наприклад, #1: Ryanair, FR2301, 3.11.2021 10:00 - 11:00 та #2: Ryanair, FR2301, 3.11.2021 10:30 - 12:00 (3)
 3. Додати валідацію на всі поля. (2)
 4. Визначити годину, на яку є найбільше замовлень. Якщо таких декілька - вивести всі години. (2)
 5. Авіалінію з найбільшою кількістю польотів за останній рік записати в інший файл: Ryanair, 5 (1.5)
 6. Вивести всі FlightBooking на екран (0.5)
'''

from FlightBookingContainer import FlightBookingContainer

def menu():
    action = input("\n ========== Select an operation ==========\n"
                     + "   1. Print container\n"
                     + "   0. Exit\n"
                     + " ==========================================\n")
    return action


def main():
    print("========================================")
    while True:
        try:
            container = read_in_container()
            break
        except ValueError as message:
            print(str(message))
            continue
        except FileNotFoundError:
            print("File not found")
            continue
 

    dictionaryActions = {"1" : print_container}

    while True:
        try:
            action = menu()
            if action == "0": break
            else:
                dictionaryActions[action](container)            
        except KeyError:
            print("Key is missing. Please try again")
        except (ValueError) as message:
            print(str(message) + "\nPlease try again")


def read_in_container():
    filename = input("Enter file name in txt format: ")
    _container = FlightBookingContainer(filename)
    _container.readFromFile()
    return _container