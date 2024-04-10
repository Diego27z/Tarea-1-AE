from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
 def build( self ):
  s1= self.addSwitch('s1')
  s2 = self.addSwitch('s2')
  s3 = self.addSwitch('s3')
  s4= self.addSwitch('s4')
  hostChile = self.addHost('h1')
  hostAustralia = self.addHost('h2')
  self.addLink(s1, s2, cls=TCLink, bw=300, delay='70ms', loss=5)
  self.addLink(s2, s3, cls=TCLink, bw=150, delay='50ms', loss=4)
  self.addLink(s3, s4, cls=TCLink, bw=200, delay='60ms', loss=3)

topos = { 'mytopo': (lambda: MyTopo()) }