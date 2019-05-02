#
# PySNMP MIB module CISCO-APPNAV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APPNAV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, MibIdentifier, Integer32, TimeTicks, Bits, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, IpAddress, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Integer32", "TimeTicks", "Bits", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAppNavMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 791))
ciscoAppNavMIB.setRevisions(('2012-06-07 00:00', '2012-05-22 00:00', '2012-04-10 00:00', '2012-03-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAppNavMIB.setRevisionsDescriptions(('Added zombie and inactive states to CAppNavCMStates.', 'Added cAppNavServContextJoinState in cAppNavServContextTable and modified CAppNavServContextOpStates.', 'There was a typo error in the name of the compliance object ciscoAppNavClusterStatisticsMIBCompliance. This object is now renamed as ciscoAppNavMIBCompliance.', 'Initial version of this MIB',))
if mibBuilder.loadTexts: ciscoAppNavMIB.setLastUpdated('201206070000Z')
if mibBuilder.loadTexts: ciscoAppNavMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAppNavMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-waas@cisco.com')
if mibBuilder.loadTexts: ciscoAppNavMIB.setDescription('This MIB module defines SNMP management objects describing the AppNav technology. A device, which implements the AppNav technology, is known as the AppNav controller. The AppNav controller intelligently navigates application traffic to a group of devices, which offer services to the application traffic. A device, which offers services to the application traffic is known as service node. As an example, the WAN optimization service uses the AppNav technology, where the AppNav controller intercepts applications traffic and redirects it to service nodes, which offer the WAN optimization service. A deployment may use more than one AppNav controllers and service nodes to provide high availability and scalability. In such deployments, AppNav controllers and service nodes together form a cluster, which is known as an AppNav cluster. Definitions of various entities related to the AppNav technology is as follows: AppNav controller: It is a device that intercepts application traffic and navigates (redirects) it to service nodes. Service node: It is a device that offers services to the traffic navigated (redirected) to it by the AppNav controller. AppNav controller group: An AppNav controller group is a group of one or more AppNav controllers. The AppNav controllers in the AppNav controller group communicate with each other regarding the connections being redirected by them, so that they redirect traffic to the right service node, irrespective of which AppNav controller receives packets for a given connection. For example, if particular connection is served by the service node A then that connection should always be served by the service node A until client or server terminates it. This mechanism is needed in the asymmetric network topologies, where packets may take different paths for forward and return journey. Service node group: A service node group is a group of one or more service nodes. The AppNav controller intercepts and redirects application traffic to service nodes in a service node group. The service nodes update their load status to the AppNav controllers, so that they can do intelligent load distribution among the available service nodes. AppNav Cluster: An AppNav controller group and a service node group together form a cluster, which is known as an AppNav cluster. An AppNav cluster is also known as a service context.')
class CAppNavServContextJoinStates(TextualConvention, Integer32):
    description = 'Represents various join states of the service context: unknown : This state indicates an internal error. notConfigured : This state indicates that the service context was enabled without the graceful option. started : This state indicates that the service context was enabled with the graceful option and the AppNav controller is currently in the Joining state. aborted : This state indicates that the service context was disabled while the AppNav controller was going through the joining process. completed : This state indicates that the service context was enabled with the graceful option and the AppNav controller completed the joining process.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("notConfigured", 2), ("started", 3), ("aborted", 4), ("completed", 5))

class CAppNavCMStates(TextualConvention, Integer32):
    description = 'Represents the cluster membership states of AppNav controllers and service nodes. dead : This state indicates that contact to the given AppNav controller or service node from the AppNav cluster is lost. alive : This state indicates that the given AppNav controller or service node is in contact of the AppNav cluster. excluded : This state indicates that given AppNav controller/service node is not a part of the AppNav cluster. partial : This state indicates that the given AppNav controller/service node is partially part of the AppNav cluster. na : This state indicates that the given AppNav controller/service node has no status information available when service context is in the admin disabled state. zombie : This state indicates that the given AppNav controller is removed from config but is still alive. inactive : This state indicates that the given AppNav controller is added to config but is inactive because of zombies.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("dead", 1), ("alive", 2), ("excluded", 3), ("partial", 4), ("na", 5), ("zombie", 6), ("inactive", 7))

class CAppNavIRStates(TextualConvention, Integer32):
    description = 'Represents the interception readiness states of the AppNav controller. The interception readiness state indicates whether AppNav controller is ready to intercept application traffic or not. ready : This state indicates that the AppNav controller is ready to do interception. notReady : This state indicates that the AppNav controller is not ready to do interception. na : This state indicates that this state is not applicable to the AppNav controller.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ready", 1), ("notReady", 2), ("na", 3))

class CAppNavServContextOpStates(TextualConvention, Integer32):
    description = 'Represents various operational states of the service context: initializing : This state indicates that the service context is in the initialization state. converging : This state indicates that the service context is in the converging state. This state is acquired when the AppNav controller detects the presence of a new AppNav controller or a service node, or loss of liveliness with any AppNav controller or service node in the service context, and is waiting to re-converge. internalError : This state indicates that service context is in the internal error state. This state is acquired when the AppNav controller fails to re-converge upon any change in service context. In this state, traffic redirection is stopped for new connections and existing connections are redirected on the best effort basis. degraded : This state indicates that the service context is in the degraded state. This state is acquired when no single fully connected subset of configured AppNav controllers and service nodes found. In this state, traffic redirection is turned off for new connections. operational : This state indicates that the service context is in the operational state. adminDisabled : This state indicates that the service context is disabled by an admin. initializingJoining : This state indicates that the service context is in the initializing joining state. This state is acquired when the AppNav controller is in the initializing state of joining process. convergingJoining : This state indicates that the service context is in the converging joining state. This state is acquired when the AppNav controller detects the presence of a new AppNav controller or a service node, or loss of liveliness with any AppNav controller or service node in the service context, and is waiting to re-converge. operationalJoining : This state indicates that the service context is stuck in joining state because of cluster view is full but either the number of non-joining AppNav controllers in the view is 1 or the set of Service Nodes seen by this AppNav controllers is smaller than the set of Service Nodes seen by the existing cluster. degradedJoining : This state indicates that the service context is stuck in joining state because the cluster view is degraded when this AppNav controller is part of the cluster.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("initializing", 1), ("converging", 2), ("internalError", 3), ("degraded", 4), ("operational", 5), ("adminDisabled", 6), ("initializingJoining", 7), ("convergingJoining", 8), ("operationalJoining", 9), ("degradedJoining", 10))

ciscoAppNavMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0))
ciscoAppNavMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 1))
ciscoAppNavMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1))
cAppNavServContext = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1))
cAppNavACG = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2))
cAppNavSNG = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3))
cAppNavAC = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4))
cAppNavSN = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5))
cAppNavServContextTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1), )
if mibBuilder.loadTexts: cAppNavServContextTable.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextTable.setDescription('This table lists the objects, which gives information related to the service contexts configured on the AppNav controller.')
cAppNavServContextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavServContextIndex"))
if mibBuilder.loadTexts: cAppNavServContextEntry.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextEntry.setDescription('An entry describing the objects, which gives information related to a service context. The AppNav controller creates a new entry, when a new service context gets configured through the management interface. The AppNav controller deletes an entry for a given service context when it is removed from the configuration through the management interface.')
cAppNavServContextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavServContextIndex.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextIndex.setDescription("This object indicates an index of the cAppNavServiceContextTable. It is an arbitrary unsigned integer value that uniquely identifies an entry in cAppNavServiceContextTable. The value for each entry must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
cAppNavServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextName.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextName.setDescription('This object indicates the name of the service context.')
cAppNavServContextCurrOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 3), CAppNavServContextOpStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextCurrOpState.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextCurrOpState.setDescription('This object indicates the current operational state of the service context.')
cAppNavServContextLastOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 4), CAppNavServContextOpStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextLastOpState.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextLastOpState.setDescription('This object indicates the last operational state of the service context.')
cAppNavServContextIRState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 5), CAppNavIRStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextIRState.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextIRState.setDescription('This object indicates the Interception Readiness(IR) state of the service context.')
cAppNavServContextJoinState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 6), CAppNavServContextJoinStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavServContextJoinState.setStatus('current')
if mibBuilder.loadTexts: cAppNavServContextJoinState.setDescription('This object indicates the join state of the service context.')
cAppNavACGTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1), )
if mibBuilder.loadTexts: cAppNavACGTable.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGTable.setDescription('This table lists the objects, which gives information related to the AppNav controller group configured on the AppNav controller.')
cAppNavACGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavACGIndex"))
if mibBuilder.loadTexts: cAppNavACGEntry.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGEntry.setDescription('An entry describing the objects, which gives information related to the AppNav controller group configured on the AppNav controller. The AppNav controller creates a new entry when a new AppNav controller group gets configured on the AppNav controller through the management interface. The AppNav controller deletes an entry for a given AppNav controller group, when it is removed from the configuration through the management interface.')
cAppNavACGIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavACGIndex.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGIndex.setDescription("This object indicates an index of the cAppNavACGTable. It is an arbitrary unsigned integer value that uniquely identifies an entry in cAppNavACGTable. The value for each entry must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
cAppNavACGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACGName.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGName.setDescription('This object indicates the name of the AppNav controller group.')
cAppNavACGServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACGServContextName.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGServContextName.setDescription('This object indicates the service context to which AppNav controller belongs.')
cAppNavSNGTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1), )
if mibBuilder.loadTexts: cAppNavSNGTable.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGTable.setDescription('This table lists the objects, which gives information related to the service node group configured on the AppNav controller.')
cAppNavSNGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavSNGIndex"))
if mibBuilder.loadTexts: cAppNavSNGEntry.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGEntry.setDescription('An entry desribing the objects, which gives information regarding the service node groups configured on the AppNav controller. An AppNav controller creates a new entry, when a new service node group gets configured on the system through the management interface. The AppNav controller deletes an entry for a given service node group, when it is removed from the configuration through the management interface.')
cAppNavSNGIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavSNGIndex.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGIndex.setDescription("This object specifies an index of the cAppNavSNGTable. It is an arbitrary unsigned integer value that uniquely identifies an entry in cAppNavSNGTable. The value for each entry must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
cAppNavSNGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNGName.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGName.setDescription('This object indicates the name of service node group.')
cAppNavSNGServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNGServContextName.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGServContextName.setDescription('This object indicates the name of the service context to which given service node group belongs.')
cAppNavACTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1), )
if mibBuilder.loadTexts: cAppNavACTable.setStatus('current')
if mibBuilder.loadTexts: cAppNavACTable.setDescription('This table lists the objects, which give information related to the AppNav controllers configured on the AppNav controller to assign them to the service context.')
cAppNavACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavACIndex"))
if mibBuilder.loadTexts: cAppNavACEntry.setStatus('current')
if mibBuilder.loadTexts: cAppNavACEntry.setDescription('An entry describing the objects, which gives information related to the AppNav controllers configured on the AppNav controller to assign them to the service context. An AppNav controller creates a new entry, when a new AppNav controller gets configured on the AppNav controller through the management interface. The AppNav controller deletes an entry for a given AppNav controller, when it is removed from the configuration through the management interface.')
cAppNavACIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavACIndex.setStatus('current')
if mibBuilder.loadTexts: cAppNavACIndex.setDescription("This object indicates an index of the cAppNavACTable. It is an arbitrary unsigned integer value that uniquely identifies an entry in cAppNavACTable. The value for each entry must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
cAppNavACIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACIpAddrType.setStatus('current')
if mibBuilder.loadTexts: cAppNavACIpAddrType.setDescription('This object indicates the address type of the cAppNavACIpAddr. The cAppNavACEntries are only valid for address type of IPv4 and IPv6.')
cAppNavACIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACIpAddr.setStatus('current')
if mibBuilder.loadTexts: cAppNavACIpAddr.setDescription('This object indicates the IP address of the AppNav controller.')
cAppNavACServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACServContextName.setStatus('current')
if mibBuilder.loadTexts: cAppNavACServContextName.setDescription('This object indicates the name of the service context to which given AppNav controller belongs.')
cAppNavACACGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACACGName.setStatus('current')
if mibBuilder.loadTexts: cAppNavACACGName.setDescription('This object indicates the name of the AppNav controller group to which given AppNav controller belongs.')
cAppNavACCurrentCMState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 6), CAppNavCMStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavACCurrentCMState.setStatus('current')
if mibBuilder.loadTexts: cAppNavACCurrentCMState.setDescription('This object indicates the current cluster membership state of the given AppNav controller.')
cAppNavSNTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1), )
if mibBuilder.loadTexts: cAppNavSNTable.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNTable.setDescription('This table lists the objects, which gives information related to the service nodes configured on the AppNav controller to assign them to the service context.')
cAppNavSNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1), ).setIndexNames((0, "CISCO-APPNAV-MIB", "cAppNavSNIndex"))
if mibBuilder.loadTexts: cAppNavSNEntry.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNEntry.setDescription('An entry describing the objects, which gives information related to the service nodes configured on the AppNav controller to assign them to the service context. An AppNav controller creates a new entry, when a new service node gets configured on the system through the management interface. An AppNav controller deletes an entry for a given service node, when it is removed from the configuration through the management interface.')
cAppNavSNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cAppNavSNIndex.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNIndex.setDescription("This object indicates an index of the cAppNavSNTable. It is an arbitrary unsigned integer value that uniquely identifies an entry in cAppNavSNTable. The value for each entry must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
cAppNavSNIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNIpAddrType.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNIpAddrType.setDescription('This object indicates the address type of cacSnIpAddr. cacSNEntries are only valid for address type of IPv4 and IPv6.')
cAppNavSNIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNIpAddr.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNIpAddr.setDescription('This object indicates the IP address of the given service node.')
cAppNavSNServContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNServContextName.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNServContextName.setDescription('This object indicates the name of the service context to which given service node belongs.')
cAppNavSNSNGName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNSNGName.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNSNGName.setDescription('This object indicates the name of the service node group to which given service node belongs.')
cAppNavSNCurrentCMState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 6), CAppNavCMStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAppNavSNCurrentCMState.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNCurrentCMState.setDescription('This object indicats the current cluster membership state of the given service node.')
ciscoAppNavMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2))
ciscoAppNavMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1, 1)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServiceContextGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavMIBCompliance = ciscoAppNavMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoAppNavMIBCompliance.setDescription('This is a default module-compliance containing default object groups.')
ciscoAppNavMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1, 2)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServiceContextGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGGroup"), ("CISCO-APPNAV-MIB", "cAppNavACGroup"), ("CISCO-APPNAV-MIB", "cAppNavSNGroup"), ("CISCO-APPNAV-MIB", "cAppNavServiceContextGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavMIBComplianceRev1 = ciscoAppNavMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoAppNavMIBComplianceRev1.setDescription('This is a default module-compliance containing default object groups. This compliance deprecated ciscoAppNavMIBCompliance.')
cAppNavServiceContextGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 1)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServContextCurrOpState"), ("CISCO-APPNAV-MIB", "cAppNavServContextLastOpState"), ("CISCO-APPNAV-MIB", "cAppNavServContextIRState"), ("CISCO-APPNAV-MIB", "cAppNavServContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavServiceContextGroup = cAppNavServiceContextGroup.setStatus('current')
if mibBuilder.loadTexts: cAppNavServiceContextGroup.setDescription('This group includes objects which gives information for service context configured on the AppNav controller.')
cAppNavACGGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 2)).setObjects(("CISCO-APPNAV-MIB", "cAppNavACGServContextName"), ("CISCO-APPNAV-MIB", "cAppNavACGName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavACGGroup = cAppNavACGGroup.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGGroup.setDescription('This group includes objects, which give information related to AppNav controller group configured on the AppNav controller.')
cAppNavSNGGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 3)).setObjects(("CISCO-APPNAV-MIB", "cAppNavSNGServContextName"), ("CISCO-APPNAV-MIB", "cAppNavSNGName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavSNGGroup = cAppNavSNGGroup.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGGroup.setDescription('This group includes objects, which gives information related to the service node group configured on the AppNav controller.')
cAppNavACGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 4)).setObjects(("CISCO-APPNAV-MIB", "cAppNavACServContextName"), ("CISCO-APPNAV-MIB", "cAppNavACACGName"), ("CISCO-APPNAV-MIB", "cAppNavACCurrentCMState"), ("CISCO-APPNAV-MIB", "cAppNavACIpAddrType"), ("CISCO-APPNAV-MIB", "cAppNavACIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavACGroup = cAppNavACGroup.setStatus('current')
if mibBuilder.loadTexts: cAppNavACGroup.setDescription('This group includes objects, which gives information related to AppNav controllers configured on the AppNav controller to assign them to the AppNav cluster.')
cAppNavSNGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 5)).setObjects(("CISCO-APPNAV-MIB", "cAppNavSNServContextName"), ("CISCO-APPNAV-MIB", "cAppNavSNSNGName"), ("CISCO-APPNAV-MIB", "cAppNavSNCurrentCMState"), ("CISCO-APPNAV-MIB", "cAppNavSNIpAddrType"), ("CISCO-APPNAV-MIB", "cAppNavSNIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavSNGroup = cAppNavSNGroup.setStatus('current')
if mibBuilder.loadTexts: cAppNavSNGroup.setDescription('This group contains objects, which gives information related to service node configured on AppNav controller to assign them to the AppNav cluster.')
cAppNavServiceContextGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 6)).setObjects(("CISCO-APPNAV-MIB", "cAppNavServContextJoinState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAppNavServiceContextGroupRev1 = cAppNavServiceContextGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cAppNavServiceContextGroupRev1.setDescription('This group includes objects which gives information for service context configured on the AppNav controller.')
mibBuilder.exportSymbols("CISCO-APPNAV-MIB", ciscoAppNavMIBComplianceRev1=ciscoAppNavMIBComplianceRev1, cAppNavSNIpAddr=cAppNavSNIpAddr, cAppNavServContextEntry=cAppNavServContextEntry, CAppNavServContextJoinStates=CAppNavServContextJoinStates, cAppNavSNGEntry=cAppNavSNGEntry, cAppNavSNGName=cAppNavSNGName, cAppNavSNGroup=cAppNavSNGroup, cAppNavSNGTable=cAppNavSNGTable, ciscoAppNavMIB=ciscoAppNavMIB, CAppNavIRStates=CAppNavIRStates, cAppNavSNCurrentCMState=cAppNavSNCurrentCMState, cAppNavACTable=cAppNavACTable, cAppNavSNEntry=cAppNavSNEntry, cAppNavACG=cAppNavACG, ciscoAppNavMIBConform=ciscoAppNavMIBConform, PYSNMP_MODULE_ID=ciscoAppNavMIB, cAppNavServContextJoinState=cAppNavServContextJoinState, cAppNavACACGName=cAppNavACACGName, ciscoAppNavMIBGroups=ciscoAppNavMIBGroups, cAppNavServContextIndex=cAppNavServContextIndex, cAppNavSNServContextName=cAppNavSNServContextName, cAppNavSNIndex=cAppNavSNIndex, CAppNavCMStates=CAppNavCMStates, cAppNavServContextName=cAppNavServContextName, cAppNavACGGroup=cAppNavACGGroup, cAppNavACGIndex=cAppNavACGIndex, cAppNavSNSNGName=cAppNavSNSNGName, cAppNavACCurrentCMState=cAppNavACCurrentCMState, ciscoAppNavMIBCompliances=ciscoAppNavMIBCompliances, cAppNavSNGIndex=cAppNavSNGIndex, cAppNavSNGGroup=cAppNavSNGGroup, cAppNavACEntry=cAppNavACEntry, cAppNavACIpAddrType=cAppNavACIpAddrType, CAppNavServContextOpStates=CAppNavServContextOpStates, cAppNavACGroup=cAppNavACGroup, cAppNavSNTable=cAppNavSNTable, ciscoAppNavMIBObjects=ciscoAppNavMIBObjects, cAppNavACGTable=cAppNavACGTable, cAppNavServContextCurrOpState=cAppNavServContextCurrOpState, cAppNavServContextLastOpState=cAppNavServContextLastOpState, cAppNavSNIpAddrType=cAppNavSNIpAddrType, cAppNavServiceContextGroup=cAppNavServiceContextGroup, cAppNavACIndex=cAppNavACIndex, cAppNavACGEntry=cAppNavACGEntry, cAppNavAC=cAppNavAC, cAppNavSNGServContextName=cAppNavSNGServContextName, cAppNavACServContextName=cAppNavACServContextName, cAppNavServContextTable=cAppNavServContextTable, cAppNavACGServContextName=cAppNavACGServContextName, cAppNavACIpAddr=cAppNavACIpAddr, cAppNavServContext=cAppNavServContext, ciscoAppNavMIBCompliance=ciscoAppNavMIBCompliance, cAppNavACGName=cAppNavACGName, cAppNavServiceContextGroupRev1=cAppNavServiceContextGroupRev1, cAppNavServContextIRState=cAppNavServContextIRState, cAppNavSN=cAppNavSN, cAppNavSNG=cAppNavSNG)
