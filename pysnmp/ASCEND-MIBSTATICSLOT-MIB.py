#
# PySNMP MIB module ASCEND-MIBSTATICSLOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSTATICSLOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, ObjectIdentity, Unsigned32, Counter64, TimeTicks, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Counter64", "TimeTicks", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibmibProfSlotStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 31))
mibmibProfSlotStaticTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 31, 1), )
if mibBuilder.loadTexts: mibmibProfSlotStaticTable.setStatus('mandatory')
mibmibProfSlotStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1), ).setIndexNames((0, "ASCEND-MIBSTATICSLOT-MIB", "mibProfSlotStatic-Shelf-o"), (0, "ASCEND-MIBSTATICSLOT-MIB", "mibProfSlotStatic-Slot-o"), (0, "ASCEND-MIBSTATICSLOT-MIB", "mibProfSlotStatic-Item-o"))
if mibBuilder.loadTexts: mibmibProfSlotStaticEntry.setStatus('mandatory')
mibProfSlotStatic_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 1), Integer32()).setLabel("mibProfSlotStatic-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfSlotStatic_Shelf_o.setStatus('mandatory')
mibProfSlotStatic_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 2), Integer32()).setLabel("mibProfSlotStatic-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfSlotStatic_Slot_o.setStatus('mandatory')
mibProfSlotStatic_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 3), Integer32()).setLabel("mibProfSlotStatic-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfSlotStatic_Item_o.setStatus('mandatory')
mibProfSlotStatic_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 4), DisplayString()).setLabel("mibProfSlotStatic-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_Name.setStatus('mandatory')
mibProfSlotStatic_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("mibProfSlotStatic-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_PhysicalAddress_Shelf.setStatus('mandatory')
mibProfSlotStatic_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("mibProfSlotStatic-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_PhysicalAddress_Slot.setStatus('mandatory')
mibProfSlotStatic_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 7), Integer32()).setLabel("mibProfSlotStatic-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_PhysicalAddress_ItemNumber.setStatus('mandatory')
mibProfSlotStatic_AtmParameters_IncomingPriority = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lowPriority", 1), ("highPriority", 2)))).setLabel("mibProfSlotStatic-AtmParameters-IncomingPriority").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_AtmParameters_IncomingPriority.setStatus('mandatory')
mibProfSlotStatic_InterfaceType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("gShdsl", 2), ("hdsl2", 3)))).setLabel("mibProfSlotStatic-InterfaceType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_InterfaceType.setStatus('mandatory')
mibProfSlotStatic_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 31, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfSlotStatic-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfSlotStatic_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSTATICSLOT-MIB", mibProfSlotStatic_AtmParameters_IncomingPriority=mibProfSlotStatic_AtmParameters_IncomingPriority, mibProfSlotStatic_InterfaceType=mibProfSlotStatic_InterfaceType, mibProfSlotStatic_Action_o=mibProfSlotStatic_Action_o, mibProfSlotStatic_PhysicalAddress_Shelf=mibProfSlotStatic_PhysicalAddress_Shelf, mibProfSlotStatic_Item_o=mibProfSlotStatic_Item_o, mibmibProfSlotStatic=mibmibProfSlotStatic, mibProfSlotStatic_Shelf_o=mibProfSlotStatic_Shelf_o, mibProfSlotStatic_PhysicalAddress_ItemNumber=mibProfSlotStatic_PhysicalAddress_ItemNumber, mibProfSlotStatic_Name=mibProfSlotStatic_Name, mibmibProfSlotStaticEntry=mibmibProfSlotStaticEntry, mibProfSlotStatic_Slot_o=mibProfSlotStatic_Slot_o, mibmibProfSlotStaticTable=mibmibProfSlotStaticTable, mibProfSlotStatic_PhysicalAddress_Slot=mibProfSlotStatic_PhysicalAddress_Slot, DisplayString=DisplayString)
