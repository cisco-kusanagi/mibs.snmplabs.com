#
# PySNMP MIB module REDSTONE-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifStackHigherLayer, ifEntry, ifStackLowerLayer = mibBuilder.importSymbols("IF-MIB", "ifStackHigherLayer", "ifEntry", "ifStackLowerLayer")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, ObjectIdentity, Integer32, iso, TimeTicks, Gauge32, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32", "iso", "TimeTicks", "Gauge32", "Counter64", "Unsigned32", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rsIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 3))
rsIfMIB.setRevisions(('1998-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsIfMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: rsIfMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsIfMIB.setOrganization('Redstone Communications, Inc.')
if mibBuilder.loadTexts: rsIfMIB.setContactInfo(' Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA Tel: +1-978-692-1999 Email: mib@redstonecom.com ')
if mibBuilder.loadTexts: rsIfMIB.setDescription('The Generic Interfaces MIB for the Redstone Communications Inc. enterprise.')
rsInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1))
rsIf = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1))
class RsIfType(TextualConvention, Integer32):
    description = 'Interface type identification for physical-, link-, and network-layer interfaces.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18))

rsIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1))
rsIfTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: rsIfTable.setStatus('current')
if mibBuilder.loadTexts: rsIfTable.setDescription('This table contains a corresponding entry for each entry found in the standard Generic Interfaces MIB ifTable/ifXTable. The entries in this table contain supplementary generic interface characteristics. Entries in ifTable/ifXTable and in this table are created/deleted as a consequence of hardware detection, or of management configuration via standard or enterprise type-specific interface MIBs.')
rsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("REDSTONE-IF-MIB", "rsIfEntry"))
rsIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: rsIfEntry.setStatus('current')
if mibBuilder.loadTexts: rsIfEntry.setDescription("An entry representing an interface's enterprise-defined generic interface characteristics.")
rsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1, 1, 1), RsIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfType.setStatus('current')
if mibBuilder.loadTexts: rsIfType.setDescription('Identifies the type of this interface.')
rsIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: rsIfInvStackTable.setStatus('current')
if mibBuilder.loadTexts: rsIfInvStackTable.setDescription("A table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'underneath' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs underneath the sub-layer with ifIndex value y, then this table contains: rsIfInvStackStatus.x.y=active For each ifIndex value, I, which identifies an active interface, there are always at least two instantiated rows in this table associated with I. For one of these rows, I is the value of ifStackHigherLayer; for the other, I is the value of ifStackLowerLayer. (If I is not involved in multiplexing, then these are the only two rows associated with I.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifStackStatus.x.0=active ifStackStatus.0.x=active This table contains exactly the same number of rows as the ifStackTable, but the rows appear in a different order.")
rsIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: rsIfInvStackEntry.setStatus('current')
if mibBuilder.loadTexts: rsIfInvStackEntry.setDescription('Information on a particular relationship between two sub- layers, specifying that one sub-layer runs underneath the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.')
rsIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInvStackStatus.setStatus('current')
if mibBuilder.loadTexts: rsIfInvStackStatus.setDescription('The status of the relationship between two sub-layers. An instance of this object exists for each instance of the ifStackStatus object, and vice versa. For example, if the variable ifStackStatus.H.L exists, then the variable rsIfInvStackStatus.L.H must also exist, and vice versa. In addition, the two variables always have the same value. However, unlike ifStackStatus, the rsIfInvStackStatus object is NOT write-able. A network management application wishing to change a relationship between sub-layers H and L cannot do so by modifying the value of rsIfInvStackStatus.L.H, but must instead modify the value of ifStackStatus.H.L. After the ifStackTable is modified, the change will be reflected in this table.')
rsIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4))
rsIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 1))
rsIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2))
rsIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 1, 1)).setObjects(("REDSTONE-IF-MIB", "rsIfGroup"), ("REDSTONE-IF-MIB", "rsIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfCompliance = rsIfCompliance.setStatus('current')
if mibBuilder.loadTexts: rsIfCompliance.setDescription('The compliance statement for entities which implement the Redstone Generic Interfaces MIB.')
rsIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2, 1)).setObjects(("REDSTONE-IF-MIB", "rsIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfGroup = rsIfGroup.setStatus('current')
if mibBuilder.loadTexts: rsIfGroup.setDescription('A collection of objects providing management capability capability of generic interfaces in a Redstone product.')
rsIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2, 2)).setObjects(("REDSTONE-IF-MIB", "rsIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfInvStackGroup = rsIfInvStackGroup.setStatus('current')
if mibBuilder.loadTexts: rsIfInvStackGroup.setDescription('A collection of objects providing inverted information on the layering of MIB-II interfaces.')
mibBuilder.exportSymbols("REDSTONE-IF-MIB", rsIfGroups=rsIfGroups, rsIfEntry=rsIfEntry, rsIfInvStackStatus=rsIfInvStackStatus, rsIfConformance=rsIfConformance, rsIfMIB=rsIfMIB, rsInterfaces=rsInterfaces, rsIfInvStackGroup=rsIfInvStackGroup, rsIfInvStackEntry=rsIfInvStackEntry, rsIfGroup=rsIfGroup, rsIfType=rsIfType, RsIfType=RsIfType, rsIfTable=rsIfTable, PYSNMP_MODULE_ID=rsIfMIB, rsIfCompliances=rsIfCompliances, rsIfObjects=rsIfObjects, rsIfCompliance=rsIfCompliance, rsIfInvStackTable=rsIfInvStackTable, rsIf=rsIf)
