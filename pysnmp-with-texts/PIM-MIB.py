#
# PySNMP MIB module PIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PIM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ipMRouteSource, ipMRouteNextHopSource, ipMRouteNextHopIfIndex, ipMRouteGroup, ipMRouteNextHopAddress, ipMRouteNextHopSourceMask, ipMRouteSourceMask, ipMRouteNextHopGroup = mibBuilder.importSymbols("IPMROUTE-STD-MIB", "ipMRouteSource", "ipMRouteNextHopSource", "ipMRouteNextHopIfIndex", "ipMRouteGroup", "ipMRouteNextHopAddress", "ipMRouteNextHopSourceMask", "ipMRouteSourceMask", "ipMRouteNextHopGroup")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Counter32, ModuleIdentity, TimeTicks, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, iso, experimental, Unsigned32, NotificationType, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "iso", "experimental", "Unsigned32", "NotificationType", "Bits", "Gauge32")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
pimMIB = ModuleIdentity((1, 3, 6, 1, 3, 61))
pimMIB.setRevisions(('2000-09-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pimMIB.setRevisionsDescriptions(('Initial version, published as RFC 2934.',))
if mibBuilder.loadTexts: pimMIB.setLastUpdated('200009280000Z')
if mibBuilder.loadTexts: pimMIB.setOrganization('IETF IDMR Working Group.')
if mibBuilder.loadTexts: pimMIB.setContactInfo(' Dave Thaler Microsoft Corporation One Microsoft Way Redmond, WA 98052-6399 US Phone: +1 425 703 8835 EMail: dthaler@microsoft.com')
if mibBuilder.loadTexts: pimMIB.setDescription('The MIB module for management of PIM routers.')
pimMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 61, 1))
pimTraps = MibIdentifier((1, 3, 6, 1, 3, 61, 1, 0))
pim = MibIdentifier((1, 3, 6, 1, 3, 61, 1, 1))
pimJoinPruneInterval = MibScalar((1, 3, 6, 1, 3, 61, 1, 1, 1), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pimJoinPruneInterval.setStatus('current')
if mibBuilder.loadTexts: pimJoinPruneInterval.setDescription('The default interval at which periodic PIM-SM Join/Prune messages are to be sent.')
pimInterfaceTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 2), )
if mibBuilder.loadTexts: pimInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceTable.setDescription("The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table.")
pimInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 2, 1), ).setIndexNames((0, "PIM-MIB", "pimInterfaceIfIndex"))
if mibBuilder.loadTexts: pimInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceEntry.setDescription('An entry (conceptual row) in the pimInterfaceTable.')
pimInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pimInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceIfIndex.setDescription('The ifIndex value of this PIM interface.')
pimInterfaceAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimInterfaceAddress.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceAddress.setDescription('The IP address of the PIM interface.')
pimInterfaceNetMask = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimInterfaceNetMask.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceNetMask.setDescription('The network mask for the IP address of the PIM interface.')
pimInterfaceMode = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dense", 1), ("sparse", 2), ("sparseDense", 3))).clone('dense')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceMode.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceMode.setDescription('The configured mode of this PIM interface. A value of sparseDense is only valid for PIMv1.')
pimInterfaceDR = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimInterfaceDR.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceDR.setDescription('The Designated Router on this PIM interface. For point-to- point interfaces, this object has the value 0.0.0.0.')
pimInterfaceHelloInterval = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 6), Integer32().clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceHelloInterval.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceHelloInterval.setDescription('The frequency at which PIM Hello messages are transmitted on this interface.')
pimInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceStatus.setDescription('The status of this entry. Creating the entry enables PIM on the interface; destroying the entry disables PIM on the interface.')
pimInterfaceJoinPruneInterval = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 8), Integer32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceJoinPruneInterval.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceJoinPruneInterval.setDescription('The frequency at which PIM Join/Prune messages are transmitted on this PIM interface. The default value of this object is the pimJoinPruneInterval.')
pimInterfaceCBSRPreference = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceCBSRPreference.setStatus('current')
if mibBuilder.loadTexts: pimInterfaceCBSRPreference.setDescription('The preference value for the local interface as a candidate bootstrap router. The value of -1 is used to indicate that the local interface is not a candidate BSR interface.')
pimNeighborTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 3), )
if mibBuilder.loadTexts: pimNeighborTable.setStatus('current')
if mibBuilder.loadTexts: pimNeighborTable.setDescription("The (conceptual) table listing the router's PIM neighbors.")
pimNeighborEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 3, 1), ).setIndexNames((0, "PIM-MIB", "pimNeighborAddress"))
if mibBuilder.loadTexts: pimNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: pimNeighborEntry.setDescription('An entry (conceptual row) in the pimNeighborTable.')
pimNeighborAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: pimNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: pimNeighborAddress.setDescription('The IP address of the PIM neighbor for which this entry contains information.')
pimNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborIfIndex.setStatus('current')
if mibBuilder.loadTexts: pimNeighborIfIndex.setDescription('The value of ifIndex for the interface used to reach this PIM neighbor.')
pimNeighborUpTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborUpTime.setStatus('current')
if mibBuilder.loadTexts: pimNeighborUpTime.setDescription('The time since this PIM neighbor (last) became a neighbor of the local router.')
pimNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborExpiryTime.setStatus('current')
if mibBuilder.loadTexts: pimNeighborExpiryTime.setDescription('The minimum time remaining before this PIM neighbor will be aged out.')
pimNeighborMode = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dense", 1), ("sparse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborMode.setStatus('deprecated')
if mibBuilder.loadTexts: pimNeighborMode.setDescription('The active PIM mode of this neighbor. This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface.')
pimIpMRouteTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 4), )
if mibBuilder.loadTexts: pimIpMRouteTable.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteTable.setDescription('The (conceptual) table listing PIM-specific information on a subset of the rows of the ipMRouteTable defined in the IP Multicast MIB.')
pimIpMRouteEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 4, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"))
if mibBuilder.loadTexts: pimIpMRouteEntry.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteEntry.setDescription('An entry (conceptual row) in the pimIpMRouteTable. There is one entry per entry in the ipMRouteTable whose incoming interface is running PIM.')
pimIpMRouteUpstreamAssertTimer = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteUpstreamAssertTimer.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteUpstreamAssertTimer.setDescription('The time remaining before the router changes its upstream neighbor back to its RPF neighbor. This timer is called the Assert timer in the PIM Sparse and Dense mode specification. A value of 0 indicates that no Assert has changed the upstream neighbor away from the RPF neighbor.')
pimIpMRouteAssertMetric = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteAssertMetric.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteAssertMetric.setDescription('The metric advertised by the assert winner on the upstream interface, or 0 if no such assert is in received.')
pimIpMRouteAssertMetricPref = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteAssertMetricPref.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteAssertMetricPref.setDescription('The preference advertised by the assert winner on the upstream interface, or 0 if no such assert is in effect.')
pimIpMRouteAssertRPTBit = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteAssertRPTBit.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteAssertRPTBit.setDescription('The value of the RPT-bit advertised by the assert winner on the upstream interface, or false if no such assert is in effect.')
pimIpMRouteFlags = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 5), Bits().clone(namedValues=NamedValues(("rpt", 0), ("spt", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteFlags.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteFlags.setDescription('This object describes PIM-specific flags related to a multicast state entry. See the PIM Sparse Mode specification for the meaning of the RPT and SPT bits.')
pimIpMRouteNextHopTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 7), )
if mibBuilder.loadTexts: pimIpMRouteNextHopTable.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteNextHopTable.setDescription('The (conceptual) table listing PIM-specific information on a subset of the rows of the ipMRouteNextHopTable defined in the IP Multicast MIB.')
pimIpMRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 7, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"))
if mibBuilder.loadTexts: pimIpMRouteNextHopEntry.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteNextHopEntry.setDescription('An entry (conceptual row) in the pimIpMRouteNextHopTable. There is one entry per entry in the ipMRouteNextHopTable whose interface is running PIM and whose ipMRouteNextHopState is pruned(1).')
pimIpMRouteNextHopPruneReason = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("prune", 2), ("assert", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteNextHopPruneReason.setStatus('current')
if mibBuilder.loadTexts: pimIpMRouteNextHopPruneReason.setDescription('This object indicates why the downstream interface was pruned, whether in response to a PIM prune message or due to PIM Assert processing.')
pimRPTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 5), )
if mibBuilder.loadTexts: pimRPTable.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPTable.setDescription('The (conceptual) table listing PIM version 1 information for the Rendezvous Points (RPs) for IP multicast groups. This table is deprecated since its function is replaced by the pimRPSetTable for PIM version 2.')
pimRPEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 5, 1), ).setIndexNames((0, "PIM-MIB", "pimRPGroupAddress"), (0, "PIM-MIB", "pimRPAddress"))
if mibBuilder.loadTexts: pimRPEntry.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPEntry.setDescription('An entry (conceptual row) in the pimRPTable. There is one entry per RP address for each IP multicast group.')
pimRPGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: pimRPGroupAddress.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPGroupAddress.setDescription('The IP multicast group address for which this entry contains information about an RP.')
pimRPAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: pimRPAddress.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPAddress.setDescription('The unicast address of the RP.')
pimRPState = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPState.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPState.setDescription('The state of the RP.')
pimRPStateTimer = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPStateTimer.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPStateTimer.setDescription('The minimum time remaining before the next state change. When pimRPState is up, this is the minimum time which must expire until it can be declared down. When pimRPState is down, this is the time until it will be declared up (in order to retry).')
pimRPLastChange = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPLastChange.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPLastChange.setDescription('The value of sysUpTime at the time when the corresponding instance of pimRPState last changed its value.')
pimRPRowStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimRPRowStatus.setStatus('deprecated')
if mibBuilder.loadTexts: pimRPRowStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
pimRPSetTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 6), )
if mibBuilder.loadTexts: pimRPSetTable.setStatus('current')
if mibBuilder.loadTexts: pimRPSetTable.setDescription('The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate-RP-Advertisements. When the local router is not the BSR, this information is obtained from received RP-Set messages.')
pimRPSetEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 6, 1), ).setIndexNames((0, "PIM-MIB", "pimRPSetComponent"), (0, "PIM-MIB", "pimRPSetGroupAddress"), (0, "PIM-MIB", "pimRPSetGroupMask"), (0, "PIM-MIB", "pimRPSetAddress"))
if mibBuilder.loadTexts: pimRPSetEntry.setStatus('current')
if mibBuilder.loadTexts: pimRPSetEntry.setDescription('An entry (conceptual row) in the pimRPSetTable.')
pimRPSetGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: pimRPSetGroupAddress.setStatus('current')
if mibBuilder.loadTexts: pimRPSetGroupAddress.setDescription('The IP multicast group address which, when combined with pimRPSetGroupMask, gives the group prefix for which this entry contains information about the Candidate-RP.')
pimRPSetGroupMask = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: pimRPSetGroupMask.setStatus('current')
if mibBuilder.loadTexts: pimRPSetGroupMask.setDescription('The multicast group address mask which, when combined with pimRPSetGroupAddress, gives the group prefix for which this entry contains information about the Candidate-RP.')
pimRPSetAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: pimRPSetAddress.setStatus('current')
if mibBuilder.loadTexts: pimRPSetAddress.setDescription('The IP address of the Candidate-RP.')
pimRPSetHoldTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPSetHoldTime.setStatus('current')
if mibBuilder.loadTexts: pimRPSetHoldTime.setDescription('The holdtime of a Candidate-RP. If the local router is not the BSR, this value is 0.')
pimRPSetExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPSetExpiryTime.setStatus('current')
if mibBuilder.loadTexts: pimRPSetExpiryTime.setDescription('The minimum time remaining before the Candidate-RP will be declared down. If the local router is not the BSR, this value is 0.')
pimRPSetComponent = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: pimRPSetComponent.setStatus('current')
if mibBuilder.loadTexts: pimRPSetComponent.setDescription(' A number uniquely identifying the component. Each protocol instance connected to a separate domain should have a different index value.')
pimCandidateRPTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 11), )
if mibBuilder.loadTexts: pimCandidateRPTable.setStatus('current')
if mibBuilder.loadTexts: pimCandidateRPTable.setDescription('The (conceptual) table listing the IP multicast groups for which the local router is to advertise itself as a Candidate-RP when the value of pimComponentCRPHoldTime is non-zero. If this table is empty, then the local router will advertise itself as a Candidate-RP for all groups (providing the value of pimComponentCRPHoldTime is non- zero).')
pimCandidateRPEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 11, 1), ).setIndexNames((0, "PIM-MIB", "pimCandidateRPGroupAddress"), (0, "PIM-MIB", "pimCandidateRPGroupMask"))
if mibBuilder.loadTexts: pimCandidateRPEntry.setStatus('current')
if mibBuilder.loadTexts: pimCandidateRPEntry.setDescription('An entry (conceptual row) in the pimCandidateRPTable.')
pimCandidateRPGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 1), IpAddress())
if mibBuilder.loadTexts: pimCandidateRPGroupAddress.setStatus('current')
if mibBuilder.loadTexts: pimCandidateRPGroupAddress.setDescription('The IP multicast group address which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate-RP.')
pimCandidateRPGroupMask = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 2), IpAddress())
if mibBuilder.loadTexts: pimCandidateRPGroupMask.setStatus('current')
if mibBuilder.loadTexts: pimCandidateRPGroupMask.setDescription('The multicast group address mask which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate-RP.')
pimCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimCandidateRPAddress.setStatus('current')
if mibBuilder.loadTexts: pimCandidateRPAddress.setDescription('The (unicast) address of the interface which will be advertised as a Candidate-RP.')
pimCandidateRPRowStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimCandidateRPRowStatus.setStatus('current')
if mibBuilder.loadTexts: pimCandidateRPRowStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
pimComponentTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 12), )
if mibBuilder.loadTexts: pimComponentTable.setStatus('current')
if mibBuilder.loadTexts: pimComponentTable.setDescription('The (conceptual) table containing objects specific to a PIM domain. One row exists for each domain to which the router is connected. A PIM-SM domain is defined as an area of the network over which Bootstrap messages are forwarded. Typically, a PIM-SM router will be a member of exactly one domain. This table also supports, however, routers which may form a border between two PIM-SM domains and do not forward Bootstrap messages between them.')
pimComponentEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 12, 1), ).setIndexNames((0, "PIM-MIB", "pimComponentIndex"))
if mibBuilder.loadTexts: pimComponentEntry.setStatus('current')
if mibBuilder.loadTexts: pimComponentEntry.setDescription('An entry (conceptual row) in the pimComponentTable.')
pimComponentIndex = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: pimComponentIndex.setStatus('current')
if mibBuilder.loadTexts: pimComponentIndex.setDescription('A number uniquely identifying the component. Each protocol instance connected to a separate domain should have a different index value. Routers that only support membership in a single PIM-SM domain should use a pimComponentIndex value of 1.')
pimComponentBSRAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimComponentBSRAddress.setStatus('current')
if mibBuilder.loadTexts: pimComponentBSRAddress.setDescription('The IP address of the bootstrap router (BSR) for the local PIM region.')
pimComponentBSRExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimComponentBSRExpiryTime.setStatus('current')
if mibBuilder.loadTexts: pimComponentBSRExpiryTime.setDescription('The minimum time remaining before the bootstrap router in the local domain will be declared down. For candidate BSRs, this is the time until the component sends an RP-Set message. For other routers, this is the time until it may accept an RP-Set message from a lower candidate BSR.')
pimComponentCRPHoldTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimComponentCRPHoldTime.setStatus('current')
if mibBuilder.loadTexts: pimComponentCRPHoldTime.setDescription('The holdtime of the component when it is a candidate RP in the local domain. The value of 0 is used to indicate that the local system is not a Candidate-RP.')
pimComponentStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimComponentStatus.setStatus('current')
if mibBuilder.loadTexts: pimComponentStatus.setDescription('The status of this entry. Creating the entry creates another protocol instance; destroying the entry disables a protocol instance.')
pimNeighborLoss = NotificationType((1, 3, 6, 1, 3, 61, 1, 0, 1)).setObjects(("PIM-MIB", "pimNeighborIfIndex"))
if mibBuilder.loadTexts: pimNeighborLoss.setStatus('current')
if mibBuilder.loadTexts: pimNeighborLoss.setDescription('A pimNeighborLoss trap signifies the loss of an adjacency with a neighbor. This trap should be generated when the neighbor timer expires, and the router has no other neighbors on the same interface with a lower IP address than itself.')
pimMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 61, 2))
pimMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 61, 2, 1))
pimMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 61, 2, 2))
pimV1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 61, 2, 1, 1)).setObjects(("PIM-MIB", "pimV1MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimV1MIBCompliance = pimV1MIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: pimV1MIBCompliance.setDescription('The compliance statement for routers running PIMv1 and implementing the PIM MIB.')
pimSparseV2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 61, 2, 1, 2)).setObjects(("PIM-MIB", "pimV2MIBGroup"), ("PIM-MIB", "pimV2CandidateRPMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimSparseV2MIBCompliance = pimSparseV2MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pimSparseV2MIBCompliance.setDescription('The compliance statement for routers running PIM Sparse Mode and implementing the PIM MIB.')
pimDenseV2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 61, 2, 1, 3)).setObjects(("PIM-MIB", "pimDenseV2MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimDenseV2MIBCompliance = pimDenseV2MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pimDenseV2MIBCompliance.setDescription('The compliance statement for routers running PIM Dense Mode and implementing the PIM MIB.')
pimNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 61, 2, 2, 1)).setObjects(("PIM-MIB", "pimNeighborLoss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimNotificationGroup = pimNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: pimNotificationGroup.setDescription('A collection of notifications for signaling important PIM events.')
pimV2MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 2)).setObjects(("PIM-MIB", "pimJoinPruneInterval"), ("PIM-MIB", "pimNeighborIfIndex"), ("PIM-MIB", "pimNeighborUpTime"), ("PIM-MIB", "pimNeighborExpiryTime"), ("PIM-MIB", "pimInterfaceAddress"), ("PIM-MIB", "pimInterfaceNetMask"), ("PIM-MIB", "pimInterfaceDR"), ("PIM-MIB", "pimInterfaceHelloInterval"), ("PIM-MIB", "pimInterfaceStatus"), ("PIM-MIB", "pimInterfaceJoinPruneInterval"), ("PIM-MIB", "pimInterfaceCBSRPreference"), ("PIM-MIB", "pimInterfaceMode"), ("PIM-MIB", "pimRPSetHoldTime"), ("PIM-MIB", "pimRPSetExpiryTime"), ("PIM-MIB", "pimComponentBSRAddress"), ("PIM-MIB", "pimComponentBSRExpiryTime"), ("PIM-MIB", "pimComponentCRPHoldTime"), ("PIM-MIB", "pimComponentStatus"), ("PIM-MIB", "pimIpMRouteFlags"), ("PIM-MIB", "pimIpMRouteUpstreamAssertTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimV2MIBGroup = pimV2MIBGroup.setStatus('current')
if mibBuilder.loadTexts: pimV2MIBGroup.setDescription('A collection of objects to support management of PIM Sparse Mode (version 2) routers.')
pimDenseV2MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 5)).setObjects(("PIM-MIB", "pimNeighborIfIndex"), ("PIM-MIB", "pimNeighborUpTime"), ("PIM-MIB", "pimNeighborExpiryTime"), ("PIM-MIB", "pimInterfaceAddress"), ("PIM-MIB", "pimInterfaceNetMask"), ("PIM-MIB", "pimInterfaceDR"), ("PIM-MIB", "pimInterfaceHelloInterval"), ("PIM-MIB", "pimInterfaceStatus"), ("PIM-MIB", "pimInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimDenseV2MIBGroup = pimDenseV2MIBGroup.setStatus('current')
if mibBuilder.loadTexts: pimDenseV2MIBGroup.setDescription('A collection of objects to support management of PIM Dense Mode (version 2) routers.')
pimV2CandidateRPMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 3)).setObjects(("PIM-MIB", "pimCandidateRPAddress"), ("PIM-MIB", "pimCandidateRPRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimV2CandidateRPMIBGroup = pimV2CandidateRPMIBGroup.setStatus('current')
if mibBuilder.loadTexts: pimV2CandidateRPMIBGroup.setDescription('A collection of objects to support configuration of which groups a router is to advertise itself as a Candidate-RP.')
pimV1MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 4)).setObjects(("PIM-MIB", "pimJoinPruneInterval"), ("PIM-MIB", "pimNeighborIfIndex"), ("PIM-MIB", "pimNeighborUpTime"), ("PIM-MIB", "pimNeighborExpiryTime"), ("PIM-MIB", "pimNeighborMode"), ("PIM-MIB", "pimInterfaceAddress"), ("PIM-MIB", "pimInterfaceNetMask"), ("PIM-MIB", "pimInterfaceJoinPruneInterval"), ("PIM-MIB", "pimInterfaceStatus"), ("PIM-MIB", "pimInterfaceMode"), ("PIM-MIB", "pimInterfaceDR"), ("PIM-MIB", "pimInterfaceHelloInterval"), ("PIM-MIB", "pimRPState"), ("PIM-MIB", "pimRPStateTimer"), ("PIM-MIB", "pimRPLastChange"), ("PIM-MIB", "pimRPRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimV1MIBGroup = pimV1MIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: pimV1MIBGroup.setDescription('A collection of objects to support management of PIM (version 1) routers.')
pimNextHopGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 6)).setObjects(("PIM-MIB", "pimIpMRouteNextHopPruneReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimNextHopGroup = pimNextHopGroup.setStatus('current')
if mibBuilder.loadTexts: pimNextHopGroup.setDescription('A collection of optional objects to provide per-next hop information for diagnostic purposes. Supporting this group may add a large number of instances to a tree walk, but the information in this group can be extremely useful in tracking down multicast connectivity problems.')
pimAssertGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 7)).setObjects(("PIM-MIB", "pimIpMRouteAssertMetric"), ("PIM-MIB", "pimIpMRouteAssertMetricPref"), ("PIM-MIB", "pimIpMRouteAssertRPTBit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimAssertGroup = pimAssertGroup.setStatus('current')
if mibBuilder.loadTexts: pimAssertGroup.setDescription('A collection of optional objects to provide extra information about the assert election process. There is no protocol reason to keep such information, but some implementations may already keep this information and make it available. These objects can also be very useful in debugging connectivity or duplicate packet problems, especially if the assert winner does not support the PIM and IP Multicast MIBs.')
mibBuilder.exportSymbols("PIM-MIB", pim=pim, pimInterfaceJoinPruneInterval=pimInterfaceJoinPruneInterval, pimRPStateTimer=pimRPStateTimer, pimCandidateRPTable=pimCandidateRPTable, pimV1MIBGroup=pimV1MIBGroup, pimRPAddress=pimRPAddress, pimComponentTable=pimComponentTable, pimIpMRouteUpstreamAssertTimer=pimIpMRouteUpstreamAssertTimer, pimV1MIBCompliance=pimV1MIBCompliance, pimRPState=pimRPState, pimIpMRouteNextHopTable=pimIpMRouteNextHopTable, pimIpMRouteNextHopEntry=pimIpMRouteNextHopEntry, pimRPRowStatus=pimRPRowStatus, pimNotificationGroup=pimNotificationGroup, pimIpMRouteTable=pimIpMRouteTable, pimInterfaceTable=pimInterfaceTable, pimNeighborAddress=pimNeighborAddress, pimIpMRouteEntry=pimIpMRouteEntry, PYSNMP_MODULE_ID=pimMIB, pimRPLastChange=pimRPLastChange, pimDenseV2MIBCompliance=pimDenseV2MIBCompliance, pimRPSetComponent=pimRPSetComponent, pimIpMRouteAssertMetricPref=pimIpMRouteAssertMetricPref, pimMIBCompliances=pimMIBCompliances, pimRPSetTable=pimRPSetTable, pimComponentStatus=pimComponentStatus, pimInterfaceNetMask=pimInterfaceNetMask, pimNeighborLoss=pimNeighborLoss, pimSparseV2MIBCompliance=pimSparseV2MIBCompliance, pimMIBGroups=pimMIBGroups, pimInterfaceStatus=pimInterfaceStatus, pimRPSetEntry=pimRPSetEntry, pimComponentCRPHoldTime=pimComponentCRPHoldTime, pimMIBObjects=pimMIBObjects, pimNeighborEntry=pimNeighborEntry, pimInterfaceEntry=pimInterfaceEntry, pimNeighborMode=pimNeighborMode, pimIpMRouteNextHopPruneReason=pimIpMRouteNextHopPruneReason, pimInterfaceAddress=pimInterfaceAddress, pimCandidateRPGroupAddress=pimCandidateRPGroupAddress, pimMIB=pimMIB, pimV2CandidateRPMIBGroup=pimV2CandidateRPMIBGroup, pimInterfaceCBSRPreference=pimInterfaceCBSRPreference, pimRPTable=pimRPTable, pimRPSetAddress=pimRPSetAddress, pimNeighborUpTime=pimNeighborUpTime, pimNeighborIfIndex=pimNeighborIfIndex, pimRPGroupAddress=pimRPGroupAddress, pimTraps=pimTraps, pimRPSetGroupAddress=pimRPSetGroupAddress, pimRPSetExpiryTime=pimRPSetExpiryTime, pimComponentIndex=pimComponentIndex, pimMIBConformance=pimMIBConformance, pimInterfaceHelloInterval=pimInterfaceHelloInterval, pimIpMRouteAssertRPTBit=pimIpMRouteAssertRPTBit, pimNextHopGroup=pimNextHopGroup, pimDenseV2MIBGroup=pimDenseV2MIBGroup, pimNeighborExpiryTime=pimNeighborExpiryTime, pimIpMRouteFlags=pimIpMRouteFlags, pimNeighborTable=pimNeighborTable, pimInterfaceDR=pimInterfaceDR, pimRPSetHoldTime=pimRPSetHoldTime, pimRPEntry=pimRPEntry, pimJoinPruneInterval=pimJoinPruneInterval, pimComponentBSRExpiryTime=pimComponentBSRExpiryTime, pimCandidateRPEntry=pimCandidateRPEntry, pimV2MIBGroup=pimV2MIBGroup, pimRPSetGroupMask=pimRPSetGroupMask, pimCandidateRPRowStatus=pimCandidateRPRowStatus, pimAssertGroup=pimAssertGroup, pimComponentEntry=pimComponentEntry, pimCandidateRPGroupMask=pimCandidateRPGroupMask, pimIpMRouteAssertMetric=pimIpMRouteAssertMetric, pimCandidateRPAddress=pimCandidateRPAddress, pimInterfaceMode=pimInterfaceMode, pimInterfaceIfIndex=pimInterfaceIfIndex, pimComponentBSRAddress=pimComponentBSRAddress)
