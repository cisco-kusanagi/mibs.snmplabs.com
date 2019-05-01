#
# PySNMP MIB module HUAWEI-VPLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VPLS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hwMpls, = mibBuilder.importSymbols("HUAWEI-MIB", "hwMpls")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, TimeTicks, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, NotificationType, Gauge32, Unsigned32, IpAddress, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "NotificationType", "Gauge32", "Unsigned32", "IpAddress", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwMplsVpls = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5))
if mibBuilder.loadTexts: hwMplsVpls.setLastUpdated('200305080900Z')
if mibBuilder.loadTexts: hwMplsVpls.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwMplsVpls.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwMplsVpls.setDescription('The HUAWEI-VPLS-MIB contains objects to manage VPLS.')
class L2VpnState(TextualConvention, Integer32):
    description = "An indication of the L2Vpn's state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("l2VpnStateDown", 0), ("l2VpnStateUp", 1))

class L2VpnEncapsType(TextualConvention, Integer32):
    description = "An indication of the L2Vpn's encapsulation type."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 64, 255))
    namedValues = NamedValues(("l2VpnEncapsFr", 1), ("l2VpnEncapsAtmAal5", 2), ("l2VpnEncapsAtmCellTransport", 3), ("l2VpnEncapsVlan", 4), ("l2VpnEncapsEthernet", 5), ("l2VpnEncapsHdlc", 6), ("l2VpnEncapsPpp", 7), ("l2VpnEncapsCem", 8), ("l2VpnEncapsAtmCellVcc", 9), ("l2VpnEncapsAtmCellVpc", 10), ("l2VpnEncapsMpls", 11), ("l2VpnEncapsVpls", 12), ("l2VpnEncapsIpInterworking", 64), ("l2VpnEncapsUnsupported", 255))

class L2VpnDownReason(TextualConvention, Integer32):
    description = "The type indicates the reason of VC's status down."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("l2VpnReasonOk", 0), ("l2VpnSessionDown", 1), ("l2VpnTunnelDown", 2), ("l2VpnLabelWithdraw", 3), ("l2VpnLabelRelease", 4), ("l2VpnEncapIfDown", 5), ("l2VpnDeleteVC", 6))

hwVplsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1))
hwVplsVCStateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1), )
if mibBuilder.loadTexts: hwVplsVCStateTable.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCStateTable.setDescription("This table contains the VPLS's VC state.")
hwVplsVCStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1), ).setIndexNames((0, "HUAWEI-VPLS-MIB", "hwVplsVCId"), (0, "HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"))
if mibBuilder.loadTexts: hwVplsVCStateEntry.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCStateEntry.setDescription('Provides the information of a VC state entry.')
hwVplsVCId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCId.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCId.setDescription("This object indicates the VC's ID.")
hwVplsVCEncapsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 2), L2VpnEncapsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCEncapsType.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCEncapsType.setDescription("This object indicates the VC's encapsulation type.")
hwVplsVCClientIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCClientIf.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCClientIf.setDescription("This object indicates the ifIndex of VC's client interface.")
hwVplsVCLocalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCLocalLabel.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCLocalLabel.setDescription("This object indicates the VC's local label.")
hwVplsVCRemoteLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCRemoteLabel.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCRemoteLabel.setDescription("This object indicates the VC's remote label.")
hwVplsVCTunnelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCTunnelLabel.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCTunnelLabel.setDescription("This object indicates the VC's tunnel label.")
hwVplsVCL2Mtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCL2Mtu.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCL2Mtu.setDescription("This object indicates the VC's layer2 MTU.")
hwVplsVCState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 8), L2VpnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCState.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCState.setDescription("This object indicates the VC's state.")
hwVplsVCDownReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 9), L2VpnDownReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCDownReason.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCDownReason.setDescription("This object indicates the reason of VC's status down.")
hwVplsMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2))
hwVplsVCStateDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2, 1)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCId"), ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"), ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
if mibBuilder.loadTexts: hwVplsVCStateDown.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCStateDown.setDescription("This notification indicates the VC's state changes to down.")
hwVplsVCStateUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2, 2)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCId"), ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"), ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
if mibBuilder.loadTexts: hwVplsVCStateUp.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCStateUp.setDescription("This notification indicates the VC's state changes to up.")
hwVplsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3))
hwVplsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 1))
hwVplsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 1, 1)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCStateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVplsMIBCompliance = hwVplsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwVplsMIBCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-VPLS-MIB.')
hwVplsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 2))
hwVplsVCStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 2, 1)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCId"), ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"), ("HUAWEI-VPLS-MIB", "hwVplsVCClientIf"), ("HUAWEI-VPLS-MIB", "hwVplsVCLocalLabel"), ("HUAWEI-VPLS-MIB", "hwVplsVCRemoteLabel"), ("HUAWEI-VPLS-MIB", "hwVplsVCTunnelLabel"), ("HUAWEI-VPLS-MIB", "hwVplsVCL2Mtu"), ("HUAWEI-VPLS-MIB", "hwVplsVCState"), ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVplsVCStateGroup = hwVplsVCStateGroup.setStatus('current')
if mibBuilder.loadTexts: hwVplsVCStateGroup.setDescription("The VPLS's VC state group.")
mibBuilder.exportSymbols("HUAWEI-VPLS-MIB", hwVplsVCStateEntry=hwVplsVCStateEntry, PYSNMP_MODULE_ID=hwMplsVpls, hwVplsVCStateUp=hwVplsVCStateUp, hwVplsVCStateTable=hwVplsVCStateTable, hwVplsMIBConformance=hwVplsMIBConformance, hwVplsVCTunnelLabel=hwVplsVCTunnelLabel, L2VpnState=L2VpnState, hwVplsMIBObjects=hwVplsMIBObjects, hwVplsVCDownReason=hwVplsVCDownReason, hwVplsVCStateGroup=hwVplsVCStateGroup, hwVplsVCClientIf=hwVplsVCClientIf, hwVplsMIBCompliance=hwVplsMIBCompliance, hwVplsVCL2Mtu=hwVplsVCL2Mtu, hwVplsVCEncapsType=hwVplsVCEncapsType, hwVplsVCStateDown=hwVplsVCStateDown, L2VpnDownReason=L2VpnDownReason, L2VpnEncapsType=L2VpnEncapsType, hwVplsVCRemoteLabel=hwVplsVCRemoteLabel, hwVplsMIBCompliances=hwVplsMIBCompliances, hwVplsVCId=hwVplsVCId, hwMplsVpls=hwMplsVpls, hwVplsMIBGroups=hwVplsMIBGroups, hwVplsMIBTraps=hwVplsMIBTraps, hwVplsVCState=hwVplsVCState, hwVplsVCLocalLabel=hwVplsVCLocalLabel)
