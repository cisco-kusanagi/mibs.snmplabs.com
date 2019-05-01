#
# PySNMP MIB module ZXR10-MPLS-L3VPN-STATIS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-MPLS-L3VPN-STATIS
# Produced by pysmi-0.3.4 at Wed May  1 15:48:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, MibIdentifier, Counter32, Counter64, TimeTicks, Bits, Gauge32, ObjectIdentity, Unsigned32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibIdentifier", "Counter32", "Counter64", "TimeTicks", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxr10L3vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L3vpn")
zxr10MplsL3vpnStatisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1))
zxr10MplsL3vpnStatisMIB.setRevisions(('2005-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setContactInfo('ZTE Corporation Nanjing Institute of ZTE Corporation No.68 Zijinghua Rd. Yuhuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: zxr10MplsL3vpnStatisMIB.setDescription('ZXROS v4.6.03 Mpls L3vpn query and configuration MIB')
zxr10L3vpnStatisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

zxr10L3vpnStatisTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1), )
if mibBuilder.loadTexts: zxr10L3vpnStatisTable.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisTable.setDescription('Mpls L3vpn instance query table')
zxr10L3vpnStatisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1), ).setIndexNames((0, "ZXR10-MPLS-L3VPN-STATIS", "zxr10L3vpnStatisVpnID"))
if mibBuilder.loadTexts: zxr10L3vpnStatisEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisEntry.setDescription('Information of Mpls L3vpn instance configured on a PE')
zxr10L3vpnStatisVpnID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisVpnID.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisVpnID.setDescription('')
zxr10L3vpnStatisVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisVpnName.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisVpnName.setDescription('')
zxr10L3vpnStatisRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisRecvPkts.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisRecvPkts.setDescription('')
zxr10L3vpnStatisRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisRecvBytes.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisRecvBytes.setDescription('')
zxr10L3vpnStatisSndPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisSndPkts.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisSndPkts.setDescription('')
zxr10L3vpnStatisSndBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 105, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10L3vpnStatisSndBytes.setStatus('current')
if mibBuilder.loadTexts: zxr10L3vpnStatisSndBytes.setDescription('')
mibBuilder.exportSymbols("ZXR10-MPLS-L3VPN-STATIS", zxr10MplsL3vpnStatisMIB=zxr10MplsL3vpnStatisMIB, DisplayString=DisplayString, InterfaceIndex=InterfaceIndex, zxr10L3vpnStatisEntry=zxr10L3vpnStatisEntry, zxr10L3vpnStatisVpnID=zxr10L3vpnStatisVpnID, zxr10L3vpnStatisSndPkts=zxr10L3vpnStatisSndPkts, PYSNMP_MODULE_ID=zxr10MplsL3vpnStatisMIB, zxr10L3vpnStatisTable=zxr10L3vpnStatisTable, zxr10L3vpnStatisRecvBytes=zxr10L3vpnStatisRecvBytes, zxr10L3vpnStatisSndBytes=zxr10L3vpnStatisSndBytes, zxr10L3vpnStatisObjects=zxr10L3vpnStatisObjects, zxr10L3vpnStatisRecvPkts=zxr10L3vpnStatisRecvPkts, zxr10L3vpnStatisVpnName=zxr10L3vpnStatisVpnName)
