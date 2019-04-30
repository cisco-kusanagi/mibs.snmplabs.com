#
# PySNMP MIB module ZXR10-MPLS-L3VPN-STATIS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-MPLS-L3VPN-STATIS
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, TimeTicks, Counter64, Integer32, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "TimeTicks", "Counter64", "Integer32", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxr10L3vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L3vpn")
zxr10MplsL3vpnStatisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1))
zxr10MplsL3vpnStatisMIB.setRevisions(('2005-09-26 00:00',))
if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setOrganization('ZTE Corporation')
zxr10L3vpnStatisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

zxr10L3vpnStatisTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1), )
if mibBuilder.loadTexts: zxr10L3vpnStatisTable.setStatus('current')
zxr10L3vpnStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1), ).setIndexNames((0, "ZXR10-MPLS-L3VPN-STATIS", "zxr10L3vpnStatisVpnID"))
if mibBuilder.loadTexts: zxr10L3vpnStatisEntry.setStatus('current')
zxr10L3vpnStatisVpnID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisVpnID.setStatus('current')
zxr10L3vpnStatisVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisVpnName.setStatus('current')
zxr10L3vpnStatisRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisRecvPkts.setStatus('current')
zxr10L3vpnStatisRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisRecvBytes.setStatus('current')
zxr10L3vpnStatisSndPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisSndPkts.setStatus('current')
zxr10L3vpnStatisSndBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisSndBytes.setStatus('current')
mibBuilder.exportSymbols("ZXR10-MPLS-L3VPN-STATIS", zxr10L3vpnStatisTable=zxr10L3vpnStatisTable, zxr10MplsL3vpnStatisMIB=zxr10MplsL3vpnStatisMIB, zxr10L3vpnStatisEntry=zxr10L3vpnStatisEntry, zxr10L3vpnStatisSndBytes=zxr10L3vpnStatisSndBytes, zxr10L3vpnStatisRecvBytes=zxr10L3vpnStatisRecvBytes, InterfaceIndex=InterfaceIndex, zxr10L3vpnStatisVpnName=zxr10L3vpnStatisVpnName, zxr10L3vpnStatisObjects=zxr10L3vpnStatisObjects, zxr10L3vpnStatisVpnID=zxr10L3vpnStatisVpnID, zxr10L3vpnStatisSndPkts=zxr10L3vpnStatisSndPkts, zxr10L3vpnStatisRecvPkts=zxr10L3vpnStatisRecvPkts, PYSNMP_MODULE_ID=zxr10MplsL3vpnStatisMIB, DisplayString=DisplayString)
