from Validation import ExceptionPayment
from Payment_Request import PAYMENT_REQUEST
from Container_PaymentRequest import ContainerPAYMENT_REQUEST


def menu():
    action = input("\n ========== Select an operation ==========\n"
                     + "   1. Print container\n"
                     + "   2. Search payments by attribute\n"
                     + "   3. Sort container by attribute\n"
                     + "   4. Delete payment from container by ID\n"
                     + "   5. Add payment to container by keyboard\n"
                     + "   6. Edit attribute of payment by ID\n"
                     + "   7. Undo last change\n"
                     + "   8. Redo last change\n"
                     + "   9. Exit\n"
                     + " ==========================================\n")
    return action


def main():
    print("========================================")
    print("The program that processes your payments")
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
 

    dictionaryActions = {"1" : print_container, "2" : search_in_container, "3" : sort_container, "4" : delete_from_container, 
                         "5" : add_to_container, "6" : edit_attribute_container, "7" : _undo, "8" : _redo}

    while True:
        try:
            action = menu()
            if action == "9": break
            else:
                dictionaryActions[action](container)            
        except KeyError:
            print("Key is missing. Please try again")
        except (ValueError, ExceptionPayment) as message:
            print(str(message) + "\nPlease try again")
            


def read_in_container():
    filename = input("Enter file name in txt format: ")
    _container = ContainerPAYMENT_REQUEST(filename)
    _container.read_from_file(filename)
    return _container


def print_container(container):
    print(container)


def search_in_container(container):
    attr = input("Enter an value to search: ")
    array = container.search_in_container(attr)
    if len(array) > 0: print("Payments found:\n\n" + str(array))


def sort_container(container):
    attr = input("  1. ID\n" +
                 "  2. Amount\n" +
                 "  3. Currency\n" + 
                 "  4. Payer email\n" + 
                 "  5. Due to date\n" +
                 "  6. Request date\n" +
                 "  7. Transaction id\n")
    container.sort(attr)


def delete_from_container(container):
    id = input("Enter ID to delete: ")
    container.delete(id)


def add_to_container(container):
    id = input("Enter ID: ")
    amount = input("Enter amount: ")
    currency = input("Enter currency: ")
    email = input("Enter payer email: ")
    transaction_id = input("Enter transaction ID: ")
    due_to_date = input("Enter due to date: ")
    request_date = input("Enter request date: ")

    payment = PAYMENT_REQUEST(id, amount, currency, email, transaction_id, due_to_date, request_date)
    container.append(payment)


def edit_attribute_container(container):
    id = input("Enter ID: ")
    attr = input("  1. ID\n" +
                 "  2. Amount\n" +
                 "  3. Currency\n" + 
                 "  4. Payer email\n" + 
                 "  5. Due to date\n" +
                 "  6. Request date\n" +
                 "  7. Transaction id\n")
    value = input("Enter new value: ")
    container.edit(id, attr, value)


def _undo(container):
    container.undo()


def _redo(container):
    container.redo()



main()
