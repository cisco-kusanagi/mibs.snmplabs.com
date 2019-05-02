#
# PySNMP MIB module NMS-EPON-OLT-SLOT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-OLT-SLOT
# Produced by pysmi-0.3.4 at Wed May  1 14:21:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, Unsigned32, TimeTicks, NotificationType, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, Integer32, Counter64, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Unsigned32", "TimeTicks", "NotificationType", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "Counter64", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
nmsEponOltSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21))
nmsEponOltSlotTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1), )
if mibBuilder.loadTexts: nmsEponOltSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponOltSlotTable.setDescription('A list of epon Olt slot table entries.')
nmsEponOltSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1), ).setIndexNames((0, "NMS-EPON-OLT-SLOT", "oltSlotIndex"))
if mibBuilder.loadTexts: nmsEponOltSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponOltSlotEntry.setDescription('A collection of additional objects in the epon Olt slot table.')
oltSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: oltSlotIndex.setDescription('Slot index, which is the same value as nmscardIfCardIndex in nmscardIfIndexTable.')
oltSlotHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotHelloInterval.setStatus('mandatory')
if mibBuilder.loadTexts: oltSlotHelloInterval.setDescription('Package sending interval between OLT chip and card CPU.')
oltSlotDeadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotDeadInterval.setStatus('mandatory')
if mibBuilder.loadTexts: oltSlotDeadInterval.setDescription('Package timeout interval between OLT chip and card CPU.')
oltSlotChipsRegisteredNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltSlotChipsRegisteredNumber.setStatus('mandatory')
if mibBuilder.loadTexts: oltSlotChipsRegisteredNumber.setDescription('Number of registered OLT chips.')
mibBuilder.exportSymbols("NMS-EPON-OLT-SLOT", nmsEponOltSlot=nmsEponOltSlot, nmsEponOltSlotTable=nmsEponOltSlotTable, nmsEponOltSlotEntry=nmsEponOltSlotEntry, oltSlotHelloInterval=oltSlotHelloInterval, oltSlotDeadInterval=oltSlotDeadInterval, oltSlotIndex=oltSlotIndex, oltSlotChipsRegisteredNumber=oltSlotChipsRegisteredNumber)
