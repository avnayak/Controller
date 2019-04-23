

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
	Topo.__init__( self )

         # Add hosts and switches
	centerSwitch = self.addSwitch( 's7' )
	leftSwitch = self.addSwitch( 's5')
	rightSwitch = self.addSwitch( 's6')
	llSwitch = self.addSwitch( 's1')
	lrSwitch = self.addSwitch( 's2')
	rlSwitch = self.addSwitch( 's3' )
	rrSwitch = self.addSwitch( 's4' )	
	ll1Host = self.addHost( 'h1' )
	ll2Host = self.addHost( 'h2' )	
	lr1Host = self.addHost( 'h3' )
	lr2Host = self.addHost( 'h4' )
	rl1Host = self.addHost( 'h5' )
	rl2Host = self.addHost( 'h6' )
	rr1Host = self.addHost( 'h7' )
	rr2Host = self.addHost( 'h8' )
        # Add links
	self.addLink( leftSwitch, centerSwitch  )
	self.addLink( rightSwitch, centerSwitch  )
	self.addLink( llSwitch, leftSwitch  )
	self.addLink( lrSwitch, leftSwitch)
	self.addLink( ll1Host, llSwitch )
	self.addLink( ll2Host, llSwitch )
	self.addLink( lr1Host, lrSwitch )
	self.addLink( lr2Host, lrSwitch )
	self.addLink( rlSwitch, rightSwitch  )
	self.addLink( rrSwitch, rightSwitch)
	self.addLink( rl1Host, rlSwitch )
	self.addLink( rl2Host, rlSwitch )
	self.addLink( rr1Host, rrSwitch )
	self.addLink( rr2Host, rrSwitch )



topos = { 'mytopo': ( lambda: MyTopo() ) }
