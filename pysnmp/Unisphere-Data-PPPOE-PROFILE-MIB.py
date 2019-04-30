#
# PySNMP MIB module Unisphere-Data-PPPOE-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPPOE-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, IpAddress, ModuleIdentity, Bits, Counter64, MibIdentifier, Counter32, Integer32, Unsigned32, ObjectIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "ObjectIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, UsdSetMap = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable", "UsdSetMap")
usdPppoeProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46))
usdPppoeProfileMIB.setRevisions(('2002-08-15 20:34', '2002-08-15 19:07', '2001-03-21 18:32',))
if mibBuilder.loadTexts: usdPppoeProfileMIB.setLastUpdated('200208152034Z')
if mibBuilder.loadTexts: usdPppoeProfileMIB.setOrganization('Juniper Networks, Inc.')
usdPppoeProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1))
usdPppoeProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1))
usdPppoeProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1), )
if mibBuilder.loadTexts: usdPppoeProfileTable.setStatus('current')
usdPppoeProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileId"))
if mibBuilder.loadTexts: usdPppoeProfileEntry.setStatus('current')
usdPppoeProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdPppoeProfileId.setStatus('current')
usdPppoeProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 2), UsdSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfileSetMap.setStatus('current')
usdPppoeProfileMaxNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfileMaxNumSessions.setStatus('current')
usdPppoeProfileSubMotm = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfileSubMotm.setStatus('current')
usdPppoeProfileSubUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfileSubUrl.setStatus('current')
usdPppoeProfileDupProtect = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 6), UsdEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfileDupProtect.setStatus('current')
usdPppoeProfileAcName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfileAcName.setStatus('current')
usdPppoeProfilePadiFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 8), UsdEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfilePadiFlag.setStatus('current')
usdPppoeProfilePacketTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 9), UsdEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdPppoeProfilePacketTrace.setStatus('current')
usdPppoeProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4))
usdPppoeProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1))
usdPppoeProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2))
usdPppoeProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 1)).setObjects(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileCompliance = usdPppoeProfileCompliance.setStatus('obsolete')
usdPppoeCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 2)).setObjects(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeCompliance2 = usdPppoeCompliance2.setStatus('obsolete')
usdPppoeCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 3)).setObjects(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeCompliance3 = usdPppoeCompliance3.setStatus('current')
usdPppoeProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 1)).setObjects(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSetMap"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileMaxNumSessions"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubMotm"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileGroup = usdPppoeProfileGroup.setStatus('obsolete')
usdPppoeProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 2)).setObjects(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSetMap"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileMaxNumSessions"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubMotm"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubUrl"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileDupProtect"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileAcName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileGroup2 = usdPppoeProfileGroup2.setStatus('obsolete')
usdPppoeProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 3)).setObjects(("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSetMap"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileMaxNumSessions"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubMotm"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileSubUrl"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileDupProtect"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileAcName"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfilePadiFlag"), ("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfilePacketTrace"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileGroup3 = usdPppoeProfileGroup3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PPPOE-PROFILE-MIB", usdPppoeProfileGroup3=usdPppoeProfileGroup3, usdPppoeProfileSubMotm=usdPppoeProfileSubMotm, PYSNMP_MODULE_ID=usdPppoeProfileMIB, usdPppoeProfileTable=usdPppoeProfileTable, usdPppoeProfileObjects=usdPppoeProfileObjects, usdPppoeProfilePadiFlag=usdPppoeProfilePadiFlag, usdPppoeProfileSetMap=usdPppoeProfileSetMap, usdPppoeProfileGroup2=usdPppoeProfileGroup2, usdPppoeProfileId=usdPppoeProfileId, usdPppoeCompliance3=usdPppoeCompliance3, usdPppoeProfileConformance=usdPppoeProfileConformance, usdPppoeProfileGroups=usdPppoeProfileGroups, usdPppoeProfile=usdPppoeProfile, usdPppoeProfileDupProtect=usdPppoeProfileDupProtect, usdPppoeProfilePacketTrace=usdPppoeProfilePacketTrace, usdPppoeProfileMaxNumSessions=usdPppoeProfileMaxNumSessions, usdPppoeProfileCompliance=usdPppoeProfileCompliance, usdPppoeProfileMIB=usdPppoeProfileMIB, usdPppoeCompliance2=usdPppoeCompliance2, usdPppoeProfileGroup=usdPppoeProfileGroup, usdPppoeProfileEntry=usdPppoeProfileEntry, usdPppoeProfileCompliances=usdPppoeProfileCompliances, usdPppoeProfileSubUrl=usdPppoeProfileSubUrl, usdPppoeProfileAcName=usdPppoeProfileAcName)
