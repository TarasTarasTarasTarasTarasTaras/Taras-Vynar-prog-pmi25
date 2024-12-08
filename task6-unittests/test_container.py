import unittest
from Container_PaymentRequest import *
from Payment_Request import *
from basedata_test import basedata_payments, basedata_valid_attr
from test_payment import *

class TestContainer_Main(unittest.TestCase):
    container = ContainerPAYMENT_REQUEST()


    def test_get_filename(self):
        self.container.set_the_file('valid_payment.txt')
        self.assertEqual(self.container.get_filename(), 'valid_payment.txt')


    def test_setter_file(self):
        self.container.set_the_file('name.txt')
        self.assertEqual(self.container.get_filename(), 'name.txt')
        self.container.set_the_file('valid_payment.txt')
        self.assertEqual(self.container.get_filename(), 'valid_payment.txt')
        

    def test_clear(self):
        self.container.read_from_file('valid_payment.txt')
        old_size = len(self.container)
        self.assertGreater(old_size, 0)
        self.container.clear()
        self.assertEqual(0, len(self.container))


    def test_get_size_container(self):
        self.container.clear()
        self.assertEqual(len(self.container), 0)
        self.container.read_from_file('valid_payment.txt')
        self.assertEqual(len(self.container), 2)


    def test_append(self):
        self.container.clear()
        for i in range(len(basedata_payments)):
            self.container.append(basedata_payments[i])
            self.assertEquals(self.container.get_payment(i), basedata_payments[i])


    def test_search(self):
        self.container.clear()
        for i in range(len(basedata_payments)): self.container.append(basedata_payments[i])
        found_items = self.container.search_in_container('1')
        self.assertEqual(len(found_items), 3)

        found_items = self.container.search_in_container('we are looking for missing elements')
        self.assertEqual(len(found_items), 0)


    def test_undo(self):
        self.container.clear()
        for i in range(len(basedata_payments)): self.container.append(basedata_payments[i])
        last_item = self.container.get_last()
        self.assertEqual(last_item, basedata_payments[2])
        
        self.container.undo(False) # False - write to file
        last_item = self.container.get_last()
        self.assertEqual(last_item, basedata_payments[1])

        self.container.undo(False) # False - write to file
        last_item = self.container.get_last()
        self.assertEqual(last_item, basedata_payments[0])

        self.container.undo(False) # False - write to file
        last_item = self.container.get_last()
        self.assertEqual(last_item, None)


    def test_redo(self):
        self.container.clear()
        for i in range(len(basedata_payments)): self.container.append(basedata_payments[i])
        for i in range(len(basedata_payments)): self.container.undo(False)

        last_item = None
        self.assertEqual(last_item, self.container.get_last())

        self.container.redo(False) # False - write to file
        last_item = self.container.get_last()
        self.assertEqual(last_item, basedata_payments[0])

        self.container.redo(False) # False - write to file
        last_item = self.container.get_last()
        self.assertEqual(last_item, basedata_payments[1])

        self.container.redo(False) # False - write to file
        last_item = self.container.get_last()
        self.assertEqual(last_item, basedata_payments[2])
        self.container.redo(False) # False - write to file



class TestContainer_Invalid(unittest.TestCase):
    container = ContainerPAYMENT_REQUEST()

    def test_read_from_file_invalid(self):
        try:
            self.container.read_from_file('invalid_payment.txt')
            self.container.clear()
            self.fail()
        except: 
            return True


    def test_sort_invalid(self):
        self.container.clear()
        try:
            self.container.sort('non-existent key')
            self.fail()
        except:
            return True


    def test_edit_invalid(self):
        self.container.clear()
        self.container.append(basedata_payments[0])
        try:
            self.container.edit('test by non-existent id', '2', 'value') 
            self.fail()
        except: pass
        try:
            self.container.edit('1', 'test by non-existent key', 'value')
            self.fail()
        except:
            return True


    def test_delete_invalid(self):
        self.container.clear()
        self.container.append(basedata_payments[0])
        try:
            self.container.delete('non-existent id')
            self.fail()
        except: 
            return True



class TestContainer_Valid(unittest.TestCase):
    container = ContainerPAYMENT_REQUEST()


    def test_read_from_file_valid(self):
        self.container.clear()
        self.container.read_from_file('valid_payment.txt')
        payment = self.container.get_payment(0)
        self.assertTrue(payment == basedata_payments[0])

      
    def test_delete_valid(self):
        self.container.clear()
        for i in range(len(basedata_payments)): self.container.append(basedata_payments[i])
        for i in range(len(basedata_payments)):
            deleted_element = self.container.delete(basedata_payments[i].get_id())
            self.assertEqual(deleted_element, basedata_payments[i])


    def test_edit_valid(self):
        self.container.clear()
        self.container.append(basedata_payments[2])
        old_attr_id = self.container.get_payment(0).get_id()
        self.container.edit('100', '1', '200')
        self.assertNotEqual(old_attr_id, self.container.get_payment(0).get_id())
            
        self.container.append(basedata_payments[1])
        old_attr_email = self.container.get_payment(1).get_payer_email()
        self.container.edit('10', '4', basedata_valid_attr[0]['payer_email'])
        self.assertEqual(basedata_valid_attr[0]['payer_email'], self.container.get_payment(1).get_payer_email())


    def test_sort_valid(self):
        self.container.clear()
        for i in range(len(basedata_payments)): self.container.append(basedata_payments[i])
        self.container.sort('7')
        self.assertEqual(self.container.get_payment(0), basedata_payments[2])
        self.assertEqual(self.container.get_payment(1), basedata_payments[1])
        self.assertEqual(self.container.get_payment(2), basedata_payments[0])

        self.container.sort('1')
        self.assertEqual(self.container.get_payment(0), basedata_payments[0])
        self.assertEqual(self.container.get_payment(1), basedata_payments[1])
        self.assertEqual(self.container.get_payment(2), basedata_payments[2])



if __name__ == '__main__':
    unittest.main()
