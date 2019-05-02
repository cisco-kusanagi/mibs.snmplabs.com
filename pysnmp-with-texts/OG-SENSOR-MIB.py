#
# PySNMP MIB module OG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OG-SENSOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Integer32, iso, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Gauge32, IpAddress, MibIdentifier, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "iso", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogSensorMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 13))
ogSensorMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogSensorMib.setRevisionsDescriptions(('Renamed from OPENGEAR-SENSOR-MIB to OG-SENSOR-MIB to fix naming discrepancy.', 'Syntax corrections by Opengear Inc.', 'Initial version.',))
if mibBuilder.loadTexts: ogSensorMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogSensorMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogSensorMib.setContactInfo('Opengear Inc. 630 West 9560 South, Sandy, UT 84070 support@opengear.com')
if mibBuilder.loadTexts: ogSensorMib.setDescription('Opengear SENSOR status MIB')
ogSensorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10))
ogsensStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1))
ogsensStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3), )
if mibBuilder.loadTexts: ogsensStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusTable.setDescription('A table of sensor status events generated by this device.')
ogsensStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1), ).setIndexNames((0, "OG-SENSOR-MIB", "ogsensStatusIndex"))
if mibBuilder.loadTexts: ogsensStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusEntry.setDescription('A sensor status event that was previously generated by this device. Each entry is indexed by a message index.')
ogsensStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogsensStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusIndex.setDescription('A monotonically increasing integer for the sole purpose of indexing messages. When it reaches the maximum value the agent flushes the table and wraps the value back to 1.')
ogsensStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusName.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusName.setDescription('The name of the device pertaining to the status event')
ogsensStatusDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusDevType.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusDevType.setDescription('The type of device pertaining to the status event')
ogsensStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusType.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusType.setDescription('The type of sensor pertaining to the status event')
ogsensStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusValue.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusValue.setDescription('The value of the sensor pertaining to the status event')
ogSensorMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2))
ogsensMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0))
ogsensEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0, 200)).setObjects(("OG-SENSOR-MIB", "ogsensStatusName"), ("OG-SENSOR-MIB", "ogsensStatusDevType"), ("OG-SENSOR-MIB", "ogsensStatusType"), ("OG-SENSOR-MIB", "ogsensStatusValue"))
if mibBuilder.loadTexts: ogsensEventOccurred.setStatus('current')
if mibBuilder.loadTexts: ogsensEventOccurred.setDescription('The notification sent when a sensor status event occurs')
ogSensorMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3))
ogSensorMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1))
ogSensorMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2))
ogSensorMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1, 1)).setObjects(("OG-SENSOR-MIB", "ogSensorMibGroup"), ("OG-SENSOR-MIB", "ogsensNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSensorMibCompliance = ogSensorMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ogSensorMibCompliance.setDescription('The compliance statement for entities which implement the Opengear sensor MIB.')
ogSensorMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 1)).setObjects(("OG-SENSOR-MIB", "ogsensStatusName"), ("OG-SENSOR-MIB", "ogsensStatusDevType"), ("OG-SENSOR-MIB", "ogsensStatusType"), ("OG-SENSOR-MIB", "ogsensStatusValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSensorMibGroup = ogSensorMibGroup.setStatus('current')
if mibBuilder.loadTexts: ogSensorMibGroup.setDescription('A collection of objects providing the sensor MIB capability.')
ogsensNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 2)).setObjects(("OG-SENSOR-MIB", "ogsensEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogsensNotificationsGroup = ogsensNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ogsensNotificationsGroup.setDescription('A collection of notification(s) for sensor system.')
mibBuilder.exportSymbols("OG-SENSOR-MIB", ogsensStatusDevType=ogsensStatusDevType, ogSensorMibObjects=ogSensorMibObjects, ogsensNotificationsGroup=ogsensNotificationsGroup, ogSensorMibGroups=ogSensorMibGroups, ogSensorMib=ogSensorMib, ogsensStatusEntry=ogsensStatusEntry, ogsensStatus=ogsensStatus, ogSensorMibConformance=ogSensorMibConformance, PYSNMP_MODULE_ID=ogSensorMib, ogsensMibNotifications=ogsensMibNotifications, ogSensorMibCompliance=ogSensorMibCompliance, ogSensorMibNotificationPrefix=ogSensorMibNotificationPrefix, ogsensEventOccurred=ogsensEventOccurred, ogsensStatusIndex=ogsensStatusIndex, ogsensStatusTable=ogsensStatusTable, ogsensStatusValue=ogsensStatusValue, ogSensorMibCompliances=ogSensorMibCompliances, ogSensorMibGroup=ogSensorMibGroup, ogsensStatusName=ogsensStatusName, ogsensStatusType=ogsensStatusType)
