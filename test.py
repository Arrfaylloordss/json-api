import json
import unittest

import jsonapi


class JsonAPITest(unittest.TestCase):

    def setUp(self):
        self.specification = jsonapi.Specification()
        self.specification.add_method(self.simple_method)

    def test_general(self):
        json_str = '''{
            "method" : "simple_method",
            "args" : {
                "a" : 1,
                "b" : 2
            }
        }
        '''
        json_obj = json.loads(json_str)
        response = self.specification.invoke_method(json_obj)
        self.assertEqual(response.get_result(), 3)

    def test_arguments_types_validation(self):
        json_str = '''{
            "method" : "simple_method",
            "args" : {
                "a" : "1",
                "b" : 2
            }
        }
        '''
        json_obj = json.loads(json_str)
        response = self.specification.invoke_method(json_obj)
        self.assertTrue(response.is_exception(jsonapi.InvalidArgumentTypeError))

    def simple_method(self, a: int, b: int) -> int:
        return a + b


if __name__ == '__main__':
    unittest.main()
