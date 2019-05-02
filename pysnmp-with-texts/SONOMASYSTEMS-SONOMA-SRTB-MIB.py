#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-SRTB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-SRTB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, IpAddress, ModuleIdentity, iso, TimeTicks, ObjectIdentity, Unsigned32, Counter64, Bits, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "IpAddress", "ModuleIdentity", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonomaBridging, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaBridging")
srtBridging = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2))
srtBridgeNumber = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 1), Integer32().clone(65535)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtBridgeNumber.setStatus('obsolete')
if mibBuilder.loadTexts: srtBridgeNumber.setDescription('Obsoleted by vlanConfigBrNumber. Was: A bridge number uniquely identifies a bridge when more than one bridge is used to span the same segments. This object can have values between 0..15 inclusive and also a value 65535. When set to 65535, source routing on the unit is DISABLED.')
srtSourceRouteAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtSourceRouteAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteAgingTime.setDescription('If no frames from a source are received for this time, any associated routing information in the Source Route Table is purged. The granularity is seconds.')
srtPortTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3), )
if mibBuilder.loadTexts: srtPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortTable.setDescription('Table of Source Routing per Port parameters. ')
srtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-SRTB-MIB", "srtPortIfIndex"))
if mibBuilder.loadTexts: srtPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortEntry.setDescription('An entry in the logical port instanced SRT Port Table. ')
srtPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortIfIndex.setDescription('The port number of the port for which this entry contains Source Route management information.')
srtPortHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtPortHopCount.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortHopCount.setDescription('The maximum number of routing descriptors allowed in an All Paths or Spanning Tree Explorer frames.')
srtPortLocalSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtPortLocalSegment.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortLocalSegment.setDescription('The segment number that uniquely identifies the segment to which this port is connected. Current source routing protocols limit this value to the range: 0 through 4095. A value of 65535 signifies that no segment number is assigned to this port.')
srtPortLargestFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("srtMtu516", 1), ("srtMtu1500", 2), ("srtMtu2052", 3), ("srtMtu4472", 4), ("srtMtu8144", 5), ("srtMtu11407", 6), ("srtMtu17800", 7), ("srtMtu65535", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtPortLargestFrame.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortLargestFrame.setDescription('The maximum size of the INFO field (LLC and above) that this port can send/receive. It does not include any MAC level (framing) octets. The value of this object is used by this bridge to determine whether a modification of the LargestFrame (LF, see [14]) field of the Routing Control field of the Routing Information Field is necessary. Valid values as defined by the 802.5 source routing bridging specification[14] are 516, 1500, 2052, 4472, 8144, 11407, 17800, and 65535 octets. Behavior of the port when an illegal value is written is implementation specific. It is recommended that a reasonable legal value be chosen.')
srtPortSTESpanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto-span", 1), ("disabled", 2), ("forced", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtPortSTESpanMode.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortSTESpanMode.setDescription("Determines how this port behaves when presented with a Spanning Tree Explorer frame. The value 'disabled(2)' indicates that the port will not accept or send Spanning Tree Explorer packets; any STE packets received will be silently discarded. The value 'forced(3)' indicates the port will always accept and propagate Spanning Tree Explorer frames. This allows a manually configured Spanning Tree for this class of packet to be configured. Note that unlike transparent bridging this is not catastrophic to the network if there are loops. The value 'auto-span(1)' can only be returned by a bridge that both implements the Spanning Tree Protocol and has use of the protocol enabled on this port. The behavior of the port for Spanning Tree Explorer frames is determined by the state of dot1dStpPortState. If the port is in the 'forwarding' state, the frame will be accepted or propagated. Otherwise it will be silently discarded.")
srtPortSpecInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortSpecInFrames.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortSpecInFrames.setDescription("The number of specifically routed frames that have been received from this port's segment.")
srtPortSpecOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortSpecOutFrames.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortSpecOutFrames.setDescription('The number of specifically routed frames that this port has transmitted on its segment.')
srtPortAREInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortAREInFrames.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortAREInFrames.setDescription('The number of all paths explorer frames that have been received by this port from its segment.')
srtPortAREOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortAREOutFrames.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortAREOutFrames.setDescription('The number of all paths explorer frames that have been transmitted by this port on its segment.')
srtPortSteInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortSteInFrames.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortSteInFrames.setDescription('The number of spanning tree explorer frames that have been received by this port from its segment.')
srtPortSteOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortSteOutFrames.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortSteOutFrames.setDescription('The number of spanning tree explorer frames that have been transmitted by this port on its segment.')
srtPortSegmentMismatchDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortSegmentMismatchDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortSegmentMismatchDiscards.setDescription('The number of explorer frames that have been discarded by this port because the routing descriptor field contained an invalid adjacent segment value.')
srtPortDuplicateSegmentDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortDuplicateSegmentDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortDuplicateSegmentDiscards.setDescription('The number of frames that have been discarded by this port because the routing descriptor field contained a duplicate segment identifier.')
srtPortHopCountExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtPortHopCountExceededDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: srtPortHopCountExceededDiscards.setDescription('The number of explorer frames that have been discarded by this port because the Routing Information Field has exceeded the maximum route descriptor length.')
srtSourceRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4), )
if mibBuilder.loadTexts: srtSourceRouteTable.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteTable.setDescription('This table contains a list of stored destination address and the routing information fields which will be inserted in frames sent to those destinations.')
srtSourceRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-SRTB-MIB", "srtSourceRouteVlanID"), (0, "SONOMASYSTEMS-SONOMA-SRTB-MIB", "srtSourceRouteAddress"))
if mibBuilder.loadTexts: srtSourceRouteEntry.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteEntry.setDescription('An source route entry.')
srtSourceRouteVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtSourceRouteVlanID.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteVlanID.setDescription('This is the ID of the Vlan on which the address corresponding to this entry was learnt.')
srtSourceRouteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtSourceRouteAddress.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteAddress.setDescription('This is the source address which was stored when the Source Routing frame which contained it was processed by the SRTB. The address is in the form it was received from the ring network.')
srtSourceRouteRIF = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtSourceRouteRIF.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteRIF.setDescription('This object contains all the routing information which was extracted from the received Source Routed frame. The data is in the form it was received from the ring network')
srtSourceRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("permanent", 1), ("temporary", 2), ("respondWithARE", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtSourceRouteType.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteType.setDescription("This object represents the type of the entry. If the value returned is sameRing (1), then this indicates that the frame from which this entry was taken originated on our local ring. A value of locked (2) is used for entries which have been learned from ARE type frames. The value provisional(3)is used for frames which have been learned from STE frames and the responsWithARE (4) values is used to indicate that when a response is sent to this entry's address is should be sent as an ARE frame.")
srtSourceRouteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 3, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inOrder", 1), ("reverseOrder", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtSourceRouteDirection.setStatus('mandatory')
if mibBuilder.loadTexts: srtSourceRouteDirection.setDescription('If this object returns a value of inOrder(0), then this means that the D bit is zero and that the frame traverses the LANs in the order in which they are specified in the routing information field. Conversely, if the D bit is set to 1 the frame will traverse the LANs in the reverse order. The D bit is meaningful only or source routed frames (SRF). For STE and ARE frames the D bit is ignored and is not altered by the unit.')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-SRTB-MIB", srtSourceRouteVlanID=srtSourceRouteVlanID, srtPortSteOutFrames=srtPortSteOutFrames, srtSourceRouteAddress=srtSourceRouteAddress, srtSourceRouteAgingTime=srtSourceRouteAgingTime, srtPortDuplicateSegmentDiscards=srtPortDuplicateSegmentDiscards, srtPortTable=srtPortTable, srtPortLargestFrame=srtPortLargestFrame, srtSourceRouteEntry=srtSourceRouteEntry, srtBridgeNumber=srtBridgeNumber, srtPortSpecOutFrames=srtPortSpecOutFrames, srtPortHopCount=srtPortHopCount, srtPortEntry=srtPortEntry, srtPortLocalSegment=srtPortLocalSegment, srtPortAREOutFrames=srtPortAREOutFrames, srtSourceRouteTable=srtSourceRouteTable, srtPortHopCountExceededDiscards=srtPortHopCountExceededDiscards, srtPortIfIndex=srtPortIfIndex, srtPortSpecInFrames=srtPortSpecInFrames, srtPortSegmentMismatchDiscards=srtPortSegmentMismatchDiscards, srtPortSTESpanMode=srtPortSTESpanMode, srtSourceRouteRIF=srtSourceRouteRIF, srtBridging=srtBridging, srtPortAREInFrames=srtPortAREInFrames, srtSourceRouteType=srtSourceRouteType, srtSourceRouteDirection=srtSourceRouteDirection, srtPortSteInFrames=srtPortSteInFrames)
