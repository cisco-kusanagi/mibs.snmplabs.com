#
# PySNMP MIB module Unisphere-Data-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:30:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifStackHigherLayer, ifStackLowerLayer, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifStackHigherLayer", "ifStackLowerLayer", "ifEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter64, Bits, ObjectIdentity, iso, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier, Integer32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "Counter32", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
usdIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3))
usdIfMIB.setRevisions(('2001-03-28 15:12', '2000-11-22 23:41', '2000-09-29 18:35', '2000-07-27 15:45', '2000-05-05 15:08', '1999-12-21 15:18', '1999-09-03 14:16', '1998-11-13 20:19',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdIfMIB.setRevisionsDescriptions(('Added interface types: l2fTunnelInterface(40), l2fSessionInterface(41), l2fDestinationInterface(42)', 'Added interface types: vlanMajorInterface(34), vlanSubInterface(35), cbfInterface(36)', 'Added interface types: multilinkFrameRelayInterface(29), ipTunnelInterface(30), serverPortInterface(31), smdsInterface(32)', 'Added interface type: sonetVTInterface(33)', 'Added interface types: l2tpSessionInterface(21), mlPppLinkInterface(22), l2tpDestinationInterface(24), mplsMajorInterface(25), mplsMinorInterface(26), mlPppNetworkInterface(27), ethernetSubInterface(28)', 'Added interface types: bridgedEthernet(19), l2TpTunnelInterface(20), slepInterface(23)', 'Added interface types: pppoe(17), pppoeSubInterface(18)', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdIfMIB.setLastUpdated('200103281512Z')
if mibBuilder.loadTexts: usdIfMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdIfMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdIfMIB.setDescription('The Generic Interfaces MIB for the Unisphere Networks Inc. enterprise.')
usdInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1))
usdIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1))
class UsdIfType(TextualConvention, Integer32):
    description = 'Interface type identification for physical-, link-, and network-layer interfaces.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18), ("bridgedEthernet", 19), ("l2tpTunnelInterface", 20), ("l2tpSessionInterface", 21), ("mlPppLinkInterface", 22), ("slepInterface", 23), ("l2tpDestinationInterface", 24), ("mplsMajorInterface", 25), ("mplsMinorInterface", 26), ("mlPppNetworkInterface", 27), ("ethernetSubInterface", 28), ("multilinkFrameRelayInterface", 29), ("ipTunnelInterface", 30), ("serverPortInterface", 31), ("smdsInterface", 32), ("sonetVTInterface", 33), ("vlanMajorInterface", 34), ("vlanSubInterface", 35), ("cbfInterface", 36), ("gtpInterface", 37), ("smdsMajorInterface", 38), ("smdsSubInterface", 39), ("l2fTunnelInterface", 40), ("l2fSessionInterface", 41), ("l2fDestinationInterface", 42), ("ipsecInterface", 43), ("sgInterface", 44), ("lacGenInterface", 47))

usdIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1))
usdIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: usdIfTable.setStatus('current')
if mibBuilder.loadTexts: usdIfTable.setDescription('This table contains a corresponding entry for each entry found in the standard Generic Interfaces MIB ifTable/ifXTable. The entries in this table contain supplementary generic interface characteristics. Entries in ifTable/ifXTable and in this table are created/deleted as a consequence of hardware detection, or of management configuration via standard or enterprise type-specific interface MIBs.')
usdIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("Unisphere-Data-IF-MIB", "usdIfEntry"))
usdIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: usdIfEntry.setStatus('current')
if mibBuilder.loadTexts: usdIfEntry.setDescription("An entry representing an interface's enterprise-defined generic interface characteristics.")
usdIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1), UsdIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIfType.setStatus('current')
if mibBuilder.loadTexts: usdIfType.setDescription('Identifies the type of this interface.')
usdIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: usdIfInvStackTable.setStatus('current')
if mibBuilder.loadTexts: usdIfInvStackTable.setDescription("A table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'underneath' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs underneath the sub-layer with ifIndex value y, then this table contains: usdIfInvStackStatus.x.y=active For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I. For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer. (If I is not involved in multiplexing, then these are the only two rows associated with I.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifStackStatus.x.0=active ifStackStatus.0.x=active This table contains exactly the same number of rows as the ifStackTable, but the rows appear in a different order.")
usdIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: usdIfInvStackEntry.setStatus('current')
if mibBuilder.loadTexts: usdIfInvStackEntry.setDescription('Information on a particular relationship between two sub-layers, specifying that one sub-layer runs underneath the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.')
usdIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIfInvStackStatus.setStatus('current')
if mibBuilder.loadTexts: usdIfInvStackStatus.setDescription('The status of the relationship between two sub-layers. An instance of this object exists for each instance of the ifStackStatus object, and vice versa. For example, if the variable ifStackStatus.H.L exists, then the variable usdIfInvStackStatus.L.H must also exist, and vice versa. In addition, the two variables always have the same value. However, unlike ifStackStatus, the usdIfInvStackStatus object is NOT write-able. A network management application wishing to change a relationship between sub-layers H and L cannot do so by modifying the value of usdIfInvStackStatus.L.H, but must instead modify the value of ifStackStatus.H.L. After the ifStackTable is modified, the change will be reflected in this table.')
usdIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4))
usdIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1))
usdIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2))
usdIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)).setObjects(("Unisphere-Data-IF-MIB", "usdIfGroup"), ("Unisphere-Data-IF-MIB", "usdIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIfCompliance = usdIfCompliance.setStatus('current')
if mibBuilder.loadTexts: usdIfCompliance.setDescription('The compliance statement for entities which implement the Unisphere Generic Interfaces MIB.')
usdIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)).setObjects(("Unisphere-Data-IF-MIB", "usdIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIfGroup = usdIfGroup.setStatus('current')
if mibBuilder.loadTexts: usdIfGroup.setDescription('A collection of objects for managing generic interfaces in a Unisphere product.')
usdIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)).setObjects(("Unisphere-Data-IF-MIB", "usdIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIfInvStackGroup = usdIfInvStackGroup.setStatus('current')
if mibBuilder.loadTexts: usdIfInvStackGroup.setDescription('A collection of objects providing inverted information on the layering of MIB-II interfaces.')
mibBuilder.exportSymbols("Unisphere-Data-IF-MIB", usdIfMIB=usdIfMIB, usdIf=usdIf, usdIfCompliances=usdIfCompliances, usdIfTable=usdIfTable, usdIfGroups=usdIfGroups, usdIfType=usdIfType, usdIfObjects=usdIfObjects, usdIfInvStackEntry=usdIfInvStackEntry, usdIfInvStackGroup=usdIfInvStackGroup, usdInterfaces=usdInterfaces, usdIfInvStackTable=usdIfInvStackTable, usdIfInvStackStatus=usdIfInvStackStatus, usdIfConformance=usdIfConformance, UsdIfType=UsdIfType, usdIfGroup=usdIfGroup, usdIfCompliance=usdIfCompliance, PYSNMP_MODULE_ID=usdIfMIB, usdIfEntry=usdIfEntry)
