from Validation import *
from Payment_Request import *
from Memento import *
import copy


class ContainerPAYMENT_REQUEST: 
    def __init__(self, file_name = "None"):
        self.__array_of_elements = []
        self.__file_name = file_name
        self.__validation = Validation()
        self.__caretaker = Caretaker()

    def __str__(self):
        string = ""
        for payment in self.__array_of_elements:
            string += str(payment) + "\n" + "-"*30 + "\n"
        return string


    def __repr__(self):
        return self.__str__()


    def __snapshot(self):
        self.__caretaker.add_snapshot_undo(Memento(copy.deepcopy(self.__array_of_elements)))


    def undo(self, write_to_file = True):
        if self.__caretaker.size_snapshot_undo() > 0:
            self.__caretaker.add_snapshot_redo(Memento(copy.deepcopy(self.__array_of_elements)))
            self.__array_of_elements = copy.deepcopy(self.__caretaker.get_undo_state())
            self.__caretaker.pop_snapshot_undo()
            if write_to_file: self.write_to_file(self.__file_name)
            print("<<< Container data restored successfully >>>\n")
            return self.__array_of_elements
        else:
            print(" Warning!!! At the moment it is impossible\n")


    def redo(self, write_to_file = True):
        if self.__caretaker.size_snapshot_redo() > 0:
            self.__snapshot()
            self.__array_of_elements = copy.deepcopy(self.__caretaker.get_redo_state())
            self.__caretaker.pop_snapshot_redo()
            if write_to_file: self.write_to_file(self.__file_name)
            print("<<< Container data restored successfully >>>\n")
            return self.__array_of_elements
        else:
            print(" Warning!!! At the moment it is impossible\n")
    


    def read_from_file(self, value = "None"):
        if (self.__validation.validate_file("File name", value)) is True: 
            file = open(value)

        
       #self.__snapshot()
        self.__array_of_elements = []
        number = success = 0

        array_values = [] 
        for i in file:
            if i[0] == "=": continue
            i = i.split()
            array_values.append(i[1])
            
        array_values.reverse()

        while len(array_values) > 0:
            try:
                number += 1
                array_attr = []
                for i in range(len(PAYMENT_REQUEST.array_of_names)):
                    array_attr.append(array_values.pop())

                payment = PAYMENT_REQUEST(*array_attr)

            except ValueError as message:
                print(message)
                print("Product number " + str(number) + " is defective")
                while len(array_values) > 0 and len(array_values) % len(PAYMENT_REQUEST.array_of_names) != 0:
                    array_values.pop()
                continue
            self.__array_of_elements.append(payment)
            success += 1
        print("\n" + str(success) + " objects were successfully read from the file: " + str(value))


    def write_to_file(self, value):
        if self.__validation.validate_file("File name", value) is True:
            file = open(value, mode = "w")

        for payments in self.__array_of_elements:
            file.write(str(payments))
            file.write("\n========================\n")
        file.close()


    def append(self, payment):    
        self.__validation.validate_PAYMENT("payment", payment)
        
        self.__snapshot()
        self.__array_of_elements.append(payment)
        if self.__file_name != "None":
            self.write_to_file(self.__file_name)
        print("Object added successfully")


    def delete(self, ID):
        self.__validation.validate_ID(lambda id : id)
        index = 0
        for payment in self.__array_of_elements:
            if str(payment.get_id()) == str(ID):
                self.__snapshot()
                deleted_payment = self.__array_of_elements.pop(index)
                if self.__file_name != "None":
                    self.write_to_file(self.__file_name)
                print("Object deleted successfully")
                return deleted_payment
            index += 1
        else: 
            raise ExceptionPayment("Object not found or container is empty")


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
            self.__snapshot()
            if type(getattr(self.__array_of_elements[0], dictionaryGets[key])) is str:
                self.__array_of_elements.sort(key = lambda payment : getattr(payment, dictionaryGets[key])().lower())
            else:
                self.__array_of_elements.sort(key = lambda payment : getattr(payment, dictionaryGets[key])())
        except:
            self.__snapshots.pop()
            print("The container can not be sorted")
            raise ExceptionPayment("Key " + key + " is missing")

        print("The container was successfully sorted by the attribute: " + key)


    def edit(self, ID, key, value):  
        for payment in self.__array_of_elements:
            if str(payment.get_id()) == str(ID):
                dictionarySets = {"1" : payment.set_id, "2" : payment.set_amount, "3" : payment.set_currency, "4" : payment.set_payer_email, 
                                  "5" : payment.set_payment_due_to_date, "6" : payment.set_payment_request_date, "7" : payment.set_transaction_id}
                try:
                    self.__snapshot()
                    dictionarySets[key](value)
                except KeyError:
                    self.__snapshots.pop()
                    raise ExceptionPayment("Key " + key + " is missing")

                if self.__file_name != "None":
                        self.write_to_file(self.__file_name)
                print("Attribute successfully edited")
                return
        raise ExceptionPayment("Element with id " + str(ID) + " is missing")


    def set_the_file(self, filename):
        self.__file_name = filename


    def get_filename(self):
        return self.__file_name


    def get_payment(self, index):
        if 0 <= index < len(self.__array_of_elements):
            return self.__array_of_elements[index]


    def get_last(self):
        if len(self.__array_of_elements) == 0: return None
        return self.__array_of_elements[len(self.__array_of_elements) - 1]


    def clear(self):
        self.__array_of_elements.clear()
        self.__file_name = 'None'


    def __len__(self):
        return len(self.__array_of_elements)