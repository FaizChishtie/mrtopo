import unittest

from mrtopo.translator import c_read
from mrtopo.interpreter import interpret, construct_networks
from mrtopo.structures import topology

class InterpreterUnitTests(unittest.TestCase):

    def test_construct_networks(self):
        topologies = [topology.Topology.RING, topology.Topology.TREE]
        expected = construct_networks(topologies)
        config = c_read('assets/valid_config_mult_topology.json')
        actual = construct_networks(config.topologies)
        self.assertEqual(expected, actual)

    def test_interpret(self):
        config = c_read('assets/valid_config_mult_topology.json')
        pass



if __name__ == '__main__':
    unittest.main()
