#
# PySNMP MIB module ZXR10-MPLS-L2VPN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-MPLS-L2VPN
# Produced by pysmi-0.3.4 at Wed May  1 15:48:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Integer32, ModuleIdentity, Counter32, Gauge32, IpAddress, MibIdentifier, Unsigned32, TimeTicks, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Integer32", "ModuleIdentity", "Counter32", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxr10L2vpn, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10L2vpn")
zxr10MplsL2vpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1))
zxr10MplsL2vpnMIB.setRevisions(('2005-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zxr10MplsL2vpnMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: zxr10MplsL2vpnMIB.setLastUpdated('200507260000Z')
if mibBuilder.loadTexts: zxr10MplsL2vpnMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: zxr10MplsL2vpnMIB.setContactInfo('ZTE Corporation Nanjing Institute of ZTE Corporation No.68 Zijinghua Rd. Yuhuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: zxr10MplsL2vpnMIB.setDescription('ZXROS v4.6.03 Mpls L2vpn query and configuration MIB')
zxr10MplsL2vpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0))
zxr10MplsL2vpnPWObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1))
zxr10MplsL2vpnVpwsIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2))
zxr10MplsL2vpnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3))
zxr10MplsL2vpnTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsL2vpnType(TextualConvention, Integer32):
    description = 'Mpls L2vpn type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("l2vpn-UNKNOWN", 0), ("l2vpn-VPWS", 1), ("l2vpn-VPLS", 2), ("l2vpn-IPLS", 3))

class MplsL2vpnPWType(TextualConvention, Integer32):
    description = 'Mpls L2vpn PW type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("pw-UNKNOWN", 0), ("pw-SPOKE", 1), ("pw-HUB", 2))

class MplsL2vpnPWEncapsulationType(TextualConvention, Integer32):
    description = 'Mpls L2vpn PW encapsulation type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("encap-UNKNOWN", 0), ("encap-FR-DLCI", 1), ("encap-ATM-AAL5", 2), ("encap-ATM-TRANSCELL", 3), ("encap-ETH-VLAN", 4), ("encap-ETH", 5), ("encap-HDLC", 6), ("encap-PPP", 7), ("encap-CEM", 8), ("encap-ATM-VCC", 9), ("encap-ATM-VPC", 10))

class MplsL2vpnPWCbit(TextualConvention, Integer32):
    description = 'Mpls L2vpn PW type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("cword-DISABLE", 0), ("cword-ENABLE", 1))

class MplsL2vpnPWPsnType(TextualConvention, Integer32):
    description = 'Mpls L2vpn PW external label encapsulation type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown-tunnel", 0), ("mpls-tunnel", 1), ("te-tunnel", 2))

class MplsL2vpnPWStatus(TextualConvention, Integer32):
    description = 'Mpls L2vpn PW status'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("not-established", 0), ("established", 1))

class MplsL2vpnTrapLevel(TextualConvention, Integer32):
    description = 'Mpls L2vpn Trap level.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergencies", 1), ("alerts", 2), ("critical", 3), ("errors", 4), ("warnings", 5), ("notifications", 6), ("informational", 7), ("debugging", 8))

class MplsL2vpnTrapDetail(TextualConvention, Integer32):
    description = 'Mpls L2vpn Trap infromation in detail.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("if-phy-down", 1), ("if-proto-down", 2), ("if-admini-down", 3), ("if-disappear", 4), ("if-encap-chg", 5), ("if-mtu-chg", 6), ("link-no-route", 7), ("link-te-tunnel-down", 8), ("link-no-mpls-tunnel", 9), ("link-no-te-tunnel", 10), ("proto-vc-withdraw", 11), ("proto-sess-down", 12), ("proto-no-vpws", 13), ("proto-no-vpls-peer", 14), ("proto-vctype-negotiate-fail", 15), ("proto-mtu-negotiate-fail", 16), ("proto-cbit-negotiate-fail", 17), ("proto-no-vfi", 18))

