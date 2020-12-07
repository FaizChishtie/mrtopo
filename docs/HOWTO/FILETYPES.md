# File Types

See `/examples` in the [GitHub repo](https://github.com/FaizChishtie/mrtopo/blob/master/examples/temp_topo.py)

### Mininet Python Topology Files

Topology files should be .py files following the format described below:

* [Example file](https://github.com/FaizChishtie/mrtopo/blob/master/examples/temp_topo.py)

```
# Example topology dependency file - Chordal topology

"""
    Example imported files
"""
from mininet.topo import Topo
from mininet.net import Mininet
# ...

"""
    Pre-topology classes to inherit from some premade Mininet files
    to allow for networks to have certain attributes (i.e. IPv6 support)
"""
class dualStackHost( Host ):
    def config( self, v6Addr='1000::1/64', **params ):
        #...

"""
    Initializing the topology by inheriting from the Mininet Topo file
    and declaring switches/hosts in the MultiGraph data structure
"""
class chordalTopo( Topo ):
    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )

        # ... and now hosts
        s1_host = self.addHost( ... )
        s2_host = self.addHost( ... )

        # add edges between switch and corresponding host
        self.addLink( s1, s1_host )
        self.addLink( s2, s2_host )

"""
    Method run to set network up according to topology described above
"""
def setupNetwork():
    "Create network"
    topo = chordalTopo()
    network = Mininet( topo=topo, ... )
    network.start()
    #...

if __name__ == '__main__':
    setLogLevel( 'info' )
    setupNetwork()
```



### Configuration Files

> Currently not supported

Configuration files should be .json files following the format described below:

```
{
  "plan": "CHO",
  "topologies": ["RING", "TREE"]
}
```