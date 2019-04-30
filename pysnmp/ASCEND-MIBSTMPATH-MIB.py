#
# PySNMP MIB module ASCEND-MIBSTMPATH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSTMPATH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, TimeTicks, Integer32, ObjectIdentity, Unsigned32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "TimeTicks", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibsTMPathProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 155))
mibsTMPathProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 155, 1), )
if mibBuilder.loadTexts: mibsTMPathProfileTable.setStatus('mandatory')
mibsTMPathProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1), ).setIndexNames((0, "ASCEND-MIBSTMPATH-MIB", "sTMPathProfile-Shelf-o"), (0, "ASCEND-MIBSTMPATH-MIB", "sTMPathProfile-Slot-o"), (0, "ASCEND-MIBSTMPATH-MIB", "sTMPathProfile-Item-o"))
if mibBuilder.loadTexts: mibsTMPathProfileEntry.setStatus('mandatory')
sTMPathProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 1), Integer32()).setLabel("sTMPathProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: sTMPathProfile_Shelf_o.setStatus('mandatory')
sTMPathProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 2), Integer32()).setLabel("sTMPathProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: sTMPathProfile_Slot_o.setStatus('mandatory')
sTMPathProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 3), Integer32()).setLabel("sTMPathProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: sTMPathProfile_Item_o.setStatus('mandatory')
sTMPathProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 4), DisplayString()).setLabel("sTMPathProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_Name.setStatus('mandatory')
sTMPathProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("sTMPathProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_PhysicalAddress_Shelf.setStatus('mandatory')
sTMPathProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("sTMPathProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_PhysicalAddress_Slot.setStatus('mandatory')
sTMPathProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 7), Integer32()).setLabel("sTMPathProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
sTMPathProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sTMPathProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_Enabled.setStatus('mandatory')
sTMPathProfile_TributaryMapping = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 5, 6, 8))).clone(namedValues=NamedValues(("vc11AsyncMapping", 2), ("vc11ByteSyncMapping", 3), ("vc12AsyncMapping", 5), ("vc12ByteSyncMapping", 6), ("vc3AsyncMapping", 8)))).setLabel("sTMPathProfile-TributaryMapping").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_TributaryMapping.setStatus('mandatory')
sTMPathProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 155, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("sTMPathProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sTMPathProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSTMPATH-MIB", mibsTMPathProfileTable=mibsTMPathProfileTable, sTMPathProfile_Enabled=sTMPathProfile_Enabled, DisplayString=DisplayString, sTMPathProfile_PhysicalAddress_Shelf=sTMPathProfile_PhysicalAddress_Shelf, sTMPathProfile_TributaryMapping=sTMPathProfile_TributaryMapping, sTMPathProfile_Item_o=sTMPathProfile_Item_o, mibsTMPathProfile=mibsTMPathProfile, sTMPathProfile_Slot_o=sTMPathProfile_Slot_o, sTMPathProfile_Shelf_o=sTMPathProfile_Shelf_o, sTMPathProfile_PhysicalAddress_Slot=sTMPathProfile_PhysicalAddress_Slot, mibsTMPathProfileEntry=mibsTMPathProfileEntry, sTMPathProfile_Action_o=sTMPathProfile_Action_o, sTMPathProfile_PhysicalAddress_ItemNumber=sTMPathProfile_PhysicalAddress_ItemNumber, sTMPathProfile_Name=sTMPathProfile_Name)
