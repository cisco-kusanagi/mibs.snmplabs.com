#
# PySNMP MIB module ASCEND-MIBSHDSLNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSHDSLNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, IpAddress, NotificationType, Bits, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibshdslNetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 147))
mibshdslNetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 147, 1), )
if mibBuilder.loadTexts: mibshdslNetworkProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibshdslNetworkProfileTable.setDescription('A list of mibshdslNetworkProfile profile entries.')
mibshdslNetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1), ).setIndexNames((0, "ASCEND-MIBSHDSLNET-MIB", "shdslNetworkProfile-Shelf-o"), (0, "ASCEND-MIBSHDSLNET-MIB", "shdslNetworkProfile-Slot-o"), (0, "ASCEND-MIBSHDSLNET-MIB", "shdslNetworkProfile-Item-o"))
if mibBuilder.loadTexts: mibshdslNetworkProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibshdslNetworkProfileEntry.setDescription('A mibshdslNetworkProfile entry containing objects that maps to the parameters of mibshdslNetworkProfile profile.')
shdslNetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 1), Integer32()).setLabel("shdslNetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: shdslNetworkProfile_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_Shelf_o.setDescription('')
shdslNetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 2), Integer32()).setLabel("shdslNetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: shdslNetworkProfile_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_Slot_o.setDescription('')
shdslNetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 3), Integer32()).setLabel("shdslNetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: shdslNetworkProfile_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_Item_o.setDescription('')
shdslNetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 4), DisplayString()).setLabel("shdslNetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_Name.setDescription('For future use. The current design does not use the name field but instead references Shdsl lines by the physical address; we may in the future support referencing Shdsl lines by name as well as by address. The name consists of a null terminated ascii string supplied by the user; it defaults to the ascii form of the Shdsl line physical address.')
shdslNetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("shdslNetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
shdslNetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("shdslNetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
shdslNetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 7), Integer32()).setLabel("shdslNetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
shdslNetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("shdslNetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_Enabled.setDescription('TRUE if the line is enabled, otherwise FALSE.')
shdslNetworkProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("shdslNetworkProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_SparingMode.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_SparingMode.setDescription('Port sparing operational mode for this port.')
shdslNetworkProfile_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("shdslNetworkProfile-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_IgnoreLineup.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_IgnoreLineup.setDescription('Ignore line up value for this port.')
shdslNetworkProfile_ProfileNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 11), Integer32()).setLabel("shdslNetworkProfile-ProfileNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_ProfileNumber.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_ProfileNumber.setDescription('For potential backwards compatibility. The current design consists of one line profile numbered 0.')
shdslNetworkProfile_LineConfig_TrunkGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 12), Integer32()).setLabel("shdslNetworkProfile-LineConfig-TrunkGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_TrunkGroup.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_TrunkGroup.setDescription('The trunk group to which this line is assigned. 0 means this line is not part of a trunk group.')
shdslNetworkProfile_LineConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 13), Integer32()).setLabel("shdslNetworkProfile-LineConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_NailedGroup.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_NailedGroup.setDescription('A number that identifies the set of lines that makes up a nailed group. 0 means this line is not part of a nailed group.')
shdslNetworkProfile_LineConfig_VpSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 14), Integer32()).setLabel("shdslNetworkProfile-LineConfig-VpSwitchingVpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_VpSwitchingVpi.setDescription('The Vpi to be used for the VP switching. Rest of the valid VPIs in valid vpi-vci-range will be used for the VC switching. Changes in this range will take effect immediately. THE USER SHOULD BE VERY CAREFUL WHILE CHANGING THIS VALUE BECAUSE ALL CONNECTIONS ON THE LIM WHERE THIS PORT BELONGS WILL BE DROPPED IN ORDER TO MAKE THIS NEW VALUE EFFECTIVE IMMEDIATELY.')
shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 15), Integer32()).setLabel("shdslNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setDescription('')
shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 16), Integer32()).setLabel("shdslNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setDescription('TNT is a multi shelf system. To minimise the changes required to existing code the shelf number is added to this structure as it will almost always be needed when a slot number is needed.')
shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 17), Integer32()).setLabel("shdslNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setDescription('')
shdslNetworkProfile_LineConfig_Activation = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dsrActive", 2), ("dcdDsrActive", 3)))).setLabel("shdslNetworkProfile-LineConfig-Activation").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_Activation.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_Activation.setDescription('Line activation mode.')
shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("shdslNetworkProfile-LineConfig-CallRouteInfo-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
shdslNetworkProfile_LineConfig_CallRouteInfo_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("shdslNetworkProfile-LineConfig-CallRouteInfo-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_CallRouteInfo_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_CallRouteInfo_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 21), Integer32()).setLabel("shdslNetworkProfile-LineConfig-CallRouteInfo-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
shdslNetworkProfile_LineConfig_UnitType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coe", 1), ("cpe", 2)))).setLabel("shdslNetworkProfile-LineConfig-UnitType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_UnitType.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_UnitType.setDescription('The Unit Type defines if a line is acting as either a Central Office (COE) or Customer Premise Equipment (CPE). Note that the remote unit needs to be configured opposite to this configureation.')
shdslNetworkProfile_LineConfig_NtrEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("shdslNetworkProfile-LineConfig-NtrEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_NtrEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_NtrEnabled.setDescription('TRUE if NTR functionality is enabled, otherwise FALSE. If the unit-type is COE, it will take the system clock as the input when NTR is enabled and allow the remote CPE port to recover the clock. If the unit-type is CPE, it will allow the port to possibly output the recovered clock as the system clock (if elected, see clock-source and clock-priority fields) when NTR is enabled.')
shdslNetworkProfile_LineConfig_ClockSource = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eligible", 1), ("notEligible", 2)))).setLabel("shdslNetworkProfile-LineConfig-ClockSource").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_ClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_ClockSource.setDescription('Determine whether the 8KHz clock from the SHDSL line (unit-type has to be CPE and ntr-enabled has to be yes) is eligible to be used as the 8KHz system clock source.')
shdslNetworkProfile_LineConfig_ClockPriority = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("highPriority", 2), ("middlePriority", 3), ("lowPriority", 4)))).setLabel("shdslNetworkProfile-LineConfig-ClockPriority").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_ClockPriority.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_ClockPriority.setDescription('Clock priority assigned to the SHDSL line. Used to select a particular SHDSL line as the 8KHz system clock source.')
shdslNetworkProfile_LineConfig_LoopBack = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("analog", 2), ("digital", 3)))).setLabel("shdslNetworkProfile-LineConfig-LoopBack").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_LoopBack.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_LoopBack.setDescription('Configuration of different modem loopbacks.')
shdslNetworkProfile_LineConfig_Margin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17))).clone(namedValues=NamedValues(("n-0db", 1), ("n-1db", 2), ("n-2db", 3), ("n-3db", 4), ("n-4db", 5), ("n-5db", 6), ("n-6db", 7), ("n-7db", 8), ("n-8db", 9), ("n-9db", 10), ("n-10db", 11), ("disable", 17)))).setLabel("shdslNetworkProfile-LineConfig-Margin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_Margin.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_Margin.setDescription('Selects a margin range between the signal to noise floor.')
shdslNetworkProfile_LineConfig_SnextMargin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("n-0db", 1), ("n-1db", 2), ("n-2db", 3), ("n-3db", 4), ("n-4db", 5), ("n-5db", 6), ("n-6db", 7), ("n-7db", 8), ("n-8db", 9), ("n-9db", 10), ("n-10db", 11), ("n-plus-10db", 12), ("n-plus-9db", 13), ("n-plus-8db", 14), ("n-plus-7db", 15), ("n-plus-6db", 16), ("n-plus-5db", 17), ("n-plus-4db", 18), ("n-plus-3db", 19), ("n-plus-2db", 20), ("n-plus-1db", 21), ("disable", 22)))).setLabel("shdslNetworkProfile-LineConfig-SnextMargin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_SnextMargin.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_SnextMargin.setDescription('Selects a Snext margin range with a worst-case self next noise model given current loop insertion loss.')
shdslNetworkProfile_LineConfig_RateMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("auto", 2)))).setLabel("shdslNetworkProfile-LineConfig-RateMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RateMode.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_RateMode.setDescription('Used for G.SHDSL technology. Selects if the modem operates in Fixed or Auto rate mode.')
shdslNetworkProfile_LineConfig_MinRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(72001, 136001, 200001, 264001, 328001, 392001, 520001, 776001, 1032001, 1160001, 1288001, 1544001, 2056001, 2312001))).clone(namedValues=NamedValues(("n-72000", 72001), ("n-136000", 136001), ("n-200000", 200001), ("n-264000", 264001), ("n-328000", 328001), ("n-392000", 392001), ("n-520000", 520001), ("n-776000", 776001), ("n-1032000", 1032001), ("n-1160000", 1160001), ("n-1288000", 1288001), ("n-1544000", 1544001), ("n-2056000", 2056001), ("n-2312000", 2312001)))).setLabel("shdslNetworkProfile-LineConfig-MinRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_MinRate.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_MinRate.setDescription('Used for G.SHDSL technology. When the rate-mode is set to Auto, this is the minimum rate the modem will train to.')
shdslNetworkProfile_LineConfig_MaxRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(72001, 136001, 200001, 264001, 328001, 392001, 520001, 776001, 1032001, 1160001, 1288001, 1544001, 2056001, 2312001))).clone(namedValues=NamedValues(("n-72000", 72001), ("n-136000", 136001), ("n-200000", 200001), ("n-264000", 264001), ("n-328000", 328001), ("n-392000", 392001), ("n-520000", 520001), ("n-776000", 776001), ("n-1032000", 1032001), ("n-1160000", 1160001), ("n-1288000", 1288001), ("n-1544000", 1544001), ("n-2056000", 2056001), ("n-2312000", 2312001)))).setLabel("shdslNetworkProfile-LineConfig-MaxRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_MaxRate.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_MaxRate.setDescription('Used for G.SHDSL technology. When the rate-mode is set to Auto, this is the maximum rate the modem will train to. When the rate-mode is set to Fixed, this is the only rate the mode trains to.')
shdslNetworkProfile_LineConfig_GshdslStandardNetworkType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("northAmericanAnnexA", 1), ("europeanAnnexB", 2), ("autoDetect", 3)))).setLabel("shdslNetworkProfile-LineConfig-GshdslStandardNetworkType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_GshdslStandardNetworkType.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_GshdslStandardNetworkType.setDescription("Per the G.SHDSL Standard G.991.2. This parameter allows selection for the modem to operate either the North American Annex 'A' or European Annex 'B' standard network types. The setting of auto-detect is only valid for CPE to train off of COE Standard Network settings.")
shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("shdslNetworkProfile-LineConfig-AnnexbAnfpEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled.setDescription('TRUE if Annex B ANFP functionality is enabled, otherwise FALSE. The gshdsl-standard-network-type must be set to European Annex B, and the port cannot be CPE. This field makes the modem perform in Annex B mode, but slightly differently. This is to comply with the UK ANFP requirements and pass the BTexact Technologies PSD measurement technique to meet BT approval. Only enable this field for that test specifically.')
shdslNetworkProfile_LineConfig_GshdslPsdType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("symmetric", 1), ("asymmetric776kPsdAnnexA", 4), ("asymmetric1544kPsdAnnexA", 5), ("asymmetric2056kPsdAnnexB", 6), ("asymmetric2312kPsdAnnexB", 7), ("autoDetect", 8)))).setLabel("shdslNetworkProfile-LineConfig-GshdslPsdType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_GshdslPsdType.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_GshdslPsdType.setDescription("Per the G.SHDSL Standard G.911.2. This parameter allows selection for the modem to output a symmetric PSD at all rates or asymmetric PSD's at fixed rates of 776kbps or 1544kbps, for Annex A networks. Annex B networks support fixed rates of 2056kbps or 2304kbps. The setting of auto-detect is only valid for CPE to train off of COE PSD settings.")
shdslNetworkProfile_LineConfig_MasterBindingPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("shdslNetworkProfile-LineConfig-MasterBindingPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_MasterBindingPort.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_LineConfig_MasterBindingPort.setDescription('This parameter defines if a port is used as a master or slave for port binding purposes. Only odd ports are configured masters for the binding feature. When the master is enabled, the master port will be bound with the next even port number. Binding two SHDSL ports together will aggregate their bandwidths together. This does not apply to HDSL2 modem technology. Other line configuration rules: 1) Port rate mode needs to be Fixed. 2) The master ports max-rate and rate-mode are used for both ports. 3) Both ports need to be enabled.')
shdslNetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("shdslNetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: shdslNetworkProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: shdslNetworkProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBSHDSLNET-MIB", shdslNetworkProfile_LineConfig_ClockSource=shdslNetworkProfile_LineConfig_ClockSource, mibshdslNetworkProfileTable=mibshdslNetworkProfileTable, shdslNetworkProfile_Name=shdslNetworkProfile_Name, mibshdslNetworkProfile=mibshdslNetworkProfile, shdslNetworkProfile_Shelf_o=shdslNetworkProfile_Shelf_o, shdslNetworkProfile_Action_o=shdslNetworkProfile_Action_o, shdslNetworkProfile_IgnoreLineup=shdslNetworkProfile_IgnoreLineup, DisplayString=DisplayString, shdslNetworkProfile_LineConfig_TrunkGroup=shdslNetworkProfile_LineConfig_TrunkGroup, mibshdslNetworkProfileEntry=mibshdslNetworkProfileEntry, shdslNetworkProfile_PhysicalAddress_Shelf=shdslNetworkProfile_PhysicalAddress_Shelf, shdslNetworkProfile_LineConfig_NtrEnabled=shdslNetworkProfile_LineConfig_NtrEnabled, shdslNetworkProfile_Item_o=shdslNetworkProfile_Item_o, shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber=shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber, shdslNetworkProfile_PhysicalAddress_Slot=shdslNetworkProfile_PhysicalAddress_Slot, shdslNetworkProfile_LineConfig_SnextMargin=shdslNetworkProfile_LineConfig_SnextMargin, shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber=shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber, shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf=shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf, shdslNetworkProfile_LineConfig_MaxRate=shdslNetworkProfile_LineConfig_MaxRate, shdslNetworkProfile_LineConfig_GshdslPsdType=shdslNetworkProfile_LineConfig_GshdslPsdType, shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled=shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled, shdslNetworkProfile_LineConfig_GshdslStandardNetworkType=shdslNetworkProfile_LineConfig_GshdslStandardNetworkType, shdslNetworkProfile_LineConfig_MasterBindingPort=shdslNetworkProfile_LineConfig_MasterBindingPort, shdslNetworkProfile_PhysicalAddress_ItemNumber=shdslNetworkProfile_PhysicalAddress_ItemNumber, shdslNetworkProfile_LineConfig_MinRate=shdslNetworkProfile_LineConfig_MinRate, shdslNetworkProfile_LineConfig_UnitType=shdslNetworkProfile_LineConfig_UnitType, shdslNetworkProfile_SparingMode=shdslNetworkProfile_SparingMode, shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber=shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber, shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber=shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber, shdslNetworkProfile_LineConfig_Activation=shdslNetworkProfile_LineConfig_Activation, shdslNetworkProfile_LineConfig_ClockPriority=shdslNetworkProfile_LineConfig_ClockPriority, shdslNetworkProfile_LineConfig_RateMode=shdslNetworkProfile_LineConfig_RateMode, shdslNetworkProfile_Slot_o=shdslNetworkProfile_Slot_o, shdslNetworkProfile_LineConfig_VpSwitchingVpi=shdslNetworkProfile_LineConfig_VpSwitchingVpi, shdslNetworkProfile_LineConfig_LoopBack=shdslNetworkProfile_LineConfig_LoopBack, shdslNetworkProfile_LineConfig_NailedGroup=shdslNetworkProfile_LineConfig_NailedGroup, shdslNetworkProfile_LineConfig_Margin=shdslNetworkProfile_LineConfig_Margin, shdslNetworkProfile_ProfileNumber=shdslNetworkProfile_ProfileNumber, shdslNetworkProfile_LineConfig_CallRouteInfo_Slot=shdslNetworkProfile_LineConfig_CallRouteInfo_Slot, shdslNetworkProfile_Enabled=shdslNetworkProfile_Enabled)
