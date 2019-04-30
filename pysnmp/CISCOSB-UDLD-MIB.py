#
# PySNMP MIB module CISCOSB-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-UDLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:08:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
switch001, rndNotifications = mibBuilder.importSymbols("CISCOSB-MIB", "switch001", "rndNotifications")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, Gauge32, iso, Counter32, Bits, IpAddress, ObjectIdentity, MibIdentifier, Integer32, Unsigned32, ModuleIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "iso", "Counter32", "Bits", "IpAddress", "ObjectIdentity", "MibIdentifier", "Integer32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
class UdldString(SnmpAdminString):
    status = 'current'

class UdldPortBidirectionalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("shutdown", 1), ("idle", 2), ("detection", 3), ("undetermined", 4), ("bidirectional", 5))

class UdldNeighborCurrentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("undefined", 3), ("bidirectional", 4))

class UdldGlobalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3))

class UdldPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3), ("default", 4))

rlUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218))
rlUdld.setRevisions(('2012-08-01 00:00',))
if mibBuilder.loadTexts: rlUdld.setLastUpdated('201208010000Z')
if mibBuilder.loadTexts: rlUdld.setOrganization('CISCOSB Computer Communications Ltd.')
rlUdldPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1), )
if mibBuilder.loadTexts: rlUdldPortTable.setStatus('current')
rlUdldPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1), ).setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldPortIfIndex"))
if mibBuilder.loadTexts: rlUdldPortEntry.setStatus('current')
rlUdldPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldPortIfIndex.setStatus('current')
rlUdldPortAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 2), UdldPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldPortAdminMode.setStatus('current')
rlUdldPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 3), UdldPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortOperMode.setStatus('current')
rlUdldPortDefaultConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortDefaultConfiguration.setStatus('current')
rlUdldBidirectionalState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 5), UdldPortBidirectionalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldBidirectionalState.setStatus('current')
rlUdldNumberOfDetectedNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNumberOfDetectedNeighbors.setStatus('current')
rlUdldNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2), )
if mibBuilder.loadTexts: rlUdldNeighborTable.setStatus('current')
rlUdldNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1), ).setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortIfIndex"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborDeviceID"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortID"))
if mibBuilder.loadTexts: rlUdldNeighborEntry.setStatus('current')
rlUdldNeighborPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldNeighborPortIfIndex.setStatus('current')
rlUdldNeighborDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 2), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborDeviceID.setStatus('current')
rlUdldNeighborPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 3), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborPortID.setStatus('current')
rlUdldNeighborDeviceMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 4), MacAddress())
if mibBuilder.loadTexts: rlUdldNeighborDeviceMACAddress.setStatus('current')
rlUdldNeighborDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 5), UdldString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborDeviceName.setStatus('current')
rlUdldNeighborMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborMessageTime.setStatus('current')
rlUdldNeighborLeftLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborLeftLifeTime.setStatus('current')
rlUdldNeighborCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 8), UdldNeighborCurrentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborCurrentState.setStatus('current')
rlUdldGlobalUDLDMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 3), UdldGlobalMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalUDLDMode.setStatus('current')
rlUdldGlobalMessageTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalMessageTime.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-UDLD-MIB", rlUdldPortIfIndex=rlUdldPortIfIndex, UdldPortMode=UdldPortMode, rlUdldNeighborEntry=rlUdldNeighborEntry, rlUdldNeighborPortID=rlUdldNeighborPortID, rlUdldNeighborCurrentState=rlUdldNeighborCurrentState, rlUdldNeighborMessageTime=rlUdldNeighborMessageTime, rlUdld=rlUdld, UdldPortBidirectionalState=UdldPortBidirectionalState, PYSNMP_MODULE_ID=rlUdld, rlUdldPortOperMode=rlUdldPortOperMode, rlUdldPortTable=rlUdldPortTable, rlUdldNeighborLeftLifeTime=rlUdldNeighborLeftLifeTime, rlUdldNeighborDeviceID=rlUdldNeighborDeviceID, rlUdldNumberOfDetectedNeighbors=rlUdldNumberOfDetectedNeighbors, rlUdldPortEntry=rlUdldPortEntry, UdldString=UdldString, rlUdldNeighborDeviceName=rlUdldNeighborDeviceName, rlUdldPortDefaultConfiguration=rlUdldPortDefaultConfiguration, rlUdldPortAdminMode=rlUdldPortAdminMode, rlUdldBidirectionalState=rlUdldBidirectionalState, rlUdldGlobalUDLDMode=rlUdldGlobalUDLDMode, rlUdldNeighborTable=rlUdldNeighborTable, rlUdldNeighborDeviceMACAddress=rlUdldNeighborDeviceMACAddress, rlUdldGlobalMessageTime=rlUdldGlobalMessageTime, UdldGlobalMode=UdldGlobalMode, rlUdldNeighborPortIfIndex=rlUdldNeighborPortIfIndex, UdldNeighborCurrentState=UdldNeighborCurrentState)
