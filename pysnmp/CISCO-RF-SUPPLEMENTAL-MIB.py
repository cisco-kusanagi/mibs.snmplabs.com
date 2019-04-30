#
# PySNMP MIB module CISCO-RF-SUPPLEMENTAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RF-SUPPLEMENTAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ConfigCopyState, = mibBuilder.importSymbols("CISCO-CONFIG-COPY-MIB", "ConfigCopyState")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Counter32, ObjectIdentity, Bits, IpAddress, TimeTicks, Gauge32, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "IpAddress", "TimeTicks", "Gauge32", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "iso")
TextualConvention, TruthValue, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DateAndTime", "DisplayString")
ciscoRfSupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 198))
ciscoRfSupMIB.setRevisions(('2004-05-27 00:00', '2004-03-04 00:00', '2001-03-16 00:00',))
if mibBuilder.loadTexts: ciscoRfSupMIB.setLastUpdated('200405270000Z')
if mibBuilder.loadTexts: ciscoRfSupMIB.setOrganization('Cisco Systems, Inc.')
class RfSupSyncAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enableAutoSync", 1), ("disableAutoSync", 2))

class RfSupSyncOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("inSync", 1), ("lastUpdateFailed", 2), ("commDown", 3), ("syncDisabled", 4), ("noStandbyPresent", 5))

ciscoRfSupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 0))
ciscoRfSupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1))
cRfSupSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1))
cRfSupCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2))
cRfSupAction = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3))
cRfSupSysAvailableStartTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysAvailableStartTime.setStatus('current')
cRfSupSysSwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysSwitchoverTime.setStatus('current')
cRfSupSysSwitchovers = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysSwitchovers.setStatus('current')
cRfSupSysRunningConfigSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysRunningConfigSyncTime.setStatus('current')
cRfSupSysRunningConfigAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 5), RfSupSyncAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysRunningConfigAdmin.setStatus('current')
cRfSupSysRunningConfigOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 6), RfSupSyncOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysRunningConfigOper.setStatus('current')
cRfSupSysStartupConfigSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysStartupConfigSyncTime.setStatus('current')
cRfSupSysStartupConfigAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 8), RfSupSyncAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysStartupConfigAdmin.setStatus('current')
cRfSupSysStartupConfigOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 9), RfSupSyncOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysStartupConfigOper.setStatus('current')
cRfSupSysBootImageSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysBootImageSyncTime.setStatus('current')
cRfSupSysBootImageAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 11), RfSupSyncAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysBootImageAdmin.setStatus('current')
cRfSupSysBootImageOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 12), RfSupSyncOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupSysBootImageOper.setStatus('current')
cRfSupSysStandbyBootFile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysStandbyBootFile.setStatus('current')
cRfSupNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupNotificationsEnabled.setStatus('current')
cRfSupSysIfCounterSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupSysIfCounterSync.setStatus('current')
cRfSupCpuTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1), )
if mibBuilder.loadTexts: cRfSupCpuTable.setStatus('current')
cRfSupCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuUniqueIndex"))
if mibBuilder.loadTexts: cRfSupCpuEntry.setStatus('current')
cRfSupCpuUniqueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 1), PhysicalIndex())
if mibBuilder.loadTexts: cRfSupCpuUniqueIndex.setStatus('current')
cRfSupCpuActiveSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("nonFaulty", 0), ("nonTrafficAffectingFault", 1), ("partialTrafficAffectingFault", 2), ("fullyTrafficAffectingFault", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupCpuActiveSeverity.setStatus('current')
cRfSupCpuInitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupCpuInitTime.setStatus('current')
cRfSupActionManualSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("runningConfig", 2), ("startupConfig", 3), ("bootImage", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cRfSupActionManualSync.setStatus('current')
cRfSupActionLastSyncResult = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3, 2), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cRfSupActionLastSyncResult.setStatus('current')
ciscoRfSupTimeChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 1)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"))
if mibBuilder.loadTexts: ciscoRfSupTimeChangeEvent.setStatus('current')
ciscoRfSupTimeZoneChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 2)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"))
if mibBuilder.loadTexts: ciscoRfSupTimeZoneChangeEvent.setStatus('current')
ciscoRfSupMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 2))
ciscoRfSupMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1))
ciscoRfSupMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2))
ciscoRfSupMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 1)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibCompliance = ciscoRfSupMibCompliance.setStatus('deprecated')
ciscoRfSupMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 2)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibComplianceRev1 = ciscoRfSupMibComplianceRev1.setStatus('deprecated')
ciscoRfSupMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 3)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupNotifGroup"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalSyncGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupMibComplianceRev2 = ciscoRfSupMibComplianceRev2.setStatus('current')
ciscoRfSupSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 1)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchovers"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigAdmin"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigOper"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigAdmin"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigOper"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageSyncTime"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageAdmin"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageOper"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStandbyBootFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupSysGroup = ciscoRfSupSysGroup.setStatus('current')
ciscoRfSupCpuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 2)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuActiveSeverity"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuInitTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupCpuGroup = ciscoRfSupCpuGroup.setStatus('current')
ciscoRfSupActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 3)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionManualSync"), ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionLastSyncResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupActionGroup = ciscoRfSupActionGroup.setStatus('current')
ciscoRfSupSysOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 4)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupNotificationsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupSysOptionalGroup = ciscoRfSupSysOptionalGroup.setStatus('current')
ciscoRfSupNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 5)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeChangeEvent"), ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeZoneChangeEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupNotifGroup = ciscoRfSupNotifGroup.setStatus('current')
ciscoRfSupSysOptionalSyncGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 6)).setObjects(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysIfCounterSync"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRfSupSysOptionalSyncGroup = ciscoRfSupSysOptionalSyncGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-RF-SUPPLEMENTAL-MIB", ciscoRfSupTimeZoneChangeEvent=ciscoRfSupTimeZoneChangeEvent, cRfSupSysStartupConfigAdmin=cRfSupSysStartupConfigAdmin, cRfSupSysRunningConfigSyncTime=cRfSupSysRunningConfigSyncTime, cRfSupCpuActiveSeverity=cRfSupCpuActiveSeverity, ciscoRfSupTimeChangeEvent=ciscoRfSupTimeChangeEvent, cRfSupActionLastSyncResult=cRfSupActionLastSyncResult, ciscoRfSupMIBNotifs=ciscoRfSupMIBNotifs, cRfSupActionManualSync=cRfSupActionManualSync, cRfSupSysStartupConfigOper=cRfSupSysStartupConfigOper, cRfSupSysStandbyBootFile=cRfSupSysStandbyBootFile, cRfSupSysAvailableStartTime=cRfSupSysAvailableStartTime, cRfSupSysSwitchovers=cRfSupSysSwitchovers, cRfSupNotificationsEnabled=cRfSupNotificationsEnabled, RfSupSyncOperState=RfSupSyncOperState, PYSNMP_MODULE_ID=ciscoRfSupMIB, cRfSupSysBootImageAdmin=cRfSupSysBootImageAdmin, ciscoRfSupSysOptionalSyncGroup=ciscoRfSupSysOptionalSyncGroup, ciscoRfSupMibGroups=ciscoRfSupMibGroups, ciscoRfSupCpuGroup=ciscoRfSupCpuGroup, cRfSupSysIfCounterSync=cRfSupSysIfCounterSync, RfSupSyncAdminState=RfSupSyncAdminState, cRfSupCpu=cRfSupCpu, ciscoRfSupMIBObjects=ciscoRfSupMIBObjects, ciscoRfSupMibConformance=ciscoRfSupMibConformance, cRfSupSysStartupConfigSyncTime=cRfSupSysStartupConfigSyncTime, ciscoRfSupMibCompliance=ciscoRfSupMibCompliance, ciscoRfSupActionGroup=ciscoRfSupActionGroup, ciscoRfSupMIB=ciscoRfSupMIB, ciscoRfSupMibCompliances=ciscoRfSupMibCompliances, cRfSupSysRunningConfigAdmin=cRfSupSysRunningConfigAdmin, ciscoRfSupMibComplianceRev2=ciscoRfSupMibComplianceRev2, cRfSupCpuInitTime=cRfSupCpuInitTime, cRfSupCpuUniqueIndex=cRfSupCpuUniqueIndex, ciscoRfSupSysGroup=ciscoRfSupSysGroup, ciscoRfSupSysOptionalGroup=ciscoRfSupSysOptionalGroup, cRfSupSysBootImageOper=cRfSupSysBootImageOper, cRfSupCpuEntry=cRfSupCpuEntry, cRfSupSystem=cRfSupSystem, cRfSupSysSwitchoverTime=cRfSupSysSwitchoverTime, cRfSupSysRunningConfigOper=cRfSupSysRunningConfigOper, cRfSupAction=cRfSupAction, ciscoRfSupNotifGroup=ciscoRfSupNotifGroup, ciscoRfSupMibComplianceRev1=ciscoRfSupMibComplianceRev1, cRfSupSysBootImageSyncTime=cRfSupSysBootImageSyncTime, cRfSupCpuTable=cRfSupCpuTable)
