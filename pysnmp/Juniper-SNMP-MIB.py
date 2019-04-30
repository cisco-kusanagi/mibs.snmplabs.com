#
# PySNMP MIB module Juniper-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Counter32, TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, Counter64, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "Counter64", "Gauge32", "Integer32")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
juniSnmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16))
juniSnmpMIB.setRevisions(('2008-09-30 06:59', '2008-04-03 10:29', '2006-09-18 08:09', '2006-04-26 13:49', '2006-01-01 00:00', '2005-06-23 13:49', '2005-05-12 21:53', '2004-06-23 13:49', '2004-01-05 16:09', '2003-12-10 15:00', '2003-02-05 22:24', '2002-11-20 14:40', '2002-08-15 20:18', '2002-08-14 19:09', '2001-11-07 17:09', '2001-11-07 15:00', '2001-05-08 12:06', '2000-08-02 00:00', '2000-05-09 00:00', '1999-02-17 00:00',))
if mibBuilder.loadTexts: juniSnmpMIB.setLastUpdated('200809300659Z')
if mibBuilder.loadTexts: juniSnmpMIB.setOrganization('Juniper Networks, Inc.')
class JuniSnmpCommunityName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class JuniSnmpAccessListName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class JuniSnmpTrapMask(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class JuniTrapSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("trapEmergency", 0), ("trapAlert", 1), ("trapCritical", 2), ("trapError", 3), ("trapWarning", 4), ("trapNotice", 5), ("trapInformational", 6), ("trapDebug", 7))

class JuniSnmpIntfCompRestrictedMask(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class JuniSnmpManagementApplicationIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("eventMgr", 1))

juniSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1))
juniSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2))
juniSnmpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1))
juniSnmpInterfaceCompress = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3))
juniSnmpCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2))
juniSnmpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3))
juniSnmpAuthFailId = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4))
juniSnmpMaxPduSize = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 8192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpMaxPduSize.setStatus('current')
juniSnmpInterfaceMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("verbose", 1), ("compress", 2), ("enhanced", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpInterfaceMode.setStatus('obsolete')
juniSnmpProxyStatus = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 4), JuniEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpProxyStatus.setStatus('current')
juniSnmpAccessPermission = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAccess", 1), ("readAccess", 2), ("readWriteAccess", 3))).clone('noAccess')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpAccessPermission.setStatus('current')
juniSnmpIntfCompCompressed = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpIntfCompCompressed.setStatus('current')
juniSnmpIntfCompEnhanced = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpIntfCompEnhanced.setStatus('current')
juniSnmpIntfCompEnhancedDisplay = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpIntfCompEnhancedDisplay.setStatus('current')
juniSnmpIntfCompRestricted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 4), JuniSnmpIntfCompRestrictedMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpIntfCompRestricted.setStatus('current')
juniSnmpIntfCompRestrictedDisplay = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpIntfCompRestrictedDisplay.setStatus('current')
juniSnmpIntfCompTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6), )
if mibBuilder.loadTexts: juniSnmpIntfCompTable.setStatus('current')
juniSnmpIntfCompEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1), ).setIndexNames((0, "Juniper-SNMP-MIB", "juniSnmpIntfCompTableType"))
if mibBuilder.loadTexts: juniSnmpIntfCompEntry.setStatus('current')
juniSnmpIntfCompTableType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("others", 0), ("ifTables", 1), ("ifStackTables", 2))))
if mibBuilder.loadTexts: juniSnmpIntfCompTableType.setStatus('current')
juniSnmpIntfCompEntryCompressed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpIntfCompEntryCompressed.setStatus('current')
juniSnmpIntfCompMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpIntfCompMask.setStatus('current')
juniSnmpIntfCompMaskDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpIntfCompMaskDisplay.setStatus('current')
juniSnmpManagementApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6), )
if mibBuilder.loadTexts: juniSnmpManagementApplicationTable.setStatus('current')
juniSnmpManagementApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1), ).setIndexNames((0, "Juniper-SNMP-MIB", "juniSnmpManagementApplicationRouterIndex"), (0, "Juniper-SNMP-MIB", "juniSnmpManagementApplicationIndex"))
if mibBuilder.loadTexts: juniSnmpManagementApplicationEntry.setStatus('current')
juniSnmpManagementApplicationRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniSnmpManagementApplicationRouterIndex.setStatus('current')
juniSnmpManagementApplicationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1, 2), JuniSnmpManagementApplicationIndex())
if mibBuilder.loadTexts: juniSnmpManagementApplicationIndex.setStatus('current')
juniSnmpManagementApplicationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpManagementApplicationRowStatus.setStatus('current')
juniSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1), )
if mibBuilder.loadTexts: juniSnmpCommunityTable.setStatus('current')
juniSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1), ).setIndexNames((1, "Juniper-SNMP-MIB", "juniSnmpCommunityName"))
if mibBuilder.loadTexts: juniSnmpCommunityEntry.setStatus('current')
juniSnmpCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 1), JuniSnmpCommunityName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpCommunityName.setStatus('current')
juniSnmpCommunityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpCommunityRowStatus.setStatus('current')
juniSnmpCommunityPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2), ("admin", 3))).clone('readOnly')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpCommunityPrivilege.setStatus('current')
juniSnmpCommunityAccessList = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpCommunityAccessList.setStatus('current')
juniSnmpCommunityAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 5), JuniSnmpAccessListName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpCommunityAccessListName.setStatus('current')
juniSnmpCommunityView = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('user')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpCommunityView.setStatus('current')
juniSnmpTrapGlobalFilter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 1), JuniSnmpTrapMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpTrapGlobalFilter.setStatus('current')
juniSnmpTrapSource = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpTrapSource.setStatus('current')
juniSnmpTrapHostTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3), )
if mibBuilder.loadTexts: juniSnmpTrapHostTable.setStatus('current')
juniSnmpTrapHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1), ).setIndexNames((0, "Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"))
if mibBuilder.loadTexts: juniSnmpTrapHostEntry.setStatus('current')
juniSnmpTrapHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapHostIpAddress.setStatus('current')
juniSnmpTrapHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostRowStatus.setStatus('current')
juniSnmpTrapHostUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostUdpPort.setStatus('current')
juniSnmpTrapHostCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 4), JuniSnmpCommunityName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostCommunity.setStatus('current')
juniSnmpTrapHostProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("v1", 0), ("v2c", 1), ("v3", 2))).clone('v1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostProtocolVersion.setStatus('current')
juniSnmpTrapHostFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 6), JuniSnmpTrapMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostFilter.setStatus('current')
juniSnmpTrapHostSends = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapHostSends.setStatus('current')
juniSnmpTrapHostDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapHostDiscards.setStatus('current')
juniSnmpTrapHostSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 9), JuniTrapSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostSeverityFilter.setStatus('current')
juniSnmpTrapHostPingTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 90)).clone(1)).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostPingTimeOut.setStatus('current')
juniSnmpTrapHostIncludeLogVarbinds = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostIncludeLogVarbinds.setStatus('current')
juniSnmpTrapHostQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 2147483647)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostQueueSize.setStatus('current')
juniSnmpTrapHostQueueDrainRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostQueueDrainRate.setStatus('current')
juniSnmpTrapHostQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dropLastIn", 0), ("dropFirstIn", 1))).clone('dropLastIn')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSnmpTrapHostQueueFull.setStatus('current')
juniSnmpTrapHostBadEncodingDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapHostBadEncodingDiscards.setStatus('current')
juniSnmpTrapHostQueueFullDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapHostQueueFullDiscards.setStatus('current')
juniSnmpTrapHostNoResponseDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapHostNoResponseDiscards.setStatus('current')
juniSnmpTrapProxy = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpTrapProxy.setStatus('current')
juniSnmpTrapTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 5), JuniTrapSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSnmpTrapTrapSeverity.setStatus('current')
juniSnmpTrapGlobalDiscards = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapGlobalDiscards.setStatus('current')
juniSnmpTrapGlobalSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 7), JuniTrapSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpTrapGlobalSeverityFilter.setStatus('current')
juniSnmpTrapTotalTrapsReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapTotalTrapsReceived.setStatus('current')
juniSnmpTrapLocalTrapsSubmitted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapLocalTrapsSubmitted.setStatus('current')
juniSnmpTrapProxyTrapsSubmitted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapProxyTrapsSubmitted.setStatus('current')
juniSnmpTrapTotalTrapsDiscarded = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapTotalTrapsDiscarded.setStatus('current')
juniSnmpTrapNoMemoryDiscards = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapNoMemoryDiscards.setStatus('current')
juniSnmpTrapNoQueueResourceDiscards = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapNoQueueResourceDiscards.setStatus('current')
juniSnmpTrapAgentSnmpNotAbleDiscards = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapAgentSnmpNotAbleDiscards.setStatus('current')
juniSnmpTrapTotalTrapsOut = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapTotalTrapsOut.setStatus('current')
juniSnmpTrapTotalProxyOut = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSnmpTrapTotalProxyOut.setStatus('current')
juniSnmpTrapSeverityFilterTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17), )
if mibBuilder.loadTexts: juniSnmpTrapSeverityFilterTable.setStatus('current')
juniSnmpTrapSeverityFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17, 1), ).setIndexNames((0, "Juniper-SNMP-MIB", "juniSnmpTrapCategory"))
if mibBuilder.loadTexts: juniSnmpTrapSeverityFilterEntry.setStatus('current')
juniSnmpTrapCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: juniSnmpTrapCategory.setStatus('current')
juniSnmpTrapSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17, 1, 2), JuniTrapSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSnmpTrapSeverityFilter.setStatus('current')
juniSnmpAuthFailIdIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSnmpAuthFailIdIpAddress.setStatus('current')
juniSnmpAuthFailIdUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSnmpAuthFailIdUdpPort.setStatus('current')
juniSnmpAuthFailIdCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 3), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSnmpAuthFailIdCommunity.setStatus('current')
juniSnmpAuthFailIdReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("other", 0), ("badCommunityName", 1), ("badCommmunityUse", 2), ("hostDenied", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniSnmpAuthFailIdReason.setStatus('current')
juniSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1))
juniSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2))
juniSnmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 1)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGroup"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance = juniSnmpCompliance.setStatus('obsolete')
juniSnmpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 2)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGroup2"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance2 = juniSnmpCompliance2.setStatus('obsolete')
juniSnmpCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 3)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGroup3"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance3 = juniSnmpCompliance3.setStatus('obsolete')
juniSnmpCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 4)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGeneralGroup"), ("Juniper-SNMP-MIB", "juniSnmpAccessGroup"), ("Juniper-SNMP-MIB", "juniSnmpTrapGroup"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance4 = juniSnmpCompliance4.setStatus('obsolete')
juniSnmpCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 5)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGeneralGroup2"), ("Juniper-SNMP-MIB", "juniSnmpAccessGroup"), ("Juniper-SNMP-MIB", "juniSnmpTrapGroup"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance5 = juniSnmpCompliance5.setStatus('obsolete')
juniSnmpCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 6)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGeneralGroup2"), ("Juniper-SNMP-MIB", "juniSnmpAccessGroup"), ("Juniper-SNMP-MIB", "juniSnmpTrapGroup2"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance6 = juniSnmpCompliance6.setStatus('obsolete')
juniSnmpCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 7)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGeneralGroup3"), ("Juniper-SNMP-MIB", "juniSnmpAccessGroup"), ("Juniper-SNMP-MIB", "juniSnmpTrapGroup2"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance7 = juniSnmpCompliance7.setStatus('obsolete')
juniSnmpCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 8)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGeneralGroup3"), ("Juniper-SNMP-MIB", "juniSnmpAccessGroup"), ("Juniper-SNMP-MIB", "juniSnmpTrapGroup3"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance8 = juniSnmpCompliance8.setStatus('obsolete')
juniSnmpCompliance9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 9)).setObjects(("Juniper-SNMP-MIB", "juniSnmpGeneralGroup4"), ("Juniper-SNMP-MIB", "juniSnmpAccessGroup"), ("Juniper-SNMP-MIB", "juniSnmpTrapGroup3"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpCompliance9 = juniSnmpCompliance9.setStatus('current')
juniSnmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 1)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpCommunityName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapSource"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGroup = juniSnmpGroup.setStatus('obsolete')
juniSnmpAuthFailGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 2)).setObjects(("Juniper-SNMP-MIB", "juniSnmpAuthFailIdIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailIdUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailIdCommunity"), ("Juniper-SNMP-MIB", "juniSnmpAuthFailIdReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAuthFailGroup = juniSnmpAuthFailGroup.setStatus('current')
juniSnmpGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 3)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpCommunityName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessListName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityView"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapSource"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGroup2 = juniSnmpGroup2.setStatus('obsolete')
juniSnmpGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 4)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpInterfaceMode"), ("Juniper-SNMP-MIB", "juniSnmpCommunityName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessListName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityView"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapSource"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGroup3 = juniSnmpGroup3.setStatus('obsolete')
juniSnmpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 5)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGeneralGroup = juniSnmpGeneralGroup.setStatus('obsolete')
juniSnmpAccessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 6)).setObjects(("Juniper-SNMP-MIB", "juniSnmpCommunityName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"), ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessListName"), ("Juniper-SNMP-MIB", "juniSnmpCommunityView"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpAccessGroup = juniSnmpAccessGroup.setStatus('current')
juniSnmpTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 7)).setObjects(("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapSource"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSeverityFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapTrapSeverity"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalSeverityFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpTrapGroup = juniSnmpTrapGroup.setStatus('obsolete')
juniSnmpGeneralGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 8)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpProxyStatus"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGeneralGroup2 = juniSnmpGeneralGroup2.setStatus('obsolete')
juniSnmpTrapGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 9)).setObjects(("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapSource"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSeverityFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostPingTimeOut"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIncludeLogVarbinds"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueSize"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueDrainRate"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFull"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostBadEncodingDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFullDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostNoResponseDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapTrapSeverity"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalSeverityFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsReceived"), ("Juniper-SNMP-MIB", "juniSnmpTrapLocalTrapsSubmitted"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxyTrapsSubmitted"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsDiscarded"), ("Juniper-SNMP-MIB", "juniSnmpTrapNoMemoryDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapNoQueueResourceDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapAgentSnmpNotAbleDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsOut"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalProxyOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpTrapGroup2 = juniSnmpTrapGroup2.setStatus('obsolete')
juniSnmpGeneralGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 10)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpProxyStatus"), ("Juniper-SNMP-MIB", "juniSnmpAccessPermission"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"), ("Juniper-SNMP-MIB", "juniSnmpManagementApplicationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGeneralGroup3 = juniSnmpGeneralGroup3.setStatus('obsolete')
juniSnmpTrapGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 11)).setObjects(("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapSource"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostSeverityFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostPingTimeOut"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostIncludeLogVarbinds"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueSize"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueDrainRate"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFull"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostBadEncodingDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFullDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapHostNoResponseDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapTrapSeverity"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalSeverityFilter"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsReceived"), ("Juniper-SNMP-MIB", "juniSnmpTrapLocalTrapsSubmitted"), ("Juniper-SNMP-MIB", "juniSnmpTrapProxyTrapsSubmitted"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsDiscarded"), ("Juniper-SNMP-MIB", "juniSnmpTrapNoMemoryDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapNoQueueResourceDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapAgentSnmpNotAbleDiscards"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsOut"), ("Juniper-SNMP-MIB", "juniSnmpTrapTotalProxyOut"), ("Juniper-SNMP-MIB", "juniSnmpTrapSeverityFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpTrapGroup3 = juniSnmpTrapGroup3.setStatus('current')
juniSnmpGeneralGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 12)).setObjects(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"), ("Juniper-SNMP-MIB", "juniSnmpProxyStatus"), ("Juniper-SNMP-MIB", "juniSnmpAccessPermission"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"), ("Juniper-SNMP-MIB", "juniSnmpManagementApplicationRowStatus"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompEntryCompressed"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompMask"), ("Juniper-SNMP-MIB", "juniSnmpIntfCompMaskDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSnmpGeneralGroup4 = juniSnmpGeneralGroup4.setStatus('current')
mibBuilder.exportSymbols("Juniper-SNMP-MIB", juniSnmpIntfCompEnhancedDisplay=juniSnmpIntfCompEnhancedDisplay, juniSnmpTrapSource=juniSnmpTrapSource, juniSnmpTrapAgentSnmpNotAbleDiscards=juniSnmpTrapAgentSnmpNotAbleDiscards, juniSnmpGeneralGroup3=juniSnmpGeneralGroup3, juniSnmpTrapHostDiscards=juniSnmpTrapHostDiscards, juniSnmpCompliance7=juniSnmpCompliance7, juniSnmpCompliances=juniSnmpCompliances, juniSnmpMIB=juniSnmpMIB, juniSnmpManagementApplicationRouterIndex=juniSnmpManagementApplicationRouterIndex, juniSnmpAuthFailIdIpAddress=juniSnmpAuthFailIdIpAddress, juniSnmpAuthFailIdReason=juniSnmpAuthFailIdReason, juniSnmpAccessGroup=juniSnmpAccessGroup, juniSnmpCommunityAccessListName=juniSnmpCommunityAccessListName, JuniTrapSeverity=JuniTrapSeverity, juniSnmpCompliance=juniSnmpCompliance, juniSnmpTrapSeverityFilterTable=juniSnmpTrapSeverityFilterTable, juniSnmpInterfaceCompress=juniSnmpInterfaceCompress, juniSnmpCommunityTable=juniSnmpCommunityTable, juniSnmpGeneralGroup=juniSnmpGeneralGroup, juniSnmpManagementApplicationIndex=juniSnmpManagementApplicationIndex, juniSnmpAuthFailIdUdpPort=juniSnmpAuthFailIdUdpPort, juniSnmpManagementApplicationRowStatus=juniSnmpManagementApplicationRowStatus, juniSnmpTrapTotalTrapsOut=juniSnmpTrapTotalTrapsOut, JuniSnmpIntfCompRestrictedMask=JuniSnmpIntfCompRestrictedMask, juniSnmpTrapHostPingTimeOut=juniSnmpTrapHostPingTimeOut, juniSnmpGeneralGroup2=juniSnmpGeneralGroup2, juniSnmpGroup3=juniSnmpGroup3, juniSnmpTrapHostCommunity=juniSnmpTrapHostCommunity, juniSnmpTrapHostProtocolVersion=juniSnmpTrapHostProtocolVersion, juniSnmpTrapProxy=juniSnmpTrapProxy, juniSnmpCompliance9=juniSnmpCompliance9, juniSnmpManagementApplicationEntry=juniSnmpManagementApplicationEntry, juniSnmpTrapGlobalFilter=juniSnmpTrapGlobalFilter, juniSnmpIntfCompMaskDisplay=juniSnmpIntfCompMaskDisplay, juniSnmpGroups=juniSnmpGroups, juniSnmpTrapHostQueueFullDiscards=juniSnmpTrapHostQueueFullDiscards, juniSnmpIntfCompRestrictedDisplay=juniSnmpIntfCompRestrictedDisplay, juniSnmpAuthFailGroup=juniSnmpAuthFailGroup, juniSnmpAccessPermission=juniSnmpAccessPermission, juniSnmpIntfCompRestricted=juniSnmpIntfCompRestricted, juniSnmpTrapHostQueueDrainRate=juniSnmpTrapHostQueueDrainRate, juniSnmpCompliance3=juniSnmpCompliance3, juniSnmpCommunityEntry=juniSnmpCommunityEntry, juniSnmpTrapGroup3=juniSnmpTrapGroup3, juniSnmpCommunityName=juniSnmpCommunityName, juniSnmpTrapHostTable=juniSnmpTrapHostTable, juniSnmpCompliance6=juniSnmpCompliance6, JuniSnmpAccessListName=JuniSnmpAccessListName, juniSnmpCommunityView=juniSnmpCommunityView, juniSnmpCompliance2=juniSnmpCompliance2, juniSnmpGeneralGroup4=juniSnmpGeneralGroup4, juniSnmpConformance=juniSnmpConformance, juniSnmpTrapHostSeverityFilter=juniSnmpTrapHostSeverityFilter, juniSnmpTrapHostEntry=juniSnmpTrapHostEntry, juniSnmpProxyStatus=juniSnmpProxyStatus, juniSnmpTrapHostRowStatus=juniSnmpTrapHostRowStatus, juniSnmpIntfCompMask=juniSnmpIntfCompMask, JuniSnmpCommunityName=JuniSnmpCommunityName, juniSnmpCompliance4=juniSnmpCompliance4, juniSnmpIntfCompEntry=juniSnmpIntfCompEntry, juniSnmpTrapProxyTrapsSubmitted=juniSnmpTrapProxyTrapsSubmitted, juniSnmpCompliance5=juniSnmpCompliance5, juniSnmpCommunityRowStatus=juniSnmpCommunityRowStatus, juniSnmpTrapGlobalSeverityFilter=juniSnmpTrapGlobalSeverityFilter, juniSnmpIntfCompTable=juniSnmpIntfCompTable, juniSnmpTrapHostIncludeLogVarbinds=juniSnmpTrapHostIncludeLogVarbinds, juniSnmpManagementApplicationTable=juniSnmpManagementApplicationTable, juniSnmpCommunity=juniSnmpCommunity, juniSnmpTrapHostQueueSize=juniSnmpTrapHostQueueSize, juniSnmpIntfCompEnhanced=juniSnmpIntfCompEnhanced, juniSnmpMaxPduSize=juniSnmpMaxPduSize, juniSnmpTrapTotalProxyOut=juniSnmpTrapTotalProxyOut, juniSnmpTrap=juniSnmpTrap, juniSnmpCommunityAccessList=juniSnmpCommunityAccessList, juniSnmpCompliance8=juniSnmpCompliance8, juniSnmpTrapSeverityFilter=juniSnmpTrapSeverityFilter, juniSnmpTrapNoQueueResourceDiscards=juniSnmpTrapNoQueueResourceDiscards, juniSnmpCommunityPrivilege=juniSnmpCommunityPrivilege, juniSnmpIntfCompCompressed=juniSnmpIntfCompCompressed, juniSnmpGroup2=juniSnmpGroup2, JuniSnmpManagementApplicationIndex=JuniSnmpManagementApplicationIndex, juniSnmpTrapSeverityFilterEntry=juniSnmpTrapSeverityFilterEntry, juniSnmpAuthFailIdCommunity=juniSnmpAuthFailIdCommunity, juniSnmpInterfaceMode=juniSnmpInterfaceMode, juniSnmpTrapHostUdpPort=juniSnmpTrapHostUdpPort, juniSnmpTrapGroup=juniSnmpTrapGroup, PYSNMP_MODULE_ID=juniSnmpMIB, juniSnmpIntfCompEntryCompressed=juniSnmpIntfCompEntryCompressed, juniSnmpTrapTotalTrapsDiscarded=juniSnmpTrapTotalTrapsDiscarded, juniSnmpTrapHostBadEncodingDiscards=juniSnmpTrapHostBadEncodingDiscards, juniSnmpGeneral=juniSnmpGeneral, juniSnmpObjects=juniSnmpObjects, juniSnmpTrapNoMemoryDiscards=juniSnmpTrapNoMemoryDiscards, juniSnmpIntfCompTableType=juniSnmpIntfCompTableType, juniSnmpTrapHostQueueFull=juniSnmpTrapHostQueueFull, juniSnmpTrapGlobalDiscards=juniSnmpTrapGlobalDiscards, juniSnmpTrapTrapSeverity=juniSnmpTrapTrapSeverity, juniSnmpTrapHostSends=juniSnmpTrapHostSends, juniSnmpTrapHostNoResponseDiscards=juniSnmpTrapHostNoResponseDiscards, juniSnmpTrapTotalTrapsReceived=juniSnmpTrapTotalTrapsReceived, juniSnmpAuthFailId=juniSnmpAuthFailId, juniSnmpGroup=juniSnmpGroup, juniSnmpTrapCategory=juniSnmpTrapCategory, JuniSnmpTrapMask=JuniSnmpTrapMask, juniSnmpTrapHostFilter=juniSnmpTrapHostFilter, juniSnmpTrapLocalTrapsSubmitted=juniSnmpTrapLocalTrapsSubmitted, juniSnmpTrapGroup2=juniSnmpTrapGroup2, juniSnmpTrapHostIpAddress=juniSnmpTrapHostIpAddress)
