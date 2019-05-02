#
# PySNMP MIB module Juniper-UNI-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-UNI-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifStackLowerLayer, ifEntry, ifStackHigherLayer = mibBuilder.importSymbols("IF-MIB", "ifStackLowerLayer", "ifEntry", "ifStackHigherLayer")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, TimeTicks, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Unsigned32, ObjectIdentity, NotificationType, Bits, Integer32, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "NotificationType", "Bits", "Integer32", "Gauge32", "Counter32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
juniIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3))
juniIfMIB.setRevisions(('2005-10-11 20:40', '2003-07-16 21:40', '2003-02-06 15:57', '2002-01-22 16:52', '2001-03-28 15:12', '2000-11-22 23:41', '2000-09-29 18:35', '2000-07-27 15:45', '2000-05-05 15:08', '1999-12-21 15:18', '1999-09-03 14:16', '1998-11-13 20:19',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIfMIB.setRevisionsDescriptions(('Added interface type: plsL2ShimInterface(45) ', 'Added interface type: atmActiveSubInterface(257) ', 'Replaced Unisphere names with Juniper names. Added interface types: bridgeInterface(48), ipsecTransportInterface(49), ipv6Interface(50), ipv6TunnelInterface(51), ipv6Loopback(52), osi(53), atmVirtualCircuit(145), pppLink(256) ', 'Added interface types: gtpInterface(37), smdsMajorInterface(38), smdsSubInterface(39), ipsecInterface(43), sgInterface(44), lacGenInterface(47) ', 'Added interface types: l2fTunnelInterface(40), l2fSessionInterface(41), l2fDestinationInterface(42) ', 'Added interface types: vlanMajorInterface(34), vlanSubInterface(35), cbfInterface(36) ', 'Added interface types: multilinkFrameRelayInterface(29), ipTunnelInterface(30), serverPortInterface(31), smdsInterface(32) ', 'Added interface type: sonetVTInterface(33) ', 'Added interface types: l2tpSessionInterface(21), mlPppLinkInterface(22), l2tpDestinationInterface(24), mplsMajorInterface(25), mplsMinorInterface(26), mlPppNetworkInterface(27), ethernetSubInterface(28) ', 'Added interface types: bridgedEthernet(19), l2TpTunnelInterface(20), slepInterface(23) ', 'Added interface types: pppoe(17), pppoeSubInterface(18) ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniIfMIB.setLastUpdated('200510112040Z')
if mibBuilder.loadTexts: juniIfMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIfMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIfMIB.setDescription('The Generic Interfaces MIB for the Juniper Networks enterprise.')
class JuniIfType(TextualConvention, Integer32):
    description = 'Interface type identification for physical-, link-, and network-layer interfaces.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 145, 256, 257))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18), ("bridgedEthernet", 19), ("l2tpTunnelInterface", 20), ("l2tpSessionInterface", 21), ("mlPppLinkInterface", 22), ("slepInterface", 23), ("l2tpDestinationInterface", 24), ("mplsMajorInterface", 25), ("mplsMinorInterface", 26), ("mlPppNetworkInterface", 27), ("ethernetSubInterface", 28), ("multilinkFrameRelayInterface", 29), ("ipTunnelInterface", 30), ("serverPortInterface", 31), ("smdsInterface", 32), ("sonetVTInterface", 33), ("vlanMajorInterface", 34), ("vlanSubInterface", 35), ("cbfInterface", 36), ("gtpInterface", 37), ("smdsMajorInterface", 38), ("smdsSubInterface", 39), ("l2fTunnelInterface", 40), ("l2fSessionInterface", 41), ("l2fDestinationInterface", 42), ("ipsecInterface", 43), ("sgInterface", 44), ("mplsL2ShimInterface", 45), ("lacGenInterface", 47), ("bridgeInterface", 48), ("ipsecTransportInterface", 49), ("ipv6Interface", 50), ("ipv6TunnelInterface", 51), ("ipv6Loopback", 52), ("osi", 53), ("lag", 54), ("ipTunnelMdt", 55), ("atmVirtualCircuit", 145), ("pppLink", 256), ("atmActiveSubInterface", 257))

juniInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1))
juniIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1))
juniIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1))
juniIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: juniIfTable.setStatus('current')
if mibBuilder.loadTexts: juniIfTable.setDescription('This table contains a corresponding entry for each entry found in the standard Generic Interfaces MIB ifTable/ifXTable. The entries in this table contain supplementary generic interface characteristics. Entries in ifTable/ifXTable and in this table are created/deleted as a consequence of hardware detection, or of management configuration via standard or enterprise type-specific interface MIBs.')
juniIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("Juniper-UNI-IF-MIB", "juniIfEntry"))
juniIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: juniIfEntry.setStatus('current')
if mibBuilder.loadTexts: juniIfEntry.setDescription("An entry representing an interface's enterprise-defined generic interface characteristics.")
juniIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1), JuniIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfType.setStatus('current')
if mibBuilder.loadTexts: juniIfType.setDescription('Identifies the type of this interface.')
juniIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: juniIfInvStackTable.setStatus('current')
if mibBuilder.loadTexts: juniIfInvStackTable.setDescription("A table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'underneath' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs underneath the sub-layer with ifIndex value y, then this table contains: juniIfInvStackStatus.x.y = active For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I. For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer. (If I is not involved in multiplexing, then these are the only two rows associated with I.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifStackStatus.x.0 = active ifStackStatus.0.x = active This table contains exactly the same number of rows as the ifStackTable, but the rows appear in a different order.")
juniIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: juniIfInvStackEntry.setStatus('current')
if mibBuilder.loadTexts: juniIfInvStackEntry.setDescription('Information on a particular relationship between two sub-layers, specifying that one sub-layer runs underneath the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.')
juniIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfInvStackStatus.setStatus('current')
if mibBuilder.loadTexts: juniIfInvStackStatus.setDescription('The status of the relationship between two sub-layers. An instance of this object exists for each instance of the ifStackStatus object, and vice versa. For example, if the variable ifStackStatus.H.L exists, then the variable juniIfInvStackStatus.L.H must also exist, and vice versa. In addition, the two variables always have the same value. However, unlike ifStackStatus, the juniIfInvStackStatus object is NOT write-able. A network management application wishing to change a relationship between sub-layers H and L cannot do so by modifying the value of juniIfInvStackStatus.L.H, but must instead modify the value of ifStackStatus.H.L. After the ifStackTable is modified, the change will be reflected in this table.')
juniIfCountTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3), )
if mibBuilder.loadTexts: juniIfCountTable.setStatus('current')
if mibBuilder.loadTexts: juniIfCountTable.setDescription("This table contains entries for each interface type's system wide interfaces counts.")
juniIfCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-UNI-IF-MIB", "juniIfCountIfType"))
if mibBuilder.loadTexts: juniIfCountEntry.setStatus('current')
if mibBuilder.loadTexts: juniIfCountEntry.setDescription('An entry represents system wide total number of interfaces configured for the particular interface type.')
juniIfCountIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 1), JuniIfType())
if mibBuilder.loadTexts: juniIfCountIfType.setStatus('current')
if mibBuilder.loadTexts: juniIfCountIfType.setDescription('Identifies the type of this interface.')
juniIfCountNumberOfInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfCountNumberOfInterfaces.setStatus('current')
if mibBuilder.loadTexts: juniIfCountNumberOfInterfaces.setDescription('Represents system wide total number of interfaces configured for the particular interface type.')
juniIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4))
juniIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1))
juniIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2))
juniIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)).setObjects(("Juniper-UNI-IF-MIB", "juniIfGroup"), ("Juniper-UNI-IF-MIB", "juniIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCompliance = juniIfCompliance.setStatus('current')
if mibBuilder.loadTexts: juniIfCompliance.setDescription('Obsolete compliance statement for entities which implement the Juniper Generic Interfaces MIB.')
juniIfCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 2)).setObjects(("Juniper-UNI-IF-MIB", "juniIfGroup"), ("Juniper-UNI-IF-MIB", "juniIfInvStackGroup"), ("Juniper-UNI-IF-MIB", "juniIfCountGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCompliance1 = juniIfCompliance1.setStatus('current')
if mibBuilder.loadTexts: juniIfCompliance1.setDescription('The compliance statement for entities which implement the Juniper Generic Interfaces MIB.')
juniIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)).setObjects(("Juniper-UNI-IF-MIB", "juniIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfGroup = juniIfGroup.setStatus('current')
if mibBuilder.loadTexts: juniIfGroup.setDescription('A collection of objects for managing generic interfaces in a Juniper product.')
juniIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)).setObjects(("Juniper-UNI-IF-MIB", "juniIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfInvStackGroup = juniIfInvStackGroup.setStatus('current')
if mibBuilder.loadTexts: juniIfInvStackGroup.setDescription('A collection of objects providing inverted information on the layering of MIB-II interfaces.')
juniIfCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 3)).setObjects(("Juniper-UNI-IF-MIB", "juniIfCountNumberOfInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCountGroup = juniIfCountGroup.setStatus('current')
if mibBuilder.loadTexts: juniIfCountGroup.setDescription('A collection of objects providing interface information on the system wide count of number of interfaces per interface type.')
mibBuilder.exportSymbols("Juniper-UNI-IF-MIB", juniIfMIB=juniIfMIB, juniIfGroups=juniIfGroups, juniIfConformance=juniIfConformance, juniIfCountNumberOfInterfaces=juniIfCountNumberOfInterfaces, juniIfCountTable=juniIfCountTable, juniIfCountEntry=juniIfCountEntry, PYSNMP_MODULE_ID=juniIfMIB, juniIfType=juniIfType, juniInterfaces=juniInterfaces, juniIfInvStackStatus=juniIfInvStackStatus, juniIfCountGroup=juniIfCountGroup, juniIfInvStackEntry=juniIfInvStackEntry, juniIfGroup=juniIfGroup, juniIfEntry=juniIfEntry, juniIfCompliance=juniIfCompliance, JuniIfType=JuniIfType, juniIfCountIfType=juniIfCountIfType, juniIfCompliances=juniIfCompliances, juniIfInvStackGroup=juniIfInvStackGroup, juniIf=juniIf, juniIfCompliance1=juniIfCompliance1, juniIfTable=juniIfTable, juniIfObjects=juniIfObjects, juniIfInvStackTable=juniIfInvStackTable)
