#
# PySNMP MIB module Juniper-HTTP-Profile-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-HTTP-Profile-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniSetMap, = mibBuilder.importSymbols("Juniper-TC", "JuniSetMap")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Integer32, TimeTicks, ObjectIdentity, Counter64, MibIdentifier, Gauge32, Counter32, NotificationType, Bits, iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "ObjectIdentity", "Counter64", "MibIdentifier", "Gauge32", "Counter32", "NotificationType", "Bits", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniHttpProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79))
juniHttpProfileMIB.setRevisions(('2005-08-19 14:21',))
if mibBuilder.loadTexts: juniHttpProfileMIB.setLastUpdated('200508191421Z')
if mibBuilder.loadTexts: juniHttpProfileMIB.setOrganization('Juniper Networks, Inc.')
juniHttpProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1))
juniHttpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1))
juniHttpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1), )
if mibBuilder.loadTexts: juniHttpProfileTable.setStatus('current')
juniHttpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-HTTP-Profile-MIB", "juniHttpProfileId"))
if mibBuilder.loadTexts: juniHttpProfileEntry.setStatus('current')
juniHttpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniHttpProfileId.setStatus('current')
juniHttpProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniHttpProfileSetMap.setStatus('current')
juniHttpProfileRedirectUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniHttpProfileRedirectUrl.setStatus('current')
juniHttpProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4))
juniHttpProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1))
juniHttpProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2))
juniHttpProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1, 1)).setObjects(("Juniper-HTTP-Profile-MIB", "juniHttpProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHttpProfileCompliance = juniHttpProfileCompliance.setStatus('current')
juniHttpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2, 1)).setObjects(("Juniper-HTTP-Profile-MIB", "juniHttpProfileSetMap"), ("Juniper-HTTP-Profile-MIB", "juniHttpProfileRedirectUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHttpProfileGroup = juniHttpProfileGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-HTTP-Profile-MIB", juniHttpProfileMIB=juniHttpProfileMIB, juniHttpProfileObjects=juniHttpProfileObjects, juniHttpProfileConformance=juniHttpProfileConformance, juniHttpProfileCompliances=juniHttpProfileCompliances, juniHttpProfileGroups=juniHttpProfileGroups, juniHttpProfileGroup=juniHttpProfileGroup, juniHttpProfileSetMap=juniHttpProfileSetMap, juniHttpProfileCompliance=juniHttpProfileCompliance, juniHttpProfileTable=juniHttpProfileTable, juniHttpProfile=juniHttpProfile, PYSNMP_MODULE_ID=juniHttpProfileMIB, juniHttpProfileEntry=juniHttpProfileEntry, juniHttpProfileRedirectUrl=juniHttpProfileRedirectUrl, juniHttpProfileId=juniHttpProfileId)
