#
# PySNMP MIB module HPN-ICF-EVI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-EVI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
IsisSystemID, = mibBuilder.importSymbols("ISIS-MIB", "IsisSystemID")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, iso, Bits, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Counter64")
DisplayString, TruthValue, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "RowStatus", "TextualConvention")
hpnicfEvi = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132))
hpnicfEvi.setRevisions(('2013-04-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfEvi.setRevisionsDescriptions(('HPN-ICF-EVI-MIB module for managing EVI-capable switches.',))
if mibBuilder.loadTexts: hpnicfEvi.setLastUpdated('201304280000Z')
if mibBuilder.loadTexts: hpnicfEvi.setOrganization('')
if mibBuilder.loadTexts: hpnicfEvi.setContactInfo('')
if mibBuilder.loadTexts: hpnicfEvi.setDescription('This MIB contains the objects for managing Ethernet Virtual Interconnect(EVI).')
hpnicfEviNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0))
hpnicfEviObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1))
hpnicfEviBase = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 1))
hpnicfEviIf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2))
hpnicfEviMac = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3))
hpnicfEviProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4))
hpnicfEviISIS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5))
hpnicfEviEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6))
hpnicfEviNbr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7))
class HpnicfEviMacType(TextualConvention, Integer32):
    description = 'MAC addresses include three types: dynamic, static, and flood (MACs configured for selective flooding).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("dynamic", 2), ("static", 3), ("flood", 4))

class HpnicfEviNeighborStatus(TextualConvention, Integer32):
    description = 'State of EVI neighbors.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

