#
# PySNMP MIB module ASCEND-MIBCMMODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBCMMODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, IpAddress, MibIdentifier, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter32, Integer32, TimeTicks, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "IpAddress", "MibIdentifier", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter32", "Integer32", "TimeTicks", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibmodemProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 144))
mibmodemProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 144, 1), )
if mibBuilder.loadTexts: mibmodemProfileTable.setStatus('mandatory')
mibmodemProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1), ).setIndexNames((0, "ASCEND-MIBCMMODEM-MIB", "modemProfile-Shelf-o"), (0, "ASCEND-MIBCMMODEM-MIB", "modemProfile-Slot-o"), (0, "ASCEND-MIBCMMODEM-MIB", "modemProfile-Item-o"))
if mibBuilder.loadTexts: mibmodemProfileEntry.setStatus('mandatory')
modemProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 1), Integer32()).setLabel("modemProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: modemProfile_Shelf_o.setStatus('mandatory')
modemProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 2), Integer32()).setLabel("modemProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: modemProfile_Slot_o.setStatus('mandatory')
modemProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 3), Integer32()).setLabel("modemProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: modemProfile_Item_o.setStatus('mandatory')
modemProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("modemProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemProfile_PhysicalAddress_Shelf.setStatus('mandatory')
modemProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("modemProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemProfile_PhysicalAddress_Slot.setStatus('mandatory')
modemProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 6), Integer32()).setLabel("modemProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
modemProfile_AutoAnswer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("primaryOnly", 3)))).setLabel("modemProfile-AutoAnswer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemProfile_AutoAnswer.setStatus('mandatory')
modemProfile_CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 11, 16, 23, 28, 33, 39, 47, 50, 61, 62, 67, 71, 81, 82, 84, 88, 89, 90, 1, 98, 106, 109, 116, 124, 127, 131, 138, 139, 140, 185, 157, 160, 161, 166, 167, 255, 181, 182))).clone(namedValues=NamedValues(("australia", 10), ("austria", 11), ("belgium", 16), ("brazil", 23), ("bulgaria", 28), ("canada", 33), ("china", 39), ("czechslovak", 47), ("denmark", 50), ("finland", 61), ("france", 62), ("germany", 67), ("greece", 71), ("hongkong", 81), ("hungary", 82), ("india", 84), ("ireland", 88), ("israel", 89), ("italy", 90), ("japan", 1), ("korea", 98), ("luxembourg", 106), ("malaysia", 109), ("mexico", 116), ("netherlands", 124), ("newzealand", 127), ("norway", 131), ("philippines", 138), ("poland", 139), ("portugal", 140), ("russia", 185), ("singapore", 157), ("southafrica", 160), ("spain", 161), ("sweden", 166), ("switzerland", 167), ("taiwan", 255), ("unitedkingdom", 181), ("unitedstates", 182)))).setLabel("modemProfile-CountryCode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemProfile_CountryCode.setStatus('mandatory')
modemProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("modemProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBCMMODEM-MIB", mibmodemProfile=mibmodemProfile, modemProfile_PhysicalAddress_Shelf=modemProfile_PhysicalAddress_Shelf, DisplayString=DisplayString, mibmodemProfileTable=mibmodemProfileTable, modemProfile_PhysicalAddress_Slot=modemProfile_PhysicalAddress_Slot, modemProfile_CountryCode=modemProfile_CountryCode, mibmodemProfileEntry=mibmodemProfileEntry, modemProfile_PhysicalAddress_ItemNumber=modemProfile_PhysicalAddress_ItemNumber, modemProfile_Action_o=modemProfile_Action_o, modemProfile_AutoAnswer=modemProfile_AutoAnswer, modemProfile_Item_o=modemProfile_Item_o, modemProfile_Shelf_o=modemProfile_Shelf_o, modemProfile_Slot_o=modemProfile_Slot_o)
