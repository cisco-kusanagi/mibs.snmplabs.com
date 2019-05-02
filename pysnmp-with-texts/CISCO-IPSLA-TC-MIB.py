#
# PySNMP MIB module CISCO-IPSLA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:02:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, ObjectIdentity, Counter64, iso, Bits, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, MibIdentifier, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Counter64", "iso", "Bits", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "MibIdentifier", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpSlaTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 624))
ciscoIpSlaTCMIB.setRevisions(('2007-03-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setLastUpdated('200703230000Z')
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553 NETS Email: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setDescription('This MIB contains textual conventions used by CISCO IPSLA MIBs. Acronyms: FEC: Forward Equivalence Class LPD: Label Path Discovery LSP: Label Switched Path MPLS: Multi Protocol Label Switching RTT: Round Trip Time SAA: Service Assurance Agent SLA: Service Level Agreement VPN: Virtual Private Network ICPIF: Calculated Planning Impairment Factor')
class IpSlaOperType(TextualConvention, Integer32):
    description = "Specifies the type of IP SLA operation to be performed. icmpEcho(1) - The value 'icmpEcho' will cause the IP SLA application to perform a timed ICMP echo request/response operation. udpEcho(2) - The value 'udpEcho' will cause the IP SLA application to perform a timed udp packet send/receive operation. tcpConnect(3) - The value 'tcpConnect' will cause the IP SLA application to perform a timed TCP connect operation. udpJitter(4) - The value 'udpjitter' will cause the IP SLA application to perform delay variance analysis using UDP timestamp packets. icmpjitter(5) - The value 'icmpjitter' will cause the IP SLA application to perform delay variance analysis using ICMP timestamp packets."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("icmpEcho", 1), ("udpEcho", 2), ("tcpConnect", 3), ("udpJitter", 4), ("icmpJitter", 5))

class IpSlaCodecType(TextualConvention, Integer32):
    description = 'Specifies the IP SLA codec type to be used with the UDP jitter operation. The following codec types are defined: notApplicable(0) - no CodecType is defined g711ulaw(1) - uses G.711 U Law 64000 bps g711alaw(2) - uses G.711 A Law 64000 bps g729a(3) - uses G.729 8000 bps'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("g711ulaw", 1), ("g711alaw", 2), ("g729a", 3))

class IpSlaReactVar(TextualConvention, Integer32):
    description = 'The following are specific reaction variables for an IP SLA operation to react upon: rtt(1) - Round Trip Time jitterSDAvg(2) - Jitter average from source to destination jitterDSAvg(3) - Jitter average from destination to source packetLossSD(4) - Packet loss from source to destination packetLossDS(5) - Packet loss from destination to source mos(6) - Mean Opinion Score timeout(7) - Timeout of the operation connectionLoss(8) - Connection failed to the destination verifyError(9) - Data corruption occurs jitterAvg(10) - Jitter average in both directions icpif(11) - Calculated Planning Impairment Factor packetMIA(12) - Missed packets in operation packetLateArrival(13) - Packets arriving late packetOutOfSequence(14) - Packets arriving out of sequence maxOfPositiveSD(15) - Maximum positive jitter from source to destination maxOfNegativeSD(16) - Maximum negative jitter from source to destination maxOfPositiveDS(17) - Maximum positive jitter from destination to source maxOfNegativeDS(18) - Maximum negative jitter from destination to source. successivePacketLoss(19)- Successive packet dropped maxOfLatencyDS(20) - Maximum Latency from Destination to Source maxOfLatencySD(21) - Maximum Latency from Source to Destination latencyDSAvg(22) - Latency average from Destination to Source latencySDAvg(23) - Latency average from Source to Destination packetLoss(24) - Packets loss in both directions'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("rtt", 1), ("jitterSDAvg", 2), ("jitterDSAvg", 3), ("packetLossSD", 4), ("packetLossDS", 5), ("mos", 6), ("timeout", 7), ("connectionLoss", 8), ("verifyError", 9), ("jitterAvg", 10), ("icpif", 11), ("packetMIA", 12), ("packetLateArrival", 13), ("packetOutOfSequence", 14), ("maxOfPositiveSD", 15), ("maxOfNegativeSD", 16), ("maxOfPositiveDS", 17), ("maxOfNegativeDS", 18), ("successivePacketLoss", 19), ("maxOfLatencyDS", 20), ("maxOfLatencySD", 21), ("latencyDSAvg", 22), ("latencySDAvg", 23), ("packetLoss", 24))

mibBuilder.exportSymbols("CISCO-IPSLA-TC-MIB", IpSlaOperType=IpSlaOperType, IpSlaCodecType=IpSlaCodecType, PYSNMP_MODULE_ID=ciscoIpSlaTCMIB, ciscoIpSlaTCMIB=ciscoIpSlaTCMIB, IpSlaReactVar=IpSlaReactVar)
