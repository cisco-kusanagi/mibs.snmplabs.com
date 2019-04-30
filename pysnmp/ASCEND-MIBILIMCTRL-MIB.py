#
# PySNMP MIB module ASCEND-MIBILIMCTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBILIMCTRL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, iso, ModuleIdentity, ObjectIdentity, NotificationType, Integer32, IpAddress, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "iso", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibilimCtrlProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 152))
mibilimCtrlProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 152, 1), )
if mibBuilder.loadTexts: mibilimCtrlProfileTable.setStatus('mandatory')
mibilimCtrlProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1), ).setIndexNames((0, "ASCEND-MIBILIMCTRL-MIB", "ilimCtrlProfile-Shelf-o"), (0, "ASCEND-MIBILIMCTRL-MIB", "ilimCtrlProfile-Slot-o"), (0, "ASCEND-MIBILIMCTRL-MIB", "ilimCtrlProfile-Item-o"))
if mibBuilder.loadTexts: mibilimCtrlProfileEntry.setStatus('mandatory')
ilimCtrlProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1, 1), Integer32()).setLabel("ilimCtrlProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ilimCtrlProfile_Shelf_o.setStatus('mandatory')
ilimCtrlProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1, 2), Integer32()).setLabel("ilimCtrlProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ilimCtrlProfile_Slot_o.setStatus('mandatory')
ilimCtrlProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1, 3), Integer32()).setLabel("ilimCtrlProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ilimCtrlProfile_Item_o.setStatus('mandatory')
ilimCtrlProfile_PrimaryLpm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("ilimCtrlProfile-PrimaryLpm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ilimCtrlProfile_PrimaryLpm.setStatus('mandatory')
ilimCtrlProfile_ActiveLine = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("workingLine", 1), ("protectionLine", 2), ("backupLine", 3)))).setLabel("ilimCtrlProfile-ActiveLine").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ilimCtrlProfile_ActiveLine.setStatus('mandatory')
ilimCtrlProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 152, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ilimCtrlProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ilimCtrlProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBILIMCTRL-MIB", ilimCtrlProfile_Item_o=ilimCtrlProfile_Item_o, DisplayString=DisplayString, ilimCtrlProfile_ActiveLine=ilimCtrlProfile_ActiveLine, ilimCtrlProfile_Shelf_o=ilimCtrlProfile_Shelf_o, mibilimCtrlProfileTable=mibilimCtrlProfileTable, ilimCtrlProfile_Slot_o=ilimCtrlProfile_Slot_o, mibilimCtrlProfileEntry=mibilimCtrlProfileEntry, mibilimCtrlProfile=mibilimCtrlProfile, ilimCtrlProfile_Action_o=ilimCtrlProfile_Action_o, ilimCtrlProfile_PrimaryLpm=ilimCtrlProfile_PrimaryLpm)
