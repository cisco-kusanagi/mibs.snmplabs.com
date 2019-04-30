#
# PySNMP MIB module DATA-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DATA-DOMAIN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, enterprises, ObjectIdentity, Unsigned32, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "enterprises", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dataDomainMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 19746))
if mibBuilder.loadTexts: dataDomainMib.setLastUpdated('200501270000Z')
if mibBuilder.loadTexts: dataDomainMib.setOrganization('Data Domain, Inc')
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
dataDomainMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0, 2))
environmentalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 1)).setObjects(("DATA-DOMAIN-MIB", "powerEnclosureID"), ("DATA-DOMAIN-MIB", "powerModuleIndex"), ("DATA-DOMAIN-MIB", "powerModuleStatus"), ("DATA-DOMAIN-MIB", "tempEnclosureID"), ("DATA-DOMAIN-MIB", "tempSensorIndex"), ("DATA-DOMAIN-MIB", "tempSensorDescription"), ("DATA-DOMAIN-MIB", "tempSensorCurrentValue"), ("DATA-DOMAIN-MIB", "tempSensorStatus"), ("DATA-DOMAIN-MIB", "fanEnclosureID"), ("DATA-DOMAIN-MIB", "fanIndex"), ("DATA-DOMAIN-MIB", "fanDescription"), ("DATA-DOMAIN-MIB", "fanLevel"), ("DATA-DOMAIN-MIB", "fanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    environmentalsGroup = environmentalsGroup.setStatus('current')
nvramGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 2)).setObjects(("DATA-DOMAIN-MIB", "nvramMemorySize"), ("DATA-DOMAIN-MIB", "nvramWindowSize"), ("DATA-DOMAIN-MIB", "nvramPCIErrorCount"), ("DATA-DOMAIN-MIB", "nvramMemoryErrorCount"), ("DATA-DOMAIN-MIB", "nvramBatteryIndex"), ("DATA-DOMAIN-MIB", "nvramBatteryStatus"), ("DATA-DOMAIN-MIB", "nvramBatteryCharge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nvramGroup = nvramGroup.setStatus('current')
fileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 3)).setObjects(("DATA-DOMAIN-MIB", "fileSystemStatus"), ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"), ("DATA-DOMAIN-MIB", "fileSystemResourceIndex"), ("DATA-DOMAIN-MIB", "fileSystemResourceName"), ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"), ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fileSystemGroup = fileSystemGroup.setStatus('current')
alertsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 4)).setObjects(("DATA-DOMAIN-MIB", "currentAlertIndex"), ("DATA-DOMAIN-MIB", "currentAlertTimestamp"), ("DATA-DOMAIN-MIB", "currentAlertDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertsGroup = alertsGroup.setStatus('current')
statisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 5)).setObjects(("DATA-DOMAIN-MIB", "systemStatsIndex"), ("DATA-DOMAIN-MIB", "cpu0PercentageBusy"), ("DATA-DOMAIN-MIB", "cpu1PercentageBusy"), ("DATA-DOMAIN-MIB", "nfsOpsPerSecond"), ("DATA-DOMAIN-MIB", "nfsIdlePercentage"), ("DATA-DOMAIN-MIB", "nfsProcPercentage"), ("DATA-DOMAIN-MIB", "nfsSendPercentage"), ("DATA-DOMAIN-MIB", "nfsReceivePercentage"), ("DATA-DOMAIN-MIB", "cifsOpsPerSecond"), ("DATA-DOMAIN-MIB", "diskReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskBusyPercentage"), ("DATA-DOMAIN-MIB", "nvramReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "nvramWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replInKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replOutKBytesPerSecond"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    statisticsGroup = statisticsGroup.setStatus('current')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 6)).setObjects(("DATA-DOMAIN-MIB", "raidDiskEnclosureID"), ("DATA-DOMAIN-MIB", "raidDiskIndex"), ("DATA-DOMAIN-MIB", "raidDiskState"), ("DATA-DOMAIN-MIB", "raidDiskGroup"), ("DATA-DOMAIN-MIB", "raidDiskStatus"), ("DATA-DOMAIN-MIB", "raidDiskReconPercentage"), ("DATA-DOMAIN-MIB", "raidDiskReconMinutes"), ("DATA-DOMAIN-MIB", "raidDiskResynchPercentage"), ("DATA-DOMAIN-MIB", "raidDiskResynchMinutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
internalDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 7)).setObjects(("DATA-DOMAIN-MIB", "diskPropEnclosureID"), ("DATA-DOMAIN-MIB", "diskPropIndex"), ("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskPerfEnclosureID"), ("DATA-DOMAIN-MIB", "diskPerfIndex"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"), ("DATA-DOMAIN-MIB", "diskErrEnclosureID"), ("DATA-DOMAIN-MIB", "diskErrIndex"), ("DATA-DOMAIN-MIB", "diskTemperature"), ("DATA-DOMAIN-MIB", "diskTimeoutCount"), ("DATA-DOMAIN-MIB", "diskReadFailCount"), ("DATA-DOMAIN-MIB", "diskWriteFailCount"), ("DATA-DOMAIN-MIB", "diskMiscFailCount"), ("DATA-DOMAIN-MIB", "diskOffTrackErrCount"), ("DATA-DOMAIN-MIB", "diskSoftEccCount"), ("DATA-DOMAIN-MIB", "diskCrcErrCount"), ("DATA-DOMAIN-MIB", "diskProbationalCount"), ("DATA-DOMAIN-MIB", "diskReallocCount"), ("DATA-DOMAIN-MIB", "diskErrState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageGroup = internalDiskStorageGroup.setStatus('current')
externalUnmanagedDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 8)).setObjects(("DATA-DOMAIN-MIB", "diskPropEnclosureID"), ("DATA-DOMAIN-MIB", "diskPropIndex"), ("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskPerfIndex"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    externalUnmanagedDiskStorageGroup = externalUnmanagedDiskStorageGroup.setStatus('current')
basicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 9)).setObjects(("DATA-DOMAIN-MIB", "powerSupplyFailedAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatShutdowntAlarm"), ("DATA-DOMAIN-MIB", "fanModuleFailedAlarm"), ("DATA-DOMAIN-MIB", "nvramFailingAlarm"), ("DATA-DOMAIN-MIB", "fileSystemFailedAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceMaintenanceAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceWarningAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceSevereAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceCriticalAlarm"), ("DATA-DOMAIN-MIB", "raidReconSevereAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalShutdownAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicNotificationsGroup = basicNotificationsGroup.setStatus('current')
internalDiskStorageNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 10)).setObjects(("DATA-DOMAIN-MIB", "diskFailingAlarm"), ("DATA-DOMAIN-MIB", "diskFailedAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatShutdowntAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageNotificationsGroup = internalDiskStorageNotificationsGroup.setStatus('current')
replGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 11)).setObjects(("DATA-DOMAIN-MIB", "replContext"), ("DATA-DOMAIN-MIB", "replState"), ("DATA-DOMAIN-MIB", "replStatus"), ("DATA-DOMAIN-MIB", "replFileSysStatus"), ("DATA-DOMAIN-MIB", "replConnTime"), ("DATA-DOMAIN-MIB", "replSource"), ("DATA-DOMAIN-MIB", "replDestination"), ("DATA-DOMAIN-MIB", "replLag"), ("DATA-DOMAIN-MIB", "replPreCompBytesSent"), ("DATA-DOMAIN-MIB", "replPostCompBytesSent"), ("DATA-DOMAIN-MIB", "replPreCompBytesRemaining"), ("DATA-DOMAIN-MIB", "replPostCompBytesReceived"), ("DATA-DOMAIN-MIB", "replThrottle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    replGroup = replGroup.setStatus('current')
power = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1))
powerModules = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1))
powerModuleTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: powerModuleTable.setStatus('mandatory')
powerModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "powerEnclosureID"), (0, "DATA-DOMAIN-MIB", "powerModuleIndex"))
if mibBuilder.loadTexts: powerModuleEntry.setStatus('mandatory')
powerEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEnclosureID.setStatus('mandatory')
powerModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 2), PowerModuleIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleIndex.setStatus('mandatory')
powerModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 3), PowerModuleStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleStatus.setStatus('mandatory')
temperatures = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1))
temperatureSensorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: temperatureSensorTable.setStatus('mandatory')
temperatureSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tempEnclosureID"), (0, "DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: temperatureSensorEntry.setStatus('mandatory')
tempEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEnclosureID.setStatus('mandatory')
tempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 2), TempSensorIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorIndex.setStatus('mandatory')
tempSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 3), TempSensorDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorDescription.setStatus('mandatory')
tempSensorCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 4), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorCurrentValue.setStatus('mandatory')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 5), TempSensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('mandatory')
fans = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3))
fanProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1))
fanPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: fanPropertiesTable.setStatus('mandatory')
fanPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fanEnclosureID"), (0, "DATA-DOMAIN-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanPropertiesEntry.setStatus('mandatory')
fanEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEnclosureID.setStatus('mandatory')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 2), FanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanIndex.setStatus('mandatory')
fanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 3), FanDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanDescription.setStatus('mandatory')
fanLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 4), FanLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanLevel.setStatus('mandatory')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 5), FanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('mandatory')
nvramProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1))
nvramMemorySize = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1), NvramMemorySize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemorySize.setStatus('mandatory')
nvramWindowSize = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 2), NvramWindowSize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWindowSize.setStatus('mandatory')
nvramStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2))
nvramPCIErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramPCIErrorCount.setStatus('mandatory')
nvramMemoryErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 2), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemoryErrorCount.setStatus('mandatory')
nvramBatteries = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3))
nvramBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1), )
if mibBuilder.loadTexts: nvramBatteryTable.setStatus('mandatory')
nvramBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramBatteryIndex"))
if mibBuilder.loadTexts: nvramBatteryEntry.setStatus('mandatory')
nvramBatteryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 1), NvramBatteryIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryIndex.setStatus('mandatory')
nvramBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 2), NvramBatteryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryStatus.setStatus('mandatory')
nvramBatteryCharge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 3), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryCharge.setStatus('mandatory')
fileSystemProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1))
fileSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 1), FileSystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemStatus.setStatus('mandatory')
fileSystemVirtualSpace = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 2), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemVirtualSpace.setStatus('mandatory')
fileSystemSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2))
fileSystemSpaceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1), )
if mibBuilder.loadTexts: fileSystemSpaceTable.setStatus('mandatory')
fileSystemSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSystemSpaceEntry.setStatus('mandatory')
fileSystemResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 1), FileSystemResourceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceIndex.setStatus('mandatory')
fileSystemResourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 2), FileSystemResourceName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceName.setStatus('mandatory')
fileSystemSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 3), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceSize.setStatus('mandatory')
fileSystemSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 4), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceUsed.setStatus('mandatory')
fileSystemSpaceAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 5), FileSystemSpaceUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceAvail.setStatus('mandatory')
fileSystemPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPercentUsed.setStatus('mandatory')
currentAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1))
currentAlertTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1), )
if mibBuilder.loadTexts: currentAlertTable.setStatus('mandatory')
currentAlertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "currentAlertIndex"))
if mibBuilder.loadTexts: currentAlertEntry.setStatus('mandatory')
currentAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 1), AlertIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertIndex.setStatus('mandatory')
currentAlertTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 2), AlertTimestamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertTimestamp.setStatus('mandatory')
currentAlertDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 3), AlertDescription()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertDescription.setStatus('mandatory')
systemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1))
systemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1), )
if mibBuilder.loadTexts: systemStatsTable.setStatus('mandatory')
systemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemStatsIndex"))
if mibBuilder.loadTexts: systemStatsEntry.setStatus('mandatory')
systemStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 1), SystemStatsIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatsIndex.setStatus('mandatory')
cpu0PercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 2), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpu0PercentageBusy.setStatus('mandatory')
cpu1PercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 3), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpu1PercentageBusy.setStatus('mandatory')
nfsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 4), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsOpsPerSecond.setStatus('mandatory')
nfsIdlePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsIdlePercentage.setStatus('mandatory')
nfsProcPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsProcPercentage.setStatus('mandatory')
nfsSendPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 7), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsSendPercentage.setStatus('mandatory')
nfsReceivePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 8), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsReceivePercentage.setStatus('mandatory')
cifsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 9), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOpsPerSecond.setStatus('mandatory')
diskReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 10), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadKBytesPerSecond.setStatus('mandatory')
diskWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 11), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteKBytesPerSecond.setStatus('mandatory')
diskBusyPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 12), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusyPercentage.setStatus('mandatory')
nvramReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 13), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramReadKBytesPerSecond.setStatus('mandatory')
nvramWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 14), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWriteKBytesPerSecond.setStatus('mandatory')
replInKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 15), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replInKBytesPerSecond.setStatus('mandatory')
replOutKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 16), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOutKBytesPerSecond.setStatus('mandatory')
diskProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1))
diskPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1), )
if mibBuilder.loadTexts: diskPropertiesTable.setStatus('mandatory')
diskPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPropEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskPropertiesEntry.setStatus('mandatory')
diskPropEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropEnclosureID.setStatus('mandatory')
diskPropIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropIndex.setStatus('mandatory')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 3), DiskModel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('mandatory')
diskFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 4), DiskFirmwareVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFirmwareVersion.setStatus('mandatory')
diskSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 5), DiskSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSerialNumber.setStatus('mandatory')
diskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 6), DiskCapacity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCapacity.setStatus('mandatory')
diskPropState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 7), DiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropState.setStatus('mandatory')
diskPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2))
diskPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1), )
if mibBuilder.loadTexts: diskPerformanceTable.setStatus('mandatory')
diskPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPerfEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPerfIndex"))
if mibBuilder.loadTexts: diskPerformanceEntry.setStatus('mandatory')
diskPerfEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfEnclosureID.setStatus('mandatory')
diskPerfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfIndex.setStatus('mandatory')
diskSectorsRead = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 3), DiskSectorsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsRead.setStatus('mandatory')
diskSectorsWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 4), DiskSectorsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsWritten.setStatus('mandatory')
diskTotalKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 5), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotalKBytes.setStatus('mandatory')
diskBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusy.setStatus('mandatory')
diskPerfState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 7), DiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfState.setStatus('mandatory')
diskReliability = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3))
diskReliabilityTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1), )
if mibBuilder.loadTexts: diskReliabilityTable.setStatus('mandatory')
diskReliabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskErrEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskReliabilityEntry.setStatus('mandatory')
diskErrEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrEnclosureID.setStatus('mandatory')
diskErrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrIndex.setStatus('mandatory')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 3), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('mandatory')
diskTimeoutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 4), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTimeoutCount.setStatus('mandatory')
diskReadFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 5), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadFailCount.setStatus('mandatory')
diskWriteFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 6), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteFailCount.setStatus('mandatory')
diskMiscFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 7), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskMiscFailCount.setStatus('mandatory')
diskOffTrackErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 8), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskOffTrackErrCount.setStatus('mandatory')
diskSoftEccCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 9), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSoftEccCount.setStatus('mandatory')
diskCrcErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 10), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCrcErrCount.setStatus('mandatory')
diskProbationalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 11), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskProbationalCount.setStatus('mandatory')
diskReallocCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 12), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReallocCount.setStatus('mandatory')
diskErrState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 13), DiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrState.setStatus('mandatory')
raidInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1))
raidInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1), )
if mibBuilder.loadTexts: raidInfoTable.setStatus('mandatory')
raidInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "raidDiskEnclosureID"), (0, "DATA-DOMAIN-MIB", "raidDiskIndex"))
if mibBuilder.loadTexts: raidInfoEntry.setStatus('mandatory')
raidDiskEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 1), EnclosureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskEnclosureID.setStatus('mandatory')
raidDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 2), DiskIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskIndex.setStatus('mandatory')
raidDiskState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 3), RaidDiskState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskState.setStatus('mandatory')
raidDiskGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 4), RaidDiskGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskGroup.setStatus('mandatory')
raidDiskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 5), RaidDiskStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskStatus.setStatus('mandatory')
raidDiskReconPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskReconPercentage.setStatus('mandatory')
raidDiskReconMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 7), Minutes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskReconMinutes.setStatus('mandatory')
raidDiskResynchPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 8), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskResynchPercentage.setStatus('mandatory')
raidDiskResynchMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 7, 1, 1, 1, 9), Minutes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidDiskResynchMinutes.setStatus('mandatory')
replicationInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1))
replicationInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1), )
if mibBuilder.loadTexts: replicationInfoTable.setStatus('mandatory')
replicationInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replContext"))
if mibBuilder.loadTexts: replicationInfoEntry.setStatus('mandatory')
replContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 1), ReplicationContext()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replContext.setStatus('mandatory')
replState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 2), ReplicationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replState.setStatus('mandatory')
replStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 3), ReplicationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replStatus.setStatus('mandatory')
replFileSysStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 4), FileSystemStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replFileSysStatus.setStatus('mandatory')
replConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 5), ReplicationConnectTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConnTime.setStatus('mandatory')
replSource = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 6), ReplicationPath()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSource.setStatus('mandatory')
replDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 7), ReplicationPath()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replDestination.setStatus('mandatory')
replLag = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 8), ReplicationLag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replLag.setStatus('mandatory')
replPreCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 9), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesSent.setStatus('mandatory')
replPostCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 10), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesSent.setStatus('mandatory')
replPreCompBytesRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 11), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesRemaining.setStatus('mandatory')
replPostCompBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 12), ReplicationTraffic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesReceived.setStatus('mandatory')
replThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 13), ReplicationThrottle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replThrottle.setStatus('mandatory')
replSyncedAsOfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 14), ReplicationSyncedTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSyncedAsOfTime.setStatus('mandatory')
powerSupplyFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 1))
if mibBuilder.loadTexts: powerSupplyFailedAlarm.setStatus('current')
systemOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 2)).setObjects(("DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: systemOverheatWarningAlarm.setStatus('current')
systemOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 3)).setObjects(("DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: systemOverheatAlertAlarm.setStatus('current')
systemOverheatShutdowntAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 4)).setObjects(("DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: systemOverheatShutdowntAlarm.setStatus('current')
fanModuleFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 5)).setObjects(("DATA-DOMAIN-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanModuleFailedAlarm.setStatus('current')
nvramFailingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 6))
if mibBuilder.loadTexts: nvramFailingAlarm.setStatus('current')
fileSystemFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 7))
if mibBuilder.loadTexts: fileSystemFailedAlarm.setStatus('current')
fileSpaceMaintenanceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 8)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceMaintenanceAlarm.setStatus('current')
fileSpaceWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 9)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceWarningAlarm.setStatus('current')
fileSpaceSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 10)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceSevereAlarm.setStatus('current')
fileSpaceCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 11)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSpaceCriticalAlarm.setStatus('current')
diskFailingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 12)).setObjects(("DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskFailingAlarm.setStatus('current')
diskFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 13)).setObjects(("DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskFailedAlarm.setStatus('current')
diskOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 14)).setObjects(("DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskOverheatWarningAlarm.setStatus('current')
diskOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 15)).setObjects(("DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskOverheatAlertAlarm.setStatus('current')
diskOverheatShutdowntAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 16)).setObjects(("DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskOverheatShutdowntAlarm.setStatus('current')
raidReconSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 17))
if mibBuilder.loadTexts: raidReconSevereAlarm.setStatus('current')
raidReconCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 18))
if mibBuilder.loadTexts: raidReconCriticalAlarm.setStatus('current')
raidReconCriticalShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 19))
if mibBuilder.loadTexts: raidReconCriticalShutdownAlarm.setStatus('current')
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", fileSystemSpaceUsed=fileSystemSpaceUsed, dd580g=dd580g, dd460=dd460, DiskIndex=DiskIndex, dd430=dd430, ErrorCount=ErrorCount, raidDiskReconPercentage=raidDiskReconPercentage, replInKBytesPerSecond=replInKBytesPerSecond, replPostCompBytesReceived=replPostCompBytesReceived, ReplicationPath=ReplicationPath, raid=raid, nvramMemoryErrorCount=nvramMemoryErrorCount, diskProbationalCount=diskProbationalCount, dataDomainMibGroups=dataDomainMibGroups, TempSensorDescription=TempSensorDescription, fileSystemSpaceTable=fileSystemSpaceTable, powerModuleStatus=powerModuleStatus, FileSystemSpaceUnit=FileSystemSpaceUnit, diskTotalKBytes=diskTotalKBytes, dd580=dd580, PowerModuleStatus=PowerModuleStatus, diskErrState=diskErrState, fanPropertiesEntry=fanPropertiesEntry, statistics=statistics, fileSystemSpace=fileSystemSpace, fanIndex=fanIndex, Minutes=Minutes, TempSensorIndex=TempSensorIndex, diskOverheatWarningAlarm=diskOverheatWarningAlarm, replPreCompBytesSent=replPreCompBytesSent, systemOverheatShutdowntAlarm=systemOverheatShutdowntAlarm, raidDiskIndex=raidDiskIndex, ddModelUnsupported=ddModelUnsupported, dd410=dd410, nvramReadKBytesPerSecond=nvramReadKBytesPerSecond, raidDiskStatus=raidDiskStatus, temperatures=temperatures, dataDomainMibObjects=dataDomainMibObjects, DiskCapacity=DiskCapacity, diskReliabilityTable=diskReliabilityTable, raidInfo=raidInfo, nvramBatteryTable=nvramBatteryTable, diskFirmwareVersion=diskFirmwareVersion, diskPropertiesEntry=diskPropertiesEntry, power=power, nvramStats=nvramStats, systemStatsIndex=systemStatsIndex, diskSectorsWritten=diskSectorsWritten, diskSerialNumber=diskSerialNumber, dd565=dd565, replicationInfoEntry=replicationInfoEntry, nfsIdlePercentage=nfsIdlePercentage, nfsOpsPerSecond=nfsOpsPerSecond, AlertDescription=AlertDescription, nvramWindowSize=nvramWindowSize, currentAlerts=currentAlerts, currentAlertTable=currentAlertTable, dd590g=dd590g, EnclosureID=EnclosureID, replicationInfoTable=replicationInfoTable, RaidDiskState=RaidDiskState, diskMiscFailCount=diskMiscFailCount, raidInfoEntry=raidInfoEntry, systemStatsTable=systemStatsTable, dd460g=dd460g, replSource=replSource, ReplicationThrottle=ReplicationThrottle, replLag=replLag, replConnTime=replConnTime, fileSystemResourceName=fileSystemResourceName, fanModuleFailedAlarm=fanModuleFailedAlarm, ReplicationConnectTime=ReplicationConnectTime, fileSystemStatus=fileSystemStatus, FanStatus=FanStatus, dataDomainMibNotifications=dataDomainMibNotifications, PowerModuleIndex=PowerModuleIndex, DiskFirmwareVersion=DiskFirmwareVersion, powerEnclosureID=powerEnclosureID, DiskState=DiskState, diskCapacity=diskCapacity, diskErrEnclosureID=diskErrEnclosureID, dd560=dd560, diskReliabilityEntry=diskReliabilityEntry, replPreCompBytesRemaining=replPreCompBytesRemaining, diskPropState=diskPropState, nvramBatteryEntry=nvramBatteryEntry, cpu1PercentageBusy=cpu1PercentageBusy, dd200Proto=dd200Proto, replPostCompBytesSent=replPostCompBytesSent, diskSoftEccCount=diskSoftEccCount, RaidDiskGroup=RaidDiskGroup, nfsSendPercentage=nfsSendPercentage, raidInfoTable=raidInfoTable, currentAlertTimestamp=currentAlertTimestamp, Temperature=Temperature, replThrottle=replThrottle, replSyncedAsOfTime=replSyncedAsOfTime, RaidDiskStatus=RaidDiskStatus, currentAlertIndex=currentAlertIndex, powerModuleEntry=powerModuleEntry, replOutKBytesPerSecond=replOutKBytesPerSecond, diskFailingAlarm=diskFailingAlarm, dd200=dd200, nvramBatteryStatus=nvramBatteryStatus, FanIndex=FanIndex, currentAlertDescription=currentAlertDescription, products=products, fileSystemPercentUsed=fileSystemPercentUsed, diskOffTrackErrCount=diskOffTrackErrCount, diskPropIndex=diskPropIndex, diskFailedAlarm=diskFailedAlarm, systemStatsEntry=systemStatsEntry, nvramPCIErrorCount=nvramPCIErrorCount, diskReliability=diskReliability, dd510=dd510, DiskSectorsPerSecond=DiskSectorsPerSecond, diskBusyPercentage=diskBusyPercentage, AlertTimestamp=AlertTimestamp, currentAlertEntry=currentAlertEntry, environmentalsGroup=environmentalsGroup, NvramWindowSize=NvramWindowSize, internalDiskStorageNotificationsGroup=internalDiskStorageNotificationsGroup, nvramMemorySize=nvramMemorySize, PYSNMP_MODULE_ID=dataDomainMib, dd400g=dd400g, DiskSerialNumber=DiskSerialNumber, dataDomainMibCompliances=dataDomainMibCompliances, tempSensorIndex=tempSensorIndex, nvramBatteryIndex=nvramBatteryIndex, raidGroup=raidGroup, nvramGroup=nvramGroup, basicNotificationsGroup=basicNotificationsGroup, internalDiskStorageGroup=internalDiskStorageGroup, fileSystem=fileSystem, powerModuleIndex=powerModuleIndex, diskSectorsRead=diskSectorsRead, diskCrcErrCount=diskCrcErrCount, raidDiskResynchPercentage=raidDiskResynchPercentage, raidReconSevereAlarm=raidReconSevereAlarm, temperatureSensorTable=temperatureSensorTable, fileSpaceMaintenanceAlarm=fileSpaceMaintenanceAlarm, NvramBatteryIndex=NvramBatteryIndex, fileSystemProperties=fileSystemProperties, nvramFailingAlarm=nvramFailingAlarm, diskOverheatShutdowntAlarm=diskOverheatShutdowntAlarm, diskBusy=diskBusy, diskWriteKBytesPerSecond=diskWriteKBytesPerSecond, tempSensorCurrentValue=tempSensorCurrentValue, NvramBytesTransferred=NvramBytesTransferred, fileSystemSpaceSize=fileSystemSpaceSize, diskTimeoutCount=diskTimeoutCount, fileSpaceWarningAlarm=fileSpaceWarningAlarm, fanProperties=fanProperties, cpu0PercentageBusy=cpu0PercentageBusy, diskPerformance=diskPerformance, diskPerfState=diskPerfState, environmentals=environmentals, FanLevel=FanLevel, fanEnclosureID=fanEnclosureID, replDestination=replDestination, NvramBatteryStatus=NvramBatteryStatus, raidDiskEnclosureID=raidDiskEnclosureID, diskErrIndex=diskErrIndex, raidDiskGroup=raidDiskGroup, systemOverheatAlertAlarm=systemOverheatAlertAlarm, replContext=replContext, diskPerfEnclosureID=diskPerfEnclosureID, fileSystemVirtualSpace=fileSystemVirtualSpace, statisticsGroup=statisticsGroup, nvramBatteries=nvramBatteries, dd590=dd590, TempSensorStatus=TempSensorStatus, diskPropertiesTable=diskPropertiesTable, DiskModel=DiskModel, ReplicationTraffic=ReplicationTraffic, Percentage=Percentage, fans=fans, diskModel=diskModel, externalUnmanagedDiskStorageGroup=externalUnmanagedDiskStorageGroup, tempSensorDescription=tempSensorDescription, replication=replication, fanPropertiesTable=fanPropertiesTable, nfsReceivePercentage=nfsReceivePercentage, diskStorage=diskStorage, fanLevel=fanLevel, powerSupplyFailedAlarm=powerSupplyFailedAlarm, fileSpaceSevereAlarm=fileSpaceSevereAlarm, FileSystemResourceIndex=FileSystemResourceIndex, diskPerformanceTable=diskPerformanceTable, AlertIndex=AlertIndex, temperatureSensorEntry=temperatureSensorEntry, tempEnclosureID=tempEnclosureID, powerModuleTable=powerModuleTable, fileSystemSpaceAvail=fileSystemSpaceAvail, powerModules=powerModules, NvramMemorySize=NvramMemorySize, fanStatus=fanStatus, raidReconCriticalShutdownAlarm=raidReconCriticalShutdownAlarm, tempSensorStatus=tempSensorStatus, dd530=dd530, dataDomainMib=dataDomainMib, raidDiskResynchMinutes=raidDiskResynchMinutes, fileSystemFailedAlarm=fileSystemFailedAlarm, dataDomainMibConformance=dataDomainMibConformance, dataDomainMibCompliance=dataDomainMibCompliance, fanDescription=fanDescription, dd560g=dd560g, nvramProperties=nvramProperties, nvram=nvram, nfsProcPercentage=nfsProcPercentage, replState=replState, cifsOpsPerSecond=cifsOpsPerSecond, nvramBatteryCharge=nvramBatteryCharge, diskPerfIndex=diskPerfIndex, fileSystemGroup=fileSystemGroup, alerts=alerts, KBytesPerSecond=KBytesPerSecond, FanDescription=FanDescription, raidDiskState=raidDiskState, SystemStatsIndex=SystemStatsIndex, ReplicationLag=ReplicationLag, replicationInfo=replicationInfo, ReplicationStatus=ReplicationStatus, FileSystemResourceName=FileSystemResourceName, diskReadFailCount=diskReadFailCount, raidDiskReconMinutes=raidDiskReconMinutes, ReplicationState=ReplicationState, nvramWriteKBytesPerSecond=nvramWriteKBytesPerSecond, diskWriteFailCount=diskWriteFailCount, fileSystemResourceIndex=fileSystemResourceIndex, fileSystemSpaceEntry=fileSystemSpaceEntry, dd120=dd120, diskProperties=diskProperties, replFileSysStatus=replFileSysStatus, ReplicationSyncedTime=ReplicationSyncedTime, temperatureSensors=temperatureSensors, diskOverheatAlertAlarm=diskOverheatAlertAlarm, alertsGroup=alertsGroup, diskPerformanceEntry=diskPerformanceEntry, fileSpaceCriticalAlarm=fileSpaceCriticalAlarm, FileSystemStatus=FileSystemStatus, replGroup=replGroup, diskReallocCount=diskReallocCount, raidReconCriticalAlarm=raidReconCriticalAlarm, restorer=restorer, diskPropEnclosureID=diskPropEnclosureID, ReplicationContext=ReplicationContext, diskReadKBytesPerSecond=diskReadKBytesPerSecond, diskTemperature=diskTemperature, replStatus=replStatus, systemOverheatWarningAlarm=systemOverheatWarningAlarm, systemStats=systemStats, OpsPerSecond=OpsPerSecond)
