#
# PySNMP MIB module Unisphere-Data-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifEntry, ifStackLowerLayer, ifStackHigherLayer = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifStackLowerLayer", "ifStackHigherLayer")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, iso, MibIdentifier, ModuleIdentity, NotificationType, Bits, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "NotificationType", "Bits", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Gauge32", "Counter32", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
usdIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3))
usdIfMIB.setRevisions(('2001-03-28 15:12', '2000-11-22 23:41', '2000-09-29 18:35', '2000-07-27 15:45', '2000-05-05 15:08', '1999-12-21 15:18', '1999-09-03 14:16', '1998-11-13 20:19',))
if mibBuilder.loadTexts: usdIfMIB.setLastUpdated('200103281512Z')
if mibBuilder.loadTexts: usdIfMIB.setOrganization('Unisphere Networks, Inc.')
usdInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1))
usdIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1))
class UsdIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ds0", 2), ("ds1", 3), ("ds3", 4), ("frameRelay", 5), ("ethernet", 6), ("sonet", 7), ("sonetPath", 8), ("atm", 9), ("aal5", 10), ("atmSubInterface", 11), ("ft1", 12), ("hdlc", 13), ("ipLoopback", 14), ("ipVirtual", 15), ("frSubInterface", 16), ("pppoe", 17), ("pppoeSubInterface", 18), ("bridgedEthernet", 19), ("l2tpTunnelInterface", 20), ("l2tpSessionInterface", 21), ("mlPppLinkInterface", 22), ("slepInterface", 23), ("l2tpDestinationInterface", 24), ("mplsMajorInterface", 25), ("mplsMinorInterface", 26), ("mlPppNetworkInterface", 27), ("ethernetSubInterface", 28), ("multilinkFrameRelayInterface", 29), ("ipTunnelInterface", 30), ("serverPortInterface", 31), ("smdsInterface", 32), ("sonetVTInterface", 33), ("vlanMajorInterface", 34), ("vlanSubInterface", 35), ("cbfInterface", 36), ("gtpInterface", 37), ("smdsMajorInterface", 38), ("smdsSubInterface", 39), ("l2fTunnelInterface", 40), ("l2fSessionInterface", 41), ("l2fDestinationInterface", 42), ("ipsecInterface", 43), ("sgInterface", 44), ("lacGenInterface", 47))

usdIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1))
usdIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: usdIfTable.setStatus('current')
usdIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1), )
ifEntry.registerAugmentions(("Unisphere-Data-IF-MIB", "usdIfEntry"))
usdIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: usdIfEntry.setStatus('current')
usdIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1), UsdIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIfType.setStatus('current')
usdIfInvStackTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2), )
if mibBuilder.loadTexts: usdIfInvStackTable.setStatus('current')
usdIfInvStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: usdIfInvStackEntry.setStatus('current')
usdIfInvStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIfInvStackStatus.setStatus('current')
usdIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4))
usdIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1))
usdIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2))
usdIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)).setObjects(("Unisphere-Data-IF-MIB", "usdIfGroup"), ("Unisphere-Data-IF-MIB", "usdIfInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIfCompliance = usdIfCompliance.setStatus('current')
usdIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)).setObjects(("Unisphere-Data-IF-MIB", "usdIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIfGroup = usdIfGroup.setStatus('current')
usdIfInvStackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)).setObjects(("Unisphere-Data-IF-MIB", "usdIfInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIfInvStackGroup = usdIfInvStackGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IF-MIB", usdIfCompliance=usdIfCompliance, usdIfInvStackEntry=usdIfInvStackEntry, usdInterfaces=usdInterfaces, usdIfInvStackStatus=usdIfInvStackStatus, usdIfGroups=usdIfGroups, usdIfType=usdIfType, usdIfObjects=usdIfObjects, UsdIfType=UsdIfType, usdIfTable=usdIfTable, PYSNMP_MODULE_ID=usdIfMIB, usdIfEntry=usdIfEntry, usdIfGroup=usdIfGroup, usdIf=usdIf, usdIfInvStackTable=usdIfInvStackTable, usdIfInvStackGroup=usdIfInvStackGroup, usdIfCompliances=usdIfCompliances, usdIfMIB=usdIfMIB, usdIfConformance=usdIfConformance)
