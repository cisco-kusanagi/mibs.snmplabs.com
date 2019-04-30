#
# PySNMP MIB module F10-ISIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/F10-ISIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:57:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, IpAddress, TimeTicks, ModuleIdentity, MibIdentifier, Gauge32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Bits, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Gauge32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Bits", "Counter32", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
f10IsisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 18))
f10IsisMib.setRevisions(('2011-07-01 00:00',))
if mibBuilder.loadTexts: f10IsisMib.setLastUpdated('201107010000Z')
if mibBuilder.loadTexts: f10IsisMib.setOrganization('Dell Inc')
class F10IsisISLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("area", 1), ("domain", 2))

f10IsisNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 0))
f10IsisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1))
f10IsisConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2))
f10IsisSysOloadSetOverload = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IsisSysOloadSetOverload.setStatus('current')
f10IsisSysOloadSetOloadOnStartupUntil = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IsisSysOloadSetOloadOnStartupUntil.setStatus('current')
f10IsisSysOloadWaitForBgp = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IsisSysOloadWaitForBgp.setStatus('current')
f10IsisSysOloadV6SetOverload = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IsisSysOloadV6SetOverload.setStatus('current')
f10IsisSysOloadV6SetOloadOnStartupUntil = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IsisSysOloadV6SetOloadOnStartupUntil.setStatus('current')
f10IsisSysOloadV6WaitForBgp = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 86400)).clone(600)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IsisSysOloadV6WaitForBgp.setStatus('current')
f10IsisSysLevelTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7), )
if mibBuilder.loadTexts: f10IsisSysLevelTable.setStatus('current')
f10IsisSysLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1), ).setIndexNames((0, "F10-ISIS-MIB", "f10IsisSysLevelIndex"))
if mibBuilder.loadTexts: f10IsisSysLevelEntry.setStatus('current')
f10IsisSysLevelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 1), F10IsisISLevel())
if mibBuilder.loadTexts: f10IsisSysLevelIndex.setStatus('current')
f10IsisSysLevelOverloadState = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IsisSysLevelOverloadState.setStatus('current')
f10IsisSysLevelV6OverloadState = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 18, 1, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IsisSysLevelV6OverloadState.setStatus('current')
f10IsisAdjChanges = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 18, 0, 1))
if mibBuilder.loadTexts: f10IsisAdjChanges.setStatus('current')
f10IsisGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1))
f10IsisCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2))
f10IsisCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 2, 1)).setObjects(("F10-ISIS-MIB", "f10IsisSystemGroup"), ("F10-ISIS-MIB", "f10IsisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10IsisCompliance = f10IsisCompliance.setStatus('current')
f10IsisSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 1)).setObjects(("F10-ISIS-MIB", "f10IsisSysOloadSetOverload"), ("F10-ISIS-MIB", "f10IsisSysOloadSetOloadOnStartupUntil"), ("F10-ISIS-MIB", "f10IsisSysOloadWaitForBgp"), ("F10-ISIS-MIB", "f10IsisSysOloadV6SetOverload"), ("F10-ISIS-MIB", "f10IsisSysOloadV6SetOloadOnStartupUntil"), ("F10-ISIS-MIB", "f10IsisSysLevelOverloadState"), ("F10-ISIS-MIB", "f10IsisSysLevelV6OverloadState"), ("F10-ISIS-MIB", "f10IsisSysOloadV6WaitForBgp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10IsisSystemGroup = f10IsisSystemGroup.setStatus('current')
f10IsisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 18, 2, 1, 2)).setObjects(("F10-ISIS-MIB", "f10IsisAdjChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10IsisNotificationGroup = f10IsisNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("F10-ISIS-MIB", PYSNMP_MODULE_ID=f10IsisMib, f10IsisNotifications=f10IsisNotifications, f10IsisSysOloadWaitForBgp=f10IsisSysOloadWaitForBgp, f10IsisSysOloadV6SetOverload=f10IsisSysOloadV6SetOverload, f10IsisSysOloadSetOverload=f10IsisSysOloadSetOverload, f10IsisSysLevelTable=f10IsisSysLevelTable, f10IsisSysLevelEntry=f10IsisSysLevelEntry, f10IsisCompliance=f10IsisCompliance, f10IsisNotificationGroup=f10IsisNotificationGroup, f10IsisObjects=f10IsisObjects, f10IsisConformance=f10IsisConformance, f10IsisSysLevelV6OverloadState=f10IsisSysLevelV6OverloadState, f10IsisMib=f10IsisMib, f10IsisAdjChanges=f10IsisAdjChanges, f10IsisGroups=f10IsisGroups, f10IsisSysOloadV6SetOloadOnStartupUntil=f10IsisSysOloadV6SetOloadOnStartupUntil, f10IsisSystemGroup=f10IsisSystemGroup, f10IsisCompliances=f10IsisCompliances, F10IsisISLevel=F10IsisISLevel, f10IsisSysOloadV6WaitForBgp=f10IsisSysOloadV6WaitForBgp, f10IsisSysLevelOverloadState=f10IsisSysLevelOverloadState, f10IsisSysLevelIndex=f10IsisSysLevelIndex, f10IsisSysOloadSetOloadOnStartupUntil=f10IsisSysOloadSetOloadOnStartupUntil)
