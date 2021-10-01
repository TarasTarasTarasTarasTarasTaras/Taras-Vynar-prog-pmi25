import json
from Validation import Validation
from Payment_Request import PAYMENT_REQUEST
from Payment_Request import ExceptionPayment


class ContainerPAYMENT_REQUEST: 
    def __init__(self, file_name = "None"):
        self.__array_of_elements = []
        self.__file_name = file_name
        self.__validation = Validation()


    def __str__(self):
        string = ""
        for payment in self.__array_of_elements:
            string += str(payment) + "\n" + "-"*30 + "\n"
        return string


    def __repr__(self):
        return self.__str__()


    def read_from_file(self, value = "None"):
        try:
            if (self.__validation.validate_file("File name", value)) is True: 
                file = open(value)
        except ValueError as message:
            raise ValueError("Error reading from file: " + str(message))
        except FileNotFoundError:
            raise ValueError("  ERROR: File not found")
        
        self.__array_of_elements = []
        filesJSON = json.load(file)
        number = success = 0
        for payment_request in filesJSON:
            number += 1
            try:
                payment = PAYMENT_REQUEST(
                    payment_request.get("ID"),
                    payment_request.get("Amount"),
                    payment_request.get("Currency"),
                    payment_request.get("Email"),
                    payment_request.get("Transaction ID"),
                    payment_request.get("Due to date"),
                    payment_request.get("Request date"))
            except ValueError as message:
                print(message)
                print("Product number " + str(number) + " is defective")
                continue
            self.__array_of_elements.append(payment)
            success += 1
        print("\n" + str(success) + " objects were successfully read from the file: " + str(value))


    def write_to_file(self, value):
        try:
            if self.__validation.validate_file("File name", value) is True:
                file = open(value, mode = "w")
        except ValueError as message:
            print("  ERROR: " + str(message))
            raise ValueError("Error reading from file")
        except FileNotFoundError:
            raise ValueError("  ERROR: File not found")

        file.write("[\n")
        current_payment = 0
        for payments in self.__array_of_elements:
            file.write(" {\n")
            file.write(str(payments))
            file.write(" }")
            current_payment += 1
            if(current_payment < len(self.__array_of_elements)):
                file.write(",\n")
        file.write("\n]")
        file.close()


    def append(self, payment):
        try:
            self.__validation.validate_PAYMENT(payment)
        except ValueError as message:
            raise ValueError(message + "\nObject not added")
        
        self.__array_of_elements.append(payment)
        if self.__file_name != "None":
            self.write_to_file(self.__file_name)
        print("Object added successfully")


    def delete(self, ID):
        try:
            if self.__validation.validate_ID("ID", ID) is not True:
                raise ValueError("")
            index = 0
            for payment in self.__array_of_elements:
                if str(payment.get_id()) == str(ID):
                    self.__array_of_elements.pop(index)
                    if self.__file_name != "None":
                        self.write_to_file(self.__file_name)
                    print("Object deleted successfully")
                    return
                index += 1
            else: 
                raise ExceptionPayment("Object not found")
            raise ExceptionPayment("Container is empty")
        except ValueError as message:
            raise ValueError("Item can not be deleted. " + message)


    def search_in_container(self, search_string):
        wanted_payments = ContainerPAYMENT_REQUEST()
        counter_of_found_elements = 0

        for payment in self.__array_of_elements:
            for getter in payment.getAll_getters():
                if str(getattr(payment, getter)()).find(str(search_string)) != -1:
                    wanted_payments.append(payment)
                    counter_of_found_elements += 1
                    break

        print("Payments successfully found: " + str(counter_of_found_elements))
        return wanted_payments


    def sort(self, key):
        dictionaryGets = {"1" : "get_id", "2" : "get_amount", "3" : "get_currency", "4" : "get_payer_email", 
                          "5" : "get_payment_due_to_date", "6" : "get_payment_request_date", "7" : "get_transaction_id"}
        try:
            if type(getattr(self.__array_of_elements[0], dictionaryGets[key])) is str:
                self.__array_of_elements.sort(key = lambda payment : getattr(payment, dictionaryGets[key])().lower())
            else:
                self.__array_of_elements.sort(key = lambda payment : getattr(payment, dictionaryGets[key])())
        except:
            print("The container can not be sorted")
            raise ExceptionPayment("Key " + key + " is missing")

        print("The container was successfully sorted by the attribute: " + key)


    def edit(self, ID, key, value):  
        for payment in self.__array_of_elements:
            if str(payment.get_id()) == str(ID):
                dictionarySets = {"1" : payment.set_id, "2" : payment.set_amount, "3" : payment.set_currency, "4" : payment.set_payer_email, 
                                  "5" : payment.set_payment_due_to_date, "6" : payment.set_payment_request_date, "7" : payment.set_transaction_id}
                try:
                    dictionarySets[key](value)
                except KeyError:
                    raise ExceptionPayment("Key " + key + " is missing")
                except (ValueError, ExceptionPayment) as message:
                    raise ExceptionPayment(str(message))
              
                if self.__file_name != "None":
                        self.write_to_file(self.__file_name)
                print("Attribute successfully edited")
                return
        raise ExceptionPayment("Element with id " + str(ID) + " is missing")


    def set_the_file(self, filename):
        self.__file_name = filename


    def __len__(self):
        return len(self.__array_of_elements)

