#
# PySNMP MIB module Juniper-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LICENSE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, NotificationType, Integer32, Bits, IpAddress, MibIdentifier, iso, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "NotificationType", "Integer32", "Bits", "IpAddress", "MibIdentifier", "iso", "Gauge32", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76))
juniLicenseMIB.setRevisions(('2004-09-14 19:24',))
if mibBuilder.loadTexts: juniLicenseMIB.setLastUpdated('200409141924Z')
if mibBuilder.loadTexts: juniLicenseMIB.setOrganization('Juniper Networks, Inc.')
juniLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1))
juniLicenseLineModuleIfLimitKey = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitKey.setStatus('current')
juniLicenseLineModuleIfLimitValue = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitValue.setStatus('current')
juniLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2))
juniLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1))
juniLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2))
juniLicenseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1, 1)).setObjects(("Juniper-LICENSE-MIB", "juniLicenseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseCompliance = juniLicenseCompliance.setStatus('current')
juniLicenseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2, 1)).setObjects(("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitKey"), ("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseGroup = juniLicenseGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-LICENSE-MIB", juniLicenseGroup=juniLicenseGroup, juniLicenseLineModuleIfLimitKey=juniLicenseLineModuleIfLimitKey, juniLicenseMIB=juniLicenseMIB, juniLicenseObjects=juniLicenseObjects, juniLicenseMIBCompliances=juniLicenseMIBCompliances, juniLicenseLineModuleIfLimitValue=juniLicenseLineModuleIfLimitValue, juniLicenseCompliance=juniLicenseCompliance, juniLicenseMIBConformance=juniLicenseMIBConformance, juniLicenseMIBGroups=juniLicenseMIBGroups, PYSNMP_MODULE_ID=juniLicenseMIB)
