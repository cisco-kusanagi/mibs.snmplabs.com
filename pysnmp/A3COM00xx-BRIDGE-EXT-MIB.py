#
# PySNMP MIB module A3COM00xx-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM00xx-BRIDGE-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
a3ComBridgeExt, = mibBuilder.importSymbols("A3COM0004-GENERIC", "a3ComBridgeExt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
Timeout, dot1dBasePort, MacAddress = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "dot1dBasePort", "MacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, iso, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "iso", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PortList(OctetString):
    pass

a3ComDot1dExtended = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1))
a3ComDot1qVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 2))
a3ComDot1dExtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1))
a3ComDot1dGarp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2))
a3ComPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3))
a3ComNeighbour = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4))
a3ComDot1dGmrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDot1dGmrpAdminStatus.setStatus('mandatory')
a3ComDot1dGvrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDot1dGvrpAdminStatus.setStatus('mandatory')
a3ComGarpJoinTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 3), Timeout()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComGarpJoinTime.setStatus('mandatory')
a3ComGarpLeaveTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 4), Timeout()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComGarpLeaveTime.setStatus('mandatory')
a3ComGarpLeaveAllTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 5), Timeout()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComGarpLeaveAllTime.setStatus('mandatory')
a3ComSingleFdbStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComSingleFdbStatus.setStatus('mandatory')
a3ComPortGarpTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1), )
if mibBuilder.loadTexts: a3ComPortGarpTable.setStatus('mandatory')
a3ComPortGarpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: a3ComPortGarpEntry.setStatus('mandatory')
a3ComPortGmrpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("useDefault", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortGmrpAdminStatus.setStatus('mandatory')
a3ComPortGmrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortGmrpOperStatus.setStatus('mandatory')
a3ComPortGvrpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("useDefault", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortGvrpAdminStatus.setStatus('mandatory')
a3ComPortGvrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortGvrpOperStatus.setStatus('mandatory')
a3ComBridgePriorityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1), )
if mibBuilder.loadTexts: a3ComBridgePriorityTable.setStatus('mandatory')
a3ComBridgePriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1), ).setIndexNames((0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComUserPriority"))
if mibBuilder.loadTexts: a3ComBridgePriorityEntry.setStatus('mandatory')
a3ComUserPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: a3ComUserPriority.setStatus('mandatory')
a3ComBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBridgePriority.setStatus('mandatory')
a3ComPortNeighbourTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1), )
if mibBuilder.loadTexts: a3ComPortNeighbourTable.setStatus('mandatory')
a3ComPortNeighbourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: a3ComPortNeighbourEntry.setStatus('mandatory')
a3ComPortForwardUnknownVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortForwardUnknownVlans.setStatus('mandatory')
a3ComDot1qVlanStaticTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1), )
if mibBuilder.loadTexts: a3ComDot1qVlanStaticTable.setStatus('mandatory')
a3ComDot1qVlanStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1), ).setIndexNames((0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qVlanId"))
if mibBuilder.loadTexts: a3ComDot1qVlanStaticEntry.setStatus('mandatory')
a3ComDot1qVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: a3ComDot1qVlanId.setStatus('mandatory')
a3ComDot1qVlanForbiddenPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDot1qVlanForbiddenPorts.setStatus('mandatory')
a3ComDot1qTpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2), )
if mibBuilder.loadTexts: a3ComDot1qTpGroupTable.setStatus('mandatory')
a3ComDot1qTpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1), ).setIndexNames((0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qVlanId"), (0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qTpGroupAddress"))
if mibBuilder.loadTexts: a3ComDot1qTpGroupEntry.setStatus('mandatory')
a3ComDot1qTpGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: a3ComDot1qTpGroupAddress.setStatus('mandatory')
a3ComDot1qTpGroupAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDot1qTpGroupAllowedToGoTo.setStatus('mandatory')
a3ComDot1qTpGroupGmrp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDot1qTpGroupGmrp.setStatus('mandatory')
a3ComDot1qTpGroupIgmp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDot1qTpGroupIgmp.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM00xx-BRIDGE-EXT-MIB", a3ComGarpLeaveTime=a3ComGarpLeaveTime, a3ComBridgePriorityTable=a3ComBridgePriorityTable, a3ComDot1qTpGroupIgmp=a3ComDot1qTpGroupIgmp, a3ComGarpJoinTime=a3ComGarpJoinTime, a3ComDot1qTpGroupEntry=a3ComDot1qTpGroupEntry, a3ComDot1dGarp=a3ComDot1dGarp, a3ComPortGvrpAdminStatus=a3ComPortGvrpAdminStatus, PortList=PortList, a3ComPortGmrpAdminStatus=a3ComPortGmrpAdminStatus, a3ComPortNeighbourEntry=a3ComPortNeighbourEntry, a3ComPriority=a3ComPriority, a3ComBridgePriority=a3ComBridgePriority, a3ComDot1qTpGroupAddress=a3ComDot1qTpGroupAddress, a3ComDot1qTpGroupGmrp=a3ComDot1qTpGroupGmrp, a3ComPortGvrpOperStatus=a3ComPortGvrpOperStatus, a3ComBridgePriorityEntry=a3ComBridgePriorityEntry, a3ComDot1qVlan=a3ComDot1qVlan, a3ComUserPriority=a3ComUserPriority, a3ComDot1dExtended=a3ComDot1dExtended, a3ComDot1qVlanForbiddenPorts=a3ComDot1qVlanForbiddenPorts, a3ComDot1dExtBase=a3ComDot1dExtBase, a3ComGarpLeaveAllTime=a3ComGarpLeaveAllTime, a3ComDot1qVlanStaticTable=a3ComDot1qVlanStaticTable, a3ComDot1dGmrpAdminStatus=a3ComDot1dGmrpAdminStatus, a3ComDot1qTpGroupAllowedToGoTo=a3ComDot1qTpGroupAllowedToGoTo, a3ComPortNeighbourTable=a3ComPortNeighbourTable, a3ComPortGmrpOperStatus=a3ComPortGmrpOperStatus, a3ComNeighbour=a3ComNeighbour, a3ComDot1qVlanStaticEntry=a3ComDot1qVlanStaticEntry, a3ComPortForwardUnknownVlans=a3ComPortForwardUnknownVlans, a3ComPortGarpTable=a3ComPortGarpTable, a3ComPortGarpEntry=a3ComPortGarpEntry, a3ComDot1qVlanId=a3ComDot1qVlanId, a3ComDot1qTpGroupTable=a3ComDot1qTpGroupTable, a3ComSingleFdbStatus=a3ComSingleFdbStatus, a3ComDot1dGvrpAdminStatus=a3ComDot1dGvrpAdminStatus)