import unittest

from helper_functions.config_parser import import_config


class TestConfigParser(unittest.TestCase):
    def test_config_parsing_file_location(self) -> None:
        with self.subTest('It raises on a file not found'):
            with self.assertRaises(FileNotFoundError):
                import_config('surely_not_found')

        with self.subTest('It raises on trying to parse a template config'):
            with self.assertRaises(ValueError):
                import_config('config_template.yml')

        with self.subTest('It successfully parses an example config'):
            config = import_config('test/test_config.yml')
            self.assertEqual(config['version'], '199001')
            self.assertEqual(config['process']['user'], 'geodbadmin')


if __name__ == '__main__':
    unittest.main()
