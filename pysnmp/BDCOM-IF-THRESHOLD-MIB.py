#
# PySNMP MIB module BDCOM-IF-THRESHOLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BDCOM-IF-THRESHOLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
bdMgmt, = mibBuilder.importSymbols("BDCOM-SMI", "bdMgmt")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Counter64, NotificationType, Gauge32, Bits, TimeTicks, IpAddress, Counter32, MibIdentifier, ObjectIdentity, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "Gauge32", "Bits", "TimeTicks", "IpAddress", "Counter32", "MibIdentifier", "ObjectIdentity", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TimeStamp, DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
bdcomIfThresholdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 9, 218))
bdcomIfThresholdMIB.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: bdcomIfThresholdMIB.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: bdcomIfThresholdMIB.setOrganization('BDCOM, Inc.')
class BdifthTemplateIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1000)

class BdifthTemplateIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class BdifthThresholdIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class BdifthThresholdList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class BdifthThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fail", 1), ("degrade", 2), ("info", 3), ("other", 4))

class BdifthThresholdSeverityOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4)

bdIfThresholdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1))
bdifthTemplateGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1))
bdifthTemplateIfAssignGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2))
bdifthIfThresholdFiredGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3))
bdifthTemplateIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 1), BdifthTemplateIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthTemplateIndexNext.setStatus('current')
bdifthTemplateLastChange = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthTemplateLastChange.setStatus('current')
bdifthTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3), )
if mibBuilder.loadTexts: bdifthTemplateTable.setStatus('current')
bdifthTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1), ).setIndexNames((0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndex"))
if mibBuilder.loadTexts: bdifthTemplateEntry.setStatus('current')
bdifthTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 1), BdifthTemplateIndex())
if mibBuilder.loadTexts: bdifthTemplateIndex.setStatus('current')
bdifthTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthTemplateName.setStatus('current')
bdifthTemplateNotifyHoldDownType = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("holdDownTimer", 2), ("fireAndClearThresholds", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthTemplateNotifyHoldDownType.setStatus('current')
bdifthTemplateNotifyHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthTemplateNotifyHoldDownTime.setStatus('current')
bdifthTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthTemplateRowStatus.setStatus('current')
bdifthThresholdLastChange = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthThresholdLastChange.setStatus('current')
bdifthThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5), )
if mibBuilder.loadTexts: bdifthThresholdTable.setStatus('current')
bdifthThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1), ).setIndexNames((0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndex"), (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdIndex"))
if mibBuilder.loadTexts: bdifthThresholdEntry.setStatus('current')
bdifthThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 1), BdifthThresholdIndex())
if mibBuilder.loadTexts: bdifthThresholdIndex.setStatus('current')
bdifthThresholdDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdDescr.setStatus('current')
bdifthThresholdObject = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdObject.setStatus('current')
bdifthThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 4), BdifthThresholdSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdSeverity.setStatus('current')
bdifthThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("rateOfIncreaseExponentXIfSpeed", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdType.setStatus('current')
bdifthThresholdDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rising", 1), ("falling", 2))).clone('rising')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdDirection.setStatus('current')
bdifthThresholdFiredValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdFiredValue.setStatus('current')
bdifthThresholdClearedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdClearedValue.setStatus('current')
bdifthThresholdSampleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 900000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdSampleInterval.setStatus('current')
bdifthThresholdApsSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdApsSwitchover.setStatus('current')
bdifthThresholdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthThresholdRowStatus.setStatus('current')
bdifthTemplateIfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthTemplateIfLastChange.setStatus('current')
bdifthTemplateIfAssignTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2), )
if mibBuilder.loadTexts: bdifthTemplateIfAssignTable.setStatus('current')
bdifthTemplateIfAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1), ).setIndexNames((0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndex"), (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignInterface"))
if mibBuilder.loadTexts: bdifthTemplateIfAssignEntry.setStatus('current')
bdifthTemplateIfAssignInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bdifthTemplateIfAssignInterface.setStatus('current')
bdifthTemplateIfAssignOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthTemplateIfAssignOperStatus.setStatus('current')
bdifthTemplateIfAssignRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bdifthTemplateIfAssignRowStatus.setStatus('current')
bdifthThresholdFiredNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 1), BdifthThresholdSeverityOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdifthThresholdFiredNotifyEnable.setStatus('current')
bdifthThresholdFiredLastChange = MibScalar((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthThresholdFiredLastChange.setStatus('current')
bdifthIfThresholdFiredTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3), )
if mibBuilder.loadTexts: bdifthIfThresholdFiredTable.setStatus('current')
bdifthIfThresholdFiredEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredTemplate"))
if mibBuilder.loadTexts: bdifthIfThresholdFiredEntry.setStatus('current')
bdifthIfThresholdFiredTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 1), BdifthTemplateIndex())
if mibBuilder.loadTexts: bdifthIfThresholdFiredTemplate.setStatus('current')
bdifthIfThresholdsFired = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 2), BdifthThresholdList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthIfThresholdsFired.setStatus('current')
bdifthIfLastThresholdFired = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 3), BdifthThresholdIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthIfLastThresholdFired.setStatus('current')
bdifthIfThresholdFiredLstChange = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthIfThresholdFiredLstChange.setStatus('current')
bdifthIfThresholdFiredLstSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 5), BdifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthIfThresholdFiredLstSeverity.setStatus('current')
bdifthIfThresholdFiredMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 6), BdifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdifthIfThresholdFiredMaxSeverity.setStatus('current')
bdIfThresholdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 2))
bdifthMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0))
bdifthIfThresholdFired = NotificationType((1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0, 1)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthIfLastThresholdFired"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: bdifthIfThresholdFired.setStatus('current')
bdifthIfThresholdCleared = NotificationType((1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0, 2)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthIfLastThresholdFired"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: bdifthIfThresholdCleared.setStatus('current')
bdifthTemplateIfStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0, 3)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignOperStatus"))
if mibBuilder.loadTexts: bdifthTemplateIfStatusChange.setStatus('current')
bdIfThresholdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3))
bdIfThresholdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 1))
bdIfThresholdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2))
bdIfThresholdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 1, 1)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdIfThresholdTemplateGroup"), ("BDCOM-IF-THRESHOLD-MIB", "bdIfThresholdFiredGroup"), ("BDCOM-IF-THRESHOLD-MIB", "bdIfThresholdNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdIfThresholdMIBCompliance = bdIfThresholdMIBCompliance.setStatus('current')
bdIfThresholdTemplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 1)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndexNext"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateLastChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateName"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateNotifyHoldDownType"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateRowStatus"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdLastChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdDescr"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdObject"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdSeverity"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdType"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdDirection"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdFiredValue"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdSampleInterval"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdRowStatus"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfLastChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignOperStatus"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdIfThresholdTemplateGroup = bdIfThresholdTemplateGroup.setStatus('current')
bdIfThresholdFiredGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 2)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdFiredNotifyEnable"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdFiredLastChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdsFired"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfLastThresholdFired"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstChange"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstSeverity"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredMaxSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdIfThresholdFiredGroup = bdIfThresholdFiredGroup.setStatus('current')
bdifthHoldDownTimerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 3)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateNotifyHoldDownTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdifthHoldDownTimerGroup = bdifthHoldDownTimerGroup.setStatus('current')
bdifthHoldDownHysteresisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 4)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdClearedValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdifthHoldDownHysteresisGroup = bdifthHoldDownHysteresisGroup.setStatus('current')
bdifthApsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 5)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdApsSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdifthApsGroup = bdifthApsGroup.setStatus('current')
bdIfThresholdNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 6)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFired"), ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdIfThresholdNotifsGroup = bdIfThresholdNotifsGroup.setStatus('current')
bdifthTemplateIfNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 7)).setObjects(("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdifthTemplateIfNotifsGroup = bdifthTemplateIfNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("BDCOM-IF-THRESHOLD-MIB", bdIfThresholdMIBGroups=bdIfThresholdMIBGroups, bdifthIfThresholdFiredGroup=bdifthIfThresholdFiredGroup, bdifthHoldDownHysteresisGroup=bdifthHoldDownHysteresisGroup, bdifthThresholdType=bdifthThresholdType, BdifthThresholdSeverity=BdifthThresholdSeverity, bdifthThresholdObject=bdifthThresholdObject, PYSNMP_MODULE_ID=bdcomIfThresholdMIB, bdifthThresholdSampleInterval=bdifthThresholdSampleInterval, bdifthThresholdRowStatus=bdifthThresholdRowStatus, bdifthTemplateIndex=bdifthTemplateIndex, bdifthIfThresholdFiredMaxSeverity=bdifthIfThresholdFiredMaxSeverity, bdIfThresholdMIBConformance=bdIfThresholdMIBConformance, BdifthTemplateIndex=BdifthTemplateIndex, bdifthTemplateLastChange=bdifthTemplateLastChange, bdifthIfThresholdFiredEntry=bdifthIfThresholdFiredEntry, bdifthTemplateIndexNext=bdifthTemplateIndexNext, bdifthThresholdTable=bdifthThresholdTable, bdIfThresholdMIBNotifications=bdIfThresholdMIBNotifications, bdifthTemplateIfLastChange=bdifthTemplateIfLastChange, bdifthIfThresholdFired=bdifthIfThresholdFired, bdifthThresholdEntry=bdifthThresholdEntry, bdifthIfThresholdFiredLstSeverity=bdifthIfThresholdFiredLstSeverity, bdifthApsGroup=bdifthApsGroup, bdIfThresholdTemplateGroup=bdIfThresholdTemplateGroup, BdifthThresholdSeverityOrZero=BdifthThresholdSeverityOrZero, bdifthTemplateIfAssignRowStatus=bdifthTemplateIfAssignRowStatus, bdifthHoldDownTimerGroup=bdifthHoldDownTimerGroup, bdIfThresholdNotifsGroup=bdIfThresholdNotifsGroup, bdifthThresholdDescr=bdifthThresholdDescr, bdifthTemplateIfAssignInterface=bdifthTemplateIfAssignInterface, bdifthTemplateRowStatus=bdifthTemplateRowStatus, bdifthIfThresholdFiredTemplate=bdifthIfThresholdFiredTemplate, BdifthThresholdIndex=BdifthThresholdIndex, bdifthThresholdSeverity=bdifthThresholdSeverity, bdifthTemplateNotifyHoldDownType=bdifthTemplateNotifyHoldDownType, bdifthMIBNotificationsPrefix=bdifthMIBNotificationsPrefix, bdifthTemplateIfAssignGroup=bdifthTemplateIfAssignGroup, bdifthThresholdFiredValue=bdifthThresholdFiredValue, bdifthTemplateName=bdifthTemplateName, BdifthThresholdList=BdifthThresholdList, bdifthIfLastThresholdFired=bdifthIfLastThresholdFired, bdifthTemplateIfAssignTable=bdifthTemplateIfAssignTable, bdifthTemplateIfNotifsGroup=bdifthTemplateIfNotifsGroup, bdifthTemplateTable=bdifthTemplateTable, bdifthThresholdClearedValue=bdifthThresholdClearedValue, bdifthTemplateIfStatusChange=bdifthTemplateIfStatusChange, bdifthThresholdFiredLastChange=bdifthThresholdFiredLastChange, bdifthIfThresholdCleared=bdifthIfThresholdCleared, bdifthThresholdDirection=bdifthThresholdDirection, bdifthTemplateIfAssignOperStatus=bdifthTemplateIfAssignOperStatus, bdifthThresholdFiredNotifyEnable=bdifthThresholdFiredNotifyEnable, bdifthIfThresholdsFired=bdifthIfThresholdsFired, bdIfThresholdMIBCompliance=bdIfThresholdMIBCompliance, bdcomIfThresholdMIB=bdcomIfThresholdMIB, bdIfThresholdMIBObjects=bdIfThresholdMIBObjects, bdIfThresholdMIBCompliances=bdIfThresholdMIBCompliances, bdifthTemplateEntry=bdifthTemplateEntry, bdifthTemplateIfAssignEntry=bdifthTemplateIfAssignEntry, bdIfThresholdFiredGroup=bdIfThresholdFiredGroup, bdifthIfThresholdFiredLstChange=bdifthIfThresholdFiredLstChange, bdifthThresholdLastChange=bdifthThresholdLastChange, bdifthThresholdApsSwitchover=bdifthThresholdApsSwitchover, bdifthThresholdIndex=bdifthThresholdIndex, bdifthTemplateGroup=bdifthTemplateGroup, bdifthTemplateNotifyHoldDownTime=bdifthTemplateNotifyHoldDownTime, bdifthIfThresholdFiredTable=bdifthIfThresholdFiredTable, BdifthTemplateIndexOrZero=BdifthTemplateIndexOrZero)
