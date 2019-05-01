#
# PySNMP MIB module ALVARION-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-CONNECTION-LIMITING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, NotificationType, MibIdentifier, ObjectIdentity, Integer32, Bits, IpAddress, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "MibIdentifier", "ObjectIdentity", "Integer32", "Bits", "IpAddress", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionConnectionLimitingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18))
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setDescription('Alvarion Connection limiting module.')
alvarionConnectionLimitingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1))
connectionLimitingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1))
connectionLimitingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2))
connectionLimitingMaximumUserConnections = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setDescription('Specifies the maximum number of simultaneous connections allowed for a specific user. If this amount of connections is reached, no other connections will be allowed for user and a trap is generated.')
connectionLimitingMaximumSystemConnections = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setDescription('Indicates the maximum number of simultaneous connections that are supported by the device. This is calculated based on the device type and available memory.')
alvarionConnectionLimitingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2))
alvarionConnectionLimitingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2, 0))
alvarionConnectionLimitingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3))
alvarionConnectionLimitingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1))
alvarionConnectionLimitingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2))
alvarionConnectionLimitingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1, 1)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "alvarionConnectionLimitingConfigMIBGroup"), ("ALVARION-CONNECTION-LIMITING-MIB", "alvarionConnectionLimitingInfoMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingMIBCompliance = alvarionConnectionLimitingMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionConnectionLimitingMIBCompliance.setDescription('The compliance statement for entities which implement the Alvarion Tools MIB.')
alvarionConnectionLimitingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 1)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingConfigMIBGroup = alvarionConnectionLimitingConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionConnectionLimitingConfigMIBGroup.setDescription('A collection of objects providing control over the connection limiting MIB capability.')
alvarionConnectionLimitingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 2)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingInfoMIBGroup = alvarionConnectionLimitingInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionConnectionLimitingInfoMIBGroup.setDescription('A collection of objects providing information over the connection limiting MIB capability.')
mibBuilder.exportSymbols("ALVARION-CONNECTION-LIMITING-MIB", connectionLimitingInfo=connectionLimitingInfo, alvarionConnectionLimitingConfigMIBGroup=alvarionConnectionLimitingConfigMIBGroup, connectionLimitingConfig=connectionLimitingConfig, alvarionConnectionLimitingMIB=alvarionConnectionLimitingMIB, alvarionConnectionLimitingMIBGroups=alvarionConnectionLimitingMIBGroups, alvarionConnectionLimitingInfoMIBGroup=alvarionConnectionLimitingInfoMIBGroup, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, alvarionConnectionLimitingMIBNotifications=alvarionConnectionLimitingMIBNotifications, alvarionConnectionLimitingMIBObjects=alvarionConnectionLimitingMIBObjects, alvarionConnectionLimitingMIBConformance=alvarionConnectionLimitingMIBConformance, alvarionConnectionLimitingMIBCompliance=alvarionConnectionLimitingMIBCompliance, PYSNMP_MODULE_ID=alvarionConnectionLimitingMIB, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections, alvarionConnectionLimitingMIBCompliances=alvarionConnectionLimitingMIBCompliances, alvarionConnectionLimitingMIBNotificationPrefix=alvarionConnectionLimitingMIBNotificationPrefix)
