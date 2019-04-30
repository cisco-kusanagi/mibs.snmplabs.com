#
# PySNMP MIB module EXTREME-IP-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-IP-SECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:54:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Integer32, TimeTicks, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter64, NotificationType, Counter32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Integer32", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter64", "NotificationType", "Counter32", "Bits", "ObjectIdentity")
MacAddress, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DisplayString", "TextualConvention")
extremeIpSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 34))
if mibBuilder.loadTexts: extremeIpSecurity.setLastUpdated('200502140000Z')
if mibBuilder.loadTexts: extremeIpSecurity.setOrganization('Extreme Networks, Inc.')
extremeIpSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1))
extremeIpSecurityTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 0))
extremeIpSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 0, 1)).setObjects(("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityIpAddr"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityMacAddress"), ("EXTREME-IP-SECURITY-MIB", "extremeIpSecurityViolationType"))
if mibBuilder.loadTexts: extremeIpSecurityViolation.setStatus('current')
extremeIpSecurityVlanIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityVlanIfIndex.setStatus('current')
extremeIpSecurityVlanDescr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityVlanDescr.setStatus('current')
extremeIpSecurityPortIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityPortIfIndex.setStatus('current')
extremeIpSecurityIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityIpAddr.setStatus('current')
extremeIpSecurityMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityMacAddress.setStatus('current')
extremeIpSecurityViolationType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("rogueDhcpServerPacket", 1), ("badIpMacBindingInArpPacket", 2), ("badIpInArpPacket", 3), ("badMacInArpPacket", 4), ("bcastSenderIpInArpPacket", 5), ("bcastTargetIpInArpPacket", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeIpSecurityViolationType.setStatus('current')
class HexOctet(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class VlanTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class IpProtocol(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 17))
    namedValues = NamedValues(("unknown", 0), ("icmp", 1), ("tcp", 6), ("udp", 17))

class TcpFlagAnomalyReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("flagSynAndSrcPort", 1), ("flagAndSeq", 2), ("flagFinAndUrgAandPshandSeq", 3), ("flagSynAndFin", 4))

class IcmpAnomalyReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("icmpOverSize", 1), ("icmpFragmented", 2))

class TcpFragmentAnomalyReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tcpHdrLessSize", 1), ("tcpFragmented", 2))

extremeIpSecurityAnomalyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2))
extremeIpSecurityAnomalyTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0))
extremeIpSecurityAnomalyIpViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 1)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyIpProto"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyIpViolation.setStatus('current')
extremeIpSecurityAnomalyL4PortViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 2)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyIpProto"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcL4Port"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestL4Port"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyL4PortViolation.setStatus('current')
extremeIpSecurityAnomalyTcpFlagViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 3)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcL4Port"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestL4Port"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFlagReason"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFlag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpSeq"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyTcpFlagViolation.setStatus('current')
extremeIpSecurityAnomalyTcpFragmentViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 4)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpFragmentReason"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyTcpHdrSize"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyTcpFragmentViolation.setStatus('current')
extremeIpSecurityAnomalyIcmpViolation = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 0, 5)).setObjects(("EXTREME-IP-SECURITY-MIB", "esAnomalyPortIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanIfIndex"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanDescr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestMacAddress"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyVlanTag"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalySrcIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddrType"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyDestIpAddr"), ("EXTREME-IP-SECURITY-MIB", "esAnomalyIcmpReason"))
if mibBuilder.loadTexts: extremeIpSecurityAnomalyIcmpViolation.setStatus('current')
esAnomalyPortIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyPortIfIndex.setStatus('current')
esAnomalyVlanIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyVlanIfIndex.setStatus('current')
esAnomalyVlanDescr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyVlanDescr.setStatus('current')
esAnomalySrcMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcMacAddress.setStatus('current')
esAnomalyDestMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestMacAddress.setStatus('current')
esAnomalySrcIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 6), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcIpAddrType.setStatus('current')
esAnomalySrcIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 7), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcIpAddr.setStatus('current')
esAnomalyDestIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 8), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestIpAddrType.setStatus('current')
esAnomalyDestIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 9), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestIpAddr.setStatus('current')
esAnomalyIpProto = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 10), IpProtocol()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyIpProto.setStatus('current')
esAnomalySrcL4Port = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 11), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalySrcL4Port.setStatus('current')
esAnomalyDestL4Port = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 12), InetPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyDestL4Port.setStatus('current')
esAnomalyTcpFlag = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 13), HexOctet()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpFlag.setStatus('current')
esAnomalyTcpSeq = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 14), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpSeq.setStatus('current')
esAnomalyTcpHdrSize = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 15), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpHdrSize.setStatus('current')
esAnomalyTcpFlagReason = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 16), TcpFlagAnomalyReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpFlagReason.setStatus('current')
esAnomalyIcmpReason = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 17), IcmpAnomalyReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyIcmpReason.setStatus('current')
esAnomalyVlanTag = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 18), VlanTag()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyVlanTag.setStatus('current')
esAnomalyTcpFragmentReason = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 34, 2, 19), TcpFragmentAnomalyReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: esAnomalyTcpFragmentReason.setStatus('current')
mibBuilder.exportSymbols("EXTREME-IP-SECURITY-MIB", extremeIpSecurityMacAddress=extremeIpSecurityMacAddress, TcpFragmentAnomalyReason=TcpFragmentAnomalyReason, extremeIpSecurityAnomalyTrapsPrefix=extremeIpSecurityAnomalyTrapsPrefix, esAnomalyDestIpAddrType=esAnomalyDestIpAddrType, esAnomalyTcpFlagReason=esAnomalyTcpFlagReason, IpProtocol=IpProtocol, esAnomalyVlanTag=esAnomalyVlanTag, esAnomalyDestMacAddress=esAnomalyDestMacAddress, extremeIpSecurityAnomalyL4PortViolation=extremeIpSecurityAnomalyL4PortViolation, esAnomalyDestIpAddr=esAnomalyDestIpAddr, extremeIpSecurityViolation=extremeIpSecurityViolation, extremeIpSecurityPortIfIndex=extremeIpSecurityPortIfIndex, esAnomalyTcpFragmentReason=esAnomalyTcpFragmentReason, esAnomalySrcIpAddrType=esAnomalySrcIpAddrType, extremeIpSecurityIpAddr=extremeIpSecurityIpAddr, VlanTag=VlanTag, extremeIpSecurityAnomalyIcmpViolation=extremeIpSecurityAnomalyIcmpViolation, esAnomalySrcIpAddr=esAnomalySrcIpAddr, esAnomalyVlanIfIndex=esAnomalyVlanIfIndex, esAnomalyIcmpReason=esAnomalyIcmpReason, extremeIpSecurityTrapsPrefix=extremeIpSecurityTrapsPrefix, esAnomalySrcMacAddress=esAnomalySrcMacAddress, IcmpAnomalyReason=IcmpAnomalyReason, extremeIpSecurityAnomalyTcpFragmentViolation=extremeIpSecurityAnomalyTcpFragmentViolation, esAnomalyPortIfIndex=esAnomalyPortIfIndex, extremeIpSecurityAnomalyTraps=extremeIpSecurityAnomalyTraps, PYSNMP_MODULE_ID=extremeIpSecurity, esAnomalyTcpFlag=esAnomalyTcpFlag, esAnomalyIpProto=esAnomalyIpProto, esAnomalySrcL4Port=esAnomalySrcL4Port, extremeIpSecurityVlanIfIndex=extremeIpSecurityVlanIfIndex, extremeIpSecurityViolationType=extremeIpSecurityViolationType, extremeIpSecurityAnomalyTcpFlagViolation=extremeIpSecurityAnomalyTcpFlagViolation, extremeIpSecurityVlanDescr=extremeIpSecurityVlanDescr, HexOctet=HexOctet, extremeIpSecurity=extremeIpSecurity, esAnomalyDestL4Port=esAnomalyDestL4Port, esAnomalyTcpSeq=esAnomalyTcpSeq, esAnomalyTcpHdrSize=esAnomalyTcpHdrSize, esAnomalyVlanDescr=esAnomalyVlanDescr, extremeIpSecurityAnomalyIpViolation=extremeIpSecurityAnomalyIpViolation, TcpFlagAnomalyReason=TcpFlagAnomalyReason, extremeIpSecurityTraps=extremeIpSecurityTraps)
