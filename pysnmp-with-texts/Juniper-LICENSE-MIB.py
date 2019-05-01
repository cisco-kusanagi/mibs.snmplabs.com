#
# PySNMP MIB module Juniper-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LICENSE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, MibIdentifier, TimeTicks, Counter32, Integer32, Counter64, Unsigned32, iso, NotificationType, IpAddress, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "Counter64", "Unsigned32", "iso", "NotificationType", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76))
juniLicenseMIB.setRevisions(('2004-09-14 19:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniLicenseMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniLicenseMIB.setLastUpdated('200409141924Z')
if mibBuilder.loadTexts: juniLicenseMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniLicenseMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniLicenseMIB.setDescription('The License Manager MIB for the Juniper Networks enterprise.')
juniLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1))
juniLicenseLineModuleIfLimitKey = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitKey.setStatus('current')
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitKey.setDescription('The license string that determines the maximum number of interfaces that can be configured on an ATM line module. A zero-length string (no license) restores the original interface limit.')
juniLicenseLineModuleIfLimitValue = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitValue.setStatus('current')
if mibBuilder.loadTexts: juniLicenseLineModuleIfLimitValue.setDescription('The maximum number of interfaces allowed on the ATM line module on the currently configured license string.')
juniLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2))
juniLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1))
juniLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2))
juniLicenseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1, 1)).setObjects(("Juniper-LICENSE-MIB", "juniLicenseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseCompliance = juniLicenseCompliance.setStatus('current')
if mibBuilder.loadTexts: juniLicenseCompliance.setDescription('The compliance statement for systems supporting licensing of features.')
juniLicenseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2, 1)).setObjects(("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitKey"), ("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniLicenseGroup = juniLicenseGroup.setStatus('current')
if mibBuilder.loadTexts: juniLicenseGroup.setDescription('The basic collection of objects providing management of feature licenses in a Juniper product.')
mibBuilder.exportSymbols("Juniper-LICENSE-MIB", juniLicenseLineModuleIfLimitValue=juniLicenseLineModuleIfLimitValue, juniLicenseGroup=juniLicenseGroup, PYSNMP_MODULE_ID=juniLicenseMIB, juniLicenseMIB=juniLicenseMIB, juniLicenseMIBConformance=juniLicenseMIBConformance, juniLicenseMIBCompliances=juniLicenseMIBCompliances, juniLicenseMIBGroups=juniLicenseMIBGroups, juniLicenseObjects=juniLicenseObjects, juniLicenseCompliance=juniLicenseCompliance, juniLicenseLineModuleIfLimitKey=juniLicenseLineModuleIfLimitKey)
