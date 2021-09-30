import re
import json
from datetime import date
from Payment_Request import PAYMENT_REQUEST
from Container_PaymentRequest import ContainerPAYMENT_REQUEST


def menu():
    print("========================================")
    print("The program that processes your payments")
    while True:
        try:
            container = read_in_container()
        except (FileNotFoundError, ValueError) as message:
            print(str(message))
            continue
        break

    while True:
        action = input("\n ========== Select an operation ==========\n"
                     + "   1. Print container\n"
                     + "   2. Search payments by attribute\n"
                     + "   3. Sort container by attribute\n"
                     + "   4. Delete payment from container by ID\n"
                     + "   5. Add payment to container by keyboard\n"
                     + "   6. Exit\n"
                     + " ==========================================\n")

        try:
            if  (action == "1"): print_container(container)
            elif(action == "2"): search_in_container(container)
            elif(action == "3"): sort_container(container)
            elif(action == "4"): delete_from_container(container)
            elif(action == "5"): add_to_container(container)
            elif(action == "6"): break
            else: print("Please try again")
        except ValueError as message:
            print(str(message))
            continue


def read_in_container():
    filename = input("Enter file name in json format: ")
    _container = ContainerPAYMENT_REQUEST(filename)
    _container.read_from_file(filename)
    return _container


def print_container(container):
    print(container)


def search_in_container(container):
    attr = input("Enter an attribute to search: ")
    array = container.search_in_container(attr)
    print("Payments found:\n" + str(array))


def sort_container(container):
    attr = input("Enter an attribute to sort: ")
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




menu()


