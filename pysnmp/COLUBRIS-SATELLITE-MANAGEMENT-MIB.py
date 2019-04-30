#
# PySNMP MIB module COLUBRIS-SATELLITE-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-SATELLITE-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSIDOrNone, ColubrisNotificationEnable = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSIDOrNone", "ColubrisNotificationEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, MibIdentifier, iso, Counter32, ModuleIdentity, NotificationType, Bits, Integer32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "MibIdentifier", "iso", "Counter32", "ModuleIdentity", "NotificationType", "Bits", "Integer32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
colubrisSatelliteManagementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 7))
if mibBuilder.loadTexts: colubrisSatelliteManagementMIB.setLastUpdated('200602230000Z')
if mibBuilder.loadTexts: colubrisSatelliteManagementMIB.setOrganization('Colubris Networks, Inc.')
colubrisSatelliteManagementMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1))
satelliteInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1))
masterSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2))
satelliteTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1), )
if mibBuilder.loadTexts: satelliteTable.setStatus('current')
satelliteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIndex"))
if mibBuilder.loadTexts: satelliteEntry.setStatus('current')
satelliteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: satelliteIndex.setStatus('current')
satelliteDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDeviceId.setStatus('current')
satelliteMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteMacAddress.setStatus('current')
satelliteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteIpAddress.setStatus('current')
satelliteName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteName.setStatus('current')
satelliteSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 6), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSSID.setStatus('current')
satelliteChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteChannelNumber.setStatus('current')
satelliteForwardWirelessToWireless = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteForwardWirelessToWireless.setStatus('current')
satelliteMasterTrafficOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteMasterTrafficOnly.setStatus('current')
satelliteSNMPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSNMPPort.setStatus('current')
satelliteSecureWebPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSecureWebPort.setStatus('current')
satelliteDeviceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDeviceMacAddress.setStatus('current')
satelliteProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteProductName.setStatus('current')
satelliteFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteFirmwareRevision.setStatus('current')
satelliteGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteGroupName.setStatus('current')
satelliteChannelNumberRadio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteChannelNumberRadio2.setStatus('current')
satelliteVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteVLAN.setStatus('current')
satelliteDetectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDetectionPort.setStatus('current')
satelliteNumber = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteNumber.setStatus('current')
satelliteUpNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteUpNotificationEnabled.setStatus('current')
satelliteDownNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteDownNotificationEnabled.setStatus('current')
colubrisSatelliteManagementMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2))
colubrisSatelliteManagementMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0))
satelliteUpNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0, 1)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
if mibBuilder.loadTexts: satelliteUpNotification.setStatus('current')
satelliteDownNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0, 2)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
if mibBuilder.loadTexts: satelliteDownNotification.setStatus('current')
colubrisSatelliteManagementMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3))
colubrisSatelliteManagementMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 1))
colubrisSatelliteManagementMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2))
colubrisSatelliteManagementMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 1, 1)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "colubrisSatelliteManagementMIBGroup"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "colubrisSatelliteNotificationControlGroup"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "colubrisSatelliteNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteManagementMIBCompliance = colubrisSatelliteManagementMIBCompliance.setStatus('current')
colubrisSatelliteManagementMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 1)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumber"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteForwardWirelessToWireless"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMasterTrafficOnly"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSNMPPort"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSecureWebPort"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteProductName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteFirmwareRevision"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteGroupName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteNumber"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumberRadio2"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteVLAN"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDetectionPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteManagementMIBGroup = colubrisSatelliteManagementMIBGroup.setStatus('current')
colubrisSatelliteNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 2)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotificationEnabled"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteNotificationControlGroup = colubrisSatelliteNotificationControlGroup.setStatus('current')
colubrisSatelliteNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 3)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotification"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteNotificationGroup = colubrisSatelliteNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SATELLITE-MANAGEMENT-MIB", satelliteNumber=satelliteNumber, colubrisSatelliteNotificationControlGroup=colubrisSatelliteNotificationControlGroup, satelliteForwardWirelessToWireless=satelliteForwardWirelessToWireless, colubrisSatelliteManagementMIB=colubrisSatelliteManagementMIB, satelliteIpAddress=satelliteIpAddress, satelliteIndex=satelliteIndex, satelliteEntry=satelliteEntry, colubrisSatelliteManagementMIBCompliance=colubrisSatelliteManagementMIBCompliance, satelliteMacAddress=satelliteMacAddress, satelliteMasterTrafficOnly=satelliteMasterTrafficOnly, satelliteUpNotificationEnabled=satelliteUpNotificationEnabled, satelliteInfo=satelliteInfo, satelliteDownNotificationEnabled=satelliteDownNotificationEnabled, colubrisSatelliteManagementMIBNotificationPrefix=colubrisSatelliteManagementMIBNotificationPrefix, satelliteDownNotification=satelliteDownNotification, PYSNMP_MODULE_ID=colubrisSatelliteManagementMIB, satelliteChannelNumber=satelliteChannelNumber, masterSettings=masterSettings, satelliteName=satelliteName, satelliteProductName=satelliteProductName, satelliteDetectionPort=satelliteDetectionPort, satelliteSNMPPort=satelliteSNMPPort, satelliteSSID=satelliteSSID, satelliteUpNotification=satelliteUpNotification, satelliteFirmwareRevision=satelliteFirmwareRevision, satelliteVLAN=satelliteVLAN, satelliteGroupName=satelliteGroupName, satelliteChannelNumberRadio2=satelliteChannelNumberRadio2, colubrisSatelliteManagementMIBConformance=colubrisSatelliteManagementMIBConformance, colubrisSatelliteManagementMIBGroup=colubrisSatelliteManagementMIBGroup, satelliteSecureWebPort=satelliteSecureWebPort, satelliteTable=satelliteTable, colubrisSatelliteManagementMIBNotifications=colubrisSatelliteManagementMIBNotifications, satelliteDeviceMacAddress=satelliteDeviceMacAddress, colubrisSatelliteManagementMIBGroups=colubrisSatelliteManagementMIBGroups, satelliteDeviceId=satelliteDeviceId, colubrisSatelliteManagementMIBCompliances=colubrisSatelliteManagementMIBCompliances, colubrisSatelliteNotificationGroup=colubrisSatelliteNotificationGroup, colubrisSatelliteManagementMIBObjects=colubrisSatelliteManagementMIBObjects)