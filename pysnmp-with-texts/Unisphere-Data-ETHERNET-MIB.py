#
# PySNMP MIB module Unisphere-Data-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:31:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Unsigned32, Counter32, NotificationType, ModuleIdentity, iso, MibIdentifier, Integer32, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Unsigned32", "Counter32", "NotificationType", "ModuleIdentity", "iso", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity", "TimeTicks")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex")
usdEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34))
usdEthernetMIB.setRevisions(('2002-04-05 19:47', '2001-01-02 16:55', '2000-04-18 00:00', '2000-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdEthernetMIB.setRevisionsDescriptions(('Added VLAN stack support.', 'Added VLAN management support.', 'Added objects for Ethernet sub-interface creation. Added usdEthernetIfOperDuplexMode to report current duplex mode. Revised descriptions to note relationship to ifTable objects and to explain autonegotiation dependencies. Added speed1000Mbps enumeration value to usdEthernetIfSpeed. Changed lower bound of usdEthernetIfMtu from 18 to 64.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdEthernetMIB.setLastUpdated('200204051947Z')
if mibBuilder.loadTexts: usdEthernetMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdEthernetMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdEthernetMIB.setDescription('The Ethernet MIB for the Unisphere Networks enterprise.')
usdEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1))
usdEthernetIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1))
usdEthernetSubIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2))
usdVlanMajorIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3))
usdVlanSubIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4))
usdEthernetIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: usdEthernetIfTable.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfTable.setDescription('The parameters for the Ethernet interface.')
usdEthernetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-ETHERNET-MIB", "usdEthernetIfIndex"))
if mibBuilder.loadTexts: usdEthernetIfEntry.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfEntry.setDescription('The Parameters for a particular Ethernet interface. Entries in this table correspond with entries in the ifTable/ifXTable/usdIfTable.')
usdEthernetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdEthernetIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfIndex.setDescription('The ifIndex value of the corresponding ethernet interface.')
usdEthernetIfDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoDuplex", 1), ("halfDuplex", 2), ("fullDuplex", 3))).clone('autoDuplex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdEthernetIfDuplexMode.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfDuplexMode.setDescription("The configured duplex setting for this ethernet interface. The operational value is reported in this table entry's corresponding usdEthernetIfOperDuplexMode object. NOTE, configuration dependency: Setting this object to values other than 'autoDuplex' takes effect only when the corresponding usdEthernetIfSpeed object is simultaneously set to other than 'autoNegotiate'. Otherwise (i.e. this object is set to 'autoDuplex', AND/OR corresponding usdEthernetIfSpeed object is set to 'autoNegotiate'), duplex mode is negotiated.")
usdEthernetIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("autoNegotiate", 1), ("speed10Mbps", 2), ("speed100Mbps", 3), ("speed1000Mbps", 4))).clone('autoNegotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdEthernetIfSpeed.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfSpeed.setDescription("The configured speed setting for this ethernet interface. The operational value is reported in the corresponding Interfaces MIB ifSpeed object. NOTE, configuration dependency: Setting this object to values other than 'autoNegotiate' takes effect only when the corresponding usdEthernetIfDuplexMode object is simultaneously set to other than 'autoDuplex'. Otherwise (i.e. this object is set to 'autoNegotiate', AND/OR the corresponding usdEthernetIfDuplexMode object is set to 'autoDuplex'), speed is negotiated.")
usdEthernetIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9188)).clone(1518)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdEthernetIfMtu.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfMtu.setDescription('The configured maximum transfer unit (MTU) for this ethernet interface. The operational value is reported in the corresponding Interfaces MIB ifMtu object.')
usdEthernetIfOperDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoDuplex", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdEthernetIfOperDuplexMode.setStatus('current')
if mibBuilder.loadTexts: usdEthernetIfOperDuplexMode.setDescription('The current operational duplex mode for this ethernet interface.')
usdEthernetSubIfNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdEthernetSubIfNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in usdEthernetSubIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
usdEthernetSubIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2), )
if mibBuilder.loadTexts: usdEthernetSubIfTable.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfTable.setDescription('This table contains entries for Ethernet Subinterfaces present in the system.')
usdEthernetSubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfIndex"))
if mibBuilder.loadTexts: usdEthernetSubIfEntry.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfEntry.setDescription('Each entry describes the characteristics of an Ethernet Subinterface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/usdIfTable.')
usdEthernetSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdEthernetSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfIndex.setDescription('The ifIndex of the Ethernet Subinterface. When creating entries in this table, suitable values for this object are determined by reading usdEthernetSubNextIfIndex.')
usdEthernetSubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdEthernetSubIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: usdEthernetSubIfRowStatus usdEthernetSubIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for usdEthernetSubIfIndex must have been determined previously, by reading usdEthernetSubIfNextIfIndex. The interface identified by usdEthernetSubIfLowerIfIndex must exist, and must be a Ethernet interface. A positive value configured for usdEthernetSubIfId must not already be assigned to another subinterface layered onto the same underlying Ethernet interface. A corresponding entry in ifTable/ifXTable/usdIfTable is created/destroyed as a result of creating/destroying an entry in this table.')
usdEthernetSubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdEthernetSubIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfLowerIfIndex.setDescription('The ifIndex of a Ethernet interface over which this Ethernet Subinterface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
usdEthernetSubIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdEthernetSubIfId.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfId.setDescription('An integer identifier for the Ethernet subinterface, used in conjunction with the command-line interface. It is provided here for cross-reference purposes only. The value must be unique among subinterfaces configured on the same underlying Ethernet interface. If this object is not configured, or is configured with a value of -1, a nonzero value will be allocated internally and can be retrieved from this object after table entry creation has succeeded. A value of zero for this object is reserved for future use.')
usdVlanMajorNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdVlanMajorNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdVlanMajorNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in usdVlanMajorIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. ')
usdVlanMajorIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2), )
if mibBuilder.loadTexts: usdVlanMajorIfTable.setStatus('current')
if mibBuilder.loadTexts: usdVlanMajorIfTable.setDescription('This table contains entries for major VLAN interfaces present in the system.')
usdVlanMajorIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1), ).setIndexNames((0, "Unisphere-Data-ETHERNET-MIB", "usdVlanMajorIfIndex"))
if mibBuilder.loadTexts: usdVlanMajorIfEntry.setStatus('current')
if mibBuilder.loadTexts: usdVlanMajorIfEntry.setDescription('Each entry describes the characteristics of a major VLAN interface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/usdIfTable.')
usdVlanMajorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdVlanMajorIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdVlanMajorIfIndex.setDescription('The ifIndex of the major VLAN interface. When creating entries in this table, suitable values for this object are determined by reading usdVlanMajorNextIfIndex.')
usdVlanMajorIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanMajorIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdVlanMajorIfLowerIfIndex.setDescription('The ifIndex of the interface over which this major VLAN interface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
usdVlanMajorIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanMajorIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdVlanMajorIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create or delete an entry in this table, the following entry objects MUST be explicitly configured: usdVlanMajorIfRowStatus usdVlanMajorIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for usdVlanMajorIfIndex must have been determined previously by reading usdVlanMajorIfNextIfIndex. The interface identified by usdVlanMajorIfLowerIfIndex must exist. A corresponding entry in ifTable/ifXTable/usdIfTable is created/destroyed as a result of creating/destroying an entry in this table.')
usdVlanSubNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdVlanSubNextIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubNextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in usdVlanSubIfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously.')
usdVlanSubIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2), )
if mibBuilder.loadTexts: usdVlanSubIfTable.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfTable.setDescription('This table contains entries for VLAN Subinterfaces present in the system.')
usdVlanSubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1), ).setIndexNames((0, "Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfIndex"))
if mibBuilder.loadTexts: usdVlanSubIfEntry.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfEntry.setDescription('Each entry describes the characteristics of a VLAN Subinterface. Creating/deleting entries in this table causes corresponding entries for be created/deleted in ifTable/ifXTable/usdIfTable.')
usdVlanSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdVlanSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfIndex.setDescription('The ifIndex of the VLAN Subinterface. When creating entries in this table, suitable values for this object are determined by reading usdVlanSubNextIfIndex.')
usdVlanSubIfVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanSubIfVlanId.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfVlanId.setDescription('An integer identifier or tag ID for this VLAN A value of zero indicates the default VLAN. When VLANs are enabled, the value must be unique among subinterfaces configured on the same underlying major VLAN interface. If the VLAN ID is non-zero, then the usdVlanSubIfVlanUntagged field must be disabled. Cannot be changed if the subinterface has upper bindings.')
usdVlanSubIfVlanUntagged = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanSubIfVlanUntagged.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfVlanUntagged.setDescription('When VLANs are enabled, this allows tagged frames to be received, while transmitted frames remain untagged. This can only be enabled when the usdVlanSubIfVlanId field is zero. Cannot be changed if the vlan subinterface has upper bindings.')
usdVlanSubIfVlanStackId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanSubIfVlanStackId.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfVlanStackId.setDescription('An integer identifier or tag ID for this S-VLAN. When S-VLANs are enabled, the VLAN and S-VLAN ID valuse must be unique among subinterfaces configured on the same underlying major VLAN interface. If the S-VLANs are enabled, then the usdVlanSubIfVlanUntagged field must be disabled. Cannot be changed if the subinterface has upper bindings.')
usdVlanSubIfVlanStackEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(37120, 37376))).clone(namedValues=NamedValues(("etherType9100h", 37120), ("etherType9200h", 37376)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanSubIfVlanStackEthertype.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfVlanStackEthertype.setDescription('The ethertype is used to recognize and demultiplex traffic for this S-VLAN. Must be either 0x9100 or 0x9200. Cannot be changed if the subinterface has upper bindings.')
usdVlanSubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanSubIfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfLowerIfIndex.setDescription('The ifIndex of VLAN major interface over which this VLAN Subinterface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
usdVlanSubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 1, 4, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdVlanSubIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: usdVlanSubIfRowStatus usdVlanSubIfLowerIfIndex usdVlanSubIfVlanId usdVlanSubIfVlanUntagged To delete an entry in this table, the following entry objects MUST be explicitly configured: usdVlanSubIfRowStatus usdVlanSubIfLowerIfIndex In addition, when creating an entry the following conditions must hold: A value for usdVlanSubIfIndex must have been determined previously by reading usdVlanSubIfNextIfIndex. The interface identified by usdVlanSubIfLowerIfIndex must exist, and must be a Ethernet interface. A corresponding entry in ifTable/ifXTable/usdIfTable is created/destroyed as a result of creating/destroying an entry in this table.')
usdEthernetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4))
usdEthernetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1))
usdEthernetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2))
usdEthernetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 1)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdEthernetGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetCompliance = usdEthernetCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdEthernetCompliance.setDescription('Obsolete compliance statement for entities which implement the Unisphere Ethernet MIB. This statement became obsolete when support for VLANs was added.')
usdEthernetCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 2)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdEthernetGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetCompliance2 = usdEthernetCompliance2.setStatus('obsolete')
if mibBuilder.loadTexts: usdEthernetCompliance2.setDescription('Obsolete compliance statement for entities which implement the Unisphere Ethernet MIB. This statement became obsolete when VLAN stack support was added.')
usdEthernetCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 1, 3)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdEthernetGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanGroup"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetCompliance3 = usdEthernetCompliance3.setStatus('current')
if mibBuilder.loadTexts: usdEthernetCompliance3.setDescription('The compliance statement for entities which implement the Unisphere Ethernet MIB.')
usdEthernetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 1)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfDuplexMode"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfSpeed"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfMtu"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetIfOperDuplexMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetGroup = usdEthernetGroup.setStatus('current')
if mibBuilder.loadTexts: usdEthernetGroup.setDescription('A collection of objects providing management of Ethernet interfaces in a Unisphere product.')
usdEthernetSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 2)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfNextIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfRowStatus"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfLowerIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdEthernetSubIfId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetSubIfGroup = usdEthernetSubIfGroup.setStatus('current')
if mibBuilder.loadTexts: usdEthernetSubIfGroup.setDescription('A collection of objects providing management of Ethernet SubInterfaces in a Unisphere product.')
usdVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 3)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdVlanMajorNextIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanMajorIfLowerIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanMajorIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVlanGroup = usdVlanGroup.setStatus('current')
if mibBuilder.loadTexts: usdVlanGroup.setDescription('A collection of objects providing management of Major VLAN interfaces in a Unisphere product.')
usdVlanSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 4)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdVlanSubNextIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanId"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanUntagged"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfLowerIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVlanSubIfGroup = usdVlanSubIfGroup.setStatus('obsolete')
if mibBuilder.loadTexts: usdVlanSubIfGroup.setDescription('Obsolete collection of objects providing management of VLAN SubInterfaces in a Unisphere product. This group became obsolete when VLAN stack support was added.')
usdVlanSubIfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 34, 4, 2, 5)).setObjects(("Unisphere-Data-ETHERNET-MIB", "usdVlanSubNextIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanId"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanUntagged"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanStackId"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfVlanStackEthertype"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfLowerIfIndex"), ("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVlanSubIfGroup2 = usdVlanSubIfGroup2.setStatus('current')
if mibBuilder.loadTexts: usdVlanSubIfGroup2.setDescription('A collection of objects providing management of VLAN SubInterfaces in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-ETHERNET-MIB", usdEthernetSubIfEntry=usdEthernetSubIfEntry, usdEthernetMIB=usdEthernetMIB, usdEthernetIfLayer=usdEthernetIfLayer, usdEthernetIfMtu=usdEthernetIfMtu, usdVlanSubIfTable=usdVlanSubIfTable, usdVlanSubIfLowerIfIndex=usdVlanSubIfLowerIfIndex, usdVlanSubIfRowStatus=usdVlanSubIfRowStatus, usdEthernetSubIfNextIfIndex=usdEthernetSubIfNextIfIndex, usdEthernetGroups=usdEthernetGroups, usdVlanSubIfIndex=usdVlanSubIfIndex, usdVlanSubIfVlanUntagged=usdVlanSubIfVlanUntagged, usdEthernetSubIfRowStatus=usdEthernetSubIfRowStatus, usdVlanSubIfVlanStackEthertype=usdVlanSubIfVlanStackEthertype, usdEthernetObjects=usdEthernetObjects, usdVlanSubIfVlanStackId=usdVlanSubIfVlanStackId, usdEthernetIfTable=usdEthernetIfTable, usdVlanMajorIfLowerIfIndex=usdVlanMajorIfLowerIfIndex, usdVlanSubIfEntry=usdVlanSubIfEntry, usdEthernetGroup=usdEthernetGroup, usdEthernetIfSpeed=usdEthernetIfSpeed, usdVlanMajorIfRowStatus=usdVlanMajorIfRowStatus, usdVlanSubIfLayer=usdVlanSubIfLayer, usdVlanMajorIfEntry=usdVlanMajorIfEntry, usdEthernetIfEntry=usdEthernetIfEntry, usdVlanMajorIfIndex=usdVlanMajorIfIndex, usdEthernetSubIfLayer=usdEthernetSubIfLayer, usdVlanMajorIfLayer=usdVlanMajorIfLayer, usdVlanSubIfGroup=usdVlanSubIfGroup, usdEthernetSubIfLowerIfIndex=usdEthernetSubIfLowerIfIndex, usdVlanMajorIfTable=usdVlanMajorIfTable, usdEthernetSubIfIndex=usdEthernetSubIfIndex, usdEthernetCompliances=usdEthernetCompliances, usdEthernetConformance=usdEthernetConformance, usdEthernetSubIfGroup=usdEthernetSubIfGroup, usdEthernetIfDuplexMode=usdEthernetIfDuplexMode, usdEthernetSubIfId=usdEthernetSubIfId, usdVlanSubIfGroup2=usdVlanSubIfGroup2, usdVlanSubIfVlanId=usdVlanSubIfVlanId, usdVlanSubNextIfIndex=usdVlanSubNextIfIndex, usdEthernetCompliance3=usdEthernetCompliance3, usdEthernetCompliance2=usdEthernetCompliance2, usdEthernetCompliance=usdEthernetCompliance, usdEthernetIfOperDuplexMode=usdEthernetIfOperDuplexMode, usdEthernetSubIfTable=usdEthernetSubIfTable, usdVlanGroup=usdVlanGroup, PYSNMP_MODULE_ID=usdEthernetMIB, usdEthernetIfIndex=usdEthernetIfIndex, usdVlanMajorNextIfIndex=usdVlanMajorNextIfIndex)
