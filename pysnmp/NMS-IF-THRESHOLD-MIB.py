#
# PySNMP MIB module NMS-IF-THRESHOLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-IF-THRESHOLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
nmsMgmt, = mibBuilder.importSymbols("NMS-SMI", "nmsMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Unsigned32, TimeTicks, Counter64, Gauge32, NotificationType, Integer32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Unsigned32", "TimeTicks", "Counter64", "Gauge32", "NotificationType", "Integer32", "MibIdentifier", "iso")
TruthValue, RowStatus, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TimeStamp", "TextualConvention")
nmsIfThresholdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218))
nmsIfThresholdMIB.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: nmsIfThresholdMIB.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: nmsIfThresholdMIB.setOrganization('')
class NMSifthTemplateIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1000)

class NMSifthTemplateIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class NMSifthThresholdIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class NMSifthThresholdList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class NMSifthThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fail", 1), ("degrade", 2), ("info", 3), ("other", 4))

class NMSifthThresholdSeverityOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4)

nmsIfThresholdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1))
nmsifthTemplateGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1))
nmsifthTemplateIfAssignGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2))
nmsifthIfThresholdFiredGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3))
nmsifthTemplateIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 1), NMSifthTemplateIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateIndexNext.setStatus('current')
nmsifthTemplateLastChange = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateLastChange.setStatus('current')
nmsifthTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3), )
if mibBuilder.loadTexts: nmsifthTemplateTable.setStatus('current')
nmsifthTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1), ).setIndexNames((0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"))
if mibBuilder.loadTexts: nmsifthTemplateEntry.setStatus('current')
nmsifthTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 1), NMSifthTemplateIndex())
if mibBuilder.loadTexts: nmsifthTemplateIndex.setStatus('current')
nmsifthTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateName.setStatus('current')
nmsifthTemplateNotifyHoldDownType = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("holdDownTimer", 2), ("fireAndClearThresholds", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateNotifyHoldDownType.setStatus('current')
nmsifthTemplateNotifyHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateNotifyHoldDownTime.setStatus('current')
nmsifthTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateRowStatus.setStatus('current')
nmsifthThresholdLastChange = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthThresholdLastChange.setStatus('current')
nmsifthThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5), )
if mibBuilder.loadTexts: nmsifthThresholdTable.setStatus('current')
nmsifthThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1), ).setIndexNames((0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"), (0, "NMS-IF-THRESHOLD-MIB", "nmsifthThresholdIndex"))
if mibBuilder.loadTexts: nmsifthThresholdEntry.setStatus('current')
nmsifthThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 1), NMSifthThresholdIndex())
if mibBuilder.loadTexts: nmsifthThresholdIndex.setStatus('current')
nmsifthThresholdDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdDescr.setStatus('current')
nmsifthThresholdObject = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdObject.setStatus('current')
nmsifthThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 4), NMSifthThresholdSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdSeverity.setStatus('current')
nmsifthThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("rateOfIncreaseExponentXIfSpeed", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdType.setStatus('current')
nmsifthThresholdDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rising", 1), ("falling", 2))).clone('rising')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdDirection.setStatus('current')
nmsifthThresholdFiredValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdFiredValue.setStatus('current')
nmsifthThresholdClearedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdClearedValue.setStatus('current')
nmsifthThresholdSampleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 900000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdSampleInterval.setStatus('current')
nmsifthThresholdApsSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdApsSwitchover.setStatus('current')
nmsifthThresholdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthThresholdRowStatus.setStatus('current')
nmsifthTemplateIfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateIfLastChange.setStatus('current')
nmsifthTemplateIfAssignTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2), )
if mibBuilder.loadTexts: nmsifthTemplateIfAssignTable.setStatus('current')
nmsifthTemplateIfAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1), ).setIndexNames((0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"), (0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignInterface"))
if mibBuilder.loadTexts: nmsifthTemplateIfAssignEntry.setStatus('current')
nmsifthTemplateIfAssignInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nmsifthTemplateIfAssignInterface.setStatus('current')
nmsifthTemplateIfAssignOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthTemplateIfAssignOperStatus.setStatus('current')
nmsifthTemplateIfAssignRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsifthTemplateIfAssignRowStatus.setStatus('current')
nmsifthThresholdFiredNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 1), NMSifthThresholdSeverityOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsifthThresholdFiredNotifyEnable.setStatus('current')
nmsifthThresholdFiredLastChange = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthThresholdFiredLastChange.setStatus('current')
nmsifthIfThresholdFiredTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3), )
if mibBuilder.loadTexts: nmsifthIfThresholdFiredTable.setStatus('current')
nmsifthIfThresholdFiredEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredTemplate"))
if mibBuilder.loadTexts: nmsifthIfThresholdFiredEntry.setStatus('current')
nmsifthIfThresholdFiredTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 1), NMSifthTemplateIndex())
if mibBuilder.loadTexts: nmsifthIfThresholdFiredTemplate.setStatus('current')
nmsifthIfThresholdsFired = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 2), NMSifthThresholdList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdsFired.setStatus('current')
nmsifthIfLastThresholdFired = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 3), NMSifthThresholdIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfLastThresholdFired.setStatus('current')
nmsifthIfThresholdFiredLstChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdFiredLstChange.setStatus('current')
nmsifthIfThresholdFiredLstSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 5), NMSifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdFiredLstSeverity.setStatus('current')
nmsifthIfThresholdFiredMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 6), NMSifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsifthIfThresholdFiredMaxSeverity.setStatus('current')
nmsIfThresholdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2))
nmsifthMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0))
nmsifthIfThresholdFired = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0, 1)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: nmsifthIfThresholdFired.setStatus('current')
nmsifthIfThresholdCleared = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0, 2)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: nmsifthIfThresholdCleared.setStatus('current')
nmsifthTemplateIfStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0, 3)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignOperStatus"))
if mibBuilder.loadTexts: nmsifthTemplateIfStatusChange.setStatus('current')
nmsIfThresholdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3))
nmsIfThresholdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 1))
nmsIfThresholdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2))
nmsIfThresholdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 1, 1)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsIfThresholdTemplateGroup"), ("NMS-IF-THRESHOLD-MIB", "nmsIfThresholdFiredGroup"), ("NMS-IF-THRESHOLD-MIB", "nmsIfThresholdNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdMIBCompliance = nmsIfThresholdMIBCompliance.setStatus('current')
nmsIfThresholdTemplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 1)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndexNext"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateLastChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateName"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateNotifyHoldDownType"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateRowStatus"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdLastChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdDescr"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdObject"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdSeverity"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdType"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdDirection"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredValue"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdSampleInterval"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdRowStatus"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfLastChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignOperStatus"), ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdTemplateGroup = nmsIfThresholdTemplateGroup.setStatus('current')
nmsIfThresholdFiredGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 2)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredNotifyEnable"), ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredLastChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdsFired"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredMaxSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdFiredGroup = nmsIfThresholdFiredGroup.setStatus('current')
nmsifthHoldDownTimerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 3)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateNotifyHoldDownTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthHoldDownTimerGroup = nmsifthHoldDownTimerGroup.setStatus('current')
nmsifthHoldDownHysteresisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 4)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdClearedValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthHoldDownHysteresisGroup = nmsifthHoldDownHysteresisGroup.setStatus('current')
nmsifthApsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 5)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdApsSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthApsGroup = nmsifthApsGroup.setStatus('current')
nmsIfThresholdNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 6)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFired"), ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsIfThresholdNotifsGroup = nmsIfThresholdNotifsGroup.setStatus('current')
nmsifthTemplateIfNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 7)).setObjects(("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nmsifthTemplateIfNotifsGroup = nmsifthTemplateIfNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("NMS-IF-THRESHOLD-MIB", NMSifthTemplateIndexOrZero=NMSifthTemplateIndexOrZero, nmsifthTemplateNotifyHoldDownTime=nmsifthTemplateNotifyHoldDownTime, nmsifthTemplateIfAssignRowStatus=nmsifthTemplateIfAssignRowStatus, nmsifthThresholdObject=nmsifthThresholdObject, nmsifthTemplateEntry=nmsifthTemplateEntry, nmsifthThresholdType=nmsifthThresholdType, nmsifthThresholdRowStatus=nmsifthThresholdRowStatus, nmsifthTemplateIfAssignTable=nmsifthTemplateIfAssignTable, nmsifthTemplateIndex=nmsifthTemplateIndex, NMSifthThresholdSeverity=NMSifthThresholdSeverity, nmsifthThresholdSampleInterval=nmsifthThresholdSampleInterval, nmsIfThresholdMIBGroups=nmsIfThresholdMIBGroups, nmsifthThresholdEntry=nmsifthThresholdEntry, nmsifthThresholdApsSwitchover=nmsifthThresholdApsSwitchover, nmsifthThresholdSeverity=nmsifthThresholdSeverity, nmsifthTemplateIfAssignInterface=nmsifthTemplateIfAssignInterface, nmsifthIfThresholdFiredMaxSeverity=nmsifthIfThresholdFiredMaxSeverity, nmsIfThresholdFiredGroup=nmsIfThresholdFiredGroup, nmsifthTemplateIfNotifsGroup=nmsifthTemplateIfNotifsGroup, nmsifthTemplateName=nmsifthTemplateName, nmsIfThresholdTemplateGroup=nmsIfThresholdTemplateGroup, nmsifthTemplateIfAssignOperStatus=nmsifthTemplateIfAssignOperStatus, nmsifthIfThresholdFiredEntry=nmsifthIfThresholdFiredEntry, NMSifthThresholdList=NMSifthThresholdList, nmsifthTemplateLastChange=nmsifthTemplateLastChange, nmsifthTemplateIfAssignEntry=nmsifthTemplateIfAssignEntry, nmsIfThresholdMIBNotifications=nmsIfThresholdMIBNotifications, nmsifthIfThresholdCleared=nmsifthIfThresholdCleared, nmsifthApsGroup=nmsifthApsGroup, nmsifthThresholdIndex=nmsifthThresholdIndex, nmsIfThresholdMIBConformance=nmsIfThresholdMIBConformance, nmsifthMIBNotificationsPrefix=nmsifthMIBNotificationsPrefix, nmsifthTemplateGroup=nmsifthTemplateGroup, nmsifthIfThresholdFiredLstChange=nmsifthIfThresholdFiredLstChange, NMSifthTemplateIndex=NMSifthTemplateIndex, nmsifthIfThresholdFiredLstSeverity=nmsifthIfThresholdFiredLstSeverity, nmsifthTemplateIfLastChange=nmsifthTemplateIfLastChange, nmsifthThresholdFiredLastChange=nmsifthThresholdFiredLastChange, nmsifthHoldDownHysteresisGroup=nmsifthHoldDownHysteresisGroup, nmsifthTemplateNotifyHoldDownType=nmsifthTemplateNotifyHoldDownType, nmsifthIfThresholdFiredGroup=nmsifthIfThresholdFiredGroup, nmsifthThresholdFiredNotifyEnable=nmsifthThresholdFiredNotifyEnable, NMSifthThresholdSeverityOrZero=NMSifthThresholdSeverityOrZero, nmsifthThresholdClearedValue=nmsifthThresholdClearedValue, nmsifthHoldDownTimerGroup=nmsifthHoldDownTimerGroup, nmsIfThresholdMIB=nmsIfThresholdMIB, nmsIfThresholdMIBObjects=nmsIfThresholdMIBObjects, nmsifthTemplateRowStatus=nmsifthTemplateRowStatus, nmsifthThresholdLastChange=nmsifthThresholdLastChange, nmsifthThresholdDescr=nmsifthThresholdDescr, nmsifthIfThresholdFiredTemplate=nmsifthIfThresholdFiredTemplate, nmsifthIfThresholdFiredTable=nmsifthIfThresholdFiredTable, PYSNMP_MODULE_ID=nmsIfThresholdMIB, nmsIfThresholdNotifsGroup=nmsIfThresholdNotifsGroup, nmsifthThresholdFiredValue=nmsifthThresholdFiredValue, nmsifthTemplateTable=nmsifthTemplateTable, nmsifthIfThresholdsFired=nmsifthIfThresholdsFired, nmsifthTemplateIfStatusChange=nmsifthTemplateIfStatusChange, nmsifthIfThresholdFired=nmsifthIfThresholdFired, nmsifthThresholdDirection=nmsifthThresholdDirection, nmsifthTemplateIfAssignGroup=nmsifthTemplateIfAssignGroup, nmsIfThresholdMIBCompliance=nmsIfThresholdMIBCompliance, NMSifthThresholdIndex=NMSifthThresholdIndex, nmsifthThresholdTable=nmsifthThresholdTable, nmsIfThresholdMIBCompliances=nmsIfThresholdMIBCompliances, nmsifthTemplateIndexNext=nmsifthTemplateIndexNext, nmsifthIfLastThresholdFired=nmsifthIfLastThresholdFired)
