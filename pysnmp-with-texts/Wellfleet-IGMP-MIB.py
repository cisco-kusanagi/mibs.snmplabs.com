#
# PySNMP MIB module Wellfleet-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IGMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, IpAddress, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "IpAddress", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfIgmpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfIgmpGroup")
wfIgmpBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1))
wfIgmpBaseCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseCreate.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete IGMP.')
wfIgmpBaseEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseEnable.setDescription('Enable/Disable Parameter indicates whether this IGMP record is enabled or disabled.')
wfIgmpBaseState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBaseState.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseState.setDescription('The current state of the entire IGMP.')
wfIgmpBaseEstimatedGroups = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseEstimatedGroups.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseEstimatedGroups.setDescription('The number of estimated groups that will be used through this router.')
wfIgmpBaseVersionThreshold = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(540)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseVersionThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseVersionThreshold.setDescription('The time (in seconds) that will pass after the last old style query before we will try to become the igmp designated querier')
wfIgmpBaseDebug = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseDebug.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseDebug.setDescription('This is a debug field for IGMP. Setting bits cause igmp to gernerate certain log messages. This field will NOT restart IGMP. The follow bits maybe set in any combination (LS stands for least significant): 0x00000001 for received IGMP protocol (join/leave) packets 0x00000002 for sent IGMP messages 0x00000004 for received mcast protocl packets 0x00000008 for MTRACE related log messages 0x00000010 for configuration related log messages 0x00000020 for interaction with mcast protocols 0x00000040 for interaction with RSVP 0x00000080 for MTM forwarding cache related log messages 0x00000100 for IGMP Relay related log messages')
wfIgmpBaseJoinAckEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseJoinAckEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseJoinAckEnable.setDescription('Enable/Disable Parameter indicates whether an immediate response is needed for an IGMP report by sending an IGMP query to the group of this IGMP report.')
wfIgmpBaseFwdCacheLimit = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 65535)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseFwdCacheLimit.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseFwdCacheLimit.setDescription('Maximum number of MTM forwarding cache entries')
wfIgmpBaseIgnoreNonLocalReport = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("accept", 2))).clone('ignore')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseIgnoreNonLocalReport.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseIgnoreNonLocalReport.setDescription('Whether IGMP joins/leaves from a non-local network are accepted. For example, if network 10.10.10.0/24 is defined on circuit 1 which is connected to a physical wire for both 10.10.10.0/24 and 10.10.11.0/24, an IGMP Join from the 10.10.11.0/24 network may be ignored on the circuit')
wfIgmpBaseRelayEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseRelayEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseRelayEnable.setDescription('Enable/Disable Parameter indicates whether the IGMP Relay is enabled or disabled.')
wfIgmpBaseRelayTimeoutValue = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseRelayTimeoutValue.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseRelayTimeoutValue.setDescription('The timer value for timing out IGMP-R forward entries.')
wfIgmpBaseRelayFwdOptions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("both", 3))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseRelayFwdOptions.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseRelayFwdOptions.setDescription('This mib attribute indicates whether multicast data is forwarded to IGMP-R primary upstream circuit, backup upstream, or both of them.')
wfIgmpBaseGroupCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBaseGroupCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBaseGroupCount.setDescription('Actual number of groups presented on the router')
wfIgmpBasePerStreamRedundEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBasePerStreamRedundEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBasePerStreamRedundEnable.setDescription('Enable/Disable Parameter indicates whether the IGMP Relay Per-Stream Redundancy is enabled or disabled. Per-Stream Redundancy allows a stream to fail over to backup link if it is not received on the primary link for a period of wfIgmpBaseRelayTimeoutValue, and then fall back if the stream is received on the primary link again. To enable this feature, you must enable wfIgmpBaseRelayEnable.')
wfIgmpIfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2), )
if mibBuilder.loadTexts: wfIgmpIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfTable.setDescription('List of configured IGMP interfaces')
wfIgmpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpIfCctno"))
if mibBuilder.loadTexts: wfIgmpIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfEntry.setDescription('A description of an IGMP interface')
wfIgmpIfCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfCreate.setDescription('Indicates whether this IGMP If record is to be deleted or created')
wfIgmpIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfEnable.setDescription('Indicates whether this IGMP intf record is to be enabled or disabled')
wfIgmpIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("invalid", 4), ("notpres", 5))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfState.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfState.setDescription('The current state of the IGMP interface. Invalid indicates an error in processing the cfg record')
wfIgmpDesignatedRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpDesignatedRouter.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpDesignatedRouter.setDescription('The current Igmp Designated Router. If there are multipule routers on a multi-access network, this is the router sending the igmp host queries.')
wfIgmpIfQueryRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfQueryRate.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfQueryRate.setDescription('Query rate. This value specifies, in seconds, how often a local group membership is queried. If set to 0, no queries will be sent out this interface, and it should mean that there are no hosts on that interface that want to multicast. This does not mean no multicast traffic will go out this port, as routed mutilcast traffic may use this interface')
wfIgmpIfMembershipTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 8192)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfMembershipTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfMembershipTimeout.setDescription('Membership timeout. This value specifies, in seconds, the amount of time that a local group membership is valid without confirmation. The suggested value is (2*QueryRate)+20')
wfIgmpIfDRTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 8192)).clone(140)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfDRTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfDRTimeout.setDescription('Designated Router Timeout. This value specifies, in seconds, the amount of time from the last host query message that will be used to determine the loss of the IGMP designated router. ')
wfIgmpIfLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfLocalIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfLocalIpAddress.setDescription('IP Address currently in use on this circuit. This is the IP address that being used to generate and multicast traffic')
wfIgmpIfCctno = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfCctno.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfCctno.setDescription('The Circuit IGMP should be running on')
wfIgmpIfInDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInDatagrams.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfInDatagrams.setDescription('The total number of IGMP datagrams received on the interface.')
wfIgmpIfOutQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfOutQueries.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfOutQueries.setDescription('The number of Host Membership Query messages sent out of this interface.')
wfIgmpIfInQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInQueries.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfInQueries.setDescription('The number of Host Membership Query messages that have been received on this interface.')
wfIgmpIfDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfDiscards.setDescription('The number of IGMP messages received on this interface that were discarded due to bad checksums, illegal message types, bad values in fields, etc.')
wfIgmpIfNetVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfNetVersion.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfNetVersion.setDescription('This is the version of igmp that this router believes is running on this network. A value of 1 means IGMPv1 (old igmp) and a value of 2 means IGMPv2 (new igmp).')
wfIgmpIfMaxHostResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfMaxHostResponse.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfMaxHostResponse.setDescription('This is the amount of time in 10th of seconds that a host is supposed to take to respond to a query. This will value will be placed in the code feild of the igmp query packet.')
wfIgmpIfRoutingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("igmp", 1), ("dvmrp", 2), ("pim", 3), ("mospf", 4), ("cbt", 5), ("internal", 6), ("relay", 7))).clone('igmp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfRoutingProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfRoutingProtocol.setDescription("This has the value of the multicast protocol running on this interface. A value 'igmp' means there is no multicast protocol up on this interface. Note : type 8 used for static configuration for MTM for ti display only.Hence is reserved ")
wfIgmpIfDroppedDataPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfDroppedDataPkt.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfDroppedDataPkt.setDescription('Number of data packets that have to be dropped on this outgoing interface due to lack of buffers. If alias flooding is used for some (s, g) and kernel could not allocate buffers for some member gates, those drops are not counted into this counter')
wfIgmpIfMtraceEntryLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 8192)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfMtraceEntryLifetime.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfMtraceEntryLifetime.setDescription('This is the amount of time in seconds that a router is supposed to keep a forwarding cache entry that was created specifically for mtrace.')
wfIgmpIfInMtraceReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInMtraceReqs.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfInMtraceReqs.setDescription('The total number of Mtrace packets received on the interface.')
wfIgmpIfOutMtraceReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfOutMtraceReqs.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfOutMtraceReqs.setDescription('The total number of Mtrace packets send from the interface.')
wfIgmpIfInMtraceResps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInMtraceResps.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfInMtraceResps.setDescription('The total number of Mtrace packets received on the interface.')
wfIgmpIfOutMtraceResps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfOutMtraceResps.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfOutMtraceResps.setDescription('The total number of Mtrace packets send from the interface.')
wfIgmpIfRelayType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("downstream", 3))).clone('downstream')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfRelayType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfRelayType.setDescription('Indicates whether the IGMP circuit is configured as the primary upstream circuit, the backup upstream circuit or a downstream circuit. At most one circuit can be configured as the primary. At most one circuit can be configured as the backup.')
wfIgmpIfUnsolicitedReportInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfUnsolicitedReportInterval.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfUnsolicitedReportInterval.setDescription("This mib attribute is the Unsolicited Report Interval, in seconds, which is the time between repetitions of a host's initial report of membership in a group. If this is zero, then do not send the report twice.")
wfIgmpIfSuppressQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfSuppressQuery.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfSuppressQuery.setDescription("Whether IGMP query is suppressed on this interface. In Bay's multicast implementation, configuring 'IGMP' on an interface means two things: 1. the interface will be used for forwarding multicast traffic 2. IGMP protocol will be running on the interface Therefore, on some interfaces like point-to-point or non-broadcast ones, even though there is no need to run IGMP protocol, 'igmp' must be configured. However, with this attribute we can disable the sending of IGMP queries.")
wfIgmpIfGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfGroupCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfGroupCount.setDescription('The total number of groups presented on the interface.')
wfIgmpIfVRRPTriggerState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfVRRPTriggerState.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfVRRPTriggerState.setDescription('Indicates whether VRRP subsystem wants this IGMP Intf to be enabled or disabled.')
wfIgmpIfStaticFwdCacheLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(80, 7200)).clone(216)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfStaticFwdCacheLifeTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIfStaticFwdCacheLifeTime.setDescription(' If the IGMPStaticForwarding Policy mode is set to static to dynamic (static inbound and multicast protcol outbound) mode. This value should be set based on which protcols are planned to be configured on the outbound. Typical values are for DVMRP(7200), MOSPF(600) and PIM(210) so that MTM cache entries will be alive for the above specified seconds even if the traffic is not present. The above value is in seconds. ')
wfIgmpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3), )
if mibBuilder.loadTexts: wfIgmpGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpGroupTable.setDescription('A table of IGMP groups')
wfIgmpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpCct"), (0, "Wellfleet-IGMP-MIB", "wfIgmpIpifAddress"), (0, "Wellfleet-IGMP-MIB", "wfIgmpGroupAddress"))
if mibBuilder.loadTexts: wfIgmpGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpGroupEntry.setDescription('An IGMP group in the group table')
wfIgmpGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpGroupAddress.setDescription('the group address')
wfIgmpCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpCct.setDescription('the circuit for this group')
wfIgmpIpifAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIpifAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpIpifAddress.setDescription('the IP interface for this group')
wfIgmpTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpTimeLeft.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpTimeLeft.setDescription('how long until this group times out.')
wfIgmpStaticGroupTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4), )
if mibBuilder.loadTexts: wfIgmpStaticGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpStaticGroupTable.setDescription('The list of elements in IGMP Static membership table')
wfIgmpStaticGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupCct"), (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupAddress"), (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupPrefix"))
if mibBuilder.loadTexts: wfIgmpStaticGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpStaticGroupEntry.setDescription('A Staticly configured group membership')
wfIgmpStaticGroupCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpStaticGroupCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpStaticGroupCreate.setDescription('Indicates whether this IGMP record is to be deleted or created')
wfIgmpStaticGroupCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpStaticGroupCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpStaticGroupCct.setDescription('the circuit for this group')
wfIgmpStaticGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpStaticGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpStaticGroupAddress.setDescription('the group address')
wfIgmpStaticGroupPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpStaticGroupPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpStaticGroupPrefix.setDescription('the prefix for this group')
wfIgmpBoundaryTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5), )
if mibBuilder.loadTexts: wfIgmpBoundaryTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryTable.setDescription('The list of elements in IGMP Boundary table')
wfIgmpBoundaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpBoundaryGroupAddress"), (0, "Wellfleet-IGMP-MIB", "wfIgmpBoundaryGroupPrefix"))
if mibBuilder.loadTexts: wfIgmpBoundaryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryEntry.setDescription('For Administratively Scoped Addresses: No group that falls into this group/prefix will be accepted on the specified cct, or forwarded out of the cct')
wfIgmpBoundaryCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryCreate.setDescription('Indicates whether this record is to be deleted or created')
wfIgmpBoundaryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryEnable.setDescription('Indicates whether this record is enabled or disabled')
wfIgmpBoundaryGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBoundaryGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryGroupAddress.setDescription('the group address in concern')
wfIgmpBoundaryGroupPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBoundaryGroupPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryGroupPrefix.setDescription('the group prefix length')
wfIgmpBoundaryCctList = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryCctList.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryCctList.setDescription('The boundary circuit list. Each circuit takes two octets')
wfIgmpBoundaryTunnelList = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryTunnelList.setStatus('mandatory')
if mibBuilder.loadTexts: wfIgmpBoundaryTunnelList.setDescription('the boundary tunnel list. Each tunnel takes 8 octets, the first 4 of which are for local IP address, and the last 4 are for remote IP address')
mibBuilder.exportSymbols("Wellfleet-IGMP-MIB", wfIgmpBoundaryEnable=wfIgmpBoundaryEnable, wfIgmpBaseJoinAckEnable=wfIgmpBaseJoinAckEnable, wfIgmpIfStaticFwdCacheLifeTime=wfIgmpIfStaticFwdCacheLifeTime, wfIgmpGroupEntry=wfIgmpGroupEntry, wfIgmpBoundaryGroupAddress=wfIgmpBoundaryGroupAddress, wfIgmpBasePerStreamRedundEnable=wfIgmpBasePerStreamRedundEnable, wfIgmpBaseEstimatedGroups=wfIgmpBaseEstimatedGroups, wfIgmpBaseEnable=wfIgmpBaseEnable, wfIgmpBaseGroupCount=wfIgmpBaseGroupCount, wfIgmpStaticGroupCreate=wfIgmpStaticGroupCreate, wfIgmpBaseCreate=wfIgmpBaseCreate, wfIgmpStaticGroupPrefix=wfIgmpStaticGroupPrefix, wfIgmpIfMtraceEntryLifetime=wfIgmpIfMtraceEntryLifetime, wfIgmpIfInMtraceResps=wfIgmpIfInMtraceResps, wfIgmpIfOutMtraceResps=wfIgmpIfOutMtraceResps, wfIgmpStaticGroupAddress=wfIgmpStaticGroupAddress, wfIgmpIfInMtraceReqs=wfIgmpIfInMtraceReqs, wfIgmpCct=wfIgmpCct, wfIgmpBaseRelayEnable=wfIgmpBaseRelayEnable, wfIgmpIfDroppedDataPkt=wfIgmpIfDroppedDataPkt, wfIgmpTimeLeft=wfIgmpTimeLeft, wfIgmpIfSuppressQuery=wfIgmpIfSuppressQuery, wfIgmpIfTable=wfIgmpIfTable, wfIgmpIfDRTimeout=wfIgmpIfDRTimeout, wfIgmpIfLocalIpAddress=wfIgmpIfLocalIpAddress, wfIgmpBaseFwdCacheLimit=wfIgmpBaseFwdCacheLimit, wfIgmpIfEntry=wfIgmpIfEntry, wfIgmpIfMaxHostResponse=wfIgmpIfMaxHostResponse, wfIgmpBoundaryTunnelList=wfIgmpBoundaryTunnelList, wfIgmpStaticGroupCct=wfIgmpStaticGroupCct, wfIgmpIfQueryRate=wfIgmpIfQueryRate, wfIgmpIfRelayType=wfIgmpIfRelayType, wfIgmpBase=wfIgmpBase, wfIgmpBaseIgnoreNonLocalReport=wfIgmpBaseIgnoreNonLocalReport, wfIgmpStaticGroupEntry=wfIgmpStaticGroupEntry, wfIgmpIfEnable=wfIgmpIfEnable, wfIgmpIfCreate=wfIgmpIfCreate, wfIgmpBaseRelayTimeoutValue=wfIgmpBaseRelayTimeoutValue, wfIgmpIfCctno=wfIgmpIfCctno, wfIgmpBoundaryCreate=wfIgmpBoundaryCreate, wfIgmpIfGroupCount=wfIgmpIfGroupCount, wfIgmpIfNetVersion=wfIgmpIfNetVersion, wfIgmpBoundaryTable=wfIgmpBoundaryTable, wfIgmpIfOutQueries=wfIgmpIfOutQueries, wfIgmpBoundaryCctList=wfIgmpBoundaryCctList, wfIgmpGroupTable=wfIgmpGroupTable, wfIgmpBaseVersionThreshold=wfIgmpBaseVersionThreshold, wfIgmpBaseState=wfIgmpBaseState, wfIgmpBoundaryEntry=wfIgmpBoundaryEntry, wfIgmpDesignatedRouter=wfIgmpDesignatedRouter, wfIgmpIfInQueries=wfIgmpIfInQueries, wfIgmpIfUnsolicitedReportInterval=wfIgmpIfUnsolicitedReportInterval, wfIgmpIfVRRPTriggerState=wfIgmpIfVRRPTriggerState, wfIgmpBaseRelayFwdOptions=wfIgmpBaseRelayFwdOptions, wfIgmpIfState=wfIgmpIfState, wfIgmpIfDiscards=wfIgmpIfDiscards, wfIgmpIfRoutingProtocol=wfIgmpIfRoutingProtocol, wfIgmpIfOutMtraceReqs=wfIgmpIfOutMtraceReqs, wfIgmpIpifAddress=wfIgmpIpifAddress, wfIgmpBaseDebug=wfIgmpBaseDebug, wfIgmpIfMembershipTimeout=wfIgmpIfMembershipTimeout, wfIgmpIfInDatagrams=wfIgmpIfInDatagrams, wfIgmpGroupAddress=wfIgmpGroupAddress, wfIgmpStaticGroupTable=wfIgmpStaticGroupTable, wfIgmpBoundaryGroupPrefix=wfIgmpBoundaryGroupPrefix)
