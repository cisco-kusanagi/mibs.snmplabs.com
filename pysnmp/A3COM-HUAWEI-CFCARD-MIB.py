#
# PySNMP MIB module A3COM-HUAWEI-CFCARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-CFCARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCfCard, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCfCard")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32, Unsigned32, MibIdentifier, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cCfCardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1))
if mibBuilder.loadTexts: h3cCfCardMIB.setLastUpdated('200412240000Z')
if mibBuilder.loadTexts: h3cCfCardMIB.setOrganization('Huawei-3com Technologies Co., Ltd.')
h3cCfCardMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1))
if mibBuilder.loadTexts: h3cCfCardMIBObjects.setStatus('current')
h3cCfCardScalarObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 1))
if mibBuilder.loadTexts: h3cCfCardScalarObjects.setStatus('current')
h3cCfCardNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardNumber.setStatus('current')
h3cCfCardInfoObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2))
if mibBuilder.loadTexts: h3cCfCardInfoObjects.setStatus('current')
h3cCfCardInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2), )
if mibBuilder.loadTexts: h3cCfCardInfoTable.setStatus('current')
h3CfCardInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardIndex"))
if mibBuilder.loadTexts: h3CfCardInfoEntry.setStatus('current')
h3cCfCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardIndex.setStatus('current')
h3cCfCardIsPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardIsPresent.setStatus('current')
h3cCfCardContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardContainedIn.setStatus('current')
h3cCfCardParentRelPos = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardParentRelPos.setStatus('current')
h3cCfCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardDescription.setStatus('current')
h3cCfCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardSerialNumber.setStatus('current')
h3cCfCardFirewareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardFirewareVersion.setStatus('current')
h3cCfCardModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardModelNumber.setStatus('current')
h3cCfCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 128, 240, 255))).clone(namedValues=NamedValues(("sNoError", 1), ("sFormatError", 2), ("sSectorBufferError", 3), ("sECCError", 4), ("sCMPError", 5), ("sSlaveError", 128), ("sIOError", 240), ("sOther", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardState.setStatus('current')
h3cCfCardSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 10), Unsigned32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardSize.setStatus('current')
h3cCfCardUsedSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 11), Unsigned32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardUsedSize.setStatus('current')
h3cCfCardFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 12), Unsigned32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfCardFreeSize.setStatus('current')
h3cCfCardNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2))
if mibBuilder.loadTexts: h3cCfCardNotifications.setStatus('current')
h3cCfCardNotificationsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2, 0))
if mibBuilder.loadTexts: h3cCfCardNotificationsV2.setStatus('current')
h3cCfCardHotSwapOn = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2, 0, 1)).setObjects(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardContainedIn"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardParentRelPos"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardDescription"))
if mibBuilder.loadTexts: h3cCfCardHotSwapOn.setStatus('current')
h3cCfCardHotSwapOff = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2, 0, 2)).setObjects(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardContainedIn"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardParentRelPos"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardDescription"))
if mibBuilder.loadTexts: h3cCfCardHotSwapOff.setStatus('current')
h3cCfCardMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4))
h3cCfCardMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 1))
currentObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 1, 1)).setObjects(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardNumber"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardIndex"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardIsPresent"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardContainedIn"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardParentRelPos"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardDescription"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardSerialNumber"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardFirewareVersion"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardModelNumber"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardState"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardSize"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardUsedSize"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardFreeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    currentObjectGroup = currentObjectGroup.setStatus('current')
currentNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 1, 2)).setObjects(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardHotSwapOn"), ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardHotSwapOff"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    currentNotificationGroup = currentNotificationGroup.setStatus('current')
h3cCfCardMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 2))
basicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 2, 1)).setObjects(("A3COM-HUAWEI-CFCARD-MIB", "currentObjectGroup"), ("A3COM-HUAWEI-CFCARD-MIB", "currentNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicCompliance = basicCompliance.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-CFCARD-MIB", h3cCfCardNotifications=h3cCfCardNotifications, h3cCfCardNotificationsV2=h3cCfCardNotificationsV2, h3cCfCardModelNumber=h3cCfCardModelNumber, h3cCfCardIsPresent=h3cCfCardIsPresent, h3cCfCardSize=h3cCfCardSize, h3cCfCardFreeSize=h3cCfCardFreeSize, PYSNMP_MODULE_ID=h3cCfCardMIB, h3CfCardInfoEntry=h3CfCardInfoEntry, h3cCfCardInfoObjects=h3cCfCardInfoObjects, h3cCfCardScalarObjects=h3cCfCardScalarObjects, h3cCfCardMIBConformance=h3cCfCardMIBConformance, currentObjectGroup=currentObjectGroup, h3cCfCardNumber=h3cCfCardNumber, h3cCfCardParentRelPos=h3cCfCardParentRelPos, h3cCfCardUsedSize=h3cCfCardUsedSize, currentNotificationGroup=currentNotificationGroup, h3cCfCardState=h3cCfCardState, h3cCfCardDescription=h3cCfCardDescription, h3cCfCardFirewareVersion=h3cCfCardFirewareVersion, h3cCfCardHotSwapOff=h3cCfCardHotSwapOff, h3cCfCardMIBCompliances=h3cCfCardMIBCompliances, h3cCfCardMIBGroups=h3cCfCardMIBGroups, h3cCfCardIndex=h3cCfCardIndex, h3cCfCardMIBObjects=h3cCfCardMIBObjects, h3cCfCardHotSwapOn=h3cCfCardHotSwapOn, h3cCfCardMIB=h3cCfCardMIB, h3cCfCardInfoTable=h3cCfCardInfoTable, h3cCfCardSerialNumber=h3cCfCardSerialNumber, h3cCfCardContainedIn=h3cCfCardContainedIn, basicCompliance=basicCompliance)
