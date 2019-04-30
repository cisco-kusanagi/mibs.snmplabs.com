#
# PySNMP MIB module RADLAN-rlInventoryEnt-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-rlInventoryEnt-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:42:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Counter64, Bits, Counter32, ModuleIdentity, IpAddress, iso, TimeTicks, Gauge32, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Counter64", "Bits", "Counter32", "ModuleIdentity", "IpAddress", "iso", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class UnitIfindexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unit", 0), ("ifindex", 1))

rlInventoryEntTable = MibTable((1, 3, 6, 1, 4, 1, 89, 217), )
if mibBuilder.loadTexts: rlInventoryEntTable.setStatus('current')
rlInventoryEntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 217, 1), ).setIndexNames((0, "RADLAN-rlInventoryEnt-MIB", "rlInventoryEntUnitOrIfindex"), (0, "RADLAN-rlInventoryEnt-MIB", "rlInventoryEntUnitIfindexID"))
if mibBuilder.loadTexts: rlInventoryEntEntry.setStatus('current')
rlInventoryEntUnitOrIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 1), UnitIfindexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setStatus('current')
rlInventoryEntUnitIfindexID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setStatus('current')
rlInventoryEntVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntVendorID.setStatus('current')
rlInventoryEntPID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntPID.setStatus('current')
rlInventoryEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntName.setStatus('current')
rlInventoryEntDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntDescription.setStatus('current')
rlInventoryEntSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setStatus('current')
rlInventoryEntUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setStatus('current')
mibBuilder.exportSymbols("RADLAN-rlInventoryEnt-MIB", rlInventoryEntName=rlInventoryEntName, rlInventoryEntUnitOrIfindex=rlInventoryEntUnitOrIfindex, rlInventoryEntUnitNum=rlInventoryEntUnitNum, rlInventoryEntEntry=rlInventoryEntEntry, rlInventoryEntUnitIfindexID=rlInventoryEntUnitIfindexID, rlInventoryEntVendorID=rlInventoryEntVendorID, rlInventoryEntPID=rlInventoryEntPID, UnitIfindexType=UnitIfindexType, rlInventoryEntTable=rlInventoryEntTable, rlInventoryEntDescription=rlInventoryEntDescription, rlInventoryEntSerialNumber=rlInventoryEntSerialNumber)
