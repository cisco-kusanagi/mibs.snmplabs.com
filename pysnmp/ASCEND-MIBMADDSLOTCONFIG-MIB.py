#
# PySNMP MIB module ASCEND-MIBMADDSLOTCONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBMADDSLOTCONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, iso, TimeTicks, IpAddress, Integer32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "iso", "TimeTicks", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibmaddSlotConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 163))
mibmaddSlotConfigTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 163, 1), )
if mibBuilder.loadTexts: mibmaddSlotConfigTable.setStatus('mandatory')
mibmaddSlotConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1), ).setIndexNames((0, "ASCEND-MIBMADDSLOTCONFIG-MIB", "maddSlotConfig-Shelf-o"), (0, "ASCEND-MIBMADDSLOTCONFIG-MIB", "maddSlotConfig-Slot-o"), (0, "ASCEND-MIBMADDSLOTCONFIG-MIB", "maddSlotConfig-Item-o"))
if mibBuilder.loadTexts: mibmaddSlotConfigEntry.setStatus('mandatory')
maddSlotConfig_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 1), Integer32()).setLabel("maddSlotConfig-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: maddSlotConfig_Shelf_o.setStatus('mandatory')
maddSlotConfig_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 2), Integer32()).setLabel("maddSlotConfig-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: maddSlotConfig_Slot_o.setStatus('mandatory')
maddSlotConfig_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 3), Integer32()).setLabel("maddSlotConfig-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: maddSlotConfig_Item_o.setStatus('mandatory')
maddSlotConfig_SlotAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("maddSlotConfig-SlotAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: maddSlotConfig_SlotAddress_Shelf.setStatus('mandatory')
maddSlotConfig_SlotAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("maddSlotConfig-SlotAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: maddSlotConfig_SlotAddress_Slot.setStatus('mandatory')
maddSlotConfig_SlotAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 6), Integer32()).setLabel("maddSlotConfig-SlotAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: maddSlotConfig_SlotAddress_ItemNumber.setStatus('mandatory')
maddSlotConfig_Subtype = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("n-288UnivPorts", 1), ("n-480VoipPorts", 2), ("n-192Ip2ipPorts", 3)))).setLabel("maddSlotConfig-Subtype").setMaxAccess("readwrite")
if mibBuilder.loadTexts: maddSlotConfig_Subtype.setStatus('mandatory')
maddSlotConfig_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("maddSlotConfig-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: maddSlotConfig_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBMADDSLOTCONFIG-MIB", maddSlotConfig_SlotAddress_ItemNumber=maddSlotConfig_SlotAddress_ItemNumber, maddSlotConfig_Slot_o=maddSlotConfig_Slot_o, mibmaddSlotConfigEntry=mibmaddSlotConfigEntry, maddSlotConfig_SlotAddress_Slot=maddSlotConfig_SlotAddress_Slot, DisplayString=DisplayString, mibmaddSlotConfig=mibmaddSlotConfig, maddSlotConfig_Action_o=maddSlotConfig_Action_o, maddSlotConfig_Shelf_o=maddSlotConfig_Shelf_o, maddSlotConfig_Item_o=maddSlotConfig_Item_o, maddSlotConfig_SlotAddress_Shelf=maddSlotConfig_SlotAddress_Shelf, mibmaddSlotConfigTable=mibmaddSlotConfigTable, maddSlotConfig_Subtype=maddSlotConfig_Subtype)
