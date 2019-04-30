#
# PySNMP MIB module CISCO-IETF-VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-VPLS-LDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cvplsPwBindIndex, cvplsConfigIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex", "cvplsConfigIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, iso, NotificationType, TimeTicks, Gauge32, ModuleIdentity, ObjectIdentity, Integer32, Counter64, Bits, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter64", "Bits", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
VPNId, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNId")
cvplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 141))
cvplsLdpMIB.setRevisions(('2007-11-22 12:00',))
if mibBuilder.loadTexts: cvplsLdpMIB.setLastUpdated('200711221200Z')
if mibBuilder.loadTexts: cvplsLdpMIB.setOrganization('Cisco Systems, Inc.')
cvplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 1))
cvplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2))
cvplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1), )
if mibBuilder.loadTexts: cvplsLdpConfigTable.setStatus('current')
cvplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setStatus('current')
cvplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setStatus('current')
cvplsLdpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2), )
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setStatus('current')
cvplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setStatus('current')
cvplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setStatus('current')
cvplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1))
cvplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleFullCompliance = cvplsLdpModuleFullCompliance.setStatus('current')
cvplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 2)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleReadOnlyCompliance = cvplsLdpModuleReadOnlyCompliance.setStatus('current')
cvplsLdpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2))
cvplsLdpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpConfigMacAddrWithdraw"), ("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpGroup = cvplsLdpGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-LDP-MIB", cvplsLdpPwBindTable=cvplsLdpPwBindTable, cvplsLdpModuleReadOnlyCompliance=cvplsLdpModuleReadOnlyCompliance, cvplsLdpConfigMacAddrWithdraw=cvplsLdpConfigMacAddrWithdraw, cvplsLdpGroup=cvplsLdpGroup, cvplsLdpPwBindMacAddressLimit=cvplsLdpPwBindMacAddressLimit, cvplsLdpConfigEntry=cvplsLdpConfigEntry, cvplsLdpPwBindEntry=cvplsLdpPwBindEntry, cvplsLdpObjects=cvplsLdpObjects, cvplsLdpConformance=cvplsLdpConformance, cvplsLdpGroups=cvplsLdpGroups, PYSNMP_MODULE_ID=cvplsLdpMIB, cvplsLdpMIB=cvplsLdpMIB, cvplsLdpModuleFullCompliance=cvplsLdpModuleFullCompliance, cvplsLdpCompliances=cvplsLdpCompliances, cvplsLdpConfigTable=cvplsLdpConfigTable)
