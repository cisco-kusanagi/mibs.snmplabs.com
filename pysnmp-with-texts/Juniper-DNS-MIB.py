#
# PySNMP MIB module Juniper-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:02:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, iso, Counter64, ModuleIdentity, IpAddress, ObjectIdentity, Gauge32, TimeTicks, Integer32, Unsigned32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "iso", "Counter64", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Gauge32", "TimeTicks", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
juniDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47))
juniDnsMIB.setRevisions(('2006-09-15 08:32', '2003-09-11 15:50', '2002-09-16 21:44', '2001-03-22 19:29',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDnsMIB.setRevisionsDescriptions(('Changed the maximum size of octet string for the object juniDnsLocalDomainNameListName from 32 to 1025.', 'Added IPv6 address support.', 'Replaced Unisphere names with Juniper names.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniDnsMIB.setLastUpdated('200609150832Z')
if mibBuilder.loadTexts: juniDnsMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDnsMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniDnsMIB.setDescription('The DNS MIB for the Juniper Networks, Inc. enterprise.')
class JuniNextServerListIndex(TextualConvention, Integer32):
    description = 'Coordinate index value allocation for entries in an associated table, by first reading an index value from this object, then creating an entry, having that index value, in the associated table. The DESCRIPTION clause for an object of this type must identify the associated table. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an object of this type is read-only, and a SET of such an object returns a notWritable error.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ServerListIndex(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each DNS server in the managed system.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class JuniNextLocalDomainNameListIndex(TextualConvention, Integer32):
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
    displayHint = '1025a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1025)

juniDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1))
juniDnsGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1))
juniDnsServerList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2))
juniDnsLocalDomainNameList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3))
juniDnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDnsEnable.setStatus('current')
if mibBuilder.loadTexts: juniDnsEnable.setDescription('Exerts administrative control to enable/disable DNS capability.')
juniDnsServerListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1), JuniNextServerListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDnsServerListNextIndex.setStatus('current')
if mibBuilder.loadTexts: juniDnsServerListNextIndex.setDescription('Coordinate juniDnsServerListIndex value allocation for entries in juniDnsServerListTable. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
juniDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2), )
if mibBuilder.loadTexts: juniDnsServerListTable.setStatus('current')
if mibBuilder.loadTexts: juniDnsServerListTable.setDescription('This table contains an entry for each DNS server.')
juniDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-DNS-MIB", "juniDnsServerListIndex"))
if mibBuilder.loadTexts: juniDnsServerListEntry.setStatus('current')
if mibBuilder.loadTexts: juniDnsServerListEntry.setDescription('Each entry corresponds to an associated DNS server.')
juniDnsServerListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1), ServerListIndex())
if mibBuilder.loadTexts: juniDnsServerListIndex.setStatus('current')
if mibBuilder.loadTexts: juniDnsServerListIndex.setDescription('The index of the DNS server. When creating entries in this table, suitable values for this object are determined by reading juniDnsServerListNextIndex.')
juniDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsServerListAddress.setStatus('obsolete')
if mibBuilder.loadTexts: juniDnsServerListAddress.setDescription('The IP address of the DNS server. This object has been replaced by juniDnsV4V6ServerListAddressType and juniDnsV4V6ServerListAddress.')
juniDnsServerListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsServerListRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniDnsServerListRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy')
juniDnsV4V6ServerListAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddressType.setStatus('current')
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddressType.setDescription('The type of IP address (IPv4 or IPv6) of the DNS server.')
juniDnsV4V6ServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddress.setStatus('current')
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddress.setDescription("The IP address of the DNS server. Note: Since this object is used to configure the IPv4 or IPv6 address depending on juniDnsV4V6ServerListAddressType value, it is mandatory to provide the IPv4 or IPv6 address by specifying each octet's positional values explicitly. Example: 1. IPv4 -- 4 octets -- 0xFF 0xFF 0xFF 0xFF 2. IPv6 -- 16 octets -- 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF 0xFF ")
juniDnsLocalDomainNameListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1), JuniNextLocalDomainNameListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListNextIndex.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListNextIndex.setDescription('Coordinate juniDnsLocalDomainNameListIndex value allocation for entries in juniDnsLocalDomainNameListTable. A GET of this object returns the next available index value to be used to create an entry in the associated table; or zero, if no valid index value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
juniDnsLocalDomainNameListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2), )
if mibBuilder.loadTexts: juniDnsLocalDomainNameListTable.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListTable.setDescription('This table contains an entry for each recognized local domain name.')
juniDnsLocalDomainNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-DNS-MIB", "juniDnsLocalDomainNameListIndex"))
if mibBuilder.loadTexts: juniDnsLocalDomainNameListEntry.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListEntry.setDescription('Each entry corresponds to a recognized local domain name.')
juniDnsLocalDomainNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1), LocalDomainNameListIndex())
if mibBuilder.loadTexts: juniDnsLocalDomainNameListIndex.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListIndex.setDescription('The index of the domain name. When creating entries in this table, suitable values for this object are determined by reading juniDnsLocalDomainNameListNextIndex.')
juniDnsLocalDomainNameListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2), LocalDomainName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListName.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListName.setDescription('A recognized local domain name.')
juniDnsLocalDomainNameListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy')
juniDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2))
juniDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1))
juniDnsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2))
juniDnsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)).setObjects(("Juniper-DNS-MIB", "juniDnsEnableGroup"), ("Juniper-DNS-MIB", "juniDnsServerListGroup"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListGroup"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsCompliance = juniDnsCompliance.setStatus('current')
if mibBuilder.loadTexts: juniDnsCompliance.setDescription('The compliance statement for entities which implement the Juniper DNS MIB.')
juniDnsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)).setObjects(("Juniper-DNS-MIB", "juniDnsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsEnableGroup = juniDnsEnableGroup.setStatus('current')
if mibBuilder.loadTexts: juniDnsEnableGroup.setDescription('A collection of objects for enabling/disabling DNS capabilities in a Juniper product.')
juniDnsServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)).setObjects(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"), ("Juniper-DNS-MIB", "juniDnsServerListAddress"), ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsServerListGroup = juniDnsServerListGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniDnsServerListGroup.setDescription('Obsolete collection of objects for managing DNS server list capabilities in a Juniper product. This group became obsolete when IPv2 address support was added.')
juniDnsLocalDomainNameListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)).setObjects(("Juniper-DNS-MIB", "juniDnsLocalDomainNameListNextIndex"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListName"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsLocalDomainNameListGroup = juniDnsLocalDomainNameListGroup.setStatus('current')
if mibBuilder.loadTexts: juniDnsLocalDomainNameListGroup.setDescription('A collection of objects for managing DNS local domain name list capabilities in a Juniper product.')
juniDnsV4V6ServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 4)).setObjects(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"), ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddress"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsV4V6ServerListGroup = juniDnsV4V6ServerListGroup.setStatus('current')
if mibBuilder.loadTexts: juniDnsV4V6ServerListGroup.setDescription('A collection of objects for managing DNS server list capabilities in a Juniper product.')
mibBuilder.exportSymbols("Juniper-DNS-MIB", juniDnsMIB=juniDnsMIB, juniDnsV4V6ServerListAddressType=juniDnsV4V6ServerListAddressType, juniDnsEnableGroup=juniDnsEnableGroup, JuniNextServerListIndex=JuniNextServerListIndex, juniDnsV4V6ServerListGroup=juniDnsV4V6ServerListGroup, JuniNextLocalDomainNameListIndex=JuniNextLocalDomainNameListIndex, juniDnsLocalDomainNameListNextIndex=juniDnsLocalDomainNameListNextIndex, juniDnsServerListTable=juniDnsServerListTable, juniDnsLocalDomainNameListGroup=juniDnsLocalDomainNameListGroup, LocalDomainName=LocalDomainName, juniDnsLocalDomainNameListName=juniDnsLocalDomainNameListName, juniDnsCompliance=juniDnsCompliance, juniDnsServerListIndex=juniDnsServerListIndex, juniDnsLocalDomainNameListEntry=juniDnsLocalDomainNameListEntry, juniDnsServerList=juniDnsServerList, juniDnsServerListAddress=juniDnsServerListAddress, ServerListIndex=ServerListIndex, PYSNMP_MODULE_ID=juniDnsMIB, juniDnsCompliances=juniDnsCompliances, juniDnsObjects=juniDnsObjects, juniDnsGeneral=juniDnsGeneral, juniDnsGroups=juniDnsGroups, juniDnsLocalDomainNameListTable=juniDnsLocalDomainNameListTable, juniDnsServerListGroup=juniDnsServerListGroup, juniDnsLocalDomainNameListIndex=juniDnsLocalDomainNameListIndex, LocalDomainNameListIndex=LocalDomainNameListIndex, juniDnsServerListRowStatus=juniDnsServerListRowStatus, juniDnsServerListEntry=juniDnsServerListEntry, juniDnsServerListNextIndex=juniDnsServerListNextIndex, juniDnsEnable=juniDnsEnable, juniDnsLocalDomainNameList=juniDnsLocalDomainNameList, juniDnsConformance=juniDnsConformance, juniDnsV4V6ServerListAddress=juniDnsV4V6ServerListAddress, juniDnsLocalDomainNameListRowStatus=juniDnsLocalDomainNameListRowStatus)
