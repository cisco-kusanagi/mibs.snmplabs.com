#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, Bits, Gauge32, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, Integer32, TimeTicks, NotificationType, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "Integer32", "TimeTicks", "NotificationType", "iso", "MibIdentifier")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
ciscoOpticalMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 264))
ciscoOpticalMonitorMIB.setRevisions(('2007-01-02 00:00', '2002-05-10 00:00',))
if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setOrganization('Cisco Systems, Inc.')
class OpticalParameterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("power", 1), ("acPower", 2), ("ambientTemp", 3), ("laserTemp", 4), ("biasCurrent", 5), ("peltierCurrent", 6), ("xcvrVoltage", 7))

class OpticalParameterValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000, 1000000)

class OpticalIfDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("receive", 1), ("transmit", 2), ("notApplicable", 3))

class OpticalIfMonLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("beforeAdjustment", 1), ("afterAdjustment", 2), ("notApplicable", 3))

class OpticalAlarmStatus(TextualConvention, OctetString):
    reference = 'Telcordia Technologies Generic Requirements GR-2918-CORE, Issue 4, December 1999, Section 8.11'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class OpticalAlarmSeverity(TextualConvention, Integer32):
    reference = 'Telcordia Technologies Generic Requirements GR-474-CORE, Issue 1, December 1997, Section 2.2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("notAlarmed", 4), ("notReported", 5), ("cleared", 6))

class OpticalAlarmSeverityOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 6)

class OpticalPMPeriod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fifteenMin", 1), ("twentyFourHour", 2))

cOpticalMonitorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 1))
cOpticalMonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1))
cOpticalPMGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2))
cOpticalMonTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1), )
if mibBuilder.loadTexts: cOpticalMonTable.setStatus('current')
cOpticalMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonDirection"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonLocation"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonParameterType"))
if mibBuilder.loadTexts: cOpticalMonEntry.setStatus('current')
cOpticalMonDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 1), OpticalIfDirection())
if mibBuilder.loadTexts: cOpticalMonDirection.setStatus('current')
cOpticalMonLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 2), OpticalIfMonLocation())
if mibBuilder.loadTexts: cOpticalMonLocation.setStatus('current')
cOpticalMonParameterType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 3), OpticalParameterType())
if mibBuilder.loadTexts: cOpticalMonParameterType.setStatus('current')
cOpticalParameterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 4), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParameterValue.setStatus('current')
cOpticalParamHighAlarmThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 5), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighAlarmThresh.setStatus('current')
cOpticalParamHighAlarmSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 6), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighAlarmSev.setStatus('current')
cOpticalParamHighWarningThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 7), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighWarningThresh.setStatus('current')
cOpticalParamHighWarningSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 8), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighWarningSev.setStatus('current')
cOpticalParamLowAlarmThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 9), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowAlarmThresh.setStatus('current')
cOpticalParamLowAlarmSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 10), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowAlarmSev.setStatus('current')
cOpticalParamLowWarningThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 11), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowWarningThresh.setStatus('current')
cOpticalParamLowWarningSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 12), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowWarningSev.setStatus('current')
cOpticalParamAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 13), OpticalAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmStatus.setStatus('current')
cOpticalParamAlarmCurMaxThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 14), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmCurMaxThresh.setStatus('current')
cOpticalParamAlarmCurMaxSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 15), OpticalAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmCurMaxSev.setStatus('current')
cOpticalParamAlarmLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmLastChange.setStatus('current')
cOpticalMon15MinValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalMon15MinValidIntervals.setStatus('current')
cOpticalMon24HrValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalMon24HrValidIntervals.setStatus('current')
cOpticalParamThreshSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 19), Bits().clone(namedValues=NamedValues(("highAlarmDefThresh", 0), ("highWarnDefThresh", 1), ("lowAlarmDefThresh", 2), ("lowWarnDefThresh", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamThreshSource.setStatus('current')
cOpticalNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 2), OpticalAlarmSeverityOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalNotifyEnable.setStatus('current')
cOpticalMonEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 3), Bits().clone(namedValues=NamedValues(("all", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalMonEnable.setStatus('current')
cOpticalMonPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 4), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalMonPollInterval.setStatus('current')
cOpticalMonIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5), )
if mibBuilder.loadTexts: cOpticalMonIfTable.setStatus('current')
cOpticalMonIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cOpticalMonIfEntry.setStatus('current')
cOpticalMonIfTimeInSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalMonIfTimeInSlot.setStatus('current')
cOpticalPMCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1), )
if mibBuilder.loadTexts: cOpticalPMCurrentTable.setStatus('current')
cOpticalPMCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentPeriod"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentDirection"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentLocation"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentParamType"))
if mibBuilder.loadTexts: cOpticalPMCurrentEntry.setStatus('current')
cOpticalPMCurrentPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 1), OpticalPMPeriod())
if mibBuilder.loadTexts: cOpticalPMCurrentPeriod.setStatus('current')
cOpticalPMCurrentDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 2), OpticalIfDirection())
if mibBuilder.loadTexts: cOpticalPMCurrentDirection.setStatus('current')
cOpticalPMCurrentLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 3), OpticalIfMonLocation())
if mibBuilder.loadTexts: cOpticalPMCurrentLocation.setStatus('current')
cOpticalPMCurrentParamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 4), OpticalParameterType())
if mibBuilder.loadTexts: cOpticalPMCurrentParamType.setStatus('current')
cOpticalPMCurrentMaxParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 5), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentMaxParam.setStatus('current')
cOpticalPMCurrentMinParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 6), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentMinParam.setStatus('current')
cOpticalPMCurrentMeanParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 7), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentMeanParam.setStatus('current')
cOpticalPMCurrentUnavailSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentUnavailSecs.setStatus('current')
cOpticalPMIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2), )
if mibBuilder.loadTexts: cOpticalPMIntervalTable.setStatus('current')
cOpticalPMIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalPeriod"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalNumber"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalDirection"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalLocation"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalParamType"))
if mibBuilder.loadTexts: cOpticalPMIntervalEntry.setStatus('current')
cOpticalPMIntervalPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 1), OpticalPMPeriod())
if mibBuilder.loadTexts: cOpticalPMIntervalPeriod.setStatus('current')
cOpticalPMIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: cOpticalPMIntervalNumber.setStatus('current')
cOpticalPMIntervalDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 3), OpticalIfDirection())
if mibBuilder.loadTexts: cOpticalPMIntervalDirection.setStatus('current')
cOpticalPMIntervalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 4), OpticalIfMonLocation())
if mibBuilder.loadTexts: cOpticalPMIntervalLocation.setStatus('current')
cOpticalPMIntervalParamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 5), OpticalParameterType())
if mibBuilder.loadTexts: cOpticalPMIntervalParamType.setStatus('current')
cOpticalPMIntervalMaxParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 6), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalMaxParam.setStatus('current')
cOpticalPMIntervalMinParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 7), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalMinParam.setStatus('current')
cOpticalPMIntervalMeanParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 8), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalMeanParam.setStatus('current')
cOpticalPMIntervalUnavailSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalUnavailSecs.setStatus('current')
cOpticalMonitorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 2))
cOpticalMonNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 2, 0))
cOpticalMonParameterStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 264, 2, 0, 1)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParameterValue"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmStatus"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmLastChange"))
if mibBuilder.loadTexts: cOpticalMonParameterStatus.setStatus('current')
cOpticalMonitorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 3))
cOpticalMonitorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1))
cOpticalMonitorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2))
cOpticalMonitorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1, 1)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBMonGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBThresholdGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBSeverityGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBPMGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifyEnableGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonitorMIBCompliance = cOpticalMonitorMIBCompliance.setStatus('deprecated')
cOpticalMonitorMIBComplianceRev = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1, 2)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBMonGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBThresholdGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBSeverityGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBPMGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonIfTimeGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifyEnableGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBEnableConfigGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBIntervalConfigGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonThreshSourceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonitorMIBComplianceRev = cOpticalMonitorMIBComplianceRev.setStatus('current')
cOpticalMIBMonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 1)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParameterValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBMonGroup = cOpticalMIBMonGroup.setStatus('current')
cOpticalMIBThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 2)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarningThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarningThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmStatus"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBThresholdGroup = cOpticalMIBThresholdGroup.setStatus('current')
cOpticalMIBSeverityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 3)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarningSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarningSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxSev"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBSeverityGroup = cOpticalMIBSeverityGroup.setStatus('current')
cOpticalMIBPMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 4)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMon15MinValidIntervals"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMon24HrValidIntervals"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMaxParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMinParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMeanParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentUnavailSecs"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMaxParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMinParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMeanParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalUnavailSecs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBPMGroup = cOpticalMIBPMGroup.setStatus('current')
cOpticalMIBNotifyEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 5)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBNotifyEnableGroup = cOpticalMIBNotifyEnableGroup.setStatus('current')
cOpticalMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 6)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonParameterStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBNotifGroup = cOpticalMIBNotifGroup.setStatus('current')
cOpticalMonIfTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 7)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonIfTimeInSlot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonIfTimeGroup = cOpticalMonIfTimeGroup.setStatus('current')
cOpticalMIBEnableConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 8)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBEnableConfigGroup = cOpticalMIBEnableConfigGroup.setStatus('current')
cOpticalMIBIntervalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 9)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonPollInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBIntervalConfigGroup = cOpticalMIBIntervalConfigGroup.setStatus('current')
cOpticalMonThreshSourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 10)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamThreshSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonThreshSourceGroup = cOpticalMonThreshSourceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-MIB", cOpticalParamHighAlarmThresh=cOpticalParamHighAlarmThresh, cOpticalParamHighWarningThresh=cOpticalParamHighWarningThresh, cOpticalPMCurrentLocation=cOpticalPMCurrentLocation, cOpticalMIBMonGroup=cOpticalMIBMonGroup, cOpticalMonNotificationPrefix=cOpticalMonNotificationPrefix, cOpticalMonGroup=cOpticalMonGroup, cOpticalMonIfTimeInSlot=cOpticalMonIfTimeInSlot, cOpticalMonitorMIBNotifications=cOpticalMonitorMIBNotifications, OpticalParameterType=OpticalParameterType, cOpticalMonEntry=cOpticalMonEntry, OpticalPMPeriod=OpticalPMPeriod, cOpticalMIBNotifGroup=cOpticalMIBNotifGroup, cOpticalMIBIntervalConfigGroup=cOpticalMIBIntervalConfigGroup, OpticalIfDirection=OpticalIfDirection, ciscoOpticalMonitorMIB=ciscoOpticalMonitorMIB, cOpticalMonParameterType=cOpticalMonParameterType, cOpticalPMCurrentTable=cOpticalPMCurrentTable, cOpticalMonEnable=cOpticalMonEnable, cOpticalMIBEnableConfigGroup=cOpticalMIBEnableConfigGroup, cOpticalMonitorMIBCompliance=cOpticalMonitorMIBCompliance, cOpticalPMGroup=cOpticalPMGroup, cOpticalPMIntervalMaxParam=cOpticalPMIntervalMaxParam, cOpticalMonIfTimeGroup=cOpticalMonIfTimeGroup, cOpticalPMCurrentUnavailSecs=cOpticalPMCurrentUnavailSecs, cOpticalMonIfTable=cOpticalMonIfTable, cOpticalParamHighWarningSev=cOpticalParamHighWarningSev, cOpticalParamThreshSource=cOpticalParamThreshSource, cOpticalMIBSeverityGroup=cOpticalMIBSeverityGroup, OpticalIfMonLocation=OpticalIfMonLocation, cOpticalMonThreshSourceGroup=cOpticalMonThreshSourceGroup, cOpticalPMCurrentPeriod=cOpticalPMCurrentPeriod, cOpticalMIBThresholdGroup=cOpticalMIBThresholdGroup, cOpticalMonitorMIBConformance=cOpticalMonitorMIBConformance, cOpticalPMCurrentMinParam=cOpticalPMCurrentMinParam, cOpticalPMIntervalEntry=cOpticalPMIntervalEntry, cOpticalParamLowWarningThresh=cOpticalParamLowWarningThresh, cOpticalMonitorMIBComplianceRev=cOpticalMonitorMIBComplianceRev, cOpticalParamLowWarningSev=cOpticalParamLowWarningSev, cOpticalPMIntervalParamType=cOpticalPMIntervalParamType, cOpticalPMIntervalUnavailSecs=cOpticalPMIntervalUnavailSecs, cOpticalPMCurrentEntry=cOpticalPMCurrentEntry, OpticalAlarmSeverityOrZero=OpticalAlarmSeverityOrZero, cOpticalParamLowAlarmThresh=cOpticalParamLowAlarmThresh, cOpticalPMCurrentMeanParam=cOpticalPMCurrentMeanParam, cOpticalPMIntervalNumber=cOpticalPMIntervalNumber, cOpticalMIBNotifyEnableGroup=cOpticalMIBNotifyEnableGroup, cOpticalMonIfEntry=cOpticalMonIfEntry, cOpticalPMCurrentMaxParam=cOpticalPMCurrentMaxParam, cOpticalPMIntervalPeriod=cOpticalPMIntervalPeriod, cOpticalPMIntervalMinParam=cOpticalPMIntervalMinParam, cOpticalParamAlarmCurMaxSev=cOpticalParamAlarmCurMaxSev, cOpticalPMCurrentParamType=cOpticalPMCurrentParamType, cOpticalParamLowAlarmSev=cOpticalParamLowAlarmSev, cOpticalParamAlarmCurMaxThresh=cOpticalParamAlarmCurMaxThresh, cOpticalParamHighAlarmSev=cOpticalParamHighAlarmSev, cOpticalMonitorMIBCompliances=cOpticalMonitorMIBCompliances, OpticalAlarmStatus=OpticalAlarmStatus, cOpticalMonDirection=cOpticalMonDirection, cOpticalMonitorMIBObjects=cOpticalMonitorMIBObjects, cOpticalParamAlarmLastChange=cOpticalParamAlarmLastChange, cOpticalPMIntervalDirection=cOpticalPMIntervalDirection, cOpticalParameterValue=cOpticalParameterValue, PYSNMP_MODULE_ID=ciscoOpticalMonitorMIB, cOpticalMonLocation=cOpticalMonLocation, cOpticalParamAlarmStatus=cOpticalParamAlarmStatus, cOpticalMonParameterStatus=cOpticalMonParameterStatus, cOpticalPMIntervalLocation=cOpticalPMIntervalLocation, OpticalParameterValue=OpticalParameterValue, cOpticalMonitorMIBGroups=cOpticalMonitorMIBGroups, cOpticalNotifyEnable=cOpticalNotifyEnable, cOpticalMIBPMGroup=cOpticalMIBPMGroup, cOpticalMon24HrValidIntervals=cOpticalMon24HrValidIntervals, cOpticalPMIntervalTable=cOpticalPMIntervalTable, cOpticalMonTable=cOpticalMonTable, cOpticalPMCurrentDirection=cOpticalPMCurrentDirection, cOpticalMon15MinValidIntervals=cOpticalMon15MinValidIntervals, cOpticalMonPollInterval=cOpticalMonPollInterval, OpticalAlarmSeverity=OpticalAlarmSeverity, cOpticalPMIntervalMeanParam=cOpticalPMIntervalMeanParam)