zxr10MplsL2vpnInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1), )
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceTable.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceTable.setDescription('Mpls L2vpn instance query table')
zxr10MplsL2vpnInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1), ).setIndexNames((0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnInstanceVCId"))
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceEntry.setDescription('Information of Mpls L2vpn instance configured on a PE')
zxr10MplsL2vpnInstanceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 1), MplsL2vpnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceType.setDescription('Mpls L2vpn type,including:vpls,vpws and ipls ')
zxr10MplsL2vpnInstanceVCId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceVCId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceVCId.setDescription('Mpls L2vpn unique vcid value on a PE.')
zxr10MplsL2vpnInstanceVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 21))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceVpnName.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnInstanceVpnName.setDescription('Name specified for each configured Mpls L2vpn.')
zxr10MplsL2vpnPwCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 0, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPwCounts.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPwCounts.setDescription('Number of PWs that belongs to a certain Mpls L2vpn')
zxr10MplsL2vpnPWTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1), )
if mibBuilder.loadTexts: zxr10MplsL2vpnPWTable.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWTable.setDescription('Mpls L2vpn PW query table.')
zxr10MplsL2vpnPWEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1), ).setIndexNames((0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnPWVcId"), (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnPWRemoteRouterId"))
if mibBuilder.loadTexts: zxr10MplsL2vpnPWEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWEntry.setDescription('Informatin of Mpls L2vpn PW configured on a PE.')
zxr10MplsL2vpnPWVcId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWVcId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWVcId.setDescription("VcId of Mpls L2vpn that PW belongs to.It can't be zero.")
zxr10MplsL2vpnPWType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 2), MplsL2vpnPWType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWType.setDescription(' Type of PW:hub or spoke,used in H-VPLS.')
zxr10MplsL2vpnPWEncapsulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 3), MplsL2vpnPWEncapsulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWEncapsulationType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWEncapsulationType.setDescription('Mpls L2vpn PW encapsulation type.')
zxr10MplsL2vpnPWVlanid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWVlanid.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWVlanid.setDescription('if zxr10MplsL2vpnPWEncapsulationType is eth-vlan type,this value represents vlan id encapsulated for L2vpn interface.It will be zero otherwise.')
zxr10MplsL2vpnPWPsnType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 5), MplsL2vpnPWPsnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWPsnType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWPsnType.setDescription('Type of external tunnel for this PW to be carried on.')
zxr10MplsL2vpnPWTunnelid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWTunnelid.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWTunnelid.setDescription('If zxr10MplsL2vpnPWPsnType is TE tunnel,this value represents Id of TE tunnel for this PW to be carried on. It will be zero otherwise.')
zxr10MplsL2vpnPWInlabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWInlabel.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWInlabel.setDescription('The PW internal label used in the inbound direction,ie label locally allocated. If the label is not yet known,the object should return a value of 0xFFFFFFFF.')
zxr10MplsL2vpnPWOutlabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWOutlabel.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWOutlabel.setDescription('The PW internal label used in the outbound direction,ie label allocated by remote peer.If the label is not yet known,the object should return a value of 0xFFFFFFFF.')
zxr10MplsL2vpnPWCbit = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 9), MplsL2vpnPWCbit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWCbit.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWCbit.setDescription('Defines if the control word will be sent with each packet by the local node.')
zxr10MplsL2vpnPWStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 10), MplsL2vpnPWStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWStatus.setDescription('If PW has finished negotiation with remote peer including internal label and other parameters,then PW will be in established status.')
zxr10MplsL2vpnPWLocalGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalGroupId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalGroupId.setDescription('Used in the Group ID field sent to peer within the maintenance protocol used for PW setup.')
zxr10MplsL2vpnPWLocalEncapsulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 12), MplsL2vpnPWEncapsulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalEncapsulationType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalEncapsulationType.setDescription('Local Mpls L2vpn PW encapsulation type.')
zxr10MplsL2vpnPWLocalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalLabel.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalLabel.setDescription('PW internal label locally allocated.If the label is not yet known, the object should return a value of 0xFFFFFFFF. ')
zxr10MplsL2vpnPWLocalCbit = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 14), MplsL2vpnPWCbit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalCbit.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalCbit.setDescription('Local configuration of the control word.')
zxr10MplsL2vpnPWLocalPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalPortName.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalPortName.setDescription('Name of local interface that PW has been configured on.')
zxr10MplsL2vpnPWLocalRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalRouterId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalRouterId.setDescription('Router ID of local PE.')
zxr10MplsL2vpnPWLocalIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalIfMtu.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWLocalIfMtu.setDescription('Locally supported MTU size over the interface associated with the PW.')
zxr10MplsL2vpnPWRemoteGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteGroupId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteGroupId.setDescription('Obtained from the Group ID field as received via the signaling protocol used for PW setup.')
zxr10MplsL2vpnPWRemoteEncapsulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 19), MplsL2vpnPWEncapsulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteEncapsulationType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteEncapsulationType.setDescription('Remote Mpls L2vpn PW encapsulation type.')
zxr10MplsL2vpnPWRemoteLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteLabel.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteLabel.setDescription('PW internal label allocated by remote peer.If the label is not yet known, the object should return a value of 0xFFFFFFFF. ')
zxr10MplsL2vpnPWRemoteCbit = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 21), MplsL2vpnPWCbit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteCbit.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteCbit.setDescription('Remote configuration of the control word.')
zxr10MplsL2vpnPWRemotePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemotePortName.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemotePortName.setDescription('Name of remote interface that PW has been configured on.')
zxr10MplsL2vpnPWRemoteRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 23), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteRouterId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteRouterId.setDescription('Router ID of remote PE.')
zxr10MplsL2vpnPWRemoteIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 1, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteIfMtu.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnPWRemoteIfMtu.setDescription('Supported MTU size of remote peer over the interface associated with the PW.')
zxr10MplsL2vpnVpwsIfTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1), )
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfTable.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfTable.setDescription('Mpls L2vpn instance query table')
zxr10MplsL2vpnVpwsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1), ).setIndexNames((0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnInstanceVCId"), (0, "ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnVpwsIfIndex"))
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfEntry.setDescription('Information of Mpls L2vpn instance configured on a PE')
zxr10MplsL2vpnVpwsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfIndex.setDescription('Index of the VPWS configuration interface.')
zxr10MplsL2vpnVpwsIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfName.setDescription('Name of the VPWS configuration interface.')
zxr10MplsL2vpnVpwsIfEncapsulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 3), MplsL2vpnPWEncapsulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfEncapsulationType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfEncapsulationType.setDescription('Encapsulation type of the VPWS configuration interface.')
zxr10MplsL2vpnVpwsIfVcid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfVcid.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfVcid.setDescription('Vcid of the VPWS configured on this interface.')
zxr10MplsL2vpnVpwsIfVpnType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 2, 1, 1, 5), MplsL2vpnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfVpnType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnVpwsIfVpnType.setDescription('Type of the L2VPN configured on this interface.')
zxr10MplsL2vpnTrapIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapIfIndex.setDescription('If a L2vpn configuration interface is down,a interface down trap pdu will be sent;zxr10MplsL2vpnTrapIfIndex is index of this interface in if table.')
zxr10MplsL2vpnTrapIfName = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapIfName.setDescription('If a L2vpn configuration interface is down,a interface down trap will be sent;zxr10MplsL2vpnTrapIfName is name of this interface.')
zxr10MplsL2vpnTrapLevel = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 3), MplsL2vpnTrapLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapLevel.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapLevel.setDescription('Alerting level of Trap pdu.')
zxr10MplsL2vpnTrapDetail = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 4), MplsL2vpnTrapDetail()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapDetail.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapDetail.setDescription('Detailed information of Trap arising.')
zxr10MplsL2vpnTrapVcid = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapVcid.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapVcid.setDescription('Vcid of L2vpn affected.')
zxr10MplsL2vpnTrapPeerAddress = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapPeerAddress.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapPeerAddress.setDescription('Peer Address of VC affected.')
zxr10MplsL2vpnTrapVpnType = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 7), MplsL2vpnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapVpnType.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapVpnType.setDescription('Peer Address of VC affected.')
zxr10MplsL2vpnTrapTETunnelId = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 4, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapTETunnelId.setStatus('current')
if mibBuilder.loadTexts: zxr10MplsL2vpnTrapTETunnelId.setDescription('TE Tunnel Id which VC has been bound to.')
mplsL2vpnGenericInterfaceTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 1)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfIndex"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfName"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVpnType"))
if mibBuilder.loadTexts: mplsL2vpnGenericInterfaceTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnGenericInterfaceTrap.setDescription('When one of following conditions happens: (1)Admini,phy or protocol status of a interface is down and it has no children. (2)Interface is off and it has no children. (3)Encapsulation of a interface has changed. (4)MTU of a interface has changed. this type of Trap pdu will be sent.There is only one VPWS type VC affected.')
mplsL2vpnMatchInterfaceTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 2)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfIndex"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapIfName"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"))
if mibBuilder.loadTexts: mplsL2vpnMatchInterfaceTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnMatchInterfaceTrap.setDescription('When one of following conditions happens: (1)Admini,phy or protocol status of a interface is down and it has children. (2)Interface is off and it has children. this type of Trap pdu will be sent.')
mplsL2vpnGenericProtocolTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 3)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVpnType"))
if mibBuilder.loadTexts: mplsL2vpnGenericProtocolTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnGenericProtocolTrap.setDescription('When one of following conditions happens: (1)Receives a VC label withdraw message from remote peer. (2)Deletes a VPWS VC. (3)Delete a VPLS peer. (4)Protocol patameters negotiation fails during VC setup. this type of Trap pdu will be sent.')
mplsL2vpnSessionDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 4)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"))
if mibBuilder.loadTexts: mplsL2vpnSessionDownTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnSessionDownTrap.setDescription('When session to VC peer is down,all the VC that have been bound to mpls Lsp Tunnel will be down;this kind of trap will be sent.')
mplsL2vpnVplsDeleteTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 5)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"))
if mibBuilder.loadTexts: mplsL2vpnVplsDeleteTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnVplsDeleteTrap.setDescription('When delete a VPLS instance.,this kind of trap will be sent.')
mplsL2vpnLinkTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 6)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVcid"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapVpnType"))
if mibBuilder.loadTexts: mplsL2vpnLinkTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnLinkTrap.setDescription("When one of following conditions happens: (1)The PSN route is off. (2)Can't find outer mpls tunnel label. (3)Can't find outer TE tunnel label. this type of Trap pdu will be sent.")
mplsL2vpnPsnRouteDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 7)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapPeerAddress"))
if mibBuilder.loadTexts: mplsL2vpnPsnRouteDownTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnPsnRouteDownTrap.setDescription('When PSN route between PE is down,all the VC between them will be down; this type of Trap pdu will be sent.')
mplsL2vpnTETunnelDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 104, 1, 3, 8)).setObjects(("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapLevel"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapDetail"), ("ZXR10-MPLS-L2VPN", "zxr10MplsL2vpnTrapTETunnelId"))
if mibBuilder.loadTexts: mplsL2vpnTETunnelDownTrap.setStatus('current')
if mibBuilder.loadTexts: mplsL2vpnTETunnelDownTrap.setDescription('When one TE Tunnel between is dwon,all the VC between them which has been bound to this tunnel will be down;this type of Trap pdu will be sent')
mibBuilder.exportSymbols("ZXR10-MPLS-L2VPN", zxr10MplsL2vpnPWTable=zxr10MplsL2vpnPWTable, zxr10MplsL2vpnTrapObjects=zxr10MplsL2vpnTrapObjects, zxr10MplsL2vpnPWLocalLabel=zxr10MplsL2vpnPWLocalLabel, zxr10MplsL2vpnPWType=zxr10MplsL2vpnPWType, zxr10MplsL2vpnPWLocalRouterId=zxr10MplsL2vpnPWLocalRouterId, DisplayString=DisplayString, mplsL2vpnVplsDeleteTrap=mplsL2vpnVplsDeleteTrap, mplsL2vpnSessionDownTrap=mplsL2vpnSessionDownTrap, MplsL2vpnPWPsnType=MplsL2vpnPWPsnType, MplsL2vpnTrapDetail=MplsL2vpnTrapDetail, mplsL2vpnTETunnelDownTrap=mplsL2vpnTETunnelDownTrap, zxr10MplsL2vpnPwCounts=zxr10MplsL2vpnPwCounts, zxr10MplsL2vpnPWLocalCbit=zxr10MplsL2vpnPWLocalCbit, zxr10MplsL2vpnNotifications=zxr10MplsL2vpnNotifications, MplsL2vpnTrapLevel=MplsL2vpnTrapLevel, mplsL2vpnPsnRouteDownTrap=mplsL2vpnPsnRouteDownTrap, zxr10MplsL2vpnVpwsIfEncapsulationType=zxr10MplsL2vpnVpwsIfEncapsulationType, zxr10MplsL2vpnVpwsIfVpnType=zxr10MplsL2vpnVpwsIfVpnType, zxr10MplsL2vpnVpwsIfIndex=zxr10MplsL2vpnVpwsIfIndex, zxr10MplsL2vpnTrapLevel=zxr10MplsL2vpnTrapLevel, mplsL2vpnLinkTrap=mplsL2vpnLinkTrap, zxr10MplsL2vpnPWObjects=zxr10MplsL2vpnPWObjects, zxr10MplsL2vpnVpwsIfName=zxr10MplsL2vpnVpwsIfName, zxr10MplsL2vpnPWLocalIfMtu=zxr10MplsL2vpnPWLocalIfMtu, zxr10MplsL2vpnObjects=zxr10MplsL2vpnObjects, zxr10MplsL2vpnInstanceType=zxr10MplsL2vpnInstanceType, zxr10MplsL2vpnPWVlanid=zxr10MplsL2vpnPWVlanid, zxr10MplsL2vpnPWInlabel=zxr10MplsL2vpnPWInlabel, MplsL2vpnType=MplsL2vpnType, MplsL2vpnPWType=MplsL2vpnPWType, zxr10MplsL2vpnTrapTETunnelId=zxr10MplsL2vpnTrapTETunnelId, PYSNMP_MODULE_ID=zxr10MplsL2vpnMIB, zxr10MplsL2vpnPWLocalEncapsulationType=zxr10MplsL2vpnPWLocalEncapsulationType, mplsL2vpnMatchInterfaceTrap=mplsL2vpnMatchInterfaceTrap, zxr10MplsL2vpnVpwsIfObjects=zxr10MplsL2vpnVpwsIfObjects, zxr10MplsL2vpnVpwsIfEntry=zxr10MplsL2vpnVpwsIfEntry, zxr10MplsL2vpnPWVcId=zxr10MplsL2vpnPWVcId, zxr10MplsL2vpnPWRemoteEncapsulationType=zxr10MplsL2vpnPWRemoteEncapsulationType, zxr10MplsL2vpnPWRemoteRouterId=zxr10MplsL2vpnPWRemoteRouterId, zxr10MplsL2vpnPWRemoteIfMtu=zxr10MplsL2vpnPWRemoteIfMtu, zxr10MplsL2vpnTrapPeerAddress=zxr10MplsL2vpnTrapPeerAddress, InterfaceIndex=InterfaceIndex, MplsL2vpnPWEncapsulationType=MplsL2vpnPWEncapsulationType, MplsL2vpnPWStatus=MplsL2vpnPWStatus, MplsL2vpnPWCbit=MplsL2vpnPWCbit, zxr10MplsL2vpnInstanceTable=zxr10MplsL2vpnInstanceTable, zxr10MplsL2vpnInstanceVpnName=zxr10MplsL2vpnInstanceVpnName, zxr10MplsL2vpnPWCbit=zxr10MplsL2vpnPWCbit, zxr10MplsL2vpnPWEntry=zxr10MplsL2vpnPWEntry, zxr10MplsL2vpnPWLocalGroupId=zxr10MplsL2vpnPWLocalGroupId, zxr10MplsL2vpnVpwsIfVcid=zxr10MplsL2vpnVpwsIfVcid, mplsL2vpnGenericInterfaceTrap=mplsL2vpnGenericInterfaceTrap, zxr10MplsL2vpnPWPsnType=zxr10MplsL2vpnPWPsnType, zxr10MplsL2vpnVpwsIfTable=zxr10MplsL2vpnVpwsIfTable, zxr10MplsL2vpnTrapDetail=zxr10MplsL2vpnTrapDetail, mplsL2vpnGenericProtocolTrap=mplsL2vpnGenericProtocolTrap, zxr10MplsL2vpnPWRemoteLabel=zxr10MplsL2vpnPWRemoteLabel, zxr10MplsL2vpnPWTunnelid=zxr10MplsL2vpnPWTunnelid, zxr10MplsL2vpnTrapIfIndex=zxr10MplsL2vpnTrapIfIndex, zxr10MplsL2vpnPWStatus=zxr10MplsL2vpnPWStatus, zxr10MplsL2vpnTrapVcid=zxr10MplsL2vpnTrapVcid, zxr10MplsL2vpnPWOutlabel=zxr10MplsL2vpnPWOutlabel, zxr10MplsL2vpnInstanceEntry=zxr10MplsL2vpnInstanceEntry, zxr10MplsL2vpnTrapVpnType=zxr10MplsL2vpnTrapVpnType, zxr10MplsL2vpnPWRemoteGroupId=zxr10MplsL2vpnPWRemoteGroupId, zxr10MplsL2vpnInstanceVCId=zxr10MplsL2vpnInstanceVCId, zxr10MplsL2vpnPWLocalPortName=zxr10MplsL2vpnPWLocalPortName, zxr10MplsL2vpnPWRemoteCbit=zxr10MplsL2vpnPWRemoteCbit, zxr10MplsL2vpnMIB=zxr10MplsL2vpnMIB, zxr10MplsL2vpnTrapIfName=zxr10MplsL2vpnTrapIfName, zxr10MplsL2vpnPWEncapsulationType=zxr10MplsL2vpnPWEncapsulationType, zxr10MplsL2vpnPWRemotePortName=zxr10MplsL2vpnPWRemotePortName)
