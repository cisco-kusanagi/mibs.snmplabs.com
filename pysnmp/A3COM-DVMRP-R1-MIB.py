#
# PySNMP MIB module A3COM-DVMRP-R1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-DVMRP-R1-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:18 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Gauge32, MibIdentifier, Unsigned32, iso, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Bits, enterprises, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "iso", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Bits", "enterprises", "ModuleIdentity", "IpAddress")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComDVMRP = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 28))
a3ComDvmrpSConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 28, 1))
a3ComDvmrpCConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 28, 2))
a3ComDvmrpData = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 28, 3))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3ComDvmrpCacheTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 86400)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpCacheTime.setStatus('mandatory')
a3ComDvmrpPrune = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpPrune.setStatus('mandatory')
a3ComDvmrpUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 5400)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpUpdateTime.setStatus('mandatory')
a3ComDvmrpMospfPolicy = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mospf", 1), ("noMospf", 2))).clone('noMospf')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpMospfPolicy.setStatus('mandatory')
a3ComDvmrpDestGroupPolicy = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("destGroup", 1), ("noDestGroup", 2))).clone('noDestGroup')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpDestGroupPolicy.setStatus('mandatory')
a3ComDvmrpPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1), )
if mibBuilder.loadTexts: a3ComDvmrpPortTable.setStatus('mandatory')
a3ComDvmrpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpPortIndex"))
if mibBuilder.loadTexts: a3ComDvmrpPortEntry.setStatus('mandatory')
a3ComDvmrpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpPortIndex.setStatus('mandatory')
a3ComDvmrpPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpPortControl.setStatus('mandatory')
a3ComDvmrpPortMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpPortMetric.setStatus('mandatory')
a3ComDvmrpPortRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpPortRateLimit.setStatus('mandatory')
a3ComDvmrpPortAggregateCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpPortAggregateCtrl.setStatus('mandatory')
a3ComDvmrpBoundaryAddrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2), )
if mibBuilder.loadTexts: a3ComDvmrpBoundaryAddrTable.setStatus('mandatory')
a3ComDvmrpBoundaryAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpBoundaryAddrPort"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpBoundaryAddrIpAddr"))
if mibBuilder.loadTexts: a3ComDvmrpBoundaryAddrEntry.setStatus('mandatory')
a3ComDvmrpBoundaryAddrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpBoundaryAddrPort.setStatus('mandatory')
a3ComDvmrpBoundaryAddrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpBoundaryAddrIpAddr.setStatus('mandatory')
a3ComDvmrpBoundaryAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpBoundaryAddrMask.setStatus('mandatory')
a3ComDvmrpBoundaryAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpBoundaryAddrStatus.setStatus('mandatory')
a3ComDvmrpMospfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3), )
if mibBuilder.loadTexts: a3ComDvmrpMospfTable.setStatus('mandatory')
a3ComDvmrpMospfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpMospfIpAddr"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpMospfIpMask"))
if mibBuilder.loadTexts: a3ComDvmrpMospfEntry.setStatus('mandatory')
a3ComDvmrpMospfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpMospfIpAddr.setStatus('mandatory')
a3ComDvmrpMospfIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpMospfIpMask.setStatus('mandatory')
a3ComDvmrpMospfMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpMospfMetric.setStatus('mandatory')
a3ComDvmrpMospfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("aggregate", 1), ("individual", 2), ("reject", 3))).clone('aggregate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpMospfAction.setStatus('mandatory')
a3ComDvmrpMospfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpMospfStatus.setStatus('mandatory')
a3ComDvmrpNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4), )
if mibBuilder.loadTexts: a3ComDvmrpNeighborTable.setStatus('mandatory')
a3ComDvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNeighborPort"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNeighborType"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNeighborAddr"))
if mibBuilder.loadTexts: a3ComDvmrpNeighborEntry.setStatus('mandatory')
a3ComDvmrpNeighborPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNeighborPort.setStatus('mandatory')
a3ComDvmrpNeighborType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("x25", 2), ("frame-relay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNeighborType.setStatus('mandatory')
a3ComDvmrpNeighborAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNeighborAddr.setStatus('mandatory')
a3ComDvmrpNeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpNeighborStatus.setStatus('mandatory')
a3ComDvmrpTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5), )
if mibBuilder.loadTexts: a3ComDvmrpTunnelTable.setStatus('mandatory')
a3ComDvmrpTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpTunnelId"))
if mibBuilder.loadTexts: a3ComDvmrpTunnelEntry.setStatus('mandatory')
a3ComDvmrpTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpTunnelId.setStatus('mandatory')
a3ComDvmrpTunnelLocalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpTunnelLocalIp.setStatus('mandatory')
a3ComDvmrpTunnelRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpTunnelRemoteIp.setStatus('mandatory')
a3ComDvmrpTunnelTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpTunnelTtl.setStatus('mandatory')
a3ComDvmrpTunnelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpTunnelStatus.setStatus('mandatory')
a3ComDvmrpAggreExceptTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6), )
if mibBuilder.loadTexts: a3ComDvmrpAggreExceptTable.setStatus('mandatory')
a3ComDvmrpAggreExceptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreExceptIpAddr"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreExceptIpMask"))
if mibBuilder.loadTexts: a3ComDvmrpAggreExceptEntry.setStatus('mandatory')
a3ComDvmrpAggreExceptIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreExceptIpAddr.setStatus('mandatory')
a3ComDvmrpAggreExceptIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreExceptIpMask.setStatus('mandatory')
a3ComDvmrpAggreExceptStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreExceptStatus.setStatus('mandatory')
a3ComDvmrpAggreRangeTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7), )
if mibBuilder.loadTexts: a3ComDvmrpAggreRangeTable.setStatus('mandatory')
a3ComDvmrpAggreRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreRangeIpAddr"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreRangeIpMask"))
if mibBuilder.loadTexts: a3ComDvmrpAggreRangeEntry.setStatus('mandatory')
a3ComDvmrpAggreRangeIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreRangeIpAddr.setStatus('mandatory')
a3ComDvmrpAggreRangeIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreRangeIpMask.setStatus('mandatory')
a3ComDvmrpAggreRangeMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreRangeMetric.setStatus('mandatory')
a3ComDvmrpAggreRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpAggreRangeStatus.setStatus('mandatory')
a3ComDvmrpDestGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8), )
if mibBuilder.loadTexts: a3ComDvmrpDestGroupTable.setStatus('mandatory')
a3ComDvmrpDestGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpDestGroupIpAddr"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpDestGroupIpMask"))
if mibBuilder.loadTexts: a3ComDvmrpDestGroupEntry.setStatus('mandatory')
a3ComDvmrpDestGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpDestGroupIpAddr.setStatus('mandatory')
a3ComDvmrpDestGroupIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpDestGroupIpMask.setStatus('mandatory')
a3ComDvmrpDestGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accept", 1), ("reject", 2))).clone('accept')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpDestGroupAction.setStatus('mandatory')
a3ComDvmrpDestGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDvmrpDestGroupStatus.setStatus('mandatory')
a3ComDvmrpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1), )
if mibBuilder.loadTexts: a3ComDvmrpRouteTable.setStatus('mandatory')
a3ComDvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpRouteSource"))
if mibBuilder.loadTexts: a3ComDvmrpRouteEntry.setStatus('mandatory')
a3ComDvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteSource.setStatus('mandatory')
a3ComDvmrpRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteMask.setStatus('mandatory')
a3ComDvmrpRoutePreHop = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRoutePreHop.setStatus('mandatory')
a3ComDvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteMetric.setStatus('mandatory')
a3ComDvmrpRoutePort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRoutePort.setStatus('mandatory')
a3ComDvmrpRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("direct", 2), ("remote", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteType.setStatus('mandatory')
a3ComDvmrpRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3), ("hold-down", 4), ("garbage-collection", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteStatus.setStatus('mandatory')
a3ComDvmrpRouteProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dvmrp", 3), ("mospf", 4), ("cbt", 5), ("pim", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteProtocol.setStatus('mandatory')
a3ComDvmrpRouteTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteTtl.setStatus('mandatory')
a3ComDvmrpRouteChild = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteChild.setStatus('mandatory')
a3ComDvmrpRouteChildTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteChildTunnel.setStatus('mandatory')
a3ComDvmrpRouteLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteLeaf.setStatus('mandatory')
a3ComDvmrpRouteLeafTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpRouteLeafTunnel.setStatus('mandatory')
a3ComDvmrpForwardTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2), )
if mibBuilder.loadTexts: a3ComDvmrpForwardTable.setStatus('mandatory')
a3ComDvmrpForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpForwardSource"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpForwardGroup"))
if mibBuilder.loadTexts: a3ComDvmrpForwardEntry.setStatus('mandatory')
a3ComDvmrpForwardSource = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardSource.setStatus('mandatory')
a3ComDvmrpForwardGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardGroup.setStatus('mandatory')
a3ComDvmrpForwardTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardTtl.setStatus('mandatory')
a3ComDvmrpForwardInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardInPort.setStatus('mandatory')
a3ComDvmrpForwardOutPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardOutPorts.setStatus('mandatory')
a3ComDvmrpForwardOutPortsTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardOutPortsTunnel.setStatus('mandatory')
a3ComDvmrpForwardScoped = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardScoped.setStatus('mandatory')
a3ComDvmrpForwardPruneSent = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpForwardPruneSent.setStatus('mandatory')
a3ComDvmrpNbrRouterTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3), )
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterTable.setStatus('mandatory')
a3ComDvmrpNbrRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1), ).setIndexNames((0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNbrRouterPort"), (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNbrRouterIpAddr"))
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterEntry.setStatus('mandatory')
a3ComDvmrpNbrRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterPort.setStatus('mandatory')
a3ComDvmrpNbrRouterIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterIpAddr.setStatus('mandatory')
a3ComDvmrpNbrRouterGenId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterGenId.setStatus('mandatory')
a3ComDvmrpNbrRouterVerProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterVerProtocol.setStatus('mandatory')
a3ComDvmrpNbrRouterVerMrouted = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterVerMrouted.setStatus('mandatory')
a3ComDvmrpNbrRouterTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterTtl.setStatus('mandatory')
a3ComDvmrpNbrRouterLeafStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterLeafStatus.setStatus('mandatory')
a3ComDvmrpNbrRouterPruneStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterPruneStatus.setStatus('mandatory')
a3ComDvmrpNbrRouterGenIdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterGenIdStatus.setStatus('mandatory')
a3ComDvmrpNbrRouterMtraceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDvmrpNbrRouterMtraceStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-DVMRP-R1-MIB", a3ComDvmrpForwardEntry=a3ComDvmrpForwardEntry, a3ComDvmrpAggreExceptTable=a3ComDvmrpAggreExceptTable, a3ComDvmrpAggreExceptIpAddr=a3ComDvmrpAggreExceptIpAddr, a3ComDvmrpForwardGroup=a3ComDvmrpForwardGroup, a3ComDvmrpNbrRouterPruneStatus=a3ComDvmrpNbrRouterPruneStatus, a3ComDvmrpDestGroupIpAddr=a3ComDvmrpDestGroupIpAddr, a3ComDvmrpRouteMask=a3ComDvmrpRouteMask, a3ComDvmrpRouteChildTunnel=a3ComDvmrpRouteChildTunnel, a3ComDvmrpNeighborType=a3ComDvmrpNeighborType, a3Com=a3Com, a3ComDvmrpDestGroupEntry=a3ComDvmrpDestGroupEntry, a3ComDvmrpNbrRouterEntry=a3ComDvmrpNbrRouterEntry, a3ComDvmrpMospfMetric=a3ComDvmrpMospfMetric, a3ComDvmrpAggreRangeIpMask=a3ComDvmrpAggreRangeIpMask, a3ComDvmrpPortRateLimit=a3ComDvmrpPortRateLimit, a3ComDvmrpMospfIpMask=a3ComDvmrpMospfIpMask, a3ComDvmrpForwardPruneSent=a3ComDvmrpForwardPruneSent, a3ComDvmrpData=a3ComDvmrpData, a3ComDvmrpMospfPolicy=a3ComDvmrpMospfPolicy, a3ComDvmrpRouteLeaf=a3ComDvmrpRouteLeaf, a3ComDvmrpMospfIpAddr=a3ComDvmrpMospfIpAddr, a3ComDvmrpForwardScoped=a3ComDvmrpForwardScoped, a3ComDvmrpNbrRouterLeafStatus=a3ComDvmrpNbrRouterLeafStatus, a3ComDvmrpNbrRouterVerProtocol=a3ComDvmrpNbrRouterVerProtocol, a3ComDvmrpForwardOutPortsTunnel=a3ComDvmrpForwardOutPortsTunnel, a3ComDvmrpRoutePort=a3ComDvmrpRoutePort, a3ComDvmrpNeighborAddr=a3ComDvmrpNeighborAddr, a3ComDvmrpForwardTable=a3ComDvmrpForwardTable, a3ComDvmrpRouteType=a3ComDvmrpRouteType, a3ComDvmrpTunnelTable=a3ComDvmrpTunnelTable, a3ComDvmrpRouteMetric=a3ComDvmrpRouteMetric, a3ComDvmrpNbrRouterPort=a3ComDvmrpNbrRouterPort, a3ComDvmrpPrune=a3ComDvmrpPrune, a3ComDvmrpBoundaryAddrTable=a3ComDvmrpBoundaryAddrTable, a3ComDvmrpMospfTable=a3ComDvmrpMospfTable, a3ComDvmrpBoundaryAddrIpAddr=a3ComDvmrpBoundaryAddrIpAddr, a3ComDvmrpBoundaryAddrMask=a3ComDvmrpBoundaryAddrMask, a3ComDvmrpAggreRangeMetric=a3ComDvmrpAggreRangeMetric, a3ComDvmrpDestGroupPolicy=a3ComDvmrpDestGroupPolicy, a3ComDvmrpTunnelId=a3ComDvmrpTunnelId, a3ComDvmrpDestGroupIpMask=a3ComDvmrpDestGroupIpMask, a3ComDvmrpCacheTime=a3ComDvmrpCacheTime, a3ComDvmrpNeighborPort=a3ComDvmrpNeighborPort, a3ComDvmrpDestGroupStatus=a3ComDvmrpDestGroupStatus, a3ComDvmrpSConfig=a3ComDvmrpSConfig, a3ComDvmrpNbrRouterGenIdStatus=a3ComDvmrpNbrRouterGenIdStatus, a3ComDvmrpRouteProtocol=a3ComDvmrpRouteProtocol, a3ComDvmrpPortMetric=a3ComDvmrpPortMetric, a3ComDvmrpPortTable=a3ComDvmrpPortTable, a3ComDvmrpDestGroupTable=a3ComDvmrpDestGroupTable, a3ComDvmrpRouteChild=a3ComDvmrpRouteChild, a3ComDvmrpMospfEntry=a3ComDvmrpMospfEntry, a3ComDvmrpDestGroupAction=a3ComDvmrpDestGroupAction, brouterMIB=brouterMIB, a3ComDvmrpPortIndex=a3ComDvmrpPortIndex, a3ComDvmrpNeighborEntry=a3ComDvmrpNeighborEntry, a3ComDvmrpMospfAction=a3ComDvmrpMospfAction, RowStatus=RowStatus, a3ComDvmrpRouteSource=a3ComDvmrpRouteSource, a3ComDvmrpRoutePreHop=a3ComDvmrpRoutePreHop, a3ComDvmrpNeighborTable=a3ComDvmrpNeighborTable, a3ComDvmrpTunnelLocalIp=a3ComDvmrpTunnelLocalIp, a3ComDvmrpAggreRangeEntry=a3ComDvmrpAggreRangeEntry, a3ComDvmrpTunnelRemoteIp=a3ComDvmrpTunnelRemoteIp, a3ComDvmrpForwardTtl=a3ComDvmrpForwardTtl, a3ComDvmrpForwardSource=a3ComDvmrpForwardSource, a3ComDvmrpRouteLeafTunnel=a3ComDvmrpRouteLeafTunnel, a3ComDvmrpBoundaryAddrEntry=a3ComDvmrpBoundaryAddrEntry, a3ComDvmrpRouteTable=a3ComDvmrpRouteTable, a3ComDvmrpTunnelEntry=a3ComDvmrpTunnelEntry, a3ComDvmrpNbrRouterTable=a3ComDvmrpNbrRouterTable, a3ComDvmrpAggreExceptEntry=a3ComDvmrpAggreExceptEntry, a3ComDvmrpAggreRangeStatus=a3ComDvmrpAggreRangeStatus, a3ComDvmrpCConfig=a3ComDvmrpCConfig, a3ComDvmrpNbrRouterMtraceStatus=a3ComDvmrpNbrRouterMtraceStatus, a3ComDvmrpBoundaryAddrStatus=a3ComDvmrpBoundaryAddrStatus, a3ComDvmrpForwardInPort=a3ComDvmrpForwardInPort, a3ComDvmrpRouteTtl=a3ComDvmrpRouteTtl, a3ComDvmrpForwardOutPorts=a3ComDvmrpForwardOutPorts, a3ComDvmrpUpdateTime=a3ComDvmrpUpdateTime, a3ComDvmrpAggreExceptIpMask=a3ComDvmrpAggreExceptIpMask, a3ComDvmrpPortAggregateCtrl=a3ComDvmrpPortAggregateCtrl, a3ComDvmrpTunnelTtl=a3ComDvmrpTunnelTtl, a3ComDvmrpAggreExceptStatus=a3ComDvmrpAggreExceptStatus, a3ComDvmrpRouteStatus=a3ComDvmrpRouteStatus, a3ComDvmrpNbrRouterVerMrouted=a3ComDvmrpNbrRouterVerMrouted, a3ComDvmrpNbrRouterIpAddr=a3ComDvmrpNbrRouterIpAddr, a3ComDvmrpMospfStatus=a3ComDvmrpMospfStatus, a3ComDvmrpTunnelStatus=a3ComDvmrpTunnelStatus, a3ComDvmrpNbrRouterTtl=a3ComDvmrpNbrRouterTtl, a3ComDVMRP=a3ComDVMRP, a3ComDvmrpPortControl=a3ComDvmrpPortControl, a3ComDvmrpBoundaryAddrPort=a3ComDvmrpBoundaryAddrPort, a3ComDvmrpNbrRouterGenId=a3ComDvmrpNbrRouterGenId, a3ComDvmrpRouteEntry=a3ComDvmrpRouteEntry, a3ComDvmrpNeighborStatus=a3ComDvmrpNeighborStatus, a3ComDvmrpAggreRangeTable=a3ComDvmrpAggreRangeTable, a3ComDvmrpAggreRangeIpAddr=a3ComDvmrpAggreRangeIpAddr, a3ComDvmrpPortEntry=a3ComDvmrpPortEntry)
