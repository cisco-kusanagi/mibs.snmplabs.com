#
# PySNMP MIB module DNOS-MVR-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-MVR-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, NotificationType, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, ModuleIdentity, Bits, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "NotificationType", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "ModuleIdentity", "Bits", "Unsigned32", "iso")
RowStatus, TimeInterval, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeInterval", "DisplayString", "TextualConvention", "TruthValue")
fastpathMvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50))
fastpathMvr.setRevisions(('2011-01-26 00:00', '2009-10-21 00:00',))
if mibBuilder.loadTexts: fastpathMvr.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastpathMvr.setOrganization('Dell, Inc.')
mvrGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1))
mvrAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrAdminMode.setStatus('current')
mvrModeType = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("compatible", 1), ("dynamic", 2))).clone('compatible')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrModeType.setStatus('current')
mvrMulticastVlanId = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 3), VlanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrMulticastVlanId.setStatus('current')
mvrMaxMulticastGroupsCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrMaxMulticastGroupsCount.setStatus('current')
mvrCurrentMulticastGroupsCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrCurrentMulticastGroupsCount.setStatus('current')
mvrQueryTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 6), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrQueryTime.setStatus('current')
mvrPortTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2), )
if mibBuilder.loadTexts: mvrPortTable.setStatus('current')
mvrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mvrPortEntry.setStatus('current')
mvrPortMvrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrPortMvrEnabled.setStatus('current')
mvrPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source", 1), ("receiver", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrPortType.setStatus('current')
mvrPortImmediateLeaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrPortImmediateLeaveMode.setStatus('current')
mvrPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("activeInVlan", 1), ("activeNotInVlan", 2), ("inactiveInVlan", 3), ("inactiveNotInVlan", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrPortStatus.setStatus('current')
mvrGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3), )
if mibBuilder.loadTexts: mvrGroupsTable.setStatus('current')
mvrGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1), ).setIndexNames((0, "DNOS-MVR-PRIVATE-MIB", "mvrGroupIPAddress"))
if mibBuilder.loadTexts: mvrGroupEntry.setStatus('current')
mvrGroupIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrGroupIPAddress.setStatus('current')
mvrGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrGroupStatus.setStatus('current')
mvrGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrGroupRowStatus.setStatus('current')
mvrPortMembershipTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4), )
if mibBuilder.loadTexts: mvrPortMembershipTable.setStatus('current')
mvrPortMembershipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1), ).setIndexNames((0, "DNOS-MVR-PRIVATE-MIB", "mvrPortMembershipGroupIPAddress"), (0, "DNOS-MVR-PRIVATE-MIB", "mvrPortMembershipPortIfIndex"))
if mibBuilder.loadTexts: mvrPortMembershipEntry.setStatus('current')
mvrPortMembershipGroupIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrPortMembershipGroupIPAddress.setStatus('current')
mvrPortMembershipPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrPortMembershipPortIfIndex.setStatus('current')
mvrPortMembershipRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrPortMembershipRowStatus.setStatus('current')
mvrStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5))
mvrIGMPQueryReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPQueryReceived.setStatus('current')
mvrIGMPReportV1Received = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV1Received.setStatus('current')
mvrIGMPReportV2Received = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV2Received.setStatus('current')
mvrIGMPLeaveReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPLeaveReceived.setStatus('current')
mvrIGMPQueryTransmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPQueryTransmitted.setStatus('current')
mvrIGMPReportV1Transmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV1Transmitted.setStatus('current')
mvrIGMPReportV2Transmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV2Transmitted.setStatus('current')
mvrIGMPLeaveTransmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPLeaveTransmitted.setStatus('current')
mvrIGMPPacketReceiveFailures = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPPacketReceiveFailures.setStatus('current')
mvrIGMPPacketTransmitFailures = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPPacketTransmitFailures.setStatus('current')
mibBuilder.exportSymbols("DNOS-MVR-PRIVATE-MIB", PYSNMP_MODULE_ID=fastpathMvr, mvrGroupRowStatus=mvrGroupRowStatus, mvrIGMPPacketReceiveFailures=mvrIGMPPacketReceiveFailures, mvrPortMembershipRowStatus=mvrPortMembershipRowStatus, mvrGlobalConfig=mvrGlobalConfig, mvrIGMPReportV2Transmitted=mvrIGMPReportV2Transmitted, mvrIGMPReportV1Transmitted=mvrIGMPReportV1Transmitted, mvrCurrentMulticastGroupsCount=mvrCurrentMulticastGroupsCount, mvrPortStatus=mvrPortStatus, mvrPortMembershipGroupIPAddress=mvrPortMembershipGroupIPAddress, mvrGroupEntry=mvrGroupEntry, mvrPortMvrEnabled=mvrPortMvrEnabled, mvrMaxMulticastGroupsCount=mvrMaxMulticastGroupsCount, mvrModeType=mvrModeType, mvrIGMPPacketTransmitFailures=mvrIGMPPacketTransmitFailures, mvrQueryTime=mvrQueryTime, mvrIGMPReportV1Received=mvrIGMPReportV1Received, mvrPortEntry=mvrPortEntry, mvrIGMPLeaveTransmitted=mvrIGMPLeaveTransmitted, mvrPortMembershipPortIfIndex=mvrPortMembershipPortIfIndex, mvrIGMPReportV2Received=mvrIGMPReportV2Received, mvrGroupsTable=mvrGroupsTable, mvrGroupIPAddress=mvrGroupIPAddress, mvrPortType=mvrPortType, mvrPortMembershipEntry=mvrPortMembershipEntry, mvrIGMPQueryTransmitted=mvrIGMPQueryTransmitted, mvrGroupStatus=mvrGroupStatus, mvrPortTable=mvrPortTable, mvrPortImmediateLeaveMode=mvrPortImmediateLeaveMode, mvrStatistics=mvrStatistics, mvrIGMPQueryReceived=mvrIGMPQueryReceived, mvrIGMPLeaveReceived=mvrIGMPLeaveReceived, mvrAdminMode=mvrAdminMode, fastpathMvr=fastpathMvr, mvrMulticastVlanId=mvrMulticastVlanId, mvrPortMembershipTable=mvrPortMembershipTable)