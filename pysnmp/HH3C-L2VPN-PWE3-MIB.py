#
# PySNMP MIB module HH3C-L2VPN-PWE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-L2VPN-PWE3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, NotificationType, Bits, TimeTicks, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Counter64, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "NotificationType", "Bits", "TimeTicks", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Counter64", "Unsigned32", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
hh3cL2VpnPwe3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 78))
if mibBuilder.loadTexts: hh3cL2VpnPwe3.setLastUpdated('200703310000Z')
if mibBuilder.loadTexts: hh3cL2VpnPwe3.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cL2VpnVcEncapsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 255))
    namedValues = NamedValues(("frameRelayDlciMartini", 1), ("atmAal5SduVccTransport", 2), ("atmTransparentCellTransport", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmN2OneVccCellTransport", 9), ("atmN2OneVpcCellTransport", 10), ("ipLayer2Transport", 11), ("atmOne2OneVccCellMode", 12), ("atmOne2OneVpcCellMode", 13), ("atmAal5PduVccTransport", 14), ("frameRelayPortMode", 15), ("cep", 16), ("saE1oP", 17), ("saT1oP", 18), ("saE3oP", 19), ("saT3oP", 20), ("cESoPsnBasicMode", 21), ("tDMoIPbasicMode", 22), ("l2VpnCESoPSNTDMwithCAS", 23), ("l2VpnTDMoIPTDMwithCAS", 24), ("frameRelayDlci", 25), ("ipInterworking", 64), ("unknown", 255))

hh3cL2VpnPwe3ScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 78, 1))
hh3cPwVcTrapOpen = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 78, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPwVcTrapOpen.setStatus('current')
hh3cL2VpnPwe3Table = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2))
hh3cPwVcTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1), )
if mibBuilder.loadTexts: hh3cPwVcTable.setStatus('current')
hh3cPwVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1), ).setIndexNames((0, "HH3C-L2VPN-PWE3-MIB", "hh3cPwVcIndex"))
if mibBuilder.loadTexts: hh3cPwVcEntry.setStatus('current')
hh3cPwVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cPwVcIndex.setStatus('current')
hh3cPwVcID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcID.setStatus('current')
hh3cPwVcType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 3), Hh3cL2VpnVcEncapsType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcType.setStatus('current')
hh3cPwVcPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcPeerAddr.setStatus('current')
hh3cPwVcMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcMtu.setStatus('current')
hh3cPwVcCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("multiPort", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcCfgType.setStatus('current')
hh3cPwVcInboundLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPwVcInboundLabel.setStatus('current')
hh3cPwVcOutboundLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPwVcOutboundLabel.setStatus('current')
hh3cPwVcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcIfIndex.setStatus('current')
hh3cPwVcAcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPwVcAcStatus.setStatus('current')
hh3cPwVcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPwVcStatus.setStatus('current')
hh3cPwVcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 78, 2, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPwVcRowStatus.setStatus('current')
hh3cL2VpnPwe3Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 78, 3))
hh3cPwVcSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 1)).setObjects(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
if mibBuilder.loadTexts: hh3cPwVcSwitchWtoP.setStatus('current')
hh3cPwVcSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 2)).setObjects(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
if mibBuilder.loadTexts: hh3cPwVcSwitchPtoW.setStatus('current')
hh3cPwVcDown = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 3)).setObjects(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
if mibBuilder.loadTexts: hh3cPwVcDown.setStatus('current')
hh3cPwVcUp = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 4)).setObjects(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
if mibBuilder.loadTexts: hh3cPwVcUp.setStatus('current')
hh3cPwVcDeleted = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 78, 3, 5)).setObjects(("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcID"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcType"), ("HH3C-L2VPN-PWE3-MIB", "hh3cPwVcPeerAddr"))
if mibBuilder.loadTexts: hh3cPwVcDeleted.setStatus('current')
mibBuilder.exportSymbols("HH3C-L2VPN-PWE3-MIB", hh3cPwVcType=hh3cPwVcType, hh3cPwVcSwitchWtoP=hh3cPwVcSwitchWtoP, hh3cL2VpnPwe3Notifications=hh3cL2VpnPwe3Notifications, hh3cL2VpnPwe3=hh3cL2VpnPwe3, hh3cPwVcSwitchPtoW=hh3cPwVcSwitchPtoW, hh3cL2VpnPwe3ScalarGroup=hh3cL2VpnPwe3ScalarGroup, hh3cPwVcEntry=hh3cPwVcEntry, hh3cPwVcIndex=hh3cPwVcIndex, hh3cPwVcTable=hh3cPwVcTable, hh3cPwVcOutboundLabel=hh3cPwVcOutboundLabel, hh3cPwVcTrapOpen=hh3cPwVcTrapOpen, hh3cPwVcMtu=hh3cPwVcMtu, Hh3cL2VpnVcEncapsType=Hh3cL2VpnVcEncapsType, hh3cPwVcUp=hh3cPwVcUp, hh3cPwVcStatus=hh3cPwVcStatus, hh3cPwVcPeerAddr=hh3cPwVcPeerAddr, hh3cPwVcAcStatus=hh3cPwVcAcStatus, hh3cPwVcCfgType=hh3cPwVcCfgType, hh3cPwVcIfIndex=hh3cPwVcIfIndex, hh3cL2VpnPwe3Table=hh3cL2VpnPwe3Table, hh3cPwVcDeleted=hh3cPwVcDeleted, hh3cPwVcRowStatus=hh3cPwVcRowStatus, PYSNMP_MODULE_ID=hh3cL2VpnPwe3, hh3cPwVcDown=hh3cPwVcDown, hh3cPwVcID=hh3cPwVcID, hh3cPwVcInboundLabel=hh3cPwVcInboundLabel)
