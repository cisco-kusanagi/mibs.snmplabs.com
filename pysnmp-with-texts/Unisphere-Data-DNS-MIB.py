#
# PySNMP MIB module Unisphere-Data-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:30:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity, Unsigned32, MibIdentifier, Integer32, Counter64, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "Gauge32", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47))
usdDnsMIB.setRevisions(('2001-03-22 19:29',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdDnsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdDnsMIB.setLastUpdated('200103221929Z')
if mibBuilder.loadTexts: usdDnsMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdDnsMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdDnsMIB.setDescription('The DNS MIB for the Unisphere Networks, Inc. enterprise.')
class UsdNextServerListIndex(TextualConvention, Integer32):
    description = 'Coordinate index value allocation for entries in an associated table, by first reading an index value from this object, then creating an entry, having that index value, in the associated table. The DESCRIPTION clause for an object of this type must identify the associated table. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an object of this type is read-only, and a SET of such an object returns a notWritable error.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ServerListIndex(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each DNS server in the managed system.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class UsdNextLocalDomainNameListIndex(TextualConvention, Integer32):
    description = 'Coordinate index value allocation for entries in an associated table, by first reading an index value from this object, then creating an entry, having that index value, in the associated table. The DESCRIPTION clause for an object of this type must identify the associated table. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an object of this type is read-only, and a SET of such an object returns a notWritable error.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LocalDomainNameListIndex(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each recognized domain name in the managed system.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class LocalDomainName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    description = 'Local domain name. Represents textual information taken from the NVT ASCII character set.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

usdDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1))
usdDnsGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1))
usdDnsServerList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2))
usdDnsLocalDomainNameList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3))
usdDnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdDnsEnable.setStatus('current')
if mibBuilder.loadTexts: usdDnsEnable.setDescription('Exerts administrative control to enable/disable DNS capability.')
usdDnsServerListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1), UsdNextServerListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDnsServerListNextIndex.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListNextIndex.setDescription('Coordinate usdDnsServerListIndex value allocation for entries in usdDnsServerListTable. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
usdDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2), )
if mibBuilder.loadTexts: usdDnsServerListTable.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListTable.setDescription('This table contains an entry for each DNS server.')
usdDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-DNS-MIB", "usdDnsServerListIndex"))
if mibBuilder.loadTexts: usdDnsServerListEntry.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListEntry.setDescription('Each entry corresponds to an associated DNS server.')
usdDnsServerListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1), ServerListIndex())
if mibBuilder.loadTexts: usdDnsServerListIndex.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListIndex.setDescription('The index of the DNS server. When creating entries in this table, suitable values for this object are determined by reading usdDnsServerListNextIndex.')
usdDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsServerListAddress.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListAddress.setDescription('The IP address of the DNS server.')
usdDnsServerListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsServerListRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy')
usdDnsLocalDomainNameListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1), UsdNextLocalDomainNameListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDnsLocalDomainNameListNextIndex.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListNextIndex.setDescription('Coordinate usdDnsLocalDomainNameListIndex value allocation for entries in usdDnsLocalDomainNameListTable. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
usdDnsLocalDomainNameListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2), )
if mibBuilder.loadTexts: usdDnsLocalDomainNameListTable.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListTable.setDescription('This table contains an entry for each recognized local domain name.')
usdDnsLocalDomainNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1), ).setIndexNames((0, "Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListIndex"))
if mibBuilder.loadTexts: usdDnsLocalDomainNameListEntry.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListEntry.setDescription('Each entry corresponds to a recognized local domain name.')
usdDnsLocalDomainNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1), LocalDomainNameListIndex())
if mibBuilder.loadTexts: usdDnsLocalDomainNameListIndex.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListIndex.setDescription('The index of the domain name. When creating entries in this table, suitable values for this object are determined by reading usdDnsLocalDomainNameListNextIndex.')
usdDnsLocalDomainNameListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2), LocalDomainName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsLocalDomainNameListName.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListName.setDescription('A recognized local domain name.')
usdDnsLocalDomainNameListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDnsLocalDomainNameListRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy')
usdDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2))
usdDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1))
usdDnsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2))
usdDnsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsEnableGroup"), ("Unisphere-Data-DNS-MIB", "usdDnsServerListGroup"), ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsCompliance = usdDnsCompliance.setStatus('current')
if mibBuilder.loadTexts: usdDnsCompliance.setDescription('The compliance statement for entities which implement the Unisphere DNS MIB.')
usdDnsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsEnableGroup = usdDnsEnableGroup.setStatus('current')
if mibBuilder.loadTexts: usdDnsEnableGroup.setDescription('A collection of objects for enabling/disabling DNS capabilities in a Unisphere product.')
usdDnsServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsServerListNextIndex"), ("Unisphere-Data-DNS-MIB", "usdDnsServerListAddress"), ("Unisphere-Data-DNS-MIB", "usdDnsServerListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsServerListGroup = usdDnsServerListGroup.setStatus('current')
if mibBuilder.loadTexts: usdDnsServerListGroup.setDescription('A collection of objects for managing DNS server list capabilities in a Unisphere product.')
usdDnsLocalDomainNameListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)).setObjects(("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListNextIndex"), ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListName"), ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsLocalDomainNameListGroup = usdDnsLocalDomainNameListGroup.setStatus('current')
if mibBuilder.loadTexts: usdDnsLocalDomainNameListGroup.setDescription('A collection of objects for managing DNS local domain name list capabilities in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-DNS-MIB", usdDnsLocalDomainNameListEntry=usdDnsLocalDomainNameListEntry, usdDnsLocalDomainNameListName=usdDnsLocalDomainNameListName, usdDnsLocalDomainNameListIndex=usdDnsLocalDomainNameListIndex, usdDnsEnableGroup=usdDnsEnableGroup, ServerListIndex=ServerListIndex, usdDnsLocalDomainNameList=usdDnsLocalDomainNameList, LocalDomainNameListIndex=LocalDomainNameListIndex, usdDnsServerListRowStatus=usdDnsServerListRowStatus, UsdNextLocalDomainNameListIndex=UsdNextLocalDomainNameListIndex, usdDnsServerListIndex=usdDnsServerListIndex, usdDnsServerListEntry=usdDnsServerListEntry, usdDnsLocalDomainNameListRowStatus=usdDnsLocalDomainNameListRowStatus, usdDnsServerListTable=usdDnsServerListTable, usdDnsCompliance=usdDnsCompliance, LocalDomainName=LocalDomainName, usdDnsMIB=usdDnsMIB, usdDnsEnable=usdDnsEnable, usdDnsServerListNextIndex=usdDnsServerListNextIndex, usdDnsGeneral=usdDnsGeneral, usdDnsCompliances=usdDnsCompliances, usdDnsServerList=usdDnsServerList, PYSNMP_MODULE_ID=usdDnsMIB, usdDnsLocalDomainNameListTable=usdDnsLocalDomainNameListTable, usdDnsServerListAddress=usdDnsServerListAddress, UsdNextServerListIndex=UsdNextServerListIndex, usdDnsServerListGroup=usdDnsServerListGroup, usdDnsLocalDomainNameListNextIndex=usdDnsLocalDomainNameListNextIndex, usdDnsLocalDomainNameListGroup=usdDnsLocalDomainNameListGroup, usdDnsGroups=usdDnsGroups, usdDnsConformance=usdDnsConformance, usdDnsObjects=usdDnsObjects)
