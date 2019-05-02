#
# PySNMP MIB module ARISTA-NEXTHOP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-NEXTHOP-GROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Gauge32, IpAddress, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Counter32, TimeTicks, ObjectIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Counter32", "TimeTicks", "ObjectIdentity", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaNexthopGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 21))
aristaNexthopGroupMIB.setRevisions(('2016-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaNexthopGroupMIB.setRevisionsDescriptions(('Initial revision of the MIB module.',))
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setLastUpdated('201604170000Z')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setDescription("This MIB contains information about NextHop Groups (NHG). General L3 routing creates routing table entries, each of which are associated with a nexthop. If multiple paths exist for a specific route, the route points to a set of nexthops (commonly referred as ECMP or Equal Cost MultiPath). Arista devices support a feature which allows customers to manually create a nexthop list, and use this list to route packets to the specified set of nexthop addresses. Customers can associate a tunnel type (GRE, for example) with the nexthop group, allowing relevant packets to be tunneled as well. The packet forwarding or routing decision happens in hardware. Nexthop group feature gives customers full control of how a route should be forwarded (tunneled or otherwise). The number of entries in the nexthop group is also determined by the user, and directly translates to the number of nexthop entries in the hardware for the specified route. Let's provide an example, looking at EOS CLI example. nexthop-group foo type ip-in-ip ttl 64 entry 0 tunnel-destination 10.1.1.1 entry 1 tunnel-destination 20.1.1.1 ! ip route 30.1.1.0/24 Nexthop-Group foo In the above configuration, any packet destined to 30.1.1.0/24 will be forwarded by the nexthop group 'foo'. Each entry inside the nexthop group specifies a particular nexthop ('tunnel destination') chosen by the customer. In this example, packets can be forwarded via either of the nexthop (traffic split equally between the 2 entries). This MIB module provides information relevant to the nexthop group feature, specifically the status of various nexthop groups configured, and traffic statistics.")
aristaNexthopGroupMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1))
aristaNexthopGroupMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2))
class NexthopGroupName(TextualConvention, OctetString):
    description = 'Each nexthop group configured by the user is associated with a name, by configuration.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NexthopGroupType(TextualConvention, Integer32):
    description = "A nexthop group is associated with a type, which determines the packet forwarding behavior. Type 'ip' refers to L3 IP routing. A route pointing to a nexthop group in this case is equivalent to multiple static route configuration entries each with a particular nexthop. Types 'gre', 'mpls', 'ip-in-ip' all refer to tunnel types. In this case a route pointing to the specified nexthop group is used to tunnel packets using the appropriate encapsulation to a tunnel destination. The encapsulation information depends on the tunnel type itself."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("ipInIp", 1), ("gre", 2), ("mpls", 3), ("ip", 4), ("mplsOverGre", 5))

aristaNexthopGroupTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1), )
if mibBuilder.loadTexts: aristaNexthopGroupTable.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupTable.setDescription('This table contains information about the nexthop groups that are present in the device.')
aristaNexthopGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1), ).setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"))
if mibBuilder.loadTexts: aristaNexthopGroupEntry.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupEntry.setDescription('A conceptual row, containing information for a specific nexthop group.')
aristaNexthopGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaNexthopGroupId.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupId.setDescription('Unique index identifying a nexthop group.')
aristaNexthopGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 2), NexthopGroupName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupName.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupName.setDescription('Unique name identifying a nexthop group.')
aristaNexthopGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 3), NexthopGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupType.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupType.setDescription('The type of the nexthop group. The encapsulation information provided for each entry in the nexthop group corresponds to the type.')
aristaNexthopGroupCounterTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2), )
if mibBuilder.loadTexts: aristaNexthopGroupCounterTable.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterTable.setDescription('Each nexthop group contains several entries - each entry specifies a particular nexthop through which a packet can be forwarded. There is packet and byte counter information associated with each such nexthop. This table represents the per nexthop counter information for every nexthop group.')
aristaNexthopGroupCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1), ).setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"), (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupEntryIndex"))
if mibBuilder.loadTexts: aristaNexthopGroupCounterEntry.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterEntry.setDescription('A conceptual row, containing counter information for every nexthop defined inside the nexthop group.')
aristaNexthopGroupEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaNexthopGroupEntryIndex.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupEntryIndex.setDescription("As described in the beginning of the MIB module each nexthop group can have multiple entries, one per 'destination' or 'nexthop'. Each entry within a nexthop group has a number or index as configured by the user. This MIB object represents the entry index within the nexthop group.")
aristaNexthopGroupCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterIndex.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterIndex.setDescription('For every nexthop within a nexthop group, packet and byte counters are maintained by the device. Counters can be shared by multiple such nexthops and the counter index will be the same for all of those nexthops.')
aristaNexthopGroupCounterPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterPacketCount.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterPacketCount.setDescription('The number of packets forwarded through the specific nexthop. Note that since counters are shared with multiple nexthops, the packet count is an aggregate of packets forwarded through all the relevant nexthops.')
aristaNexthopGroupCounterByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterByteCount.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterByteCount.setDescription('The byte count of packets forwarded through the specific nexthop. Note that since counters are shared with multiple nexthops, the byte count is an aggregate of packets forwarded through all the relevant nexthops.')
aristaNexthopGroupMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1))
aristaNexthopGroupMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2))
aristaNexthopGroupMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupGroup"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupMibCompliance = aristaNexthopGroupMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupMibCompliance.setDescription('The compliance statement for Arista switches that implement the ARISTA-NEXTHOP-GROUP-MIB.')
aristaNexthopGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupName"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupGroup = aristaNexthopGroupGroup.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupGroup.setDescription('The collection of objects that provide nexthop group information in the system.')
aristaNexthopGroupCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 2)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterIndex"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterPacketCount"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterByteCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupCounterGroup = aristaNexthopGroupCounterGroup.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterGroup.setDescription('The collection of objects that provide counter information for every nexthop in the nexthop group.')
mibBuilder.exportSymbols("ARISTA-NEXTHOP-GROUP-MIB", aristaNexthopGroupMIB=aristaNexthopGroupMIB, PYSNMP_MODULE_ID=aristaNexthopGroupMIB, NexthopGroupName=NexthopGroupName, aristaNexthopGroupCounterIndex=aristaNexthopGroupCounterIndex, aristaNexthopGroupCounterTable=aristaNexthopGroupCounterTable, aristaNexthopGroupMibGroups=aristaNexthopGroupMibGroups, aristaNexthopGroupEntry=aristaNexthopGroupEntry, aristaNexthopGroupType=aristaNexthopGroupType, aristaNexthopGroupCounterByteCount=aristaNexthopGroupCounterByteCount, aristaNexthopGroupEntryIndex=aristaNexthopGroupEntryIndex, aristaNexthopGroupMibCompliances=aristaNexthopGroupMibCompliances, aristaNexthopGroupMibObjects=aristaNexthopGroupMibObjects, aristaNexthopGroupMibCompliance=aristaNexthopGroupMibCompliance, aristaNexthopGroupId=aristaNexthopGroupId, aristaNexthopGroupName=aristaNexthopGroupName, aristaNexthopGroupCounterGroup=aristaNexthopGroupCounterGroup, NexthopGroupType=NexthopGroupType, aristaNexthopGroupGroup=aristaNexthopGroupGroup, aristaNexthopGroupCounterEntry=aristaNexthopGroupCounterEntry, aristaNexthopGroupTable=aristaNexthopGroupTable, aristaNexthopGroupCounterPacketCount=aristaNexthopGroupCounterPacketCount, aristaNexthopGroupMibConformance=aristaNexthopGroupMibConformance)
