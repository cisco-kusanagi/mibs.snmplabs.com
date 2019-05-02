#
# PySNMP MIB module BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, NotificationType, Integer32, Counter64, Counter32, iso, ModuleIdentity, Unsigned32, MibIdentifier, Gauge32, mib_2, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "NotificationType", "Integer32", "Counter64", "Counter32", "iso", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "mib-2", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

dot1dBridge = MibIdentifier((1, 3, 6, 1, 2, 1, 17))
dot1dBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 1))
dot1dStp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2))
dot1dSr = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 3))
dot1dTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 4))
dot1dStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 5))
dot1dBaseBridgeAddress = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBaseBridgeAddress.setReference('IEEE 802.1D-1990: Sections 6.4.1.1.3 and 3.12.5')
if mibBuilder.loadTexts: dot1dBaseBridgeAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBaseBridgeAddress.setDescription('The MAC address used by this bridge when it must be referred to in a unique fashion. It is recommended that this be the numerically smallest MAC address of all ports that belong to this bridge. However it is only required to be unique. When concatenated with dot1dStpPriority a unique BridgeIdentifier is formed which is used in the Spanning Tree Protocol.')
dot1dBaseNumPorts = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBaseNumPorts.setReference('IEEE 802.1D-1990: Section 6.4.1.1.3')
if mibBuilder.loadTexts: dot1dBaseNumPorts.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBaseNumPorts.setDescription('The number of ports controlled by this bridging entity.')
dot1dBaseType = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBaseType.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBaseType.setDescription('Indicates what type of bridging this bridge can perform. If a bridge is actually performing a certain type of bridging this will be indicated by entries in the port table for the given type.')
dot1dBasePortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 1, 4), )
if mibBuilder.loadTexts: dot1dBasePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePortTable.setDescription('A table that contains generic information about every port that is associated with this bridge. Transparent, source-route, and srt ports are included.')
dot1dBasePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 1, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: dot1dBasePortEntry.setReference('IEEE 802.1D-1990: Section 6.4.2, 6.6.1')
if mibBuilder.loadTexts: dot1dBasePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePortEntry.setDescription('A list of information for each port of the bridge.')
dot1dBasePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBasePort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePort.setDescription('The port number of the port for which this entry contains bridge management information.')
dot1dBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBasePortIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePortIfIndex.setDescription('The value of the instance of the ifIndex object, defined in MIB-II, for the interface corresponding to this port.')
dot1dBasePortCircuit = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBasePortCircuit.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePortCircuit.setDescription('For a port which (potentially) has the same value of dot1dBasePortIfIndex as another port on the same bridge, this object contains the name of an object instance unique to this port. For example, in the case where multiple ports correspond one- to-one with multiple X.25 virtual circuits, this value might identify an (e.g., the first) object instance associated with the X.25 virtual circuit corresponding to this port. For a port which has a unique value of dot1dBasePortIfIndex, this object can have the value { 0 0 }.')
dot1dBasePortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBasePortDelayExceededDiscards.setReference('IEEE 802.1D-1990: Section 6.6.1.1.3')
if mibBuilder.loadTexts: dot1dBasePortDelayExceededDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePortDelayExceededDiscards.setDescription('The number of frames discarded by this port due to excessive transit delay through the bridge. It is incremented by both transparent and source route bridges.')
dot1dBasePortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dBasePortMtuExceededDiscards.setReference('IEEE 802.1D-1990: Section 6.6.1.1.3')
if mibBuilder.loadTexts: dot1dBasePortMtuExceededDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dBasePortMtuExceededDiscards.setDescription('The number of frames discarded by this port due to an excessive size. It is incremented by both transparent and source route bridges.')
dot1dStpProtocolSpecification = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpProtocolSpecification.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpProtocolSpecification.setDescription("An indication of what version of the Spanning Tree Protocol is being run. The value 'decLb100(2)' indicates the DEC LANbridge 100 Spanning Tree protocol. IEEE 802.1d implementations will return 'ieee8021d(3)'. If future versions of the IEEE Spanning Tree Protocol are released that are incompatible with the current version a new value will be defined.")
dot1dStpPriority = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPriority.setReference('IEEE 802.1D-1990: Section 4.5.3.7')
if mibBuilder.loadTexts: dot1dStpPriority.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPriority.setDescription('The value of the write-able portion of the Bridge ID, i.e., the first two octets of the (8 octet long) Bridge ID. The other (last) 6 octets of the Bridge ID are given by the value of dot1dBaseBridgeAddress.')
dot1dStpTimeSinceTopologyChange = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpTimeSinceTopologyChange.setReference('IEEE 802.1D-1990: Section 6.8.1.1.3')
if mibBuilder.loadTexts: dot1dStpTimeSinceTopologyChange.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpTimeSinceTopologyChange.setDescription('The time (in hundredths of a second) since the last time a topology change was detected by the bridge entity.')
dot1dStpTopChanges = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpTopChanges.setReference('IEEE 802.1D-1990: Section 6.8.1.1.3')
if mibBuilder.loadTexts: dot1dStpTopChanges.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpTopChanges.setDescription('The total number of topology changes detected by this bridge since the management entity was last reset or initialized.')
dot1dStpDesignatedRoot = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpDesignatedRoot.setReference('IEEE 802.1D-1990: Section 4.5.3.1')
if mibBuilder.loadTexts: dot1dStpDesignatedRoot.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpDesignatedRoot.setDescription('The bridge identifier of the root of the spanning tree as determined by the Spanning Tree Protocol as executed by this node. This value is used as the Root Identifier parameter in all Configuration Bridge PDUs originated by this node.')
dot1dStpRootCost = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpRootCost.setReference('IEEE 802.1D-1990: Section 4.5.3.2')
if mibBuilder.loadTexts: dot1dStpRootCost.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpRootCost.setDescription('The cost of the path to the root as seen from this bridge.')
dot1dStpRootPort = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpRootPort.setReference('IEEE 802.1D-1990: Section 4.5.3.3')
if mibBuilder.loadTexts: dot1dStpRootPort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpRootPort.setDescription('The port number of the port which offers the lowest cost path from this bridge to the root bridge.')
dot1dStpMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 8), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpMaxAge.setReference('IEEE 802.1D-1990: Section 4.5.3.4')
if mibBuilder.loadTexts: dot1dStpMaxAge.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpMaxAge.setDescription('The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second. This is the actual value that this bridge is currently using.')
dot1dStpHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 9), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpHelloTime.setReference('IEEE 802.1D-1990: Section 4.5.3.5')
if mibBuilder.loadTexts: dot1dStpHelloTime.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpHelloTime.setDescription('The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree or trying to become so, in units of hundredths of a second. This is the actual value that this bridge is currently using.')
dot1dStpHoldTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpHoldTime.setReference('IEEE 802.1D-1990: Section 4.5.3.14')
if mibBuilder.loadTexts: dot1dStpHoldTime.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpHoldTime.setDescription('This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second.')
dot1dStpForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 11), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpForwardDelay.setReference('IEEE 802.1D-1990: Section 4.5.3.6')
if mibBuilder.loadTexts: dot1dStpForwardDelay.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpForwardDelay.setDescription('This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state. The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state. This value is also used, when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. [Note that this value is the one that this bridge is currently using, in contrast to dot1dStpBridgeForwardDelay which is the value that this bridge and all others would start using if/when this bridge were to become the root.]')
dot1dStpBridgeMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 12), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpBridgeMaxAge.setReference('IEEE 802.1D-1990: Section 4.5.3.8')
if mibBuilder.loadTexts: dot1dStpBridgeMaxAge.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpBridgeMaxAge.setDescription('The value that all bridges use for MaxAge when this bridge is acting as the root. Note that 802.1D-1990 specifies that the range for this parameter is related to the value of dot1dStpBridgeHelloTime. The granularity of this timer is specified by 802.1D-1990 to be 1 second. An agent may return a badValue error if a set is attempted to a value which is not a whole number of seconds.')
dot1dStpBridgeHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpBridgeHelloTime.setReference('IEEE 802.1D-1990: Section 4.5.3.9')
if mibBuilder.loadTexts: dot1dStpBridgeHelloTime.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpBridgeHelloTime.setDescription('The value that all bridges use for HelloTime when this bridge is acting as the root. The granularity of this timer is specified by 802.1D- 1990 to be 1 second. An agent may return a badValue error if a set is attempted to a value which is not a whole number of seconds.')
dot1dStpBridgeForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpBridgeForwardDelay.setReference('IEEE 802.1D-1990: Section 4.5.3.10')
if mibBuilder.loadTexts: dot1dStpBridgeForwardDelay.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpBridgeForwardDelay.setDescription('The value that all bridges use for ForwardDelay when this bridge is acting as the root. Note that 802.1D-1990 specifies that the range for this parameter is related to the value of dot1dStpBridgeMaxAge. The granularity of this timer is specified by 802.1D-1990 to be 1 second. An agent may return a badValue error if a set is attempted to a value which is not a whole number of seconds.')
dot1dStpPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 2, 15), )
if mibBuilder.loadTexts: dot1dStpPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortTable.setDescription('A table that contains port-specific information for the Spanning Tree Protocol.')
dot1dStpPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 2, 15, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: dot1dStpPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortEntry.setDescription('A list of information maintained by every port about the Spanning Tree Protocol state for that port.')
dot1dStpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPort.setReference('IEEE 802.1D-1990: Section 6.8.2.1.2')
if mibBuilder.loadTexts: dot1dStpPort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPort.setDescription('The port number of the port for which this entry contains Spanning Tree Protocol management information.')
dot1dStpPortPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortPriority.setReference('IEEE 802.1D-1990: Section 4.5.5.1')
if mibBuilder.loadTexts: dot1dStpPortPriority.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortPriority.setDescription('The value of the priority field which is contained in the first (in network byte order) octet of the (2 octet long) Port ID. The other octet of the Port ID is given by the value of dot1dStpPort.')
dot1dStpPortState = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortState.setReference('IEEE 802.1D-1990: Section 4.5.5.2')
if mibBuilder.loadTexts: dot1dStpPortState.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortState.setDescription("The port's current state as defined by application of the Spanning Tree Protocol. This state controls what action a port takes on reception of a frame. If the bridge has detected a port that is malfunctioning it will place that port into the broken(6) state. For ports which are disabled (see dot1dStpPortEnable), this object will have a value of disabled(1).")
dot1dStpPortEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortEnable.setReference('IEEE 802.1D-1990: Section 4.5.5.2')
if mibBuilder.loadTexts: dot1dStpPortEnable.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortEnable.setDescription('The enabled/disabled status of the port.')
dot1dStpPortPathCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortPathCost.setReference('IEEE 802.1D-1990: Section 4.5.5.3')
if mibBuilder.loadTexts: dot1dStpPortPathCost.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortPathCost.setDescription('The contribution of this port to the path cost of paths towards the spanning tree root which include this port. 802.1D-1990 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.')
dot1dStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortDesignatedRoot.setReference('IEEE 802.1D-1990: Section 4.5.5.4')
if mibBuilder.loadTexts: dot1dStpPortDesignatedRoot.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortDesignatedRoot.setDescription('The unique Bridge Identifier of the Bridge recorded as the Root in the Configuration BPDUs transmitted by the Designated Bridge for the segment to which the port is attached.')
dot1dStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortDesignatedCost.setReference('IEEE 802.1D-1990: Section 4.5.5.5')
if mibBuilder.loadTexts: dot1dStpPortDesignatedCost.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortDesignatedCost.setDescription('The path cost of the Designated Port of the segment connected to this port. This value is compared to the Root Path Cost field in received bridge PDUs.')
dot1dStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 8), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortDesignatedBridge.setReference('IEEE 802.1D-1990: Section 4.5.5.6')
if mibBuilder.loadTexts: dot1dStpPortDesignatedBridge.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortDesignatedBridge.setDescription("The Bridge Identifier of the bridge which this port considers to be the Designated Bridge for this port's segment.")
dot1dStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortDesignatedPort.setReference('IEEE 802.1D-1990: Section 4.5.5.7')
if mibBuilder.loadTexts: dot1dStpPortDesignatedPort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortDesignatedPort.setDescription("The Port Identifier of the port on the Designated Bridge for this port's segment.")
dot1dStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortForwardTransitions.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStpPortForwardTransitions.setDescription('The number of times this port has transitioned from the Learning state to the Forwarding state.')
dot1dTpLearnedEntryDiscards = MibScalar((1, 3, 6, 1, 2, 1, 17, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpLearnedEntryDiscards.setReference('IEEE 802.1D-1990: Section 6.7.1.1.3')
if mibBuilder.loadTexts: dot1dTpLearnedEntryDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpLearnedEntryDiscards.setDescription('The total number of Forwarding Database entries, which have been or would have been learnt, but have been discarded due to a lack of space to store them in the Forwarding Database. If this counter is increasing, it indicates that the Forwarding Database is regularly becoming full (a condition which has unpleasant performance effects on the subnetwork). If this counter has a significant value but is not presently increasing, it indicates that the problem has been occurring but is not persistent.')
dot1dTpAgingTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dTpAgingTime.setReference('IEEE 802.1D-1990: Section 6.7.1.1.3')
if mibBuilder.loadTexts: dot1dTpAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpAgingTime.setDescription('The timeout period in seconds for aging out dynamically learned forwarding information. 802.1D-1990 recommends a default of 300 seconds.')
dot1dTpFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 3), )
if mibBuilder.loadTexts: dot1dTpFdbTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpFdbTable.setDescription('A table that contains information about unicast entries for which the bridge has forwarding and/or filtering information. This information is used by the transparent bridging function in determining how to propagate a received frame.')
dot1dTpFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
if mibBuilder.loadTexts: dot1dTpFdbEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpFdbEntry.setDescription('Information about a specific unicast MAC address for which the bridge has some forwarding and/or filtering information.')
dot1dTpFdbAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpFdbAddress.setReference('IEEE 802.1D-1990: Section 3.9.1, 3.9.2')
if mibBuilder.loadTexts: dot1dTpFdbAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpFdbAddress.setDescription('A unicast MAC address for which the bridge has forwarding and/or filtering information.')
dot1dTpFdbPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpFdbPort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpFdbPort.setDescription("Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1dTpFdbAddress has been seen. A value of '0' indicates that the port number has not been learned but that the bridge does have some forwarding/filtering information about this address (e.g. in the dot1dStaticTable). Implementors are encouraged to assign the port value to this object whenever it is learned even for addresses for which the corresponding value of dot1dTpFdbStatus is not learned(3).")
dot1dTpFdbStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpFdbStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpFdbStatus.setDescription("The status of this entry. The meanings of the values are: other(1) : none of the following. This would include the case where some other MIB object (not the corresponding instance of dot1dTpFdbPort, nor an entry in the dot1dStaticTable) is being used to determine if and how frames addressed to the value of the corresponding instance of dot1dTpFdbAddress are being forwarded. invalid(2) : this entry is not longer valid (e.g., it was learned but has since aged-out), but has not yet been flushed from the table. learned(3) : the value of the corresponding instance of dot1dTpFdbPort was learned, and is being used. self(4) : the value of the corresponding instance of dot1dTpFdbAddress represents one of the bridge's addresses. The corresponding instance of dot1dTpFdbPort indicates which of the bridge's ports has this address. mgmt(5) : the value of the corresponding instance of dot1dTpFdbAddress is also the value of an existing instance of dot1dStaticAddress.")
dot1dTpPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 4), )
if mibBuilder.loadTexts: dot1dTpPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPortTable.setDescription('A table that contains information about every port that is associated with this transparent bridge.')
dot1dTpPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
if mibBuilder.loadTexts: dot1dTpPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPortEntry.setDescription('A list of information for each port of a transparent bridge.')
dot1dTpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpPort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPort.setDescription('The port number of the port for which this entry contains Transparent bridging management information.')
dot1dTpPortMaxInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpPortMaxInfo.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPortMaxInfo.setDescription('The maximum size of the INFO (non-MAC) field that this port will receive or transmit.')
dot1dTpPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpPortInFrames.setReference('IEEE 802.1D-1990: Section 6.6.1.1.3')
if mibBuilder.loadTexts: dot1dTpPortInFrames.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPortInFrames.setDescription('The number of frames that have been received by this port from its segment. Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames.')
dot1dTpPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpPortOutFrames.setReference('IEEE 802.1D-1990: Section 6.6.1.1.3')
if mibBuilder.loadTexts: dot1dTpPortOutFrames.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPortOutFrames.setDescription('The number of frames that have been transmitted by this port to its segment. Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames.')
dot1dTpPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dTpPortInDiscards.setReference('IEEE 802.1D-1990: Section 6.6.1.1.3')
if mibBuilder.loadTexts: dot1dTpPortInDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dTpPortInDiscards.setDescription('Count of valid frames received which were discarded (i.e., filtered) by the Forwarding Process.')
dot1dStaticTable = MibTable((1, 3, 6, 1, 2, 1, 17, 5, 1), )
if mibBuilder.loadTexts: dot1dStaticTable.setReference('IEEE 802.1D-1990: Section 6.7.2')
if mibBuilder.loadTexts: dot1dStaticTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStaticTable.setDescription('A table containing filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific destination addresses are allowed to be forwarded. The value of zero in this table as the port number from which frames with a specific destination address are received, is used to specify all ports for which there is no specific entry in this table for that particular destination address. Entries are valid for unicast and for group/broadcast addresses.')
dot1dStaticEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 5, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dStaticAddress"), (0, "BRIDGE-MIB", "dot1dStaticReceivePort"))
if mibBuilder.loadTexts: dot1dStaticEntry.setReference('IEEE 802.1D-1990: Section 6.7.2')
if mibBuilder.loadTexts: dot1dStaticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStaticEntry.setDescription('Filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from a specific port and containing a specific destination address are allowed to be forwarded.')
dot1dStaticAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStaticAddress.setReference('IEEE 802.1D-1990: Section 3.9.1, 3.9.2')
if mibBuilder.loadTexts: dot1dStaticAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStaticAddress.setDescription("The destination MAC address in a frame to which this entry's filtering information applies. This object can take the value of a unicast address, a group address or the broadcast address.")
dot1dStaticReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStaticReceivePort.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStaticReceivePort.setDescription("Either the value '0', or the port number of the port from which a frame must be received in order for this entry's filtering information to apply. A value of zero indicates that this entry applies on all ports of the bridge for which there is no other applicable entry.")
dot1dStaticAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStaticAllowedToGoTo.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStaticAllowedToGoTo.setDescription("The set of ports to which frames received from a specific port and destined for a specific MAC address, are allowed to be forwarded. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'. (Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant.) The default value of this object is a string of ones of appropriate length.")
dot1dStaticStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStaticStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dot1dStaticStatus.setDescription('This object indicates the status of this entry. The default value is permanent(3). other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. invalid(2) - writing this value to the object removes the corresponding entry. permanent(3) - this entry is currently in use and will remain so after the next reset of the bridge. deleteOnReset(4) - this entry is currently in use and will remain so until the next reset of the bridge. deleteOnTimeout(5) - this entry is currently in use and will remain so until it is aged out.')
newRoot = NotificationType((1, 3, 6, 1, 2, 1, 17) + (0,1))
if mibBuilder.loadTexts: newRoot.setDescription('The newRoot trap indicates that the sending agent has become the new root of the Spanning Tree; the trap is sent by a bridge soon after its election as the new root, e.g., upon expiration of the Topology Change Timer immediately subsequent to its election. Implementation of this trap is optional.')
topologyChange = NotificationType((1, 3, 6, 1, 2, 1, 17) + (0,2))
if mibBuilder.loadTexts: topologyChange.setDescription('A topologyChange trap is sent by a bridge when any of its configured ports transitions from the Learning state to the Forwarding state, or from the Forwarding state to the Blocking state. The trap is not sent if a newRoot trap is sent for the same transition. Implementation of this trap is optional.')
mibBuilder.exportSymbols("BRIDGE-MIB", dot1dStpPortDesignatedBridge=dot1dStpPortDesignatedBridge, dot1dStatic=dot1dStatic, dot1dStpPortForwardTransitions=dot1dStpPortForwardTransitions, dot1dStpPort=dot1dStpPort, dot1dTpPortMaxInfo=dot1dTpPortMaxInfo, dot1dStaticStatus=dot1dStaticStatus, dot1dBaseType=dot1dBaseType, dot1dBasePortMtuExceededDiscards=dot1dBasePortMtuExceededDiscards, dot1dStpProtocolSpecification=dot1dStpProtocolSpecification, dot1dStpRootCost=dot1dStpRootCost, dot1dStp=dot1dStp, dot1dStaticReceivePort=dot1dStaticReceivePort, dot1dStpBridgeForwardDelay=dot1dStpBridgeForwardDelay, dot1dStpMaxAge=dot1dStpMaxAge, dot1dStpBridgeMaxAge=dot1dStpBridgeMaxAge, dot1dTpFdbTable=dot1dTpFdbTable, dot1dTpFdbPort=dot1dTpFdbPort, dot1dTpPortOutFrames=dot1dTpPortOutFrames, dot1dTpLearnedEntryDiscards=dot1dTpLearnedEntryDiscards, dot1dBasePortEntry=dot1dBasePortEntry, dot1dTpPortInDiscards=dot1dTpPortInDiscards, newRoot=newRoot, dot1dStpBridgeHelloTime=dot1dStpBridgeHelloTime, topologyChange=topologyChange, dot1dTpAgingTime=dot1dTpAgingTime, dot1dTpPortEntry=dot1dTpPortEntry, dot1dSr=dot1dSr, dot1dStpPriority=dot1dStpPriority, dot1dTpFdbEntry=dot1dTpFdbEntry, dot1dBasePortDelayExceededDiscards=dot1dBasePortDelayExceededDiscards, dot1dStaticAddress=dot1dStaticAddress, dot1dBasePortCircuit=dot1dBasePortCircuit, dot1dBasePort=dot1dBasePort, dot1dStpTimeSinceTopologyChange=dot1dStpTimeSinceTopologyChange, dot1dStpPortPriority=dot1dStpPortPriority, dot1dBaseNumPorts=dot1dBaseNumPorts, dot1dStpPortEntry=dot1dStpPortEntry, dot1dStpDesignatedRoot=dot1dStpDesignatedRoot, dot1dBasePortIfIndex=dot1dBasePortIfIndex, dot1dStpPortEnable=dot1dStpPortEnable, dot1dTpFdbStatus=dot1dTpFdbStatus, dot1dStpPortDesignatedCost=dot1dStpPortDesignatedCost, dot1dTp=dot1dTp, dot1dBaseBridgeAddress=dot1dBaseBridgeAddress, dot1dStpPortPathCost=dot1dStpPortPathCost, dot1dStpForwardDelay=dot1dStpForwardDelay, dot1dStpPortState=dot1dStpPortState, dot1dStaticEntry=dot1dStaticEntry, dot1dBase=dot1dBase, dot1dStpPortDesignatedRoot=dot1dStpPortDesignatedRoot, BridgeId=BridgeId, dot1dStpTopChanges=dot1dStpTopChanges, dot1dStpHoldTime=dot1dStpHoldTime, dot1dTpFdbAddress=dot1dTpFdbAddress, dot1dBridge=dot1dBridge, dot1dStpPortDesignatedPort=dot1dStpPortDesignatedPort, dot1dStpRootPort=dot1dStpRootPort, Timeout=Timeout, dot1dStaticAllowedToGoTo=dot1dStaticAllowedToGoTo, dot1dStpHelloTime=dot1dStpHelloTime, dot1dStaticTable=dot1dStaticTable, dot1dTpPortTable=dot1dTpPortTable, dot1dBasePortTable=dot1dBasePortTable, dot1dTpPort=dot1dTpPort, dot1dStpPortTable=dot1dStpPortTable, dot1dTpPortInFrames=dot1dTpPortInFrames, MacAddress=MacAddress)
