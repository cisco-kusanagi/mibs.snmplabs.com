#
# PySNMP MIB module EXTREME-IP-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-IP-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:08:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Integer32, IpAddress, Counter32, NotificationType, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Integer32", "IpAddress", "Counter32", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Counter64")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
extremeIpSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 34))
if mibBuilder.loadTexts: extremeIpSecurity.setLastUpdated('200502140000Z')
if mibBuilder.loadTexts: extremeIpSecurity.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeIpSecurity.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeIpSecurity.setDescription('Extreme IP Security MIB')
extremeIpSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1))
extremeIpSecurityTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 0))
extremeIpSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 0, 1)).setObjects(("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityIpAddr"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityMacAddress"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityViolationType"))
if mibBuilder.loadTexts: extremeIpSecurityViolation.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityViolation.setDescription('For vlans/ports on which one or more of the IP Security features have been enabled, this trap will be generated when a packet received on that vlan/port is in violation of the configured IP Security protections')
extremeIpSecurityVlanIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityVlanIfIndex.setDescription('The ifIndex of the VLAN on which the violating packet was received.')
extremeIpSecurityVlanDescr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityVlanDescr.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityVlanDescr.setDescription('The description(name) of the VLAN on which the violating packet was received.')
extremeIpSecurityPortIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityPortIfIndex.setDescription('The ifIndex of the port on which the violating packet was received.')
extremeIpSecurityIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityIpAddr.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityIpAddr.setDescription('Source IP address of the violating packet')
extremeIpSecurityMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityMacAddress.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityMacAddress.setDescription('Source MAC address from the ethernet header of the violating packet')
extremeIpSecurityViolationType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("rogueDhcpServerPacket", 1), ("badIpMacBindingInArpPacket", 2), ("badIpInArpPacket", 3), ("badMacInArpPacket", 4), ("bcastSenderIpInArpPacket", 5), ("bcastTargetIpInArpPacket", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityViolationType.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityViolationType.setDescription('The type of IP Security violation that occurred - rogueDhcpServerPacket(1) A rogue DHCP server packet was received. - badIpMacBindingInArpPacket(2) The IP-MAC binding received in the ARP packet does not exist in the DHCP Bindings table or is incorrect. - badIpInArpPacket(3) The Source IP address in the ARP payload is invalid. - badMacInArpPacket(4) One of the MAC addresses in the ARP payload does not match with its counterpart in the ethernet header. - bcastSenderIpInArpPacket(5) The Sender IP address in the ARP payload is Broadcast. - bcastTargetIpInArpPacket(6) The Target IP address in the ARP payload is Broadcast.')
class HexOctet(TextualConvention, OctetString):
    description = 'A single hexidecimal octet used to specify TCP flags'
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class VlanTag(TextualConvention, Integer32):
    description = 'The tag used when encapsulating packets transmitted'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class IpProtocol(TextualConvention, Integer32):
    description = 'The value of the IP Protocol field of an IP Datagram Header. This identifies the protocol layer above IP. For example, the value 6 is used for TCP and the value 17 is used for UDP. The values of this field are defined in the Assigned Numbers RFC.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 17))
    namedValues = NamedValues(("unknown", 0), ("icmp", 1), ("tcp", 6), ("udp", 17))

class TcpFlagAnomalyReason(TextualConvention, Integer32):
    description = ' 1) (TCP flag SYN is set) and (its TCP source port < 1024). OR 2) (TCP flag == 0) and (TCP seq # == 0). OR 3) (TCP flag FIN/URG/PSH bits sre set) and (TCP seq # == 0). OR 4) Both TCP iflag SYN and FIN are set'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("flagSynAndSrcPort", 1), ("flagAndSeq", 2), ("flagFinAndUrgAandPshandSeq", 3), ("flagSynAndFin", 4))

class IcmpAnomalyReason(TextualConvention, Integer32):
    description = ' 1) the size of ICMP is large than pre-configured allowed size 2) Fragmented ICMP packet'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("icmpOverSize", 1), ("icmpFragmented", 2))

class TcpFragmentAnomalyReason(TextualConvention, Integer32):
    description = ' 1) TCP packet and incompleted TCP header (IP payload less tahn MIN_TCP_HDR_SIZE) 2) Fragmented TCP packet (IP fragment offset = 1) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tcpHdrLessSize", 1), ("tcpFragmented", 2))

extremeIpSecurityAnomalyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2))
extremeIpSecurityAnomalyTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0))
extremeIpSecurityAnomalyIpViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 1)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyIpProto"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyIpViolation.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityAnomalyIpViolation.setDescription("For ports on which the protocol anomaly protection IP features has been enabled, this trap will be generated when a packet received on that port if the packet's source IP == destination IP")
extremeIpSecurityAnomalyL4PortViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 2)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyIpProto"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcL4Port"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestL4Port"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyL4PortViolation.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityAnomalyL4PortViolation.setDescription('For ports on which the protocol anomaly protection L4port features has been enabled, this trap will be generated when a packet received on that port if 1) the packet is a TCP or UDP packetr. AND 2) its source L4 port == destination port')
extremeIpSecurityAnomalyTcpFlagViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 3)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcL4Port"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestL4Port"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFlagReason"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFlag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpSeq"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyTcpFlagViolation.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityAnomalyTcpFlagViolation.setDescription('For ports on which the protocol anomaly protection TCP flags features has been enabled, this trap will be generated when a TCP packet received on that port if 1) (TCP flag SYN is set) and (its TCP source port < 1024). OR 2) (TCP flag == 0) and (TCP seq # == 0). OR 3) (TCP flag FIN/URG/PSH bits sre set) and (TCP seq # == 0). OR 4) Both TCP iflag SYN and FIN are set')
extremeIpSecurityAnomalyTcpFragmentViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 4)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFragmentReason"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpHdrSize"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyTcpFragmentViolation.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityAnomalyTcpFragmentViolation.setDescription('For ports on which the protocol anomaly protection TCP fragment features has been enabled, this trap will be generated when a packet received on that port if 1) the packet is a TCP, and its size of the TCP header is less than pre-configured value; or 2) the packet is a TCP and it is a IP fragmented packet (IP offset != 0)')
extremeIpSecurityAnomalyIcmpViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 5)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyIcmpReason"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyIcmpViolation.setStatus('current')
if mibBuilder.loadTexts: extremeIpSecurityAnomalyIcmpViolation.setDescription('For ports on which the protocol anomaly protection ICMP features has been enabled, this trap will be generated when an ICMP packet received on that port if 1) the size of ICMP (IP payload) is large thant pre-configured value; or 2) it is a fragmented IP/ICMP packet (IP offset != 0)')
esAnomalyPortIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: esAnomalyPortIfIndex.setDescription('The ifIndex of the port on which the violating packet was received.')
esAnomalyVlanIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: esAnomalyVlanIfIndex.setDescription('The ifIndex of the VLAN on which the violating packet was received.')
esAnomalyVlanDescr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyVlanDescr.setStatus('current')
if mibBuilder.loadTexts: esAnomalyVlanDescr.setDescription('The description(name) of the VLAN on which the violating packet was received.')
esAnomalySrcMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcMacAddress.setStatus('current')
if mibBuilder.loadTexts: esAnomalySrcMacAddress.setDescription('Source MAC address in the violating packet')
esAnomalyDestMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestMacAddress.setStatus('current')
if mibBuilder.loadTexts: esAnomalyDestMacAddress.setDescription('Destination MAC address in the violating packet')
esAnomalySrcIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 6), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcIpAddrType.setStatus('current')
if mibBuilder.loadTexts: esAnomalySrcIpAddrType.setDescription('source IP address type: ipv4 or ipv6')
esAnomalySrcIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 7), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcIpAddr.setStatus('current')
if mibBuilder.loadTexts: esAnomalySrcIpAddr.setDescription('source IP address in the violating packet')
esAnomalyDestIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 8), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestIpAddrType.setStatus('current')
if mibBuilder.loadTexts: esAnomalyDestIpAddrType.setDescription('destination IP address type: ipv4 or ipv6')
esAnomalyDestIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 9), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestIpAddr.setStatus('current')
if mibBuilder.loadTexts: esAnomalyDestIpAddr.setDescription('destination IP address in the violating packet')
esAnomalyIpProto = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 10), IpProtocol()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyIpProto.setStatus('current')
if mibBuilder.loadTexts: esAnomalyIpProto.setDescription('IP protocol in the violating packet')
esAnomalySrcL4Port = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 11), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcL4Port.setStatus('current')
if mibBuilder.loadTexts: esAnomalySrcL4Port.setDescription('tcp/udp source port number in the violating packet')
esAnomalyDestL4Port = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 12), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestL4Port.setStatus('current')
if mibBuilder.loadTexts: esAnomalyDestL4Port.setDescription('tcp/udp destination port in the violating packet')
esAnomalyTcpFlag = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 13), HexOctet()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpFlag.setStatus('current')
if mibBuilder.loadTexts: esAnomalyTcpFlag.setDescription('TCP flags in the violating packet')
esAnomalyTcpSeq = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 14), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpSeq.setStatus('current')
if mibBuilder.loadTexts: esAnomalyTcpSeq.setDescription('TCP sequence number in the violating packet')
esAnomalyTcpHdrSize = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 15), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpHdrSize.setStatus('current')
if mibBuilder.loadTexts: esAnomalyTcpHdrSize.setDescription('TCP Header size in the violating packet')
esAnomalyTcpFlagReason = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 16), TcpFlagAnomalyReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpFlagReason.setStatus('current')
if mibBuilder.loadTexts: esAnomalyTcpFlagReason.setDescription('TCP flag anomaly reason code')
esAnomalyIcmpReason = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 17), IcmpAnomalyReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyIcmpReason.setStatus('current')
if mibBuilder.loadTexts: esAnomalyIcmpReason.setDescription('ICMP anomaly reason code')
esAnomalyVlanTag = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 18), VlanTag()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyVlanTag.setStatus('current')
if mibBuilder.loadTexts: esAnomalyVlanTag.setDescription('the vlan tag in the violating packet')
esAnomalyTcpFragmentReason = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 19), TcpFragmentAnomalyReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpFragmentReason.setStatus('current')
if mibBuilder.loadTexts: esAnomalyTcpFragmentReason.setDescription('TCP fragment anomaly reason code')
mibBuilder.exportSymbols("EXTREME-IP-SECURITY-MIB", extremeIpSecurityIpAddr=extremeIpSecurityIpAddr, extremeIpSecurityAnomalyL4PortViolation=extremeIpSecurityAnomalyL4PortViolation, esAnomalyTcpHdrSize=esAnomalyTcpHdrSize, extremeIpSecurity=extremeIpSecurity, HexOctet=HexOctet, esAnomalyTcpSeq=esAnomalyTcpSeq, TcpFragmentAnomalyReason=TcpFragmentAnomalyReason, esAnomalyPortIfIndex=esAnomalyPortIfIndex, extremeIpSecurityPortIfIndex=extremeIpSecurityPortIfIndex, extremeIpSecurityAnomalyTraps=extremeIpSecurityAnomalyTraps, extremeIpSecurityAnomalyIcmpViolation=extremeIpSecurityAnomalyIcmpViolation, IcmpAnomalyReason=IcmpAnomalyReason, extremeIpSecurityAnomalyIpViolation=extremeIpSecurityAnomalyIpViolation, esAnomalyIcmpReason=esAnomalyIcmpReason, esAnomalyVlanTag=esAnomalyVlanTag, esAnomalyIpProto=esAnomalyIpProto, esAnomalySrcL4Port=esAnomalySrcL4Port, extremeIpSecurityVlanDescr=extremeIpSecurityVlanDescr, extremeIpSecurityAnomalyTcpFlagViolation=extremeIpSecurityAnomalyTcpFlagViolation, VlanTag=VlanTag, extremeIpSecurityViolation=extremeIpSecurityViolation, esAnomalySrcIpAddrType=esAnomalySrcIpAddrType, esAnomalyDestIpAddrType=esAnomalyDestIpAddrType, esAnomalyDestL4Port=esAnomalyDestL4Port, esAnomalyTcpFlagReason=esAnomalyTcpFlagReason, extremeIpSecurityMacAddress=extremeIpSecurityMacAddress, extremeIpSecurityViolationType=extremeIpSecurityViolationType, extremeIpSecurityAnomalyTcpFragmentViolation=extremeIpSecurityAnomalyTcpFragmentViolation, esAnomalyTcpFlag=esAnomalyTcpFlag, extremeIpSecurityVlanIfIndex=extremeIpSecurityVlanIfIndex, extremeIpSecurityTrapsPrefix=extremeIpSecurityTrapsPrefix, esAnomalyDestIpAddr=esAnomalyDestIpAddr, extremeIpSecurityAnomalyTrapsPrefix=extremeIpSecurityAnomalyTrapsPrefix, esAnomalyTcpFragmentReason=esAnomalyTcpFragmentReason, esAnomalyVlanIfIndex=esAnomalyVlanIfIndex, PYSNMP_MODULE_ID=extremeIpSecurity, extremeIpSecurityTraps=extremeIpSecurityTraps, esAnomalySrcMacAddress=esAnomalySrcMacAddress, IpProtocol=IpProtocol, esAnomalyVlanDescr=esAnomalyVlanDescr, esAnomalyDestMacAddress=esAnomalyDestMacAddress, esAnomalySrcIpAddr=esAnomalySrcIpAddr, TcpFlagAnomalyReason=TcpFlagAnomalyReason)
