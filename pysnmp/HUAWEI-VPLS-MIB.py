#
# PySNMP MIB module HUAWEI-VPLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VPLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hwMpls, = mibBuilder.importSymbols("HUAWEI-MIB", "hwMpls")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, NotificationType, ModuleIdentity, Counter32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Bits, iso, ObjectIdentity, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Bits", "iso", "ObjectIdentity", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwMplsVpls = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5))
if mibBuilder.loadTexts: hwMplsVpls.setLastUpdated('200305080900Z')
if mibBuilder.loadTexts: hwMplsVpls.setOrganization('Huawei Technologies Co., Ltd.')
class L2VpnState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("l2VpnStateDown", 0), ("l2VpnStateUp", 1))

class L2VpnEncapsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 64, 255))
    namedValues = NamedValues(("l2VpnEncapsFr", 1), ("l2VpnEncapsAtmAal5", 2), ("l2VpnEncapsAtmCellTransport", 3), ("l2VpnEncapsVlan", 4), ("l2VpnEncapsEthernet", 5), ("l2VpnEncapsHdlc", 6), ("l2VpnEncapsPpp", 7), ("l2VpnEncapsCem", 8), ("l2VpnEncapsAtmCellVcc", 9), ("l2VpnEncapsAtmCellVpc", 10), ("l2VpnEncapsMpls", 11), ("l2VpnEncapsVpls", 12), ("l2VpnEncapsIpInterworking", 64), ("l2VpnEncapsUnsupported", 255))

class L2VpnDownReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("l2VpnReasonOk", 0), ("l2VpnSessionDown", 1), ("l2VpnTunnelDown", 2), ("l2VpnLabelWithdraw", 3), ("l2VpnLabelRelease", 4), ("l2VpnEncapIfDown", 5), ("l2VpnDeleteVC", 6))

hwVplsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1))
hwVplsVCStateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1), )
if mibBuilder.loadTexts: hwVplsVCStateTable.setStatus('current')
hwVplsVCStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1), ).setIndexNames((0, "HUAWEI-VPLS-MIB", "hwVplsVCId"), (0, "HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"))
if mibBuilder.loadTexts: hwVplsVCStateEntry.setStatus('current')
hwVplsVCId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCId.setStatus('current')
hwVplsVCEncapsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 2), L2VpnEncapsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCEncapsType.setStatus('current')
hwVplsVCClientIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCClientIf.setStatus('current')
hwVplsVCLocalLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCLocalLabel.setStatus('current')
hwVplsVCRemoteLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCRemoteLabel.setStatus('current')
hwVplsVCTunnelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCTunnelLabel.setStatus('current')
hwVplsVCL2Mtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCL2Mtu.setStatus('current')
hwVplsVCState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 8), L2VpnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCState.setStatus('current')
hwVplsVCDownReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 1, 1, 1, 9), L2VpnDownReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVplsVCDownReason.setStatus('current')
hwVplsMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2))
hwVplsVCStateDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2, 1)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCId"), ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"), ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
if mibBuilder.loadTexts: hwVplsVCStateDown.setStatus('current')
hwVplsVCStateUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 2, 2)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCId"), ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"), ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
if mibBuilder.loadTexts: hwVplsVCStateUp.setStatus('current')
hwVplsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3))
hwVplsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 1))
hwVplsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 1, 1)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCStateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVplsMIBCompliance = hwVplsMIBCompliance.setStatus('current')
hwVplsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 2))
hwVplsVCStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5, 3, 2, 1)).setObjects(("HUAWEI-VPLS-MIB", "hwVplsVCId"), ("HUAWEI-VPLS-MIB", "hwVplsVCEncapsType"), ("HUAWEI-VPLS-MIB", "hwVplsVCClientIf"), ("HUAWEI-VPLS-MIB", "hwVplsVCLocalLabel"), ("HUAWEI-VPLS-MIB", "hwVplsVCRemoteLabel"), ("HUAWEI-VPLS-MIB", "hwVplsVCTunnelLabel"), ("HUAWEI-VPLS-MIB", "hwVplsVCL2Mtu"), ("HUAWEI-VPLS-MIB", "hwVplsVCState"), ("HUAWEI-VPLS-MIB", "hwVplsVCDownReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVplsVCStateGroup = hwVplsVCStateGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-VPLS-MIB", PYSNMP_MODULE_ID=hwMplsVpls, hwVplsVCStateTable=hwVplsVCStateTable, L2VpnState=L2VpnState, hwMplsVpls=hwMplsVpls, hwVplsVCRemoteLabel=hwVplsVCRemoteLabel, hwVplsMIBConformance=hwVplsMIBConformance, hwVplsMIBCompliances=hwVplsMIBCompliances, hwVplsMIBTraps=hwVplsMIBTraps, hwVplsVCStateGroup=hwVplsVCStateGroup, hwVplsVCDownReason=hwVplsVCDownReason, hwVplsVCState=hwVplsVCState, hwVplsVCStateDown=hwVplsVCStateDown, hwVplsVCTunnelLabel=hwVplsVCTunnelLabel, hwVplsVCClientIf=hwVplsVCClientIf, hwVplsVCStateUp=hwVplsVCStateUp, hwVplsMIBCompliance=hwVplsMIBCompliance, hwVplsVCLocalLabel=hwVplsVCLocalLabel, hwVplsVCStateEntry=hwVplsVCStateEntry, L2VpnDownReason=L2VpnDownReason, hwVplsMIBObjects=hwVplsMIBObjects, hwVplsVCL2Mtu=hwVplsVCL2Mtu, hwVplsVCEncapsType=hwVplsVCEncapsType, L2VpnEncapsType=L2VpnEncapsType, hwVplsMIBGroups=hwVplsMIBGroups, hwVplsVCId=hwVplsVCId)
