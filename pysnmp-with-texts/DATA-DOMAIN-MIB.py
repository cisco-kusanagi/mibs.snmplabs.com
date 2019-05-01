#
# PySNMP MIB module DATA-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DATA-DOMAIN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, MibIdentifier, Bits, Unsigned32, Counter64, IpAddress, NotificationType, enterprises, ObjectIdentity, ModuleIdentity, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "Counter64", "IpAddress", "NotificationType", "enterprises", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dataDomainMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 19746))
if mibBuilder.loadTexts: dataDomainMib.setLastUpdated('200501270000Z')
if mibBuilder.loadTexts: dataDomainMib.setOrganization('Data Domain, Inc')
if mibBuilder.loadTexts: dataDomainMib.setContactInfo('Phone: +1-650-565-7300 Fax: +1-650-424-1057')
if mibBuilder.loadTexts: dataDomainMib.setDescription('This MIB is used for managing the suite of Data Domain Products.')
dataDomainMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0))
dataDomainMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1))
environmentals = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1))
nvram = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2))
fileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3))
alerts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4))
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 5))
diskStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6))
raid = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 7))
replication = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8))
dataDomainMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 2))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3))
restorer = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1))
dd200 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 1))
dd200Proto = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 2))
dd410 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 3))
dd430 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 4))
dd460 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 5))
dd400g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 6))
dd460g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 7))
dd560 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 8))
dd560g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 9))
dd580 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 10))
dd580g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 11))
dd565 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 12))
dd530 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 13))
dd510 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 14))
dd120 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 15))
dd590 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 16))
dd590g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 17))
ddModelUnsupported = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 9999))
class EnclosureID(Integer32):
    pass

class Temperature(Integer32):
    pass

class Minutes(Integer32):
    pass

class Percentage(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class KBytesPerSecond(Counter32):
    pass

class OpsPerSecond(Counter32):
    pass

class ErrorCount(Counter32):
    pass

class PowerModuleIndex(Integer32):
    pass

class PowerModuleStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("fail", 3))

class TempSensorIndex(Integer32):
    pass

class TempSensorDescription(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class TempSensorStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("absent", 0), ("ok", 1), ("notfound", 2))

class FanIndex(Integer32):
    pass

