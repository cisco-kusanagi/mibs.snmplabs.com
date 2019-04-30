#
# PySNMP MIB module Unisphere-Data-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter64, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter64", "TimeTicks", "Integer32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdSnmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16))
usdSnmpMIB.setRevisions(('2002-08-15 20:18', '2002-08-14 19:09', '2001-11-07 17:09', '2001-11-07 15:00', '2001-05-08 12:06', '2000-08-02 00:00', '2000-05-09 00:00', '1999-02-17 00:00',))
if mibBuilder.loadTexts: usdSnmpMIB.setLastUpdated('200208152018Z')
if mibBuilder.loadTexts: usdSnmpMIB.setOrganization('Juniper Networks, Inc.')
class UsdSnmpCommunityName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class UsdSnmpAccessListName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class UsdSnmpTrapMask(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class UsdTrapSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("trapEmergency", 0), ("trapAlert", 1), ("trapCritical", 2), ("trapError", 3), ("trapWarning", 4), ("trapNotice", 5), ("trapInformational", 6), ("trapDebug", 7))

class UsdSnmpIntfCompRestrictedMask(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

usdSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1))
usdSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2))
usdSnmpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1))
usdSnmpInterfaceCompress = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3))
usdSnmpCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2))
usdSnmpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3))
usdSnmpAuthFailId = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4))
usdSnmpMaxPduSize = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 8192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpMaxPduSize.setStatus('current')
usdSnmpInterfaceMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("usdSnmpInterfaceModeVerbose", 1), ("usdSnmpInterfaceModeCompress", 2), ("usdSnmpInterfaceModeEnhanced", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpInterfaceMode.setStatus('obsolete')
usdSnmpProxyStatus = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 4), UsdEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpProxyStatus.setStatus('current')
usdSnmpIntfCompCompressed = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpIntfCompCompressed.setStatus('current')
usdSnmpIntfCompEnhanced = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpIntfCompEnhanced.setStatus('current')
usdSnmpIntfCompEnhancedDisplay = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpIntfCompEnhancedDisplay.setStatus('current')
usdSnmpIntfCompRestricted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 4), UsdSnmpIntfCompRestrictedMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpIntfCompRestricted.setStatus('current')
usdSnmpIntfCompRestrictedDisplay = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpIntfCompRestrictedDisplay.setStatus('current')
usdSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1), )
if mibBuilder.loadTexts: usdSnmpCommunityTable.setStatus('current')
usdSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1), ).setIndexNames((1, "Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"))
if mibBuilder.loadTexts: usdSnmpCommunityEntry.setStatus('current')
usdSnmpCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 1), UsdSnmpCommunityName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpCommunityName.setStatus('current')
usdSnmpCommunityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityRowStatus.setStatus('current')
usdSnmpCommunityPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2), ("admin", 3))).clone('readOnly')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityPrivilege.setStatus('current')
usdSnmpCommunityAccessList = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityAccessList.setStatus('current')
usdSnmpCommunityAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 5), UsdSnmpAccessListName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityAccessListName.setStatus('current')
usdSnmpCommunityView = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("everything", 1), ("user", 2), ("nothing", 3))).clone('user')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityView.setStatus('current')
usdSnmpTrapGlobalFilter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 1), UsdSnmpTrapMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapGlobalFilter.setStatus('current')
usdSnmpTrapSource = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapSource.setStatus('current')
usdSnmpTrapHostTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3), )
if mibBuilder.loadTexts: usdSnmpTrapHostTable.setStatus('current')
usdSnmpTrapHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1), ).setIndexNames((0, "Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"))
if mibBuilder.loadTexts: usdSnmpTrapHostEntry.setStatus('current')
usdSnmpTrapHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapHostIpAddress.setStatus('current')
usdSnmpTrapHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostRowStatus.setStatus('current')
usdSnmpTrapHostUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostUdpPort.setStatus('current')
usdSnmpTrapHostCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 4), UsdSnmpCommunityName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostCommunity.setStatus('current')
usdSnmpTrapHostProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("v1", 0), ("v2c", 1), ("v3", 2))).clone('v1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostProtocolVersion.setStatus('current')
usdSnmpTrapHostFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 6), UsdSnmpTrapMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostFilter.setStatus('current')
usdSnmpTrapHostSends = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapHostSends.setStatus('current')
usdSnmpTrapHostDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapHostDiscards.setStatus('current')
usdSnmpTrapHostSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 9), UsdTrapSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostSeverityFilter.setStatus('current')
usdSnmpTrapProxy = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapProxy.setStatus('current')
usdSnmpTrapTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 5), UsdTrapSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpTrapTrapSeverity.setStatus('current')
usdSnmpTrapGlobalDiscards = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapGlobalDiscards.setStatus('current')
usdSnmpTrapGlobalSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 7), UsdTrapSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapGlobalSeverityFilter.setStatus('current')
usdSnmpAuthFailIdIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdIpAddress.setStatus('current')
usdSnmpAuthFailIdUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdUdpPort.setStatus('current')
usdSnmpAuthFailIdCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 3), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdCommunity.setStatus('current')
usdSnmpAuthFailIdReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("other", 0), ("badCommunityName", 1), ("badCommmunityUse", 2), ("hostDenied", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdReason.setStatus('current')
usdSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1))
usdSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2))
usdSnmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 1)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance = usdSnmpCompliance.setStatus('obsolete')
usdSnmpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 2)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGroup2"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance2 = usdSnmpCompliance2.setStatus('obsolete')
usdSnmpCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 3)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGroup3"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance3 = usdSnmpCompliance3.setStatus('obsolete')
usdSnmpCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 4)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGeneralGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAccessGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance4 = usdSnmpCompliance4.setStatus('obsolete')
usdSnmpCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 5)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGeneralGroup2"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAccessGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance5 = usdSnmpCompliance5.setStatus('current')
usdSnmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 1)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGroup = usdSnmpGroup.setStatus('obsolete')
usdSnmpAuthFailGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 2)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAuthFailGroup = usdSnmpAuthFailGroup.setStatus('current')
usdSnmpGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 3)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGroup2 = usdSnmpGroup2.setStatus('obsolete')
usdSnmpGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 4)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpInterfaceMode"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGroup3 = usdSnmpGroup3.setStatus('obsolete')
usdSnmpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 5)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompCompressed"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhanced"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhancedDisplay"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestricted"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestrictedDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGeneralGroup = usdSnmpGeneralGroup.setStatus('obsolete')
usdSnmpAccessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 6)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAccessGroup = usdSnmpAccessGroup.setStatus('current')
usdSnmpTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 7)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostDiscards"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSeverityFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapTrapSeverity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalDiscards"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalSeverityFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpTrapGroup = usdSnmpTrapGroup.setStatus('current')
usdSnmpGeneralGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 8)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpProxyStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompCompressed"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhanced"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhancedDisplay"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestricted"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestrictedDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGeneralGroup2 = usdSnmpGeneralGroup2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SNMP-MIB", usdSnmpGroup3=usdSnmpGroup3, usdSnmpTrapHostProtocolVersion=usdSnmpTrapHostProtocolVersion, usdSnmpProxyStatus=usdSnmpProxyStatus, usdSnmpCommunityAccessList=usdSnmpCommunityAccessList, UsdSnmpAccessListName=UsdSnmpAccessListName, usdSnmpTrapHostUdpPort=usdSnmpTrapHostUdpPort, usdSnmpIntfCompEnhanced=usdSnmpIntfCompEnhanced, usdSnmpAuthFailId=usdSnmpAuthFailId, UsdSnmpCommunityName=UsdSnmpCommunityName, usdSnmpTrapGlobalFilter=usdSnmpTrapGlobalFilter, usdSnmpCommunityTable=usdSnmpCommunityTable, usdSnmpAuthFailIdCommunity=usdSnmpAuthFailIdCommunity, usdSnmpTrapHostFilter=usdSnmpTrapHostFilter, usdSnmpIntfCompCompressed=usdSnmpIntfCompCompressed, usdSnmpCommunityRowStatus=usdSnmpCommunityRowStatus, usdSnmpAuthFailIdIpAddress=usdSnmpAuthFailIdIpAddress, usdSnmpAuthFailGroup=usdSnmpAuthFailGroup, usdSnmpInterfaceMode=usdSnmpInterfaceMode, usdSnmpTrapProxy=usdSnmpTrapProxy, usdSnmpTrapHostRowStatus=usdSnmpTrapHostRowStatus, usdSnmpCompliances=usdSnmpCompliances, usdSnmpIntfCompEnhancedDisplay=usdSnmpIntfCompEnhancedDisplay, usdSnmpTrapHostEntry=usdSnmpTrapHostEntry, usdSnmpMIB=usdSnmpMIB, usdSnmpCompliance4=usdSnmpCompliance4, UsdSnmpIntfCompRestrictedMask=UsdSnmpIntfCompRestrictedMask, usdSnmpTrapTrapSeverity=usdSnmpTrapTrapSeverity, usdSnmpGroup=usdSnmpGroup, usdSnmpAuthFailIdReason=usdSnmpAuthFailIdReason, usdSnmpGeneralGroup2=usdSnmpGeneralGroup2, usdSnmpCompliance3=usdSnmpCompliance3, usdSnmpCommunityView=usdSnmpCommunityView, usdSnmpMaxPduSize=usdSnmpMaxPduSize, usdSnmpCommunityName=usdSnmpCommunityName, usdSnmpTrapHostDiscards=usdSnmpTrapHostDiscards, UsdTrapSeverity=UsdTrapSeverity, usdSnmpTrapHostSeverityFilter=usdSnmpTrapHostSeverityFilter, usdSnmpAuthFailIdUdpPort=usdSnmpAuthFailIdUdpPort, usdSnmpCompliance=usdSnmpCompliance, usdSnmpCompliance5=usdSnmpCompliance5, usdSnmpCommunityEntry=usdSnmpCommunityEntry, UsdSnmpTrapMask=UsdSnmpTrapMask, usdSnmpTrapHostTable=usdSnmpTrapHostTable, usdSnmpGeneralGroup=usdSnmpGeneralGroup, usdSnmpTrapSource=usdSnmpTrapSource, usdSnmpTrapGroup=usdSnmpTrapGroup, PYSNMP_MODULE_ID=usdSnmpMIB, usdSnmpConformance=usdSnmpConformance, usdSnmpCommunity=usdSnmpCommunity, usdSnmpTrapHostSends=usdSnmpTrapHostSends, usdSnmpGroups=usdSnmpGroups, usdSnmpCommunityPrivilege=usdSnmpCommunityPrivilege, usdSnmpCompliance2=usdSnmpCompliance2, usdSnmpIntfCompRestricted=usdSnmpIntfCompRestricted, usdSnmpGroup2=usdSnmpGroup2, usdSnmpTrapGlobalSeverityFilter=usdSnmpTrapGlobalSeverityFilter, usdSnmpIntfCompRestrictedDisplay=usdSnmpIntfCompRestrictedDisplay, usdSnmpCommunityAccessListName=usdSnmpCommunityAccessListName, usdSnmpTrapHostIpAddress=usdSnmpTrapHostIpAddress, usdSnmpTrapHostCommunity=usdSnmpTrapHostCommunity, usdSnmpTrap=usdSnmpTrap, usdSnmpTrapGlobalDiscards=usdSnmpTrapGlobalDiscards, usdSnmpGeneral=usdSnmpGeneral, usdSnmpInterfaceCompress=usdSnmpInterfaceCompress, usdSnmpObjects=usdSnmpObjects, usdSnmpAccessGroup=usdSnmpAccessGroup)
