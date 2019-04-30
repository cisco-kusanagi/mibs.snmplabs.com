#
# PySNMP MIB module RADLAN-VOIP-SNOOP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-VOIP-SNOOP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:42:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddressType, InetVersion, InetAddress, InetAddressPrefixLength, InetZoneIndex = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetVersion", "InetAddress", "InetAddressPrefixLength", "InetZoneIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, TimeTicks, Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity")
TextualConvention, MacAddress, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus", "TruthValue")
rlVoipSnoop = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 213))
if mibBuilder.loadTexts: rlVoipSnoop.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlVoipSnoop.setOrganization('')
rlVoipMngSnoopEnableScalar = MibScalar((1, 3, 6, 1, 4, 1, 89, 213, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVoipMngSnoopEnableScalar.setStatus('current')
class RlVoipQosType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("queue", 1), ("vpt", 2), ("dscp", 3))

rlVoipMngSnoopQosTable = MibTable((1, 3, 6, 1, 4, 1, 89, 213, 2), )
if mibBuilder.loadTexts: rlVoipMngSnoopQosTable.setStatus('current')
rlVoipMngSnoopQosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 213, 2, 1), ).setIndexNames((0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopQosType"))
if mibBuilder.loadTexts: rlVoipMngSnoopQosEntry.setStatus('current')
rlVoipMngSnoopQosType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 2, 1, 1), RlVoipQosType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVoipMngSnoopQosType.setStatus('current')
rlVoipMngSnoopQosValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVoipMngSnoopQosValue.setStatus('current')
class RlVoipMngSnoopIfIndexStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

rlVoipMngSnoopIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 89, 213, 3), )
if mibBuilder.loadTexts: rlVoipMngSnoopIfIndexTable.setStatus('current')
rlVoipMngSnoopIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 213, 3, 1), ).setIndexNames((0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopIfIndex"))
if mibBuilder.loadTexts: rlVoipMngSnoopIfIndexEntry.setStatus('current')
rlVoipMngSnoopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlVoipMngSnoopIfIndex.setStatus('current')
rlVoipMngSnoopIfIndexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 3, 1, 2), RlVoipMngSnoopIfIndexStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVoipMngSnoopIfIndexStatus.setStatus('current')
class RlVoipProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sip", 1), ("h323", 2), ("sccp", 3))

class RlVoipTcpUdpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("tcp", 2))

rlVoipMngSnoopSessionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 213, 4), )
if mibBuilder.loadTexts: rlVoipMngSnoopSessionTable.setStatus('current')
rlVoipMngSnoopSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 213, 4, 1), ).setIndexNames((0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstIpAddrType"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstIpAddr"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcIpAddrType"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcIpAddr"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstUdpRtp"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionDstUdpRtcp"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcUdpRtp"), (0, "RADLAN-VOIP-SNOOP", "rlVoipMngSnoopSessionSrcUdpRtcp"))
if mibBuilder.loadTexts: rlVoipMngSnoopSessionEntry.setStatus('current')
rlVoipMngSnoopSessionDstIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionDstIpAddrType.setStatus('current')
rlVoipMngSnoopSessionDstIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionDstIpAddr.setStatus('current')
rlVoipMngSnoopSessionSrcIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionSrcIpAddrType.setStatus('current')
rlVoipMngSnoopSessionSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionSrcIpAddr.setStatus('current')
rlVoipMngSnoopSessionDstUdpRtp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionDstUdpRtp.setStatus('current')
rlVoipMngSnoopSessionDstUdpRtcp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionDstUdpRtcp.setStatus('current')
rlVoipMngSnoopSessionSrcUdpRtp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionSrcUdpRtp.setStatus('current')
rlVoipMngSnoopSessionSrcUdpRtcp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionSrcUdpRtcp.setStatus('current')
rlVoipMngSnoopSessionProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 9), RlVoipProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionProtocolType.setStatus('current')
rlVoipMngSnoopSessionSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionSessionId.setStatus('current')
rlVoipMngSnoopSessionTcpUdpType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 213, 4, 1, 11), RlVoipTcpUdpType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlVoipMngSnoopSessionTcpUdpType.setStatus('current')
mibBuilder.exportSymbols("RADLAN-VOIP-SNOOP", rlVoipMngSnoopSessionSrcIpAddrType=rlVoipMngSnoopSessionSrcIpAddrType, rlVoipMngSnoopIfIndexTable=rlVoipMngSnoopIfIndexTable, rlVoipMngSnoopSessionDstIpAddr=rlVoipMngSnoopSessionDstIpAddr, rlVoipMngSnoopQosEntry=rlVoipMngSnoopQosEntry, RlVoipTcpUdpType=RlVoipTcpUdpType, rlVoipMngSnoopSessionTable=rlVoipMngSnoopSessionTable, rlVoipMngSnoopSessionSrcIpAddr=rlVoipMngSnoopSessionSrcIpAddr, rlVoipMngSnoopSessionDstIpAddrType=rlVoipMngSnoopSessionDstIpAddrType, rlVoipMngSnoopIfIndexStatus=rlVoipMngSnoopIfIndexStatus, rlVoipMngSnoopEnableScalar=rlVoipMngSnoopEnableScalar, rlVoipSnoop=rlVoipSnoop, rlVoipMngSnoopSessionDstUdpRtcp=rlVoipMngSnoopSessionDstUdpRtcp, rlVoipMngSnoopQosTable=rlVoipMngSnoopQosTable, RlVoipMngSnoopIfIndexStatus=RlVoipMngSnoopIfIndexStatus, rlVoipMngSnoopSessionProtocolType=rlVoipMngSnoopSessionProtocolType, RlVoipProtocolType=RlVoipProtocolType, rlVoipMngSnoopIfIndex=rlVoipMngSnoopIfIndex, rlVoipMngSnoopSessionTcpUdpType=rlVoipMngSnoopSessionTcpUdpType, rlVoipMngSnoopSessionSessionId=rlVoipMngSnoopSessionSessionId, PYSNMP_MODULE_ID=rlVoipSnoop, rlVoipMngSnoopQosValue=rlVoipMngSnoopQosValue, RlVoipQosType=RlVoipQosType, rlVoipMngSnoopSessionDstUdpRtp=rlVoipMngSnoopSessionDstUdpRtp, rlVoipMngSnoopSessionSrcUdpRtp=rlVoipMngSnoopSessionSrcUdpRtp, rlVoipMngSnoopSessionSrcUdpRtcp=rlVoipMngSnoopSessionSrcUdpRtcp, rlVoipMngSnoopIfIndexEntry=rlVoipMngSnoopIfIndexEntry, rlVoipMngSnoopSessionEntry=rlVoipMngSnoopSessionEntry, rlVoipMngSnoopQosType=rlVoipMngSnoopQosType)
