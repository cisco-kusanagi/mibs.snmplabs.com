#
# PySNMP MIB module TPT-BAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-BAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, NotificationType, Bits, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, iso, Counter64, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "NotificationType", "Bits", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "iso", "Counter64", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_tpa_eventsV2, tpt_tpa_unkparams, tpt_tpa_objs = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-eventsV2", "tpt-tpa-unkparams", "tpt-tpa-objs")
tpt_slot_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17)).setLabel("tpt-slot-objs")
tpt_slot_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_slot_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_slot_objs.setOrganization('Trend Micro, Inc.')
class SlotStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("empty", 0), ("active", 1), ("error", 2))

class SlotEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("insert", 0), ("remove", 1))

class SlotModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("type-12-port-1g-copper", 1), ("type-12-port-1g-sfp", 2), ("type-8-port-10g-sfp", 3), ("type-2-port-40g-sfp", 4), ("type-6100", 5), ("type-5100", 6), ("type-2500", 7), ("type-1400", 8), ("type-660", 9), ("type-330", 10), ("type-110", 11), ("type-10", 12), ("type-empty", 13), ("type-8-port-1g-copper-bypass", 14), ("type-4-port-1g-sfp-sr-bypass", 15), ("type-4-port-1g-sfp-lr-bypass", 16), ("type-4-port-10g-sfp-sr-bypass", 17), ("type-4-port-10g-sfp-lr-bypass", 18))

slotTempTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1), )
if mibBuilder.loadTexts: slotTempTable.setStatus('current')
slotTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1), ).setIndexNames((0, "TPT-BAY-MIB", "slotTempIndex"))
if mibBuilder.loadTexts: slotTempEntry.setStatus('current')
slotTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: slotTempIndex.setStatus('current')
slotName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotName.setStatus('current')
slotModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleName.setStatus('current')
slotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 4), SlotStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotStatus.setStatus('current')
slotModuleSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleSerialNum.setStatus('current')
slotModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 6), SlotModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleType.setStatus('current')
tptSlotDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 281), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotDeviceID.setStatus('current')
tptSlotID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 282), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotID.setStatus('current')
tptSlotEvent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 283), SlotEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotEvent.setStatus('current')
tptSlotChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 54)).setObjects(("TPT-BAY-MIB", "tptSlotDeviceID"), ("TPT-BAY-MIB", "tptSlotID"), ("TPT-BAY-MIB", "tptSlotEvent"))
if mibBuilder.loadTexts: tptSlotChangeNotify.setStatus('current')
mibBuilder.exportSymbols("TPT-BAY-MIB", SlotModuleType=SlotModuleType, slotName=slotName, slotModuleType=slotModuleType, tptSlotID=tptSlotID, slotTempIndex=slotTempIndex, SlotStatus=SlotStatus, tptSlotEvent=tptSlotEvent, slotModuleName=slotModuleName, tptSlotChangeNotify=tptSlotChangeNotify, slotTempEntry=slotTempEntry, slotTempTable=slotTempTable, SlotEvent=SlotEvent, slotStatus=slotStatus, slotModuleSerialNum=slotModuleSerialNum, tptSlotDeviceID=tptSlotDeviceID, PYSNMP_MODULE_ID=tpt_slot_objs, tpt_slot_objs=tpt_slot_objs)
