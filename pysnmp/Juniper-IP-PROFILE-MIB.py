#
# PySNMP MIB module Juniper-IP-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniName, JuniSetMap, JuniEnable = mibBuilder.importSymbols("Juniper-TC", "JuniName", "JuniSetMap", "JuniEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, Counter32, MibIdentifier, iso, TimeTicks, Gauge32, ModuleIdentity, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "Counter32", "MibIdentifier", "iso", "TimeTicks", "Gauge32", "ModuleIdentity", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniIpProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26))
juniIpProfileMIB.setRevisions(('2006-09-08 10:26', '2005-09-13 17:21', '2004-10-05 14:04', '2003-09-24 15:33', '2002-10-11 13:20', '2001-01-24 20:06', '2000-05-08 00:00', '1999-08-25 00:00',))
if mibBuilder.loadTexts: juniIpProfileMIB.setLastUpdated('200609081026Z')
if mibBuilder.loadTexts: juniIpProfileMIB.setOrganization('Juniper Networks')
juniIpProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1))
juniIpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1))
juniIpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1), )
if mibBuilder.loadTexts: juniIpProfileTable.setStatus('current')
juniIpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-IP-PROFILE-MIB", "juniIpProfileId"))
if mibBuilder.loadTexts: juniIpProfileEntry.setStatus('current')
juniIpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniIpProfileId.setStatus('current')
juniIpProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileRowStatus.setStatus('deprecated')
juniIpProfileRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 3), JuniName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileRouterName.setStatus('current')
juniIpProfileIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIpAddr.setStatus('current')
juniIpProfileIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIpMask.setStatus('current')
juniIpProfileDirectedBcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 6), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileDirectedBcastEnable.setStatus('current')
juniIpProfileIcmpRedirectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 7), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIcmpRedirectEnable.setStatus('current')
juniIpProfileAccessRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 8), JuniEnable().clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileAccessRoute.setStatus('current')
juniIpProfileMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(512, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileMtu.setStatus('current')
juniIpProfileLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileLoopbackIfIndex.setStatus('obsolete')
juniIpProfileLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileLoopback.setStatus('obsolete')
juniIpProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 12), JuniSetMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileSetMap.setStatus('current')
juniIpProfileSrcAddrValidEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 13), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileSrcAddrValidEnable.setStatus('current')
juniIpProfileInheritNumString = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileInheritNumString.setStatus('current')
juniIpProfileTcpMss = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(160, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileTcpMss.setStatus('current')
juniIpProfileFilterOptionsAll = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 16), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileFilterOptionsAll.setStatus('current')
juniIpProfileFlowStats = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 17), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileFlowStats.setStatus('current')
juniIpProfileBlockMulticastSources = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 18), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileBlockMulticastSources.setStatus('current')
juniIpProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4))
juniIpProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1))
juniIpProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2))
juniIpProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 1)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance = juniIpProfileCompliance.setStatus('obsolete')
juniIpProfileCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 2)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance1 = juniIpProfileCompliance1.setStatus('obsolete')
juniIpProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 3)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance2 = juniIpProfileCompliance2.setStatus('obsolete')
juniIpProfileCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 4)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance3 = juniIpProfileCompliance3.setStatus('obsolete')
juniIpProfileCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 5)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance4 = juniIpProfileCompliance4.setStatus('obsolete')
juniIpProfileCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 6)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance5 = juniIpProfileCompliance5.setStatus('current')
juniIpProfileCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 7)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance6 = juniIpProfileCompliance6.setStatus('current')
juniIpProfileCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 8)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance7 = juniIpProfileCompliance7.setStatus('current')
juniIpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 1)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopbackIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup = juniIpProfileGroup.setStatus('obsolete')
juniIpProfileGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 2)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup1 = juniIpProfileGroup1.setStatus('obsolete')
juniIpProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 3)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup2 = juniIpProfileGroup2.setStatus('obsolete')
juniIpProfileDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 4)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileDeprecatedGroup = juniIpProfileDeprecatedGroup.setStatus('deprecated')
juniIpProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 5)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup3 = juniIpProfileGroup3.setStatus('obsolete')
juniIpProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 6)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup4 = juniIpProfileGroup4.setStatus('obsolete')
juniIpProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 7)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup5 = juniIpProfileGroup5.setStatus('obsolete')
juniIpProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 8)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup6 = juniIpProfileGroup6.setStatus('obsolete')
juniIpProfileGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 9)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileBlockMulticastSources"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup7 = juniIpProfileGroup7.setStatus('current')
mibBuilder.exportSymbols("Juniper-IP-PROFILE-MIB", juniIpProfileTable=juniIpProfileTable, juniIpProfileMIB=juniIpProfileMIB, juniIpProfileAccessRoute=juniIpProfileAccessRoute, juniIpProfileRowStatus=juniIpProfileRowStatus, juniIpProfileMtu=juniIpProfileMtu, juniIpProfileMIBCompliances=juniIpProfileMIBCompliances, juniIpProfileGroup5=juniIpProfileGroup5, juniIpProfileTcpMss=juniIpProfileTcpMss, juniIpProfileGroup3=juniIpProfileGroup3, juniIpProfileDeprecatedGroup=juniIpProfileDeprecatedGroup, juniIpProfileIpAddr=juniIpProfileIpAddr, juniIpProfileCompliance=juniIpProfileCompliance, juniIpProfileCompliance5=juniIpProfileCompliance5, juniIpProfileGroup1=juniIpProfileGroup1, juniIpProfileFlowStats=juniIpProfileFlowStats, juniIpProfileCompliance7=juniIpProfileCompliance7, juniIpProfileMIBGroups=juniIpProfileMIBGroups, juniIpProfileCompliance1=juniIpProfileCompliance1, juniIpProfileGroup6=juniIpProfileGroup6, juniIpProfileGroup2=juniIpProfileGroup2, juniIpProfileObjects=juniIpProfileObjects, PYSNMP_MODULE_ID=juniIpProfileMIB, juniIpProfile=juniIpProfile, juniIpProfileSetMap=juniIpProfileSetMap, juniIpProfileCompliance6=juniIpProfileCompliance6, juniIpProfileRouterName=juniIpProfileRouterName, juniIpProfileCompliance4=juniIpProfileCompliance4, juniIpProfileGroup4=juniIpProfileGroup4, juniIpProfileIcmpRedirectEnable=juniIpProfileIcmpRedirectEnable, juniIpProfileIpMask=juniIpProfileIpMask, juniIpProfileLoopbackIfIndex=juniIpProfileLoopbackIfIndex, juniIpProfileGroup7=juniIpProfileGroup7, juniIpProfileSrcAddrValidEnable=juniIpProfileSrcAddrValidEnable, juniIpProfileDirectedBcastEnable=juniIpProfileDirectedBcastEnable, juniIpProfileGroup=juniIpProfileGroup, juniIpProfileId=juniIpProfileId, juniIpProfileCompliance2=juniIpProfileCompliance2, juniIpProfileMIBConformance=juniIpProfileMIBConformance, juniIpProfileEntry=juniIpProfileEntry, juniIpProfileCompliance3=juniIpProfileCompliance3, juniIpProfileLoopback=juniIpProfileLoopback, juniIpProfileFilterOptionsAll=juniIpProfileFilterOptionsAll, juniIpProfileInheritNumString=juniIpProfileInheritNumString, juniIpProfileBlockMulticastSources=juniIpProfileBlockMulticastSources)
