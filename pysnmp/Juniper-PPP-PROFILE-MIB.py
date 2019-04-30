#
# PySNMP MIB module Juniper-PPP-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPP-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniPppAuthentication, = mibBuilder.importSymbols("Juniper-PPP-MIB", "JuniPppAuthentication")
JuniName, JuniSetMap, JuniEnable, JuniNibbleConfig = mibBuilder.importSymbols("Juniper-TC", "JuniName", "JuniSetMap", "JuniEnable", "JuniNibbleConfig")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, ModuleIdentity, Integer32, ObjectIdentity, NotificationType, iso, Bits, TimeTicks, Counter32, IpAddress, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "ObjectIdentity", "NotificationType", "iso", "Bits", "TimeTicks", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPppProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45))
juniPppProfileMIB.setRevisions(('2009-09-18 07:24', '2009-08-10 14:23', '2007-07-12 12:15', '2005-10-19 16:26', '2003-11-03 21:10', '2003-09-29 18:58', '2003-03-11 21:59', '2002-09-16 21:44', '2002-09-03 22:38', '2002-01-25 14:00', '2002-01-16 17:58', '2002-01-08 19:43', '2001-10-02 12:41',))
if mibBuilder.loadTexts: juniPppProfileMIB.setLastUpdated('200909180724Z')
if mibBuilder.loadTexts: juniPppProfileMIB.setOrganization('Juniper Networks, Inc.')
juniPppProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1))
juniPppProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1))
juniPppProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1), )
if mibBuilder.loadTexts: juniPppProfileTable.setStatus('current')
juniPppProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-PPP-PROFILE-MIB", "juniPppProfileId"))
if mibBuilder.loadTexts: juniPppProfileEntry.setStatus('current')
juniPppProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniPppProfileId.setStatus('current')
juniPppProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileSetMap.setStatus('current')
juniPppProfileLcpMagicNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileLcpMagicNumber.setStatus('current')
juniPppProfileLcpKeepalive = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 64800), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileLcpKeepalive.setStatus('current')
juniPppProfileLcpAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 5), JuniPppAuthentication().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileLcpAuthentication.setStatus('deprecated')
juniPppProfileIpPeerDnsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 6), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileIpPeerDnsPriority.setStatus('current')
juniPppProfileIpPeerWinsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 7), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileIpPeerWinsPriority.setStatus('current')
juniPppProfileLcpInitialMRU = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(64, 65535), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileLcpInitialMRU.setStatus('current')
juniPppProfilePacketLog = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 9), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfilePacketLog.setStatus('current')
juniPppProfileStateLog = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 10), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileStateLog.setStatus('current')
juniPppProfileChapMinChallengeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 63)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileChapMinChallengeLength.setStatus('current')
juniPppProfileChapMaxChallengeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 63)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileChapMaxChallengeLength.setStatus('current')
juniPppProfilePassiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 13), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfilePassiveMode.setStatus('current')
juniPppProfileMlppp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 14), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileMlppp.setStatus('current')
juniPppProfileIpcpNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 15), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileIpcpNetmask.setStatus('current')
juniPppProfileAuthenticatorVirtualRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 16), JuniName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileAuthenticatorVirtualRouter.setStatus('current')
juniPppProfileAaaProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 17), JuniName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileAaaProfile.setStatus('current')
juniPppProfileInitiateIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 18), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileInitiateIp.setStatus('current')
juniPppProfileInitiateIpv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 19), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileInitiateIpv6.setStatus('current')
juniPppProfileFragmentation = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 20), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileFragmentation.setStatus('current')
juniPppProfileReassembly = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 21), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileReassembly.setStatus('current')
juniPppProfileMaxReceiveReconstructedUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(64, 65535), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileMaxReceiveReconstructedUnit.setStatus('current')
juniPppProfileFragmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(128, 65535), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileFragmentSize.setStatus('current')
juniPppProfileHashLinkSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 24), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileHashLinkSelection.setStatus('current')
juniPppProfileLcpAuthentication2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 25), JuniNibbleConfig()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileLcpAuthentication2.setStatus('current')
juniPppProfileIgnoreMagicNumberMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 26), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileIgnoreMagicNumberMismatch.setStatus('current')
juniPppProfileIpcpPromptDnsOption = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 27), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileIpcpPromptDnsOption.setStatus('current')
juniPppProfileIpcpLockout = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 28), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileIpcpLockout.setStatus('current')
juniPppProfileMultilinkMulticlass = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 29), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniPppProfileMultilinkMulticlass.setStatus('current')
juniPppProfileMultilinkMaxMultiClasses = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniPppProfileMultilinkMaxMultiClasses.setStatus('current')
class JuniPppProfileMulticlassTcName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

juniPppProfileMulticlassTraffiClassTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2), )
if mibBuilder.loadTexts: juniPppProfileMulticlassTraffiClassTable.setStatus('current')
juniPppProfileMulticlassTrafficClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-PPP-PROFILE-MIB", "juniPppProfileId"), (0, "Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassIndex"))
if mibBuilder.loadTexts: juniPppProfileMulticlassTrafficClassEntry.setStatus('current')
juniPppProfileMulticlassId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniPppProfileMulticlassId.setStatus('current')
juniPppProfileMulticlassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 2), Integer32().clone(15))
if mibBuilder.loadTexts: juniPppProfileMulticlassIndex.setStatus('current')
juniPppProfileMulticlassTcName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 3), JuniPppProfileMulticlassTcName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileMulticlassTcName.setStatus('current')
juniPppProfileMulticlassFragmentation = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 4), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileMulticlassFragmentation.setStatus('current')
juniPppProfileMulticlassReassembly = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 1, 1, 2, 1, 5), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppProfileMulticlassReassembly.setStatus('current')
juniPppProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4))
juniPppProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1))
juniPppProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2))
juniPppProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 1)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance = juniPppProfileCompliance.setStatus('obsolete')
juniPppProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 2)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance2 = juniPppProfileCompliance2.setStatus('obsolete')
juniPppProfileCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 3)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance3 = juniPppProfileCompliance3.setStatus('obsolete')
juniPppProfileCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 4)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance4 = juniPppProfileCompliance4.setStatus('obsolete')
juniPppProfileCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 5)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance5 = juniPppProfileCompliance5.setStatus('obsolete')
juniPppProfileCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 6)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance6 = juniPppProfileCompliance6.setStatus('obsolete')
juniPppProfileCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 7)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance7 = juniPppProfileCompliance7.setStatus('obsolete')
juniPppProfileCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 8)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup8"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance8 = juniPppProfileCompliance8.setStatus('obsolete')
juniPppProfileCompliance9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 9)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance9 = juniPppProfileCompliance9.setStatus('obsolete')
juniPppProfileCompliance10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 1, 10)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileGroup11"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileCompliance10 = juniPppProfileCompliance10.setStatus('current')
juniPppProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 1)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup = juniPppProfileGroup.setStatus('obsolete')
juniPppProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 2)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup2 = juniPppProfileGroup2.setStatus('obsolete')
juniPppProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 3)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup3 = juniPppProfileGroup3.setStatus('obsolete')
juniPppProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 4)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup4 = juniPppProfileGroup4.setStatus('obsolete')
juniPppProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 5)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup5 = juniPppProfileGroup5.setStatus('obsolete')
juniPppProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 6)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup6 = juniPppProfileGroup6.setStatus('obsolete')
juniPppProfileGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 7)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup7 = juniPppProfileGroup7.setStatus('obsolete')
juniPppProfileGroup8 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 8)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup8 = juniPppProfileGroup8.setStatus('obsolete')
juniPppProfileGroup9 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 9)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup9 = juniPppProfileGroup9.setStatus('obsolete')
juniPppProfileGroup10 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 10)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIgnoreMagicNumberMismatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup10 = juniPppProfileGroup10.setStatus('obsolete')
juniPppProfileGroup11 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 11)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIgnoreMagicNumberMismatch"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpPromptDnsOption"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpLockout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup11 = juniPppProfileGroup11.setStatus('current')
juniPppProfileGroup12 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 12)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileSetMap"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpMagicNumber"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpKeepalive"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerDnsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpPeerWinsPriority"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpInitialMRU"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePacketLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileStateLog"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMinChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileChapMaxChallengeLength"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfilePassiveMode"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMlppp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIpcpNetmask"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAuthenticatorVirtualRouter"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileAaaProfile"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIp"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileInitiateIpv6"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileReassembly"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMaxReceiveReconstructedUnit"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileFragmentSize"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileHashLinkSelection"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileLcpAuthentication2"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileIgnoreMagicNumberMismatch"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMultilinkMulticlass"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMultilinkMaxMultiClasses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileGroup12 = juniPppProfileGroup12.setStatus('current')
juniPppProfileMulticlassTrafficClassGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 45, 4, 2, 13)).setObjects(("Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassTcName"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassFragmentation"), ("Juniper-PPP-PROFILE-MIB", "juniPppProfileMulticlassReassembly"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppProfileMulticlassTrafficClassGroup1 = juniPppProfileMulticlassTrafficClassGroup1.setStatus('current')
mibBuilder.exportSymbols("Juniper-PPP-PROFILE-MIB", juniPppProfileCompliance4=juniPppProfileCompliance4, juniPppProfileGroup3=juniPppProfileGroup3, juniPppProfileCompliances=juniPppProfileCompliances, juniPppProfileGroup5=juniPppProfileGroup5, juniPppProfileCompliance6=juniPppProfileCompliance6, juniPppProfileMaxReceiveReconstructedUnit=juniPppProfileMaxReceiveReconstructedUnit, juniPppProfileCompliance8=juniPppProfileCompliance8, juniPppProfileGroup11=juniPppProfileGroup11, juniPppProfileIpPeerDnsPriority=juniPppProfileIpPeerDnsPriority, juniPppProfileMultilinkMaxMultiClasses=juniPppProfileMultilinkMaxMultiClasses, juniPppProfileCompliance7=juniPppProfileCompliance7, juniPppProfileMulticlassTcName=juniPppProfileMulticlassTcName, juniPppProfileCompliance3=juniPppProfileCompliance3, juniPppProfileAaaProfile=juniPppProfileAaaProfile, juniPppProfileMulticlassId=juniPppProfileMulticlassId, juniPppProfileIpcpNetmask=juniPppProfileIpcpNetmask, juniPppProfileIpPeerWinsPriority=juniPppProfileIpPeerWinsPriority, juniPppProfileInitiateIpv6=juniPppProfileInitiateIpv6, juniPppProfileIpcpLockout=juniPppProfileIpcpLockout, juniPppProfileMulticlassTrafficClassEntry=juniPppProfileMulticlassTrafficClassEntry, juniPppProfileConformance=juniPppProfileConformance, juniPppProfileReassembly=juniPppProfileReassembly, juniPppProfileGroup6=juniPppProfileGroup6, juniPppProfileGroup9=juniPppProfileGroup9, juniPppProfileCompliance2=juniPppProfileCompliance2, PYSNMP_MODULE_ID=juniPppProfileMIB, juniPppProfileTable=juniPppProfileTable, juniPppProfileCompliance9=juniPppProfileCompliance9, juniPppProfileSetMap=juniPppProfileSetMap, juniPppProfileGroup7=juniPppProfileGroup7, juniPppProfileChapMinChallengeLength=juniPppProfileChapMinChallengeLength, juniPppProfileChapMaxChallengeLength=juniPppProfileChapMaxChallengeLength, juniPppProfileMulticlassIndex=juniPppProfileMulticlassIndex, juniPppProfileGroups=juniPppProfileGroups, juniPppProfileLcpMagicNumber=juniPppProfileLcpMagicNumber, juniPppProfileMulticlassTrafficClassGroup1=juniPppProfileMulticlassTrafficClassGroup1, juniPppProfileFragmentation=juniPppProfileFragmentation, juniPppProfileLcpKeepalive=juniPppProfileLcpKeepalive, juniPppProfileMultilinkMulticlass=juniPppProfileMultilinkMulticlass, juniPppProfileGroup8=juniPppProfileGroup8, juniPppProfileGroup10=juniPppProfileGroup10, juniPppProfileMIB=juniPppProfileMIB, juniPppProfileGroup12=juniPppProfileGroup12, juniPppProfileAuthenticatorVirtualRouter=juniPppProfileAuthenticatorVirtualRouter, juniPppProfileObjects=juniPppProfileObjects, juniPppProfileCompliance5=juniPppProfileCompliance5, JuniPppProfileMulticlassTcName=JuniPppProfileMulticlassTcName, juniPppProfileMulticlassReassembly=juniPppProfileMulticlassReassembly, juniPppProfileEntry=juniPppProfileEntry, juniPppProfileGroup=juniPppProfileGroup, juniPppProfileLcpAuthentication=juniPppProfileLcpAuthentication, juniPppProfileFragmentSize=juniPppProfileFragmentSize, juniPppProfileCompliance10=juniPppProfileCompliance10, juniPppProfileGroup4=juniPppProfileGroup4, juniPppProfile=juniPppProfile, juniPppProfileGroup2=juniPppProfileGroup2, juniPppProfileIpcpPromptDnsOption=juniPppProfileIpcpPromptDnsOption, juniPppProfileCompliance=juniPppProfileCompliance, juniPppProfileStateLog=juniPppProfileStateLog, juniPppProfileLcpInitialMRU=juniPppProfileLcpInitialMRU, juniPppProfileIgnoreMagicNumberMismatch=juniPppProfileIgnoreMagicNumberMismatch, juniPppProfilePacketLog=juniPppProfilePacketLog, juniPppProfilePassiveMode=juniPppProfilePassiveMode, juniPppProfileHashLinkSelection=juniPppProfileHashLinkSelection, juniPppProfileLcpAuthentication2=juniPppProfileLcpAuthentication2, juniPppProfileId=juniPppProfileId, juniPppProfileMlppp=juniPppProfileMlppp, juniPppProfileMulticlassFragmentation=juniPppProfileMulticlassFragmentation, juniPppProfileMulticlassTraffiClassTable=juniPppProfileMulticlassTraffiClassTable, juniPppProfileInitiateIp=juniPppProfileInitiateIp)
