#
# PySNMP MIB module WWP-SYSTEM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SYSTEM-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dot1dStpPort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, IpAddress, ObjectIdentity, iso, MibIdentifier, Counter32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "iso", "MibIdentifier", "Counter32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "TimeTicks")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSysCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 30))
wwpSysCtrlMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpSysCtrlMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpSysCtrlMIB.setOrganization('World Wide Packets, Inc')
wwpSysCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1))
wwpSysCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1))
wwpSysCtrlMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2))
wwpSysCtrlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0))
wwpSysCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3))
wwpSysCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 1))
wwpSysCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 2))
wwpSysCtrlBridgeRSTPEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSysCtrlBridgeRSTPEnable.setStatus('current')
wwpSysCtrlLacpEnable = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSysCtrlLacpEnable.setStatus('current')
wwpPvstBpduReceived = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0, 1)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: wwpPvstBpduReceived.setStatus('current')
mibBuilder.exportSymbols("WWP-SYSTEM-CONTROL-MIB", wwpSysCtrlMIBGroups=wwpSysCtrlMIBGroups, PYSNMP_MODULE_ID=wwpSysCtrlMIB, wwpSysCtrlMIBCompliances=wwpSysCtrlMIBCompliances, wwpSysCtrl=wwpSysCtrl, wwpSysCtrlLacpEnable=wwpSysCtrlLacpEnable, wwpSysCtrlMIBObjects=wwpSysCtrlMIBObjects, wwpSysCtrlBridgeRSTPEnable=wwpSysCtrlBridgeRSTPEnable, wwpSysCtrlMIBConformance=wwpSysCtrlMIBConformance, wwpPvstBpduReceived=wwpPvstBpduReceived, wwpSysCtrlMIBNotifications=wwpSysCtrlMIBNotifications, wwpSysCtrlMIB=wwpSysCtrlMIB, wwpSysCtrlMIBNotificationPrefix=wwpSysCtrlMIBNotificationPrefix)
