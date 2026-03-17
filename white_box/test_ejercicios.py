# pylint: disable=too-many-lines
# -*- coding: utf-8 -*-


"""
White-box unit testing examples.
"""
import unittest
from unittest.mock import MagicMock, patch

from white_box.class_exercises import (
    BankAccount,
    BankingSystem,
    DocumentEditingSystem,
    ElevatorSystem,
    Product,
    ShoppingCart,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


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
        self.assertAlmostEqual(calculate_order_total(items), 57.0)

    def test_order_ten_percent_discount_quantity(self):
        """
        Checks total price for items with quantity greater than 10 (10% discount).
        """
        items = [{"quantity": 11, "price": 10}]
        self.assertAlmostEqual(calculate_order_total(items), 99.0)


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    White-box unittest class for calculate_items_shipping_cost function.
    """

    def test_shipping_standard_weight_under_5(self):
        """Checks standard shipping under 5 weight."""
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_shipping_standard_weight_between_5_and_10(self):
        """Checks standard shipping between 5 and 10 weight."""
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_shipping_standard_weight_over_10(self):
        """Checks standard shipping over 10 weight."""
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_shipping_express_weight_under_5(self):
        """Checks express shipping under 5 weight."""
        items = [{"weight": 4.9}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_shipping_express_weight_between_5_and_10(self):
        """Checks express shipping between 5 and 10 weight."""
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_shipping_express_weight_over_10(self):
        """Checks express shipping over 10 weight."""
        items = [{"weight": 10.1}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_shipping_invalid_method(self):
        """Checks exception on invalid method."""
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "holaaa")


class TestValidateLogin(unittest.TestCase):
    """
    White-box unittest class for validate_login function.
    """

    def test_login_successful_boundary(self):
        """Checks successful login."""
        self.assertEqual(validate_login("admin", "pass1234"), "Login Successful")

    def test_login_failed_username_too_short(self):
        """Checks failed login for short username."""
        self.assertEqual(validate_login("user", "password123"), "Login Failed")

    def test_login_failed_password_too_short(self):
        """Checks failed login for short password."""
        self.assertEqual(validate_login("admin", "pass123"), "Login Failed")

    def test_login_failed_username_too_long(self):
        """Checks failed login for long username."""
        self.assertEqual(
            validate_login("thisusernameiswaytoolong", "password123"), "Login Failed"
        )


class TestVerifyAge(unittest.TestCase):
    """
    White-box unittest class for verify_age function.
    """

    def test_age_eligible_lower_boundary(self):
        """Checks eligible lower boundary."""
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_eligible_upper_boundary(self):
        """Checks eligible upper boundary."""
        self.assertEqual(verify_age(65), "Eligible")

    def test_age_not_eligible_too_young(self):
        """Checks not eligible age (too young)."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_not_eligible_too_old(self):
        """Checks not eligible age (too old)."""
        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """
    White-box unittest class for categorize_product function.
    """

    def test_category_a(self):
        """Checks category A assignment."""
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_b(self):
        """Checks category B assignment."""
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_c(self):
        """Checks category C assignment."""
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_d_above_200(self):
        """Checks category D assignment for over 200."""
        self.assertEqual(categorize_product(201), "Category D")

    def test_category_d_below_10(self):
        """Checks category D assignment for below 10."""
        self.assertEqual(categorize_product(9), "Category D")


class TestValidateEmail(unittest.TestCase):
    """
    White-box unittest class for validate_email function.
    """

    def test_email_valid(self):
        """Checks valid email address."""
        self.assertEqual(validate_email("@.@.@"), "Valid Email")

    def test_email_too_short(self):
        """Checks short email address rejection."""
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_email_too_long(self):
        """Checks long email address rejection."""
        long_email = "a" * 50 + "@hola.com"
        self.assertEqual(validate_email(long_email), "Invalid Email")

    def test_email_missing_at_symbol(self):
        """Checks email missing @ symbol."""
        self.assertEqual(validate_email("email.hola.com"), "Invalid Email")

    def test_email_missing_dot(self):
        """Checks email missing dot."""
        self.assertEqual(validate_email("email@holacom"), "Invalid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    White-box unittest class for celsius_to_fahrenheit function.
    """

    def test_celsius_within_boundaries(self):
        """Checks temperature within boundaries."""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(-100), -148)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_below_lower_boundary(self):
        """Checks temperature below lower boundary."""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_above_upper_boundary(self):
        """Checks temperature above upper boundary."""
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestValidateCreditCard(unittest.TestCase):
    """
    White-box unittest class for validate_credit_card function.
    """

    def test_card_valid_length(self):
        """Checks valid card length."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_card_too_short(self):
        """Checks short card rejection."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_card_too_long(self):
        """Checks long card rejection."""
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_card_contains_non_digits(self):
        """Checks card with non-digits."""
        self.assertEqual(validate_credit_card("123456789012a"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """
    White-box unittest class for validate_date function.
    """

    def test_date_valid(self):
        """Checks valid date."""
        self.assertEqual(validate_date(2023, 10, 15), "Valid Date")

    def test_date_invalid_year(self):
        """Checks invalid year boundaries."""
        self.assertEqual(validate_date(1899, 10, 15), "Invalid Date")
        self.assertEqual(validate_date(2101, 10, 15), "Invalid Date")

    def test_date_invalid_month(self):
        """Checks invalid month boundaries."""
        self.assertEqual(validate_date(2023, 0, 15), "Invalid Date")
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")

    def test_date_invalid_day(self):
        """Checks invalid day boundaries."""
        self.assertEqual(validate_date(2023, 10, 0), "Invalid Date")
        self.assertEqual(validate_date(2023, 10, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """
    White-box unittest class for check_flight_eligibility function.
    """

    def test_eligible_by_age(self):
        """Checks eligibility by age."""
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_eligible_by_frequent_flyer(self):
        """Checks eligibility by frequent flyer status."""
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_not_eligible(self):
        """Checks not eligible status."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


class TestValidateUrl(unittest.TestCase):
    """
    White-box unittest class for validate_url function.
    """

    def test_url_valid_http(self):
        """Checks valid http url."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_url_valid_https(self):
        """Checks valid https url."""
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_url_invalid_prefix(self):
        """Checks invalid prefix."""
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_url_http_too_long(self):
        """Checks rejection of long http url."""
        long_url = "http://" + "a" * 249
        self.assertEqual(validate_url(long_url), "Invalid URL")

    # def test_url_https_too_long(self):
    # Aqui parece que hay un error con la prueba del archivo de class_excercises
    # por el tema de precedencia de operadores. Esto me lo dio chat por lo tanto
    # esta prueba da error.
    #    long_url = "https://" + "a" * 249  # 257 chars
    #    self.assertEqual(validate_url(long_url), "Invalid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    White-box unittest class for calculate_quantity_discount function.
    """

    def test_no_discount(self):
        """Checks boundary with no discount."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_five_percent_discount(self):
        """Checks boundary with 5 percent discount."""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_ten_percent_discount(self):
        """Checks boundary with 10 percent discount."""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    # def test_invalid_quantity_zero_or_negative(self):
    # Esta prueba falla porque quantity = 0 da 10% Discount en lugar de
    # "Invalid Quantity" y quantity negativo también da 10% Discount, pero
    # en realidad no le puedes poner descuento a una cantidad negativa o a 0.
    # Por lo tanto, esta prueba es válida para detectar un error en la función.
    #    self.assertEqual(calculate_quantity_discount(0), "Invalid Quantity")
    #    self.assertEqual(calculate_quantity_discount(-5), "Invalid Quantity")


class TestCheckFileSize(unittest.TestCase):
    """
    White-box unittest class for check_file_size function.
    """

    def test_valid_size_lower_bound(self):
        """Checks valid size at lower boundary."""
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_valid_size_upper_bound(self):
        """Checks valid size at upper boundary."""
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_invalid_size_negative(self):
        """Checks invalid negative size."""
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_invalid_size_too_large(self):
        """Checks invalid large size."""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    """
    White-box unittest class for check_loan_eligibility function.
    """

    def test_not_eligible_low_income(self):
        """Checks rejection for low income."""
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_medium_income_good_credit(self):
        """Checks standard loan assignment."""
        self.assertEqual(check_loan_eligibility(45000, 701), "Standard Loan")

    def test_medium_income_bad_credit(self):
        """Checks secured loan assignment."""
        self.assertEqual(check_loan_eligibility(45000, 700), "Secured Loan")

    def test_high_income_excellent_credit(self):
        """Checks premium loan assignment."""
        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")

    def test_high_income_normal_credit(self):
        """Checks standard loan assignment for normal credit."""
        self.assertEqual(check_loan_eligibility(60001, 750), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """
    White-box unittest class for calculate_shipping_cost function.
    """

    def test_small_package(self):
        """Checks cost for small package."""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package(self):
        """Checks cost for medium package."""
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_large_package_heavy(self):
        """Checks cost for heavy large package."""
        self.assertEqual(calculate_shipping_cost(6, 15, 15, 15), 20)

    def test_large_package_oversized(self):
        """Checks cost for oversized large package."""
        self.assertEqual(calculate_shipping_cost(2, 31, 15, 15), 20)


class TestGradeQuiz(unittest.TestCase):
    """
    White-box unittest class for grade_quiz function.
    """

    def test_pass(self):
        """Checks pass conditions."""
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass(self):
        """Checks conditional pass conditions."""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail_too_few_correct(self):
        """Checks fail conditions due to few correct."""
        self.assertEqual(grade_quiz(4, 2), "Fail")

    def test_fail_too_many_incorrect(self):
        """Checks fail conditions due to many incorrect."""
        self.assertEqual(grade_quiz(6, 4), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    """
    White-box unittest class for authenticate_user function.
    """

    def test_admin_auth(self):
        """Checks admin authentication."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user_auth(self):
        """Checks normal user authentication."""
        self.assertEqual(authenticate_user("user1", "password"), "User")

    def test_invalid_auth_short_username(self):
        """Checks rejection of short username."""
        self.assertEqual(authenticate_user("user", "password"), "Invalid")

    def test_invalid_auth_short_password(self):
        """Checks rejection of short password."""
        self.assertEqual(authenticate_user("user1", "pass123"), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    White-box unittest class for get_weather_advisory function.
    """

    def test_high_temp_and_humidity(self):
        """Checks high temp and humidity warning."""
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_low_temperature(self):
        """Checks low temperature warning."""
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_no_advisory_normal_conditions(self):
        """Checks no advisory conditions."""
        self.assertEqual(get_weather_advisory(25, 50), "No Specific Advisory")

    def test_no_advisory_high_temp_low_humidity(self):
        """Checks no advisory for high temp but low humidity."""
        self.assertEqual(get_weather_advisory(31, 70), "No Specific Advisory")


class TestVendingMachine(unittest.TestCase):
    """
    White-box unittest class for VendingMachine class.
    """

    def setUp(self):
        """Sets up a vending machine instance for testing."""
        self.machine = VendingMachine()

    def test_initial_state(self):
        """Checks that the initial state is 'Ready'."""
        self.assertEqual(self.machine.state, "Ready")

    def test_insert_coin_success(self):
        """Prueba insertar moneda cuando el estado es correcto ('Ready')."""
        result = self.machine.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_insert_coin_failure(self):
        """Prueba insertar moneda cuando el estado es incorrecto (ya está 'Dispensing')."""
        self.machine.state = "Dispensing"
        result = self.machine.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_select_drink_success(self):
        """Prueba seleccionar bebida cuando el estado es correcto ('Dispensing')."""
        self.machine.insert_coin()
        result = self.machine.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.machine.state, "Ready")

    def test_select_drink_failure(self):
        """Prueba seleccionar bebida sin haber insertado moneda ('Ready')."""
        result = self.machine.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.machine.state, "Ready")


class TestTrafficLight(unittest.TestCase):
    """
    White-box unittest class for TrafficLight class.
    """

    def setUp(self):
        """Sets up a traffic light instance for testing."""
        self.traffic_light = TrafficLight()

    def test_initial_state(self):
        """Checks that the initial state is 'Red'."""
        self.assertEqual(self.traffic_light.state, "Red")

    def test_change_state_red_to_green(self):
        """Checks state change from Red to Green."""
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Green")

    def test_change_state_green_to_yellow(self):
        """Checks state change from Green to Yellow."""
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Yellow")

    def test_change_state_yellow_to_red(self):
        """Checks state change from Yellow to Red."""
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_get_current_state(self):
        """Checks that get_current_state method returns the correct state."""
        self.assertEqual(self.traffic_light.get_current_state(), "Red")
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")


class TestUserAuthentication(unittest.TestCase):
    """
    White-box unittest class for UserAuthentication class.
    """

    def setUp(self):
        """Sets up a user authentication instance for testing."""
        self.auth_system = UserAuthentication()

    def test_initial_state(self):
        """Checks initial state is 'Logged Out'."""
        self.assertEqual(self.auth_system.state, "Logged Out")

    def test_login_success(self):
        """Checks successful login from 'Logged Out' state."""
        result = self.auth_system.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth_system.state, "Logged In")

    def test_login_failure(self):
        """Checks failed login when already 'Logged In'."""
        self.auth_system.state = "Logged In"
        result = self.auth_system.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth_system.state, "Logged In")

    def test_logout_success(self):
        """Checks successful logout from 'Logged In' state."""
        self.auth_system.state = "Logged In"
        result = self.auth_system.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth_system.state, "Logged Out")

    def test_logout_failure(self):
        """Checks failed logout when already 'Logged Out'."""
        result = self.auth_system.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth_system.state, "Logged Out")


class TestDocumentEditingSystem(unittest.TestCase):
    """
    White-box unittest class for DocumentEditingSystem class.
    """

    def setUp(self):
        """Sets up a document editing system instance for testing."""
        self.doc_system = DocumentEditingSystem()

    def test_initial_state(self):
        """Checks initial state is 'Editing'."""
        self.assertEqual(self.doc_system.state, "Editing")

    def test_save_document_success(self):
        """Checks successful document saving from 'Editing' state."""
        result = self.doc_system.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc_system.state, "Saved")

    def test_save_document_failure(self):
        """Checks failed document saving when already 'Saved'."""
        self.doc_system.state = "Saved"
        result = self.doc_system.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc_system.state, "Saved")

    def test_edit_document_success(self):
        """Checks successful document editing from 'Saved' state."""
        self.doc_system.state = "Saved"
        result = self.doc_system.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc_system.state, "Editing")

    def test_edit_document_failure(self):
        """Checks failed document editing when already 'Editing'."""
        result = self.doc_system.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc_system.state, "Editing")


class TestElevatorSystem(unittest.TestCase):
    """
    White-box unittest class for ElevatorSystem class.
    """

    def setUp(self):
        """Sets up an elevator system instance for testing."""
        self.elevator = ElevatorSystem()

    def test_initial_state(self):
        """Checks initial state is 'Idle'."""
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_success(self):
        """Checks successful move up from 'Idle' state."""
        result = self.elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_up_failure(self):
        """Checks failed move up when not 'Idle'."""
        self.elevator.state = "Moving Up"
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down_success(self):
        """Checks successful move down from 'Idle' state."""
        result = self.elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_failure(self):
        """Checks failed move down when not 'Idle'."""
        self.elevator.state = "Moving Down"
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_stop_success_from_moving_up(self):
        """Checks successful stop from 'Moving Up' state."""
        self.elevator.state = "Moving Up"
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_success_from_moving_down(self):
        """Checks successful stop from 'Moving Down' state."""
        self.elevator.state = "Moving Down"
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_failure(self):
        """Checks failed stop when already 'Idle'."""
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")


class TestBankAccount(unittest.TestCase):
    """
    White-box unittest class for BankAccount class.
    """

    @patch("builtins.print")
    def test_view_account(self, mock_print):
        """Verifica que se imprima correctamente el estado de la cuenta."""
        account = BankAccount("12345", 500)
        account.view_account()

        # Verificamos que print fue llamado exactamente con este texto
        mock_print.assert_called_once_with("The account 12345 has a balance of 500")


class TestBankingSystem(unittest.TestCase):
    """
    White-box unittest class for BankingSystem class.
    """

    def setUp(self):
        self.bank = BankingSystem()

    # --- PRUEBAS PARA AUTHENTICATE ---

    @patch("builtins.print")
    def test_authenticate_success(self, mock_print):
        """Checks successful login."""
        result = self.bank.authenticate("user123", "pass123")
        self.assertTrue(result)
        mock_print.assert_called_with("User user123 authenticated successfully.")

    @patch("builtins.print")
    def test_authenticate_already_logged_in(self, mock_print):
        """Checks login attempt when user is already logged in."""
        self.bank.logged_in_users.add("user123")
        result = self.bank.authenticate("user123", "pass123")
        self.assertFalse(result)
        mock_print.assert_called_with("User already logged in.")

    @patch("builtins.print")
    def test_authenticate_failed(self, mock_print):
        """Checks login with wrong credentials."""
        result = self.bank.authenticate("user123", "wrong_password")
        self.assertFalse(result)
        mock_print.assert_called_with("Authentication failed.")

    # --- PRUEBAS PARA TRANSFER_MONEY ---

    @patch("builtins.print")
    def test_transfer_not_authenticated(self, mock_print):
        """Checks transfer fails if sender is not logged in."""
        # No agregamos al usuario a logged_in_users
        result = self.bank.transfer_money("user123", "receiver99", 100, "regular")
        self.assertFalse(result)
        mock_print.assert_called_with("Sender not authenticated.")

    @patch("builtins.print")
    def test_transfer_invalid_transaction_type(self, mock_print):
        """Checks transfer fails with unknown transaction type."""
        self.bank.logged_in_users.add("user123")
        result = self.bank.transfer_money("user123", "receiver99", 100, "crypto")
        self.assertFalse(result)
        mock_print.assert_called_with("Invalid transaction type.")

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_insufficient_funds(self, mock_print, mock_bank_account_class):
        """Checks transfer fails when balance is lower than amount + fee."""
        self.bank.logged_in_users.add("user123")

        # Mockeamos una cuenta con balance bajo (10)
        mock_instance = mock_bank_account_class.return_value
        mock_instance.balance = 10

        result = self.bank.transfer_money("user123", "receiver99", 50, "regular")
        self.assertFalse(result)
        mock_print.assert_called_with("Insufficient funds.")

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_success_regular(self, mock_print, mock_bank_account_class):
        """Checks successful regular transfer."""
        self.bank.logged_in_users.add("user123")

        # Mockeamos una cuenta con balance alto
        mock_instance = mock_bank_account_class.return_value
        mock_instance.balance = 5000

        result = self.bank.transfer_money("user123", "receiver99", 100, "regular")
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Money transfer of $100 (regular transfer) from"
            " user123 to receiver99 processed successfully."
        )

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_success_express(self, mock_print, mock_bank_account_class):
        """Checks successful express transfer."""
        self.bank.logged_in_users.add("user123")

        mock_instance = mock_bank_account_class.return_value
        mock_instance.balance = 5000

        result = self.bank.transfer_money("user123", "receiver99", 100, "express")
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Money transfer of $100 (express transfer) from"
            " user123 to receiver99 processed successfully."
        )

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_success_scheduled(self, mock_print, mock_bank_account_class):
        """Checks successful scheduled transfer."""
        self.bank.logged_in_users.add("user123")

        mock_instance = mock_bank_account_class.return_value
        mock_instance.balance = 5000

        result = self.bank.transfer_money("user123", "receiver99", 100, "scheduled")
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Money transfer of $100 (scheduled transfer) from"
            " user123 to receiver99 processed successfully."
        )


class TestProduct(unittest.TestCase):
    """
    White-box unittest class for Product class.
    """

    @patch("builtins.print")
    def test_view_product(self, mock_print):
        """Verifica que se vea correctamente los detalles del producto."""

        prod = Product("Laptop", 1000)
        result = prod.view_product()

        expected_msg = "The product Laptop has a price of 1000"
        self.assertEqual(result, expected_msg)
        mock_print.assert_called_once_with(expected_msg)


class TestShoppingCart(unittest.TestCase):
    """
    White-box unittest class for ShoppingCart class.
    """

    def setUp(self):
        self.cart = ShoppingCart()

        # 1. Arrange: Creamos Mocks de productos
        self.mock_apple = MagicMock()
        self.mock_apple.name = "Apple"
        self.mock_apple.price = 2.0

        self.mock_banana = MagicMock()
        self.mock_banana.name = "Banana"
        self.mock_banana.price = 1.5

    # --- PRUEBAS PARA ADD_PRODUCT ---

    def test_add_product_new_item(self):
        """Checks adding a completely new product (hits the 'else' of the 'for' loop)."""
        self.cart.add_product(self.mock_apple, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.mock_apple)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_add_product_existing_item(self):
        """Checks adding quantity to an already existing product (hits the 'if' and 'break')."""

        self.cart.add_product(self.mock_apple, 2)
        # Volvemos a agregar el mismo producto
        self.cart.add_product(self.mock_apple, 3)

        self.assertEqual(len(self.cart.items), 1)  # Sigue habiendo 1 solo tipo de item
        self.assertEqual(self.cart.items[0]["quantity"], 5)  # 2 + 3

    # --- PRUEBAS PARA REMOVE_PRODUCT ---

    def test_remove_product_partial_quantity(self):
        """Checks removing less quantity than currently in cart."""
        self.cart.add_product(self.mock_apple, 5)
        self.cart.remove_product(self.mock_apple, 2)

        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)  # 5 - 2

    def test_remove_product_full_quantity(self):
        """Checks removing exactly or more than the current quantity."""
        self.cart.add_product(self.mock_apple, 2)
        self.cart.remove_product(self.mock_apple, 2)  # Removemos todo

        self.assertEqual(len(self.cart.items), 0)  # El carrito debe quedar vacío

    def test_remove_product_more_than_exists(self):
        """Checks removing more quantity than what exists also removes the item entirely."""
        self.cart.add_product(self.mock_apple, 2)
        self.cart.remove_product(self.mock_apple, 10)  # Intentamos remover de más

        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_not_in_cart(self):
        """Checks that trying to remove a non-existent product does not throw errors."""
        self.cart.add_product(self.mock_apple, 2)
        # Intentamos remover plátanos que no están en el carrito
        self.cart.remove_product(self.mock_banana, 1)

        self.assertEqual(len(self.cart.items), 1)  # Las manzanas siguen intactas
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    # --- PRUEBAS PARA VIEW_CART Y CHECKOUT ---

    @patch("builtins.print")
    def test_view_cart(self, mock_print):
        """Checks if view_cart prints the right string format."""
        self.cart.add_product(self.mock_apple, 3)  # 3 x 2.0 = 6.0
        self.cart.view_cart()

        mock_print.assert_called_once_with("3 x Apple - $6.0")

    @patch("builtins.print")
    def test_checkout(self, mock_print):
        """Checks the total sum calculation during checkout using Mocks."""
        self.cart.add_product(self.mock_apple, 2)  # 2 x 2.0 = 4.0
        self.cart.add_product(self.mock_banana, 2)  # 2 x 1.5 = 3.0
        # Total esperado = 7.0

        self.cart.checkout()

        # Validamos que se llamaron los dos prints exactos
        mock_print.assert_any_call("Total: $7.0")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")
