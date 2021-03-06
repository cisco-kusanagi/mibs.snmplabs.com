#
# PySNMP MIB module BGP4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BGP4-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, ModuleIdentity, MibIdentifier, NotificationType, Gauge32, Integer32, iso, Bits, TimeTicks, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Gauge32", "Integer32", "iso", "Bits", "TimeTicks", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bgp = ModuleIdentity((1, 3, 6, 1, 2, 1, 15))
if mibBuilder.loadTexts: bgp.setLastUpdated('9405050000Z')
if mibBuilder.loadTexts: bgp.setOrganization('IETF BGP Working Group')
if mibBuilder.loadTexts: bgp.setContactInfo(' John Chu (Editor) Postal: IBM Corp. P.O.Box 218 Yorktown Heights, NY 10598 US Tel: +1 914 945 3156 Fax: +1 914 945 2141 E-mail: jychu@watson.ibm.com')
if mibBuilder.loadTexts: bgp.setDescription('The MIB module for BGP-4.')
bgpVersion = MibScalar((1, 3, 6, 1, 2, 1, 15, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpVersion.setStatus('current')
if mibBuilder.loadTexts: bgpVersion.setDescription('Vector of supported BGP protocol version numbers. Each peer negotiates the version from this vector. Versions are identified via the string of bits contained within this object. The first octet contains bits 0 to 7, the second octet contains bits 8 to 15, and so on, with the most significant bit referring to the lowest bit number in the octet (e.g., the MSB of the first octet refers to bit 0). If a bit, i, is present and set, then the version (i+1) of the BGP is supported.')
bgpLocalAs = MibScalar((1, 3, 6, 1, 2, 1, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpLocalAs.setStatus('current')
if mibBuilder.loadTexts: bgpLocalAs.setDescription('The local autonomous system number.')
bgpPeerTable = MibTable((1, 3, 6, 1, 2, 1, 15, 3), )
if mibBuilder.loadTexts: bgpPeerTable.setStatus('current')
if mibBuilder.loadTexts: bgpPeerTable.setDescription('BGP peer table. This table contains, one entry per BGP peer, information about the connections with BGP peers.')
bgpPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 3, 1), ).setIndexNames((0, "BGP4-MIB", "bgpPeerRemoteAddr"))
if mibBuilder.loadTexts: bgpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: bgpPeerEntry.setDescription('Entry containing information about the connection with a BGP peer.')
bgpPeerIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerIdentifier.setStatus('current')
if mibBuilder.loadTexts: bgpPeerIdentifier.setDescription("The BGP Identifier of this entry's BGP peer.")
bgpPeerState = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerState.setStatus('current')
if mibBuilder.loadTexts: bgpPeerState.setDescription('The BGP peer connection state.')
bgpPeerAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerAdminStatus.setStatus('current')
if mibBuilder.loadTexts: bgpPeerAdminStatus.setDescription("The desired state of the BGP connection. A transition from 'stop' to 'start' will cause the BGP Start Event to be generated. A transition from 'start' to 'stop' will cause the BGP Stop Event to be generated. This parameter can be used to restart BGP peer connections. Care should be used in providing write access to this object without adequate authentication.")
bgpPeerNegotiatedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerNegotiatedVersion.setStatus('current')
if mibBuilder.loadTexts: bgpPeerNegotiatedVersion.setDescription('The negotiated version of BGP running between the two peers.')
bgpPeerLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalAddr.setStatus('current')
if mibBuilder.loadTexts: bgpPeerLocalAddr.setDescription("The local IP address of this entry's BGP connection.")
bgpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalPort.setStatus('current')
if mibBuilder.loadTexts: bgpPeerLocalPort.setDescription('The local port for the TCP connection between the BGP peers.')
bgpPeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAddr.setStatus('current')
if mibBuilder.loadTexts: bgpPeerRemoteAddr.setDescription("The remote IP address of this entry's BGP peer.")
bgpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemotePort.setStatus('current')
if mibBuilder.loadTexts: bgpPeerRemotePort.setDescription('The remote port for the TCP connection between the BGP peers. Note that the objects bgpPeerLocalAddr, bgpPeerLocalPort, bgpPeerRemoteAddr and bgpPeerRemotePort provide the appropriate reference to the standard MIB TCP connection table.')
bgpPeerRemoteAs = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAs.setStatus('current')
if mibBuilder.loadTexts: bgpPeerRemoteAs.setDescription('The remote autonomous system number.')
bgpPeerInUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdates.setStatus('current')
if mibBuilder.loadTexts: bgpPeerInUpdates.setDescription('The number of BGP UPDATE messages received on this connection. This object should be initialized to zero (0) when the connection is established.')
bgpPeerOutUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutUpdates.setStatus('current')
if mibBuilder.loadTexts: bgpPeerOutUpdates.setDescription('The number of BGP UPDATE messages transmitted on this connection. This object should be initialized to zero (0) when the connection is established.')
bgpPeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInTotalMessages.setStatus('current')
if mibBuilder.loadTexts: bgpPeerInTotalMessages.setDescription('The total number of messages received from the remote peer on this connection. This object should be initialized to zero when the connection is established.')
bgpPeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutTotalMessages.setStatus('current')
if mibBuilder.loadTexts: bgpPeerOutTotalMessages.setDescription('The total number of messages transmitted to the remote peer on this connection. This object should be initialized to zero when the connection is established.')
bgpPeerLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLastError.setStatus('current')
if mibBuilder.loadTexts: bgpPeerLastError.setDescription('The last error code and subcode seen by this peer on this connection. If no error has occurred, this field is zero. Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode.')
bgpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTransitions.setStatus('current')
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTransitions.setDescription('The total number of times the BGP FSM transitioned into the established state.')
bgpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTime.setStatus('current')
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTime.setDescription('This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state. It is set to zero when a new peer is configured or the router is booted.')
bgpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerConnectRetryInterval.setStatus('current')
if mibBuilder.loadTexts: bgpPeerConnectRetryInterval.setDescription('Time interval in seconds for the ConnectRetry timer. The suggested value for this timer is 120 seconds.')
bgpPeerHoldTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerHoldTime.setStatus('current')
if mibBuilder.loadTexts: bgpPeerHoldTime.setDescription('Time interval in seconds for the Hold Timer established with the peer. The value of this object is calculated by this BGP speaker by using the smaller of the value in bgpPeerHoldTimeConfigured and the Hold Time received in the OPEN message. This value must be at lease three seconds if it is not zero (0) in which case the Hold Timer has not been established with the peer, or, the value of bgpPeerHoldTimeConfigured is zero (0).')
bgpPeerKeepAlive = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerKeepAlive.setStatus('current')
if mibBuilder.loadTexts: bgpPeerKeepAlive.setDescription('Time interval in seconds for the KeepAlive timer established with the peer. The value of this object is calculated by this BGP speaker such that, when compared with bgpPeerHoldTime, it has the same proportion as what bgpPeerKeepAliveConfigured has when compared with bgpPeerHoldTimeConfigured. If the value of this object is zero (0), it indicates that the KeepAlive timer has not been established with the peer, or, the value of bgpPeerKeepAliveConfigured is zero (0).')
bgpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerHoldTimeConfigured.setStatus('current')
if mibBuilder.loadTexts: bgpPeerHoldTimeConfigured.setDescription('Time interval in seconds for the Hold Time configured for this BGP speaker with this peer. This value is placed in an OPEN message sent to this peer by this BGP speaker, and is compared with the Hold Time field in an OPEN message received from the peer when determining the Hold Time (bgpPeerHoldTime) with the peer. This value must not be less than three seconds if it is not zero (0) in which case the Hold Time is NOT to be established with the peer. The suggested value for this timer is 90 seconds.')
bgpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerKeepAliveConfigured.setStatus('current')
if mibBuilder.loadTexts: bgpPeerKeepAliveConfigured.setDescription("Time interval in seconds for the KeepAlive timer configured for this BGP speaker with this peer. The value of this object will only determine the KEEPALIVE messages' frequency relative to the value specified in bgpPeerHoldTimeConfigured; the actual time interval for the KEEPALIVE messages is indicated by bgpPeerKeepAlive. A reasonable maximum value for this timer would be configured to be one third of that of bgpPeerHoldTimeConfigured. If the value of this object is zero (0), no periodical KEEPALIVE messages are sent to the peer after the BGP connection has been established. The suggested value for this timer is 30 seconds.")
bgpPeerMinASOriginationInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerMinASOriginationInterval.setStatus('current')
if mibBuilder.loadTexts: bgpPeerMinASOriginationInterval.setDescription('Time interval in seconds for the MinASOriginationInterval timer. The suggested value for this timer is 15 seconds.')
bgpPeerMinRouteAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerMinRouteAdvertisementInterval.setStatus('current')
if mibBuilder.loadTexts: bgpPeerMinRouteAdvertisementInterval.setDescription('Time interval in seconds for the MinRouteAdvertisementInterval timer. The suggested value for this timer is 30 seconds.')
bgpPeerInUpdateElapsedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdateElapsedTime.setStatus('current')
if mibBuilder.loadTexts: bgpPeerInUpdateElapsedTime.setDescription('Elapsed time in seconds since the last BGP UPDATE message was received from the peer. Each time bgpPeerInUpdates is incremented, the value of this object is set to zero (0).')
bgpIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 15, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpIdentifier.setStatus('current')
if mibBuilder.loadTexts: bgpIdentifier.setDescription('The BGP Identifier of local system.')
bgp4PathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 6), )
if mibBuilder.loadTexts: bgp4PathAttrTable.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrTable.setDescription('The BGP-4 Received Path Attribute Table contains information about paths to destination networks received from all BGP4 peers.')
bgp4PathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 6, 1), ).setIndexNames((0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"), (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"), (0, "BGP4-MIB", "bgp4PathAttrPeer"))
if mibBuilder.loadTexts: bgp4PathAttrEntry.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrEntry.setDescription('Information about a path to a network.')
bgp4PathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrPeer.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrPeer.setDescription('The IP address of the peer where the path information was learned.')
bgp4PathAttrIpAddrPrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefixLen.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefixLen.setDescription('Length in bits of the IP address prefix in the Network Layer Reachability Information field.')
bgp4PathAttrIpAddrPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefix.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefix.setDescription('An IP address prefix in the Network Layer Reachability Information field. This object is an IP address containing the prefix with length specified by bgp4PathAttrIpAddrPrefixLen. Any bits beyond the length specified by bgp4PathAttrIpAddrPrefixLen are zeroed.')
bgp4PathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrOrigin.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrOrigin.setDescription('The ultimate origin of the path information.')
bgp4PathAttrASPathSegment = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrASPathSegment.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrASPathSegment.setDescription('The sequence of AS path segments. Each AS path segment is represented by a triple <type, length, value>. The type is a 1-octet field which has two possible values: 1 AS_SET: unordered set of ASs a route in the UPDATE message has traversed 2 AS_SEQUENCE: ordered set of ASs a route in the UPDATE message has traversed. The length is a 1-octet field containing the number of ASs in the value field. The value field contains one or more AS numbers, each AS is represented in the octet string as a pair of octets according to the following algorithm: first-byte-of-pair = ASNumber / 256; second-byte-of-pair = ASNumber & 255;')
bgp4PathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrNextHop.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrNextHop.setDescription('The address of the border router that should be used for the destination network.')
bgp4PathAttrMultiExitDisc = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrMultiExitDisc.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrMultiExitDisc.setDescription('This metric is used to discriminate between multiple exit points to an adjacent autonomous system. A value of -1 indicates the absence of this attribute.')
bgp4PathAttrLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrLocalPref.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrLocalPref.setDescription("The originating BGP4 speaker's degree of preference for an advertised route. A value of -1 indicates the absence of this attribute.")
bgp4PathAttrAtomicAggregate = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lessSpecificRrouteNotSelected", 1), ("lessSpecificRouteSelected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAtomicAggregate.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrAtomicAggregate.setDescription('Whether or not the local system has selected a less specific route without selecting a more specific route.')
bgp4PathAttrAggregatorAS = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAS.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAS.setDescription('The AS number of the last BGP4 speaker that performed route aggregation. A value of zero (0) indicates the absence of this attribute.')
bgp4PathAttrAggregatorAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAddr.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAddr.setDescription('The IP address of the last BGP4 speaker that performed route aggregation. A value of 0.0.0.0 indicates the absence of this attribute.')
bgp4PathAttrCalcLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrCalcLocalPref.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrCalcLocalPref.setDescription('The degree of preference calculated by the receiving BGP4 speaker for an advertised route. A value of -1 indicates the absence of this attribute.')
bgp4PathAttrBest = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrBest.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrBest.setDescription('An indication of whether or not this route was chosen as the best BGP4 route.')
bgp4PathAttrUnknown = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrUnknown.setStatus('current')
if mibBuilder.loadTexts: bgp4PathAttrUnknown.setDescription('One or more path attributes not understood by this BGP4 speaker. Size zero (0) indicates the absence of such attribute(s). Octets beyond the maximum size, if any, are not recorded by this object.')
bgpTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 7))
bgpEstablished = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 1)).setObjects(("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpEstablished.setStatus('current')
if mibBuilder.loadTexts: bgpEstablished.setDescription('The BGP Established event is generated when the BGP FSM enters the ESTABLISHED state.')
bgpBackwardTransition = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 2)).setObjects(("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpBackwardTransition.setStatus('current')
if mibBuilder.loadTexts: bgpBackwardTransition.setDescription('The BGPBackwardTransition Event is generated when the BGP FSM moves from a higher numbered state to a lower numbered state.')
mibBuilder.exportSymbols("BGP4-MIB", bgpPeerInUpdates=bgpPeerInUpdates, bgpPeerAdminStatus=bgpPeerAdminStatus, bgp4PathAttrMultiExitDisc=bgp4PathAttrMultiExitDisc, bgp4PathAttrAtomicAggregate=bgp4PathAttrAtomicAggregate, bgp4PathAttrUnknown=bgp4PathAttrUnknown, bgpPeerFsmEstablishedTime=bgpPeerFsmEstablishedTime, bgpPeerInUpdateElapsedTime=bgpPeerInUpdateElapsedTime, bgpPeerState=bgpPeerState, bgpPeerNegotiatedVersion=bgpPeerNegotiatedVersion, PYSNMP_MODULE_ID=bgp, bgpVersion=bgpVersion, bgp4PathAttrTable=bgp4PathAttrTable, bgpEstablished=bgpEstablished, bgp4PathAttrPeer=bgp4PathAttrPeer, bgpPeerLastError=bgpPeerLastError, bgpPeerOutUpdates=bgpPeerOutUpdates, bgpPeerRemotePort=bgpPeerRemotePort, bgpPeerLocalAddr=bgpPeerLocalAddr, bgpPeerKeepAliveConfigured=bgpPeerKeepAliveConfigured, bgp4PathAttrEntry=bgp4PathAttrEntry, bgp4PathAttrNextHop=bgp4PathAttrNextHop, bgpBackwardTransition=bgpBackwardTransition, bgpPeerInTotalMessages=bgpPeerInTotalMessages, bgp4PathAttrLocalPref=bgp4PathAttrLocalPref, bgp=bgp, bgpLocalAs=bgpLocalAs, bgpPeerRemoteAs=bgpPeerRemoteAs, bgp4PathAttrASPathSegment=bgp4PathAttrASPathSegment, bgp4PathAttrAggregatorAddr=bgp4PathAttrAggregatorAddr, bgpPeerLocalPort=bgpPeerLocalPort, bgp4PathAttrCalcLocalPref=bgp4PathAttrCalcLocalPref, bgp4PathAttrAggregatorAS=bgp4PathAttrAggregatorAS, bgpPeerHoldTime=bgpPeerHoldTime, bgpPeerMinRouteAdvertisementInterval=bgpPeerMinRouteAdvertisementInterval, bgp4PathAttrIpAddrPrefix=bgp4PathAttrIpAddrPrefix, bgpPeerIdentifier=bgpPeerIdentifier, bgpPeerRemoteAddr=bgpPeerRemoteAddr, bgpPeerKeepAlive=bgpPeerKeepAlive, bgpPeerFsmEstablishedTransitions=bgpPeerFsmEstablishedTransitions, bgp4PathAttrOrigin=bgp4PathAttrOrigin, bgpPeerMinASOriginationInterval=bgpPeerMinASOriginationInterval, bgp4PathAttrIpAddrPrefixLen=bgp4PathAttrIpAddrPrefixLen, bgp4PathAttrBest=bgp4PathAttrBest, bgpPeerTable=bgpPeerTable, bgpPeerConnectRetryInterval=bgpPeerConnectRetryInterval, bgpPeerHoldTimeConfigured=bgpPeerHoldTimeConfigured, bgpIdentifier=bgpIdentifier, bgpTraps=bgpTraps, bgpPeerOutTotalMessages=bgpPeerOutTotalMessages, bgpPeerEntry=bgpPeerEntry)
