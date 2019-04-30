#
# PySNMP MIB module VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPLS-LDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
pwIndex, pwID = mibBuilder.importSymbols("PW-STD-MIB", "pwIndex", "pwID")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
transmission, Counter64, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, ModuleIdentity, MibIdentifier, TimeTicks, Counter32, Unsigned32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "Counter64", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Unsigned32", "ObjectIdentity", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
vplsConfigName, vplsConfigIndex = mibBuilder.importSymbols("VPLS-GENERIC-MIB", "vplsConfigName", "vplsConfigIndex")
vplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 275))
vplsLdpMIB.setRevisions(('2014-05-19 12:00',))
if mibBuilder.loadTexts: vplsLdpMIB.setLastUpdated('201405191200Z')
if mibBuilder.loadTexts: vplsLdpMIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
vplsLdpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 0))
vplsLdpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 1))
vplsLdpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2))
vplsLdpConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 275, 1, 1), )
if mibBuilder.loadTexts: vplsLdpConfigTable.setStatus('current')
vplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsLdpConfigEntry.setStatus('current')
vplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsLdpConfigMacAddrWithdraw.setStatus('current')
vplsLdpPwBindTable = MibTable((1, 3, 6, 1, 2, 1, 10, 275, 1, 2), )
if mibBuilder.loadTexts: vplsLdpPwBindTable.setStatus('current')
vplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: vplsLdpPwBindEntry.setStatus('current')
vplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsLdpPwBindMacAddressLimit.setStatus('current')
vplsLdpPwBindMacTableFull = NotificationType((1, 3, 6, 1, 2, 1, 10, 275, 0, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigName"), ("PW-STD-MIB", "pwID"))
if mibBuilder.loadTexts: vplsLdpPwBindMacTableFull.setStatus('current')
vplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2, 1))
vplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 1)).setObjects(("VPLS-LDP-MIB", "vplsLdpGroup"), ("VPLS-LDP-MIB", "vplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpModuleFullCompliance = vplsLdpModuleFullCompliance.setStatus('current')
vplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 2)).setObjects(("VPLS-LDP-MIB", "vplsLdpGroup"), ("VPLS-LDP-MIB", "vplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpModuleReadOnlyCompliance = vplsLdpModuleReadOnlyCompliance.setStatus('current')
vplsLdpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2, 2))
vplsLdpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 1)).setObjects(("VPLS-LDP-MIB", "vplsLdpConfigMacAddrWithdraw"), ("VPLS-LDP-MIB", "vplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpGroup = vplsLdpGroup.setStatus('current')
vplsLdpNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 2)).setObjects(("VPLS-LDP-MIB", "vplsLdpPwBindMacTableFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpNotificationGroup = vplsLdpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VPLS-LDP-MIB", vplsLdpCompliances=vplsLdpCompliances, vplsLdpConformance=vplsLdpConformance, vplsLdpConfigEntry=vplsLdpConfigEntry, vplsLdpModuleReadOnlyCompliance=vplsLdpModuleReadOnlyCompliance, vplsLdpGroup=vplsLdpGroup, vplsLdpObjects=vplsLdpObjects, vplsLdpConfigTable=vplsLdpConfigTable, vplsLdpPwBindMacTableFull=vplsLdpPwBindMacTableFull, vplsLdpGroups=vplsLdpGroups, vplsLdpMIB=vplsLdpMIB, vplsLdpConfigMacAddrWithdraw=vplsLdpConfigMacAddrWithdraw, vplsLdpModuleFullCompliance=vplsLdpModuleFullCompliance, PYSNMP_MODULE_ID=vplsLdpMIB, vplsLdpPwBindTable=vplsLdpPwBindTable, vplsLdpNotificationGroup=vplsLdpNotificationGroup, vplsLdpPwBindEntry=vplsLdpPwBindEntry, vplsLdpNotifications=vplsLdpNotifications, vplsLdpPwBindMacAddressLimit=vplsLdpPwBindMacAddressLimit)
