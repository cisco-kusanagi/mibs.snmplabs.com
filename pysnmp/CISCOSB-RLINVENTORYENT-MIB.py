#
# PySNMP MIB module CISCOSB-RLINVENTORYENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-RLINVENTORYENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, ModuleIdentity, IpAddress, ObjectIdentity, MibIdentifier, iso, TimeTicks, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibIdentifier", "iso", "TimeTicks", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class UnitIfindexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unit", 0), ("ifindex", 1))

rlInventoryEntTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217), )
if mibBuilder.loadTexts: rlInventoryEntTable.setStatus('current')
rlInventoryEntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1), ).setIndexNames((0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitOrIfindex"), (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitIfindexID"))
if mibBuilder.loadTexts: rlInventoryEntEntry.setStatus('current')
rlInventoryEntUnitOrIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 1), UnitIfindexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setStatus('current')
rlInventoryEntUnitIfindexID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setStatus('current')
rlInventoryEntVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntVendorID.setStatus('current')
rlInventoryEntPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntPID.setStatus('current')
rlInventoryEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntName.setStatus('current')
rlInventoryEntDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntDescription.setStatus('current')
rlInventoryEntSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setStatus('current')
rlInventoryEntUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-RLINVENTORYENT-MIB", UnitIfindexType=UnitIfindexType, rlInventoryEntUnitOrIfindex=rlInventoryEntUnitOrIfindex, rlInventoryEntPID=rlInventoryEntPID, rlInventoryEntName=rlInventoryEntName, rlInventoryEntVendorID=rlInventoryEntVendorID, rlInventoryEntDescription=rlInventoryEntDescription, rlInventoryEntTable=rlInventoryEntTable, rlInventoryEntSerialNumber=rlInventoryEntSerialNumber, rlInventoryEntUnitIfindexID=rlInventoryEntUnitIfindexID, rlInventoryEntUnitNum=rlInventoryEntUnitNum, rlInventoryEntEntry=rlInventoryEntEntry)
