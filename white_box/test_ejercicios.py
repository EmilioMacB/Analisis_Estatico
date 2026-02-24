# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import *

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


class TestNumberStatus(unittest.TestCase):
    """
    White-box unittest class for check_number_status function.
    """

    def test_check_number_status_positive(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")


class TestValidPassword(unittest.TestCase):
    """
    White-box unittest class for validate_password function.
    """

    def test_length_password_short(self):
        """
        Checks if the password returns False when length is under 8.
        """
        self.assertFalse(validate_password("Short1!"))

    def test_password_missing_uppercase(self):
        """
        Checks if password fails without an uppercase letter.
        """
        self.assertFalse(validate_password("lowercase1!"))

    def test_password_missing_lowercase(self):
        """
        Checks if password fails without a lowercase letter.
        """
        self.assertFalse(validate_password("UPPERCASE1!"))

    def test_password_missing_digit(self):
        """
        Checks if password fails without a digit.
        """
        self.assertFalse(validate_password("NoDigitsHere!"))

    def test_password_missing_special_character(self):
        """
        Checks if password fails without a special character.
        """
        self.assertFalse(validate_password("NoSpecialChar1"))

    def test_password_valid(self):
        """
        Checks if a fully compliant password returns True.
        """
        self.assertTrue(validate_password("ValidPassw0rd!"))
        

class TestCalculateTotalDiscount(unittest.TestCase):
    """
    White-box unittest class for calculate_total_discount function.
    """

    def test_discount_below_100(self):
        """
        Checks discount for amounts strictly under 100.
        """
        self.assertEqual(calculate_total_discount(99.99), 0)

    def test_discount_between_100_and_500(self):
        """
        Checks 10% discount for amounts inclusive between 100 and 500.
        Testing lower boundary.
        """
        self.assertEqual(calculate_total_discount(100), 10.0)
        self.assertEqual(calculate_total_discount(500), 50.0)

    def test_discount_above_500(self):
        """
        Checks 20% discount for amounts strictly over 500.
        """
        self.assertAlmostEqual(calculate_total_discount(500.01), 100.002)


class TestCalculateOrderTotal(unittest.TestCase):
    """
    White-box unittest class for calculate_order_total function.
    """

    def test_order_no_discount_quantity(self):
        """
        Checks total price for items with quantity 1 to 5 (No discount).
        """
        items = [{"quantity": 5, "price": 10}]
        self.assertEqual(calculate_order_total(items), 50)

    def test_order_five_percent_discount_quantity(self):
        """
        Checks total price for items with quantity 6 to 10 (5% discount).
        """
        items = [{"quantity": 6, "price": 10}]
        # 6 * 10 = 60. 60 * 0.95 = 57.0
        self.assertAlmostEqual(calculate_order_total(items), 57.0)

    def test_order_ten_percent_discount_quantity(self):
        """
        Checks total price for items with quantity greater than 10 (10% discount).
        """
        items = [{"quantity": 11, "price": 10}]
        # 11 * 10 = 110. 110 * 0.9 = 99.0
        self.assertAlmostEqual(calculate_order_total(items), 99.0)


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    White-box unittest class for calculate_items_shipping_cost function.
    """

    def test_shipping_standard_weight_under_5(self):
        items = [{"weight": 2}, {"weight": 3}] # Total: 5
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_shipping_standard_weight_between_5_and_10(self):
        items = [{"weight": 6}] # Total: 6
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_shipping_standard_weight_over_10(self):
        items = [{"weight": 11}] # Total: 11
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_shipping_express_weight_under_5(self):
        items = [{"weight": 4.9}] # Total: 4.9
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_shipping_express_weight_between_5_and_10(self):
        items = [{"weight": 10}] # Total: 10
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_shipping_express_weight_over_10(self):
        items = [{"weight": 10.1}] # Total: 10.1
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_shipping_invalid_method(self):
        items = [{"weight": 5}]
        # Usamos assertRaises para comprobar que la función lanza una excepción
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "holaaa")


class TestValidateLogin(unittest.TestCase):
    """
    White-box unittest class for validate_login function.
    """

    def test_login_successful_boundary(self):
        # Username 5 chars, password 8 chars
        self.assertEqual(validate_login("admin", "pass1234"), "Login Successful")

    def test_login_failed_username_too_short(self):
        # Username 4 chars
        self.assertEqual(validate_login("user", "password123"), "Login Failed")

    def test_login_failed_password_too_short(self):
        # Username 5 chars, password 7 chars
        self.assertEqual(validate_login("admin", "pass123"), "Login Failed")

    def test_login_failed_username_too_long(self):
        # Username 21 chars
        self.assertEqual(validate_login("thisusernameiswaytoolong", "password123"), "Login Failed")


class TestVerifyAge(unittest.TestCase):
    """
    White-box unittest class for verify_age function.
    """

    def test_age_eligible_lower_boundary(self):
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_eligible_upper_boundary(self):
        self.assertEqual(verify_age(65), "Eligible")

    def test_age_not_eligible_too_young(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_not_eligible_too_old(self):
        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """
    White-box unittest class for categorize_product function.
    """

    def test_category_a(self):
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_b(self):
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_c(self):
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_d_above_200(self):
        self.assertEqual(categorize_product(201), "Category D")

    def test_category_d_below_10(self):
        self.assertEqual(categorize_product(9), "Category D")


class TestValidateEmail(unittest.TestCase):
    """
    White-box unittest class for validate_email function.
    """

    def test_email_valid(self):
        self.assertEqual(validate_email("@.@.@"), "Valid Email") # 5 chars, contains @ and .

    def test_email_too_short(self):
        self.assertEqual(validate_email("a@b."), "Invalid Email") # 4 chars

    def test_email_too_long(self):
        long_email = "a" * 50 + "@hola.com" # 59 chars
        self.assertEqual(validate_email(long_email), "Invalid Email")

    def test_email_missing_at_symbol(self):
        self.assertEqual(validate_email("email.hola.com"), "Invalid Email")

    def test_email_missing_dot(self):
        self.assertEqual(validate_email("email@holacom"), "Invalid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    White-box unittest class for celsius_to_fahrenheit function.
    """

    def test_celsius_within_boundaries(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(-100), -148)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_below_lower_boundary(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_above_upper_boundary(self):
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    
class TestValidateCreditCard(unittest.TestCase):
    """
    White-box unittest class for validate_credit_card function.
    """

    def test_card_valid_length(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card") # 13 chars
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card") # 16 chars

    def test_card_too_short(self):
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card") # 12 chars

    def test_card_too_long(self):
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card") # 17 chars

    def test_card_contains_non_digits(self):
        self.assertEqual(validate_credit_card("123456789012a"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """
    White-box unittest class for validate_date function.
    """

    def test_date_valid(self):
        self.assertEqual(validate_date(2023, 10, 15), "Valid Date")

    def test_date_invalid_year(self):
        self.assertEqual(validate_date(1899, 10, 15), "Invalid Date")
        self.assertEqual(validate_date(2101, 10, 15), "Invalid Date")

    def test_date_invalid_month(self):
        self.assertEqual(validate_date(2023, 0, 15), "Invalid Date")
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")

    def test_date_invalid_day(self):
        self.assertEqual(validate_date(2023, 10, 0), "Invalid Date")
        self.assertEqual(validate_date(2023, 10, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """
    White-box unittest class for check_flight_eligibility function.
    """

    def test_eligible_by_age(self):
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_eligible_by_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_not_eligible(self):
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


class TestValidateUrl(unittest.TestCase):
    """
    White-box unittest class for validate_url function.
    """

    def test_url_valid_http(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_url_valid_https(self):
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_url_invalid_prefix(self):
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_url_http_too_long(self):
        long_url = "http://" + "a" * 249 # 256 chars
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_url_https_too_long(self):
        # Aqui parece que hay un error con la prueba del archivo de class_excercises por el tema de precedencia de operadores. esto me lo dio chat
        # por lo tanto esta prueba da error
        long_url = "https://" + "a" * 249 # 257 chars
        self.assertEqual(validate_url(long_url), "Invalid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    White-box unittest class for calculate_quantity_discount function.
    """

    def test_no_discount(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_five_percent_discount(self):
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_ten_percent_discount(self):
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_invalid_quantity_zero_or_negative(self):
        # Esta prueba falla porque quantity = 0 da 10% Discount en lugar de "Invalid Quantity" y quantity negativo también da 10% Discount
        # pero en realidad no le puedes poner descuento a una cantidad negativa o a 0, por lo tanto esta prueba es válida para detectar un error en la función.
        self.assertEqual(calculate_quantity_discount(0), "Invalid Quantity")
        self.assertEqual(calculate_quantity_discount(-5), "Invalid Quantity")


class TestCheckFileSize(unittest.TestCase):
    """
    White-box unittest class for check_file_size function.
    """

    def test_valid_size_lower_bound(self):
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_valid_size_upper_bound(self):
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_invalid_size_negative(self):
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_invalid_size_too_large(self):
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    """
    White-box unittest class for check_loan_eligibility function.
    """

    def test_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_medium_income_good_credit(self):
        self.assertEqual(check_loan_eligibility(45000, 701), "Standard Loan")

    def test_medium_income_bad_credit(self):
        self.assertEqual(check_loan_eligibility(45000, 700), "Secured Loan")

    def test_high_income_excellent_credit(self):
        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")

    def test_high_income_normal_credit(self):
        self.assertEqual(check_loan_eligibility(60001, 750), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """
    White-box unittest class for calculate_shipping_cost function.
    """

    def test_small_package(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package(self):
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_large_package_heavy(self):
        # Falla las primeras condiciones por el peso > 5
        self.assertEqual(calculate_shipping_cost(6, 15, 15, 15), 20)
        
    def test_large_package_oversized(self):
        # Falla las segundas condiciones por el largo > 30
        self.assertEqual(calculate_shipping_cost(2, 31, 15, 15), 20)


class TestGradeQuiz(unittest.TestCase):
    """
    White-box unittest class for grade_quiz function.
    """

    def test_pass(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail_too_few_correct(self):
        self.assertEqual(grade_quiz(4, 2), "Fail")

    def test_fail_too_many_incorrect(self):
        self.assertEqual(grade_quiz(6, 4), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    """
    White-box unittest class for authenticate_user function.
    """

    def test_admin_auth(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user_auth(self):
        self.assertEqual(authenticate_user("user1", "password"), "User")

    def test_invalid_auth_short_username(self):
        self.assertEqual(authenticate_user("user", "password"), "Invalid")

    def test_invalid_auth_short_password(self):
        self.assertEqual(authenticate_user("user1", "pass123"), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    White-box unittest class for get_weather_advisory function.
    """

    def test_high_temp_and_humidity(self):
        self.assertEqual(get_weather_advisory(31, 71), "High Temperature and Humidity. Stay Hydrated.")

    def test_low_temperature(self):
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_no_advisory_normal_conditions(self):
        self.assertEqual(get_weather_advisory(25, 50), "No Specific Advisory")

    def test_no_advisory_high_temp_low_humidity(self):
        self.assertEqual(get_weather_advisory(31, 70), "No Specific Advisory")


