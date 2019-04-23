from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()



class Tutorial (object):
 
  def __init__ (self, connection):
   
    self.connection = connection
 connection.addListeners(self)
 self.mac_to_port = {}


  def resend_packet (self, packet_in, out_port):
    msg = of.ofp_packet_out()
    msg.data = packet_in

    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    self.connection.send(msg)


  def act_like_hub (self, packet, packet_in):
   
    self.resend_packet(packet_in, of.OFPP_ALL)


  def act_like_switch (self, packet, packet_in):
   
    in_port = packet_in.in_port
    dl_src = str(packet.src)
    dl_dst = str(packet.dst)
    self.mac_to_port[dl_src] = in_port
  
    if dl_dst in self.mac_to_port:
      dst_in_port = self.mac_to_port[dl_dst]
      self.resend_packet(packet_in, dst_in_port)

      log.debug("Installing flow for mac address {} on port {}. Destination mac is {}".format(dl_src, in_port, dl_dst))
   
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet)
      msg.match = of.ofp_match.from_packet(packet)
      action = of.ofp_action_output(port=dst_in_port)
      msg.actions.append(action)
 
      self.connection.send(msg)

    else:
      self.resend_packet(packet_in, of.OFPP_ALL)


  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.

    #self.act_like_hub(packet, packet_in)
    self.act_like_switch(packet, packet_in)



def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Tutorial(event.connection)
core.openflow.addListenerByName("ConnectionUp", start_switch)
