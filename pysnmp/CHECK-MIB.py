#
# PySNMP MIB module CHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHECK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Bits, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, ObjectIdentity, mib_2, zeroDotZero, Gauge32, Integer32, Counter64, Counter32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "ObjectIdentity", "mib-2", "zeroDotZero", "Gauge32", "Integer32", "Counter64", "Counter32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, StorageType, TimeStamp, DisplayString, RowStatus, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "TimeStamp", "DisplayString", "RowStatus", "TimeInterval")
checkMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 7777))
checkMIB.setRevisions(('2003-12-19 13:13',))
if mibBuilder.loadTexts: checkMIB.setLastUpdated('200312191313Z')
if mibBuilder.loadTexts: checkMIB.setOrganization('IETF Distributed Management man Working Group')
class RuleValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'

class SeverityConfigured(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967293)

class SeverityReturned(TextualConvention, Unsigned32):
    status = 'current'

checkObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 1))
checkNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 2))
checkConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 3))
checkCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 1, 1))
checkCapabMinCheckInterval = MibScalar((1, 3, 6, 1, 2, 1, 7777, 1, 1, 1), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: checkCapabMinCheckInterval.setStatus('current')
checkCapabMaxResults = MibScalar((1, 3, 6, 1, 2, 1, 7777, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkCapabMaxResults.setStatus('current')
checkCapabMaxRules = MibScalar((1, 3, 6, 1, 2, 1, 7777, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkCapabMaxRules.setStatus('current')
checkControl = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 1, 2))
checkCtrlAdminStatus = MibScalar((1, 3, 6, 1, 2, 1, 7777, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("silent", 2), ("down", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: checkCtrlAdminStatus.setStatus('current')
checkCtrlOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 7777, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("silent", 2), ("down", 3), ("flushing", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkCtrlOperStatus.setStatus('current')
checkResultTable = MibTable((1, 3, 6, 1, 2, 1, 7777, 1, 3), )
if mibBuilder.loadTexts: checkResultTable.setStatus('current')
checkResultEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1), ).setIndexNames((0, "CHECK-MIB", "checkResultName"))
if mibBuilder.loadTexts: checkResultEntry.setStatus('current')
checkResultName = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: checkResultName.setStatus('current')
checkResultSeverity = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 2), SeverityReturned()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkResultSeverity.setStatus('current')
checkResultSize = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkResultSize.setStatus('current')
checkResultTime = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkResultTime.setStatus('current')
checkResultInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 5), TimeInterval()).setUnits('centi-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkResultInterval.setStatus('current')
checkResultSeverityThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 6), SeverityConfigured()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkResultSeverityThreshold.setStatus('current')
checkResultStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 7), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkResultStorageType.setStatus('current')
checkResultRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkResultRowStatus.setStatus('current')
checkRuleTable = MibTable((1, 3, 6, 1, 2, 1, 7777, 1, 4), )
if mibBuilder.loadTexts: checkRuleTable.setStatus('current')
checkRuleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1), ).setIndexNames((0, "CHECK-MIB", "checkResultName"), (0, "CHECK-MIB", "checkRuleName"))
if mibBuilder.loadTexts: checkRuleEntry.setStatus('current')
checkRuleName = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: checkRuleName.setStatus('current')
checkRuleOid = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 3), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkRuleOid.setStatus('current')
checkRuleValue = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 4), RuleValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkRuleValue.setStatus('current')
checkRuleOperation = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noOperation", 0), ("unequal", 1), ("equal", 2), ("less", 3), ("lessOrEqual", 4), ("greater", 5), ("greaterOrEqual", 6), ("delta", 7))).clone('noOperation')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: checkRuleOperation.setStatus('current')
checkRuleSeverity = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 6), SeverityConfigured().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkRuleSeverity.setStatus('current')
checkRuleRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: checkRuleRowStatus.setStatus('current')
checkFailureTable = MibTable((1, 3, 6, 1, 2, 1, 7777, 1, 5), )
if mibBuilder.loadTexts: checkFailureTable.setStatus('current')
checkFailureEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7777, 1, 5, 1), ).setIndexNames((0, "CHECK-MIB", "checkResultName"), (0, "CHECK-MIB", "checkFailureSeverity"), (0, "CHECK-MIB", "checkRuleName"))
if mibBuilder.loadTexts: checkFailureEntry.setStatus('current')
checkFailureSeverity = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 5, 1, 1), SeverityReturned())
if mibBuilder.loadTexts: checkFailureSeverity.setStatus('current')
checkFailureOid = MibTableColumn((1, 3, 6, 1, 2, 1, 7777, 1, 5, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checkFailureOid.setStatus('current')
checkEvent = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 2, 0))
checkFailed = NotificationType((1, 3, 6, 1, 2, 1, 7777, 2, 0, 1)).setObjects(("CHECK-MIB", "checkResultSeverity"))
if mibBuilder.loadTexts: checkFailed.setStatus('current')
checkCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 3, 1))
checkGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 7777, 3, 2))
checkCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 7777, 3, 1, 1)).setObjects(("CHECK-MIB", "checkCapabilitiesGroup"), ("CHECK-MIB", "checkControlGroup"), ("CHECK-MIB", "checkResultGroup"), ("CHECK-MIB", "checkRuleGroup"), ("CHECK-MIB", "checkFailureGroup"), ("CHECK-MIB", "checkNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkCompliance = checkCompliance.setStatus('current')
checkCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 7777, 3, 2, 1)).setObjects(("CHECK-MIB", "checkCapabMinCheckInterval"), ("CHECK-MIB", "checkCapabMaxResults"), ("CHECK-MIB", "checkCapabMaxRules"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkCapabilitiesGroup = checkCapabilitiesGroup.setStatus('current')
checkControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 7777, 3, 2, 2)).setObjects(("CHECK-MIB", "checkCtrlAdminStatus"), ("CHECK-MIB", "checkCtrlOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkControlGroup = checkControlGroup.setStatus('current')
checkResultGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 7777, 3, 2, 3)).setObjects(("CHECK-MIB", "checkResultSeverity"), ("CHECK-MIB", "checkResultSize"), ("CHECK-MIB", "checkResultTime"), ("CHECK-MIB", "checkResultInterval"), ("CHECK-MIB", "checkResultSeverityThreshold"), ("CHECK-MIB", "checkResultStorageType"), ("CHECK-MIB", "checkResultRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkResultGroup = checkResultGroup.setStatus('current')
checkRuleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 7777, 3, 2, 4)).setObjects(("CHECK-MIB", "checkRuleOid"), ("CHECK-MIB", "checkRuleValue"), ("CHECK-MIB", "checkRuleOperation"), ("CHECK-MIB", "checkRuleSeverity"), ("CHECK-MIB", "checkRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkRuleGroup = checkRuleGroup.setStatus('current')
checkFailureGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 7777, 3, 2, 5)).setObjects(("CHECK-MIB", "checkFailureOid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkFailureGroup = checkFailureGroup.setStatus('current')
checkNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 7777, 3, 2, 6)).setObjects(("CHECK-MIB", "checkFailed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    checkNotificationsGroup = checkNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CHECK-MIB", checkResultName=checkResultName, checkEvent=checkEvent, checkRuleGroup=checkRuleGroup, checkRuleRowStatus=checkRuleRowStatus, checkCapabMaxResults=checkCapabMaxResults, PYSNMP_MODULE_ID=checkMIB, checkCapabMaxRules=checkCapabMaxRules, checkFailureSeverity=checkFailureSeverity, checkFailureEntry=checkFailureEntry, checkResultTime=checkResultTime, SeverityConfigured=SeverityConfigured, checkCtrlAdminStatus=checkCtrlAdminStatus, checkCapabMinCheckInterval=checkCapabMinCheckInterval, checkRuleOid=checkRuleOid, checkNotifications=checkNotifications, checkResultSeverity=checkResultSeverity, checkRuleValue=checkRuleValue, checkGroups=checkGroups, checkCapabilitiesGroup=checkCapabilitiesGroup, checkFailureGroup=checkFailureGroup, SeverityReturned=SeverityReturned, checkFailed=checkFailed, checkResultSeverityThreshold=checkResultSeverityThreshold, checkCompliances=checkCompliances, checkRuleTable=checkRuleTable, checkCtrlOperStatus=checkCtrlOperStatus, checkRuleEntry=checkRuleEntry, checkNotificationsGroup=checkNotificationsGroup, checkMIB=checkMIB, checkResultInterval=checkResultInterval, checkCompliance=checkCompliance, checkFailureTable=checkFailureTable, checkResultEntry=checkResultEntry, checkCapabilities=checkCapabilities, checkResultRowStatus=checkResultRowStatus, checkResultTable=checkResultTable, checkObjects=checkObjects, checkControlGroup=checkControlGroup, checkConformance=checkConformance, checkFailureOid=checkFailureOid, RuleValue=RuleValue, checkRuleOperation=checkRuleOperation, checkResultSize=checkResultSize, checkControl=checkControl, checkResultStorageType=checkResultStorageType, checkResultGroup=checkResultGroup, checkRuleSeverity=checkRuleSeverity, checkRuleName=checkRuleName)
