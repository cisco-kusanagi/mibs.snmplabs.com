#
# PySNMP MIB module BIANCA-BRICK-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-IPX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Counter32, Integer32, Unsigned32, Bits, Counter64, Gauge32, TimeTicks, iso, IpAddress, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Counter32", "Integer32", "Unsigned32", "Bits", "Counter64", "Gauge32", "TimeTicks", "iso", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboipx = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 9))
ipxClientTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 9, 1), )
if mibBuilder.loadTexts: ipxClientTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxClientTable.setDescription('Each entry describes a client that has connected via WAN 2')
ipxClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-IPX-MIB", "ipxClientCircIndex"))
if mibBuilder.loadTexts: ipxClientEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxClientEntry.setDescription('')
ipxClientNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxClientNode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxClientNode.setDescription('The dynamically assigned Node Id of the client')
ipxClientCircIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxClientCircIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxClientCircIndex.setDescription('The dynamically assigned Network Number of the client')
ipxClientReconns = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxClientReconns.setStatus('mandatory')
if mibBuilder.loadTexts: ipxClientReconns.setDescription('The number of reconnections')
ipxAllowTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 9, 2), )
if mibBuilder.loadTexts: ipxAllowTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowTable.setDescription('Each entry describes a rule for filtering IPX packets. Only IPX packets matching all of those rules will be delivered.')
ipxAllowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1), ).setIndexNames((0, "BIANCA-BRICK-IPX-MIB", "ipxAllowPktTypeMode"), (0, "BIANCA-BRICK-IPX-MIB", "ipxAllowSrcIfIndexMode"))
if mibBuilder.loadTexts: ipxAllowEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowEntry.setDescription('')
ipxAllowPktTypeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowPktTypeMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowPktTypeMode.setDescription("The IPX packet type will be checked if this field is set to 'verify'")
ipxAllowPktType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(256, 1, 4, 5, 17, 20))).clone(namedValues=NamedValues(("unknown", 256), ("rip", 1), ("sap", 4), ("spx", 5), ("ncp", 17), ("netbios", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowPktType.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowPktType.setDescription('The various IPX packet types')
ipxAllowDstIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("up", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstIfStatus.setDescription("Set this value to 'up', if packets should only be forwarded to active (dialup-)links")
ipxAllowDstNetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstNetMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstNetMode.setDescription("The IPX destination network address will be checked if this field is set to 'verify'")
ipxAllowDstNet = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstNet.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstNet.setDescription('The IPX destination network address')
ipxAllowDstNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstNodeMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstNodeMode.setDescription("The IPX destination node address will be checked if this field is set to 'verify'")
ipxAllowDstNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstNode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstNode.setDescription('The IPX destination node address')
ipxAllowDstSockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstSockMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstSockMode.setDescription("The IPX destination socket number will be checked if this field is set to 'verify'")
ipxAllowDstSock = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowDstSock.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowDstSock.setDescription('The destination socket')
ipxAllowSrcIfIndexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcIfIndexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcIfIndexMode.setDescription("The index of the receiving interface will be checked if this field is set to 'verify'")
ipxAllowSrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcIfIndex.setDescription('The index of the receiving interface')
ipxAllowSrcNetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcNetMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcNetMode.setDescription("The IPX source network address will be checked if this field is set to 'verify'")
ipxAllowSrcNet = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcNet.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcNet.setDescription('The IPX source network address')
ipxAllowSrcNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcNodeMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcNodeMode.setDescription("The IPX source node address will be checked if this field is set to 'verify'")
ipxAllowSrcNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcNode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcNode.setDescription('The IPX source node address')
ipxAllowSrcSockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcSockMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcSockMode.setDescription("The IPX source socket number will be checked if this field is set to 'verify'")
ipxAllowSrcSock = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAllowSrcSock.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAllowSrcSock.setDescription('The source socket')
ipxDenyTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 9, 3), )
if mibBuilder.loadTexts: ipxDenyTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyTable.setDescription('Each entry describes a rule for filtering IPX packets. IPX packets matching any of those rules will be discarded.')
ipxDenyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1), ).setIndexNames((0, "BIANCA-BRICK-IPX-MIB", "ipxDenyPktTypeMode"), (0, "BIANCA-BRICK-IPX-MIB", "ipxDenySrcIfIndexMode"))
if mibBuilder.loadTexts: ipxDenyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyEntry.setDescription('')
ipxDenyPktTypeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyPktTypeMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyPktTypeMode.setDescription("The IPX packet type will be checked if this field is set to 'verify'")
ipxDenyPktType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(256, 1, 4, 5, 17, 20))).clone(namedValues=NamedValues(("unknown", 256), ("rip", 1), ("sap", 4), ("spx", 5), ("ncp", 17), ("netbios", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyPktType.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyPktType.setDescription('The various IPX packet types')
ipxDenyDstIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("dormant", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstIfStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstIfStatus.setDescription("Set this value to 'dormant', if packets should not be forwarded to sleeping (dialup-)links")
ipxDenyDstNetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstNetMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstNetMode.setDescription("The IPX destination network address will be checked if this field is set to 'verify'")
ipxDenyDstNet = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstNet.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstNet.setDescription('The IPX destination network address')
ipxDenyDstNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstNodeMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstNodeMode.setDescription("The IPX destination node address will be checked if this field is set to 'verify'")
ipxDenyDstNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstNode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstNode.setDescription('The IPX destination node address')
ipxDenyDstSockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstSockMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstSockMode.setDescription("The destination socket will be checked if this field is set to 'verify'")
ipxDenyDstSock = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenyDstSock.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenyDstSock.setDescription('The destination socket')
ipxDenySrcIfIndexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcIfIndexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcIfIndexMode.setDescription("The index of the receiving interface will be checked if this field is set to 'verify'")
ipxDenySrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcIfIndex.setDescription('The index of the receiving interface')
ipxDenySrcNetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcNetMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcNetMode.setDescription("The IPX source socket number will be checked if this field is set to 'verify'")
ipxDenySrcNet = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcNet.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcNet.setDescription('The IPX source network address')
ipxDenySrcNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcNodeMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcNodeMode.setDescription("The IPX destination node address will be checked if this field is set to 'verify'")
ipxDenySrcNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcNode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcNode.setDescription('The IPX destination node address')
ipxDenySrcSockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcSockMode.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcSockMode.setDescription("The IPX source socket number will be checked if this field is set to 'verify'")
ipxDenySrcSock = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxDenySrcSock.setStatus('mandatory')
if mibBuilder.loadTexts: ipxDenySrcSock.setDescription('The source socket')
ipxAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 9, 4))
ipxAdmSpxSpoofing = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmSpxSpoofing.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmSpxSpoofing.setDescription('Enable/disable SPX watchdog spoofing (on WAN links only)')
ipxAdmIpxSpoofing = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmIpxSpoofing.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmIpxSpoofing.setDescription('Enable/disable IPX watchdog spoofing (on WAN links only)')
ipxAdmNETBIOSRepl = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("lan-only", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmNETBIOSRepl.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmNETBIOSRepl.setDescription('Handling of replicated NetBIOS broadcasts: off : dont replicate at all on : enable normal replication lan_only: dont replicate on WAN links')
ipxAdmSpxVerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmSpxVerTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmSpxVerTimeout.setDescription('Idle time SPX will wait before sending a watchdog')
ipxAdmSpxAbrTimeout = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmSpxAbrTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmSpxAbrTimeout.setDescription('Idle time SPX will wait before aborting the connection')
ipxAdmRIPSAPOffset = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmRIPSAPOffset.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmRIPSAPOffset.setDescription('Offset interval between RIP-Response and SAP-Response')
ipxAdmLearnStatics = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("done", 1), ("rip", 2), ("sap", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxAdmLearnStatics.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmLearnStatics.setDescription('take entries from ipxDestTable and/or ipxDestServTable and put them into ipxStaticRoute-/ipxStaticServTable')
ipxAdmSpxConns = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxAdmSpxConns.setStatus('mandatory')
if mibBuilder.loadTexts: ipxAdmSpxConns.setDescription('Number of spoofed SPX connections')
sapAllowTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 9, 5), )
if mibBuilder.loadTexts: sapAllowTable.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowTable.setDescription('Each entry describes a rule for filtering services. Only services matching any of those rules will be learned/forwarded.')
sapAllowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1), ).setIndexNames((0, "BIANCA-BRICK-IPX-MIB", "sapAllowIfIndex"))
if mibBuilder.loadTexts: sapAllowEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowEntry.setDescription('')
sapAllowIfIndexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowIfIndexMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowIfIndexMode.setDescription(' dont_verify: the interface index is not verified verify: check interface index delete: delete this rule ')
sapAllowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowIfIndex.setDescription('This rule is applied to services originating and/or (see sapAllowDirection) destined for the interface with this index. ')
sapAllowDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dont-verify", 1), ("outgoing", 2), ("incoming", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowDirection.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowDirection.setDescription(' dont_verify: the interface index is not verified outgoing: this rule is applied to services being sent incoming: this rule is applied to incoming services both: this rule is applied to incoming and outgoing services ')
sapAllowTypeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowTypeMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowTypeMode.setDescription(" dont_verify: don't check service type verify: check service type ")
sapAllowType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowType.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowType.setDescription('The service type to be checked. Examples: 4: file server 7: print server ')
sapAllowNetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowNetMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowNetMode.setDescription(" dont_verify: don't check network number verify: check network number ")
sapAllowNet = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowNet.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowNet.setDescription(" the service's network number to be checked ")
sapAllowNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowNodeMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowNodeMode.setDescription(" dont_verify: don't check node number verify: check node number ")
sapAllowNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowNode.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowNode.setDescription(" the service's node number to be checked ")
sapAllowSockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowSockMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowSockMode.setDescription(" dont_verify: don't check socket number verify: check socket number ")
sapAllowSock = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowSock.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowSock.setDescription(" the service's socket number to be checked ")
sapAllowName = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapAllowName.setStatus('mandatory')
if mibBuilder.loadTexts: sapAllowName.setDescription(' Instead of entering Type/Net/Node/Socket directly, you could fill in the server name here. The Type/Net/Node/Socket fields will then be looked up in the ipxDestServTable. If a service of this name exists, the values of this rule will be set. Caution: the Brick IPX does not use this name field for filtering. It is just meant for easier usage. Only Type/Net/Node/Socket fields above will be checked (according to the dont_verify/verify fields) ')
sapDenyTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 9, 6), )
if mibBuilder.loadTexts: sapDenyTable.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyTable.setDescription('Each entry describes a rule for filtering services. Services matching any of those rules will be discarded.')
sapDenyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1), ).setIndexNames((0, "BIANCA-BRICK-IPX-MIB", "sapDenyIfIndex"))
if mibBuilder.loadTexts: sapDenyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyEntry.setDescription('')
sapDenyIfIndexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyIfIndexMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyIfIndexMode.setDescription(' dont_verify: the interface index is not verified verify: the interface index is not verified delete: delete this rule ')
sapDenyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyIfIndex.setDescription('This rule is applied to services originating and/or (see sapDenyDirection) destined for the interface with this index. ')
sapDenyDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dont-verify", 1), ("outgoing", 2), ("incoming", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyDirection.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyDirection.setDescription(' dont_verify: the direction is not verified outgoing: this rule is applied to services being sent incoming: this rule is applied to incoming services both: this rule is applied to incoming and outgoing services ')
sapDenyTypeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyTypeMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyTypeMode.setDescription(" dont_verify: don't check service type verify: check service type ")
sapDenyType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyType.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyType.setDescription('The service type to be checked. Examples: 4: file server 7: print server ')
sapDenyNetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyNetMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyNetMode.setDescription(" dont_verify: don't check network number verify: check network number ")
sapDenyNet = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyNet.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyNet.setDescription(" the service's network number to be checked ")
sapDenyNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyNodeMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyNodeMode.setDescription(" dont_verify: don't check node number verify: check node number ")
sapDenyNode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyNode.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyNode.setDescription(" the service's node number to be checked ")
sapDenySockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenySockMode.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenySockMode.setDescription(" dont_verify: don't check socket number verify: check socket number ")
sapDenySock = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenySock.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenySock.setDescription(" the service's socket number to be checked ")
sapDenyName = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sapDenyName.setStatus('mandatory')
if mibBuilder.loadTexts: sapDenyName.setDescription(' Instead of entering Type/Net/Node/Socket directly, you could fill in the server name here. The Type/Net/Node/Socket fields will then be looked up in the ipxDestServTable. If a service of this name exists, the values of this rule will be set. Caution: the Brick IPX does not use this name field for filtering. It is just meant for easier usage. Only Type/Net/Node/Socket fields above will be checked (according to the dont_verify/verify fields) ')
mibBuilder.exportSymbols("BIANCA-BRICK-IPX-MIB", ipxDenySrcIfIndex=ipxDenySrcIfIndex, ipxAdmin=ipxAdmin, sapDenyIfIndex=sapDenyIfIndex, ipxClientEntry=ipxClientEntry, internet=internet, ipxAdmSpxVerTimeout=ipxAdmSpxVerTimeout, sapAllowIfIndexMode=sapAllowIfIndexMode, sapAllowNode=sapAllowNode, sapAllowEntry=sapAllowEntry, sapAllowNodeMode=sapAllowNodeMode, sapAllowNet=sapAllowNet, sapAllowDirection=sapAllowDirection, sapAllowIfIndex=sapAllowIfIndex, ipxDenySrcNet=ipxDenySrcNet, org=org, sapDenyNet=sapDenyNet, ipxDenyDstSock=ipxDenyDstSock, ipxClientNode=ipxClientNode, ipxAllowSrcIfIndex=ipxAllowSrcIfIndex, ipxAllowSrcNetMode=ipxAllowSrcNetMode, dod=dod, ipxAdmIpxSpoofing=ipxAdmIpxSpoofing, ipxAdmRIPSAPOffset=ipxAdmRIPSAPOffset, sapAllowNetMode=sapAllowNetMode, sapDenyTypeMode=sapDenyTypeMode, ipxDenyPktTypeMode=ipxDenyPktTypeMode, sapDenyIfIndexMode=sapDenyIfIndexMode, sapAllowSock=sapAllowSock, sapDenyType=sapDenyType, ipxAllowDstSock=ipxAllowDstSock, ipxDenyDstNode=ipxDenyDstNode, private=private, ipxClientCircIndex=ipxClientCircIndex, ipxAllowSrcNet=ipxAllowSrcNet, ipxDenyDstSockMode=ipxDenyDstSockMode, ipxAdmNETBIOSRepl=ipxAdmNETBIOSRepl, ipxDenySrcNetMode=ipxDenySrcNetMode, sapDenyDirection=sapDenyDirection, sapDenyNode=sapDenyNode, sapDenyNodeMode=sapDenyNodeMode, ipxAllowTable=ipxAllowTable, sapAllowSockMode=sapAllowSockMode, sapAllowTypeMode=sapAllowTypeMode, sapDenySockMode=sapDenySockMode, biboipx=biboipx, ipxAllowDstNodeMode=ipxAllowDstNodeMode, ipxDenyDstIfStatus=ipxDenyDstIfStatus, ipxAdmSpxSpoofing=ipxAdmSpxSpoofing, bintec=bintec, ipxDenyEntry=ipxDenyEntry, ipxAllowEntry=ipxAllowEntry, ipxDenyDstNet=ipxDenyDstNet, ipxDenyDstNetMode=ipxDenyDstNetMode, ipxDenySrcIfIndexMode=ipxDenySrcIfIndexMode, sapDenyTable=sapDenyTable, ipxAllowSrcIfIndexMode=ipxAllowSrcIfIndexMode, ipxAllowDstNetMode=ipxAllowDstNetMode, ipxDenyDstNodeMode=ipxDenyDstNodeMode, ipxDenyPktType=ipxDenyPktType, ipxAllowSrcSockMode=ipxAllowSrcSockMode, ipxAllowPktType=ipxAllowPktType, ipxAllowSrcSock=ipxAllowSrcSock, ipxAllowPktTypeMode=ipxAllowPktTypeMode, ipxAllowSrcNodeMode=ipxAllowSrcNodeMode, ipxAllowSrcNode=ipxAllowSrcNode, sapDenyEntry=sapDenyEntry, sapDenyName=sapDenyName, sapAllowType=sapAllowType, ipxAllowDstSockMode=ipxAllowDstSockMode, ipxDenySrcSock=ipxDenySrcSock, ipxDenySrcSockMode=ipxDenySrcSockMode, ipxDenySrcNodeMode=ipxDenySrcNodeMode, bibo=bibo, sapAllowTable=sapAllowTable, ipxClientTable=ipxClientTable, ipxAdmSpxConns=ipxAdmSpxConns, ipxAllowDstNet=ipxAllowDstNet, enterprises=enterprises, sapAllowName=sapAllowName, sapDenySock=sapDenySock, ipxAllowDstNode=ipxAllowDstNode, ipxClientReconns=ipxClientReconns, ipxAllowDstIfStatus=ipxAllowDstIfStatus, ipxDenySrcNode=ipxDenySrcNode, sapDenyNetMode=sapDenyNetMode, ipxAdmLearnStatics=ipxAdmLearnStatics, ipxDenyTable=ipxDenyTable, ipxAdmSpxAbrTimeout=ipxAdmSpxAbrTimeout)
