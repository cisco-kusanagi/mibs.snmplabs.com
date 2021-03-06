#
# PySNMP MIB module NETWORK-DIAGS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETWORK-DIAGS
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
nwDiagnostics, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "nwDiagnostics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, Integer32, NotificationType, Counter64, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Unsigned32, TimeTicks, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Integer32", "NotificationType", "Counter64", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Unsigned32", "TimeTicks", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nwRevision = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 1))
nwInternet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2))
nwIpPing = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1))
nwIpTraceRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2))
nwRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwRevisionLevel.setStatus('mandatory')
nwIpPingTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1), )
if mibBuilder.loadTexts: nwIpPingTable.setStatus('mandatory')
nwIpPingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1), ).setIndexNames((0, "NETWORK-DIAGS", "nwIpPingDestination"), (0, "NETWORK-DIAGS", "nwIpPingOwner"))
if mibBuilder.loadTexts: nwIpPingEntry.setStatus('mandatory')
nwIpPingDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingDestination.setStatus('mandatory')
nwIpPingOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingOwner.setStatus('mandatory')
nwIpPingType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2))).clone('other')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingType.setStatus('mandatory')
nwIpPingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("activate", 2), ("suspend", 3))).clone('activate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpPingAction.setStatus('mandatory')
nwIpPingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("other", 1), ("not-sent", 2), ("in-progress", 3), ("alive", 4), ("timeout", 5), ("bad-results", 6), ("failed", 7), ("net-unreach", 8), ("host-unreach", 9), ("proto-unreach", 10), ("port-unreach", 11), ("cant-frag", 12), ("sr-failed", 13), ("net-unknown", 14), ("host-unknown", 15), ("isolated", 16), ("no-net-comm", 17), ("no-host-comm", 18), ("no-net-tos", 19), ("no-host-tos", 20), ("source-quence", 21), ("ttl-exceeded", 22), ("frag-exceeded", 23), ("parameter", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpPingStatus.setStatus('mandatory')
nwIpTraceRouteTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1), )
if mibBuilder.loadTexts: nwIpTraceRouteTable.setStatus('mandatory')
nwIpTraceRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1), ).setIndexNames((0, "NETWORK-DIAGS", "nwIpTraceRouteDestination"), (0, "NETWORK-DIAGS", "nwIpTraceRouteOwner"))
if mibBuilder.loadTexts: nwIpTraceRouteEntry.setStatus('mandatory')
nwIpTraceRouteDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteDestination.setStatus('mandatory')
nwIpTraceRouteOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteOwner.setStatus('mandatory')
nwIpTraceRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2))).clone('other')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteType.setStatus('mandatory')
nwIpTraceRouteAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("activate", 2), ("suspend", 3))).clone('activate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwIpTraceRouteAction.setStatus('mandatory')
nwIpTraceRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("other", 1), ("not-sent", 2), ("in-progress", 3), ("alive", 4), ("timeout", 5), ("bad-results", 6), ("failed", 7), ("net-unreach", 8), ("host-unreach", 9), ("proto-unreach", 10), ("port-unreach", 11), ("cant-frag", 12), ("sr-failed", 13), ("net-unknown", 14), ("host-unknown", 15), ("isolated", 16), ("no-net-comm", 17), ("no-host-comm", 18), ("no-net-tos", 19), ("no-host-tos", 20), ("source-quence", 21), ("ttl-exceeded", 22), ("frag-exceeded", 23), ("parameter", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteStatus.setStatus('mandatory')
nwIpTraceRouteNextHops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteNextHops.setStatus('mandatory')
nwIpTraceRouteHopTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2), )
if mibBuilder.loadTexts: nwIpTraceRouteHopTable.setStatus('mandatory')
nwIpTraceRouteHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1), ).setIndexNames((0, "NETWORK-DIAGS", "nwIpTraceRouteHopDestination"), (0, "NETWORK-DIAGS", "nwIpTraceRouteHopOwner"), (0, "NETWORK-DIAGS", "nwIpTraceRouteHopNumber"))
if mibBuilder.loadTexts: nwIpTraceRouteHopEntry.setStatus('mandatory')
nwIpTraceRouteHopDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopDestination.setStatus('mandatory')
nwIpTraceRouteHopOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopOwner.setStatus('mandatory')
nwIpTraceRouteHopNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopNumber.setStatus('mandatory')
nwIpTraceRouteHopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwIpTraceRouteHopIp.setStatus('mandatory')
mibBuilder.exportSymbols("NETWORK-DIAGS", nwIpTraceRouteNextHops=nwIpTraceRouteNextHops, nwIpTraceRouteHopNumber=nwIpTraceRouteHopNumber, nwIpTraceRouteHopEntry=nwIpTraceRouteHopEntry, nwRevision=nwRevision, nwIpPingAction=nwIpPingAction, nwInternet=nwInternet, nwIpTraceRouteHopTable=nwIpTraceRouteHopTable, nwIpPingOwner=nwIpPingOwner, nwIpTraceRouteStatus=nwIpTraceRouteStatus, nwIpTraceRouteTable=nwIpTraceRouteTable, nwIpPing=nwIpPing, nwIpTraceRouteAction=nwIpTraceRouteAction, nwIpTraceRouteType=nwIpTraceRouteType, nwIpPingEntry=nwIpPingEntry, nwIpPingDestination=nwIpPingDestination, nwIpPingStatus=nwIpPingStatus, nwIpTraceRouteHopDestination=nwIpTraceRouteHopDestination, nwIpTraceRouteHopIp=nwIpTraceRouteHopIp, nwIpPingTable=nwIpPingTable, nwIpTraceRouteOwner=nwIpTraceRouteOwner, nwIpTraceRouteEntry=nwIpTraceRouteEntry, nwIpPingType=nwIpPingType, nwIpTraceRouteDestination=nwIpTraceRouteDestination, nwIpTraceRoute=nwIpTraceRoute, nwIpTraceRouteHopOwner=nwIpTraceRouteHopOwner, nwRevisionLevel=nwRevisionLevel)
