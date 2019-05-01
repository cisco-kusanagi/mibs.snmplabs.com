#
# PySNMP MIB module HP-ICF-PRIVATEVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-PRIVATEVLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
VlanId, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "dot1qVlanStaticEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Unsigned32, Bits, Counter64, NotificationType, Integer32, Gauge32, ObjectIdentity, Counter32, IpAddress, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Counter64", "NotificationType", "Integer32", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hpicfPrivateVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114))
hpicfPrivateVlan.setRevisions(('2015-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfPrivateVlan.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: hpicfPrivateVlan.setLastUpdated('201504220000Z')
if mibBuilder.loadTexts: hpicfPrivateVlan.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfPrivateVlan.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfPrivateVlan.setDescription('This MIB module contains HP proprietary definition of Private Vlan.')
class PrivateVlanType(TextualConvention, Integer32):
    description = "The VLAN types defined are 'notAPrivateVLAN' This is a regular VLAN. 'primary' This a VLAN which is partitioned into independent broadcast domains. 'isolated' This is a VLAN carved out from the primary VLAN and having strict traffic isolation between member ports. 'community' This is a VLAN carved out from the primary VLAN and with traffic allowed between member ports."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notAPrivateVLAN", 1), ("primary", 2), ("isolated", 3), ("community", 4))

hpicfPrivateVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1))
hpicfPrivateVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1))
hpicfPrivateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfPrivateVlanTable.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanTable.setDescription('An HP proprietary extension to the dot1qVlanStaticTable to contain Private VLAN type.')
hpicfPrivateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanEntry"))
hpicfPrivateVlanEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfPrivateVlanEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanEntry.setDescription('An entry for HP Specific extension to the dot1qVlanStaticTable to contain Private VLAN type.')
hpicfPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1, 1), PrivateVlanType().clone('notAPrivateVLAN')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPrivateVlanType.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanType.setDescription('This object refers to the type of a Private VLAN which can be a primary, isolated or a community VLAN.')
hpicfPrivateVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfPrivateVlanMappingTable.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanMappingTable.setDescription('A table containing the mapping of a primary to secondary VLANs.')
hpicfPrivateVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1), ).setIndexNames((0, "HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanPrimary"))
if mibBuilder.loadTexts: hpicfPrivateVlanMappingEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanMappingEntry.setDescription('An entry which containing the configuration of Primary to Secondary VLANs.')
hpicfPrivateVlanPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: hpicfPrivateVlanPrimary.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanPrimary.setDescription('This object is the Primary VLAN.')
hpicfPrivateVlanIsolated = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanIsolated.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanIsolated.setDescription('This object refers to an Isolated VLAN ID associated to the Primary VLAN.')
hpicfPrivateVlanCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 3), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanCommunity.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanCommunity.setDescription('This object refers to the list of Community VLANs which are associated to the Primary VLAN.')
hpicfPrivateVlanMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanMappingRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanMappingRowStatus.setDescription('The Row status for the Primary VLAN entry.')
hpicfPrivateVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2))
hpicfPrivateVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1))
hpicfPrivateVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2))
hpicfPVlanTableCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 1)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanTableGroup"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanTableCompliance = hpicfPVlanTableCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfPVlanTableCompliance.setDescription('A compliance statement for HP Routing switches which hpicfPrviateVlan MIB.')
hpicfPVlanMappingTblCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 2)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPVlanMappingTableGroup"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPVlanMappingTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanMappingTblCompliance = hpicfPVlanMappingTblCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfPVlanMappingTblCompliance.setDescription('The compliance statement for SNMP entities which implement the hpicfPrviateVlan MIB.')
hpicfPrivateVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 1)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPrivateVlanTableGroup = hpicfPrivateVlanTableGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfPrivateVlanTableGroup.setDescription('The collection of object(s) represent the Private VLAN Type.')
hpicfPVlanMappingTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 2)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanIsolated"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanCommunity"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanMappingTableGroup = hpicfPVlanMappingTableGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfPVlanMappingTableGroup.setDescription('The collection of objects which are used to represent the Primary and associated Secondary VLANs.')
mibBuilder.exportSymbols("HP-ICF-PRIVATEVLAN-MIB", hpicfPrivateVlanConfig=hpicfPrivateVlanConfig, hpicfPVlanTableCompliance=hpicfPVlanTableCompliance, hpicfPrivateVlanEntry=hpicfPrivateVlanEntry, hpicfPrivateVlanTableGroup=hpicfPrivateVlanTableGroup, hpicfPrivateVlanCompliances=hpicfPrivateVlanCompliances, hpicfPrivateVlanConformance=hpicfPrivateVlanConformance, PrivateVlanType=PrivateVlanType, hpicfPrivateVlanMappingRowStatus=hpicfPrivateVlanMappingRowStatus, hpicfPrivateVlanPrimary=hpicfPrivateVlanPrimary, hpicfPrivateVlanType=hpicfPrivateVlanType, hpicfPrivateVlanMappingTable=hpicfPrivateVlanMappingTable, hpicfPVlanMappingTableGroup=hpicfPVlanMappingTableGroup, hpicfPrivateVlan=hpicfPrivateVlan, hpicfPrivateVlanObjects=hpicfPrivateVlanObjects, hpicfPrivateVlanTable=hpicfPrivateVlanTable, hpicfPrivateVlanMappingEntry=hpicfPrivateVlanMappingEntry, hpicfPrivateVlanIsolated=hpicfPrivateVlanIsolated, hpicfPrivateVlanGroup=hpicfPrivateVlanGroup, PYSNMP_MODULE_ID=hpicfPrivateVlan, hpicfPrivateVlanCommunity=hpicfPrivateVlanCommunity, hpicfPVlanMappingTblCompliance=hpicfPVlanMappingTblCompliance)
