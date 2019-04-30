#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODULE-AUTO-SHUTDOWN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalName, entPhysicalModelName, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalName", "entPhysicalModelName", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, NotificationType, Bits, ObjectIdentity, Counter64, Unsigned32, Counter32, Gauge32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "NotificationType", "Bits", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32", "Gauge32", "ModuleIdentity", "iso")
DisplayString, TruthValue, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "DateAndTime")
ciscoModuleAutoShutdownMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 386))
ciscoModuleAutoShutdownMIB.setRevisions(('2008-03-12 00:00', '2003-12-29 00:00',))
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setLastUpdated('200803120000Z')
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setOrganization('Cisco Systems, Inc.')
cmasMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 0))
cmasMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1))
cmasMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2))
cmasGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1))
cmasNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2))
cmasModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3))
cmasModuleSysActionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4))
class CiscoModuleAutoShutSysAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("reset", 2), ("powerCycle", 3), ("powerDown", 4))

cmasFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasFrequency.setStatus('current')
cmasPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 2), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasPeriod.setStatus('current')
cmasMIBEnableNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasMIBEnableNotification.setStatus('current')
cmasModuleSysActionNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleSysActionNotifEnable.setStatus('current')
cmasModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1), )
if mibBuilder.loadTexts: cmasModuleTable.setStatus('current')
cmasModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cmasModuleEntry.setStatus('current')
cmasModuleEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleEnable.setStatus('current')
cmasModuleNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleNumResets.setStatus('current')
cmasModuleLastResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetReason.setStatus('current')
cmasModuleLastResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetTime.setStatus('current')
cmasModuleSysAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 1), CiscoModuleAutoShutSysAction()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysAction.setStatus('current')
cmasModuleSysActionReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysActionReason.setStatus('current')
cmasModuleAutoShutdown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"))
if mibBuilder.loadTexts: cmasModuleAutoShutdown.setStatus('current')
cmasModuleSysActionNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if mibBuilder.loadTexts: cmasModuleSysActionNotif.setStatus('current')
cmasMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1))
cmasMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2))
cmasMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance = cmasMIBCompliance.setStatus('deprecated')
cmasMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance2 = cmasMIBCompliance2.setStatus('current')
cmasModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasFrequency"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasPeriod"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleGroup = cmasModuleGroup.setStatus('current')
cmasNotificationEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasMIBEnableNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationEnableGroup = cmasNotificationEnableGroup.setStatus('current')
cmasNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 3)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleAutoShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup = cmasNotificationsGroup.setStatus('current')
cmasModuleSysActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 4)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotifEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleSysActionGroup = cmasModuleSysActionGroup.setStatus('current')
cmasNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 5)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup2 = cmasNotificationsGroup2.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-MIB", cmasModuleTable=cmasModuleTable, cmasModuleNumResets=cmasModuleNumResets, cmasMIBObjects=cmasMIBObjects, cmasMIBCompliance=cmasMIBCompliance, cmasModuleSysActionNotifEnable=cmasModuleSysActionNotifEnable, ciscoModuleAutoShutdownMIB=ciscoModuleAutoShutdownMIB, cmasModuleSysAction=cmasModuleSysAction, cmasModule=cmasModule, CiscoModuleAutoShutSysAction=CiscoModuleAutoShutSysAction, cmasModuleSysActionNotif=cmasModuleSysActionNotif, cmasMIBNotifs=cmasMIBNotifs, cmasMIBGroups=cmasMIBGroups, cmasFrequency=cmasFrequency, cmasGlobal=cmasGlobal, cmasModuleSysActionReason=cmasModuleSysActionReason, cmasModuleEnable=cmasModuleEnable, cmasMIBConformance=cmasMIBConformance, cmasMIBCompliances=cmasMIBCompliances, cmasNotifObjects=cmasNotifObjects, cmasModuleGroup=cmasModuleGroup, cmasMIBCompliance2=cmasMIBCompliance2, cmasModuleLastResetReason=cmasModuleLastResetReason, cmasMIBEnableNotification=cmasMIBEnableNotification, cmasModuleSysActionObjects=cmasModuleSysActionObjects, cmasModuleLastResetTime=cmasModuleLastResetTime, cmasNotificationsGroup=cmasNotificationsGroup, cmasNotificationEnableGroup=cmasNotificationEnableGroup, cmasModuleSysActionGroup=cmasModuleSysActionGroup, PYSNMP_MODULE_ID=ciscoModuleAutoShutdownMIB, cmasModuleAutoShutdown=cmasModuleAutoShutdown, cmasNotificationsGroup2=cmasNotificationsGroup2, cmasModuleEntry=cmasModuleEntry, cmasPeriod=cmasPeriod)
