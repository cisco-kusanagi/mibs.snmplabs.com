#
# PySNMP MIB module CISCO-PORT-STORM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PORT-STORM-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Bits, TimeTicks, IpAddress, NotificationType, Unsigned32, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Bits", "TimeTicks", "IpAddress", "NotificationType", "Unsigned32", "iso", "Gauge32", "Counter32")
TruthValue, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention")
ciscoPortStormControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 362))
ciscoPortStormControlMIB.setRevisions(('2007-10-19 00:00', '2003-07-03 00:00',))
if mibBuilder.loadTexts: ciscoPortStormControlMIB.setLastUpdated('200710190000Z')
if mibBuilder.loadTexts: ciscoPortStormControlMIB.setOrganization('Cisco Systems, Inc.')
ciscoPortStormControlMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 0))
ciscoPortStormControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 1))
ciscoPortStormControlMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 2))
cpscConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1))
cpscStatusObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2))
class CPortStormControlTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("broadcast", 1), ("multicast", 2), ("unicast", 3), ("all", 4))

class CPortStormControlActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("filter", 1), ("shutdown", 2))

class CPortStormControlStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("inactive", 1), ("forwarding", 2), ("trafficTypeFiltered", 3), ("allTrafficFiltered", 4), ("shutdown", 5))

cpscThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1), )
if mibBuilder.loadTexts: cpscThresholdTable.setStatus('current')
cpscThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscTrafficType"))
if mibBuilder.loadTexts: cpscThresholdEntry.setStatus('current')
cpscTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 1), CPortStormControlTrafficType())
if mibBuilder.loadTexts: cpscTrafficType.setStatus('current')
cpscUpperThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('0.01 Percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscUpperThreshold.setStatus('current')
cpscLowerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('0.01 Percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscLowerThreshold.setStatus('current')
cpscActionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2), )
if mibBuilder.loadTexts: cpscActionTable.setStatus('current')
cpscActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpscActionEntry.setStatus('current')
cpscAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1, 1), CPortStormControlActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscAction.setStatus('current')
cpscNotificationControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("stormOccurred", 2), ("stormCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscNotificationControl.setStatus('current')
cpscNotificationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('Notifications per Minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpscNotificationThreshold.setStatus('current')
cpscStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1), )
if mibBuilder.loadTexts: cpscStatusTable.setStatus('current')
cpscStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscTrafficType"))
if mibBuilder.loadTexts: cpscStatusEntry.setStatus('current')
cpscStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 1), CPortStormControlStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscStatus.setStatus('current')
cpscCurrentLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('0.01 Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscCurrentLevel.setStatus('current')
cpscSuppressedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscSuppressedPacket.setStatus('current')
cpscHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2), )
if mibBuilder.loadTexts: cpscHistoryTable.setStatus('current')
cpscHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryTrafficType"), (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryIndex"))
if mibBuilder.loadTexts: cpscHistoryEntry.setStatus('current')
cpscHistoryTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 1), CPortStormControlTrafficType())
if mibBuilder.loadTexts: cpscHistoryTrafficType.setStatus('current')
cpscHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: cpscHistoryIndex.setStatus('current')
cpscHistoryStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscHistoryStartTime.setStatus('current')
cpscHistoryEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpscHistoryEndTime.setStatus('current')
cpscNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 1))
cpscEventRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 2)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"))
if mibBuilder.loadTexts: cpscEventRev1.setStatus('current')
cpscEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 1, 1)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"))
if mibBuilder.loadTexts: cpscEvent.setStatus('deprecated')
ciscoPortStormControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1))
ciscoPortStormControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2))
ciscoPortStormControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1, 1)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotifConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatusGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatisticsGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortStormControlMIBCompliance = ciscoPortStormControlMIBCompliance.setStatus('deprecated')
ciscoPortStormControlMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1, 2)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotifConfigurationGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationGroupRev1"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatusGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatisticsGroup"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortStormControlMIBComplianceRev1 = ciscoPortStormControlMIBComplianceRev1.setStatus('current')
cpscConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 1)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscUpperThreshold"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscLowerThreshold"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscConfigurationGroup = cpscConfigurationGroup.setStatus('current')
cpscStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 2)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscCurrentLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscStatusGroup = cpscStatusGroup.setStatus('current')
cpscNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 3)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscNotificationGroup = cpscNotificationGroup.setStatus('deprecated')
cpscNotifConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 4)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationControl"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscNotifConfigurationGroup = cpscNotifConfigurationGroup.setStatus('current')
cpscStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 5)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscSuppressedPacket"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscStatisticsGroup = cpscStatisticsGroup.setStatus('current')
cpscHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 6)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryStartTime"), ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryEndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscHistoryGroup = cpscHistoryGroup.setStatus('current')
cpscNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 7)).setObjects(("CISCO-PORT-STORM-CONTROL-MIB", "cpscEventRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscNotificationGroupRev1 = cpscNotificationGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-STORM-CONTROL-MIB", CPortStormControlActionType=CPortStormControlActionType, cpscHistoryEntry=cpscHistoryEntry, cpscHistoryStartTime=cpscHistoryStartTime, PYSNMP_MODULE_ID=ciscoPortStormControlMIB, cpscEventRev1=cpscEventRev1, ciscoPortStormControlMIBConform=ciscoPortStormControlMIBConform, cpscLowerThreshold=cpscLowerThreshold, CPortStormControlTrafficType=CPortStormControlTrafficType, cpscAction=cpscAction, cpscHistoryTrafficType=cpscHistoryTrafficType, ciscoPortStormControlMIBObjects=ciscoPortStormControlMIBObjects, cpscStatusEntry=cpscStatusEntry, cpscStatusGroup=cpscStatusGroup, cpscStatusTable=cpscStatusTable, cpscActionEntry=cpscActionEntry, cpscSuppressedPacket=cpscSuppressedPacket, ciscoPortStormControlMIBCompliances=ciscoPortStormControlMIBCompliances, ciscoPortStormControlMIBComplianceRev1=ciscoPortStormControlMIBComplianceRev1, cpscThresholdTable=cpscThresholdTable, cpscNotificationControl=cpscNotificationControl, cpscNotificationThreshold=cpscNotificationThreshold, ciscoPortStormControlMIBGroups=ciscoPortStormControlMIBGroups, cpscConfigurationGroup=cpscConfigurationGroup, cpscHistoryEndTime=cpscHistoryEndTime, cpscTrafficType=cpscTrafficType, cpscHistoryIndex=cpscHistoryIndex, CPortStormControlStatusType=CPortStormControlStatusType, cpscCurrentLevel=cpscCurrentLevel, cpscEvent=cpscEvent, cpscThresholdEntry=cpscThresholdEntry, cpscHistoryTable=cpscHistoryTable, ciscoPortStormControlMIBCompliance=ciscoPortStormControlMIBCompliance, ciscoPortStormControlMIB=ciscoPortStormControlMIB, cpscUpperThreshold=cpscUpperThreshold, cpscNotificationGroup=cpscNotificationGroup, cpscHistoryGroup=cpscHistoryGroup, cpscStatusObjects=cpscStatusObjects, cpscStatisticsGroup=cpscStatisticsGroup, cpscActionTable=cpscActionTable, cpscStatus=cpscStatus, cpscConfigObjects=cpscConfigObjects, cpscNotificationsPrefix=cpscNotificationsPrefix, cpscNotificationGroupRev1=cpscNotificationGroupRev1, ciscoPortStormControlMIBNotifs=ciscoPortStormControlMIBNotifs, cpscNotifConfigurationGroup=cpscNotifConfigurationGroup)
