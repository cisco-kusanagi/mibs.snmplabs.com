#
# PySNMP MIB module ASCEND-MIBLINEDIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBLINEDIAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, Integer32, Bits, TimeTicks, Counter64, ObjectIdentity, Counter32, IpAddress, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "Integer32", "Bits", "TimeTicks", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibmibProfLineDiag = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 145))
mibmibProfLineDiagTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 145, 1), )
if mibBuilder.loadTexts: mibmibProfLineDiagTable.setStatus('mandatory')
mibmibProfLineDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1), ).setIndexNames((0, "ASCEND-MIBLINEDIAG-MIB", "mibProfLineDiag-Shelf-o"), (0, "ASCEND-MIBLINEDIAG-MIB", "mibProfLineDiag-Slot-o"), (0, "ASCEND-MIBLINEDIAG-MIB", "mibProfLineDiag-Item-o"))
if mibBuilder.loadTexts: mibmibProfLineDiagEntry.setStatus('mandatory')
mibProfLineDiag_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 1), Integer32()).setLabel("mibProfLineDiag-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfLineDiag_Shelf_o.setStatus('mandatory')
mibProfLineDiag_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 2), Integer32()).setLabel("mibProfLineDiag-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfLineDiag_Slot_o.setStatus('mandatory')
mibProfLineDiag_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 3), Integer32()).setLabel("mibProfLineDiag-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfLineDiag_Item_o.setStatus('mandatory')
mibProfLineDiag_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("mibProfLineDiag-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_PhysicalAddress_Shelf.setStatus('mandatory')
mibProfLineDiag_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("mibProfLineDiag-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_PhysicalAddress_Slot.setStatus('mandatory')
mibProfLineDiag_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 6), Integer32()).setLabel("mibProfLineDiag-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_PhysicalAddress_ItemNumber.setStatus('mandatory')
mibProfLineDiag_BertTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(60001, 120001, 180001, 240001, 300001, 600001, 900001, 1200001, 1800001))).clone(namedValues=NamedValues(("n-1Minute", 60001), ("n-2Minutes", 120001), ("n-3Minutes", 180001), ("n-4Minutes", 240001), ("n-5Minutes", 300001), ("n-10Minutes", 600001), ("n-15Minutes", 900001), ("n-20Minutes", 1200001), ("n-30Minutes", 1800001)))).setLabel("mibProfLineDiag-BertTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_BertTimer.setStatus('mandatory')
mibProfLineDiag_BertEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfLineDiag-BertEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_BertEnable.setStatus('mandatory')
mibProfLineDiag_IdtEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfLineDiag-IdtEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_IdtEnable.setStatus('mandatory')
mibProfLineDiag_IdtNumOfMsg = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 10), Integer32()).setLabel("mibProfLineDiag-IdtNumOfMsg").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_IdtNumOfMsg.setStatus('mandatory')
mibProfLineDiag_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfLineDiag-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfLineDiag_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBLINEDIAG-MIB", mibProfLineDiag_Action_o=mibProfLineDiag_Action_o, mibmibProfLineDiag=mibmibProfLineDiag, mibmibProfLineDiagTable=mibmibProfLineDiagTable, mibProfLineDiag_PhysicalAddress_ItemNumber=mibProfLineDiag_PhysicalAddress_ItemNumber, mibmibProfLineDiagEntry=mibmibProfLineDiagEntry, DisplayString=DisplayString, mibProfLineDiag_Item_o=mibProfLineDiag_Item_o, mibProfLineDiag_IdtEnable=mibProfLineDiag_IdtEnable, mibProfLineDiag_IdtNumOfMsg=mibProfLineDiag_IdtNumOfMsg, mibProfLineDiag_PhysicalAddress_Shelf=mibProfLineDiag_PhysicalAddress_Shelf, mibProfLineDiag_PhysicalAddress_Slot=mibProfLineDiag_PhysicalAddress_Slot, mibProfLineDiag_BertTimer=mibProfLineDiag_BertTimer, mibProfLineDiag_BertEnable=mibProfLineDiag_BertEnable, mibProfLineDiag_Slot_o=mibProfLineDiag_Slot_o, mibProfLineDiag_Shelf_o=mibProfLineDiag_Shelf_o)