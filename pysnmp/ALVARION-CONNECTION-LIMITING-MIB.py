#
# PySNMP MIB module ALVARION-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-CONNECTION-LIMITING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, NotificationType, iso, TimeTicks, IpAddress, MibIdentifier, Bits, Counter64, Integer32, Unsigned32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "NotificationType", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "Counter64", "Integer32", "Unsigned32", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alvarionConnectionLimitingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18))
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionConnectionLimitingMIB.setOrganization('Alvarion Ltd.')
alvarionConnectionLimitingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1))
connectionLimitingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1))
connectionLimitingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2))
connectionLimitingMaximumUserConnections = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setStatus('current')
connectionLimitingMaximumSystemConnections = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setStatus('current')
alvarionConnectionLimitingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2))
alvarionConnectionLimitingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 2, 0))
alvarionConnectionLimitingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3))
alvarionConnectionLimitingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1))
alvarionConnectionLimitingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2))
alvarionConnectionLimitingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 1, 1)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "alvarionConnectionLimitingConfigMIBGroup"), ("ALVARION-CONNECTION-LIMITING-MIB", "alvarionConnectionLimitingInfoMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingMIBCompliance = alvarionConnectionLimitingMIBCompliance.setStatus('current')
alvarionConnectionLimitingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 1)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingConfigMIBGroup = alvarionConnectionLimitingConfigMIBGroup.setStatus('current')
alvarionConnectionLimitingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 18, 3, 2, 2)).setObjects(("ALVARION-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionConnectionLimitingInfoMIBGroup = alvarionConnectionLimitingInfoMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-CONNECTION-LIMITING-MIB", connectionLimitingConfig=connectionLimitingConfig, alvarionConnectionLimitingMIBNotificationPrefix=alvarionConnectionLimitingMIBNotificationPrefix, alvarionConnectionLimitingMIB=alvarionConnectionLimitingMIB, PYSNMP_MODULE_ID=alvarionConnectionLimitingMIB, alvarionConnectionLimitingMIBConformance=alvarionConnectionLimitingMIBConformance, alvarionConnectionLimitingMIBCompliances=alvarionConnectionLimitingMIBCompliances, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections, alvarionConnectionLimitingMIBGroups=alvarionConnectionLimitingMIBGroups, alvarionConnectionLimitingMIBNotifications=alvarionConnectionLimitingMIBNotifications, alvarionConnectionLimitingConfigMIBGroup=alvarionConnectionLimitingConfigMIBGroup, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, alvarionConnectionLimitingInfoMIBGroup=alvarionConnectionLimitingInfoMIBGroup, alvarionConnectionLimitingMIBObjects=alvarionConnectionLimitingMIBObjects, alvarionConnectionLimitingMIBCompliance=alvarionConnectionLimitingMIBCompliance, connectionLimitingInfo=connectionLimitingInfo)
