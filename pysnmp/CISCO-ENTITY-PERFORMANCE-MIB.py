#
# PySNMP MIB module CISCO-ENTITY-PERFORMANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-PERFORMANCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, IpAddress, MibIdentifier, Bits, iso, Gauge32, TimeTicks, Counter64, Unsigned32, NotificationType, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "IpAddress", "MibIdentifier", "Bits", "iso", "Gauge32", "TimeTicks", "Counter64", "Unsigned32", "NotificationType", "ModuleIdentity", "ObjectIdentity")
TimeStamp, TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
ciscoEntityPerformanceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 756))
ciscoEntityPerformanceMIB.setRevisions(('2014-06-18 00:00', '2010-09-09 00:00',))
if mibBuilder.loadTexts: ciscoEntityPerformanceMIB.setLastUpdated('201406180000Z')
if mibBuilder.loadTexts: ciscoEntityPerformanceMIB.setOrganization('Cisco Systems, Inc.')
class CiscoEntPerfMeasurement(TextualConvention, Counter64):
    status = 'current'

class CiscoEntPerfRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rangePercentage", 1), ("rangeInt32", 2), ("rangeInt64", 3))

class CiscoEntPerfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("utilization", 1), ("bitInputRate", 2), ("bitOutputRate", 3), ("bitDropRate", 4), ("packetInputRate", 5), ("packetOutputRate", 6), ("packetDropRate", 7))

class CiscoEntPerfInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("current", 1), ("oneMinute", 2), ("fiveMinutes", 3), ("fifteenMinutes", 4))

class CiscoEntPerfHistInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("oneMinute", 1), ("fiveMinutes", 2), ("fifteenMinutes", 3))

class CiscoEntPerfIntervalAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("current", 3), ("algoSMA", 4))

ciscoEntityPerformanceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 0))
ciscoEntityPerformanceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 1))
ciscoEntityPerformanceMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 2))
cepEntityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1), )
if mibBuilder.loadTexts: cepEntityTable.setStatus('current')
cepEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cepEntityEntry.setStatus('current')
cepEntityNumReloads = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1, 1), Counter32()).setUnits('reloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepEntityNumReloads.setStatus('current')
cepEntityLastReloadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepEntityLastReloadTime.setStatus('current')
cepConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2), )
if mibBuilder.loadTexts: cepConfigTable.setStatus('current')
cepConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigInterval"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"))
if mibBuilder.loadTexts: cepConfigEntry.setStatus('current')
cepConfigInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 1), CiscoEntPerfInterval())
if mibBuilder.loadTexts: cepConfigInterval.setStatus('current')
cepConfigPerfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 2), CiscoEntPerfType())
if mibBuilder.loadTexts: cepConfigPerfType.setStatus('current')
cepConfigPerfRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 3), CiscoEntPerfRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepConfigPerfRange.setStatus('current')
cepConfigRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 4), CiscoEntPerfMeasurement()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepConfigRisingThreshold.setStatus('current')
cepConfigFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 5), CiscoEntPerfMeasurement()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepConfigFallingThreshold.setStatus('current')
cepConfigThresholdNotifEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepConfigThresholdNotifEnabled.setStatus('current')
cepStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3), )
if mibBuilder.loadTexts: cepStatsTable.setStatus('current')
cepStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigInterval"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"))
if mibBuilder.loadTexts: cepStatsEntry.setStatus('current')
cepStatsAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1, 1), CiscoEntPerfIntervalAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepStatsAlgorithm.setStatus('current')
cepStatsMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1, 2), CiscoEntPerfMeasurement()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepStatsMeasurement.setStatus('current')
cepEntityIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4), )
if mibBuilder.loadTexts: cepEntityIntervalTable.setStatus('current')
cepEntityIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepHistInterval"))
if mibBuilder.loadTexts: cepEntityIntervalEntry.setStatus('current')
cepHistInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 1), CiscoEntPerfHistInterval())
if mibBuilder.loadTexts: cepHistInterval.setStatus('current')
cepIntervalTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalTimeElapsed.setStatus('current')
cepValidIntervalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepValidIntervalCount.setStatus('current')
cepIntervalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5), )
if mibBuilder.loadTexts: cepIntervalStatsTable.setStatus('current')
cepIntervalStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepHistInterval"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalNumber"))
if mibBuilder.loadTexts: cepIntervalStatsEntry.setStatus('current')
cepIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: cepIntervalNumber.setStatus('current')
cepIntervalStatsValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsValidData.setStatus('current')
cepIntervalStatsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 3), CiscoEntPerfRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsRange.setStatus('current')
cepIntervalStatsMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 4), CiscoEntPerfMeasurement()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsMeasurement.setStatus('current')
cepIntervalStatsCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsCreateTime.setStatus('current')
ciscoEntityPerformanceMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6))
cepThroughputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7), )
if mibBuilder.loadTexts: cepThroughputTable.setStatus('current')
cepThroughputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cepThroughputEntry.setStatus('current')
cepThroughputLicensedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 1), Counter64()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepThroughputLicensedBW.setStatus('current')
cepThroughputLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("exceed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepThroughputLevel.setStatus('current')
cepThroughputInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThroughputInterval.setStatus('current')
cepThroughputThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(75, 95))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThroughputThreshold.setStatus('current')
cepThroughputAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 5), Counter64()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepThroughputAvgRate.setStatus('current')
cepThresholdNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThresholdNotifEnabled.setStatus('current')
cepThroughputNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThroughputNotifEnabled.setStatus('current')
cepPerfThreshRisingEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 1)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigRisingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
if mibBuilder.loadTexts: cepPerfThreshRisingEvent.setStatus('current')
cepPerfThreshFallingEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 2)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigFallingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
if mibBuilder.loadTexts: cepPerfThreshFallingEvent.setStatus('current')
cepThroughputNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 3)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLicensedBW"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLevel"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputAvgRate"))
if mibBuilder.loadTexts: cepThroughputNotif.setStatus('current')
ciscoEntityPerformanceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 1))
ciscoEntityPerformanceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2))
ciscoEntityPerformanceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 1, 1)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBEntityGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBConfigGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBNotificationGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBPerfStatsGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBIntervalStatsGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBNotifControlGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBEntityIntervalGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBThroughputGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBCompliance = ciscoEntityPerformanceMIBCompliance.setStatus('current')
ciscoEntityPerformanceMIBEntityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 1)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepEntityNumReloads"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepEntityLastReloadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBEntityGroup = ciscoEntityPerformanceMIBEntityGroup.setStatus('current')
ciscoEntityPerformanceMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 2)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigRisingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigFallingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigThresholdNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBConfigGroup = ciscoEntityPerformanceMIBConfigGroup.setStatus('current')
ciscoEntityPerformanceMIBPerfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 3)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsAlgorithm"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBPerfStatsGroup = ciscoEntityPerformanceMIBPerfStatsGroup.setStatus('current')
ciscoEntityPerformanceMIBEntityIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 4)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalTimeElapsed"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepValidIntervalCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBEntityIntervalGroup = ciscoEntityPerformanceMIBEntityIntervalGroup.setStatus('current')
ciscoEntityPerformanceMIBIntervalStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 5)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsValidData"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsMeasurement"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsCreateTime"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsRange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBIntervalStatsGroup = ciscoEntityPerformanceMIBIntervalStatsGroup.setStatus('current')
ciscoEntityPerformanceMIBNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 6)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThresholdNotifEnabled"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBNotifControlGroup = ciscoEntityPerformanceMIBNotifControlGroup.setStatus('current')
ciscoEntityPerformanceMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 7)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepPerfThreshRisingEvent"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepPerfThreshFallingEvent"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBNotificationGroup = ciscoEntityPerformanceMIBNotificationGroup.setStatus('current')
ciscoEntityPerformanceMIBThroughputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 8)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLicensedBW"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLevel"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputInterval"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputAvgRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBThroughputGroup = ciscoEntityPerformanceMIBThroughputGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PERFORMANCE-MIB", cepConfigEntry=cepConfigEntry, cepConfigThresholdNotifEnabled=cepConfigThresholdNotifEnabled, ciscoEntityPerformanceMIBConform=ciscoEntityPerformanceMIBConform, cepStatsEntry=cepStatsEntry, cepThroughputLicensedBW=cepThroughputLicensedBW, cepConfigRisingThreshold=cepConfigRisingThreshold, ciscoEntityPerformanceMIBEntityIntervalGroup=ciscoEntityPerformanceMIBEntityIntervalGroup, cepThroughputEntry=cepThroughputEntry, cepIntervalStatsTable=cepIntervalStatsTable, ciscoEntityPerformanceMIB=ciscoEntityPerformanceMIB, cepThresholdNotifEnabled=cepThresholdNotifEnabled, CiscoEntPerfRange=CiscoEntPerfRange, cepIntervalTimeElapsed=cepIntervalTimeElapsed, ciscoEntityPerformanceMIBNotifControlGroup=ciscoEntityPerformanceMIBNotifControlGroup, cepStatsMeasurement=cepStatsMeasurement, cepStatsAlgorithm=cepStatsAlgorithm, cepConfigInterval=cepConfigInterval, cepEntityNumReloads=cepEntityNumReloads, ciscoEntityPerformanceMIBNotificationGroup=ciscoEntityPerformanceMIBNotificationGroup, cepThroughputInterval=cepThroughputInterval, cepIntervalStatsRange=cepIntervalStatsRange, ciscoEntityPerformanceMIBPerfStatsGroup=ciscoEntityPerformanceMIBPerfStatsGroup, cepPerfThreshFallingEvent=cepPerfThreshFallingEvent, cepThroughputNotif=cepThroughputNotif, ciscoEntityPerformanceMIBGroups=ciscoEntityPerformanceMIBGroups, CiscoEntPerfInterval=CiscoEntPerfInterval, cepThroughputNotifEnabled=cepThroughputNotifEnabled, ciscoEntityPerformanceMIBThroughputGroup=ciscoEntityPerformanceMIBThroughputGroup, cepStatsTable=cepStatsTable, ciscoEntityPerformanceMIBNotifs=ciscoEntityPerformanceMIBNotifs, ciscoEntityPerformanceMIBObjects=ciscoEntityPerformanceMIBObjects, cepEntityLastReloadTime=cepEntityLastReloadTime, ciscoEntityPerformanceMIBNotifObjects=ciscoEntityPerformanceMIBNotifObjects, cepPerfThreshRisingEvent=cepPerfThreshRisingEvent, cepEntityIntervalTable=cepEntityIntervalTable, ciscoEntityPerformanceMIBCompliance=ciscoEntityPerformanceMIBCompliance, cepIntervalNumber=cepIntervalNumber, cepHistInterval=cepHistInterval, ciscoEntityPerformanceMIBConfigGroup=ciscoEntityPerformanceMIBConfigGroup, ciscoEntityPerformanceMIBIntervalStatsGroup=ciscoEntityPerformanceMIBIntervalStatsGroup, cepIntervalStatsEntry=cepIntervalStatsEntry, ciscoEntityPerformanceMIBEntityGroup=ciscoEntityPerformanceMIBEntityGroup, cepThroughputAvgRate=cepThroughputAvgRate, CiscoEntPerfHistInterval=CiscoEntPerfHistInterval, cepConfigFallingThreshold=cepConfigFallingThreshold, cepThroughputTable=cepThroughputTable, ciscoEntityPerformanceMIBCompliances=ciscoEntityPerformanceMIBCompliances, PYSNMP_MODULE_ID=ciscoEntityPerformanceMIB, cepConfigTable=cepConfigTable, cepConfigPerfType=cepConfigPerfType, CiscoEntPerfIntervalAlgo=CiscoEntPerfIntervalAlgo, CiscoEntPerfType=CiscoEntPerfType, cepEntityEntry=cepEntityEntry, cepConfigPerfRange=cepConfigPerfRange, cepThroughputLevel=cepThroughputLevel, cepThroughputThreshold=cepThroughputThreshold, cepEntityIntervalEntry=cepEntityIntervalEntry, cepIntervalStatsMeasurement=cepIntervalStatsMeasurement, cepValidIntervalCount=cepValidIntervalCount, cepEntityTable=cepEntityTable, CiscoEntPerfMeasurement=CiscoEntPerfMeasurement, cepIntervalStatsCreateTime=cepIntervalStatsCreateTime, cepIntervalStatsValidData=cepIntervalStatsValidData)
