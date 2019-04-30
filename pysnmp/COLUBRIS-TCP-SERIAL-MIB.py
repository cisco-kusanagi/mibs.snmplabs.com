#
# PySNMP MIB module COLUBRIS-TCP-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-TCP-SERIAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, MibIdentifier, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Integer32, TimeTicks, NotificationType, Gauge32, Counter64, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "Counter64", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisTCPSerialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 37))
if mibBuilder.loadTexts: colubrisTCPSerialMIB.setLastUpdated('200808210000Z')
if mibBuilder.loadTexts: colubrisTCPSerialMIB.setOrganization('Colubris Networks, Inc.')
colubrisTCPSerialMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1))
coTCPSerialStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1))
coTCPSerialConnectionStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("active", 3), ("idle", 4), ("connect", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialConnectionStatus.setStatus('current')
coTCPSerialRemoteIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialRemoteIPAddress.setStatus('current')
coTCPSerialRemoteTCPPort = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialRemoteTCPPort.setStatus('current')
coTCPSerialConnectTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialConnectTime.setStatus('current')
coTCPSerialTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 5), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialTxBytes.setStatus('current')
coTCPSerialRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 6), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: coTCPSerialRxBytes.setStatus('current')
colubrisTCPSerialMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 2))
colubrisTCPSerialMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 2, 0))
colubrisTCPSerialMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3))
colubrisTCPSerialMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 1))
colubrisTCPSerialMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 2))
colubrisTCPSerialMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 1, 1)).setObjects(("COLUBRIS-TCP-SERIAL-MIB", "colubrisTCPSerialConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisTCPSerialMIBCompliance = colubrisTCPSerialMIBCompliance.setStatus('current')
colubrisTCPSerialConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 2, 1)).setObjects(("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialConnectionStatus"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRemoteIPAddress"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRemoteTCPPort"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialConnectTime"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialTxBytes"), ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRxBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisTCPSerialConfigMIBGroup = colubrisTCPSerialConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-TCP-SERIAL-MIB", colubrisTCPSerialConfigMIBGroup=colubrisTCPSerialConfigMIBGroup, coTCPSerialConnectionStatus=coTCPSerialConnectionStatus, coTCPSerialRxBytes=coTCPSerialRxBytes, colubrisTCPSerialMIBCompliances=colubrisTCPSerialMIBCompliances, colubrisTCPSerialMIBNotifications=colubrisTCPSerialMIBNotifications, coTCPSerialRemoteIPAddress=coTCPSerialRemoteIPAddress, coTCPSerialStatusGroup=coTCPSerialStatusGroup, colubrisTCPSerialMIB=colubrisTCPSerialMIB, colubrisTCPSerialMIBObjects=colubrisTCPSerialMIBObjects, coTCPSerialConnectTime=coTCPSerialConnectTime, colubrisTCPSerialMIBGroups=colubrisTCPSerialMIBGroups, colubrisTCPSerialMIBCompliance=colubrisTCPSerialMIBCompliance, coTCPSerialTxBytes=coTCPSerialTxBytes, PYSNMP_MODULE_ID=colubrisTCPSerialMIB, colubrisTCPSerialMIBNotificationPrefix=colubrisTCPSerialMIBNotificationPrefix, colubrisTCPSerialMIBConformance=colubrisTCPSerialMIBConformance, coTCPSerialRemoteTCPPort=coTCPSerialRemoteTCPPort)
