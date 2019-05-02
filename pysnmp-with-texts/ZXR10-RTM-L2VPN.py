#
# PySNMP MIB module ZXR10-RTM-L2VPN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-RTM-L2VPN
# Produced by pysmi-0.3.4 at Wed May  1 15:48:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Integer32, Unsigned32, Bits, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter32", "ObjectIdentity", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
zxr10L2vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L2vpn")
rtmL2vpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3))
rtmL2vpnMIB.setRevisions(('2005-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rtmL2vpnMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: rtmL2vpnMIB.setLastUpdated('200507260000Z')
if mibBuilder.loadTexts: rtmL2vpnMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: rtmL2vpnMIB.setContactInfo('ZTE Corporation NanJing Institute of ZTE Corporation No.68 Zijinghua Rd. Yuhuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: rtmL2vpnMIB.setDescription('ZXROS v4.6.03 RTM L2vpn query and configuration MIB')
rtmL2vpnVcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0))
rtmL2vpnVplsIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class RtmL2vpnEncapType(TextualConvention, Integer32):
    description = 'Mpls L2vpn Vfi Interface EncapType'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("encap-UNKNOWN", 0), ("encap-FR-DLCI", 1), ("encap-ATM-AAL5", 2), ("encap-ATM-TRANSCELL", 3), ("encap-ETH-VLAN", 4), ("encap-ETH", 5), ("encap-HDLC", 6), ("encap-PPP", 7), ("encap-CEM", 8), ("encap-ATM-VCC", 9), ("encap-ATM-VPC", 10))

class RtmL2vpnType(TextualConvention, Integer32):
    description = 'Rtm L2vpn Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("l2vpn-UNKNOWN", 0), ("l2vpn-VPWS", 1), ("l2vpn-VPLS", 2), ("l2vpn-IPLS", 3))

class RtmL2vpnVCStatus(TextualConvention, Integer32):
    description = 'Rtm L2vpn Vc Status'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("vc-Down", 0), ("vc-Up", 1))

class RtmL2vpnCsType(TextualConvention, Integer32):
    description = 'Rtm L2vpn Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("server", 0), ("client", 1))

