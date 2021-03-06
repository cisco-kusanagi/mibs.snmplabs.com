#
# PySNMP MIB module Juniper-SMDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SMDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:04:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Integer32, ObjectIdentity, NotificationType, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, MibIdentifier, iso, IpAddress, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ObjectIdentity", "NotificationType", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "MibIdentifier", "iso", "IpAddress", "ModuleIdentity", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
juniSmdsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50))
juniSmdsMIB.setRevisions(('2002-09-16 21:44', '2001-09-20 14:41', '2001-03-08 20:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSmdsMIB.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added support for major and sub interfaces.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniSmdsMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniSmdsMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSmdsMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniSmdsMIB.setDescription('The Switched Multimegabit Data Service (SMDS) MIB for the Juniper Networks enterprise.')
juniSmdsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1))
juniSmdsNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in juniSmdsIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
juniSmdsIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2), )
if mibBuilder.loadTexts: juniSmdsIfTable.setStatus('current')
if mibBuilder.loadTexts: juniSmdsIfTable.setDescription('This table contains entries for SMDS interfaces present in the system.')
juniSmdsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1), ).setIndexNames((0, "Juniper-SMDS-MIB", "juniSmdsIfIndex"))
if mibBuilder.loadTexts: juniSmdsIfEntry.setStatus('current')
if mibBuilder.loadTexts: juniSmdsIfEntry.setDescription('Each entry describes the characteristics of an SMDS interface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/juniIfTable.')
juniSmdsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSmdsIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsIfIndex.setDescription('The ifIndex of the SMDS interface. When creating entries in this table, suitable values for this object are determined by reading juniSmdsNextIfIndex.')
juniSmdsIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniSmdsIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: juniSmdsIfRowStatus juniSmdsIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for juniSmdsIfIndex must have been determined previously, by reading juniSmdsNextIfIndex. The interface identified by juniSmdsIfLowerIfIndex must exist. A corresponding entry in ifTable/ifXTable/juniIfTable is created/ destroyed as a result of creating/destroying an entry in this table. ')
juniSmdsIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsIfLowerIfIndex.setDescription('The ifIndex of an interface over which this SMDS interface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
juniSmdsMajorNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 3), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsMajorNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in juniSmdsMajorIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. ')
juniSmdsMajorIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4), )
if mibBuilder.loadTexts: juniSmdsMajorIfTable.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfTable.setDescription('This table contains entries for SMDS major interfaces present in the system.')
juniSmdsMajorIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1), ).setIndexNames((0, "Juniper-SMDS-MIB", "juniSmdsMajorIfIndex"))
if mibBuilder.loadTexts: juniSmdsMajorIfEntry.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfEntry.setDescription('Each entry describes the characteristics of an SMDS major interface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/juniIfTable.')
juniSmdsMajorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSmdsMajorIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfIndex.setDescription('The ifIndex of the SMDS major interface. When creating entries in this table, suitable values for this object are determined by reading juniSmdsMajorNextIfIndex.')
juniSmdsMajorIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsMajorIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: juniSmdsMajorIfRowStatus juniSmdsMajorIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for juniSmdsMajorIfIndex must have been determined previously, by reading juniSmdsMajorNextIfIndex. The interface identified by juniSmdsMajorIfLowerIfIndex must exist. A corresponding entry in ifTable/ifXTable/juniIfTable is created/ destroyed as a result of creating/destroying an entry in this table.')
juniSmdsMajorIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsMajorIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfLowerIfIndex.setDescription('The ifIndex of an interface over which this SMDS major interface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
juniSmdsMajorIfKeepalive = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 32767), ))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsMajorIfKeepalive.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfKeepalive.setDescription('Keepalive interval in seconds. A value of zero disables keepalive.')
juniSmdsSubNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 5), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsSubNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in juniSmdsSubIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
juniSmdsSubIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6), )
if mibBuilder.loadTexts: juniSmdsSubIfTable.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfTable.setDescription('This table contains entries for SMDS subinterfaces present in the system.')
juniSmdsSubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1), ).setIndexNames((0, "Juniper-SMDS-MIB", "juniSmdsSubIfIndex"))
if mibBuilder.loadTexts: juniSmdsSubIfEntry.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfEntry.setDescription('Each entry describes the characteristics of an SMDS subinterface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/juniIfTable.')
juniSmdsSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSmdsSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfIndex.setDescription('The ifIndex of the SMDS subinterface. When creating entries in this table, suitable values for this object are determined by reading juniSmdsSubNextIfIndex.')
juniSmdsSubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsSubIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: juniSmdsSubIfRowStatus juniSmdsSubIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for juniSmdsSubIfIndex must have been determined previously, by reading juniSmdsSubNextIfIndex. The interface identified by juniSmdsSubIfLowerIfIndex must exist. A corresponding entry in ifTable/ifXTable/juniIfTable is created/ destroyed as a result of creating/destroying an entry in this table. ')
juniSmdsSubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsSubIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfLowerIfIndex.setDescription('The ifIndex of an interface over which this SMDS subinterface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
juniSmdsSubIfSmdsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsSubIfSmdsAddress.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfSmdsAddress.setDescription('The 64 bit E.164 SMDS address that has been assigned to this SMDS subinterface. A value of 0 indicates no address is configured.')
juniSmdsSubIfSmdsMulticastIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsSubIfSmdsMulticastIpAddress.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfSmdsMulticastIpAddress.setDescription('The 64 bit E.164 SMDS ip multicast address that has been assigned to this SMDS subinterface. A value of 0 indicates no address is configured.')
juniSmdsSubIfSmdsMulticastArpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 6, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniSmdsSubIfSmdsMulticastArpAddress.setStatus('current')
if mibBuilder.loadTexts: juniSmdsSubIfSmdsMulticastArpAddress.setDescription('The 64 bit E.164 SMDS multicast arp address that has been assigned to this SMDS subinterface. A value of 0 indicates no address is configured.')
juniSmdsMajorIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7), )
if mibBuilder.loadTexts: juniSmdsMajorIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsTable.setDescription('This table contains entries for SMDS major interface statistics present in the system.')
juniSmdsMajorIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1), )
juniSmdsMajorIfEntry.registerAugmentions(("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsEntry"))
juniSmdsMajorIfStatsEntry.setIndexNames(*juniSmdsMajorIfEntry.getIndexNames())
if mibBuilder.loadTexts: juniSmdsMajorIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsEntry.setDescription('Each entry describes the statistics of an SMDS major interface.')
juniSmdsMajorIfStatsInKeepaliveRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsMajorIfStatsInKeepaliveRequests.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsInKeepaliveRequests.setDescription('The number of keepalive requests received.')
juniSmdsMajorIfStatsOutKeepaliveRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsMajorIfStatsOutKeepaliveRequests.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsOutKeepaliveRequests.setDescription('The number of keepalive requests transmitted.')
juniSmdsMajorIfStatsInKeepaliveReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsMajorIfStatsInKeepaliveReplies.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsInKeepaliveReplies.setDescription('The number of keepalive replies received.')
juniSmdsMajorIfStatsOutKeepaliveReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsMajorIfStatsOutKeepaliveReplies.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsOutKeepaliveReplies.setDescription('The number of keepalive replies transmitted.')
juniSmdsMajorIfStatsKeepaliveFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniSmdsMajorIfStatsKeepaliveFailures.setStatus('current')
if mibBuilder.loadTexts: juniSmdsMajorIfStatsKeepaliveFailures.setDescription('The number of keepalive failures detected.')
juniSmdsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4))
juniSmdsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1))
juniSmdsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2))
juniSmdsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1, 1)).setObjects(("Juniper-SMDS-MIB", "juniSmdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsCompliance = juniSmdsCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniSmdsCompliance.setDescription('Obsolete compliance statement for entities which implement the Juniper SMDS MIB. This statement became obsolete when support was added for major and sub interfaces.')
juniSmdsCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 1, 2)).setObjects(("Juniper-SMDS-MIB", "juniSmdsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsCompliance2 = juniSmdsCompliance2.setStatus('current')
if mibBuilder.loadTexts: juniSmdsCompliance2.setDescription('The compliance statement for entities which implement the Juniper SMDS MIB.')
juniSmdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2, 1)).setObjects(("Juniper-SMDS-MIB", "juniSmdsNextIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsIfRowStatus"), ("Juniper-SMDS-MIB", "juniSmdsIfLowerIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsGroup = juniSmdsGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniSmdsGroup.setDescription('Obsolete collection of objects providing management of SMDS interfaces in a Juniper product. This group became obsolete when support was added for major and sub interfaces.')
juniSmdsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 50, 4, 2, 2)).setObjects(("Juniper-SMDS-MIB", "juniSmdsNextIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsIfRowStatus"), ("Juniper-SMDS-MIB", "juniSmdsIfLowerIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsMajorNextIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfRowStatus"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfLowerIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfKeepalive"), ("Juniper-SMDS-MIB", "juniSmdsSubNextIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsSubIfRowStatus"), ("Juniper-SMDS-MIB", "juniSmdsSubIfLowerIfIndex"), ("Juniper-SMDS-MIB", "juniSmdsSubIfSmdsAddress"), ("Juniper-SMDS-MIB", "juniSmdsSubIfSmdsMulticastIpAddress"), ("Juniper-SMDS-MIB", "juniSmdsSubIfSmdsMulticastArpAddress"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsInKeepaliveRequests"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsOutKeepaliveRequests"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsInKeepaliveReplies"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsOutKeepaliveReplies"), ("Juniper-SMDS-MIB", "juniSmdsMajorIfStatsKeepaliveFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsGroup2 = juniSmdsGroup2.setStatus('current')
if mibBuilder.loadTexts: juniSmdsGroup2.setDescription('A collection of objects providing management of SMDS interfaces in a Juniper product.')
mibBuilder.exportSymbols("Juniper-SMDS-MIB", juniSmdsMajorIfStatsEntry=juniSmdsMajorIfStatsEntry, juniSmdsSubIfEntry=juniSmdsSubIfEntry, juniSmdsCompliance2=juniSmdsCompliance2, juniSmdsSubIfSmdsMulticastArpAddress=juniSmdsSubIfSmdsMulticastArpAddress, juniSmdsMajorIfStatsOutKeepaliveReplies=juniSmdsMajorIfStatsOutKeepaliveReplies, juniSmdsSubIfIndex=juniSmdsSubIfIndex, juniSmdsMajorIfRowStatus=juniSmdsMajorIfRowStatus, juniSmdsSubNextIfIndex=juniSmdsSubNextIfIndex, juniSmdsSubIfSmdsMulticastIpAddress=juniSmdsSubIfSmdsMulticastIpAddress, juniSmdsSubIfRowStatus=juniSmdsSubIfRowStatus, juniSmdsIfLowerIfIndex=juniSmdsIfLowerIfIndex, juniSmdsMIB=juniSmdsMIB, juniSmdsMajorIfKeepalive=juniSmdsMajorIfKeepalive, juniSmdsMajorIfEntry=juniSmdsMajorIfEntry, juniSmdsMajorIfStatsKeepaliveFailures=juniSmdsMajorIfStatsKeepaliveFailures, juniSmdsMajorIfLowerIfIndex=juniSmdsMajorIfLowerIfIndex, PYSNMP_MODULE_ID=juniSmdsMIB, juniSmdsSubIfSmdsAddress=juniSmdsSubIfSmdsAddress, juniSmdsMajorIfTable=juniSmdsMajorIfTable, juniSmdsMajorIfStatsOutKeepaliveRequests=juniSmdsMajorIfStatsOutKeepaliveRequests, juniSmdsIfTable=juniSmdsIfTable, juniSmdsMajorNextIfIndex=juniSmdsMajorNextIfIndex, juniSmdsCompliance=juniSmdsCompliance, juniSmdsNextIfIndex=juniSmdsNextIfIndex, juniSmdsMajorIfIndex=juniSmdsMajorIfIndex, juniSmdsSubIfLowerIfIndex=juniSmdsSubIfLowerIfIndex, juniSmdsCompliances=juniSmdsCompliances, juniSmdsMajorIfStatsInKeepaliveReplies=juniSmdsMajorIfStatsInKeepaliveReplies, juniSmdsGroups=juniSmdsGroups, juniSmdsIfEntry=juniSmdsIfEntry, juniSmdsMajorIfStatsTable=juniSmdsMajorIfStatsTable, juniSmdsMajorIfStatsInKeepaliveRequests=juniSmdsMajorIfStatsInKeepaliveRequests, juniSmdsIfIndex=juniSmdsIfIndex, juniSmdsGroup=juniSmdsGroup, juniSmdsSubIfTable=juniSmdsSubIfTable, juniSmdsObjects=juniSmdsObjects, juniSmdsIfRowStatus=juniSmdsIfRowStatus, juniSmdsGroup2=juniSmdsGroup2, juniSmdsConformance=juniSmdsConformance)
