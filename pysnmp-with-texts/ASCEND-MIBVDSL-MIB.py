#
# PySNMP MIB module ASCEND-MIBVDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBVDSL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, TimeTicks, IpAddress, ModuleIdentity, Gauge32, iso, MibIdentifier, Counter32, NotificationType, Counter64, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "IpAddress", "ModuleIdentity", "Gauge32", "iso", "MibIdentifier", "Counter32", "NotificationType", "Counter64", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibvdslLineStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 161))
mibvdslLineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 161, 1), )
if mibBuilder.loadTexts: mibvdslLineStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibvdslLineStatusTable.setDescription('A list of mibvdslLineStatus profile entries.')
mibvdslLineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1), ).setIndexNames((0, "ASCEND-MIBVDSL-MIB", "vdslLineStatus-Shelf-o"), (0, "ASCEND-MIBVDSL-MIB", "vdslLineStatus-Slot-o"), (0, "ASCEND-MIBVDSL-MIB", "vdslLineStatus-Item-o"))
if mibBuilder.loadTexts: mibvdslLineStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibvdslLineStatusEntry.setDescription('A mibvdslLineStatus entry containing objects that maps to the parameters of mibvdslLineStatus profile.')
vdslLineStatus_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 1), Integer32()).setLabel("vdslLineStatus-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_Shelf_o.setDescription('')
vdslLineStatus_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 2), Integer32()).setLabel("vdslLineStatus-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_Slot_o.setDescription('')
vdslLineStatus_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 3), Integer32()).setLabel("vdslLineStatus-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_Item_o.setDescription('')
vdslLineStatus_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("vdslLineStatus-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
vdslLineStatus_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("vdslLineStatus-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
vdslLineStatus_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 6), Integer32()).setLabel("vdslLineStatus-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
vdslLineStatus_LineState = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("doesNotExist", 1), ("disabled", 2), ("active", 3)))).setLabel("vdslLineStatus-LineState").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_LineState.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_LineState.setDescription('The overall state of the line.')
vdslLineStatus_SparePhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("vdslLineStatus-SparePhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_SparePhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparePhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
vdslLineStatus_SparePhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("vdslLineStatus-SparePhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_SparePhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparePhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
vdslLineStatus_SparePhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 10), Integer32()).setLabel("vdslLineStatus-SparePhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_SparePhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparePhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
vdslLineStatus_SparingState = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("sparingNone", 1), ("primaryActive", 2), ("primaryInactive", 3), ("secondaryActive", 4), ("secondaryInactive", 5)))).setLabel("vdslLineStatus-SparingState").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_SparingState.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparingState.setDescription('The sparing state of the line.')
vdslLineStatus_SparingChangeReason = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("manual", 2), ("automatic", 3), ("test", 4)))).setLabel("vdslLineStatus-SparingChangeReason").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_SparingChangeReason.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparingChangeReason.setDescription('The reason for the last sparing state change.')
vdslLineStatus_SparingChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 13), Integer32()).setLabel("vdslLineStatus-SparingChangeTime").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_SparingChangeTime.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparingChangeTime.setDescription('The time of the last sparing state change.')
vdslLineStatus_SparingChangeCounter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 14), Integer32()).setLabel("vdslLineStatus-SparingChangeCounter").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_SparingChangeCounter.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_SparingChangeCounter.setDescription('The number of sparing state changes.')
vdslLineStatus_VpiVciRange = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vpi01Vci321023", 6), ("vpi03Vci32511", 1), ("vpi07Vci32255", 2), ("vpi015Vci32127", 3), ("vpi031Vci3263", 4), ("notApplicable", 5)))).setLabel("vdslLineStatus-VpiVciRange").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_VpiVciRange.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_VpiVciRange.setDescription('The valid range of vpi and vci for the circuits established for the line. This range can change only after LIM reboot.')
vdslLineStatus_VpSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 16), Integer32()).setLabel("vdslLineStatus-VpSwitchingVpi").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_VpSwitchingVpi.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_VpSwitchingVpi.setDescription('VPI to be used for the VP switching. Rest of the VPIs will be used for the VC switching.')
vdslLineStatus_PhysicalStatus_IfGroupIndex = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 17), Integer32()).setLabel("vdslLineStatus-PhysicalStatus-IfGroupIndex").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_IfGroupIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_IfGroupIndex.setDescription('Interface groups index assigned to this physical port.')
vdslLineStatus_PhysicalStatus_UnitType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("dslCoe", 2), ("dslCpe", 3)))).setLabel("vdslLineStatus-PhysicalStatus-UnitType").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_UnitType.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_UnitType.setDescription('Unit types defines if the node is operating Central Office or Customer Premise equipment software.')
vdslLineStatus_PhysicalStatus_DevLineState = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("dslStatDwnInd", 2), ("dslStatWaitInit", 3), ("dslStatInit", 4), ("dslStatUpInd", 5), ("dslStatFailInd", 6), ("dslStatLback", 7), ("dslStatTest", 8), ("dslStatDownload", 9), ("dslStatNumberStates", 10)))).setLabel("vdslLineStatus-PhysicalStatus-DevLineState").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_DevLineState.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_DevLineState.setDescription('Display of current interface state.')
vdslLineStatus_PhysicalStatus_OpUpRates = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 27), Integer32()).setLabel("vdslLineStatus-PhysicalStatus-OpUpRates").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_OpUpRates.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_OpUpRates.setDescription('Display operational up rate.')
vdslLineStatus_PhysicalStatus_OpDownRates = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 28), Integer32()).setLabel("vdslLineStatus-PhysicalStatus-OpDownRates").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_OpDownRates.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_OpDownRates.setDescription('Display operational down rate.')
vdslLineStatus_PhysicalStatus_FirmwareVer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 29), DisplayString()).setLabel("vdslLineStatus-PhysicalStatus-FirmwareVer").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_FirmwareVer.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatus_FirmwareVer.setDescription('Firmware version ID.')
vdslLineStatus_PhysicalStatistic_LineUpTimer_Days = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 20), Integer32()).setLabel("vdslLineStatus-PhysicalStatistic-LineUpTimer-Days").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_LineUpTimer_Days.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_LineUpTimer_Days.setDescription('Number of days that the DSL line has been up.')
vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 21), Integer32()).setLabel("vdslLineStatus-PhysicalStatistic-LineUpTimer-Hours").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setDescription('Number of hours that the DSL line has been up.')
vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 22), Integer32()).setLabel("vdslLineStatus-PhysicalStatistic-LineUpTimer-Minutes").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setDescription('Number of minutes that the DSL line has been up.')
vdslLineStatus_PhysicalStatistic_RxSignalPresent = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 2))).clone(namedValues=NamedValues(("yes", 3), ("no", 2)))).setLabel("vdslLineStatus-PhysicalStatistic-RxSignalPresent").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_RxSignalPresent.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_RxSignalPresent.setDescription('State if the receive signal is present or not.')
vdslLineStatus_PhysicalStatistic_UpDwnCntr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 24), Integer32()).setLabel("vdslLineStatus-PhysicalStatistic-UpDwnCntr").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_UpDwnCntr.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_UpDwnCntr.setDescription('Interface Up Down counter value displays the number of times the interface trasitions from a down to up state.')
vdslLineStatus_PhysicalStatistic_SelfTest = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("dslSelfTestNone", 2), ("dslSelfTestFailed", 3), ("dslSelfTestPassed", 4)))).setLabel("vdslLineStatus-PhysicalStatistic-SelfTest").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_SelfTest.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_PhysicalStatistic_SelfTest.setDescription('Hardware/firmware self test results.')
vdslLineStatus_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("vdslLineStatus-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslLineStatus_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslLineStatus_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBVDSL-MIB", vdslLineStatus_PhysicalAddress_Slot=vdslLineStatus_PhysicalAddress_Slot, vdslLineStatus_PhysicalAddress_ItemNumber=vdslLineStatus_PhysicalAddress_ItemNumber, vdslLineStatus_Slot_o=vdslLineStatus_Slot_o, vdslLineStatus_PhysicalStatus_FirmwareVer=vdslLineStatus_PhysicalStatus_FirmwareVer, vdslLineStatus_PhysicalStatistic_SelfTest=vdslLineStatus_PhysicalStatistic_SelfTest, vdslLineStatus_PhysicalStatus_OpDownRates=vdslLineStatus_PhysicalStatus_OpDownRates, vdslLineStatus_VpSwitchingVpi=vdslLineStatus_VpSwitchingVpi, vdslLineStatus_SparePhysicalAddress_ItemNumber=vdslLineStatus_SparePhysicalAddress_ItemNumber, vdslLineStatus_VpiVciRange=vdslLineStatus_VpiVciRange, vdslLineStatus_Shelf_o=vdslLineStatus_Shelf_o, vdslLineStatus_Item_o=vdslLineStatus_Item_o, vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours=vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours, DisplayString=DisplayString, vdslLineStatus_SparingChangeCounter=vdslLineStatus_SparingChangeCounter, mibvdslLineStatusEntry=mibvdslLineStatusEntry, vdslLineStatus_LineState=vdslLineStatus_LineState, mibvdslLineStatusTable=mibvdslLineStatusTable, vdslLineStatus_PhysicalAddress_Shelf=vdslLineStatus_PhysicalAddress_Shelf, vdslLineStatus_PhysicalStatus_UnitType=vdslLineStatus_PhysicalStatus_UnitType, vdslLineStatus_PhysicalStatistic_UpDwnCntr=vdslLineStatus_PhysicalStatistic_UpDwnCntr, vdslLineStatus_Action_o=vdslLineStatus_Action_o, vdslLineStatus_PhysicalStatistic_RxSignalPresent=vdslLineStatus_PhysicalStatistic_RxSignalPresent, vdslLineStatus_SparePhysicalAddress_Slot=vdslLineStatus_SparePhysicalAddress_Slot, vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes=vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes, vdslLineStatus_PhysicalStatus_DevLineState=vdslLineStatus_PhysicalStatus_DevLineState, vdslLineStatus_SparingChangeReason=vdslLineStatus_SparingChangeReason, vdslLineStatus_SparingState=vdslLineStatus_SparingState, vdslLineStatus_SparingChangeTime=vdslLineStatus_SparingChangeTime, vdslLineStatus_PhysicalStatus_IfGroupIndex=vdslLineStatus_PhysicalStatus_IfGroupIndex, vdslLineStatus_PhysicalStatistic_LineUpTimer_Days=vdslLineStatus_PhysicalStatistic_LineUpTimer_Days, mibvdslLineStatus=mibvdslLineStatus, vdslLineStatus_SparePhysicalAddress_Shelf=vdslLineStatus_SparePhysicalAddress_Shelf, vdslLineStatus_PhysicalStatus_OpUpRates=vdslLineStatus_PhysicalStatus_OpUpRates)
