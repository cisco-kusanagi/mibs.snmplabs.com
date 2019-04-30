#
# PySNMP MIB module CISCO-DDP-IAPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DDP-IAPP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, ObjectIdentity, NotificationType, Integer32, Gauge32, IpAddress, Counter32, Bits, Counter64, Unsigned32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ObjectIdentity", "NotificationType", "Integer32", "Gauge32", "IpAddress", "Counter32", "Bits", "Counter64", "Unsigned32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention")
ciscoDdpIappMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 277))
ciscoDdpIappMIB.setRevisions(('2002-07-31 00:00', '2002-07-17 00:00', '2002-03-19 00:00', '2002-03-07 00:00', '2001-09-28 00:00',))
if mibBuilder.loadTexts: ciscoDdpIappMIB.setLastUpdated('200207310000Z')
if mibBuilder.loadTexts: ciscoDdpIappMIB.setOrganization('Cisco System Inc.')
ciscoDdpIappMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 0))
ciscoDdpIappMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1))
ciscoDdpIappMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2))
cDdpIappGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1))
cDdpIappRogueApInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2))
cDdpIappMcastIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddrType.setStatus('current')
cDdpIappMcastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 2), InetAddress().clone(hexValue="e0000128")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappMcastIpAddr.setStatus('current')
cDdpIappPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 3), CiscoPort().clone(2887)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappPort.setStatus('current')
cDdpIappRogueApNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDdpIappRogueApNotifEnabled.setStatus('current')
cDdpIappLastRogueApMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 277, 1, 2, 1), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDdpIappLastRogueApMacAddr.setStatus('current')
cDdpIappLastRogueApNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 277, 0, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if mibBuilder.loadTexts: cDdpIappLastRogueApNotif.setStatus('current')
ciscoDdpIappMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1))
ciscoDdpIappMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2))
ciscoDdpIappCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 1, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "ciscoDdpIappConfigGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappRogueApInfoGroup"), ("CISCO-DDP-IAPP-MIB", "ciscoDdpIappNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappCompliance = ciscoDdpIappCompliance.setStatus('current')
ciscoDdpIappConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 1)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddrType"), ("CISCO-DDP-IAPP-MIB", "cDdpIappMcastIpAddr"), ("CISCO-DDP-IAPP-MIB", "cDdpIappPort"), ("CISCO-DDP-IAPP-MIB", "cDdpIappRogueApNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappConfigGroup = ciscoDdpIappConfigGroup.setStatus('current')
ciscoDdpIappRogueApInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 2)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappRogueApInfoGroup = ciscoDdpIappRogueApInfoGroup.setStatus('current')
ciscoDdpIappNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 277, 2, 2, 3)).setObjects(("CISCO-DDP-IAPP-MIB", "cDdpIappLastRogueApNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDdpIappNotificationGroup = ciscoDdpIappNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DDP-IAPP-MIB", PYSNMP_MODULE_ID=ciscoDdpIappMIB, cDdpIappRogueApInfo=cDdpIappRogueApInfo, ciscoDdpIappConfigGroup=ciscoDdpIappConfigGroup, cDdpIappLastRogueApMacAddr=cDdpIappLastRogueApMacAddr, ciscoDdpIappMIBGroups=ciscoDdpIappMIBGroups, cDdpIappGlobalConfig=cDdpIappGlobalConfig, ciscoDdpIappRogueApInfoGroup=ciscoDdpIappRogueApInfoGroup, cDdpIappMcastIpAddrType=cDdpIappMcastIpAddrType, ciscoDdpIappNotificationGroup=ciscoDdpIappNotificationGroup, cDdpIappPort=cDdpIappPort, cDdpIappLastRogueApNotif=cDdpIappLastRogueApNotif, cDdpIappRogueApNotifEnabled=cDdpIappRogueApNotifEnabled, ciscoDdpIappMIBNotifications=ciscoDdpIappMIBNotifications, cDdpIappMcastIpAddr=cDdpIappMcastIpAddr, ciscoDdpIappMIB=ciscoDdpIappMIB, ciscoDdpIappCompliance=ciscoDdpIappCompliance, ciscoDdpIappMIBConformance=ciscoDdpIappMIBConformance, ciscoDdpIappMIBCompliances=ciscoDdpIappMIBCompliances, ciscoDdpIappMIBObjects=ciscoDdpIappMIBObjects)
