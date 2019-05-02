#
# PySNMP MIB module CISCO-ENTITY-SENSOR-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-SENSOR-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalName, entPhysicalDescr, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalName", "entPhysicalDescr", "entPhysicalIndex")
EntitySensorValue, entPhySensorValue, entPhySensorType = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorValue", "entPhySensorType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Counter32, Integer32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32", "Integer32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoEntitySensorExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 745))
ciscoEntitySensorExtMIB.setRevisions(('2010-06-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setLastUpdated('201006100000Z')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setContactInfo('Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 408 526 4000 E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setDescription('This MIB is extension to ENTITY-SENSOR-MIB(RFC 3433). This MIB also defines the notifications applicable for sensors reported in ENTITY-MIB(RFC 4133).')
ciscoEntitySensorExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 0))
ciscoEntitySensorExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1))
ciscoEntitySensorExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2))
class CiscoSensorThresholdSeverity(TextualConvention, Integer32):
    description = 'sensor threshold severity. Valid values are: other(1) : a severity other than those listed below. minor(10) : Minor Problem threshold. major(20) : Major Problem threshold. critical(30): Critical problem threshold. A system might shut down the sensor associated FRU automatically if the sensor value reach the critical problem threshold.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class CiscoSensorThresholdRelation(TextualConvention, Integer32):
    description = 'sensor threshold relational operator types. valid values are: lessThan(1): if the sensor value is less than the threshold value lessOrEqual(2): if the sensor value is less than or equal to the threshold value greaterThan(3): if the sensor value is greater than the threshold value greaterOrEqual(4): if the sensor value is greater than or equal to the threshold value equalTo(5): if the sensor value is equal to the threshold value notEqualTo(6): if the sensor value is not equal to the threshold value'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

ceSensorExtThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1), )
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setReference('ENTITY-MIB contains definition for entPhysicalTable')
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setDescription('This table lists the threshold severity, relation, and comparison value, for a sensor entity listed in entPhysicalTable.')
ceSensorExtThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdIndex"))
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setReference('ENTITY-MIB contains definition for entPhysicalClass')
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setDescription("An ceSensorExtThresholdTable entry describes the thresholds for a sensor: the threshold severity, the threshold value, the relation, and the evaluation of the threshold. Only entities with entPhysicalClass 'sensor' are listed in this table. For non FRU entities the entries are created by the agent at system startup and entries are never deleted by the agent. For FRU entities the entries are created at system startup if FRU is inserted at system startup, else entries are created when FRU is inserted. Entries are deleted by the agent when FRU is removed.")
ceSensorExtThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ceSensorExtThresholdIndex.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdIndex.setDescription('An index that uniquely identifies an entry in the ceSensorExtThresholdTable. This index permits the same sensor to have several different thresholds.')
ceSensorExtThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 2), CiscoSensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdSeverity.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdSeverity.setDescription('This object specifies the severity of this threshold.')
ceSensorExtThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 3), CiscoSensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdRelation.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdRelation.setDescription("This object specifies the boolean relation between sensor value (entPhySensorValue) and threshold value (ceSensorExtThresholdValue), required to trigger the alarm. in pseudo-code, the evaluation-alarm mechanism is: ... if (evaluate(entPhySensorValue, ceSensorExtThresholdRelation, ceSensorExtThresholdValue)) then if (((ceSensorExtThresholdNotifEnable == enabled) || (ceSensorExtThresholdNotifEnable == transparent)) && (ceSensorExtThresholdNotifGlobalEnable == enabled)) then raise_alarm(sensor's entPhysicalIndex); endif endif ...")
ceSensorExtThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setReference('ENTITY-SENSOR-MIB contains definitions for entPhysSensorScale and entPhySensorPrecision')
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setDescription('This object specifies the value of the threshold. The value of objects entPhySensorType, entPhysSensorScale and entPhySensorPrecision for this sensor entity defines how ceSensorExtThresholdValue can be displayed or intepreted by the user. entPhySensorValue can be compared with ceSensorExtThresholdValue without taking care of semantics of both objects.')
ceSensorExtThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setReference('ENTITY-SENSOR-MIB contains definition for entPhySensorValueUpdateRate')
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setDescription("This object indicates the result of the most recent evaluation of the threshold. The agent will execute the below 'evaluate' function to generate the notification. 'evaluate' function returns a boolean value. evaluate(entPhySensorValue, ceSensorExtThresholdRelation, ceSensorExtThresholdValue) If evalute function returns true then ceSensorExtThresholdEvaluation is set to 'true' If evaluate function returns false then ceSensorExtThresholdEvaluation is set to 'false'. Thresholds are evaluated at the rate indicated by entPhySensorValueUpdateRate.")
ceSensorExtThresholdNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("transparent", 3))).clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifEnable.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdNotifEnable.setDescription("A control object to activate/deactivate ceSensorExtThresholdNotification. This object should hold any of the below values. enabled(1) - The notification is enabled for this entity disabled(2) - The notification is disabled for this entity transparent(3)- The notification is enabled/disabled based on ceSensorExtThresholdNotifGlobalEnable object This object controls generation of ceSensorExtThresholdNotification for this threshold. An exception to this is, if this object is set to 'transparent' then ceSensorExtThresholdNotification for this threshold is controlled by ceSensorExtThresholdNotifGlobalEnable object. This truth table explains how ceSensorExtThresholdNotifEnable is related with ceSensorExtThresholdNotifGlobalEnable to control the ceSensorExtThresholdNotification for this threshold E = enabled, D = Disabled, T = Transparent local_flag = ceSensorExtThresholdNotifEnable global_flag = ceSensorExtThresholdNotifGlobalEnable local_flag global_flag outcome_per_interface --------------------------------------------- E E E E D D D E D D D D T E E T D D")
ciscoEntSensorExtGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2))
ceSensorExtThresholdNotifGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdNotifGlobalEnable.setDescription("A control object to activate/deactivate ceSensorExtThresholdNotification. This object should hold any of the below values. enabled(1) - The notification is enabled globally on the device disabled(2)- The notification is disabled globally on the device This object enables the generation of ceSensorExtThresholdNotification globally on the device. If this object value is 'disabled', then no ceSensorExtThresholdNotification will be generated on this device. If this object value is 'enabled', then whether a ceSensorExtThresholdNotification for a threshold will be generated or not depends on the instance value of ceSensorExtThresholdNotifEnable for that threshold.")
ceSensorExtThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 745, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorType"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"))
if mibBuilder.loadTexts: ceSensorExtThresholdNotification.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdNotification.setDescription('This notification is generated once each time the sensor value crosses the threshold value specified by ceSensorExtThresholdValue object.')
ciscoEntSensorExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1))
ciscoEntSensorExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2))
ciscoEntSensorExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtThresholdGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationCtrlGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtMIBCompliance = ciscoEntSensorExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtMIBCompliance.setDescription('An ENTITY-MIB implementation that adds notification for sensors in the entPhysicalTable must implement this group.')
ciscoEntSensorExtThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdSeverity"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdRelation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtThresholdGroup = ciscoEntSensorExtThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtThresholdGroup.setDescription('The collection of objects which are used to describe and monitor thresholds for sensors.')
ciscoEntSensorExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationGroup = ciscoEntSensorExtNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtNotificationGroup.setDescription('The collection of notifications used for monitoring sensor threshold activity.')
ciscoEntSensorExtNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationCtrlGroup = ciscoEntSensorExtNotificationCtrlGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtNotificationCtrlGroup.setDescription('The collection of objects which provide the global notification control on ceSensorExtThresholdNotification.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-EXT-MIB", ciscoEntSensorExtMIBCompliance=ciscoEntSensorExtMIBCompliance, ciscoEntSensorExtGlobalObjects=ciscoEntSensorExtGlobalObjects, ceSensorExtThresholdValue=ceSensorExtThresholdValue, ciscoEntitySensorExtMIBNotifs=ciscoEntitySensorExtMIBNotifs, ciscoEntSensorExtNotificationGroup=ciscoEntSensorExtNotificationGroup, ciscoEntSensorExtThresholdGroup=ciscoEntSensorExtThresholdGroup, ciscoEntitySensorExtMIBConform=ciscoEntitySensorExtMIBConform, ciscoEntSensorExtMIBGroups=ciscoEntSensorExtMIBGroups, ceSensorExtThresholdSeverity=ceSensorExtThresholdSeverity, ciscoEntSensorExtMIBCompliances=ciscoEntSensorExtMIBCompliances, ciscoEntitySensorExtMIB=ciscoEntitySensorExtMIB, ceSensorExtThresholdNotification=ceSensorExtThresholdNotification, ceSensorExtThresholdEvaluation=ceSensorExtThresholdEvaluation, ceSensorExtThresholdNotifEnable=ceSensorExtThresholdNotifEnable, ceSensorExtThresholdIndex=ceSensorExtThresholdIndex, ceSensorExtThresholdRelation=ceSensorExtThresholdRelation, CiscoSensorThresholdSeverity=CiscoSensorThresholdSeverity, ciscoEntitySensorExtMIBObjects=ciscoEntitySensorExtMIBObjects, ceSensorExtThresholdTable=ceSensorExtThresholdTable, CiscoSensorThresholdRelation=CiscoSensorThresholdRelation, ceSensorExtThresholdNotifGlobalEnable=ceSensorExtThresholdNotifGlobalEnable, ceSensorExtThresholdEntry=ceSensorExtThresholdEntry, PYSNMP_MODULE_ID=ciscoEntitySensorExtMIB, ciscoEntSensorExtNotificationCtrlGroup=ciscoEntSensorExtNotificationCtrlGroup)
