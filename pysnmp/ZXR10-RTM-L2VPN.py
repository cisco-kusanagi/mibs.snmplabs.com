#
# PySNMP MIB module ZXR10-RTM-L2VPN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-RTM-L2VPN
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Gauge32, NotificationType, iso, TimeTicks, Unsigned32, Counter32, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "NotificationType", "iso", "TimeTicks", "Unsigned32", "Counter32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
zxr10L2vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L2vpn")
rtmL2vpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3))
rtmL2vpnMIB.setRevisions(('2005-07-26 00:00',))
if mibBuilder.loadTexts: rtmL2vpnMIB.setLastUpdated('200507260000Z')
if mibBuilder.loadTexts: rtmL2vpnMIB.setOrganization('ZTE Corporation')
rtmL2vpnVcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0))
rtmL2vpnVplsIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class RtmL2vpnEncapType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("encap-UNKNOWN", 0), ("encap-FR-DLCI", 1), ("encap-ATM-AAL5", 2), ("encap-ATM-TRANSCELL", 3), ("encap-ETH-VLAN", 4), ("encap-ETH", 5), ("encap-HDLC", 6), ("encap-PPP", 7), ("encap-CEM", 8), ("encap-ATM-VCC", 9), ("encap-ATM-VPC", 10))

class RtmL2vpnType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("l2vpn-UNKNOWN", 0), ("l2vpn-VPWS", 1), ("l2vpn-VPLS", 2), ("l2vpn-IPLS", 3))

class RtmL2vpnVCStatus(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("vc-Down", 0), ("vc-Up", 1))

class RtmL2vpnCsType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("server", 0), ("client", 1))

rtmL2vpnIfTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1), )
if mibBuilder.loadTexts: rtmL2vpnIfTable.setStatus('current')
rtmL2vpnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1), ).setIndexNames((0, "ZXR10-RTM-L2VPN", "rtmL2vpnVplsIfVcid"), (0, "ZXR10-RTM-L2VPN", "rtmL2vpnVplsIfIndex"))
if mibBuilder.loadTexts: rtmL2vpnIfEntry.setStatus('current')
rtmL2vpnVplsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfIndex.setStatus('current')
rtmL2vpnVplsIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfName.setStatus('current')
rtmL2vpnVplsIfEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfEncapType.setStatus('current')
rtmL2vpnVplsIfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 21))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfVpnName.setStatus('current')
rtmL2vpnVplsIfVcid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfVcid.setStatus('current')
rtmL2vpnVplsIfVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfVpnType.setStatus('current')
rtmL2vpnIfQinQEx = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfQinQEx.setStatus('current')
rtmL2vpnIfQinQIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfQinQIn.setStatus('current')
rtmL2vpnIfVlanRangeTop1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop1.setStatus('current')
rtmL2vpnIfVlanRangeTop2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop2.setStatus('current')
rtmL2vpnIfVlanRangeTop3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop3.setStatus('current')
rtmL2vpnIfVlanRangeBot1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot1.setStatus('current')
rtmL2vpnIfVlanRangeBot2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot2.setStatus('current')
rtmL2vpnIfVlanRangeBot3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot3.setStatus('current')
rtmL2vpnIfCSAttr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 15), RtmL2vpnCsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfCSAttr.setStatus('current')
rtmL2vpnVcTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1), )
if mibBuilder.loadTexts: rtmL2vpnVcTable.setStatus('current')
rtmL2vpnVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1), ).setIndexNames((0, "ZXR10-RTM-L2VPN", "rtmL2vpnVCInInternalLabel"))
if mibBuilder.loadTexts: rtmL2vpnVcEntry.setStatus('current')
rtmL2vpnVCVcId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCVcId.setStatus('current')
rtmL2vpnVCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 2), RtmL2vpnVCStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCStatus.setStatus('current')
rtmL2vpnVCPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCPeerIP.setStatus('current')
rtmL2vpnVCInInternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCInInternalLabel.setStatus('current')
rtmL2vpnVCOutInternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCOutInternalLabel.setStatus('current')
rtmL2vpnVCInExternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCInExternalLabel.setStatus('current')
rtmL2vpnVCOutExternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCOutExternalLabel.setStatus('current')
mibBuilder.exportSymbols("ZXR10-RTM-L2VPN", rtmL2vpnVCOutExternalLabel=rtmL2vpnVCOutExternalLabel, rtmL2vpnVCInExternalLabel=rtmL2vpnVCInExternalLabel, RtmL2vpnCsType=RtmL2vpnCsType, rtmL2vpnVplsIfObjects=rtmL2vpnVplsIfObjects, rtmL2vpnIfVlanRangeBot1=rtmL2vpnIfVlanRangeBot1, rtmL2vpnVcEntry=rtmL2vpnVcEntry, rtmL2vpnIfTable=rtmL2vpnIfTable, rtmL2vpnVplsIfVpnType=rtmL2vpnVplsIfVpnType, rtmL2vpnIfQinQIn=rtmL2vpnIfQinQIn, RtmL2vpnVCStatus=RtmL2vpnVCStatus, rtmL2vpnIfVlanRangeTop1=rtmL2vpnIfVlanRangeTop1, rtmL2vpnVCStatus=rtmL2vpnVCStatus, RtmL2vpnType=RtmL2vpnType, rtmL2vpnIfCSAttr=rtmL2vpnIfCSAttr, rtmL2vpnVplsIfEncapType=rtmL2vpnVplsIfEncapType, RtmL2vpnEncapType=RtmL2vpnEncapType, rtmL2vpnVCInInternalLabel=rtmL2vpnVCInInternalLabel, DisplayString=DisplayString, rtmL2vpnIfVlanRangeBot2=rtmL2vpnIfVlanRangeBot2, rtmL2vpnIfVlanRangeBot3=rtmL2vpnIfVlanRangeBot3, PYSNMP_MODULE_ID=rtmL2vpnMIB, rtmL2vpnVCPeerIP=rtmL2vpnVCPeerIP, rtmL2vpnVplsIfName=rtmL2vpnVplsIfName, rtmL2vpnIfEntry=rtmL2vpnIfEntry, rtmL2vpnVplsIfIndex=rtmL2vpnVplsIfIndex, rtmL2vpnIfQinQEx=rtmL2vpnIfQinQEx, rtmL2vpnVcObjects=rtmL2vpnVcObjects, rtmL2vpnVCOutInternalLabel=rtmL2vpnVCOutInternalLabel, rtmL2vpnVCVcId=rtmL2vpnVCVcId, rtmL2vpnVcTable=rtmL2vpnVcTable, InterfaceIndex=InterfaceIndex, rtmL2vpnMIB=rtmL2vpnMIB, rtmL2vpnIfVlanRangeTop3=rtmL2vpnIfVlanRangeTop3, rtmL2vpnIfVlanRangeTop2=rtmL2vpnIfVlanRangeTop2, rtmL2vpnVplsIfVcid=rtmL2vpnVplsIfVcid, rtmL2vpnVplsIfVpnName=rtmL2vpnVplsIfVpnName)
