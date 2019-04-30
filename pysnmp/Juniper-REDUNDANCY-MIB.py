#
# PySNMP MIB module Juniper-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, TimeTicks, IpAddress, iso, ObjectIdentity, Counter32, Integer32, Bits, ModuleIdentity, Counter64, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "iso", "ObjectIdentity", "Counter32", "Integer32", "Bits", "ModuleIdentity", "Counter64", "MibIdentifier", "NotificationType")
TextualConvention, RowStatus, DisplayString, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime", "TruthValue")
juniRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74))
juniRedundancyMIB.setRevisions(('2003-12-12 00:00',))
if mibBuilder.loadTexts: juniRedundancyMIB.setLastUpdated('200312122104Z')
if mibBuilder.loadTexts: juniRedundancyMIB.setOrganization('Juniper Networks, Inc.')
class JuniRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notKnown", 1), ("fileSystemSyncing", 2), ("disabled", 3), ("initializing", 4), ("pending", 5), ("active", 6))

class JuniRedundancyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fileSystemSynchronization", 1), ("highAvailability", 2))

class JuniRedundancyResetReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("notKnown", 2), ("userInitiated", 3))

class JuniRedundancySystemActivationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reload", 1), ("coldSwitch", 2), ("warmSwitch", 3))

class JuniRedundancyResetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notKnown", 1), ("srpReload", 2), ("srpSwitchover", 3), ("linecardReload", 4), ("linecardSwitchover", 5))

class JuniRedundancyHistoryCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("keep", 1), ("clear", 2))

juniRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0))
juniRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1))
juniRedundancyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2))
juniRedundancyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1))
juniRedundancyCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2))
juniRedundancyHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3))
juniRedundancyActiveSlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyActiveSlot.setStatus('current')
juniRedundancyActiveSlotState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 2), JuniRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyActiveSlotState.setStatus('current')
juniRedundancyStandbySlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyStandbySlot.setStatus('current')
juniRedundancyStandbySlotState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 4), JuniRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyStandbySlotState.setStatus('current')
juniRedundancyLastResetReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 5), JuniRedundancyResetReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastResetReason.setStatus('current')
juniRedundancyLastSystemActivationTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationTime.setStatus('current')
juniRedundancyLastSystemActivationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 7), JuniRedundancySystemActivationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationType.setStatus('current')
juniRedundancyHaActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHaActiveTime.setStatus('current')
juniRedundancyNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancyNotifsEnabled.setStatus('current')
juniRedundancyCfgRedundancyMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 2), JuniRedundancyMode().clone('fileSystemSynchronization')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancyCfgRedundancyMode.setStatus('current')
juniRedundancySystemActivationHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTableMaxLength.setStatus('current')
juniRedundancySystemActivationHistoryCommand = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 2), JuniRedundancyHistoryCommand().clone('keep')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryCommand.setStatus('current')
juniRedundancySystemActivationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3), )
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTable.setStatus('current')
juniRedundancySystemActivationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1), ).setIndexNames((0, "Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryIndex"))
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryEntry.setStatus('current')
juniRedundancySystemActivationHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryIndex.setStatus('current')
juniRedundancyHistoryResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 2), JuniRedundancyResetType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryResetType.setStatus('current')
juniRedundancyHistoryActivationType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 3), JuniRedundancySystemActivationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryActivationType.setStatus('current')
juniRedundancyHistoryPrevActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveSlot.setStatus('current')
juniRedundancyHistoryPrevActiveRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveRelease.setStatus('current')
juniRedundancyHistoryCurrActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveSlot.setStatus('current')
juniRedundancyHistoryCurrActiveRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveRelease.setStatus('current')
juniRedundancyHistoryResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 8), JuniRedundancyResetReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryResetReason.setStatus('current')
juniRedundancyHistoryActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryActivationTime.setStatus('current')
juniRedundancyHistoryReloads = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryReloads.setStatus('current')
juniRedundancyHistoryColdSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryColdSwitchovers.setStatus('current')
juniRedundancyHistoryWarmSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryWarmSwitchovers.setStatus('current')
juniRedundancyColdSwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
if mibBuilder.loadTexts: juniRedundancyColdSwitchoverNotification.setStatus('current')
juniRedundancyWarmSwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 2)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
if mibBuilder.loadTexts: juniRedundancyWarmSwitchoverNotification.setStatus('current')
juniRedundancyStateEnabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 3)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStateEnabledNotification.setStatus('current')
juniRedundancyStateDisabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 4)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStateDisabledNotification.setStatus('current')
juniRedundancyStatePendingNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 5)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStatePendingNotification.setStatus('current')
juniRedundancyModeNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 6)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
if mibBuilder.loadTexts: juniRedundancyModeNotification.setStatus('current')
juniRedundancyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1))
juniRedundancyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2))
juniRedundancyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyStatusGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyMIBCompliance = juniRedundancyMIBCompliance.setStatus('current')
juniRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlotState"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlotState"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationTime"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHaActiveTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyStatusGroup = juniRedundancyStatusGroup.setStatus('current')
juniRedundancyCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 2)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyNotifsEnabled"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyCfgGroup = juniRedundancyCfgGroup.setStatus('current')
juniRedundancyHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 3)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryTableMaxLength"), ("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryCommand"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveRelease"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveRelease"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetReason"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationTime"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryReloads"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryColdSwitchovers"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryWarmSwitchovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyHistoryGroup = juniRedundancyHistoryGroup.setStatus('current')
juniRedundancyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 4)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyColdSwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyWarmSwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateEnabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateDisabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStatePendingNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyModeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyNotificationGroup = juniRedundancyNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-REDUNDANCY-MIB", juniRedundancyStatusGroup=juniRedundancyStatusGroup, juniRedundancyHistoryGroup=juniRedundancyHistoryGroup, JuniRedundancyHistoryCommand=JuniRedundancyHistoryCommand, juniRedundancyStatePendingNotification=juniRedundancyStatePendingNotification, juniRedundancySystemActivationHistoryCommand=juniRedundancySystemActivationHistoryCommand, juniRedundancyStateEnabledNotification=juniRedundancyStateEnabledNotification, juniRedundancySystemActivationHistoryIndex=juniRedundancySystemActivationHistoryIndex, PYSNMP_MODULE_ID=juniRedundancyMIB, juniRedundancyMIBCompliance=juniRedundancyMIBCompliance, JuniRedundancyState=JuniRedundancyState, juniRedundancyStateDisabledNotification=juniRedundancyStateDisabledNotification, juniRedundancyMIBConformance=juniRedundancyMIBConformance, juniRedundancyNotifsEnabled=juniRedundancyNotifsEnabled, juniRedundancySystemActivationHistoryTable=juniRedundancySystemActivationHistoryTable, juniRedundancyCfgGroup=juniRedundancyCfgGroup, juniRedundancyModeNotification=juniRedundancyModeNotification, juniRedundancyCfg=juniRedundancyCfg, juniRedundancyHistoryColdSwitchovers=juniRedundancyHistoryColdSwitchovers, juniRedundancyLastSystemActivationTime=juniRedundancyLastSystemActivationTime, juniRedundancyColdSwitchoverNotification=juniRedundancyColdSwitchoverNotification, juniRedundancyActiveSlotState=juniRedundancyActiveSlotState, juniRedundancyHistoryActivationType=juniRedundancyHistoryActivationType, JuniRedundancyMode=JuniRedundancyMode, juniRedundancyHistoryCurrActiveRelease=juniRedundancyHistoryCurrActiveRelease, juniRedundancyHistoryPrevActiveSlot=juniRedundancyHistoryPrevActiveSlot, juniRedundancyStatus=juniRedundancyStatus, juniRedundancyHistoryResetType=juniRedundancyHistoryResetType, juniRedundancyNotificationGroup=juniRedundancyNotificationGroup, juniRedundancyHistoryReloads=juniRedundancyHistoryReloads, juniRedundancyNotifications=juniRedundancyNotifications, juniRedundancyObjects=juniRedundancyObjects, juniRedundancyMIB=juniRedundancyMIB, juniRedundancyHistory=juniRedundancyHistory, juniRedundancySystemActivationHistoryEntry=juniRedundancySystemActivationHistoryEntry, JuniRedundancyResetReason=JuniRedundancyResetReason, juniRedundancyCfgRedundancyMode=juniRedundancyCfgRedundancyMode, juniRedundancySystemActivationHistoryTableMaxLength=juniRedundancySystemActivationHistoryTableMaxLength, juniRedundancyHistoryWarmSwitchovers=juniRedundancyHistoryWarmSwitchovers, juniRedundancyLastResetReason=juniRedundancyLastResetReason, juniRedundancyStandbySlot=juniRedundancyStandbySlot, juniRedundancyHistoryResetReason=juniRedundancyHistoryResetReason, juniRedundancyMIBGroups=juniRedundancyMIBGroups, JuniRedundancyResetType=JuniRedundancyResetType, juniRedundancyMIBCompliances=juniRedundancyMIBCompliances, JuniRedundancySystemActivationType=JuniRedundancySystemActivationType, juniRedundancyHistoryCurrActiveSlot=juniRedundancyHistoryCurrActiveSlot, juniRedundancyHaActiveTime=juniRedundancyHaActiveTime, juniRedundancyHistoryPrevActiveRelease=juniRedundancyHistoryPrevActiveRelease, juniRedundancyHistoryActivationTime=juniRedundancyHistoryActivationTime, juniRedundancyWarmSwitchoverNotification=juniRedundancyWarmSwitchoverNotification, juniRedundancyLastSystemActivationType=juniRedundancyLastSystemActivationType, juniRedundancyStandbySlotState=juniRedundancyStandbySlotState, juniRedundancyActiveSlot=juniRedundancyActiveSlot)
