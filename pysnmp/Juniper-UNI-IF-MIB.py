#
# PySNMP MIB module Juniper-UNI-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-UNI-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifStackLowerLayer, ifEntry, ifStackHigherLayer = mibBuilder.importSymbols("IF-MIB", "ifStackLowerLayer", "ifEntry", "ifStackHigherLayer")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Gauge32, MibIdentifier, Counter64, Counter32, Bits, NotificationType, Unsigned32, Integer32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibIdentifier", "Counter64", "Counter32", "Bits", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3))
juniIfMIB.setRevisions(('2005-10-11 20:40', '2003-07-16 21:40', '2003-02-06 15:57', '2002-01-22 16:52', '2001-03-28 15:12', '2000-11-22 23:41', '2000-09-29 18:35', '2000-07-27 15:45', '2000-05-05 15:08', '1999-12-21 15:18', '1999-09-03 14:16', '1998-11-13 20:19',))
if mibBuilder.loadTexts: juniIfMIB.setLastUpdated('200510112040Z')
if mibBuilder.loadTexts: juniIfMIB.setOrganization('Juniper Networks, Inc.')
class JuniIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 145, 256, 257))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18), ("bridgedEthernet", 19), ("l2tpTunnelInterface", 20), ("l2tpSessionInterface", 21), ("mlPppLinkInterface", 22), ("slepInterface", 23), ("l2tpDestinationInterface", 24), ("mplsMajorInterface", 25), ("mplsMinorInterface", 26), ("mlPppNetworkInterface", 27), ("ethernetSubInterface", 28), ("multilinkFrameRelayInterface", 29), ("ipTunnelInterface", 30), ("serverPortInterface", 31), ("smdsInterface", 32), ("sonetVTInterface", 33), ("vlanMajorInterface", 34), ("vlanSubInterface", 35), ("cbfInterface", 36), ("gtpInterface", 37), ("smdsMajorInterface", 38), ("smdsSubInterface", 39), ("l2fTunnelInterface", 40), ("l2fSessionInterface", 41), ("l2fDestinationInterface", 42), ("ipsecInterface", 43), ("sgInterface", 44), ("mplsL2ShimInterface", 45), ("lacGenInterface", 47), ("bridgeInterface", 48), ("ipsecTransportInterface", 49), ("ipv6Interface", 50), ("ipv6TunnelInterface", 51), ("ipv6Loopback", 52), ("osi", 53), ("lag", 54), ("ipTunnelMdt", 55), ("atmVirtualCircuit", 145), ("pppLink", 256), ("atmActiveSubInterface", 257))

juniInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1))
juniIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1))
juniIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1))
juniIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: juniIfTable.setStatus('current')
juniIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("Juniper-UNI-IF-MIB", "juniIfEntry"))
juniIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: juniIfEntry.setStatus('current')
juniIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1), JuniIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfType.setStatus('current')
juniIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: juniIfInvStackTable.setStatus('current')
juniIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: juniIfInvStackEntry.setStatus('current')
juniIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfInvStackStatus.setStatus('current')
juniIfCountTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3), )
if mibBuilder.loadTexts: juniIfCountTable.setStatus('current')
juniIfCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-UNI-IF-MIB", "juniIfCountIfType"))
if mibBuilder.loadTexts: juniIfCountEntry.setStatus('current')
juniIfCountIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 1), JuniIfType())
if mibBuilder.loadTexts: juniIfCountIfType.setStatus('current')
juniIfCountNumberOfInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIfCountNumberOfInterfaces.setStatus('current')
juniIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4))
juniIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1))
juniIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2))
juniIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)).setObjects(("Juniper-UNI-IF-MIB", "juniIfGroup"), ("Juniper-UNI-IF-MIB", "juniIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCompliance = juniIfCompliance.setStatus('current')
juniIfCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 2)).setObjects(("Juniper-UNI-IF-MIB", "juniIfGroup"), ("Juniper-UNI-IF-MIB", "juniIfInvStackGroup"), ("Juniper-UNI-IF-MIB", "juniIfCountGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCompliance1 = juniIfCompliance1.setStatus('current')
juniIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)).setObjects(("Juniper-UNI-IF-MIB", "juniIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfGroup = juniIfGroup.setStatus('current')
juniIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)).setObjects(("Juniper-UNI-IF-MIB", "juniIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfInvStackGroup = juniIfInvStackGroup.setStatus('current')
juniIfCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 3)).setObjects(("Juniper-UNI-IF-MIB", "juniIfCountNumberOfInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIfCountGroup = juniIfCountGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-UNI-IF-MIB", juniIfCountIfType=juniIfCountIfType, juniIfInvStackEntry=juniIfInvStackEntry, juniInterfaces=juniInterfaces, juniIfCountGroup=juniIfCountGroup, juniIfCompliances=juniIfCompliances, juniIfConformance=juniIfConformance, juniIfInvStackTable=juniIfInvStackTable, juniIfObjects=juniIfObjects, juniIfType=juniIfType, juniIfCountNumberOfInterfaces=juniIfCountNumberOfInterfaces, juniIfCountTable=juniIfCountTable, juniIfInvStackGroup=juniIfInvStackGroup, juniIfEntry=juniIfEntry, juniIfMIB=juniIfMIB, juniIfCompliance1=juniIfCompliance1, juniIfGroup=juniIfGroup, PYSNMP_MODULE_ID=juniIfMIB, juniIfCompliance=juniIfCompliance, juniIf=juniIf, JuniIfType=JuniIfType, juniIfTable=juniIfTable, juniIfGroups=juniIfGroups, juniIfInvStackStatus=juniIfInvStackStatus, juniIfCountEntry=juniIfCountEntry)
