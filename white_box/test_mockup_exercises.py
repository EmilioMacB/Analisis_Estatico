# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest
from unittest.mock import mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestPerformActionBasedOnTime(unittest.TestCase):
    """Unit tests for the perform_action_based_on_time function."""

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_a(self, mock_time):
        """Prueba que devuelve 'Action A' cuando el tiempo < 10."""
        mock_time.return_value = 5.0
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_b(self, mock_time):
        """Prueba que devuelve 'Action B' cuando el tiempo >= 10."""
        mock_time.return_value = 15.0
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()


class TestFetchDataFromAPI(unittest.TestCase):
    """Unit tests for the fetch_data_from_api function."""

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api(self, mock_get):
        """Test that fetch_data_from_api returns the expected data."""
        mock_response = mock_get.return_value
        expected_json = {"id": 1, "name": "Test Item"}
        mock_response.json.return_value = expected_json

        url = "https://api.ejemplo.com/data"
        result = fetch_data_from_api(url)

        self.assertEqual(result, expected_json)
        mock_get.assert_called_once_with(url, timeout=10)


class TestExecuteCommand(unittest.TestCase):
    """Unit tests for the execute command function."""

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command(self, mock_run):
        """Test that execute_command returns the expected output."""
        mock_response = mock_run.return_value
        expected_output = "Comando ejecutado con éxito"
        mock_response.stdout = expected_output

        command = ["echo", "Hola Mundo"]
        result = execute_command(command)

        self.assertEqual(result, expected_output)
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )


class TestReadDataFromFile(unittest.TestCase):
    """Unit tests for the read_data_from_file function."""

    @patch("builtins.open", new_callable=mock_open, read_data="Contenido de prueba")
    def test_read_data_success(self, mock_file):
        """Prueba la lectura exitosa de un archivo."""
        result = read_data_from_file("test.txt")
        self.assertEqual(result, "Contenido de prueba")
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_data_file_not_found(
        self, _mock_file
    ):  # Se agregó '_' para evitar W0613
        """Prueba el manejo de error cuando el archivo no existe."""
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("inexistente.txt")


if __name__ == "__main__":
    unittest.main()