class FanDescription(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class FanLevel(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("low", 1), ("normal", 2), ("high", 3))

class FanStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notfound", 0), ("ok", 1), ("fail", 2))

class NvramMemorySize(Integer32):
    pass

class NvramWindowSize(Integer32):
    pass

class NvramBytesTransferred(Integer32):
    pass

class NvramBatteryIndex(Integer32):
    pass

class NvramBatteryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ok", 1), ("disabled", 2), ("discharged", 3), ("unknown", 4), ("softdisabled", 5))

class DiskIndex(Integer32):
    pass

class DiskModel(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskFirmwareVersion(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskSerialNumber(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskCapacity(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 20)

class DiskState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("absent", 3), ("failed", 4))

class DiskSectorsPerSecond(Counter32):
    pass

class FileSystemStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("running", 3), ("unknown", 4))

class FileSystemResourceIndex(Integer32):
    pass

class FileSystemResourceName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class FileSystemSpaceUnit(Counter32):
    pass

class AlertIndex(Integer32):
    pass

class AlertTimestamp(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class AlertDescription(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class SystemStatsIndex(Integer32):
    pass

class RaidDiskState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("inuse", 1), ("notinuse", 2), ("spare", 3), ("absent", 4), ("failed", 5), ("unknown", 6))

class RaidDiskStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("reconstructing", 2), ("resynching", 3), ("unknown", 4))

class RaidDiskGroup(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class ReplicationState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("disabledNeedsResync", 3))

class ReplicationStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("connected", 1), ("disconnected", 2), ("migrating", 3), ("suspended", 4), ("neverConnected", 5))

class ReplicationConnectTime(Integer32):
    pass

class ReplicationPath(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 254)

class ReplicationLag(Integer32):
    pass

class ReplicationTraffic(Integer32):
    pass

class ReplicationThrottle(Integer32):
    pass

class ReplicationSyncedTime(Integer32):
    pass

class ReplicationContext(Integer32):
    pass

dataDomainMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0, 1))
dataDomainMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 1)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroup"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "raidGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "basicNotificationsGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageNotificationsGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibCompliance = dataDomainMibCompliance.setStatus('current')
if mibBuilder.loadTexts: dataDomainMibCompliance.setDescription('The compliance statement for SNMP entities which implement this MIB module.')
dataDomainMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0, 2))
environmentalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 1)).setObjects(("DATA-DOMAIN-MIB", "powerEnclosureID"), ("DATA-DOMAIN-MIB", "powerModuleIndex"), ("DATA-DOMAIN-MIB", "powerModuleStatus"), ("DATA-DOMAIN-MIB", "tempEnclosureID"), ("DATA-DOMAIN-MIB", "tempSensorIndex"), ("DATA-DOMAIN-MIB", "tempSensorDescription"), ("DATA-DOMAIN-MIB", "tempSensorCurrentValue"), ("DATA-DOMAIN-MIB", "tempSensorStatus"), ("DATA-DOMAIN-MIB", "fanEnclosureID"), ("DATA-DOMAIN-MIB", "fanIndex"), ("DATA-DOMAIN-MIB", "fanDescription"), ("DATA-DOMAIN-MIB", "fanLevel"), ("DATA-DOMAIN-MIB", "fanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    environmentalsGroup = environmentalsGroup.setStatus('current')
if mibBuilder.loadTexts: environmentalsGroup.setDescription('A collection of objects providing environmental monitoring information.')
nvramGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 2)).setObjects(("DATA-DOMAIN-MIB", "nvramMemorySize"), ("DATA-DOMAIN-MIB", "nvramWindowSize"), ("DATA-DOMAIN-MIB", "nvramPCIErrorCount"), ("DATA-DOMAIN-MIB", "nvramMemoryErrorCount"), ("DATA-DOMAIN-MIB", "nvramBatteryIndex"), ("DATA-DOMAIN-MIB", "nvramBatteryStatus"), ("DATA-DOMAIN-MIB", "nvramBatteryCharge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nvramGroup = nvramGroup.setStatus('current')
if mibBuilder.loadTexts: nvramGroup.setDescription('A collection of objects providing nvram monitoring information.')
fileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 3)).setObjects(("DATA-DOMAIN-MIB", "fileSystemStatus"), ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"), ("DATA-DOMAIN-MIB", "fileSystemResourceIndex"), ("DATA-DOMAIN-MIB", "fileSystemResourceName"), ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"), ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fileSystemGroup = fileSystemGroup.setStatus('current')
if mibBuilder.loadTexts: fileSystemGroup.setDescription('A collection of objects providing file system monitoring information.')
alertsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 4)).setObjects(("DATA-DOMAIN-MIB", "currentAlertIndex"), ("DATA-DOMAIN-MIB", "currentAlertTimestamp"), ("DATA-DOMAIN-MIB", "currentAlertDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertsGroup = alertsGroup.setStatus('current')
if mibBuilder.loadTexts: alertsGroup.setDescription('A collection of objects providing alert monitoring information.')
statisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 5)).setObjects(("DATA-DOMAIN-MIB", "systemStatsIndex"), ("DATA-DOMAIN-MIB", "cpu0PercentageBusy"), ("DATA-DOMAIN-MIB", "cpu1PercentageBusy"), ("DATA-DOMAIN-MIB", "nfsOpsPerSecond"), ("DATA-DOMAIN-MIB", "nfsIdlePercentage"), ("DATA-DOMAIN-MIB", "nfsProcPercentage"), ("DATA-DOMAIN-MIB", "nfsSendPercentage"), ("DATA-DOMAIN-MIB", "nfsReceivePercentage"), ("DATA-DOMAIN-MIB", "cifsOpsPerSecond"), ("DATA-DOMAIN-MIB", "diskReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskBusyPercentage"), ("DATA-DOMAIN-MIB", "nvramReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "nvramWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replInKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replOutKBytesPerSecond"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    statisticsGroup = statisticsGroup.setStatus('current')
if mibBuilder.loadTexts: statisticsGroup.setDescription('A collection of objects providing statistics information.')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 6)).setObjects(("DATA-DOMAIN-MIB", "raidDiskEnclosureID"), ("DATA-DOMAIN-MIB", "raidDiskIndex"), ("DATA-DOMAIN-MIB", "raidDiskState"), ("DATA-DOMAIN-MIB", "raidDiskGroup"), ("DATA-DOMAIN-MIB", "raidDiskStatus"), ("DATA-DOMAIN-MIB", "raidDiskReconPercentage"), ("DATA-DOMAIN-MIB", "raidDiskReconMinutes"), ("DATA-DOMAIN-MIB", "raidDiskResynchPercentage"), ("DATA-DOMAIN-MIB", "raidDiskResynchMinutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
if mibBuilder.loadTexts: raidGroup.setDescription('A collection of objects providing raid monitoring information.')
internalDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 7)).setObjects(("DATA-DOMAIN-MIB", "diskPropEnclosureID"), ("DATA-DOMAIN-MIB", "diskPropIndex"), ("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskPerfEnclosureID"), ("DATA-DOMAIN-MIB", "diskPerfIndex"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"), ("DATA-DOMAIN-MIB", "diskErrEnclosureID"), ("DATA-DOMAIN-MIB", "diskErrIndex"), ("DATA-DOMAIN-MIB", "diskTemperature"), ("DATA-DOMAIN-MIB", "diskTimeoutCount"), ("DATA-DOMAIN-MIB", "diskReadFailCount"), ("DATA-DOMAIN-MIB", "diskWriteFailCount"), ("DATA-DOMAIN-MIB", "diskMiscFailCount"), ("DATA-DOMAIN-MIB", "diskOffTrackErrCount"), ("DATA-DOMAIN-MIB", "diskSoftEccCount"), ("DATA-DOMAIN-MIB", "diskCrcErrCount"), ("DATA-DOMAIN-MIB", "diskProbationalCount"), ("DATA-DOMAIN-MIB", "diskReallocCount"), ("DATA-DOMAIN-MIB", "diskErrState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageGroup = internalDiskStorageGroup.setStatus('current')
if mibBuilder.loadTexts: internalDiskStorageGroup.setDescription('A collection of objects providing internal disk monitoring information.')
externalUnmanagedDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 8)).setObjects(("DATA-DOMAIN-MIB", "diskPropEnclosureID"), ("DATA-DOMAIN-MIB", "diskPropIndex"), ("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskPerfIndex"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    externalUnmanagedDiskStorageGroup = externalUnmanagedDiskStorageGroup.setStatus('current')
if mibBuilder.loadTexts: externalUnmanagedDiskStorageGroup.setDescription('A collection of objects providing internal disk monitoring information.')
basicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 9)).setObjects(("DATA-DOMAIN-MIB", "powerSupplyFailedAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatShutdowntAlarm"), ("DATA-DOMAIN-MIB", "fanModuleFailedAlarm"), ("DATA-DOMAIN-MIB", "nvramFailingAlarm"), ("DATA-DOMAIN-MIB", "fileSystemFailedAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceMaintenanceAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceWarningAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceSevereAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceCriticalAlarm"), ("DATA-DOMAIN-MIB", "raidReconSevereAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalShutdownAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicNotificationsGroup = basicNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: basicNotificationsGroup.setDescription('A collection of objects providing basic notifications.')
internalDiskStorageNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 10)).setObjects(("DATA-DOMAIN-MIB", "diskFailingAlarm"), ("DATA-DOMAIN-MIB", "diskFailedAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatShutdowntAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageNotificationsGroup = internalDiskStorageNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: internalDiskStorageNotificationsGroup.setDescription('A collection of objects providing internal disk storage notifications.')
replGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 11)).setObjects(("DATA-DOMAIN-MIB", "replContext"), ("DATA-DOMAIN-MIB", "replState"), ("DATA-DOMAIN-MIB", "replStatus"), ("DATA-DOMAIN-MIB", "replFileSysStatus"), ("DATA-DOMAIN-MIB", "replConnTime"), ("DATA-DOMAIN-MIB", "replSource"), ("DATA-DOMAIN-MIB", "replDestination"), ("DATA-DOMAIN-MIB", "replLag"), ("DATA-DOMAIN-MIB", "replPreCompBytesSent"), ("DATA-DOMAIN-MIB", "replPostCompBytesSent"), ("DATA-DOMAIN-MIB", "replPreCompBytesRemaining"), ("DATA-DOMAIN-MIB", "replPostCompBytesReceived"), ("DATA-DOMAIN-MIB", "replThrottle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    replGroup = replGroup.setStatus('current')
if mibBuilder.loadTexts: replGroup.setDescription('a collection of objects providing replication pair config and monitoring information.')
power = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1))
powerModules = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1))
powerModuleTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: powerModuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: powerModuleTable.setDescription('A table containing entries of PowerModuleEntry.')
powerModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "powerEnclosureID"), (0, "DATA-DOMAIN-MIB", "powerModuleIndex"))
if mibBuilder.loadTexts: powerModuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: powerModuleEntry.setDescription('powerModuleTable Row Description')
powerEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: powerEnclosureID.setDescription('Power Module Enclosure ID')
powerModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 2), PowerModuleIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: powerModuleIndex.setDescription('Power Module index')
powerModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 3), PowerModuleStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleStatus.setStatus('mandatory')
if mibBuilder.loadTexts: powerModuleStatus.setDescription('current enclosure Power Module status')
temperatures = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1))
temperatureSensorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: temperatureSensorTable.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureSensorTable.setDescription('A table containing entries of TemperatureSensorEntry.')
temperatureSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tempEnclosureID"), (0, "DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: temperatureSensorEntry.setStatus('mandatory')
if mibBuilder.loadTexts: temperatureSensorEntry.setDescription('temperatureSensorTable Row Description')
tempEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: tempEnclosureID.setDescription('Temperature Sensor Enclosure ID')
tempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 2), TempSensorIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorIndex.setStatus('mandatory')
if mibBuilder.loadTexts: tempSensorIndex.setDescription('Temperature Sensor Number')
tempSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 3), TempSensorDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorDescription.setStatus('mandatory')
if mibBuilder.loadTexts: tempSensorDescription.setDescription('Temperature Sensor Description')
tempSensorCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 4), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorCurrentValue.setStatus('mandatory')
if mibBuilder.loadTexts: tempSensorCurrentValue.setDescription('Current Temperature Value of the sensor')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 5), TempSensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('mandatory')
if mibBuilder.loadTexts: tempSensorStatus.setDescription('Current status of the sensor')
fans = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3))
fanProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1))
fanPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: fanPropertiesTable.setStatus('mandatory')
if mibBuilder.loadTexts: fanPropertiesTable.setDescription('A table containing entries of FanPropertiesEntry.')
fanPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fanEnclosureID"), (0, "DATA-DOMAIN-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanPropertiesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fanPropertiesEntry.setDescription('fanPropertiesTable Row Description')
fanEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: fanEnclosureID.setDescription('Enclosure ID of fan')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 2), FanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fanIndex.setDescription('Fan Number')
fanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 3), FanDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanDescription.setStatus('mandatory')
if mibBuilder.loadTexts: fanDescription.setDescription('Vendor supplied description of the fan')
fanLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 4), FanLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanLevel.setStatus('mandatory')
if mibBuilder.loadTexts: fanLevel.setDescription('current run level of fan')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 5), FanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fanStatus.setDescription('Current status of the fan')
nvramProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1))
nvramMemorySize = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1), NvramMemorySize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemorySize.setStatus('mandatory')
if mibBuilder.loadTexts: nvramMemorySize.setDescription('Size of NVRAM Memory in megabytes')
nvramWindowSize = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 2), NvramWindowSize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWindowSize.setStatus('mandatory')
if mibBuilder.loadTexts: nvramWindowSize.setDescription('Window size of NVRAM in megabytes')
nvramStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2))
nvramPCIErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramPCIErrorCount.setStatus('mandatory')
if mibBuilder.loadTexts: nvramPCIErrorCount.setDescription('Number of PCI Errors Encountered on NVRAM Card')
nvramMemoryErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 2), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemoryErrorCount.setStatus('mandatory')
if mibBuilder.loadTexts: nvramMemoryErrorCount.setDescription('Number of Memory Errors Encountered on NVRAM Card')
nvramBatteries = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3))
nvramBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1), )
if mibBuilder.loadTexts: nvramBatteryTable.setStatus('mandatory')
if mibBuilder.loadTexts: nvramBatteryTable.setDescription('A table containing entries of NvramBatteryEntry.')
nvramBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramBatteryIndex"))
if mibBuilder.loadTexts: nvramBatteryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nvramBatteryEntry.setDescription('nvramBatteryTable Row Description')
nvramBatteryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 1), NvramBatteryIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nvramBatteryIndex.setDescription('NVRAM Battery Number')
nvramBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 2), NvramBatteryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nvramBatteryStatus.setDescription('NVRAM Battery Status')
nvramBatteryCharge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 3), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryCharge.setStatus('mandatory')
if mibBuilder.loadTexts: nvramBatteryCharge.setDescription('NVRAM Battery change percentage')
fileSystemProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1))
fileSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 1), FileSystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemStatus.setDescription('Status of the file system')
fileSystemVirtualSpace = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 2), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemVirtualSpace.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemVirtualSpace.setDescription('Amount of Uncompressed data that has been backed up by the system')
fileSystemSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2))
fileSystemSpaceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1), )
if mibBuilder.loadTexts: fileSystemSpaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemSpaceTable.setDescription('A table containing entries of FileSystemSpaceEntry.')
fileSystemSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSystemSpaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemSpaceEntry.setDescription('fileSystemSpaceTable Row Description')
fileSystemResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 1), FileSystemResourceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemResourceIndex.setDescription('File system resource index')
fileSystemResourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 2), FileSystemResourceName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceName.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemResourceName.setDescription('File system resource name')
fileSystemSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 3), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceSize.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemSpaceSize.setDescription('Size of the file system resource in gigabytes')
fileSystemSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 4), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceUsed.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemSpaceUsed.setDescription('Amount of used space within the file system resource in gigabytes')
fileSystemSpaceAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 5), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceAvail.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemSpaceAvail.setDescription('Amount of available space within the file system resource in gigabytes')
fileSystemPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPercentUsed.setStatus('mandatory')
if mibBuilder.loadTexts: fileSystemPercentUsed.setDescription('Percentage of used space within the file system resource')
currentAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1))
currentAlertTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1), )
if mibBuilder.loadTexts: currentAlertTable.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlertTable.setDescription('A table containing entries of CurrentAlertEntry.')
currentAlertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "currentAlertIndex"))
if mibBuilder.loadTexts: currentAlertEntry.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlertEntry.setDescription('currentAlertTable Row Description')
currentAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 1), AlertIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertIndex.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlertIndex.setDescription('Current Alert Row index')
currentAlertTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 2), AlertTimestamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlertTimestamp.setDescription('Timestamp of current alert')
currentAlertDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 3), AlertDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertDescription.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlertDescription.setDescription('Alert Description')
systemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1))
systemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1), )
if mibBuilder.loadTexts: systemStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: systemStatsTable.setDescription('A table containing entries of SystemStatsEntry.')
systemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemStatsIndex"))
if mibBuilder.loadTexts: systemStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: systemStatsEntry.setDescription('systemStatsTable Row Description')
systemStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 1), SystemStatsIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: systemStatsIndex.setDescription('System Stats Row index')
cpu0PercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 2), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpu0PercentageBusy.setStatus('mandatory')
if mibBuilder.loadTexts: cpu0PercentageBusy.setDescription('CPU 0 Percentage Busy')
cpu1PercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 3), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpu1PercentageBusy.setStatus('mandatory')
if mibBuilder.loadTexts: cpu1PercentageBusy.setDescription('CPU 1 Percentage Busy')
nfsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 4), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsOpsPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: nfsOpsPerSecond.setDescription('Number of NFS Operations performed per second')
nfsIdlePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsIdlePercentage.setStatus('mandatory')
if mibBuilder.loadTexts: nfsIdlePercentage.setDescription('Percentage of time NFS was Idle')
nfsProcPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsProcPercentage.setStatus('mandatory')
if mibBuilder.loadTexts: nfsProcPercentage.setDescription('Percentage of time NFS was processing')
nfsSendPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 7), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsSendPercentage.setStatus('mandatory')
if mibBuilder.loadTexts: nfsSendPercentage.setDescription('Percentage of time NFS was sending requests')
nfsReceivePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 8), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsReceivePercentage.setStatus('mandatory')
if mibBuilder.loadTexts: nfsReceivePercentage.setDescription('Percentage of time NFS was receiving requests')
cifsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 9), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOpsPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: cifsOpsPerSecond.setDescription('Number of CIFS Operations performed per second')
diskReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 10), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadKBytesPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: diskReadKBytesPerSecond.setDescription('Number of KBytes per second read from disk')
diskWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 11), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteKBytesPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: diskWriteKBytesPerSecond.setDescription('Number of KBytes per second read from disk')
diskBusyPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 12), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusyPercentage.setStatus('mandatory')
if mibBuilder.loadTexts: diskBusyPercentage.setDescription('Percentage of Time Disks were busy')
nvramReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 13), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramReadKBytesPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: nvramReadKBytesPerSecond.setDescription('Number of KBytes read per second from NVRAM')
nvramWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 14), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWriteKBytesPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: nvramWriteKBytesPerSecond.setDescription('Number of KBytes read per second from NVRAM')
replInKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 15), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replInKBytesPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: replInKBytesPerSecond.setDescription('Number of KBytes per second received for Replication')
replOutKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 16), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOutKBytesPerSecond.setStatus('mandatory')
if mibBuilder.loadTexts: replOutKBytesPerSecond.setDescription('Number of KBytes per second sent for Replication')
diskProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1))
diskPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1), )
if mibBuilder.loadTexts: diskPropertiesTable.setStatus('mandatory')
if mibBuilder.loadTexts: diskPropertiesTable.setDescription('A table containing entries of DiskPropertiesEntry.')
diskPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPropEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskPropertiesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: diskPropertiesEntry.setDescription('diskPropertiesTable Row Description')
diskPropEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: diskPropEnclosureID.setDescription('Enclosure ID of disk')
diskPropIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropIndex.setStatus('mandatory')
if mibBuilder.loadTexts: diskPropIndex.setDescription('Disk Number')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 3), DiskModel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('mandatory')
if mibBuilder.loadTexts: diskModel.setDescription('Manufacture and model of the disk')
diskFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 4), DiskFirmwareVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFirmwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: diskFirmwareVersion.setDescription('Firmware version of the disk')
diskSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 5), DiskSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: diskSerialNumber.setDescription('Serial Number of the disk')
diskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 6), DiskCapacity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: diskCapacity.setDescription('Capacity of the disk')
diskPropState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 7), DiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropState.setStatus('mandatory')
if mibBuilder.loadTexts: diskPropState.setDescription('Current State of the disk')
diskPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2))
diskPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1), )
if mibBuilder.loadTexts: diskPerformanceTable.setStatus('mandatory')
if mibBuilder.loadTexts: diskPerformanceTable.setDescription('A table containing entries of DiskPerformanceEntry.')
diskPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPerfEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPerfIndex"))
if mibBuilder.loadTexts: diskPerformanceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: diskPerformanceEntry.setDescription('diskPerformanceTable Row Description')
diskPerfEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: diskPerfEnclosureID.setDescription('Enclosure ID of disk')
diskPerfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: diskPerfIndex.setDescription('Disk Number')
diskSectorsRead = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 3), DiskSectorsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsRead.setStatus('mandatory')
if mibBuilder.loadTexts: diskSectorsRead.setDescription('Number of disk sectors read per second')
diskSectorsWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 4), DiskSectorsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsWritten.setStatus('mandatory')
if mibBuilder.loadTexts: diskSectorsWritten.setDescription('Number of disk sectors written per second')
diskTotalKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 5), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotalKBytes.setStatus('mandatory')
if mibBuilder.loadTexts: diskTotalKBytes.setDescription('Total Number of Kilo-bytes read/written per second')
diskBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusy.setStatus('mandatory')
if mibBuilder.loadTexts: diskBusy.setDescription('Percentage of time disk is busy')
diskPerfState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 7), DiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfState.setStatus('mandatory')
if mibBuilder.loadTexts: diskPerfState.setDescription('Current State of the disk')
diskReliability = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3))
diskReliabilityTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1), )
if mibBuilder.loadTexts: diskReliabilityTable.setStatus('mandatory')
if mibBuilder.loadTexts: diskReliabilityTable.setDescription('A table containing entries of DiskReliabilityEntry.')
diskReliabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskErrEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskReliabilityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: diskReliabilityEntry.setDescription('diskReliabilityTable Row Description')
diskErrEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: diskErrEnclosureID.setDescription('Enclosure ID of disk')
diskErrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrIndex.setStatus('mandatory')
if mibBuilder.loadTexts: diskErrIndex.setDescription('Disk Number')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 3), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: diskTemperature.setDescription('Current Disk Temperature in Celsius')
diskTimeoutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 4), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTimeoutCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskTimeoutCount.setDescription('Number of command timeouts')
diskReadFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 5), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadFailCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskReadFailCount.setDescription('Number of read failures')
diskWriteFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 6), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteFailCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskWriteFailCount.setDescription('Number of write failures')
diskMiscFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 7), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskMiscFailCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskMiscFailCount.setDescription('Number of miscellaneous failures')
diskOffTrackErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 8), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskOffTrackErrCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskOffTrackErrCount.setDescription('Number of offtrack errors')
diskSoftEccCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 9), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSoftEccCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskSoftEccCount.setDescription('Number of soft ecc errors')
diskCrcErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 10), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCrcErrCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskCrcErrCount.setDescription('Number of crc errors')
diskProbationalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 11), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskProbationalCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskProbationalCount.setDescription('Number of probational errors')
diskReallocCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 12), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReallocCount.setStatus('mandatory')
if mibBuilder.loadTexts: diskReallocCount.setDescription('Number of reallocation errors')
diskErrState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 13), DiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrState.setStatus('mandatory')
if mibBuilder.loadTexts: diskErrState.setDescription('Current State of the disk')
raidInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1))
raidInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1), )
if mibBuilder.loadTexts: raidInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: raidInfoTable.setDescription('A table containing entries of RaidInfoEntry.')
raidInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "raidDiskEnclosureID"), (0, "DATA-DOMAIN-MIB", "raidDiskIndex"))
if mibBuilder.loadTexts: raidInfoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: raidInfoEntry.setDescription('raidInfoTable Row Description')
raidDiskEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskEnclosureID.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskEnclosureID.setDescription('Enclosure id of raid disk')
raidDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskIndex.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskIndex.setDescription('Disk Number of raid disk')
raidDiskState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 3), RaidDiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskState.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskState.setDescription('State of raid disk')
raidDiskGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 4), RaidDiskGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskGroup.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskGroup.setDescription('Disk Group of raid disk')
raidDiskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 5), RaidDiskStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskStatus.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskStatus.setDescription('Status of raid disk')
raidDiskReconPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskReconPercentage.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskReconPercentage.setDescription('Reconstruction Percentage complete if raidDiskStatus = reconstructing')
raidDiskReconMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 7), Minutes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskReconMinutes.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskReconMinutes.setDescription('Number of minutes reconstruction has taken if raidDiskStatus = reconstructing')
raidDiskResynchPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 8), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskResynchPercentage.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskResynchPercentage.setDescription('Resynch Percentage complete if raidDiskStatus = resynching')
raidDiskResynchMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 9), Minutes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskResynchMinutes.setStatus('mandatory')
if mibBuilder.loadTexts: raidDiskResynchMinutes.setDescription('Number of minutes resynching has taken if raidDiskStatus = resynching')
replicationInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1))
replicationInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1), )
if mibBuilder.loadTexts: replicationInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: replicationInfoTable.setDescription('A table containing entries of ReplicationInfoEntry.')
replicationInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replContext"))
if mibBuilder.loadTexts: replicationInfoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: replicationInfoEntry.setDescription('replicationInfoTable Row Description')
replContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 1), ReplicationContext()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replContext.setStatus('mandatory')
if mibBuilder.loadTexts: replContext.setDescription('context ID of replication source/dest pair')
replState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 2), ReplicationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replState.setStatus('mandatory')
if mibBuilder.loadTexts: replState.setDescription('state of replication source/dest pair')
replStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 3), ReplicationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replStatus.setStatus('mandatory')
if mibBuilder.loadTexts: replStatus.setDescription('status of replication source/dest pair connection')
replFileSysStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 4), FileSystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replFileSysStatus.setStatus('mandatory')
if mibBuilder.loadTexts: replFileSysStatus.setDescription('status of filesystem')
replConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 5), ReplicationConnectTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConnTime.setStatus('mandatory')
if mibBuilder.loadTexts: replConnTime.setDescription("time of connection established between source and dest, or time since disconnect if status is 'disconnected'")
replSource = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 6), ReplicationPath()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSource.setStatus('mandatory')
if mibBuilder.loadTexts: replSource.setDescription('network path to replication source directory')
replDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 7), ReplicationPath()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replDestination.setStatus('mandatory')
if mibBuilder.loadTexts: replDestination.setDescription('network path to replication destination directory')
replLag = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 8), ReplicationLag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replLag.setStatus('mandatory')
if mibBuilder.loadTexts: replLag.setDescription('time lag between source and destination')
replPreCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 9), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesSent.setStatus('mandatory')
if mibBuilder.loadTexts: replPreCompBytesSent.setDescription('pre compression bytes sent')
replPostCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 10), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesSent.setStatus('mandatory')
if mibBuilder.loadTexts: replPostCompBytesSent.setDescription('post compression bytes sent')
replPreCompBytesRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 11), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesRemaining.setStatus('mandatory')
if mibBuilder.loadTexts: replPreCompBytesRemaining.setDescription('pre compression bytes remaining')
replPostCompBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 12), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesReceived.setStatus('mandatory')
if mibBuilder.loadTexts: replPostCompBytesReceived.setDescription('post compression bytes received')
replThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 13), ReplicationThrottle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replThrottle.setStatus('mandatory')
if mibBuilder.loadTexts: replThrottle.setDescription('replication throttle in bps -- -1 is disabled, 0 unlimited')
replSyncedAsOfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 14), ReplicationSyncedTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSyncedAsOfTime.setStatus('mandatory')
if mibBuilder.loadTexts: replSyncedAsOfTime.setDescription('time when the source and destination were in sync, or 0 if the time is unknown')
powerSupplyFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 1))
if mibBuilder.loadTexts: powerSupplyFailedAlarm.setStatus('current')
if mibBuilder.loadTexts: powerSupplyFailedAlarm.setDescription('Meaning: Power Supply failed What to do: replace the power supply')
systemOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 2)).setObjects(("DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: systemOverheatWarningAlarm.setStatus('current')
if mibBuilder.loadTexts: systemOverheatWarningAlarm.setDescription("Meaning: the temperature reading of one of the thermometers in the Chassis has exceeded the 'warning' temperature level. If it continues to rise, it may eventually trigger a shutdown of the DDR. The index value of the alarm indicates the thermometer index that may be looked up in the environmentals table 'temperatures' for more information about the actual thermometer reading the high value. What to do: check the Fan status, temperatures of the environment in which the DDR is, and other factors which may increase the temperature.")
systemOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 3)).setObjects(("DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: systemOverheatAlertAlarm.setStatus('current')
if mibBuilder.loadTexts: systemOverheatAlertAlarm.setDescription("Meaning: the temperature reading of one of the thermometers in the Chassis is more than halfway between the 'warning' and 'shutdown' temperature levels. If it continues to rise, it may eventually trigger a shutdown of the DDR. The index value of the alarm indicates the thermometer index that may be looked up in the environmentals table 'temperatures' for more information about the actual thermometer reading the high value. What to do: check the Fan status, temperatures of the environment in which the DDR is, and other factors which may increase the system temperature.")
systemOverheatShutdowntAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 4)).setObjects(("DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: systemOverheatShutdowntAlarm.setStatus('current')
if mibBuilder.loadTexts: systemOverheatShutdowntAlarm.setDescription("Meaning: the temperature reading of one of the thermometers in the Chassis has reached or exceeded the 'shutdown' temperature level. The DDR will be shutdown to prevent damage to the system. The index value of the alarm indicates the thermometer index that may be looked up in the environmentals table 'temperatures' for more information about the actual thermometer reading the high value. What to do: Once the system has been brought back up, after checking for high environment temperatures or other factors which may increase the system temperature, check other environmental values, such as Fan Status, Disk Temperatures, etc...")
fanModuleFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 5)).setObjects(("DATA-DOMAIN-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanModuleFailedAlarm.setStatus('current')
if mibBuilder.loadTexts: fanModuleFailedAlarm.setDescription("Meaning: a Fan Module in the enclosure has failed. The index of the fan is given as the index of the alarm. This same index can be looked up in the environmentals table 'fanProperies' for more information about which fan has failed. What to do: replace the fan")
nvramFailingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 6))
if mibBuilder.loadTexts: nvramFailingAlarm.setStatus('current')
if mibBuilder.loadTexts: nvramFailingAlarm.setDescription("Meaning: The system has detected that the NVRAM is potentially failing. There has been an excessive amount of PCI or Memory errors. The nvram tables 'nvramProperties' and 'nvramStats' may provide for information on why the NVRAM is failing. What to do: check the status of the NVRAM after reboot, and replace if the errors continue.")
fileSystemFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 7))
if mibBuilder.loadTexts: fileSystemFailedAlarm.setStatus('current')
if mibBuilder.loadTexts: fileSystemFailedAlarm.setDescription('Meaning: The File System process on the DDR has had a serious problem and has had to restart. What to do: check the system logs for conditions that may be triggering the failure. Other alarms may also indicate why the File System is having problems.')
fileSpaceMaintenanceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 8)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceMaintenanceAlarm.setStatus('current')
if mibBuilder.loadTexts: fileSpaceMaintenanceAlarm.setDescription('Meaning: DDVAR File System Resource Space is running low for system maintenance activities. The system may not have enough space for the routine system activities to run without error. What to do: Delete unneeded files, such as old log files, support bundles, core files, upgrade rpm files stored in the /ddvar file system. Consider upgrading the hardware or adding shelves to high-end units. Reducing the retention times for backup data can also help. When files are deleted from outside of the /ddvar space, filesys clean will have to be done before the space is recovered.')
fileSpaceWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 9)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceWarningAlarm.setStatus('current')
if mibBuilder.loadTexts: fileSpaceWarningAlarm.setDescription("Meaning: A File System Resource space is 90% utilized. The index value of the alarm indicates the file system index that may be looked up in the fileSystem table 'fileSystemSpace' for more information about the actual FS that is getting full. What to do: Delete unneeded files, such as old log files, support bundles, core files, upgrade rpm files stored in the /ddvar file system. Consider upgrading the hardware or adding shelves to high-end units. Reducing the retention times for backup data can also help. When files are deleted from outside of the /ddvar space, filesys clean will have to be done before the space is recovered.")
fileSpaceSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 10)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceSevereAlarm.setStatus('current')
if mibBuilder.loadTexts: fileSpaceSevereAlarm.setDescription("Meaning: A File System Resource space is 95% utilized. The index value of the alarm indicates the file system index that may be looked up in the fileSystem table 'fileSystemSpace' for more information about the actual FS that is getting full. What to do: Delete unneeded files, such as old log files, support bundles, core files, upgrade rpm files stored in the /ddvar file system. Consider upgrading the hardware or adding shelves to high-end units. Reducing the retention times for backup data can also help. When files are deleted from outside of the /ddvar space, filesys clean will have to be done before the space is recovered.")
fileSpaceCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 11)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceCriticalAlarm.setStatus('current')
if mibBuilder.loadTexts: fileSpaceCriticalAlarm.setDescription("Meaning: A File System Resource space is 100% utilized. The index value of the alarm indicates the file system index that may be looked up in the fileSystem table 'fileSystemSpace' for more information about the actual FS that is full. What to do: Delete unneeded files, such as old log files, support bundles, core files, upgrade rpm files stored in the /ddvar file system. Consider upgrading the hardware or adding shelves to high-end units. Reducing the retention times for backup data can also help. When files are deleted from outside of the /ddvar space, filesys clean will have to be done before the space is recovered.")
diskFailingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 12)).setObjects(("DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskFailingAlarm.setStatus('current')
if mibBuilder.loadTexts: diskFailingAlarm.setDescription("Meaning: some problem has been detected about the indicated disk. The index value of the alarm indicates the disk index that may be looked up in the disk tables 'diskProperties', 'diskPerformance', and 'diskReliability' for more information about the actual disk that is failing. What to do: monitor the status of the disk, and consider replacing if the problem continues.")
diskFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 13)).setObjects(("DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskFailedAlarm.setStatus('current')
if mibBuilder.loadTexts: diskFailedAlarm.setDescription("Meaning: some problem has been detected about the indicated disk. The index value of the alarm indicates the disk index that may be looked up in the disk tables 'diskProperties', 'diskPerformance', and 'diskReliability' for more information about the actual disk that has failed. What to do: replace the disk.")
diskOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 14)).setObjects(("DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskOverheatWarningAlarm.setStatus('current')
if mibBuilder.loadTexts: diskOverheatWarningAlarm.setDescription("Meaning: the temperature reading of the indicated disk has exceeded the 'warning' temperature level. If it continues to rise, it may eventually trigger a shutdown of the DDR. The index value of the alarm indicates the disk index that may be looked up in the disk tables 'diskProperties', 'diskPerformance', and 'diskReliability' for more information about the actual disk reading the high value. What to do: check the disk status, temperatures of the environment in which the DDR is, and other factors which may increase the temperature.")
diskOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 15)).setObjects(("DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskOverheatAlertAlarm.setStatus('current')
if mibBuilder.loadTexts: diskOverheatAlertAlarm.setDescription("Meaning: the temperature reading of the indicated disk is more than halfway between the 'warning' and 'shutdown' temperature levels. If it continues to rise, it will trigger a shutdown of the DDR. The index value of the alarm indicates the disk index that may be looked up in the disk tables 'diskProperties', 'diskPerformance', and 'diskReliability' for more information about the actual disk reading the high value. What to do: check the disk status, temperatures of the environment in which the DDR is, and other factors which may increase the temperature. If the temperature continues stays at this level or rises, and no other disks are reading this trouble, consider 'failing' the disk, and get a replacement.")
diskOverheatShutdowntAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 16)).setObjects(("DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskOverheatShutdowntAlarm.setStatus('current')
if mibBuilder.loadTexts: diskOverheatShutdowntAlarm.setDescription("Meaning: the temperature reading of the indicated disk has surpassed the 'shutdown' temperature level. The DDR will be shutdown. The index value of the alarm indicates the disk index that may be looked up in the disk tables 'diskProperties', 'diskPerformance', and 'diskReliability' for more information about the actual disk reading the high value. What to do: Boot the DDR and monitor the status and temperatures. If the same disk has continued problems, consider 'failing' it and get a replacement disk.")
raidReconSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 17))
if mibBuilder.loadTexts: raidReconSevereAlarm.setStatus('current')
if mibBuilder.loadTexts: raidReconSevereAlarm.setDescription("Meaning: Raid group reconstruction is currently active and has not completed after 71 hours. Reconstruction occurs when the raid group falls into 'degraded' mode. This can happen due to a disk failing at run-time or boot-up. What to do: while it is still possible that the reconstruction could succeed, the disk should be replaced to ensure data safety.")
raidReconCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 18))
if mibBuilder.loadTexts: raidReconCriticalAlarm.setStatus('current')
if mibBuilder.loadTexts: raidReconCriticalAlarm.setDescription("Meaning: Raid group reconstruction is currently active and has not completed after 72 hours. Reconstruction occurs when the raid group falls into 'degraded' mode. This can happen due to a disk failing at run-time or boot-up. What to do: the disk should be replaced to ensure data safety.")
raidReconCriticalShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 19))
if mibBuilder.loadTexts: raidReconCriticalShutdownAlarm.setStatus('current')
if mibBuilder.loadTexts: raidReconCriticalShutdownAlarm.setDescription("Meaning: Raid group reconstruction is currently active and has not completed after more than 72 hours. Reconstruction occurs when the raid group falls into 'degraded' mode. This can happen due to a disk failing at run-time or boot-up. What to do: the disk must be replaced.")
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", FanStatus=FanStatus, diskBusyPercentage=diskBusyPercentage, AlertDescription=AlertDescription, raidDiskStatus=raidDiskStatus, tempSensorDescription=tempSensorDescription, replPreCompBytesRemaining=replPreCompBytesRemaining, diskReliability=diskReliability, systemOverheatWarningAlarm=systemOverheatWarningAlarm, raidDiskResynchPercentage=raidDiskResynchPercentage, internalDiskStorageGroup=internalDiskStorageGroup, ErrorCount=ErrorCount, replicationInfoTable=replicationInfoTable, nvramStats=nvramStats, diskProperties=diskProperties, fileSystemSpaceUsed=fileSystemSpaceUsed, raidInfo=raidInfo, SystemStatsIndex=SystemStatsIndex, dataDomainMibGroups=dataDomainMibGroups, replInKBytesPerSecond=replInKBytesPerSecond, raidDiskIndex=raidDiskIndex, powerModuleStatus=powerModuleStatus, replContext=replContext, fileSpaceMaintenanceAlarm=fileSpaceMaintenanceAlarm, temperatureSensorTable=temperatureSensorTable, replPostCompBytesReceived=replPostCompBytesReceived, diskOverheatWarningAlarm=diskOverheatWarningAlarm, PYSNMP_MODULE_ID=dataDomainMib, fileSystemSpaceAvail=fileSystemSpaceAvail, raidDiskReconMinutes=raidDiskReconMinutes, dd120=dd120, DiskFirmwareVersion=DiskFirmwareVersion, powerSupplyFailedAlarm=powerSupplyFailedAlarm, replOutKBytesPerSecond=replOutKBytesPerSecond, diskStorage=diskStorage, diskErrIndex=diskErrIndex, nvramBatteryTable=nvramBatteryTable, tempSensorCurrentValue=tempSensorCurrentValue, replSyncedAsOfTime=replSyncedAsOfTime, diskBusy=diskBusy, DiskIndex=DiskIndex, Temperature=Temperature, RaidDiskStatus=RaidDiskStatus, diskCrcErrCount=diskCrcErrCount, tempEnclosureID=tempEnclosureID, NvramBatteryIndex=NvramBatteryIndex, ReplicationTraffic=ReplicationTraffic, powerEnclosureID=powerEnclosureID, diskReallocCount=diskReallocCount, raid=raid, diskReliabilityTable=diskReliabilityTable, alerts=alerts, replPreCompBytesSent=replPreCompBytesSent, diskReliabilityEntry=diskReliabilityEntry, dd460g=dd460g, fanStatus=fanStatus, systemStatsEntry=systemStatsEntry, nfsProcPercentage=nfsProcPercentage, dd580=dd580, dd590g=dd590g, PowerModuleIndex=PowerModuleIndex, nvramBatteryCharge=nvramBatteryCharge, diskReadFailCount=diskReadFailCount, fileSystemFailedAlarm=fileSystemFailedAlarm, Percentage=Percentage, dataDomainMibCompliances=dataDomainMibCompliances, diskPropIndex=diskPropIndex, raidDiskReconPercentage=raidDiskReconPercentage, diskPropEnclosureID=diskPropEnclosureID, FanIndex=FanIndex, FileSystemStatus=FileSystemStatus, ReplicationThrottle=ReplicationThrottle, diskPerfIndex=diskPerfIndex, diskPerformanceEntry=diskPerformanceEntry, raidDiskGroup=raidDiskGroup, dd510=dd510, fileSystemProperties=fileSystemProperties, replDestination=replDestination, raidInfoEntry=raidInfoEntry, dd410=dd410, TempSensorIndex=TempSensorIndex, powerModuleEntry=powerModuleEntry, nvramWriteKBytesPerSecond=nvramWriteKBytesPerSecond, systemStatsIndex=systemStatsIndex, replSource=replSource, nvramWindowSize=nvramWindowSize, diskPerfEnclosureID=diskPerfEnclosureID, statistics=statistics, FileSystemSpaceUnit=FileSystemSpaceUnit, products=products, dd530=dd530, diskErrEnclosureID=diskErrEnclosureID, replicationInfo=replicationInfo, dd400g=dd400g, ReplicationSyncedTime=ReplicationSyncedTime, fileSystemSpaceTable=fileSystemSpaceTable, dd430=dd430, DiskCapacity=DiskCapacity, diskSerialNumber=diskSerialNumber, dd565=dd565, ddModelUnsupported=ddModelUnsupported, replState=replState, replGroup=replGroup, internalDiskStorageNotificationsGroup=internalDiskStorageNotificationsGroup, environmentals=environmentals, TempSensorStatus=TempSensorStatus, currentAlertEntry=currentAlertEntry, diskFirmwareVersion=diskFirmwareVersion, currentAlerts=currentAlerts, OpsPerSecond=OpsPerSecond, ReplicationStatus=ReplicationStatus, diskOverheatShutdowntAlarm=diskOverheatShutdowntAlarm, DiskState=DiskState, fileSystemSpace=fileSystemSpace, diskWriteFailCount=diskWriteFailCount, dd460=dd460, externalUnmanagedDiskStorageGroup=externalUnmanagedDiskStorageGroup, diskSectorsRead=diskSectorsRead, fileSpaceWarningAlarm=fileSpaceWarningAlarm, dataDomainMibNotifications=dataDomainMibNotifications, NvramMemorySize=NvramMemorySize, diskReadKBytesPerSecond=diskReadKBytesPerSecond, nvramMemoryErrorCount=nvramMemoryErrorCount, replStatus=replStatus, powerModuleIndex=powerModuleIndex, fanPropertiesEntry=fanPropertiesEntry, fileSystemVirtualSpace=fileSystemVirtualSpace, dd200=dd200, diskPerformance=diskPerformance, alertsGroup=alertsGroup, dd560g=dd560g, nvramPCIErrorCount=nvramPCIErrorCount, nvramBatteryStatus=nvramBatteryStatus, replPostCompBytesSent=replPostCompBytesSent, AlertIndex=AlertIndex, diskTotalKBytes=diskTotalKBytes, ReplicationContext=ReplicationContext, diskPerformanceTable=diskPerformanceTable, systemOverheatAlertAlarm=systemOverheatAlertAlarm, RaidDiskState=RaidDiskState, ReplicationState=ReplicationState, dd560=dd560, NvramBatteryStatus=NvramBatteryStatus, ReplicationPath=ReplicationPath, DiskSectorsPerSecond=DiskSectorsPerSecond, FanDescription=FanDescription, nvramGroup=nvramGroup, cifsOpsPerSecond=cifsOpsPerSecond, KBytesPerSecond=KBytesPerSecond, dataDomainMibConformance=dataDomainMibConformance, diskPropertiesTable=diskPropertiesTable, diskMiscFailCount=diskMiscFailCount, fileSystemPercentUsed=fileSystemPercentUsed, replConnTime=replConnTime, fanPropertiesTable=fanPropertiesTable, AlertTimestamp=AlertTimestamp, cpu0PercentageBusy=cpu0PercentageBusy, diskOffTrackErrCount=diskOffTrackErrCount, diskTimeoutCount=diskTimeoutCount, systemStats=systemStats, nvramReadKBytesPerSecond=nvramReadKBytesPerSecond, fanProperties=fanProperties, powerModuleTable=powerModuleTable, diskFailedAlarm=diskFailedAlarm, replThrottle=replThrottle, nvramBatteries=nvramBatteries, diskFailingAlarm=diskFailingAlarm, DiskSerialNumber=DiskSerialNumber, environmentalsGroup=environmentalsGroup, diskSectorsWritten=diskSectorsWritten, diskProbationalCount=diskProbationalCount, tempSensorStatus=tempSensorStatus, diskErrState=diskErrState, fileSpaceCriticalAlarm=fileSpaceCriticalAlarm, DiskModel=DiskModel, statisticsGroup=statisticsGroup, dataDomainMib=dataDomainMib, dataDomainMibObjects=dataDomainMibObjects, cpu1PercentageBusy=cpu1PercentageBusy, fileSystemStatus=fileSystemStatus, temperatureSensorEntry=temperatureSensorEntry, fans=fans, tempSensorIndex=tempSensorIndex, currentAlertIndex=currentAlertIndex, nfsOpsPerSecond=nfsOpsPerSecond, diskPropState=diskPropState, replFileSysStatus=replFileSysStatus, nvramBatteryIndex=nvramBatteryIndex, fileSystem=fileSystem, dd580g=dd580g, power=power, diskModel=diskModel, dd200Proto=dd200Proto, replication=replication, temperatureSensors=temperatureSensors, FileSystemResourceName=FileSystemResourceName, replLag=replLag, raidDiskEnclosureID=raidDiskEnclosureID, raidReconCriticalAlarm=raidReconCriticalAlarm, ReplicationLag=ReplicationLag, NvramWindowSize=NvramWindowSize, dd590=dd590, currentAlertDescription=currentAlertDescription, currentAlertTimestamp=currentAlertTimestamp, raidDiskResynchMinutes=raidDiskResynchMinutes, systemOverheatShutdowntAlarm=systemOverheatShutdowntAlarm, diskPerfState=diskPerfState, basicNotificationsGroup=basicNotificationsGroup, raidDiskState=raidDiskState, raidGroup=raidGroup, TempSensorDescription=TempSensorDescription, Minutes=Minutes, raidInfoTable=raidInfoTable, fileSystemGroup=fileSystemGroup, fileSpaceSevereAlarm=fileSpaceSevereAlarm, fileSystemSpaceSize=fileSystemSpaceSize, restorer=restorer, nvramBatteryEntry=nvramBatteryEntry, NvramBytesTransferred=NvramBytesTransferred, nvramMemorySize=nvramMemorySize, EnclosureID=EnclosureID, FanLevel=FanLevel, nfsReceivePercentage=nfsReceivePercentage, diskWriteKBytesPerSecond=diskWriteKBytesPerSecond, fanEnclosureID=fanEnclosureID, diskPropertiesEntry=diskPropertiesEntry, diskSoftEccCount=diskSoftEccCount, nvram=nvram, nvramFailingAlarm=nvramFailingAlarm, raidReconCriticalShutdownAlarm=raidReconCriticalShutdownAlarm, diskOverheatAlertAlarm=diskOverheatAlertAlarm, PowerModuleStatus=PowerModuleStatus, temperatures=temperatures, dataDomainMibCompliance=dataDomainMibCompliance, fileSystemResourceName=fileSystemResourceName, currentAlertTable=currentAlertTable, ReplicationConnectTime=ReplicationConnectTime, nfsIdlePercentage=nfsIdlePercentage, diskTemperature=diskTemperature, replicationInfoEntry=replicationInfoEntry, fanLevel=fanLevel, nfsSendPercentage=nfsSendPercentage, powerModules=powerModules, nvramProperties=nvramProperties, fanIndex=fanIndex, fanDescription=fanDescription, diskCapacity=diskCapacity, fanModuleFailedAlarm=fanModuleFailedAlarm, RaidDiskGroup=RaidDiskGroup, FileSystemResourceIndex=FileSystemResourceIndex, raidReconSevereAlarm=raidReconSevereAlarm, fileSystemResourceIndex=fileSystemResourceIndex, systemStatsTable=systemStatsTable, fileSystemSpaceEntry=fileSystemSpaceEntry)
