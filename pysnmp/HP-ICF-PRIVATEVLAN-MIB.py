#
# PySNMP MIB module HP-ICF-PRIVATEVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-PRIVATEVLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
VlanId, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "dot1qVlanStaticEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Counter64, Bits, Integer32, iso, TimeTicks, Unsigned32, IpAddress, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Counter64", "Bits", "Integer32", "iso", "TimeTicks", "Unsigned32", "IpAddress", "Counter32", "NotificationType")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hpicfPrivateVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114))
hpicfPrivateVlan.setRevisions(('2015-04-22 00:00',))
if mibBuilder.loadTexts: hpicfPrivateVlan.setLastUpdated('201504220000Z')
if mibBuilder.loadTexts: hpicfPrivateVlan.setOrganization('HP Networking')
class PrivateVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notAPrivateVLAN", 1), ("primary", 2), ("isolated", 3), ("community", 4))

hpicfPrivateVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1))
hpicfPrivateVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1))
hpicfPrivateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfPrivateVlanTable.setStatus('current')
hpicfPrivateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanEntry"))
hpicfPrivateVlanEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfPrivateVlanEntry.setStatus('current')
hpicfPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1, 1), PrivateVlanType().clone('notAPrivateVLAN')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPrivateVlanType.setStatus('current')
hpicfPrivateVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfPrivateVlanMappingTable.setStatus('current')
hpicfPrivateVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1), ).setIndexNames((0, "HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanPrimary"))
if mibBuilder.loadTexts: hpicfPrivateVlanMappingEntry.setStatus('current')
hpicfPrivateVlanPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: hpicfPrivateVlanPrimary.setStatus('current')
hpicfPrivateVlanIsolated = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanIsolated.setStatus('current')
hpicfPrivateVlanCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 3), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanCommunity.setStatus('current')
hpicfPrivateVlanMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanMappingRowStatus.setStatus('current')
hpicfPrivateVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2))
hpicfPrivateVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1))
hpicfPrivateVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2))
hpicfPVlanTableCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 1)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanTableGroup"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanTableCompliance = hpicfPVlanTableCompliance.setStatus('current')
hpicfPVlanMappingTblCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 2)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPVlanMappingTableGroup"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPVlanMappingTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanMappingTblCompliance = hpicfPVlanMappingTblCompliance.setStatus('current')
hpicfPrivateVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 1)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPrivateVlanTableGroup = hpicfPrivateVlanTableGroup.setStatus('current')
hpicfPVlanMappingTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 2)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanIsolated"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanCommunity"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanMappingTableGroup = hpicfPVlanMappingTableGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-PRIVATEVLAN-MIB", hpicfPrivateVlan=hpicfPrivateVlan, hpicfPVlanMappingTblCompliance=hpicfPVlanMappingTblCompliance, hpicfPVlanMappingTableGroup=hpicfPVlanMappingTableGroup, hpicfPVlanTableCompliance=hpicfPVlanTableCompliance, hpicfPrivateVlanObjects=hpicfPrivateVlanObjects, hpicfPrivateVlanTable=hpicfPrivateVlanTable, PYSNMP_MODULE_ID=hpicfPrivateVlan, hpicfPrivateVlanType=hpicfPrivateVlanType, PrivateVlanType=PrivateVlanType, hpicfPrivateVlanTableGroup=hpicfPrivateVlanTableGroup, hpicfPrivateVlanGroup=hpicfPrivateVlanGroup, hpicfPrivateVlanEntry=hpicfPrivateVlanEntry, hpicfPrivateVlanMappingTable=hpicfPrivateVlanMappingTable, hpicfPrivateVlanMappingRowStatus=hpicfPrivateVlanMappingRowStatus, hpicfPrivateVlanConformance=hpicfPrivateVlanConformance, hpicfPrivateVlanIsolated=hpicfPrivateVlanIsolated, hpicfPrivateVlanCompliances=hpicfPrivateVlanCompliances, hpicfPrivateVlanConfig=hpicfPrivateVlanConfig, hpicfPrivateVlanPrimary=hpicfPrivateVlanPrimary, hpicfPrivateVlanCommunity=hpicfPrivateVlanCommunity, hpicfPrivateVlanMappingEntry=hpicfPrivateVlanMappingEntry)
