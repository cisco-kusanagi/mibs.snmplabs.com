#
# PySNMP MIB module Unisphere-Data-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DNS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, iso, Gauge32, MibIdentifier, Bits, IpAddress, Counter32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "iso", "Gauge32", "MibIdentifier", "Bits", "IpAddress", "Counter32", "NotificationType", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47))
usdDnsMIB.setRevisions(('2001-03-22 19:29',))
if mibBuilder.loadTexts: usdDnsMIB.setLastUpdated('200103221929Z')
if mibBuilder.loadTexts: usdDnsMIB.setOrganization('Unisphere Networks, Inc.')
class UsdNextServerListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ServerListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class UsdNextLocalDomainNameListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LocalDomainNameListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class LocalDomainName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

usdDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1))
usdDnsGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1))
usdDnsServerList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2))
usdDnsLocalDomainNameList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3))
usdDnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdDnsEnable.setStatus('current')
usdDnsServerListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1), UsdNextServerListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDnsServerListNextIndex.setStatus('current')
usdDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2), )
if mibBuilder.loadTexts: usdDnsServerListTable.setStatus('current')
usdDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-DNS-MIB", "usdDnsServerListIndex"))
if mibBuilder.loadTexts: usdDnsServerListEntry.setStatus('current')
usdDnsServerListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1), ServerListIndex())
if mibBuilder.loadTexts: usdDnsServerListIndex.setStatus('current')
usdDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsServerListAddress.setStatus('current')
usdDnsServerListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsServerListRowStatus.setStatus('current')
usdDnsLocalDomainNameListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1), UsdNextLocalDomainNameListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDnsLocalDomainNameListNextIndex.setStatus('current')
usdDnsLocalDomainNameListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2), )
if mibBuilder.loadTexts: usdDnsLocalDomainNameListTable.setStatus('current')
usdDnsLocalDomainNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1), ).setIndexNames((0, "Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListIndex"))
if mibBuilder.loadTexts: usdDnsLocalDomainNameListEntry.setStatus('current')
usdDnsLocalDomainNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1), LocalDomainNameListIndex())
if mibBuilder.loadTexts: usdDnsLocalDomainNameListIndex.setStatus('current')
usdDnsLocalDomainNameListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2), LocalDomainName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsLocalDomainNameListName.setStatus('current')
usdDnsLocalDomainNameListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsLocalDomainNameListRowStatus.setStatus('current')
usdDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2))
usdDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1))
usdDnsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2))
usdDnsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsEnableGroup"), ("Unisphere-Data-DNS-MIB", "usdDnsServerListGroup"), ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsCompliance = usdDnsCompliance.setStatus('current')
usdDnsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsEnableGroup = usdDnsEnableGroup.setStatus('current')
usdDnsServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsServerListNextIndex"), ("Unisphere-Data-DNS-MIB", "usdDnsServerListAddress"), ("Unisphere-Data-DNS-MIB", "usdDnsServerListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsServerListGroup = usdDnsServerListGroup.setStatus('current')
usdDnsLocalDomainNameListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListNextIndex"), ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListName"), ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsLocalDomainNameListGroup = usdDnsLocalDomainNameListGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-DNS-MIB", LocalDomainNameListIndex=LocalDomainNameListIndex, usdDnsGroups=usdDnsGroups, usdDnsServerListGroup=usdDnsServerListGroup, usdDnsLocalDomainNameListGroup=usdDnsLocalDomainNameListGroup, UsdNextLocalDomainNameListIndex=UsdNextLocalDomainNameListIndex, LocalDomainName=LocalDomainName, usdDnsServerListNextIndex=usdDnsServerListNextIndex, usdDnsLocalDomainNameListEntry=usdDnsLocalDomainNameListEntry, usdDnsLocalDomainNameList=usdDnsLocalDomainNameList, usdDnsLocalDomainNameListTable=usdDnsLocalDomainNameListTable, usdDnsServerList=usdDnsServerList, usdDnsServerListEntry=usdDnsServerListEntry, usdDnsLocalDomainNameListRowStatus=usdDnsLocalDomainNameListRowStatus, usdDnsServerListTable=usdDnsServerListTable, usdDnsEnable=usdDnsEnable, PYSNMP_MODULE_ID=usdDnsMIB, usdDnsLocalDomainNameListName=usdDnsLocalDomainNameListName, usdDnsCompliance=usdDnsCompliance, usdDnsServerListIndex=usdDnsServerListIndex, usdDnsGeneral=usdDnsGeneral, usdDnsCompliances=usdDnsCompliances, usdDnsLocalDomainNameListNextIndex=usdDnsLocalDomainNameListNextIndex, usdDnsServerListAddress=usdDnsServerListAddress, usdDnsEnableGroup=usdDnsEnableGroup, usdDnsConformance=usdDnsConformance, usdDnsLocalDomainNameListIndex=usdDnsLocalDomainNameListIndex, usdDnsMIB=usdDnsMIB, usdDnsObjects=usdDnsObjects, UsdNextServerListIndex=UsdNextServerListIndex, ServerListIndex=ServerListIndex, usdDnsServerListRowStatus=usdDnsServerListRowStatus)
