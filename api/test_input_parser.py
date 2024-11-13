from api.input_parser import InputParser


class TestInputParser:
    def test_parse_input_date(self):
        parser = InputParser()
        result = parser.parse_input('2024-11-13')
        assert result == "date detected in input."
    
    def test_parse_input_phone(self):
        parser = InputParser()
        result = parser.parse_input('+1-800-555-5555')
        assert result == "phone detected in input."
    
    def test_parse_input_invalid(self):
        parser = InputParser()
        result = parser.parse_input('invalid-input')
        assert result == "No specific pattern detected or invalid input."