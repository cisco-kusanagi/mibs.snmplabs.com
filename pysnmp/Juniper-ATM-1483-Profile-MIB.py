#
# PySNMP MIB module Juniper-ATM-1483-Profile-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ATM-1483-Profile-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniProfileIfEncaps, = mibBuilder.importSymbols("Juniper-PROFILE-MIB", "JuniProfileIfEncaps")
JuniEnable, JuniSetMap = mibBuilder.importSymbols("Juniper-TC", "JuniEnable", "JuniSetMap")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32, NotificationType, MibIdentifier, Bits, Counter32, ObjectIdentity, IpAddress, Integer32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32", "NotificationType", "MibIdentifier", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniAtm1483ProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58))
juniAtm1483ProfileMIB.setRevisions(('2005-11-18 14:07', '2004-11-02 21:07', '2004-11-02 21:07', '2004-11-02 21:07',))
if mibBuilder.loadTexts: juniAtm1483ProfileMIB.setLastUpdated('200511181407Z')
if mibBuilder.loadTexts: juniAtm1483ProfileMIB.setOrganization('Juniper Networks, Inc.')
juniAtm1483ProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1))
juniAtm1483Profile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1))
juniAtm1483ProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1), )
if mibBuilder.loadTexts: juniAtm1483ProfileTable.setStatus('current')
juniAtm1483ProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileId"))
if mibBuilder.loadTexts: juniAtm1483ProfileEntry.setStatus('current')
juniAtm1483ProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniAtm1483ProfileId.setStatus('current')
juniAtm1483ProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileSetMap.setStatus('current')
juniAtm1483ProfileVccType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("rfc1483VcMux", 0), ("rfc1483Llc", 1), ("autoconfig", 2))).clone('rfc1483VcMux')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccType.setStatus('current')
juniAtm1483ProfileVccServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ubr", 0), ("ubrPcr", 1), ("nrtVbr", 2), ("cbr", 3), ("rtVbr", 4))).clone('ubr')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccServiceCategory.setStatus('current')
juniAtm1483ProfileVccPcr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 5), Gauge32()).setUnits('kilo-bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccPcr.setStatus('current')
juniAtm1483ProfileVccScr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 6), Gauge32()).setUnits('kilo-bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccScr.setStatus('current')
juniAtm1483ProfileVccMbs = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 7), Gauge32()).setUnits('cells').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccMbs.setStatus('current')
juniAtm1483ProfileIfAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileIfAlias.setStatus('current')
juniAtm1483ProfileAdvisoryRxSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kilo-bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileAdvisoryRxSpeed.setStatus('current')
juniAtm1483ProfileVccOamAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oamAdminStateDisabled", 1), ("oamAdminStateEnabled", 2))).clone('oamAdminStateDisabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccOamAdminStatus.setStatus('current')
juniAtm1483ProfileVccOamLoopbackFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVccOamLoopbackFrequency.setStatus('current')
juniAtm1483ProfileVcClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileVcClassName.setStatus('current')
juniAtm1483ProfileAutoConfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2), )
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfTable.setStatus('current')
juniAtm1483ProfileAutoConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfId"), (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEncaps"))
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfEntry.setStatus('current')
juniAtm1483ProfileAutoConfId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfId.setStatus('current')
juniAtm1483ProfileAutoConfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 2), JuniProfileIfEncaps())
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfEncaps.setStatus('current')
juniAtm1483ProfileAutoConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 3), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfEnable.setStatus('current')
juniAtm1483ProfileAutoConfLockoutMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfLockoutMin.setStatus('current')
juniAtm1483ProfileAutoConfLockoutMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileAutoConfLockoutMax.setStatus('current')
juniAtm1483ProfileNestedProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3), )
if mibBuilder.loadTexts: juniAtm1483ProfileNestedProfileTable.setStatus('current')
juniAtm1483ProfileNestedProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileId"), (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileEncaps"))
if mibBuilder.loadTexts: juniAtm1483ProfileNestedProfileEntry.setStatus('current')
juniAtm1483ProfileNestedProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniAtm1483ProfileNestedProfileId.setStatus('current')
juniAtm1483ProfileNestedProfileEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1, 2), JuniProfileIfEncaps())
if mibBuilder.loadTexts: juniAtm1483ProfileNestedProfileEncaps.setStatus('current')
juniAtm1483ProfileNestedProfileUpperIfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileNestedProfileUpperIfProfileName.setStatus('current')
juniAtm1483ProfileSubscriberTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4), )
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberTable.setStatus('current')
juniAtm1483ProfileSubscriberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1), ).setIndexNames((0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberId"), (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberEncaps"))
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberEntry.setStatus('current')
juniAtm1483ProfileSubscriberId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberId.setStatus('current')
juniAtm1483ProfileSubscriberEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 2), JuniProfileIfEncaps())
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberEncaps.setStatus('current')
juniAtm1483ProfileSubscriberNamePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 3), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberNamePrefix.setStatus('current')
juniAtm1483ProfileSubscriberName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberName.setStatus('current')
juniAtm1483ProfileSubscriberPasswordPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 5), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberPasswordPrefix.setStatus('current')
juniAtm1483ProfileSubscriberPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberPassword.setStatus('current')
juniAtm1483ProfileSubscriberDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAtm1483ProfileSubscriberDomain.setStatus('current')
juniAtm1483ProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4))
juniAtm1483ProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1))
juniAtm1483ProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2))
juniAtm1483ProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 1)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileCompliance = juniAtm1483ProfileCompliance.setStatus('obsolete')
juniAtm1483ProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 2)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileCompliance2 = juniAtm1483ProfileCompliance2.setStatus('obsolete')
juniAtm1483ProfileCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 3)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileCompliance3 = juniAtm1483ProfileCompliance3.setStatus('obsolete')
juniAtm1483ProfileCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 4)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileCompliance4 = juniAtm1483ProfileCompliance4.setStatus('current')
juniAtm1483ProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 1)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileGroup = juniAtm1483ProfileGroup.setStatus('obsolete')
juniAtm1483ProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 2)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileGroup2 = juniAtm1483ProfileGroup2.setStatus('obsolete')
juniAtm1483ProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 3)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileGroup3 = juniAtm1483ProfileGroup3.setStatus('obsolete')
juniAtm1483ProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 4)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileGroup4 = juniAtm1483ProfileGroup4.setStatus('obsolete')
juniAtm1483ProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 5)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMin"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMax"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileGroup5 = juniAtm1483ProfileGroup5.setStatus('obsolete')
juniAtm1483ProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 6)).setObjects(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVcClassName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMin"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMax"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"), ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtm1483ProfileGroup6 = juniAtm1483ProfileGroup6.setStatus('current')
mibBuilder.exportSymbols("Juniper-ATM-1483-Profile-MIB", juniAtm1483ProfileAutoConfTable=juniAtm1483ProfileAutoConfTable, juniAtm1483ProfileNestedProfileEncaps=juniAtm1483ProfileNestedProfileEncaps, juniAtm1483ProfileSubscriberDomain=juniAtm1483ProfileSubscriberDomain, juniAtm1483ProfileSubscriberTable=juniAtm1483ProfileSubscriberTable, juniAtm1483ProfileSubscriberPassword=juniAtm1483ProfileSubscriberPassword, juniAtm1483ProfileSubscriberName=juniAtm1483ProfileSubscriberName, juniAtm1483Profile=juniAtm1483Profile, juniAtm1483ProfileVccType=juniAtm1483ProfileVccType, juniAtm1483ProfileIfAlias=juniAtm1483ProfileIfAlias, juniAtm1483ProfileSubscriberId=juniAtm1483ProfileSubscriberId, juniAtm1483ProfileGroup3=juniAtm1483ProfileGroup3, juniAtm1483ProfileCompliances=juniAtm1483ProfileCompliances, juniAtm1483ProfileObjects=juniAtm1483ProfileObjects, juniAtm1483ProfileAutoConfEncaps=juniAtm1483ProfileAutoConfEncaps, juniAtm1483ProfileAutoConfEnable=juniAtm1483ProfileAutoConfEnable, juniAtm1483ProfileVccPcr=juniAtm1483ProfileVccPcr, juniAtm1483ProfileGroup5=juniAtm1483ProfileGroup5, juniAtm1483ProfileSetMap=juniAtm1483ProfileSetMap, juniAtm1483ProfileVcClassName=juniAtm1483ProfileVcClassName, juniAtm1483ProfileNestedProfileEntry=juniAtm1483ProfileNestedProfileEntry, juniAtm1483ProfileVccScr=juniAtm1483ProfileVccScr, juniAtm1483ProfileAutoConfEntry=juniAtm1483ProfileAutoConfEntry, juniAtm1483ProfileVccOamLoopbackFrequency=juniAtm1483ProfileVccOamLoopbackFrequency, juniAtm1483ProfileNestedProfileUpperIfProfileName=juniAtm1483ProfileNestedProfileUpperIfProfileName, juniAtm1483ProfileConformance=juniAtm1483ProfileConformance, juniAtm1483ProfileTable=juniAtm1483ProfileTable, juniAtm1483ProfileSubscriberNamePrefix=juniAtm1483ProfileSubscriberNamePrefix, juniAtm1483ProfileCompliance4=juniAtm1483ProfileCompliance4, juniAtm1483ProfileGroup4=juniAtm1483ProfileGroup4, juniAtm1483ProfileVccMbs=juniAtm1483ProfileVccMbs, juniAtm1483ProfileSubscriberEncaps=juniAtm1483ProfileSubscriberEncaps, juniAtm1483ProfileAutoConfLockoutMin=juniAtm1483ProfileAutoConfLockoutMin, juniAtm1483ProfileAutoConfId=juniAtm1483ProfileAutoConfId, juniAtm1483ProfileCompliance2=juniAtm1483ProfileCompliance2, PYSNMP_MODULE_ID=juniAtm1483ProfileMIB, juniAtm1483ProfileCompliance=juniAtm1483ProfileCompliance, juniAtm1483ProfileNestedProfileId=juniAtm1483ProfileNestedProfileId, juniAtm1483ProfileSubscriberEntry=juniAtm1483ProfileSubscriberEntry, juniAtm1483ProfileAutoConfLockoutMax=juniAtm1483ProfileAutoConfLockoutMax, juniAtm1483ProfileVccOamAdminStatus=juniAtm1483ProfileVccOamAdminStatus, juniAtm1483ProfileSubscriberPasswordPrefix=juniAtm1483ProfileSubscriberPasswordPrefix, juniAtm1483ProfileGroups=juniAtm1483ProfileGroups, juniAtm1483ProfileCompliance3=juniAtm1483ProfileCompliance3, juniAtm1483ProfileGroup=juniAtm1483ProfileGroup, juniAtm1483ProfileGroup2=juniAtm1483ProfileGroup2, juniAtm1483ProfileGroup6=juniAtm1483ProfileGroup6, juniAtm1483ProfileAdvisoryRxSpeed=juniAtm1483ProfileAdvisoryRxSpeed, juniAtm1483ProfileMIB=juniAtm1483ProfileMIB, juniAtm1483ProfileEntry=juniAtm1483ProfileEntry, juniAtm1483ProfileVccServiceCategory=juniAtm1483ProfileVccServiceCategory, juniAtm1483ProfileId=juniAtm1483ProfileId, juniAtm1483ProfileNestedProfileTable=juniAtm1483ProfileNestedProfileTable)
