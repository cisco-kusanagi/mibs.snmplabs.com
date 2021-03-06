#
# PySNMP MIB module ASCEND-MIBAPSCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBAPSCFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, ObjectIdentity, Counter32, Gauge32, NotificationType, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "ObjectIdentity", "Counter32", "Gauge32", "NotificationType", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibapsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 148))
mibapsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 148, 1), )
if mibBuilder.loadTexts: mibapsConfigTable.setStatus('mandatory')
mibapsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1), ).setIndexNames((0, "ASCEND-MIBAPSCFG-MIB", "apsConfig-Name"))
if mibBuilder.loadTexts: mibapsConfigEntry.setStatus('mandatory')
apsConfig_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 1), DisplayString()).setLabel("apsConfig-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsConfig_Name.setStatus('mandatory')
apsConfig_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("apsConfig-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_Active.setStatus('mandatory')
apsConfig_LinearProtectionChannel_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("apsConfig-LinearProtectionChannel-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_LinearProtectionChannel_Shelf.setStatus('mandatory')
apsConfig_LinearProtectionChannel_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("apsConfig-LinearProtectionChannel-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_LinearProtectionChannel_Slot.setStatus('mandatory')
apsConfig_LinearProtectionChannel_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 5), Integer32()).setLabel("apsConfig-LinearProtectionChannel-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_LinearProtectionChannel_ItemNumber.setStatus('mandatory')
apsConfig_ProtectionMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("n-1-plus-1", 1), ("n-1-divide-n", 2)))).setLabel("apsConfig-ProtectionMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ProtectionMode.setStatus('mandatory')
apsConfig_DirectionMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setLabel("apsConfig-DirectionMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_DirectionMode.setStatus('mandatory')
apsConfig_RevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("nonRevertive", 2), ("revertive", 1)))).setLabel("apsConfig-RevertiveMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_RevertiveMode.setStatus('mandatory')
apsConfig_WtrTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 9), Integer32()).setLabel("apsConfig-WtrTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_WtrTimerDuration.setStatus('mandatory')
apsConfig_PsbfFailureTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 10), Integer32()).setLabel("apsConfig-PsbfFailureTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_PsbfFailureTimerDuration.setStatus('mandatory')
apsConfig_PsbfClearTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 11), Integer32()).setLabel("apsConfig-PsbfClearTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_PsbfClearTimerDuration.setStatus('mandatory')
apsConfig_ModeMismatchFailureTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 12), Integer32()).setLabel("apsConfig-ModeMismatchFailureTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ModeMismatchFailureTimerDuration.setStatus('mandatory')
apsConfig_ModeMismatchClearTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 13), Integer32()).setLabel("apsConfig-ModeMismatchClearTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ModeMismatchClearTimerDuration.setStatus('mandatory')
apsConfig_ChannelMismatchFailureTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 14), Integer32()).setLabel("apsConfig-ChannelMismatchFailureTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ChannelMismatchFailureTimerDuration.setStatus('mandatory')
apsConfig_ChannelMismatchClearTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 15), Integer32()).setLabel("apsConfig-ChannelMismatchClearTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ChannelMismatchClearTimerDuration.setStatus('mandatory')
apsConfig_FeplMismatchFailureTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 16), Integer32()).setLabel("apsConfig-FeplMismatchFailureTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_FeplMismatchFailureTimerDuration.setStatus('mandatory')
apsConfig_FeplMismatchClearTimerDuration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 17), Integer32()).setLabel("apsConfig-FeplMismatchClearTimerDuration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_FeplMismatchClearTimerDuration.setStatus('mandatory')
apsConfig_ProtectionChannelSignalDegradeExponent = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 18), Integer32()).setLabel("apsConfig-ProtectionChannelSignalDegradeExponent").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ProtectionChannelSignalDegradeExponent.setStatus('mandatory')
apsConfig_ProtectionChannelSignalFailureExponent = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 19), Integer32()).setLabel("apsConfig-ProtectionChannelSignalFailureExponent").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_ProtectionChannelSignalFailureExponent.setStatus('mandatory')
apsConfig_WorkingChannelSignalDegradeExponent = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 20), Integer32()).setLabel("apsConfig-WorkingChannelSignalDegradeExponent").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_WorkingChannelSignalDegradeExponent.setStatus('mandatory')
apsConfig_WorkingChannelSignalFailureExponent = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 21), Integer32()).setLabel("apsConfig-WorkingChannelSignalFailureExponent").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_WorkingChannelSignalFailureExponent.setStatus('mandatory')
apsConfig_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("apsConfig-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsConfig_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBAPSCFG-MIB", apsConfig_ProtectionChannelSignalFailureExponent=apsConfig_ProtectionChannelSignalFailureExponent, DisplayString=DisplayString, apsConfig_ChannelMismatchClearTimerDuration=apsConfig_ChannelMismatchClearTimerDuration, apsConfig_PsbfFailureTimerDuration=apsConfig_PsbfFailureTimerDuration, apsConfig_RevertiveMode=apsConfig_RevertiveMode, apsConfig_ProtectionChannelSignalDegradeExponent=apsConfig_ProtectionChannelSignalDegradeExponent, apsConfig_FeplMismatchFailureTimerDuration=apsConfig_FeplMismatchFailureTimerDuration, apsConfig_Action_o=apsConfig_Action_o, apsConfig_WorkingChannelSignalDegradeExponent=apsConfig_WorkingChannelSignalDegradeExponent, apsConfig_Name=apsConfig_Name, apsConfig_LinearProtectionChannel_Slot=apsConfig_LinearProtectionChannel_Slot, apsConfig_LinearProtectionChannel_Shelf=apsConfig_LinearProtectionChannel_Shelf, apsConfig_ChannelMismatchFailureTimerDuration=apsConfig_ChannelMismatchFailureTimerDuration, apsConfig_PsbfClearTimerDuration=apsConfig_PsbfClearTimerDuration, apsConfig_DirectionMode=apsConfig_DirectionMode, apsConfig_LinearProtectionChannel_ItemNumber=apsConfig_LinearProtectionChannel_ItemNumber, apsConfig_ModeMismatchClearTimerDuration=apsConfig_ModeMismatchClearTimerDuration, apsConfig_ModeMismatchFailureTimerDuration=apsConfig_ModeMismatchFailureTimerDuration, apsConfig_ProtectionMode=apsConfig_ProtectionMode, mibapsConfig=mibapsConfig, mibapsConfigTable=mibapsConfigTable, mibapsConfigEntry=mibapsConfigEntry, apsConfig_Active=apsConfig_Active, apsConfig_WtrTimerDuration=apsConfig_WtrTimerDuration, apsConfig_WorkingChannelSignalFailureExponent=apsConfig_WorkingChannelSignalFailureExponent, apsConfig_FeplMismatchClearTimerDuration=apsConfig_FeplMismatchClearTimerDuration)
