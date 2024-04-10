from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

class CustomTopo(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3, bw=250, delay='5ms', loss=5)
        self.addLink(s3, s4, bw=150, delay='20ms', loss=2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

if __name__ == '__main__':
    setLogLevel('info')
    topo = CustomTopo()
    net = Mininet(topo=topo, link=TCLink, autoSetMacs=True, autoStaticArp=True)
    net.start()
    CLI(net)
    net.stop()
