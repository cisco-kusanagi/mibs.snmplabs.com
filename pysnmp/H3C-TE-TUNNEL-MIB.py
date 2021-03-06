#
# PySNMP MIB module H3C-TE-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-TE-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
MplsLabel, MplsTunnelInstanceIndex, MplsTunnelIndex, MplsExtendedTunnelId = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabel", "MplsTunnelInstanceIndex", "MplsTunnelIndex", "MplsExtendedTunnelId")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Counter32, iso, Integer32, ObjectIdentity, ModuleIdentity, IpAddress, Unsigned32, Counter64, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "iso", "Integer32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Unsigned32", "Counter64", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32")
DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention")
h3cTeTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115))
if mibBuilder.loadTexts: h3cTeTunnel.setLastUpdated('201103240948Z')
if mibBuilder.loadTexts: h3cTeTunnel.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cTeTunnelScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 1))
h3cTeTunnelMaxTunnelIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 1, 1), MplsTunnelIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelMaxTunnelIndex.setStatus('current')
h3cTeTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2))
h3cTeTunnelStaticCrlspTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1), )
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspTable.setStatus('current')
h3cTeTunnelStaticCrlspEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1), ).setIndexNames((0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspInLabel"))
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspEntry.setStatus('current')
h3cTeTunnelStaticCrlspInLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 1), MplsLabel())
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspInLabel.setStatus('current')
h3cTeTunnelStaticCrlspName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspName.setStatus('current')
h3cTeTunnelStaticCrlspStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspStatus.setStatus('current')
h3cTeTunnelStaticCrlspRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("transit", 1), ("tail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspRole.setStatus('current')
h3cTeTunnelStaticCrlspXCPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 1, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelStaticCrlspXCPointer.setStatus('current')
h3cTeTunnelCoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2), )
if mibBuilder.loadTexts: h3cTeTunnelCoTable.setStatus('current')
h3cTeTunnelCoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1), ).setIndexNames((0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoIndex"), (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoLspInstance"), (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoIngressLSRId"), (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoEgressLSRId"))
if mibBuilder.loadTexts: h3cTeTunnelCoEntry.setStatus('current')
h3cTeTunnelCoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: h3cTeTunnelCoIndex.setStatus('current')
h3cTeTunnelCoLspInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 2), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: h3cTeTunnelCoLspInstance.setStatus('current')
h3cTeTunnelCoIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 3), MplsExtendedTunnelId())
if mibBuilder.loadTexts: h3cTeTunnelCoIngressLSRId.setStatus('current')
h3cTeTunnelCoEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 4), MplsExtendedTunnelId())
if mibBuilder.loadTexts: h3cTeTunnelCoEgressLSRId.setStatus('current')
h3cTeTunnelCoBiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coroutedActive", 1), ("coroutedPassive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelCoBiMode.setStatus('current')
h3cTeTunnelCoReverseLspInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 6), MplsTunnelInstanceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelCoReverseLspInstance.setStatus('current')
h3cTeTunnelCoReverseLspXCPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 2, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelCoReverseLspXCPointer.setStatus('current')
h3cTeTunnelPsTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3), )
if mibBuilder.loadTexts: h3cTeTunnelPsTable.setStatus('current')
h3cTeTunnelPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1), ).setIndexNames((0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsIndex"), (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsIngressLSRId"), (0, "H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsEgressLSRId"))
if mibBuilder.loadTexts: h3cTeTunnelPsEntry.setStatus('current')
h3cTeTunnelPsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: h3cTeTunnelPsIndex.setStatus('current')
h3cTeTunnelPsIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 2), MplsExtendedTunnelId())
if mibBuilder.loadTexts: h3cTeTunnelPsIngressLSRId.setStatus('current')
h3cTeTunnelPsEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 3), MplsExtendedTunnelId())
if mibBuilder.loadTexts: h3cTeTunnelPsEgressLSRId.setStatus('current')
h3cTeTunnelPsProtectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 4), MplsTunnelIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsProtectIndex.setStatus('current')
h3cTeTunnelPsProtectIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 5), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsProtectIngressLSRId.setStatus('current')
h3cTeTunnelPsProtectEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 6), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsProtectEgressLSRId.setStatus('current')
h3cTeTunnelPsProtectType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneToOne", 1), ("onePlusOne", 2))).clone('oneToOne')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsProtectType.setStatus('current')
h3cTeTunnelPsRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("revertive", 1), ("noRevertive", 2))).clone('revertive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsRevertiveMode.setStatus('current')
h3cTeTunnelPsWtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(24)).setUnits('30 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsWtrTime.setStatus('current')
h3cTeTunnelPsHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setUnits('500ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsHoldOffTime.setStatus('current')
h3cTeTunnelPsSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uniDirectional", 1), ("biDirectional", 2))).clone('uniDirectional')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsSwitchMode.setStatus('current')
h3cTeTunnelPsWorkPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("noDefect", 2), ("inDefect", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsWorkPathStatus.setStatus('current')
h3cTeTunnelPsProtectPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("noDefect", 2), ("inDefect", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsProtectPathStatus.setStatus('current')
h3cTeTunnelPsSwitchResult = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("workPath", 1), ("protectPath", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTeTunnelPsSwitchResult.setStatus('current')
h3cTeTunnelNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3))
h3cTeTunnelNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3, 0))
h3cTeTunnelPsSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3, 0, 1)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWorkPathStatus"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectPathStatus"))
if mibBuilder.loadTexts: h3cTeTunnelPsSwitchWtoP.setStatus('current')
h3cTeTunnelPsSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 3, 0, 2)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWorkPathStatus"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectPathStatus"))
if mibBuilder.loadTexts: h3cTeTunnelPsSwitchPtoW.setStatus('current')
h3cTeTunnelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4))
h3cTeTunnelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 1))
h3cTeTunnelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 1, 1)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelNotificationsGroup"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelScalarsGroup"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspGroup"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCorouteGroup"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cTeTunnelCompliance = h3cTeTunnelCompliance.setStatus('current')
h3cTeTunnelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2))
h3cTeTunnelNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 1)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchPtoW"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchWtoP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cTeTunnelNotificationsGroup = h3cTeTunnelNotificationsGroup.setStatus('current')
h3cTeTunnelScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 2)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelMaxTunnelIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cTeTunnelScalarsGroup = h3cTeTunnelScalarsGroup.setStatus('current')
h3cTeTunnelStaticCrlspGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 3)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspName"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspStatus"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspRole"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelStaticCrlspXCPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cTeTunnelStaticCrlspGroup = h3cTeTunnelStaticCrlspGroup.setStatus('current')
h3cTeTunnelCorouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 4)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoBiMode"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoReverseLspInstance"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelCoReverseLspXCPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cTeTunnelCorouteGroup = h3cTeTunnelCorouteGroup.setStatus('current')
h3cTeTunnelPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 115, 4, 2, 5)).setObjects(("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectIndex"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectIngressLSRId"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectEgressLSRId"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectType"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsRevertiveMode"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWtrTime"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsHoldOffTime"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchMode"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsWorkPathStatus"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsProtectPathStatus"), ("H3C-TE-TUNNEL-MIB", "h3cTeTunnelPsSwitchResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cTeTunnelPsGroup = h3cTeTunnelPsGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-TE-TUNNEL-MIB", h3cTeTunnelStaticCrlspStatus=h3cTeTunnelStaticCrlspStatus, h3cTeTunnelCompliance=h3cTeTunnelCompliance, h3cTeTunnelCoBiMode=h3cTeTunnelCoBiMode, h3cTeTunnelPsEgressLSRId=h3cTeTunnelPsEgressLSRId, h3cTeTunnelCoIngressLSRId=h3cTeTunnelCoIngressLSRId, h3cTeTunnelPsTable=h3cTeTunnelPsTable, h3cTeTunnelPsSwitchWtoP=h3cTeTunnelPsSwitchWtoP, h3cTeTunnelMaxTunnelIndex=h3cTeTunnelMaxTunnelIndex, h3cTeTunnelStaticCrlspName=h3cTeTunnelStaticCrlspName, h3cTeTunnelPsSwitchMode=h3cTeTunnelPsSwitchMode, h3cTeTunnelPsProtectPathStatus=h3cTeTunnelPsProtectPathStatus, h3cTeTunnelStaticCrlspEntry=h3cTeTunnelStaticCrlspEntry, h3cTeTunnelStaticCrlspGroup=h3cTeTunnelStaticCrlspGroup, h3cTeTunnelCoReverseLspInstance=h3cTeTunnelCoReverseLspInstance, h3cTeTunnelPsProtectEgressLSRId=h3cTeTunnelPsProtectEgressLSRId, h3cTeTunnelNotificationsPrefix=h3cTeTunnelNotificationsPrefix, h3cTeTunnelScalars=h3cTeTunnelScalars, h3cTeTunnelStaticCrlspTable=h3cTeTunnelStaticCrlspTable, h3cTeTunnelPsWorkPathStatus=h3cTeTunnelPsWorkPathStatus, h3cTeTunnelScalarsGroup=h3cTeTunnelScalarsGroup, h3cTeTunnelPsIngressLSRId=h3cTeTunnelPsIngressLSRId, h3cTeTunnelStaticCrlspInLabel=h3cTeTunnelStaticCrlspInLabel, h3cTeTunnelNotifications=h3cTeTunnelNotifications, h3cTeTunnelCorouteGroup=h3cTeTunnelCorouteGroup, PYSNMP_MODULE_ID=h3cTeTunnel, h3cTeTunnelStaticCrlspXCPointer=h3cTeTunnelStaticCrlspXCPointer, h3cTeTunnelCompliances=h3cTeTunnelCompliances, h3cTeTunnelPsProtectIngressLSRId=h3cTeTunnelPsProtectIngressLSRId, h3cTeTunnelPsGroup=h3cTeTunnelPsGroup, h3cTeTunnelPsHoldOffTime=h3cTeTunnelPsHoldOffTime, h3cTeTunnelPsRevertiveMode=h3cTeTunnelPsRevertiveMode, h3cTeTunnelObjects=h3cTeTunnelObjects, h3cTeTunnelPsProtectType=h3cTeTunnelPsProtectType, h3cTeTunnelCoReverseLspXCPointer=h3cTeTunnelCoReverseLspXCPointer, h3cTeTunnelPsProtectIndex=h3cTeTunnelPsProtectIndex, h3cTeTunnelConformance=h3cTeTunnelConformance, h3cTeTunnelGroups=h3cTeTunnelGroups, h3cTeTunnelCoLspInstance=h3cTeTunnelCoLspInstance, h3cTeTunnelNotificationsGroup=h3cTeTunnelNotificationsGroup, h3cTeTunnelCoEntry=h3cTeTunnelCoEntry, h3cTeTunnelCoIndex=h3cTeTunnelCoIndex, h3cTeTunnelPsSwitchPtoW=h3cTeTunnelPsSwitchPtoW, h3cTeTunnelPsSwitchResult=h3cTeTunnelPsSwitchResult, h3cTeTunnelStaticCrlspRole=h3cTeTunnelStaticCrlspRole, h3cTeTunnel=h3cTeTunnel, h3cTeTunnelPsWtrTime=h3cTeTunnelPsWtrTime, h3cTeTunnelCoEgressLSRId=h3cTeTunnelCoEgressLSRId, h3cTeTunnelCoTable=h3cTeTunnelCoTable, h3cTeTunnelPsIndex=h3cTeTunnelPsIndex, h3cTeTunnelPsEntry=h3cTeTunnelPsEntry)
