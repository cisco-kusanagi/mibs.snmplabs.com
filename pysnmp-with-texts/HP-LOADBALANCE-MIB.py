#
# PySNMP MIB module HP-LOADBALANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-LOADBALANCE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:36:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Counter32, TimeTicks, Unsigned32, Bits, IpAddress, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "Bits", "IpAddress", "MibIdentifier", "Counter64")
TextualConvention, MacAddress, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "RowStatus", "TruthValue", "DisplayString")
hpicfLoadBalanceMod = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76))
hpicfLoadBalanceMod.setRevisions(('2011-03-22 22:22', '2010-06-22 22:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfLoadBalanceMod.setRevisionsDescriptions(('Added a table to get the current egress port in the trunk.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpicfLoadBalanceMod.setLastUpdated('201103222222Z')
if mibBuilder.loadTexts: hpicfLoadBalanceMod.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfLoadBalanceMod.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfLoadBalanceMod.setDescription('MIB module for configuring trunk Load Balancing on Hewlett-Packard network devices.')
hpicfLoadBalanceNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 0))
hpicfLoadBalanceMethodMod = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1))
hpicfLoadBalanceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2))
hpicfTrunkLoadBalanceMethod = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("l3based", 1), ("l4based", 2), ("l2based", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTrunkLoadBalanceMethod.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkLoadBalanceMethod.setDescription('Method to be used for Load Balancing.')
hpicfTrunkClearStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2), )
if mibBuilder.loadTexts: hpicfTrunkClearStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkClearStatsTable.setDescription('This table is for resetting the statistics for the given trunk.')
hpicfTrunkClearStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2, 1), ).setIndexNames((0, "HP-LOADBALANCE-MIB", "hpicfTrunkId"))
if mibBuilder.loadTexts: hpicfTrunkClearStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkClearStatsEntry.setDescription('This entry is used to clear the statistics for the given trunk.')
hpicfTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfTrunkId.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkId.setDescription('This object uniquely identifies the entry in this table.')
hpicfTrunkStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTrunkStatsClear.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkStatsClear.setDescription("This object is to clear the statistics for the trunk identified by 'hpicfTrunkId'. Statistics counters will be cleared when this object is set to 'true'. This object will always returns 'false'.")
hpicfTrunkStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3), )
if mibBuilder.loadTexts: hpicfTrunkStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkStatsTable.setDescription('A collection of statistics for the specified trunk.')
hpicfTrunkStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1), ).setIndexNames((0, "HP-LOADBALANCE-MIB", "hpicfTrunkId"))
if mibBuilder.loadTexts: hpicfTrunkStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkStatsEntry.setDescription('A collection of statistics for the specified trunk.')
hpicfTrunkUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 1), Unsigned32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkUpTime.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkUpTime.setDescription('The time the trunk has been up or since the counters were reset.')
hpicfTrunkTotalBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 2), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkTotalBytesRx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkTotalBytesRx.setDescription('Total number of bytes received on this trunk.')
hpicfTrunkTotalBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 3), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkTotalBytesTx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkTotalBytesTx.setDescription('Total number of bytes transmitted on this trunk.')
hpicfTrunkTotalFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 4), Counter64()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkTotalFramesRx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkTotalFramesRx.setDescription('Total number of frames received on this trunk.')
hpicfTrunkTotalFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 5), Counter64()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkTotalFramesTx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkTotalFramesTx.setDescription('Total number of frames transmitted on this trunk.')
hpicfTrunkTotalDropsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 3, 1, 6), Counter64()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkTotalDropsTx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkTotalDropsTx.setDescription('Total number of transmitted frames which were dropped because the port was oversubscribed.')
hpicfTrunkPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4), )
if mibBuilder.loadTexts: hpicfTrunkPortStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortStatsTable.setDescription('A collection of statistics for specified port of the trunk.')
hpicfTrunkPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1), ).setIndexNames((0, "HP-LOADBALANCE-MIB", "hpicfTrunkId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfTrunkPortStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortStatsEntry.setDescription('A collection of statistics for specified port of the trunk.')
hpicfTrunkPortBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 1), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortBytesRx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortBytesRx.setDescription('Total number of bytes received on the specified port of the trunk.')
hpicfTrunkPortBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 2), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortBytesTx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortBytesTx.setDescription('Total number of bytes transmitted on the specified port of the trunk.')
hpicfTrunkPortFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 3), Counter64()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortFramesRx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortFramesRx.setDescription('Total number of frames received on the specified port of the trunk.')
hpicfTrunkPortFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 4), Counter64()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortFramesTx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortFramesTx.setDescription('Total number of frames transmitted on the specified port of the trunk.')
hpicfTrunkPortFramesDropTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 5), Counter64()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortFramesDropTx.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortFramesDropTx.setDescription('Total number of transmitted frames which were dropped on the specified port of the trunk because of oversubscription.')
hpicfTrunkPortRxFramePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 6), Unsigned32()).setUnits('Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortRxFramePercent.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortRxFramePercent.setDescription('Percentage of frames received by this specified port of the trunk, calculated as the total number of frames received by this port over the total number of frames received by all ports in the trunk group')
hpicfTrunkPortTxFramePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 7), Unsigned32()).setUnits('Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortTxFramePercent.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortTxFramePercent.setDescription('Percentage of frames transmitted by this specified port of the trunk, calculated as the total number of frames transmitted by this port over the total number of frames transmitted by all ports in the trunk group')
hpicfTrunkPortDropTxFramePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTrunkPortDropTxFramePercent.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortDropTxFramePercent.setDescription('Percentage of frames transmitted by this port that are dropped because of oversubscription, calculated as the total number of dropped frames in transmission over the total number of frames transmitted by the specified port of the trunk.')
hpicfLoadBalanceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5))
hpicfLoadBalanceTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1), )
if mibBuilder.loadTexts: hpicfLoadBalanceTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceTable.setDescription('A table which gives the current egress port in the trunk for the specific conversation.')
hpicfLoadBalanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1), ).setIndexNames((0, "HP-LOADBALANCE-MIB", "hpicfLoadBalanceIndex"))
if mibBuilder.loadTexts: hpicfLoadBalanceEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceEntry.setDescription('gives the current egress port in the trunk for the specific conversation.')
hpicfLoadBalanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfLoadBalanceIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceIndex.setDescription('The index which uniquely identifies a row in the table.')
hpicfLoadBalanceTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceTrunkId.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceTrunkId.setDescription('Specifies the trunk index.')
hpicfLoadBalanceSourceMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceSourceMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceSourceMacAddr.setDescription('Specifies the source Mac address.')
hpicfLoadBalanceDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceDestMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceDestMacAddr.setDescription('Specifies the destination Mac address')
hpicfLoadBalanceIPSourceAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceIPSourceAddrType.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceIPSourceAddrType.setDescription('Specifies the source IP address type.')
hpicfLoadBalanceIPSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 6), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceIPSourceAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceIPSourceAddr.setDescription('Specifies the source IP address.')
hpicfLoadBalanceIPDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 7), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceIPDestAddrType.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceIPDestAddrType.setDescription('Specifies the destination IP address type.')
hpicfLoadBalanceIPDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 8), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceIPDestAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceIPDestAddr.setDescription('Specifies the destination IP address.')
hpicfLoadBalanceSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceSourcePort.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceSourcePort.setDescription('Specifies the TCP/UDP source port.')
hpicfLoadBalanceDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceDestPort.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceDestPort.setDescription('Specifies the TCP/UDP destination port.')
hpicfLoadBalanceEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceEtherType.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceEtherType.setDescription('Specifies the ether-type of the packet.')
hpicfLoadBalanceInboundVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceInboundVlan.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceInboundVlan.setDescription('Specifies the inbound VLAN of the packet.')
hpicfLoadBalanceInboundPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 13), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceInboundPort.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceInboundPort.setDescription('Specifies the inbound port of the packet.')
hpicfLoadBalanceOutboundPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 14), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfLoadBalanceOutboundPort.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceOutboundPort.setDescription('Specifies the port on which the specified stream with given source and destination information will be forwarded out.')
hpicfLoadBalanceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 1, 5, 1, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfLoadBalanceStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceStatus.setDescription('Status of the load balance entry.')
hpicfLoadBalanceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 1))
hpicfLoadBalanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2))
hpicfLoadBalanceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 1, 1)).setObjects(("HP-LOADBALANCE-MIB", "hpicfLoadBalanceGroup"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLoadBalanceCompliance = hpicfLoadBalanceCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceCompliance.setDescription('The compliance statement for devices implementing the hpicfLoadBalanceMethodMod MIB.')
hpicfTrunkStatsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 1, 2)).setObjects(("HP-LOADBALANCE-MIB", "hpicfTrunkStatsClearGroup"), ("HP-LOADBALANCE-MIB", "hpicfTrunkStatsGroup"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrunkStatsCompliance = hpicfTrunkStatsCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkStatsCompliance.setDescription('The compliance statement for devices implementing the statistics of the trunk and trunk port.')
hpicfLoadBalanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 1)).setObjects(("HP-LOADBALANCE-MIB", "hpicfTrunkLoadBalanceMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLoadBalanceGroup = hpicfLoadBalanceGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceGroup.setDescription('A collection of objects for selecting a load balancing method to use.')
hpicfTrunkStatsClearGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 2)).setObjects(("HP-LOADBALANCE-MIB", "hpicfTrunkStatsClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrunkStatsClearGroup = hpicfTrunkStatsClearGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkStatsClearGroup.setDescription('A collection of objects for clearing the statistics.')
hpicfTrunkStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 3)).setObjects(("HP-LOADBALANCE-MIB", "hpicfTrunkUpTime"), ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalBytesRx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalBytesTx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalFramesTx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalFramesRx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkTotalDropsTx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrunkStatsGroup = hpicfTrunkStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkStatsGroup.setDescription('A collection of objects for trunk statistics.')
hpicfTrunkPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 4)).setObjects(("HP-LOADBALANCE-MIB", "hpicfTrunkPortBytesRx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortBytesTx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortFramesRx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortFramesTx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortFramesDropTx"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortRxFramePercent"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortTxFramePercent"), ("HP-LOADBALANCE-MIB", "hpicfTrunkPortDropTxFramePercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrunkPortStatsGroup = hpicfTrunkPortStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfTrunkPortStatsGroup.setDescription('A collection of objects for statistics of a specified port of a trunk.')
hpicfLoadBalanceGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76, 2, 2, 5)).setObjects(("HP-LOADBALANCE-MIB", "hpicfLoadBalanceTrunkId"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceSourceMacAddr"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceDestMacAddr"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPSourceAddrType"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPSourceAddr"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPDestAddrType"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceIPDestAddr"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceSourcePort"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceDestPort"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceEtherType"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceInboundVlan"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceInboundPort"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceOutboundPort"), ("HP-LOADBALANCE-MIB", "hpicfLoadBalanceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLoadBalanceGroup5 = hpicfLoadBalanceGroup5.setStatus('current')
if mibBuilder.loadTexts: hpicfLoadBalanceGroup5.setDescription(' ')
mibBuilder.exportSymbols("HP-LOADBALANCE-MIB", hpicfTrunkStatsCompliance=hpicfTrunkStatsCompliance, hpicfTrunkPortFramesDropTx=hpicfTrunkPortFramesDropTx, hpicfTrunkLoadBalanceMethod=hpicfTrunkLoadBalanceMethod, hpicfLoadBalanceSourceMacAddr=hpicfLoadBalanceSourceMacAddr, hpicfLoadBalanceDestMacAddr=hpicfLoadBalanceDestMacAddr, hpicfTrunkPortStatsGroup=hpicfTrunkPortStatsGroup, hpicfLoadBalanceNotifications=hpicfLoadBalanceNotifications, hpicfLoadBalanceGroup5=hpicfLoadBalanceGroup5, hpicfLoadBalanceStatus=hpicfLoadBalanceStatus, hpicfLoadBalanceMethodMod=hpicfLoadBalanceMethodMod, hpicfTrunkTotalBytesTx=hpicfTrunkTotalBytesTx, hpicfLoadBalanceIPDestAddr=hpicfLoadBalanceIPDestAddr, hpicfTrunkStatsEntry=hpicfTrunkStatsEntry, hpicfLoadBalanceObjects=hpicfLoadBalanceObjects, hpicfTrunkTotalBytesRx=hpicfTrunkTotalBytesRx, hpicfLoadBalanceDestPort=hpicfLoadBalanceDestPort, hpicfLoadBalanceIndex=hpicfLoadBalanceIndex, hpicfTrunkPortBytesTx=hpicfTrunkPortBytesTx, hpicfTrunkStatsGroup=hpicfTrunkStatsGroup, hpicfLoadBalanceCompliance=hpicfLoadBalanceCompliance, hpicfLoadBalanceInboundVlan=hpicfLoadBalanceInboundVlan, hpicfLoadBalanceEntry=hpicfLoadBalanceEntry, hpicfTrunkPortDropTxFramePercent=hpicfTrunkPortDropTxFramePercent, hpicfLoadBalanceTable=hpicfLoadBalanceTable, hpicfLoadBalanceOutboundPort=hpicfLoadBalanceOutboundPort, hpicfTrunkTotalFramesTx=hpicfTrunkTotalFramesTx, hpicfTrunkUpTime=hpicfTrunkUpTime, hpicfTrunkStatsTable=hpicfTrunkStatsTable, hpicfTrunkStatsClear=hpicfTrunkStatsClear, hpicfTrunkPortFramesRx=hpicfTrunkPortFramesRx, hpicfTrunkTotalDropsTx=hpicfTrunkTotalDropsTx, hpicfTrunkStatsClearGroup=hpicfTrunkStatsClearGroup, hpicfTrunkPortTxFramePercent=hpicfTrunkPortTxFramePercent, hpicfLoadBalanceTrunkId=hpicfLoadBalanceTrunkId, hpicfLoadBalanceSourcePort=hpicfLoadBalanceSourcePort, hpicfLoadBalanceGroup=hpicfLoadBalanceGroup, hpicfTrunkPortBytesRx=hpicfTrunkPortBytesRx, hpicfLoadBalanceGroups=hpicfLoadBalanceGroups, hpicfLoadBalanceInboundPort=hpicfLoadBalanceInboundPort, hpicfTrunkPortStatsEntry=hpicfTrunkPortStatsEntry, hpicfLoadBalanceIPSourceAddrType=hpicfLoadBalanceIPSourceAddrType, hpicfTrunkClearStatsTable=hpicfTrunkClearStatsTable, hpicfLoadBalanceMod=hpicfLoadBalanceMod, PYSNMP_MODULE_ID=hpicfLoadBalanceMod, hpicfTrunkId=hpicfTrunkId, hpicfLoadBalanceIPSourceAddr=hpicfLoadBalanceIPSourceAddr, hpicfTrunkTotalFramesRx=hpicfTrunkTotalFramesRx, hpicfTrunkPortStatsTable=hpicfTrunkPortStatsTable, hpicfLoadBalanceEtherType=hpicfLoadBalanceEtherType, hpicfLoadBalanceIPDestAddrType=hpicfLoadBalanceIPDestAddrType, hpicfLoadBalanceConformance=hpicfLoadBalanceConformance, hpicfTrunkPortRxFramePercent=hpicfTrunkPortRxFramePercent, hpicfLoadBalanceCompliances=hpicfLoadBalanceCompliances, hpicfTrunkPortFramesTx=hpicfTrunkPortFramesTx, hpicfTrunkClearStatsEntry=hpicfTrunkClearStatsEntry)