hpnicfEviDesignatedVlan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 1, 1), VlanId().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviDesignatedVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviDesignatedVlan.setDescription('The designated VLAN is used for edge devices on a multihomed site to exchange EVI IS-IS hello packets for DED election and extended-VLAN assignment.')
hpnicfEviSiteID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviSiteID.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviSiteID.setDescription('Site ID. The edge devices in the same site must have the same site ID.')
hpnicfEviIfExtendVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanTable.setDescription('A table that contains extended VLAN entries. A site extends extended VLANs to remote sites over an EVI tunnel.')
hpnicfEviIfExtendVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfExtendVlanIndex"))
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanEntry.setDescription('Detailed information about each extended VLAN.')
hpnicfEviIfExtendVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanIndex.setDescription('Each VLAN index specifies a VLAN ID in the range of 1 to 4094.')
hpnicfEviIfExtendVlanLAV = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanLAV.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanLAV.setDescription('Local Active VLANs (LAVs), which are active VLANs on the EVI tunnel interface. The interface can extend only active VLANs to remote sites.')
hpnicfEviIfExtendVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfExtendVlanRowStatus.setDescription('Entry status.')
hpnicfEviIfVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2), )
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingTable.setDescription('VLAN mapping table on the interface.')
hpnicfEviIfVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfVlanMappingSiteId"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfVlanMappingSrc"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfVlanMappingDst"))
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingEntry.setDescription('Detailed information about each VLAN mapping.')
hpnicfEviIfVlanMappingSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingSiteId.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingSiteId.setDescription("Site ID of the interface on which the VLAN mapping is configured. If '0' is specified, the operation applies to all sites.")
hpnicfEviIfVlanMappingSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 2), VlanId())
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingSrc.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingSrc.setDescription('Local VLAN ID in the mapping.')
hpnicfEviIfVlanMappingDst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 3), VlanId())
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingDst.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingDst.setDescription('Remote VLAN ID in the mapping.')
hpnicfEviIfVlanMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfVlanMappingRowStatus.setDescription('Entry status.')
hpnicfEviIfAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3), )
if mibBuilder.loadTexts: hpnicfEviIfAttributeTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfAttributeTable.setDescription('A table that contains EVI tunnel attribute entries.')
hpnicfEviIfAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfEviIfAttributeEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfAttributeEntry.setDescription('Detailed information about the attributes of each EVI tunnel.')
hpnicfEviIfFloodingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviIfFloodingMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfFloodingMode.setDescription('State of the EVI flooding function. The function is enabled if the value is set to true.')
hpnicfEviIfARPSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviIfARPSuppression.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfARPSuppression.setDescription('State of the ARP flooding suppression function. The function is enabled if the value is set to true.')
hpnicfEviIfFloodingMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4), )
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacTable.setDescription('A table that contains MAC addresses configured for selective flooding.')
hpnicfEviIfFloodingMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfFloodingMacAddress"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviIfFloodMacVlanIndex"))
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacEntry.setDescription('Detailed information about each MAC address used for EVI selective flooding.')
hpnicfEviIfFloodingMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacAddress.setDescription('MAC address used for EVI selective flooding.')
hpnicfEviIfFloodMacVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1, 2), VlanId())
if mibBuilder.loadTexts: hpnicfEviIfFloodMacVlanIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfFloodMacVlanIndex.setDescription('The VLAN that contains the MAC address.')
hpnicfEviIfFloodingMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 2, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviIfFloodingMacRowStatus.setDescription('State of the MAC address entry. You can use this object to create or delete entries. Deleting entries does not delete this object.')
hpnicfEviMacCountTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1), )
if mibBuilder.loadTexts: hpnicfEviMacCountTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacCountTable.setDescription('EVI MAC statistics table. The table contains MAC entry counts sorted by MAC address types, including local MACs, local MAC conflicts, remote MACs, and remote MAC conflicts.')
hpnicfEviMacCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfEviMacCountEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacCountEntry.setDescription('EVI MAC entry counts.')
hpnicfEviMacLocalMacs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacLocalMacs.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalMacs.setDescription('Number of local MACs.')
hpnicfEviMacLocalConflicts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacLocalConflicts.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalConflicts.setDescription('Number of local MACs that conflict with remote MACs.')
hpnicfEviMacRemoteMacs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacRemoteMacs.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteMacs.setDescription('Number of remote MACs received from remote edge devices.')
hpnicfEviMacRemoteConflicts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacRemoteConflicts.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteConflicts.setDescription('Number of remote MACs that conflict with local MACs.')
hpnicfEviMacLocalTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2), )
if mibBuilder.loadTexts: hpnicfEviMacLocalTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalTable.setDescription('MAC address table that only contains MAC addresses at the site.')
hpnicfEviMacLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacLocalVlan"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacLocalMacAddr"))
if mibBuilder.loadTexts: hpnicfEviMacLocalEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalEntry.setDescription('Detailed informaiton about each local MAC entry.')
hpnicfEviMacLocalVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: hpnicfEviMacLocalVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalVlan.setDescription('VLANs that contain the local MACs.')
hpnicfEviMacLocalMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 2), MacAddress())
if mibBuilder.loadTexts: hpnicfEviMacLocalMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalMacAddr.setDescription('Local MAC addresses.')
hpnicfEviMacLocalMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 3), HpnicfEviMacType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacLocalMacType.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalMacType.setDescription('MAC address types, including: dynamic MACs, static MACs, and flood MACs (MACs configured for selective flooding).')
hpnicfEviMacLocalConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacLocalConflict.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalConflict.setDescription('Whether the MAC conflicts with any remote MAC.')
hpnicfEviMacLocalFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacLocalFiltered.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacLocalFiltered.setDescription('Whether the MAC is filtered.')
hpnicfEviMacRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3), )
if mibBuilder.loadTexts: hpnicfEviMacRemoteTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteTable.setDescription('A table contains MAC addresses received from remote edge devices.')
hpnicfEviMacRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacRemoteVlan"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviMacRemoteMacAddr"))
if mibBuilder.loadTexts: hpnicfEviMacRemoteEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteEntry.setDescription('Detailed information about each remote MAC.')
hpnicfEviMacRemoteVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 1), VlanId())
if mibBuilder.loadTexts: hpnicfEviMacRemoteVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteVlan.setDescription('VLANs that contain remote MAC addresses.')
hpnicfEviMacRemoteMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: hpnicfEviMacRemoteMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteMacAddr.setDescription('Remote MAC address.')
hpnicfEviMacRemoteMacEffect = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacRemoteMacEffect.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteMacEffect.setDescription('Whether the MAC can be used for forwarding traffic.')
hpnicfEviMacRemoteConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 3, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviMacRemoteConflict.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviMacRemoteConflict.setDescription('The remote MAC conflicts with a local MAC.')
hpnicfEviProcessPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1), )
if mibBuilder.loadTexts: hpnicfEviProcessPolicyTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessPolicyTable.setDescription('A table that contains routing policy information for each EVI IS-IS process.')
hpnicfEviProcessPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1, 1), ).setIndexNames((0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"))
if mibBuilder.loadTexts: hpnicfEviProcessPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessPolicyEntry.setDescription('Detailed information about the routing policy for each EVI IS-IS process.')
hpnicfEviProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfEviProcessId.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessId.setDescription('EVI IS-IS process ID.')
hpnicfEviProcessPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviProcessPolicy.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessPolicy.setDescription('Routing policy for the EVI IS-IS process.')
hpnicfEviProcessGrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2), )
if mibBuilder.loadTexts: hpnicfEviProcessGrTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessGrTable.setDescription('A table that contains graceful restart (GR) information.')
hpnicfEviProcessGrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2, 1), ).setIndexNames((0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"))
if mibBuilder.loadTexts: hpnicfEviProcessGrEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessGrEntry.setDescription('Detailed GR information for each EVI IS-IS process.')
hpnicfEviProcessGrEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviProcessGrEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessGrEnable.setDescription('Whether the GR function is enabled.')
hpnicfEviProcessGrInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 1800)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviProcessGrInterval.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessGrInterval.setDescription('EVI IS-IS GR interval in the range of 30 to 1800, in seconds.')
hpnicfEviProcessVSysTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3), )
if mibBuilder.loadTexts: hpnicfEviProcessVSysTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessVSysTable.setDescription('A table that contains virtual system entries. Virtual systems are associated with EVI IS-IS processes.')
hpnicfEviProcessVSysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3, 1), ).setIndexNames((0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviVirtualSysId"))
if mibBuilder.loadTexts: hpnicfEviProcessVSysEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviProcessVSysEntry.setDescription('Detailed information about each vitual system.')
hpnicfEviVirtualSysId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3, 1, 1), IsisSystemID())
if mibBuilder.loadTexts: hpnicfEviVirtualSysId.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviVirtualSysId.setDescription('Virtual system ID in hexadecimal notation. The virtual system ID must be unique in the EVI network.')
hpnicfEviVirtualSysRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 4, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEviVirtualSysRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviVirtualSysRowStatus.setDescription('Entry status.')
hpnicfEviISISNbrSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1), )
if mibBuilder.loadTexts: hpnicfEviISISNbrSummaryTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrSummaryTable.setDescription('EVI neighbor statistics table.')
hpnicfEviISISNbrSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1), ).setIndexNames((0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"))
if mibBuilder.loadTexts: hpnicfEviISISNbrSummaryEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrSummaryEntry.setDescription('EVI neighbor statistics table entries. The entries contain the EVI neighbor summary for each EVI IS-IS process.')
hpnicfEviISISNbrMaxMultiHomes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviISISNbrMaxMultiHomes.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrMaxMultiHomes.setDescription('The maximum number of edge devices that the site can contain.')
hpnicfEviISISNbrSiteNbrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviISISNbrSiteNbrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrSiteNbrs.setDescription('The count of neighbors that belong to the same site.')
hpnicfEviISISNbrLinkNbrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviISISNbrLinkNbrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrLinkNbrs.setDescription('The count of neighbors that are in remote sites.')
hpnicfEviISISNbrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2), )
if mibBuilder.loadTexts: hpnicfEviISISNbrTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrTable.setDescription('A table that contains generic information about all neighbors.')
hpnicfEviISISNbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1), ).setIndexNames((0, "HPN-ICF-EVI-MIB", "hpnicfEviProcessId"), (0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviISISNbrSysId"))
if mibBuilder.loadTexts: hpnicfEviISISNbrEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrEntry.setDescription('Detailed information about each neighbor of the edge device.')
hpnicfEviISISNbrSysId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 1), IsisSystemID()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfEviISISNbrSysId.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrSysId.setDescription('System ID of the neighbor.')
hpnicfEviISISNbrMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviISISNbrMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrMacAddr.setDescription('MAC address of the neighbor.')
hpnicfEviISISNbrSiteId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviISISNbrSiteId.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrSiteId.setDescription('Site ID of the neighbor.')
hpnicfEviISISNbrTransStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 5, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviISISNbrTransStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviISISNbrTransStatus.setDescription('State of EVI transport-facing links.')
hpnicfEviEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6, 1), )
if mibBuilder.loadTexts: hpnicfEviEnableTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviEnableTable.setDescription('A table that contains all EVI-enabled neighboring ports of the edge device.')
hpnicfEviEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfEviEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviEnableEntry.setDescription('Detailed information about each EVI-enabled port in the EVI network.')
hpnicfEviEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 6, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviEnableStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviEnableStatus.setDescription('End station service disable (trunk port) bit. When this bit is set (true), all native frames received on the port and all native frames that would have been sent on the port are discarded. The value of this object MUST be retained across reinitializations of the management system.')
hpnicfEviNbrBaseTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1), )
if mibBuilder.loadTexts: hpnicfEviNbrBaseTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrBaseTable.setDescription('A table that contains basic information about the EVI Neighbor Discovery Protocol (ENDP).')
hpnicfEviNbrBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfEviNbrBaseEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrBaseEntry.setDescription('Detailed information about ENDP for each EVI tunnel.')
hpnicfEviNbrSelfServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviNbrSelfServerStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrSelfServerStatus.setDescription('If the value is set to true, the EVI neighbor discovery server (ENDS) is enabled. When you enable ENDS on an EVI tunnel interface, an EVI neighbor discovery client (ENDC) on the EVI tunnel interface is also enabled automatically, with the source address of the EVI tunnel as the server address.')
hpnicfEviNbrAuthPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviNbrAuthPassword.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrAuthPassword.setDescription('ENDP authentication key. It is a zero-length string when being read.')
hpnicfEviNbrClientRegisterInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEviNbrClientRegisterInterval.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrClientRegisterInterval.setDescription('Interval at which the ENDCs on an EVI tunnel interface update their registration with their ENDSs.')
hpnicfEviNbrRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2), )
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerTable.setDescription('A table that contains basic information about the remote ENDSs.')
hpnicfEviNbrRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrRemoteServerType"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrRemoteServer"))
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerEntry.setDescription('Detailed information about each remote ENDS. When you set the address of a remote ENDS on an EVI tunnel interface, an ENDC is enabled automatically on the EVI tunnel interface.')
hpnicfEviNbrRemoteServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerType.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerType.setDescription('Address type of the remote ENDS, including ipv4 and ipv6.')
hpnicfEviNbrRemoteServer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServer.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServer.setDescription('Address of the remote ENDS. The address type is specified by the hpnicfEviNbrRemoteServerType object. Address length (4 or 16 bytes) must be consistent with the address type.')
hpnicfEviNbrRemoteServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrRemoteServerRowStatus.setDescription('Entry status. This object is used to create or delete entries. Deleting entries does not delete this object.')
hpnicfEviNbrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3), )
if mibBuilder.loadTexts: hpnicfEviNbrTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrTable.setDescription('A table that contains basic information about neighbors discovered with ENDP.')
hpnicfEviNbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrAddressType"), (0, "HPN-ICF-EVI-MIB", "hpnicfEviNbrAddress"))
if mibBuilder.loadTexts: hpnicfEviNbrEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrEntry.setDescription('Detailed information about each EVI neighbor.')
hpnicfEviNbrAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpnicfEviNbrAddressType.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrAddressType.setDescription('Address type of the neighbor, including ipv4 and ipv6.')
hpnicfEviNbrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: hpnicfEviNbrAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrAddress.setDescription('Address of the neighbor. The address type is specified by the hpnicfEviNbrAddressType object. Address length (4 or 16 bytes) must be consistent with the address type.')
hpnicfEviNbrSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviNbrSystemID.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrSystemID.setDescription('System ID of the neighbor.')
hpnicfEviNbrExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviNbrExpireTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrExpireTime.setDescription('Expiration time of the neighbor.')
hpnicfEviNbrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 1, 7, 3, 1, 5), HpnicfEviNeighborStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEviNbrStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNbrStatus.setDescription('State of the neighbor.')
hpnicfEviNewDed = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-EVI-MIB", "hpnicfEviProcessId"), ("HPN-ICF-EVI-MIB", "hpnicfEviISISNbrSysId"))
if mibBuilder.loadTexts: hpnicfEviNewDed.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviNewDed.setDescription('Notifies that a new DED has been elected.')
hpnicfEviSiteEDTopoChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0, 2)).setObjects(("HPN-ICF-EVI-MIB", "hpnicfEviProcessId"), ("HPN-ICF-EVI-MIB", "hpnicfEviISISNbrSiteNbrs"))
if mibBuilder.loadTexts: hpnicfEviSiteEDTopoChange.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviSiteEDTopoChange.setDescription('Notifies that the EVI network topology has changed.')
hpnicfEviEDLinkDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132, 0, 3)).setObjects(("HPN-ICF-EVI-MIB", "hpnicfEviProcessId"))
if mibBuilder.loadTexts: hpnicfEviEDLinkDisconnect.setStatus('current')
if mibBuilder.loadTexts: hpnicfEviEDLinkDisconnect.setDescription('Notifies that all the EVI links on a tunnel are down.')
mibBuilder.exportSymbols("HPN-ICF-EVI-MIB", hpnicfEviNbrAddress=hpnicfEviNbrAddress, hpnicfEviMacRemoteMacEffect=hpnicfEviMacRemoteMacEffect, hpnicfEviISISNbrMaxMultiHomes=hpnicfEviISISNbrMaxMultiHomes, hpnicfEviBase=hpnicfEviBase, hpnicfEviDesignatedVlan=hpnicfEviDesignatedVlan, hpnicfEviNbrClientRegisterInterval=hpnicfEviNbrClientRegisterInterval, hpnicfEviSiteID=hpnicfEviSiteID, hpnicfEviEnableStatus=hpnicfEviEnableStatus, hpnicfEviIfFloodingMacRowStatus=hpnicfEviIfFloodingMacRowStatus, hpnicfEviNbrEntry=hpnicfEviNbrEntry, hpnicfEviISISNbrLinkNbrs=hpnicfEviISISNbrLinkNbrs, hpnicfEviNbrSystemID=hpnicfEviNbrSystemID, hpnicfEviIfExtendVlanLAV=hpnicfEviIfExtendVlanLAV, hpnicfEviNbrRemoteServerType=hpnicfEviNbrRemoteServerType, hpnicfEviIfFloodingMacEntry=hpnicfEviIfFloodingMacEntry, PYSNMP_MODULE_ID=hpnicfEvi, hpnicfEviProcess=hpnicfEviProcess, hpnicfEviIfVlanMappingSrc=hpnicfEviIfVlanMappingSrc, hpnicfEviNbrAuthPassword=hpnicfEviNbrAuthPassword, hpnicfEviIfVlanMappingEntry=hpnicfEviIfVlanMappingEntry, hpnicfEviEDLinkDisconnect=hpnicfEviEDLinkDisconnect, hpnicfEviVirtualSysId=hpnicfEviVirtualSysId, hpnicfEviISISNbrSummaryTable=hpnicfEviISISNbrSummaryTable, hpnicfEviNbrRemoteServerRowStatus=hpnicfEviNbrRemoteServerRowStatus, hpnicfEviNbrRemoteServerTable=hpnicfEviNbrRemoteServerTable, hpnicfEviMacLocalMacType=hpnicfEviMacLocalMacType, hpnicfEviProcessPolicy=hpnicfEviProcessPolicy, hpnicfEviIfVlanMappingDst=hpnicfEviIfVlanMappingDst, hpnicfEviNbrRemoteServer=hpnicfEviNbrRemoteServer, hpnicfEviNbrBaseEntry=hpnicfEviNbrBaseEntry, hpnicfEviProcessGrEntry=hpnicfEviProcessGrEntry, hpnicfEviISISNbrMacAddr=hpnicfEviISISNbrMacAddr, hpnicfEviMac=hpnicfEviMac, hpnicfEviProcessVSysTable=hpnicfEviProcessVSysTable, hpnicfEviEnableTable=hpnicfEviEnableTable, hpnicfEviMacRemoteTable=hpnicfEviMacRemoteTable, hpnicfEviMacLocalMacAddr=hpnicfEviMacLocalMacAddr, hpnicfEviProcessVSysEntry=hpnicfEviProcessVSysEntry, hpnicfEviIfFloodingMode=hpnicfEviIfFloodingMode, hpnicfEviNbrRemoteServerEntry=hpnicfEviNbrRemoteServerEntry, hpnicfEviNbrExpireTime=hpnicfEviNbrExpireTime, hpnicfEviProcessPolicyTable=hpnicfEviProcessPolicyTable, hpnicfEviIfExtendVlanTable=hpnicfEviIfExtendVlanTable, hpnicfEviIfExtendVlanIndex=hpnicfEviIfExtendVlanIndex, hpnicfEvi=hpnicfEvi, hpnicfEviEnable=hpnicfEviEnable, hpnicfEviIfFloodingMacTable=hpnicfEviIfFloodingMacTable, hpnicfEviNewDed=hpnicfEviNewDed, hpnicfEviISISNbrSummaryEntry=hpnicfEviISISNbrSummaryEntry, hpnicfEviISIS=hpnicfEviISIS, hpnicfEviISISNbrSiteNbrs=hpnicfEviISISNbrSiteNbrs, hpnicfEviNbrTable=hpnicfEviNbrTable, hpnicfEviIfExtendVlanRowStatus=hpnicfEviIfExtendVlanRowStatus, hpnicfEviProcessPolicyEntry=hpnicfEviProcessPolicyEntry, hpnicfEviISISNbrSiteId=hpnicfEviISISNbrSiteId, hpnicfEviIfVlanMappingTable=hpnicfEviIfVlanMappingTable, hpnicfEviSiteEDTopoChange=hpnicfEviSiteEDTopoChange, hpnicfEviISISNbrTable=hpnicfEviISISNbrTable, hpnicfEviProcessGrTable=hpnicfEviProcessGrTable, hpnicfEviMacCountTable=hpnicfEviMacCountTable, hpnicfEviMacRemoteMacAddr=hpnicfEviMacRemoteMacAddr, hpnicfEviIfVlanMappingSiteId=hpnicfEviIfVlanMappingSiteId, hpnicfEviIfFloodingMacAddress=hpnicfEviIfFloodingMacAddress, hpnicfEviNbrBaseTable=hpnicfEviNbrBaseTable, hpnicfEviISISNbrTransStatus=hpnicfEviISISNbrTransStatus, hpnicfEviIfFloodMacVlanIndex=hpnicfEviIfFloodMacVlanIndex, hpnicfEviMacLocalVlan=hpnicfEviMacLocalVlan, hpnicfEviMacRemoteConflicts=hpnicfEviMacRemoteConflicts, hpnicfEviProcessGrInterval=hpnicfEviProcessGrInterval, hpnicfEviMacRemoteMacs=hpnicfEviMacRemoteMacs, hpnicfEviIfAttributeEntry=hpnicfEviIfAttributeEntry, hpnicfEviNbrStatus=hpnicfEviNbrStatus, hpnicfEviMacLocalMacs=hpnicfEviMacLocalMacs, hpnicfEviIf=hpnicfEviIf, hpnicfEviMacLocalConflict=hpnicfEviMacLocalConflict, hpnicfEviISISNbrEntry=hpnicfEviISISNbrEntry, hpnicfEviIfARPSuppression=hpnicfEviIfARPSuppression, hpnicfEviVirtualSysRowStatus=hpnicfEviVirtualSysRowStatus, hpnicfEviNbrAddressType=hpnicfEviNbrAddressType, hpnicfEviIfExtendVlanEntry=hpnicfEviIfExtendVlanEntry, hpnicfEviMacRemoteEntry=hpnicfEviMacRemoteEntry, hpnicfEviMacLocalEntry=hpnicfEviMacLocalEntry, hpnicfEviEnableEntry=hpnicfEviEnableEntry, HpnicfEviNeighborStatus=HpnicfEviNeighborStatus, hpnicfEviNbrSelfServerStatus=hpnicfEviNbrSelfServerStatus, hpnicfEviIfVlanMappingRowStatus=hpnicfEviIfVlanMappingRowStatus, hpnicfEviMacCountEntry=hpnicfEviMacCountEntry, HpnicfEviMacType=HpnicfEviMacType, hpnicfEviIfAttributeTable=hpnicfEviIfAttributeTable, hpnicfEviNbr=hpnicfEviNbr, hpnicfEviNotifications=hpnicfEviNotifications, hpnicfEviMacRemoteVlan=hpnicfEviMacRemoteVlan, hpnicfEviProcessGrEnable=hpnicfEviProcessGrEnable, hpnicfEviMacLocalConflicts=hpnicfEviMacLocalConflicts, hpnicfEviISISNbrSysId=hpnicfEviISISNbrSysId, hpnicfEviMacLocalTable=hpnicfEviMacLocalTable, hpnicfEviMacLocalFiltered=hpnicfEviMacLocalFiltered, hpnicfEviObjects=hpnicfEviObjects, hpnicfEviProcessId=hpnicfEviProcessId, hpnicfEviMacRemoteConflict=hpnicfEviMacRemoteConflict)
