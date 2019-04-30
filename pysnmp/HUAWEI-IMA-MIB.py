#
# PySNMP MIB module HUAWEI-IMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-IMA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndexOrZero, InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, Bits, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, NotificationType, IpAddress, Counter64, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Bits", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "Counter64", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks")
TextualConvention, RowStatus, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime")
hwImaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176))
if mibBuilder.loadTexts: hwImaMIB.setLastUpdated('200902101400Z')
if mibBuilder.loadTexts: hwImaMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwImaMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1))
hwImaMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2))
class MilliSeconds(TextualConvention, Integer32):
    status = 'current'

class ImaGroupState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("notConfigured", 1), ("startUp", 2), ("startUpAck", 3), ("configAbortUnsupportedM", 4), ("configAbortIncompatibleSymmetry", 5), ("configAbortOther", 6), ("insufficientLinks", 7), ("blocked", 8), ("operational", 9), ("configAbortUnsupportedImaVersion", 10))

class ImaGroupSymmetry(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("symmetricOperation", 1), ("asymmetricOperation", 2), ("asymmetricConfiguration", 3))

class ImaFrameLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 64, 128, 256))
    namedValues = NamedValues(("m32", 32), ("m64", 64), ("m128", 128), ("m256", 256))

class ImaLinkState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notInGroup", 1), ("unusableNoGivenReason", 2), ("unusableFault", 3), ("unusableMisconnected", 4), ("unusableInhibited", 5), ("unusableFailed", 6), ("usable", 7), ("active", 8))

hwImaGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1), )
if mibBuilder.loadTexts: hwImaGroupTable.setStatus('current')
hwImaGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1), ).setIndexNames((0, "HUAWEI-IMA-MIB", "hwImaGroupIfIndex"))
if mibBuilder.loadTexts: hwImaGroupEntry.setStatus('current')
hwImaGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupIfIndex.setStatus('current')
hwImaGroupNeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 2), ImaGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupNeState.setStatus('current')
hwImaGroupFeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 3), ImaGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupFeState.setStatus('current')
hwImaGroupSymmetry = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 4), ImaGroupSymmetry().clone('symmetricOperation')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupSymmetry.setStatus('current')
hwImaGroupMinNumTxLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwImaGroupMinNumTxLinks.setStatus('current')
hwImaGroupMinNumRxLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwImaGroupMinNumRxLinks.setStatus('current')
hwImaGroupTxTimingRefLink = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupTxTimingRefLink.setStatus('current')
hwImaGroupRxTimingRefLink = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupRxTimingRefLink.setStatus('current')
hwImaGroupTxImaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupTxImaId.setStatus('current')
hwImaGroupRxImaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupRxImaId.setStatus('current')
hwImaGroupTxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 11), ImaFrameLength().clone('m128')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwImaGroupTxFrameLength.setStatus('current')
hwImaGroupRxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 12), ImaFrameLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupRxFrameLength.setStatus('current')
hwImaGroupDiffDelayMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 13), MilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(25, 100)).clone(25)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwImaGroupDiffDelayMax.setStatus('current')
hwImaGroupAlphaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupAlphaValue.setStatus('current')
hwImaGroupBetaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupBetaValue.setStatus('current')
hwImaGroupGammaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupGammaValue.setStatus('current')
hwImaGroupNumTxActLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupNumTxActLinks.setStatus('current')
hwImaGroupNumRxActLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupNumRxActLinks.setStatus('current')
hwImaGroupTxOamLabelValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupTxOamLabelValue.setStatus('current')
hwImaGroupRxOamLabelValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupRxOamLabelValue.setStatus('current')
hwImaGroupFirstLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 21), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaGroupFirstLinkIfIndex.setStatus('current')
hwImaLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2), )
if mibBuilder.loadTexts: hwImaLinkTable.setStatus('current')
hwImaLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1), ).setIndexNames((0, "HUAWEI-IMA-MIB", "hwImaLinkIfIndex"))
if mibBuilder.loadTexts: hwImaLinkEntry.setStatus('current')
hwImaLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwImaLinkIfIndex.setStatus('current')
hwImaLinkGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwImaLinkGroupIfIndex.setStatus('current')
hwImaLinkNeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 3), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaLinkNeTxState.setStatus('current')
hwImaLinkNeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 4), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaLinkNeRxState.setStatus('current')
hwImaLinkFeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 5), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaLinkFeTxState.setStatus('current')
hwImaLinkFeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 6), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwImaLinkFeRxState.setStatus('current')
hwImaLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwImaLinkRowStatus.setStatus('current')
hwImaMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1))
hwImaMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 2))
hwImaMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 2, 1)).setObjects(("HUAWEI-IMA-MIB", "hwImaGroupGroup"), ("HUAWEI-IMA-MIB", "hwImaLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwImaMibCompliance = hwImaMibCompliance.setStatus('current')
hwImaGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1, 1)).setObjects(("HUAWEI-IMA-MIB", "hwImaGroupIfIndex"), ("HUAWEI-IMA-MIB", "hwImaGroupNeState"), ("HUAWEI-IMA-MIB", "hwImaGroupFeState"), ("HUAWEI-IMA-MIB", "hwImaGroupSymmetry"), ("HUAWEI-IMA-MIB", "hwImaGroupMinNumTxLinks"), ("HUAWEI-IMA-MIB", "hwImaGroupMinNumRxLinks"), ("HUAWEI-IMA-MIB", "hwImaGroupTxTimingRefLink"), ("HUAWEI-IMA-MIB", "hwImaGroupRxTimingRefLink"), ("HUAWEI-IMA-MIB", "hwImaGroupTxImaId"), ("HUAWEI-IMA-MIB", "hwImaGroupRxImaId"), ("HUAWEI-IMA-MIB", "hwImaGroupTxFrameLength"), ("HUAWEI-IMA-MIB", "hwImaGroupRxFrameLength"), ("HUAWEI-IMA-MIB", "hwImaGroupDiffDelayMax"), ("HUAWEI-IMA-MIB", "hwImaGroupAlphaValue"), ("HUAWEI-IMA-MIB", "hwImaGroupBetaValue"), ("HUAWEI-IMA-MIB", "hwImaGroupGammaValue"), ("HUAWEI-IMA-MIB", "hwImaGroupNumTxActLinks"), ("HUAWEI-IMA-MIB", "hwImaGroupNumRxActLinks"), ("HUAWEI-IMA-MIB", "hwImaGroupTxOamLabelValue"), ("HUAWEI-IMA-MIB", "hwImaGroupRxOamLabelValue"), ("HUAWEI-IMA-MIB", "hwImaGroupFirstLinkIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwImaGroupGroup = hwImaGroupGroup.setStatus('current')
hwImaLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1, 2)).setObjects(("HUAWEI-IMA-MIB", "hwImaLinkGroupIfIndex"), ("HUAWEI-IMA-MIB", "hwImaLinkNeTxState"), ("HUAWEI-IMA-MIB", "hwImaLinkNeRxState"), ("HUAWEI-IMA-MIB", "hwImaLinkFeTxState"), ("HUAWEI-IMA-MIB", "hwImaLinkFeRxState"), ("HUAWEI-IMA-MIB", "hwImaLinkRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwImaLinkGroup = hwImaLinkGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-IMA-MIB", ImaGroupState=ImaGroupState, hwImaLinkEntry=hwImaLinkEntry, hwImaMIB=hwImaMIB, hwImaLinkIfIndex=hwImaLinkIfIndex, MilliSeconds=MilliSeconds, hwImaLinkGroupIfIndex=hwImaLinkGroupIfIndex, hwImaMibCompliances=hwImaMibCompliances, ImaFrameLength=ImaFrameLength, hwImaGroupAlphaValue=hwImaGroupAlphaValue, hwImaGroupMinNumTxLinks=hwImaGroupMinNumTxLinks, hwImaGroupNumTxActLinks=hwImaGroupNumTxActLinks, ImaGroupSymmetry=ImaGroupSymmetry, hwImaLinkNeRxState=hwImaLinkNeRxState, hwImaGroupTable=hwImaGroupTable, hwImaGroupRxTimingRefLink=hwImaGroupRxTimingRefLink, hwImaGroupFirstLinkIfIndex=hwImaGroupFirstLinkIfIndex, hwImaLinkFeTxState=hwImaLinkFeTxState, hwImaMibConformance=hwImaMibConformance, hwImaGroupDiffDelayMax=hwImaGroupDiffDelayMax, hwImaGroupTxOamLabelValue=hwImaGroupTxOamLabelValue, hwImaLinkTable=hwImaLinkTable, hwImaLinkRowStatus=hwImaLinkRowStatus, hwImaGroupIfIndex=hwImaGroupIfIndex, hwImaGroupNumRxActLinks=hwImaGroupNumRxActLinks, ImaLinkState=ImaLinkState, hwImaMibGroups=hwImaMibGroups, hwImaGroupTxFrameLength=hwImaGroupTxFrameLength, hwImaGroupGammaValue=hwImaGroupGammaValue, hwImaGroupTxImaId=hwImaGroupTxImaId, hwImaGroupRxFrameLength=hwImaGroupRxFrameLength, hwImaGroupMinNumRxLinks=hwImaGroupMinNumRxLinks, hwImaGroupTxTimingRefLink=hwImaGroupTxTimingRefLink, hwImaGroupEntry=hwImaGroupEntry, hwImaGroupGroup=hwImaGroupGroup, hwImaMibObjects=hwImaMibObjects, PYSNMP_MODULE_ID=hwImaMIB, hwImaGroupSymmetry=hwImaGroupSymmetry, hwImaLinkNeTxState=hwImaLinkNeTxState, hwImaGroupRxOamLabelValue=hwImaGroupRxOamLabelValue, hwImaGroupRxImaId=hwImaGroupRxImaId, hwImaMibCompliance=hwImaMibCompliance, hwImaLinkGroup=hwImaLinkGroup, hwImaGroupNeState=hwImaGroupNeState, hwImaGroupFeState=hwImaGroupFeState, hwImaLinkFeRxState=hwImaLinkFeRxState, hwImaGroupBetaValue=hwImaGroupBetaValue)
