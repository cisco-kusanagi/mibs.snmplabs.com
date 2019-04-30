#
# PySNMP MIB module MY-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-PRIVATE-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Unsigned32, NotificationType, IpAddress, MibIdentifier, Integer32, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "iso", "TimeTicks", "ModuleIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
myPrivateVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44))
myPrivateVlanMIB.setRevisions(('2009-03-01 00:00',))
if mibBuilder.loadTexts: myPrivateVlanMIB.setLastUpdated('200903230000Z')
if mibBuilder.loadTexts: myPrivateVlanMIB.setOrganization('D-Link Crop.')
class PrivateVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("primary", 2), ("isolated", 3), ("community", 4))

class VlanIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanIndexBitmap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

mypvlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1))
mypvlanVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1))
mypvlanPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2))
mypvlanSVIObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3))
mypvlanVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1), )
if mibBuilder.loadTexts: mypvlanVlanTable.setStatus('current')
mypvlanVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1), ).setIndexNames((0, "MY-PRIVATE-VLAN-MIB", "mypvlanVlanIndex"))
if mibBuilder.loadTexts: mypvlanVlanEntry.setStatus('current')
mypvlanVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 1), VlanIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mypvlanVlanIndex.setStatus('current')
mypvlanVlanPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 2), PrivateVlanType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mypvlanVlanPrivateVlanType.setStatus('current')
mypvlanVlanAssociatedPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 3), VlanIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mypvlanVlanAssociatedPrimaryVlan.setStatus('current')
mypvlanIfAssociatedPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mypvlanIfAssociatedPrimaryVlan.setStatus('current')
mypvlanPrivatePortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1), )
if mibBuilder.loadTexts: mypvlanPrivatePortTable.setStatus('current')
mypvlanPrivatePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mypvlanPrivatePortEntry.setStatus('current')
mypvlanPrivatePortPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1, 1), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPrivatePortPrimaryVlan.setStatus('current')
mypvlanPrivatePortSecondaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1, 2), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPrivatePortSecondaryVlan.setStatus('current')
mypvlanPromPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2), )
if mibBuilder.loadTexts: mypvlanPromPortTable.setStatus('current')
mypvlanPromPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mypvlanPromPortEntry.setStatus('current')
mypvlanPrivatePortPrimaryVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 1), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPrivatePortPrimaryVlanId.setStatus('current')
mypvlanPromPortSecondaryRemap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap.setStatus('current')
mypvlanPromPortSecondaryRemap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap2k.setStatus('current')
mypvlanPromPortSecondaryRemap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap3k.setStatus('current')
mypvlanPromPortSecondaryRemap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap4k.setStatus('current')
mypvlanPortModeTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3), )
if mibBuilder.loadTexts: mypvlanPortModeTable.setStatus('current')
mypvlanPortModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mypvlanPortModeEntry.setStatus('current')
mypvlanPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonPrivateVlan", 1), ("host", 2), ("promiscuous", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPortMode.setStatus('current')
mypvlanSVIMappingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1), )
if mibBuilder.loadTexts: mypvlanSVIMappingTable.setStatus('current')
mypvlanSVIMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1), ).setIndexNames((0, "MY-PRIVATE-VLAN-MIB", "mypvlanSVIMappingVlanIndex"))
if mibBuilder.loadTexts: mypvlanSVIMappingEntry.setStatus('current')
mypvlanSVIMappingVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1, 1), VlanIndexOrZero())
if mibBuilder.loadTexts: mypvlanSVIMappingVlanIndex.setStatus('current')
mypvlanSVIMappingPrimarySVI = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1, 2), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanSVIMappingPrimarySVI.setStatus('current')
mypvlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2))
mypvlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 1))
mypvlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2))
mypvlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 1, 1)).setObjects(("MY-PRIVATE-VLAN-MIB", "mypvlanVlanGroup"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortGroup"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortGroup"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPortModeGroup"), ("MY-PRIVATE-VLAN-MIB", "mypvlanSVIGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanMIBCompliance = mypvlanMIBCompliance.setStatus('current')
mypvlanVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 1)).setObjects(("MY-PRIVATE-VLAN-MIB", "mypvlanVlanIndex"), ("MY-PRIVATE-VLAN-MIB", "mypvlanVlanPrivateVlanType"), ("MY-PRIVATE-VLAN-MIB", "mypvlanVlanAssociatedPrimaryVlan"), ("MY-PRIVATE-VLAN-MIB", "mypvlanIfAssociatedPrimaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanVlanGroup = mypvlanVlanGroup.setStatus('current')
mypvlanPrivatePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 2)).setObjects(("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortPrimaryVlan"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortSecondaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanPrivatePortGroup = mypvlanPrivatePortGroup.setStatus('current')
mypvlanPromPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 3)).setObjects(("MY-PRIVATE-VLAN-MIB", "mypvlanPrivatePortPrimaryVlan"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap2k"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap3k"), ("MY-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanPromPortGroup = mypvlanPromPortGroup.setStatus('current')
mypvlanPortModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 4)).setObjects(("MY-PRIVATE-VLAN-MIB", "mypvlanPortMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanPortModeGroup = mypvlanPortModeGroup.setStatus('current')
mypvlanSVIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 5)).setObjects(("MY-PRIVATE-VLAN-MIB", "mypvlanSVIMappingPrimarySVI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanSVIGroup = mypvlanSVIGroup.setStatus('current')
mibBuilder.exportSymbols("MY-PRIVATE-VLAN-MIB", mypvlanSVIMappingPrimarySVI=mypvlanSVIMappingPrimarySVI, mypvlanPromPortSecondaryRemap3k=mypvlanPromPortSecondaryRemap3k, mypvlanPrivatePortSecondaryVlan=mypvlanPrivatePortSecondaryVlan, mypvlanIfAssociatedPrimaryVlan=mypvlanIfAssociatedPrimaryVlan, mypvlanPromPortSecondaryRemap4k=mypvlanPromPortSecondaryRemap4k, mypvlanVlanIndex=mypvlanVlanIndex, mypvlanMIBCompliances=mypvlanMIBCompliances, VlanIndexBitmap=VlanIndexBitmap, mypvlanMIBGroups=mypvlanMIBGroups, mypvlanPromPortTable=mypvlanPromPortTable, mypvlanSVIMappingVlanIndex=mypvlanSVIMappingVlanIndex, mypvlanMIBConformance=mypvlanMIBConformance, mypvlanVlanGroup=mypvlanVlanGroup, mypvlanPortObjects=mypvlanPortObjects, PYSNMP_MODULE_ID=myPrivateVlanMIB, mypvlanPortModeTable=mypvlanPortModeTable, mypvlanPrivatePortPrimaryVlan=mypvlanPrivatePortPrimaryVlan, mypvlanPromPortGroup=mypvlanPromPortGroup, mypvlanPrivatePortGroup=mypvlanPrivatePortGroup, mypvlanPrivatePortTable=mypvlanPrivatePortTable, mypvlanVlanPrivateVlanType=mypvlanVlanPrivateVlanType, mypvlanPortModeEntry=mypvlanPortModeEntry, VlanIndexOrZero=VlanIndexOrZero, mypvlanPortMode=mypvlanPortMode, mypvlanSVIMappingEntry=mypvlanSVIMappingEntry, mypvlanSVIGroup=mypvlanSVIGroup, mypvlanSVIMappingTable=mypvlanSVIMappingTable, mypvlanPromPortSecondaryRemap2k=mypvlanPromPortSecondaryRemap2k, mypvlanPrivatePortPrimaryVlanId=mypvlanPrivatePortPrimaryVlanId, PrivateVlanType=PrivateVlanType, mypvlanVlanAssociatedPrimaryVlan=mypvlanVlanAssociatedPrimaryVlan, mypvlanPromPortEntry=mypvlanPromPortEntry, mypvlanVlanObjects=mypvlanVlanObjects, mypvlanMIBObjects=mypvlanMIBObjects, mypvlanPromPortSecondaryRemap=mypvlanPromPortSecondaryRemap, mypvlanPortModeGroup=mypvlanPortModeGroup, mypvlanVlanEntry=mypvlanVlanEntry, myPrivateVlanMIB=myPrivateVlanMIB, mypvlanPrivatePortEntry=mypvlanPrivatePortEntry, mypvlanSVIObjects=mypvlanSVIObjects, mypvlanMIBCompliance=mypvlanMIBCompliance, mypvlanVlanTable=mypvlanVlanTable)
