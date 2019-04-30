#
# PySNMP MIB module Juniper-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DNS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, Gauge32, Bits, TimeTicks, Counter64, ObjectIdentity, Integer32, Counter32, Unsigned32, MibIdentifier, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Gauge32", "Bits", "TimeTicks", "Counter64", "ObjectIdentity", "Integer32", "Counter32", "Unsigned32", "MibIdentifier", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
juniDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47))
juniDnsMIB.setRevisions(('2006-09-15 08:32', '2003-09-11 15:50', '2002-09-16 21:44', '2001-03-22 19:29',))
if mibBuilder.loadTexts: juniDnsMIB.setLastUpdated('200609150832Z')
if mibBuilder.loadTexts: juniDnsMIB.setOrganization('Juniper Networks, Inc.')
class JuniNextServerListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ServerListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class JuniNextLocalDomainNameListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LocalDomainNameListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class LocalDomainName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '1025a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1025)

juniDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1))
juniDnsGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1))
juniDnsServerList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2))
juniDnsLocalDomainNameList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3))
juniDnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDnsEnable.setStatus('current')
juniDnsServerListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1), JuniNextServerListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDnsServerListNextIndex.setStatus('current')
juniDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2), )
if mibBuilder.loadTexts: juniDnsServerListTable.setStatus('current')
juniDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-DNS-MIB", "juniDnsServerListIndex"))
if mibBuilder.loadTexts: juniDnsServerListEntry.setStatus('current')
juniDnsServerListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1), ServerListIndex())
if mibBuilder.loadTexts: juniDnsServerListIndex.setStatus('current')
juniDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsServerListAddress.setStatus('obsolete')
juniDnsServerListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsServerListRowStatus.setStatus('current')
juniDnsV4V6ServerListAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddressType.setStatus('current')
juniDnsV4V6ServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddress.setStatus('current')
juniDnsLocalDomainNameListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1), JuniNextLocalDomainNameListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListNextIndex.setStatus('current')
juniDnsLocalDomainNameListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2), )
if mibBuilder.loadTexts: juniDnsLocalDomainNameListTable.setStatus('current')
juniDnsLocalDomainNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-DNS-MIB", "juniDnsLocalDomainNameListIndex"))
if mibBuilder.loadTexts: juniDnsLocalDomainNameListEntry.setStatus('current')
juniDnsLocalDomainNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1), LocalDomainNameListIndex())
if mibBuilder.loadTexts: juniDnsLocalDomainNameListIndex.setStatus('current')
juniDnsLocalDomainNameListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2), LocalDomainName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListName.setStatus('current')
juniDnsLocalDomainNameListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListRowStatus.setStatus('current')
juniDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2))
juniDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1))
juniDnsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2))
juniDnsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)).setObjects(("Juniper-DNS-MIB", "juniDnsEnableGroup"), ("Juniper-DNS-MIB", "juniDnsServerListGroup"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListGroup"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsCompliance = juniDnsCompliance.setStatus('current')
juniDnsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)).setObjects(("Juniper-DNS-MIB", "juniDnsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsEnableGroup = juniDnsEnableGroup.setStatus('current')
juniDnsServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)).setObjects(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"), ("Juniper-DNS-MIB", "juniDnsServerListAddress"), ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsServerListGroup = juniDnsServerListGroup.setStatus('obsolete')
juniDnsLocalDomainNameListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)).setObjects(("Juniper-DNS-MIB", "juniDnsLocalDomainNameListNextIndex"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListName"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsLocalDomainNameListGroup = juniDnsLocalDomainNameListGroup.setStatus('current')
juniDnsV4V6ServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 4)).setObjects(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"), ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddress"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsV4V6ServerListGroup = juniDnsV4V6ServerListGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-DNS-MIB", juniDnsServerList=juniDnsServerList, PYSNMP_MODULE_ID=juniDnsMIB, juniDnsLocalDomainNameListRowStatus=juniDnsLocalDomainNameListRowStatus, juniDnsLocalDomainNameListName=juniDnsLocalDomainNameListName, juniDnsLocalDomainNameListNextIndex=juniDnsLocalDomainNameListNextIndex, juniDnsConformance=juniDnsConformance, juniDnsMIB=juniDnsMIB, juniDnsServerListNextIndex=juniDnsServerListNextIndex, JuniNextServerListIndex=JuniNextServerListIndex, juniDnsServerListIndex=juniDnsServerListIndex, juniDnsEnableGroup=juniDnsEnableGroup, juniDnsServerListAddress=juniDnsServerListAddress, LocalDomainName=LocalDomainName, juniDnsServerListGroup=juniDnsServerListGroup, JuniNextLocalDomainNameListIndex=JuniNextLocalDomainNameListIndex, LocalDomainNameListIndex=LocalDomainNameListIndex, juniDnsLocalDomainNameListGroup=juniDnsLocalDomainNameListGroup, juniDnsEnable=juniDnsEnable, juniDnsV4V6ServerListAddress=juniDnsV4V6ServerListAddress, juniDnsServerListTable=juniDnsServerListTable, juniDnsLocalDomainNameListEntry=juniDnsLocalDomainNameListEntry, juniDnsGroups=juniDnsGroups, juniDnsV4V6ServerListGroup=juniDnsV4V6ServerListGroup, juniDnsCompliances=juniDnsCompliances, juniDnsCompliance=juniDnsCompliance, juniDnsServerListEntry=juniDnsServerListEntry, juniDnsLocalDomainNameListTable=juniDnsLocalDomainNameListTable, juniDnsGeneral=juniDnsGeneral, juniDnsV4V6ServerListAddressType=juniDnsV4V6ServerListAddressType, juniDnsObjects=juniDnsObjects, juniDnsLocalDomainNameList=juniDnsLocalDomainNameList, ServerListIndex=ServerListIndex, juniDnsLocalDomainNameListIndex=juniDnsLocalDomainNameListIndex, juniDnsServerListRowStatus=juniDnsServerListRowStatus)
