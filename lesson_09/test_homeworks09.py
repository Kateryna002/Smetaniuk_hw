import unittest
from homeworks import starts_with_by_the_time, starts_by_title, sentence_in_order_lower_case, reverse, longest_word


class MyTest(unittest.TestCase):
    def test_it_starts_with(self):
        result = starts_with_by_the_time("By the time today")
        self.assertEqual(result, "Рядок починається з 'By the time'")

    def test_it_does_not_start_with(self):
        result = starts_with_by_the_time("It does not start with By the time today")
        self.assertEqual(result, "Рядок не починається з 'By the time'")

    def test_if_not_str(self):
        with self.assertRaises(TypeError):
            starts_by_title(1234)

    def test_index_out_of_range(self):
        result = sentence_in_order_lower_case("ONE TIME. I SLEPT. REALLY GOOD", 18)
        self.assertIsNone(result)

    def test_negative_index(self):
        result = sentence_in_order_lower_case("Hello. World", -1)
        self.assertEqual(result, "world")

    def test_empty_string(self):
        result = sentence_in_order_lower_case("", 0)
        self.assertEqual(result, "")

    def test_regular_string(self):
        result = reverse("hello")
        self.assertEqual(result, "olleh")

    def test_string_with_spaces(self):
        result = reverse("hello world")
        self.assertEqual(result, "dlrow olleh")

    def test_string_with_numbers_and_symbols(self):
        result = reverse("123!abc")
        self.assertEqual(result, "cba!321")

    def test_numbers_as_strings(self):
        words = ["123", "12345", "!@#"]
        result = longest_word(words)
        self.assertEqual(result, "12345")


if __name__ == '__main__':
    unittest.main()
