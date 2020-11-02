import unittest
from mrtopo.translator import *

class TranslatorUnitTests(unittest.TestCase):

    def test_read_json(self):
        _dict = { "test": "hi", "number": 20, "list": ["1", "2", "3"]}
        parsed_dict = read_json("assets/valid_json.json")
        self.assertEqual(_dict, parsed_dict)

    # def test_invalid_read_json(self):
    #     self.assertRaises(json.decoder.JSONDecodeError, read_json("assets/invalid_json.json")) # TODO INVALIDATE

    def test_c_read_valid_single(self):
        _dict = {"plan": "CHO", "topologies": "RING"}
        expected = config.Config.build(_dict)
        actual = c_read("assets/valid_config_single_topology.json")
        self.assertEqual(expected, actual)
        pass

    def test_c_read_valid_mult(self):
        _dict = {"plan": "CHO", "topologies": ["RING", "CHORDAL"]}
        expected = config.Config.build(_dict)
        actual = c_read("assets/valid_config_mult_topology.json")
        self.assertEqual(expected, actual)
        pass

    def test_c_read_valid_no_plan(self):
        _dict = {"topologies": ["RING", "CHORDAL"]}
        expected = config.Config.build(_dict)
        actual = c_read("assets/valid_config_no_plan.json")
        self.assertEqual(expected, actual)
        pass

    def test_c_read_valid_no_topologies(self):
        _dict = {"plan": "CHO"}
        expected = config.Config.build(_dict)
        actual = c_read("assets/valid_config_no_topologies.json")
        self.assertEqual(expected, actual)
        pass

if __name__ == '__main__':
    unittest.main()
