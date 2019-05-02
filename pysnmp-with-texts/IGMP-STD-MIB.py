#
# PySNMP MIB module IGMP-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IGMP-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, ModuleIdentity, MibIdentifier, Gauge32, NotificationType, iso, TimeTicks, Bits, Integer32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "ModuleIdentity", "MibIdentifier", "Gauge32", "NotificationType", "iso", "TimeTicks", "Bits", "Integer32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "mib-2")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
igmpStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 85))
igmpStdMIB.setRevisions(('2000-09-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: igmpStdMIB.setRevisionsDescriptions(('Initial version, published as RFC 2933.',))
if mibBuilder.loadTexts: igmpStdMIB.setLastUpdated('200009280000Z')
if mibBuilder.loadTexts: igmpStdMIB.setOrganization('IETF IDMR Working Group.')
if mibBuilder.loadTexts: igmpStdMIB.setContactInfo(' Dave Thaler Microsoft Corporation One Microsoft Way Redmond, WA 98052-6399 US Phone: +1 425 703 8835 EMail: dthaler@microsoft.com')
if mibBuilder.loadTexts: igmpStdMIB.setDescription('The MIB module for IGMP Management.')
igmpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 1))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 85, 1, 1), )
if mibBuilder.loadTexts: igmpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceTable.setDescription('The (conceptual) table listing the interfaces on which IGMP is enabled.')
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 85, 1, 1, 1), ).setIndexNames((0, "IGMP-STD-MIB", "igmpInterfaceIfIndex"))
if mibBuilder.loadTexts: igmpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceEntry.setDescription('An entry (conceptual row) representing an interface on which IGMP is enabled.')
igmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setDescription('The ifIndex value of the interface for which IGMP is enabled.')
igmpInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 2), Unsigned32().clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setDescription('The frequency at which IGMP Host-Query packets are transmitted on this interface.')
igmpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceStatus.setDescription('The activation of a row enables IGMP on the interface. The destruction of a row disables IGMP on the interface.')
igmpInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 4), Unsigned32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceVersion.setDescription('The version of IGMP which is running on this interface. This object can be used to configure a router capable of running either value. For IGMP to function correctly, all routers on a LAN must be configured to run the same version of IGMP on that LAN.')
igmpInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerier.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerier.setDescription('The address of the IGMP Querier on the IP subnet to which this interface is attached.')
igmpInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setDescription('The maximum query response time advertised in IGMPv2 queries on this interface.')
igmpInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerierUpTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerierUpTime.setDescription('The time since igmpInterfaceQuerier was last changed.')
igmpInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerierExpiryTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerierExpiryTime.setDescription('The amount of time remaining before the Other Querier Present Timer expires. If the local system is the querier, the value of this object is zero.')
igmpInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setDescription('The time remaining until the host assumes that there are no IGMPv1 routers present on the interface. While this is non- zero, the host will reply to all queries with version 1 membership reports.')
igmpInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setDescription('The number of queries received whose IGMP version does not match igmpInterfaceVersion, over the lifetime of the row entry. IGMP requires that all routers on a LAN be configured to run the same version of IGMP. Thus, if any queries are received with the wrong version, this indicates a configuration error.')
igmpInterfaceJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceJoins.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceJoins.setDescription('The number of times a group membership has been added on this interface; that is, the number of times an entry for this interface has been added to the Cache Table. This object gives an indication of the amount of IGMP activity over the lifetime of the row entry.')
igmpInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 12), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceProxyIfIndex.setDescription('Some devices implement a form of IGMP proxying whereby memberships learned on the interface represented by this row, cause IGMP Host Membership Reports to be sent on the interface whose ifIndex value is given by this object. Such a device would implement the igmpV2RouterMIBGroup only on its router interfaces (those interfaces with non-zero igmpInterfaceProxyIfIndex). Typically, the value of this object is 0, indicating that no proxying is being done.')
igmpInterfaceGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceGroups.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceGroups.setDescription('The current number of entries for this interface in the Cache Table.')
igmpInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceRobustness.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceRobustness.setDescription('The Robustness Variable allows tuning for the expected packet loss on a subnet. If a subnet is expected to be lossy, the Robustness Variable may be increased. IGMP is robust to (Robustness Variable-1) packet losses.')
igmpInterfaceLastMembQueryIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceLastMembQueryIntvl.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceLastMembQueryIntvl.setDescription('The Last Member Query Interval is the Max Response Time inserted into Group-Specific Queries sent in response to Leave Group messages, and is also the amount of time between Group-Specific Query messages. This value may be tuned to modify the leave latency of the network. A reduced value results in reduced time to detect the loss of the last member of a group. The value of this object is irrelevant if igmpInterfaceVersion is 1.')
igmpCacheTable = MibTable((1, 3, 6, 1, 2, 1, 85, 1, 2), )
if mibBuilder.loadTexts: igmpCacheTable.setStatus('current')
if mibBuilder.loadTexts: igmpCacheTable.setDescription('The (conceptual) table listing the IP multicast groups for which there are members on a particular interface.')
igmpCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 85, 1, 2, 1), ).setIndexNames((0, "IGMP-STD-MIB", "igmpCacheAddress"), (0, "IGMP-STD-MIB", "igmpCacheIfIndex"))
if mibBuilder.loadTexts: igmpCacheEntry.setStatus('current')
if mibBuilder.loadTexts: igmpCacheEntry.setDescription('An entry (conceptual row) in the igmpCacheTable.')
igmpCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: igmpCacheAddress.setStatus('current')
if mibBuilder.loadTexts: igmpCacheAddress.setDescription('The IP multicast group address for which this entry contains information.')
igmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: igmpCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpCacheIfIndex.setDescription('The interface for which this entry contains information for an IP multicast group address.')
igmpCacheSelf = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpCacheSelf.setStatus('current')
if mibBuilder.loadTexts: igmpCacheSelf.setDescription('An indication of whether the local system is a member of this group address on this interface.')
igmpCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheLastReporter.setStatus('current')
if mibBuilder.loadTexts: igmpCacheLastReporter.setDescription('The IP address of the source of the last membership report received for this IP Multicast group address on this interface. If no membership report has been received, this object has the value 0.0.0.0.')
igmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheUpTime.setStatus('current')
if mibBuilder.loadTexts: igmpCacheUpTime.setDescription('The time elapsed since this entry was created.')
igmpCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheExpiryTime.setStatus('current')
if mibBuilder.loadTexts: igmpCacheExpiryTime.setDescription('The minimum amount of time remaining before this entry will be aged out. A value of 0 indicates that the entry is only present because igmpCacheSelf is true and that if the router left the group, this entry would be aged out immediately. Note that some implementations may process membership reports from the local system in the same way as reports from other hosts, so a value of 0 is not required.')
igmpCacheStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpCacheStatus.setStatus('current')
if mibBuilder.loadTexts: igmpCacheStatus.setDescription('The status of this entry.')
igmpCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setStatus('current')
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setDescription('The time remaining until the local router will assume that there are no longer any IGMP version 1 members on the IP subnet attached to this interface. Upon hearing any IGMPv1 Membership Report, this value is reset to the group membership timer. While this time remaining is non-zero, the local router ignores any IGMPv2 Leave messages for this group that it receives on this interface.')
igmpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 2))
igmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 2, 1))
igmpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 85, 2, 2))
igmpV1HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 85, 2, 1, 1)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1HostMIBCompliance = igmpV1HostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV1HostMIBCompliance.setDescription('The compliance statement for hosts running IGMPv1 and implementing the IGMP MIB.')
igmpV1RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 85, 2, 1, 2)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1RouterMIBCompliance = igmpV1RouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV1RouterMIBCompliance.setDescription('The compliance statement for routers running IGMPv1 and implementing the IGMP MIB.')
igmpV2HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 85, 2, 1, 3)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBCompliance = igmpV2HostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV2HostMIBCompliance.setDescription('The compliance statement for hosts running IGMPv2 and implementing the IGMP MIB.')
igmpV2RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 85, 2, 1, 4)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpRouterMIBGroup"), ("IGMP-STD-MIB", "igmpV2RouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBCompliance = igmpV2RouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV2RouterMIBCompliance.setDescription('The compliance statement for routers running IGMPv2 and implementing the IGMP MIB.')
igmpBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 1)).setObjects(("IGMP-STD-MIB", "igmpCacheSelf"), ("IGMP-STD-MIB", "igmpCacheStatus"), ("IGMP-STD-MIB", "igmpInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpBaseMIBGroup = igmpBaseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpBaseMIBGroup.setDescription('The basic collection of objects providing management of IGMP version 1 or 2.')
igmpRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 2)).setObjects(("IGMP-STD-MIB", "igmpCacheUpTime"), ("IGMP-STD-MIB", "igmpCacheExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceJoins"), ("IGMP-STD-MIB", "igmpInterfaceGroups"), ("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceQuerierUpTime"), ("IGMP-STD-MIB", "igmpInterfaceQuerierExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceQueryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterMIBGroup = igmpRouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpRouterMIBGroup.setDescription('A collection of additional objects for management of IGMP version 1 or 2 in routers.')
igmpV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 3)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion1QuerierTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBGroup = igmpV2HostMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2HostMIBGroup.setDescription('A collection of additional objects for management of IGMP version 2 in hosts.')
igmpHostOptMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 4)).setObjects(("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpHostOptMIBGroup = igmpHostOptMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpHostOptMIBGroup.setDescription('A collection of optional objects for IGMP hosts. Supporting this group can be especially useful in an environment with a router which does not support the IGMP MIB.')
igmpV2RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 5)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"), ("IGMP-STD-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-STD-MIB", "igmpInterfaceRobustness"), ("IGMP-STD-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-STD-MIB", "igmpInterfaceLastMembQueryIntvl"), ("IGMP-STD-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBGroup = igmpV2RouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2RouterMIBGroup.setDescription('A collection of additional objects for management of IGMP version 2 in routers.')
igmpV2ProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 85, 2, 2, 6)).setObjects(("IGMP-STD-MIB", "igmpInterfaceProxyIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2ProxyMIBGroup = igmpV2ProxyMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2ProxyMIBGroup.setDescription('A collection of additional objects for management of IGMP proxy devices.')
mibBuilder.exportSymbols("IGMP-STD-MIB", igmpV2RouterMIBGroup=igmpV2RouterMIBGroup, igmpInterfaceQueryMaxResponseTime=igmpInterfaceQueryMaxResponseTime, igmpInterfaceIfIndex=igmpInterfaceIfIndex, igmpInterfaceJoins=igmpInterfaceJoins, igmpInterfaceStatus=igmpInterfaceStatus, igmpInterfaceQuerierUpTime=igmpInterfaceQuerierUpTime, igmpRouterMIBGroup=igmpRouterMIBGroup, igmpMIBCompliances=igmpMIBCompliances, igmpInterfaceEntry=igmpInterfaceEntry, igmpBaseMIBGroup=igmpBaseMIBGroup, igmpStdMIB=igmpStdMIB, igmpHostOptMIBGroup=igmpHostOptMIBGroup, igmpMIBConformance=igmpMIBConformance, igmpInterfaceGroups=igmpInterfaceGroups, igmpV2HostMIBCompliance=igmpV2HostMIBCompliance, igmpInterfaceProxyIfIndex=igmpInterfaceProxyIfIndex, igmpV2RouterMIBCompliance=igmpV2RouterMIBCompliance, igmpInterfaceWrongVersionQueries=igmpInterfaceWrongVersionQueries, igmpV1HostMIBCompliance=igmpV1HostMIBCompliance, igmpMIBObjects=igmpMIBObjects, igmpInterfaceVersion=igmpInterfaceVersion, igmpCacheEntry=igmpCacheEntry, igmpCacheAddress=igmpCacheAddress, igmpCacheUpTime=igmpCacheUpTime, igmpInterfaceLastMembQueryIntvl=igmpInterfaceLastMembQueryIntvl, igmpCacheSelf=igmpCacheSelf, igmpCacheIfIndex=igmpCacheIfIndex, igmpInterfaceVersion1QuerierTimer=igmpInterfaceVersion1QuerierTimer, igmpMIBGroups=igmpMIBGroups, igmpCacheTable=igmpCacheTable, igmpInterfaceQuerier=igmpInterfaceQuerier, igmpInterfaceQueryInterval=igmpInterfaceQueryInterval, igmpCacheVersion1HostTimer=igmpCacheVersion1HostTimer, igmpV2ProxyMIBGroup=igmpV2ProxyMIBGroup, igmpInterfaceRobustness=igmpInterfaceRobustness, igmpV2HostMIBGroup=igmpV2HostMIBGroup, igmpCacheLastReporter=igmpCacheLastReporter, igmpCacheExpiryTime=igmpCacheExpiryTime, igmpInterfaceQuerierExpiryTime=igmpInterfaceQuerierExpiryTime, igmpInterfaceTable=igmpInterfaceTable, igmpV1RouterMIBCompliance=igmpV1RouterMIBCompliance, igmpCacheStatus=igmpCacheStatus, PYSNMP_MODULE_ID=igmpStdMIB)
