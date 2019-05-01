#
# PySNMP MIB module IF-INVERTED-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IF-INVERTED-STACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:53:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ifStackLowerLayer, ifStackHigherLayer, ifStackGroup2 = mibBuilder.importSymbols("IF-MIB", "ifStackLowerLayer", "ifStackHigherLayer", "ifStackGroup2")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, iso, Counter32, TimeTicks, ModuleIdentity, Integer32, Gauge32, Counter64, Unsigned32, MibIdentifier, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "iso", "Counter32", "TimeTicks", "ModuleIdentity", "Integer32", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "mib-2", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ifInvertedStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 77))
ifInvertedStackMIB.setRevisions(('2000-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ifInvertedStackMIB.setRevisionsDescriptions(('Initial revision, published as RFC 2864',))
if mibBuilder.loadTexts: ifInvertedStackMIB.setLastUpdated('200006140000Z')
if mibBuilder.loadTexts: ifInvertedStackMIB.setOrganization('IETF Interfaces MIB Working Group')
if mibBuilder.loadTexts: ifInvertedStackMIB.setContactInfo(' Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 US 408-526-5260 kzm@cisco.com')
if mibBuilder.loadTexts: ifInvertedStackMIB.setDescription('The MIB module which provides the Inverted Stack Table for interface sub-layers.')
ifInvMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1))
ifInvStackTable = MibTable((1, 3, 6, 1, 2, 1, 77, 1, 1), )
if mibBuilder.loadTexts: ifInvStackTable.setReference('ifStackTable of RFC 2863')
if mibBuilder.loadTexts: ifInvStackTable.setStatus('current')
if mibBuilder.loadTexts: ifInvStackTable.setDescription("A table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'underneath' which other sub-layers, where each sub-layer corresponds to a conceptual row in the ifTable. For example, when the sub-layer with ifIndex value x runs underneath the sub-layer with ifIndex value y, then this table contains: ifInvStackStatus.x.y=active For each ifIndex value, z, which identifies an active interface, there are always at least two instantiated rows in this table associated with z. For one of these rows, z is the value of ifStackHigherLayer; for the other, z is the value of ifStackLowerLayer. (If z is not involved in multiplexing, then these are the only two rows associated with z.) For example, two rows exist even for an interface which has no others stacked on top or below it: ifInvStackStatus.z.0=active ifInvStackStatus.0.z=active This table contains exactly the same number of rows as the ifStackTable, but the rows appear in a different order.")
ifInvStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 77, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvStackEntry.setStatus('current')
if mibBuilder.loadTexts: ifInvStackEntry.setDescription('Information on a particular relationship between two sub- layers, specifying that one sub-layer runs underneath the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.')
ifInvStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvStackStatus.setStatus('current')
if mibBuilder.loadTexts: ifInvStackStatus.setDescription('The status of the relationship between two sub-layers. An instance of this object exists for each instance of the ifStackStatus object, and vice versa. For example, if the variable ifStackStatus.H.L exists, then the variable ifInvStackStatus.L.H must also exist, and vice versa. In addition, the two variables always have the same value. However, unlike ifStackStatus, the ifInvStackStatus object is NOT write-able. A network management application wishing to change a relationship between sub-layers H and L cannot do so by modifying the value of ifInvStackStatus.L.H, but must instead modify the value of ifStackStatus.H.L. After the ifStackTable is modified, the change will be reflected in this table.')
ifInvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2))
ifInvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 1))
ifInvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 2))
ifInvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"), ("IF-MIB", "ifStackGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvCompliance = ifInvCompliance.setStatus('current')
if mibBuilder.loadTexts: ifInvCompliance.setDescription('The compliance statement for SNMP entities which provide inverted information on the layering of network interfaces.')
ifInvStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvStackGroup = ifInvStackGroup.setStatus('current')
if mibBuilder.loadTexts: ifInvStackGroup.setDescription('A collection of objects providing inverted information on the layering of MIB-II interfaces.')
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", ifInvStackEntry=ifInvStackEntry, PYSNMP_MODULE_ID=ifInvertedStackMIB, ifInvCompliances=ifInvCompliances, ifInvStackStatus=ifInvStackStatus, ifInvCompliance=ifInvCompliance, ifInvertedStackMIB=ifInvertedStackMIB, ifInvStackGroup=ifInvStackGroup, ifInvGroups=ifInvGroups, ifInvConformance=ifInvConformance, ifInvMIBObjects=ifInvMIBObjects, ifInvStackTable=ifInvStackTable)