rtmL2vpnIfTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1), )
if mibBuilder.loadTexts: rtmL2vpnIfTable.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfTable.setDescription('Mpls L2vpn Interface Information query table')
rtmL2vpnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1), ).setIndexNames((0, "ZXR10-RTM-L2VPN", "rtmL2vpnVplsIfVcid"), (0, "ZXR10-RTM-L2VPN", "rtmL2vpnVplsIfIndex"))
if mibBuilder.loadTexts: rtmL2vpnIfEntry.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfEntry.setDescription('Interface Information of Rtm L2vpn instance')
rtmL2vpnVplsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfIndex.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVplsIfIndex.setDescription('Rtm L2vpn Vfi Interface Index')
rtmL2vpnVplsIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfName.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVplsIfName.setDescription('Rtm L2vpn Vfi Interface Name')
rtmL2vpnVplsIfEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfEncapType.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVplsIfEncapType.setDescription('Rtm L2vpn Vfi Interface EncapType')
rtmL2vpnVplsIfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 21))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfVpnName.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVplsIfVpnName.setDescription('Rtm L2vpn Vfi Interface Vpn Name')
rtmL2vpnVplsIfVcid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfVcid.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVplsIfVcid.setDescription('Rtm L2vpn Vfi Interface Vcid')
rtmL2vpnVplsIfVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVplsIfVpnType.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVplsIfVpnType.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfQinQEx = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfQinQEx.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfQinQEx.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfQinQIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfQinQIn.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfQinQIn.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfVlanRangeTop1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop1.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop1.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfVlanRangeTop2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop2.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop2.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfVlanRangeTop3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop3.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeTop3.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfVlanRangeBot1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot1.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot1.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfVlanRangeBot2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot2.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot2.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfVlanRangeBot3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot3.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfVlanRangeBot3.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnIfCSAttr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 1, 1, 1, 15), RtmL2vpnCsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnIfCSAttr.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnIfCSAttr.setDescription('Rtm L2vpn Vfi Interface Vpn Type')
rtmL2vpnVcTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1), )
if mibBuilder.loadTexts: rtmL2vpnVcTable.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVcTable.setDescription('Mpls L2vpn Vc Information query table')
rtmL2vpnVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1), ).setIndexNames((0, "ZXR10-RTM-L2VPN", "rtmL2vpnVCInInternalLabel"))
if mibBuilder.loadTexts: rtmL2vpnVcEntry.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVcEntry.setDescription('Vc Information of Rtm L2vpn instance')
rtmL2vpnVCVcId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCVcId.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCVcId.setDescription('Rtm L2vpn Vcid')
rtmL2vpnVCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 2), RtmL2vpnVCStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCStatus.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCStatus.setDescription('Rtm L2vpn Vc Status')
rtmL2vpnVCPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCPeerIP.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCPeerIP.setDescription('Rtm L2vpn Vc peer address')
rtmL2vpnVCInInternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCInInternalLabel.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCInInternalLabel.setDescription('Rtm L2vpn VC InInternalLabel')
rtmL2vpnVCOutInternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCOutInternalLabel.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCOutInternalLabel.setDescription('Rtm L2vpn VC InInternalLabel')
rtmL2vpnVCInExternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCInExternalLabel.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCInExternalLabel.setDescription('Rtm L2vpn VC InInternalLabel')
rtmL2vpnVCOutExternalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 3, 0, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtmL2vpnVCOutExternalLabel.setStatus('current')
if mibBuilder.loadTexts: rtmL2vpnVCOutExternalLabel.setDescription('Rtm L2vpn VC InInternalLabel')
mibBuilder.exportSymbols("ZXR10-RTM-L2VPN", rtmL2vpnIfVlanRangeTop1=rtmL2vpnIfVlanRangeTop1, rtmL2vpnIfEntry=rtmL2vpnIfEntry, InterfaceIndex=InterfaceIndex, rtmL2vpnMIB=rtmL2vpnMIB, rtmL2vpnVCInExternalLabel=rtmL2vpnVCInExternalLabel, rtmL2vpnVcEntry=rtmL2vpnVcEntry, rtmL2vpnVCPeerIP=rtmL2vpnVCPeerIP, rtmL2vpnVCStatus=rtmL2vpnVCStatus, rtmL2vpnVplsIfObjects=rtmL2vpnVplsIfObjects, rtmL2vpnIfVlanRangeTop3=rtmL2vpnIfVlanRangeTop3, rtmL2vpnVplsIfEncapType=rtmL2vpnVplsIfEncapType, rtmL2vpnIfTable=rtmL2vpnIfTable, rtmL2vpnVCOutExternalLabel=rtmL2vpnVCOutExternalLabel, rtmL2vpnIfVlanRangeTop2=rtmL2vpnIfVlanRangeTop2, rtmL2vpnVplsIfVpnName=rtmL2vpnVplsIfVpnName, rtmL2vpnIfQinQEx=rtmL2vpnIfQinQEx, rtmL2vpnIfVlanRangeBot2=rtmL2vpnIfVlanRangeBot2, rtmL2vpnVCOutInternalLabel=rtmL2vpnVCOutInternalLabel, rtmL2vpnIfQinQIn=rtmL2vpnIfQinQIn, RtmL2vpnType=RtmL2vpnType, rtmL2vpnVCInInternalLabel=rtmL2vpnVCInInternalLabel, rtmL2vpnVplsIfName=rtmL2vpnVplsIfName, rtmL2vpnVcObjects=rtmL2vpnVcObjects, RtmL2vpnEncapType=RtmL2vpnEncapType, rtmL2vpnIfVlanRangeBot3=rtmL2vpnIfVlanRangeBot3, rtmL2vpnVplsIfVpnType=rtmL2vpnVplsIfVpnType, rtmL2vpnVcTable=rtmL2vpnVcTable, rtmL2vpnVCVcId=rtmL2vpnVCVcId, rtmL2vpnIfVlanRangeBot1=rtmL2vpnIfVlanRangeBot1, rtmL2vpnVplsIfIndex=rtmL2vpnVplsIfIndex, rtmL2vpnVplsIfVcid=rtmL2vpnVplsIfVcid, rtmL2vpnIfCSAttr=rtmL2vpnIfCSAttr, DisplayString=DisplayString, RtmL2vpnVCStatus=RtmL2vpnVCStatus, PYSNMP_MODULE_ID=rtmL2vpnMIB, RtmL2vpnCsType=RtmL2vpnCsType)
