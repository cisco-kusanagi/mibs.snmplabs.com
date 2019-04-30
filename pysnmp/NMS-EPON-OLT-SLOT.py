#
# PySNMP MIB module NMS-EPON-OLT-SLOT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-OLT-SLOT
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter32, ObjectIdentity, TimeTicks, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Gauge32, Unsigned32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter32", "ObjectIdentity", "TimeTicks", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
nmsEponOltSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21))
nmsEponOltSlotTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1), )
if mibBuilder.loadTexts: nmsEponOltSlotTable.setStatus('mandatory')
nmsEponOltSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1), ).setIndexNames((0, "NMS-EPON-OLT-SLOT", "oltSlotIndex"))
if mibBuilder.loadTexts: nmsEponOltSlotEntry.setStatus('mandatory')
oltSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotIndex.setStatus('mandatory')
oltSlotHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotHelloInterval.setStatus('mandatory')
oltSlotDeadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotDeadInterval.setStatus('mandatory')
oltSlotChipsRegisteredNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotChipsRegisteredNumber.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-OLT-SLOT", oltSlotDeadInterval=oltSlotDeadInterval, oltSlotChipsRegisteredNumber=oltSlotChipsRegisteredNumber, nmsEponOltSlot=nmsEponOltSlot, oltSlotIndex=oltSlotIndex, nmsEponOltSlotTable=nmsEponOltSlotTable, oltSlotHelloInterval=oltSlotHelloInterval, nmsEponOltSlotEntry=nmsEponOltSlotEntry)
