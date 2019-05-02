#
# PySNMP MIB module APPIAN-STRATUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-STRATUM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acChassisCurrentTime, acChassisRingId = mibBuilder.importSymbols("APPIAN-CHASSIS-MIB", "acChassisCurrentTime", "acChassisRingId")
acOsap, AcOpStatus, AcNodeId = mibBuilder.importSymbols("APPIAN-SMI-MIB", "acOsap", "AcOpStatus", "AcNodeId")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter64, Gauge32, ObjectIdentity, Counter32, MibIdentifier, Integer32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "iso", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
acStratum = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785, 2, 9))
acStratum.setRevisions(('1900-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acStratum.setRevisionsDescriptions(('Draft MIB for Engineering use only.',))
if mibBuilder.loadTexts: acStratum.setLastUpdated('0008220000Z')
if mibBuilder.loadTexts: acStratum.setOrganization('Appian Communications, Inc.')
if mibBuilder.loadTexts: acStratum.setContactInfo('Brian Johnson')
if mibBuilder.loadTexts: acStratum.setDescription('Appian Communications Stratum MIB contain the definitions for the configuration and control of Stratum Clock module hardware information and status.')
acStratumTable = MibTable((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1), )
if mibBuilder.loadTexts: acStratumTable.setStatus('current')
if mibBuilder.loadTexts: acStratumTable.setDescription('This table contains two rows for access and control of the Stratum-3 clock modules.')
acStratumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1), ).setIndexNames((0, "APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumEntry.setStatus('current')
if mibBuilder.loadTexts: acStratumEntry.setDescription('A row within the Stratum table containing access control and status information relating to the operation of the Stratum-3 clock module.')
acStratumNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 1), AcNodeId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acStratumNodeId.setStatus('current')
if mibBuilder.loadTexts: acStratumNodeId.setDescription("The unique node identification number representing a chassis within a ring of OSAP's.")
acStratumClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("bits", 2), ("line", 3))).clone('internal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumClockSource.setStatus('current')
if mibBuilder.loadTexts: acStratumClockSource.setDescription('This attribute determines the clock source.')
acStratumOpStatusModuleA = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 3), AcOpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumOpStatusModuleA.setStatus('current')
if mibBuilder.loadTexts: acStratumOpStatusModuleA.setDescription('This field indicates the current operational status for the clock card in slot 16, module A . Only the following values are applicable to the module: operational, offline, initializing, selfTesting, upgrading, standby, shuttingDown, failed, and hw not present.')
acStratumOpStatusModuleB = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 4), AcOpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumOpStatusModuleB.setStatus('current')
if mibBuilder.loadTexts: acStratumOpStatusModuleB.setDescription('This field indicates the current operational status for the clock card in slot 16, module B . Only the following values are applicable to the module: operational, offline, initializing, selfTesting, upgrading, standby, shuttingDown, failed, and hw not present.')
acStratumAlarmStatusModuleA = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumAlarmStatusModuleA.setStatus('current')
if mibBuilder.loadTexts: acStratumAlarmStatusModuleA.setDescription('This attribute contains the current status of the clock alarms. The acStratumAlarmStatus is a bit map represented as a sum. Normal may only be set if and only if no other alarms are set. The various bit positions are: 1 normal No alarm present 2 los Loss of Signal 4 lof Loss of Frame ')
acStratumAlarmStatusModuleB = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumAlarmStatusModuleB.setStatus('current')
if mibBuilder.loadTexts: acStratumAlarmStatusModuleB.setDescription('This attribute contains the current status of the clock alarms. The acStratumAlarmStatus is a bit map represented as a sum. Normal must be set if and oly if no other flash is set. The various bit positions are: 1 normal No alarm present 2 los Loss of Signal 4 lof Loss of Frame ')
acStratumCurrentClockSourceModuleA = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 0), ("none", 1), ("bits-a", 2), ("bits-b", 3), ("line-slot1-port1", 4), ("line-slot1-port2", 5), ("line-slot2-port1", 6), ("line-slot2-port2", 7), ("holdover", 8), ("internal", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumCurrentClockSourceModuleA.setStatus('current')
if mibBuilder.loadTexts: acStratumCurrentClockSourceModuleA.setDescription('This attribute displays the current source that the clock card is selecting.')
acStratumCurrentClockSourceModuleB = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 0), ("none", 1), ("bits-a", 2), ("bits-b", 3), ("line-slot1-port1", 4), ("line-slot1-port2", 5), ("line-slot2-port1", 6), ("line-slot2-port2", 7), ("holdover", 8), ("internal", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumCurrentClockSourceModuleB.setStatus('current')
if mibBuilder.loadTexts: acStratumCurrentClockSourceModuleB.setDescription('This attribute displays the current source that the clock card is selecting.')
acStratumLockoutReference = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumLockoutReference.setStatus('current')
if mibBuilder.loadTexts: acStratumLockoutReference.setDescription('This attribute is a bit mask of clock references that should be locked out from selection for the clock source. None can only be selected when no other lockout references are selected. The various bit positions are: 0 none No clock references are locked out from selection. 1 bits-a BITS source from clock module A is locked out. 2 bits-b BITS source from clock module B is locked out. 4 line-slot1 LINE timing source from SONET slot 1 is locked out. 8 line-slot2 LINE timing source from SONET slot 2 is locked out. 16 holdover-a Holdover from clock module A is locked out. 32 holdover-b Holdover from clock module B is locked out. ')
acStratumManualSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("bits-a", 1), ("bits-b", 2), ("line-slot1", 3), ("line-slot2", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumManualSwitch.setStatus('current')
if mibBuilder.loadTexts: acStratumManualSwitch.setDescription('This attribute will manually switch the clock references. If the clock reference does not exist, is locked out, or the reference has failed, the switch will not take place.')
acStratumForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("bits-a", 1), ("bits-b", 2), ("line-slot1", 3), ("line-slot2", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumForcedSwitch.setStatus('current')
if mibBuilder.loadTexts: acStratumForcedSwitch.setDescription('This attribute will force switch the clock references. If the clock reference does not exist or is locked out, the switch will not take place.')
acStratumRevertiveRefSwitchEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumRevertiveRefSwitchEnabled.setStatus('current')
if mibBuilder.loadTexts: acStratumRevertiveRefSwitchEnabled.setDescription('Setting of this attribute to true(1) will the reference to revert back to the original reference when that reference become ready again.')
acStratumClearAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumClearAlarms.setStatus('current')
if mibBuilder.loadTexts: acStratumClearAlarms.setDescription('Setting of this attribute to true(1) will cause the alarm contacts to clear. Reading this attribute will always return false.')
acStratumLineTimingPortSlot1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumLineTimingPortSlot1.setStatus('current')
if mibBuilder.loadTexts: acStratumLineTimingPortSlot1.setDescription('When configured for line timing, this value describes which port on the SONET card will be used to drive the line. This value is not applicable when not configured for line timing.')
acStratumLineTimingPortSlot2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumLineTimingPortSlot2.setStatus('current')
if mibBuilder.loadTexts: acStratumLineTimingPortSlot2.setDescription('When configured for line timing, this value describes which port on the SONET card will be used to drive the line. This value is not applicable when not configured for line timing.')
acStratumBITSFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("esf", 1), ("d4", 2))).clone('esf')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acStratumBITSFramingType.setStatus('current')
if mibBuilder.loadTexts: acStratumBITSFramingType.setDescription('When configured for BITS timing, this value describes the type of framing that will be used on the BITS interface. This value is not applicable when not configured for BITS timing.')
acStratumCurrentClockSourceSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 0), ("bits-a", 1), ("bits-b", 2), ("line-slot1-port1", 3), ("line-slot1-port2", 4), ("line-slot2-port1", 5), ("line-slot2-port2", 6), ("holdover-clock-a", 7), ("holdover-clock-b", 8), ("internal-clock-a", 9), ("internal-clock-b", 10), ("internal-sonet-slot1", 11), ("internal-sonet-slot2", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acStratumCurrentClockSourceSystem.setStatus('current')
if mibBuilder.loadTexts: acStratumCurrentClockSourceSystem.setDescription('This attribute displays the current clock source that the system is selecting.')
acStratumTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0))
acStratumFailedModuleATrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 1)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumFailedModuleATrap.setStatus('current')
if mibBuilder.loadTexts: acStratumFailedModuleATrap.setDescription('The stratum clock module failed.')
acStratumFailedModuleBTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 2)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumFailedModuleBTrap.setStatus('current')
if mibBuilder.loadTexts: acStratumFailedModuleBTrap.setDescription('The stratum clock module failed.')
acStratumClockFailureModuleATrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 3)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"), ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleA"))
if mibBuilder.loadTexts: acStratumClockFailureModuleATrap.setStatus('current')
if mibBuilder.loadTexts: acStratumClockFailureModuleATrap.setDescription('Stratum clock agent has detected a clock timing failure.')
acStratumClockFailureModuleBTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 4)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"), ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleB"))
if mibBuilder.loadTexts: acStratumClockFailureModuleBTrap.setStatus('current')
if mibBuilder.loadTexts: acStratumClockFailureModuleBTrap.setDescription('Stratum clock agent has detected a clock timing failure.')
acStratumRemovalModuleATrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 5)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumRemovalModuleATrap.setStatus('current')
if mibBuilder.loadTexts: acStratumRemovalModuleATrap.setDescription('The stratum clock module has been removed from the system.')
acStratumRemovalModuleBTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 6)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumRemovalModuleBTrap.setStatus('current')
if mibBuilder.loadTexts: acStratumRemovalModuleBTrap.setDescription('The stratum clock module has been removed from the system.')
acStratumInsertedModuleATrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 7)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumInsertedModuleATrap.setStatus('current')
if mibBuilder.loadTexts: acStratumInsertedModuleATrap.setDescription('A stratum clock module has been inserted into the system.')
acStratumInsertedModuleBTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 8)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
if mibBuilder.loadTexts: acStratumInsertedModuleBTrap.setStatus('current')
if mibBuilder.loadTexts: acStratumInsertedModuleBTrap.setDescription('A stratum clock module has been inserted into the system.')
acStratumClockModuleAOk = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 9)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"), ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleA"))
if mibBuilder.loadTexts: acStratumClockModuleAOk.setStatus('current')
if mibBuilder.loadTexts: acStratumClockModuleAOk.setDescription('Stratum clock agent has recovered clock timing.')
acStratumClockModuleBOk = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 10)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"), ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleB"))
if mibBuilder.loadTexts: acStratumClockModuleBOk.setStatus('current')
if mibBuilder.loadTexts: acStratumClockModuleBOk.setDescription('Stratum clock agent has recovered clock timing.')
acStratumSystemClockSourceChange = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 11)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-STRATUM-MIB", "acStratumNodeId"), ("APPIAN-STRATUM-MIB", "acStratumCurrentClockSourceSystem"))
if mibBuilder.loadTexts: acStratumSystemClockSourceChange.setStatus('current')
if mibBuilder.loadTexts: acStratumSystemClockSourceChange.setDescription('Stratum clock source has changed to acStratumCurrentClockSourceSystem.')
mibBuilder.exportSymbols("APPIAN-STRATUM-MIB", acStratumClockFailureModuleATrap=acStratumClockFailureModuleATrap, acStratumManualSwitch=acStratumManualSwitch, acStratumClockModuleBOk=acStratumClockModuleBOk, acStratumRemovalModuleBTrap=acStratumRemovalModuleBTrap, acStratumBITSFramingType=acStratumBITSFramingType, acStratumTable=acStratumTable, acStratumRevertiveRefSwitchEnabled=acStratumRevertiveRefSwitchEnabled, acStratumRemovalModuleATrap=acStratumRemovalModuleATrap, acStratumFailedModuleBTrap=acStratumFailedModuleBTrap, acStratumLineTimingPortSlot2=acStratumLineTimingPortSlot2, acStratumInsertedModuleATrap=acStratumInsertedModuleATrap, acStratumFailedModuleATrap=acStratumFailedModuleATrap, acStratumTraps=acStratumTraps, acStratumAlarmStatusModuleA=acStratumAlarmStatusModuleA, acStratumNodeId=acStratumNodeId, acStratumClockModuleAOk=acStratumClockModuleAOk, acStratumOpStatusModuleB=acStratumOpStatusModuleB, acStratumForcedSwitch=acStratumForcedSwitch, acStratumCurrentClockSourceModuleA=acStratumCurrentClockSourceModuleA, acStratumAlarmStatusModuleB=acStratumAlarmStatusModuleB, acStratumCurrentClockSourceSystem=acStratumCurrentClockSourceSystem, acStratumClockSource=acStratumClockSource, acStratumCurrentClockSourceModuleB=acStratumCurrentClockSourceModuleB, PYSNMP_MODULE_ID=acStratum, acStratum=acStratum, acStratumLineTimingPortSlot1=acStratumLineTimingPortSlot1, acStratumSystemClockSourceChange=acStratumSystemClockSourceChange, acStratumEntry=acStratumEntry, acStratumOpStatusModuleA=acStratumOpStatusModuleA, acStratumClearAlarms=acStratumClearAlarms, acStratumLockoutReference=acStratumLockoutReference, acStratumClockFailureModuleBTrap=acStratumClockFailureModuleBTrap, acStratumInsertedModuleBTrap=acStratumInsertedModuleBTrap)
