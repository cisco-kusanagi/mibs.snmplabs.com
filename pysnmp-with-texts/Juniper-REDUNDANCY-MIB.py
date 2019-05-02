#
# PySNMP MIB module Juniper-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:04:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter32, ObjectIdentity, Bits, TimeTicks, NotificationType, IpAddress, Gauge32, ModuleIdentity, MibIdentifier, Integer32, iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Bits", "TimeTicks", "NotificationType", "IpAddress", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "TruthValue", "RowStatus", "DisplayString")
juniRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74))
juniRedundancyMIB.setRevisions(('2003-12-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRedundancyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniRedundancyMIB.setLastUpdated('200312122104Z')
if mibBuilder.loadTexts: juniRedundancyMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRedundancyMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Road Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniRedundancyMIB.setDescription('The redundancy configuration MIB for Juniper Networks enterprise.')
class JuniRedundancyState(TextualConvention, Integer32):
    description = 'The current state of redundancy subsystem: notKnown - Redundancy state is unknown. fileSystemSyncing - Redundancy operation is based on file system synchronization. SRP switchover stops forwarding. disabled - Redundancy operation is based on high availability model but high availability is not yet operational. SRP switchover stops forwarding. initializing - Redundancy operation is based on high availability model and standby SRP is being bulk synchronized from active SRP. SRP switchover stops forwarding. pending - Redundancy operation is based on high availability model and bulk synchronization of standby SRP completed. SRP switchover stops forwarding. active - Redundancy operation is based on high availability model and high availability is fully operational. SRP switchover does not stop forwarding.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notKnown", 1), ("fileSystemSyncing", 2), ("disabled", 3), ("initializing", 4), ("pending", 5), ("active", 6))

class JuniRedundancyMode(TextualConvention, Integer32):
    description = 'The mode of the redundancy subsystem: fileSystemSynchronization - SRP synchronization is based on file synchronization. highAvailability - SRP synchronization is based on high availability model that allows non-stop forwarding.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fileSystemSynchronization", 1), ("highAvailability", 2))

class JuniRedundancyResetReason(TextualConvention, Integer32):
    description = "Reason codes for the reset of active SRP or a line card that might result in switch of control to standby SRP or spare line card. none - No reset or switchover has occurred and indicates 'power-on' situation. notKnown - Reason is unknown. userInitiated - A safe, manual reset was initiated by the user."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("notKnown", 2), ("userInitiated", 3))

class JuniRedundancySystemActivationType(TextualConvention, Integer32):
    description = 'Various kinds of system activation: reload - System has reloaded, i.e., no switchover has occurred. coldSwitch - System switched over from active to standby SRP and the switchover involved reloading of line cards interrupting forwarding. warmSwitch - System switched over from active to standby SRP; line cards were not reloaded during switchover and forwarding was uninterrupted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reload", 1), ("coldSwitch", 2), ("warmSwitch", 3))

class JuniRedundancyResetType(TextualConvention, Integer32):
    description = 'Identifies the nature of the reset and slot types involved since the system is powered on. notKnown - Reset type is unknown. srpReload - The reset involved reloading SRP slot(s). srpSwitchover - The reset involved switchover of SRP slot(s). linecardReload - The reset involved reloading the line card slot(s). linecardSwitchover - The reset involved line card redundancy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notKnown", 1), ("srpReload", 2), ("srpSwitchover", 3), ("linecardReload", 4), ("linecardSwitchover", 5))

class JuniRedundancyHistoryCommand(TextualConvention, Integer32):
    description = 'Identifies the command to be performed on the system activation history table. keep - Retain history in persistent storage. clear - Erase the current entries of juniRedundancySystemActivationHistoryTable.'
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
if mibBuilder.loadTexts: juniRedundancyActiveSlot.setDescription('A unique identifier for active SRP slot.')
juniRedundancyActiveSlotState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 2), JuniRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyActiveSlotState.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyActiveSlotState.setDescription('The current state of redundancy on active SRP.')
juniRedundancyStandbySlot = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyStandbySlot.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyStandbySlot.setDescription('A unique identifier for standby SRP slot.')
juniRedundancyStandbySlotState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 4), JuniRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyStandbySlotState.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyStandbySlotState.setDescription('The current state of redundancy on standby SRP.')
juniRedundancyLastResetReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 5), JuniRedundancyResetReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastResetReason.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyLastResetReason.setDescription('The reason for the last SRP reset.')
juniRedundancyLastSystemActivationTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationTime.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationTime.setDescription("The value of sysUptime when the system is operational either following a reload or a switchover. The value 0 is a special value to indicate 'from reset'.")
juniRedundancyLastSystemActivationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 7), JuniRedundancySystemActivationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationType.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyLastSystemActivationType.setDescription('The type of last SRP activation when the system became operational.')
juniRedundancyHaActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHaActiveTime.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHaActiveTime.setDescription("The value of sysUptime when active SRP enters 'active' state as indicated in juniRedundancyActiveSlotState object. The value is 0 in file system synchronization redundancy mode.")
juniRedundancyNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancyNotifsEnabled.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyNotifsEnabled.setDescription('Allows enabling and disabling of redundancy subsystem notifications.')
juniRedundancyCfgRedundancyMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 2), JuniRedundancyMode().clone('fileSystemSynchronization')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancyCfgRedundancyMode.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyCfgRedundancyMode.setDescription('Indicates the redundancy mode configured on the system.')
juniRedundancySystemActivationHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTableMaxLength.setStatus('current')
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTableMaxLength.setDescription('Maximum number of entries allowed in juniRedundancySystemActivationHistoryTable. A value of 0 will result in no history being displayed in juniRedundancySystemActivationHistoryTable.')
juniRedundancySystemActivationHistoryCommand = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 2), JuniRedundancyHistoryCommand().clone('keep')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryCommand.setStatus('current')
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryCommand.setDescription('A control variable to perform certain operations on juniRedundancySystemActivationHistoryTable.')
juniRedundancySystemActivationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3), )
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTable.setStatus('current')
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryTable.setDescription('A table that tracks the history of all reloads and switchovers that have occurred since system is powered on. The maximum number of entries permissible in this table is defined by juniRedundancySystemActivationHistoryTableMaxLength. When the number of entries in the table reaches the maximum limit, the next entry would replace the oldest existing entry in the table.')
juniRedundancySystemActivationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1), ).setIndexNames((0, "Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryIndex"))
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryEntry.setDescription('The entries in this table contain the reload and switchover information. Each entry in the table is indexed by juniRedundancySystemActivationHistoryIndex. The index wraps around to 1 after reaching the maximum value.')
juniRedundancySystemActivationHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: juniRedundancySystemActivationHistoryIndex.setDescription('An integer value for the purpose of indexing system activation history table. After reaching maximum value as indicated by juniRedundancySystemActivationHistoryTableMaxLength, it wraps around to 1.')
juniRedundancyHistoryResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 2), JuniRedundancyResetType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryResetType.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryResetType.setDescription('Indicates the nature of the reset - reload or switchover - and the slot types involved. Depending on the value of this object, certain elements of JuniRedundancySystemActivationHistoryEntry will not be applicable.')
juniRedundancyHistoryActivationType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 3), JuniRedundancySystemActivationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryActivationType.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryActivationType.setDescription('Indicates the activation type of the particular historical system activation entry with respect to the slot types involved.')
juniRedundancyHistoryPrevActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveSlot.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveSlot.setDescription('Indicates the slot number of active SRP or line card that went down.')
juniRedundancyHistoryPrevActiveRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveRelease.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryPrevActiveRelease.setDescription('Indicates the system-wide boot release file name of the slot indicated by juniRedundancyHistoryPrevActiveSlot.')
juniRedundancyHistoryCurrActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveSlot.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveSlot.setDescription('Indicates the slot number of standby SRP or spare line card that took over.')
juniRedundancyHistoryCurrActiveRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveRelease.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryCurrActiveRelease.setDescription('Indicates the system-wide boot release file name of the slot indicated by juniRedundancyHistoryCurrActiveSlot.')
juniRedundancyHistoryResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 8), JuniRedundancyResetReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryResetReason.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryResetReason.setDescription('Indicates the reason for reload or switchover of the slots involved.')
juniRedundancyHistoryActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryActivationTime.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryActivationTime.setDescription('Indicates the date and time when the reload or switchover of the slots occurred.')
juniRedundancyHistoryReloads = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryReloads.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryReloads.setDescription('Indicates the number of reloads since the system is powered on.')
juniRedundancyHistoryColdSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryColdSwitchovers.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryColdSwitchovers.setDescription('Indicates the number of cold switchovers since the system is powered on.')
juniRedundancyHistoryWarmSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRedundancyHistoryWarmSwitchovers.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryWarmSwitchovers.setDescription('Indicates the number of warm switchovers since the system is powered on.')
juniRedundancyColdSwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
if mibBuilder.loadTexts: juniRedundancyColdSwitchoverNotification.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyColdSwitchoverNotification.setDescription('This notification is generated in a dual SRP system when control transfers from one to SRP to the other in file system synchronization mode or when high availability is not operational. This notification is sent by the newly active SRP immediately following the switchover in which configuration is preserved but volatile state is lost.')
juniRedundancyWarmSwitchoverNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 2)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
if mibBuilder.loadTexts: juniRedundancyWarmSwitchoverNotification.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyWarmSwitchoverNotification.setDescription('This notification is generated in a dual SRP system when control transfers from one SRP to the other and high availability is operational. This notification is sent by the newly active SRP immediately following the switchover in which configuration and volatile state are preserved.')
juniRedundancyStateEnabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 3)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStateEnabledNotification.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyStateEnabledNotification.setDescription("A state change notification sent by active SRP whenever system enters 'active' state.")
juniRedundancyStateDisabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 4)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStateDisabledNotification.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyStateDisabledNotification.setDescription("A state change notification sent by active SRP whenever system enters 'disabled' state.")
juniRedundancyStatePendingNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 5)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"))
if mibBuilder.loadTexts: juniRedundancyStatePendingNotification.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyStatePendingNotification.setDescription("A state change notification sent by active SRP whenever system enters 'pending' state.")
juniRedundancyModeNotification = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 6)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
if mibBuilder.loadTexts: juniRedundancyModeNotification.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyModeNotification.setDescription("A mode change notification sent by active SRP whenever redundancy mode of the system is changed from 'fileSystemSynchronization' to 'highAvailability' and vice versa.")
juniRedundancyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1))
juniRedundancyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2))
juniRedundancyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyStatusGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryGroup"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyMIBCompliance = juniRedundancyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyMIBCompliance.setDescription('The compliance statement for system redundancy support.')
juniRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 1)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlotState"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlotState"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationTime"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHaActiveTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyStatusGroup = juniRedundancyStatusGroup.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyStatusGroup.setDescription('The collection of redundancy status objects.')
juniRedundancyCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 2)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyNotifsEnabled"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyCfgGroup = juniRedundancyCfgGroup.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyCfgGroup.setDescription('The collection of redundancy configuration objects.')
juniRedundancyHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 3)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryTableMaxLength"), ("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryCommand"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationType"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveRelease"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveSlot"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveRelease"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetReason"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationTime"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryReloads"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryColdSwitchovers"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryWarmSwitchovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyHistoryGroup = juniRedundancyHistoryGroup.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyHistoryGroup.setDescription('The collection of redundancy history objects.')
juniRedundancyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 4)).setObjects(("Juniper-REDUNDANCY-MIB", "juniRedundancyColdSwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyWarmSwitchoverNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateEnabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateDisabledNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyStatePendingNotification"), ("Juniper-REDUNDANCY-MIB", "juniRedundancyModeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRedundancyNotificationGroup = juniRedundancyNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: juniRedundancyNotificationGroup.setDescription('The collection of notifications for redundancy events.')
mibBuilder.exportSymbols("Juniper-REDUNDANCY-MIB", juniRedundancySystemActivationHistoryTable=juniRedundancySystemActivationHistoryTable, JuniRedundancyResetType=JuniRedundancyResetType, JuniRedundancyResetReason=JuniRedundancyResetReason, PYSNMP_MODULE_ID=juniRedundancyMIB, juniRedundancyMIBGroups=juniRedundancyMIBGroups, juniRedundancyStateEnabledNotification=juniRedundancyStateEnabledNotification, juniRedundancyStateDisabledNotification=juniRedundancyStateDisabledNotification, juniRedundancyHaActiveTime=juniRedundancyHaActiveTime, juniRedundancyMIB=juniRedundancyMIB, juniRedundancyStatus=juniRedundancyStatus, JuniRedundancySystemActivationType=JuniRedundancySystemActivationType, juniRedundancyHistoryWarmSwitchovers=juniRedundancyHistoryWarmSwitchovers, juniRedundancySystemActivationHistoryCommand=juniRedundancySystemActivationHistoryCommand, JuniRedundancyState=JuniRedundancyState, juniRedundancyMIBCompliance=juniRedundancyMIBCompliance, juniRedundancyHistoryColdSwitchovers=juniRedundancyHistoryColdSwitchovers, juniRedundancyHistoryGroup=juniRedundancyHistoryGroup, juniRedundancyHistoryActivationType=juniRedundancyHistoryActivationType, juniRedundancyCfgRedundancyMode=juniRedundancyCfgRedundancyMode, juniRedundancyHistoryCurrActiveRelease=juniRedundancyHistoryCurrActiveRelease, juniRedundancyHistoryReloads=juniRedundancyHistoryReloads, juniRedundancyHistoryActivationTime=juniRedundancyHistoryActivationTime, juniRedundancyCfgGroup=juniRedundancyCfgGroup, juniRedundancyLastResetReason=juniRedundancyLastResetReason, juniRedundancyStandbySlot=juniRedundancyStandbySlot, juniRedundancyObjects=juniRedundancyObjects, juniRedundancyNotifsEnabled=juniRedundancyNotifsEnabled, juniRedundancyLastSystemActivationType=juniRedundancyLastSystemActivationType, juniRedundancyNotificationGroup=juniRedundancyNotificationGroup, juniRedundancyActiveSlot=juniRedundancyActiveSlot, juniRedundancyStatusGroup=juniRedundancyStatusGroup, juniRedundancyWarmSwitchoverNotification=juniRedundancyWarmSwitchoverNotification, juniRedundancyHistoryCurrActiveSlot=juniRedundancyHistoryCurrActiveSlot, juniRedundancyHistory=juniRedundancyHistory, juniRedundancyStandbySlotState=juniRedundancyStandbySlotState, juniRedundancyModeNotification=juniRedundancyModeNotification, juniRedundancyNotifications=juniRedundancyNotifications, juniRedundancySystemActivationHistoryTableMaxLength=juniRedundancySystemActivationHistoryTableMaxLength, juniRedundancyHistoryResetType=juniRedundancyHistoryResetType, juniRedundancyColdSwitchoverNotification=juniRedundancyColdSwitchoverNotification, juniRedundancyStatePendingNotification=juniRedundancyStatePendingNotification, juniRedundancySystemActivationHistoryIndex=juniRedundancySystemActivationHistoryIndex, juniRedundancyHistoryPrevActiveSlot=juniRedundancyHistoryPrevActiveSlot, juniRedundancyHistoryPrevActiveRelease=juniRedundancyHistoryPrevActiveRelease, juniRedundancyActiveSlotState=juniRedundancyActiveSlotState, juniRedundancyMIBCompliances=juniRedundancyMIBCompliances, juniRedundancyHistoryResetReason=juniRedundancyHistoryResetReason, juniRedundancyLastSystemActivationTime=juniRedundancyLastSystemActivationTime, JuniRedundancyMode=JuniRedundancyMode, JuniRedundancyHistoryCommand=JuniRedundancyHistoryCommand, juniRedundancyCfg=juniRedundancyCfg, juniRedundancyMIBConformance=juniRedundancyMIBConformance, juniRedundancySystemActivationHistoryEntry=juniRedundancySystemActivationHistoryEntry)
