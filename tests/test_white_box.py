# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
from io import StringIO
import unittest
from unittest.mock import patch

from src.white_box import *

class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """
    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxExcersises(unittest.TestCase):

    # 1 
    def test_is_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    def test_is_positive(self):
        self.assertEqual(check_number_status(6), "Positive")

    def test_is_negative(self):
        self.assertEqual(check_number_status(-4), "Negative")

    # 2
    def test_password_is_valid(self):
        self.assertTrue(validate_password("abAB123@$"))

    def test_password_is_not_valid_length(self):
        self.assertFalse(validate_password("aA1@"))

    def test_password_is_not_valid_lowercase(self):
        self.assertFalse(validate_password("ABAB123@$"))

    def test_password_is_not_valid_uppercase(self):
        self.assertFalse(validate_password("abab123@$"))

    def test_password_is_not_valid_digit(self):
        self.assertFalse(validate_password("abABacd@$"))

    def test_password_is_not_valid_special_char(self):
        self.assertFalse(validate_password("abAB123?-"))

    # 3
    def test_no_discount(self):
        self.assertEqual(calculate_total_discount(20), 0)

    def test_yes_discount_10_percent(self):
        self.assertEqual(calculate_total_discount(150), 150*0.1)

    def test_yes_discount_20_percent(self):
        self.assertEqual(calculate_total_discount(550), 550*0.2)


    # 4
    def test_empty_order(self):
        self.assertEqual(calculate_order_total([]), 0)

    def test_no_discount(self):
        items = [{"quantity": 3, "price": 10.0}]
        self.assertEqual(calculate_order_total(items), 30.0)

    def test_small_discount(self):
        items = [{"quantity": 8, "price": 10.0}]
        self.assertEqual(calculate_order_total(items), 8 * 10.0 * 0.95)

    def test_large_discount(self):
        items = [{"quantity": 15, "price": 10.0}]
        self.assertEqual(calculate_order_total(items), 15 * 10.0 * 0.9)

    # 5
    def test_standard_shipping_under_equal_5kg(self):
        items = [{"weight": 2.5}, {"weight": 1.5}]  #4kg
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_between_5_and_10kg(self):
        items = [{"weight": 4}, {"weight": 3}]  #7kg
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_over_10kg(self):
        items = [{"weight": 8}, {"weight": 4}]  #12kg
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_under_equal_5kg(self):
        items = [{"weight": 2.5}, {"weight": 1.5}]  #4kg
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_between_5_and_10kg(self):
        items = [{"weight": 4}, {"weight": 3}]  #7kg
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_over_10kg(self):
        items = [{"weight": 8}, {"weight": 4}]  #12kg
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        items = [{"weight": 1}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "fastest")

    # 6
    def test_valid_login_credentials(self):
        result = validate_login("johndoe", "password123")
        self.assertEqual(result, "Login Successful")

    def test_username_too_short(self):
        result = validate_login("joe", "password123")
        self.assertEqual(result, "Login Failed")

    def test_username_too_long(self):
        result = validate_login("abcdefghijklmnopqrstu", "password123")
        self.assertEqual(result, "Login Failed")

    def test_password_too_short(self):
        result = validate_login("johndoe", "pass123")
        self.assertEqual(result, "Login Failed")

    def test_password_too_long(self):
        result = validate_login("johndoe", "1234567890123456")  
        self.assertEqual(result, "Login Failed")

    # 7
    def test_eligible_age(self):
        self.assertEqual(verify_age(25), "Eligible")

    def test_below_minimum_age(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_above_maximum_age(self):
        self.assertEqual(verify_age(66), "Not Eligible")

    # 8
    def test_category_a(self):
        self.assertEqual(categorize_product(30), "Category A")

    def test_category_b(self):
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c(self):
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d(self):
        self.assertEqual(categorize_product(250), "Category D")

    # 9 
    def test_valid_email(self):
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_email_too_short(self):
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_email_too_long(self):
        too_long_email = "a" * 39 + "@example.com"
        self.assertEqual(validate_email(too_long_email), "Invalid Email")

    def test_email_missing_at_symbol(self):
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_email_missing_dot(self):
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")

    # 10
    def test_valid_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_below_valid_range(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_above_valid_range(self):
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    # 11
    def test_valid_card(self):
        self.assertEqual(validate_credit_card("12345678901234"), "Valid Card")  

    def test_invalid_card_len(self):
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")  

    def test_invalid_card_non_digit(self):
        self.assertEqual(validate_credit_card("12345678a90123"), "Invalid Card")  

    # 12
    def test_valid_date(self):
        self.assertEqual(validate_date(2023, 5, 15), "Valid Date")

    def test_invalid_year_too_early(self):
        self.assertEqual(validate_date(1899, 5, 15), "Invalid Date")

    def test_invalid_year_too_late(self):
        self.assertEqual(validate_date(2101, 5, 15), "Invalid Date")

    def test_invalid_month_too_small(self):
        self.assertEqual(validate_date(2023, 0, 15), "Invalid Date")

    def test_invalid_month_too_large(self):
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")

    def test_invalid_day_too_small(self):
        self.assertEqual(validate_date(2023, 5, 0), "Invalid Date")

    def test_invalid_day_too_large(self):
        self.assertEqual(validate_date(2023, 5, 32), "Invalid Date")

    # 13
    def test_eligible_age(self):
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_invalid_age(self):
        self.assertEqual(check_flight_eligibility(16, False), "Not Eligible to Book")

    # 14
    def test_valid_http_url(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_valid_https_url(self):
        too_long_url = "https://" + "a" * 248  # 8 + 248 = 256 chars
        self.assertEqual(validate_url(too_long_url), "Valid URL")  

    def test_url_no_http(self):
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_http_url_exceeds_max_length(self):
        too_long_url = "http://" + "a" * 249  # 7 + 249 = 256 
        self.assertEqual(validate_url(too_long_url), "Invalid URL")

    # 15
    def test_no_discount(self):
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_small_discount(self):
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")

    def test_large_discount(self):
        self.assertEqual(calculate_quantity_discount(100), "10% Discount")

    # 16
    def test_valid_medium_file(self):
        self.assertEqual(check_file_size(512000), "Valid File Size")  # 500 KB

    def test_invalid_file(self):
        self.assertEqual(check_file_size(2097152), "Invalid File Size")  # 2 MB

    # 17
    def test_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(20000, 800), "Not Eligible")

    def test_standard_loan_medium_income_high_credit(self):
        self.assertEqual(check_loan_eligibility(45000, 750), "Standard Loan")

    def test_secured_loan_medium_income_low_credit(self):
        self.assertEqual(check_loan_eligibility(45000, 650), "Secured Loan")

    def test_premium_loan_high_income_excellent_credit(self):
        self.assertEqual(check_loan_eligibility(80000, 800), "Premium Loan")
   
    def test_standard_loan_high_income_good_credit(self):
        self.assertEqual(check_loan_eligibility(75000, 720), "Standard Loan")

    # 18 
    def test_small_package(self):
        self.assertEqual(calculate_shipping_cost(0.5, 8, 7, 6), 5)
        
    def test_medium_package(self):
        self.assertEqual(calculate_shipping_cost(3, 20, 15, 25), 10)
        
    def test_large_package(self):
        self.assertEqual(calculate_shipping_cost(7, 35, 40, 20), 20)

    # 19
    def test_pass_grade(self):
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_fail_grade_incorrect(self):
        self.assertEqual(grade_quiz(8, 3), "Conditional Pass")

    def test_conditional_pass_grade(self):
        self.assertEqual(grade_quiz(6, 2), "Conditional Pass")

    def test_fail_grade_incorrect(self):
        self.assertEqual(grade_quiz(8, 4), "Fail")

    def test_fail_grade_correct(self):
        self.assertEqual(grade_quiz(4, 1), "Fail")

    # 20
    def test_valid_admin_authentication(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_valid_user_authentication(self):
        self.assertEqual(authenticate_user("regularuser", "securepass123"), "User")

    def test_invalid_user_authentication_username(self):
        self.assertEqual(authenticate_user("usr", "password123"), "Invalid")
    
    def test_invalid_user_authentication_password(self):
        self.assertEqual(authenticate_user("testuser", "pass"), "Invalid")

    # 21
    def test_high_temperature_high_humidity(self):
        self.assertEqual(get_weather_advisory(31, 71), "High Temperature and Humidity. Stay Hydrated.")

    def test_low_temperature(self):
        self.assertEqual(get_weather_advisory(-1, 80), "Low Temperature. Bundle Up!")

    def test_no_advice_temp(self):
        self.assertEqual(get_weather_advisory(25, 80), "No Specific Advisory")

    def test_no_advice_humidity(self):
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")


# 22
class TestWhiteBoxVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_vending_machine_insert_coin_success(self):
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")

    def test_vending_machine_insert_coin_error(self):
        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_select_drink_success(self):
        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Drink Dispensed. Thank you!")

    def test_vending_machine_select_drink_error(self):
        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Invalid operation in current state.")

# 23 
class TestWhiteBoxTrafficLight(unittest.TestCase):
    def setUp(self):
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")
    
    def test_change_state_from_red_to_green(self):
        self.assertEqual(self.traffic_light.state, "Red")
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Green")
    
    def test_change_state_from_green_to_yellow(self):
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Yellow")
    
    def test_change_state_from_yellow_to_red(self):
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Red")
    
    def test_get_current_state(self):
        self.assertEqual(self.traffic_light.get_current_state(), "Red")
        
        self.traffic_light.state = "Green"
        self.assertEqual(self.traffic_light.get_current_state(), "Green")
        
        self.traffic_light.state = "Yellow"
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

# 24
class TestWhiteBoxUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.user_auth = UserAuthentication()
        self.assertEqual(self.user_auth.state, "Logged Out")
    
    def test_login_success(self):
        self.assertEqual(self.user_auth.state, "Logged Out")
        result = self.user_auth.login()
        self.assertEqual(self.user_auth.state, "Logged In")
        self.assertEqual(result, "Login successful")
    
    def test_login_error(self):
        self.user_auth.state = "Logged In"
        result = self.user_auth.login()
        self.assertEqual(self.user_auth.state, "Logged In")
        self.assertEqual(result, "Invalid operation in current state")
    
    def test_logout_success(self):
        self.user_auth.state = "Logged In"
        result = self.user_auth.logout()
        self.assertEqual(self.user_auth.state, "Logged Out")
        self.assertEqual(result, "Logout successful")
    
    def test_logout_error(self):
        self.assertEqual(self.user_auth.state, "Logged Out")
        result = self.user_auth.logout()
        self.assertEqual(self.user_auth.state, "Logged Out")
        self.assertEqual(result, "Invalid operation in current state")
    
# 25
class TestWhiteBoxDocumentEditingSystem(unittest.TestCase):
    def setUp(self):
        self.doc_system = DocumentEditingSystem()
        self.assertEqual(self.doc_system.state, "Editing")
    
    def test_save_document_success(self):
        self.assertEqual(self.doc_system.state, "Editing")
        result = self.doc_system.save_document()
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(result, "Document saved successfully")
    
    def test_save_document_error(self):
        self.doc_system.state = "Saved"
        result = self.doc_system.save_document()
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(result, "Invalid operation in current state")
    
    def test_edit_document_success(self):
        self.doc_system.state = "Saved"
        result = self.doc_system.edit_document()
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(result, "Editing resumed")
    
    def test_edit_document_error(self):
        self.assertEqual(self.doc_system.state, "Editing")
        result = self.doc_system.edit_document()
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(result, "Invalid operation in current state")

# 26
class TestWhiteBoxElevatorSystem(unittest.TestCase):
    def setUp(self):
        self.elevator = ElevatorSystem()
        self.assertEqual(self.elevator.state, "Idle")
    
    def test_move_up_from_idle(self):
        self.assertEqual(self.elevator.state, "Idle")
        result = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(result, "Elevator moving up")
    
    def test_move_up_error_from_moving_up(self):
        self.elevator.state = "Moving Up"
        result = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(result, "Invalid operation in current state")
    
    def test_move_up_error_from_moving_down(self):
        self.elevator.state = "Moving Down"
        result = self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(result, "Invalid operation in current state")
    
    def test_move_down_from_idle(self):
        self.assertEqual(self.elevator.state, "Idle")
        result = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(result, "Elevator moving down")
    
    def test_move_down_error_from_moving_up(self):
        self.elevator.state = "Moving Up"
        result = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(result, "Invalid operation in current state")
    
    def test_move_down_error_from_moving_down(self):
        self.elevator.state = "Moving Down"
        result = self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(result, "Invalid operation in current state")
    
    def test_stop_from_moving_up(self):
        self.elevator.state = "Moving Up"
        result = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(result, "Elevator stopped")
    
    def test_stop_from_moving_down(self):
        self.elevator.state = "Moving Down"
        result = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(result, "Elevator stopped")
    
    def test_stop_error_from_idle(self):
        self.assertEqual(self.elevator.state, "Idle")
        result = self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(result, "Invalid operation in current state")

# 27
class TestWhiteBoxBankAccount(unittest.TestCase):
    def test_bank_account_initialization(self):
        account = BankAccount("12345", 1000)
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.balance, 1000)

    @patch('sys.stdout', new_callable=StringIO) #print goes to StringIO instead of normal output of the system
    def test_view_account(self, mock_stdout): #output automatically goes to the mock_stdout var
        account = BankAccount("ACC001", 500)
        account.view_account()
        self.assertEqual(mock_stdout.getvalue(), "The account ACC001 has a balance of 500\n") #get the "print" from the StringIO object

class TestWhiteBoxBankingSystem(unittest.TestCase):
    def setUp(self):
        self.banking_system = BankingSystem()
        self.assertEqual(self.banking_system.users, {"user123": "pass123"})
        self.assertEqual(self.banking_system.logged_in_users, set())

    @patch('sys.stdout', new_callable=StringIO)
    def test_authenticate_success(self, mock_stdout):
        result = self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(result)
        self.assertIn("user123", self.banking_system.logged_in_users)
        self.assertEqual(mock_stdout.getvalue(), "User user123 authenticated successfully.\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_authenticate_already_logged_in(self, mock_stdout):
        self.banking_system.authenticate("user123", "pass123")
        mock_stdout.truncate(0) #erase current saved output
        mock_stdout.seek(0)
        
        result = self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(result)
        self.assertEqual(mock_stdout.getvalue(), "User already logged in.\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_authenticate_invalid_credentials(self, mock_stdout):
        result = self.banking_system.authenticate("user123", "wrongpass")
        self.assertFalse(result)
        self.assertNotIn("user123", self.banking_system.logged_in_users)
        self.assertEqual(mock_stdout.getvalue(), "Authentication failed.\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_authenticate_invalid_user(self, mock_stdout):
        result = self.banking_system.authenticate("nonexistent", "pass123")
        self.assertFalse(result)
        self.assertNotIn("nonexistent", self.banking_system.logged_in_users)
        self.assertEqual(mock_stdout.getvalue(), "Authentication failed.\n")

# 28
class TestWhiteBoxProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Test Product", 10.99)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.99)

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_product(self, mock_stdout):
        product = Product("Test Product", 10.99)
        result = product.view_product()
        
        expected_output = "The product Test Product has a price of 10.99"
        self.assertEqual(result, expected_output)
        self.assertEqual(mock_stdout.getvalue(), expected_output + "\n")

class TestWhiteBoxShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.product1 = Product("Product 1", 10.99)
        self.product2 = Product("Product 2", 5.99)

        self.assertEqual(len(self.cart.items), 0)

    def test_add_product_new(self):
        self.cart.add_product(self.product1)
        
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    def test_add_product_existing(self):
        self.cart.add_product(self.product1)
        
        self.cart.add_product(self.product1)
        
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_remove_product_partial(self):
        self.cart.add_product(self.product1, 3)
        
        self.cart.remove_product(self.product1)
        
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_remove_product_complete(self):
        self.cart.add_product(self.product1, 3)
        
        self.cart.remove_product(self.product1, 3)
        
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_more_than_exists(self):
        self.cart.add_product(self.product1, 2)
        
        self.cart.remove_product(self.product1, 3)
        
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_nonexistent_product(self):
        self.cart.add_product(self.product1)
        
        self.cart.remove_product(self.product2)
        
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_cart_empty(self, mock_stdout):
        self.cart.view_cart()
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_cart_with_items(self, mock_stdout):
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 1)
        
        self.cart.view_cart()
        
        expected_output = "2 x Product 1 - $21.98\n1 x Product 2 - $5.99\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_checkout_empty_cart(self, mock_stdout):
        self.cart.checkout()
        
        expected_output = "Total: $0\nCheckout completed. Thank you for shopping!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_checkout_with_items(self, mock_stdout):
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 1)
        
        self.cart.checkout()
        
        expected_output = "Total: $27.97\nCheckout completed. Thank you for shopping!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)