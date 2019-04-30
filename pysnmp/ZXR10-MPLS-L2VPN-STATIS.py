#
# PySNMP MIB module ZXR10-MPLS-L2VPN-STATIS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-MPLS-L2VPN-STATIS
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Counter32, ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, iso, TimeTicks, NotificationType, IpAddress, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Counter32", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "iso", "TimeTicks", "NotificationType", "IpAddress", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxr10L2vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L2vpn")
zxr10MplsL2vpnStatisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6))
zxr10MplsL2vpnStatisMIB.setRevisions(('2005-07-26 00:00',))
if mibBuilder.loadTexts: zxr10MplsL2vpnStatisMIB.setLastUpdated('200507260000Z')
if mibBuilder.loadTexts: zxr10MplsL2vpnStatisMIB.setOrganization('ZTE Corporation')
zxr10L2vpnStatisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

zxr10L2vpnStatisTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1), )
if mibBuilder.loadTexts: zxr10L2vpnStatisTable.setStatus('current')
zxr10L2vpnStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1), ).setIndexNames((0, "ZXR10-MPLS-L2VPN-STATIS", "zxr10L2vpnStatisVCID"))
if mibBuilder.loadTexts: zxr10L2vpnStatisEntry.setStatus('current')
zxr10L2vpnStatisVCID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVCID.setStatus('current')
zxr10L2vpnStatisVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVpnName.setStatus('current')
zxr10L2vpnStatisRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisRecvPkts.setStatus('current')
zxr10L2vpnStatisRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisRecvBytes.setStatus('current')
zxr10L2vpnStatisSndPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisSndPkts.setStatus('current')
zxr10L2vpnStatisSndBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisSndBytes.setStatus('current')
zxr10L2vpnStatisVcTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2), )
if mibBuilder.loadTexts: zxr10L2vpnStatisVcTable.setStatus('current')
zxr10L2vpnStatisVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1), ).setIndexNames((0, "ZXR10-MPLS-L2VPN-STATIS", "zxr10L2vpnStatisVcID"), (0, "ZXR10-MPLS-L2VPN-STATIS", "zxr10L2vpnStatisVcPeerAddr"))
if mibBuilder.loadTexts: zxr10L2vpnStatisVcEntry.setStatus('current')
zxr10L2vpnStatisVcID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVcID.setStatus('current')
zxr10L2vpnStatisVcPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVcPeerAddr.setStatus('current')
zxr10L2vpnStatisVcRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVcRecvPkts.setStatus('current')
zxr10L2vpnStatisVcRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVcRecvBytes.setStatus('current')
zxr10L2vpnStatisVcSndPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVcSndPkts.setStatus('current')
zxr10L2vpnStatisVcSndBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 6, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L2vpnStatisVcSndBytes.setStatus('current')
mibBuilder.exportSymbols("ZXR10-MPLS-L2VPN-STATIS", zxr10MplsL2vpnStatisMIB=zxr10MplsL2vpnStatisMIB, zxr10L2vpnStatisVcTable=zxr10L2vpnStatisVcTable, zxr10L2vpnStatisVcPeerAddr=zxr10L2vpnStatisVcPeerAddr, zxr10L2vpnStatisVcID=zxr10L2vpnStatisVcID, zxr10L2vpnStatisVcSndPkts=zxr10L2vpnStatisVcSndPkts, zxr10L2vpnStatisRecvPkts=zxr10L2vpnStatisRecvPkts, zxr10L2vpnStatisTable=zxr10L2vpnStatisTable, zxr10L2vpnStatisRecvBytes=zxr10L2vpnStatisRecvBytes, zxr10L2vpnStatisVcSndBytes=zxr10L2vpnStatisVcSndBytes, zxr10L2vpnStatisVcRecvBytes=zxr10L2vpnStatisVcRecvBytes, zxr10L2vpnStatisObjects=zxr10L2vpnStatisObjects, zxr10L2vpnStatisSndBytes=zxr10L2vpnStatisSndBytes, zxr10L2vpnStatisVCID=zxr10L2vpnStatisVCID, zxr10L2vpnStatisVpnName=zxr10L2vpnStatisVpnName, zxr10L2vpnStatisVcEntry=zxr10L2vpnStatisVcEntry, zxr10L2vpnStatisSndPkts=zxr10L2vpnStatisSndPkts, PYSNMP_MODULE_ID=zxr10MplsL2vpnStatisMIB, zxr10L2vpnStatisVcRecvPkts=zxr10L2vpnStatisVcRecvPkts, InterfaceIndex=InterfaceIndex, zxr10L2vpnStatisEntry=zxr10L2vpnStatisEntry, DisplayString=DisplayString)
