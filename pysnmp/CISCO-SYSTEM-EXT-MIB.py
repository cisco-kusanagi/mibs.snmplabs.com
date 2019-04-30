#
# PySNMP MIB module CISCO-SYSTEM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSTEM-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, EntPhysicalIndexOrZero = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "EntPhysicalIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
IpAddress, ModuleIdentity, Integer32, iso, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Integer32", "iso", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Counter32", "NotificationType", "TimeTicks")
TextualConvention, DisplayString, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "DateAndTime")
ciscoSystemExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 305))
ciscoSystemExtMIB.setRevisions(('2016-07-19 00:00', '2016-06-07 00:00', '2015-08-19 00:00', '2007-08-06 00:00', '2006-11-29 00:00', '2006-09-25 00:00', '2005-11-09 00:00', '2005-06-14 00:00', '2004-04-19 00:00', '2003-05-02 00:00', '2003-03-02 00:00', '2002-11-19 00:00', '2002-10-04 00:00',))
if mibBuilder.loadTexts: ciscoSystemExtMIB.setLastUpdated('201606140000Z')
if mibBuilder.loadTexts: ciscoSystemExtMIB.setOrganization('Cisco Systems Inc.')
ciscoSystemExtMIBNotifsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 0))
ciscoSystemExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1))
ciscoSystemExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 2))
ciscoSysInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1))
ciscoSysErrorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2))
ciscoHaGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3))
ciscoSwFailureGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4))
ciscoSwFailureNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 5))
ciscoSystemSwitchingModeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6))
ciscoSystemMaintModeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7))
ciscoSystemMaintModeNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8))
ciscoSystemReloadGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 9))
class CseHaRestartReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 1), ("ungracefulExit", 2), ("otherSignal", 3), ("sigterm", 4), ("softwareUpgrade", 5), ("configUpdate", 6), ("configRemove", 7), ("shutdown", 8), ("aborted", 9), ("heartbeatFailure", 10), ("userTerminate", 11), ("gracefulExit", 12), ("noCallHomeFailure", 13), ("serviceTimeout", 14))

class CiscoMaintModeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("maintenance", 2), ("unplannedMaint", 3))

cseSysCPUUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysCPUUtilization.setStatus('current')
cseSysMemoryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysMemoryUtilization.setStatus('current')
cseSysConfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysConfLastChange.setStatus('current')
cseSysAutoSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sync", 1), ("noSync", 2))).clone('noSync')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseSysAutoSync.setStatus('current')
cseSysAutoSyncState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("succeeded", 2), ("failed", 3), ("notStarted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysAutoSyncState.setStatus('current')
cseWriteErase = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("eraseAll", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseWriteErase.setStatus('current')
cseSysConsolePortStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("notConnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysConsolePortStatus.setStatus('current')
cseSysTelnetServiceActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseSysTelnetServiceActivation.setStatus('current')
cseSysFIPSModeActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cseSysFIPSModeActivation.setStatus('current')
cseSysUpTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 10), TimeIntervalSec()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSysUpTime.setStatus('current')
cseSnmpErrorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1), )
if mibBuilder.loadTexts: cseSnmpErrorTable.setStatus('current')
cseSnmpErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorAddressType"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorAddress"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorRequestId"))
if mibBuilder.loadTexts: cseSnmpErrorEntry.setStatus('current')
cseSnmpErrorAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cseSnmpErrorAddressType.setStatus('current')
cseSnmpErrorAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: cseSnmpErrorAddress.setStatus('current')
cseSnmpErrorRequestId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cseSnmpErrorRequestId.setStatus('current')
cseSnmpErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSnmpErrorCode.setStatus('current')
cseSnmpErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSnmpErrorDescription.setStatus('current')
cseHaRestartReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 2), CseHaRestartReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaRestartReason.setStatus('current')
cseHaRestartStateless = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 3), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaRestartStateless.setStatus('current')
cseHaRestartService = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaRestartService.setStatus('current')
cseHaShutDownReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cseHaShutDownReason.setStatus('current')
cseSwCorePath = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCorePath.setStatus('current')
cseSwCoresTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2), )
if mibBuilder.loadTexts: cseSwCoresTable.setStatus('current')
cseSwCoresEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1), ).setIndexNames((0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresModule"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresProcName"), (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresInstance"))
if mibBuilder.loadTexts: cseSwCoresEntry.setStatus('current')
cseSwCoresModule = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 1), EntPhysicalIndexOrZero())
if mibBuilder.loadTexts: cseSwCoresModule.setStatus('current')
cseSwCoresProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cseSwCoresProcName.setStatus('current')
cseSwCoresInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cseSwCoresInstance.setStatus('current')
cseSwCoresPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresPID.setStatus('current')
cseSwCoresTimeCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresTimeCreated.setStatus('current')
cseSwCoresSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresSlotNum.setStatus('current')
cseSwCoresFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSwCoresFileName.setStatus('current')
ciscoSystemSwitchingModeAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("notApplicable", 2), ("nexus3000", 3), ("nexus9000", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSystemSwitchingModeAdmin.setStatus('current')
ciscoSystemSwitchingModeOper = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("notApplicable", 2), ("nexus3000", 3), ("nexus9000", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSystemSwitchingModeOper.setStatus('current')
cseMaintModeState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 1), CiscoMaintModeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseMaintModeState.setStatus('current')
cseSystemReloadPending = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 9, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSystemReloadPending.setStatus('current')
ciscoSwFailureNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSwFailureNotifEnable.setStatus('current')
ciscoSystemNormalModeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSystemNormalModeNotifEnable.setStatus('current')
ciscoSystemMaintModeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoSystemMaintModeNotifEnable.setStatus('current')
cseHaNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5))
cseHaNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0))
cseHaRestartNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartReason"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartService"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartStateless"))
if mibBuilder.loadTexts: cseHaRestartNotify.setStatus('current')
cseShutDownNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaShutDownReason"))
if mibBuilder.loadTexts: cseShutDownNotify.setStatus('current')
cseFailNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3))
cseFailNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0))
cseFailSwCoreNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0, 1))
if mibBuilder.loadTexts: cseFailSwCoreNotify.setStatus('current')
cseFailSwCoreNotifyExtended = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0, 2)).setObjects(("SNMPv2-MIB", "sysName"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresFileName"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCorePath"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresPID"))
if mibBuilder.loadTexts: cseFailSwCoreNotifyExtended.setStatus('current')
cseMaintModeNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2))
cseMaintModeNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0))
cseNormalModeChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"))
if mibBuilder.loadTexts: cseNormalModeChangeNotify.setStatus('current')
cseMaintModeChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"))
if mibBuilder.loadTexts: cseMaintModeChangeNotify.setStatus('current')
ciscoSystemExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1))
ciscoSystemExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2))
ciscoSystemExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBCompliance = ciscoSystemExtMIBCompliance.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev1 = ciscoSystemExtMIBComplianceRev1.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 3)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev2 = ciscoSystemExtMIBComplianceRev2.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 4)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev3 = ciscoSystemExtMIBComplianceRev3.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 5)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev4 = ciscoSystemExtMIBComplianceRev4.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 6)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev5 = ciscoSystemExtMIBComplianceRev5.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 7)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev6 = ciscoSystemExtMIBComplianceRev6.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 8)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev7 = ciscoSystemExtMIBComplianceRev7.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 9)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev8 = ciscoSystemExtMIBComplianceRev8.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 11)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev9 = ciscoSystemExtMIBComplianceRev9.setStatus('deprecated')
ciscoSystemExtMIBComplianceRev10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 12)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev3"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupRev2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtErrorGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtNotificationGroupSup1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtHaGroupRev1"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoGroupOptional"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtSwFailureGroup2"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoTelnetGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemExtInfoFIPSGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeObjectsGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeObjectsGroup"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtMIBComplianceRev10 = ciscoSystemExtMIBComplianceRev10.setStatus('current')
ciscoSystemExtInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 1)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroup = ciscoSystemExtInfoGroup.setStatus('deprecated')
ciscoSystemExtErrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 2)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorCode"), ("CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtErrorGroup = ciscoSystemExtErrorGroup.setStatus('current')
ciscoSystemExtHaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 3)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartReason"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartService"), ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartStateless"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtHaGroup = ciscoSystemExtHaGroup.setStatus('current')
ciscoSystemExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 4)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtNotificationGroup = ciscoSystemExtNotificationGroup.setStatus('current')
ciscoSystemExtInfoGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 5)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSync"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSyncState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupRev1 = ciscoSystemExtInfoGroupRev1.setStatus('deprecated')
ciscoSystemExtInfoGroupOptional = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 6)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseWriteErase"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupOptional = ciscoSystemExtInfoGroupOptional.setStatus('current')
ciscoSystemExtSwFailureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 7)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSwCorePath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureGroup = ciscoSystemExtSwFailureGroup.setStatus('current')
ciscoSystemExtInfoGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 8)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysConsolePortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupRev2 = ciscoSystemExtInfoGroupRev2.setStatus('current')
ciscoSystemExtSwFailureGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 9)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSwCoresPID"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresTimeCreated"), ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresSlotNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureGroup2 = ciscoSystemExtSwFailureGroup2.setStatus('current')
ciscoSystemExtNotificationGroupSup1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 10)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseShutDownNotify"), ("CISCO-SYSTEM-EXT-MIB", "cseFailSwCoreNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtNotificationGroupSup1 = ciscoSystemExtNotificationGroupSup1.setStatus('current')
ciscoSystemExtHaGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 11)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseHaShutDownReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtHaGroupRev1 = ciscoSystemExtHaGroupRev1.setStatus('current')
ciscoSystemExtInfoTelnetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 12)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysTelnetServiceActivation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoTelnetGroup = ciscoSystemExtInfoTelnetGroup.setStatus('current')
ciscoSystemExtNotificationGroupSup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 13)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseFailSwCoreNotifyExtended"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtNotificationGroupSup2 = ciscoSystemExtNotificationGroupSup2.setStatus('current')
ciscoSystemExtSwFailureGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 14)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSwCoresFileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureGroup3 = ciscoSystemExtSwFailureGroup3.setStatus('current')
ciscoSystemExtSwFailureControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 15)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSwFailureNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtSwFailureControlGroup = ciscoSystemExtSwFailureControlGroup.setStatus('current')
ciscoSystemExtInfoFIPSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 16)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysFIPSModeActivation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoFIPSGroup = ciscoSystemExtInfoFIPSGroup.setStatus('current')
ciscoSystemExtInfoGroupRev3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 17)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"), ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSync"), ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSyncState"), ("CISCO-SYSTEM-EXT-MIB", "cseSysUpTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemExtInfoGroupRev3 = ciscoSystemExtInfoGroupRev3.setStatus('current')
ciscoSystemSwitchingModeObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 18)).setObjects(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeAdmin"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemSwitchingModeObjectsGroup = ciscoSystemSwitchingModeObjectsGroup.setStatus('current')
ciscoSystemMaintModeObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 19)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemNormalModeNotifEnable"), ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMaintModeObjectsGroup = ciscoSystemMaintModeObjectsGroup.setStatus('current')
ciscoSystemMaintModeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 20)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseNormalModeChangeNotify"), ("CISCO-SYSTEM-EXT-MIB", "cseMaintModeChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemMaintModeNotificationGroup = ciscoSystemMaintModeNotificationGroup.setStatus('current')
ciscoSystemReloadObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 21)).setObjects(("CISCO-SYSTEM-EXT-MIB", "cseSystemReloadPending"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemReloadObjectsGroup = ciscoSystemReloadObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-MIB", ciscoSystemExtInfoGroupOptional=ciscoSystemExtInfoGroupOptional, cseSysConsolePortStatus=cseSysConsolePortStatus, ciscoSystemExtMIBComplianceRev1=ciscoSystemExtMIBComplianceRev1, ciscoSystemMaintModeObjectsGroup=ciscoSystemMaintModeObjectsGroup, cseSysConfLastChange=cseSysConfLastChange, ciscoSystemExtNotificationGroup=ciscoSystemExtNotificationGroup, ciscoSystemExtSwFailureGroup=ciscoSystemExtSwFailureGroup, CseHaRestartReason=CseHaRestartReason, cseSnmpErrorEntry=cseSnmpErrorEntry, ciscoSystemExtInfoTelnetGroup=ciscoSystemExtInfoTelnetGroup, ciscoSystemExtHaGroupRev1=ciscoSystemExtHaGroupRev1, cseSnmpErrorAddressType=cseSnmpErrorAddressType, ciscoSwFailureNotifEnable=ciscoSwFailureNotifEnable, ciscoSystemExtMIBComplianceRev4=ciscoSystemExtMIBComplianceRev4, ciscoSysErrorGroup=ciscoSysErrorGroup, cseWriteErase=cseWriteErase, ciscoSystemExtHaGroup=ciscoSystemExtHaGroup, ciscoSystemExtMIBComplianceRev7=ciscoSystemExtMIBComplianceRev7, ciscoSystemExtMIBComplianceRev10=ciscoSystemExtMIBComplianceRev10, cseNormalModeChangeNotify=cseNormalModeChangeNotify, ciscoSystemExtInfoFIPSGroup=ciscoSystemExtInfoFIPSGroup, cseMaintModeNotification=cseMaintModeNotification, ciscoSystemExtMIBComplianceRev6=ciscoSystemExtMIBComplianceRev6, cseSysMemoryUtilization=cseSysMemoryUtilization, ciscoSystemExtMIBCompliance=ciscoSystemExtMIBCompliance, cseSystemReloadPending=cseSystemReloadPending, ciscoSystemExtInfoGroupRev2=ciscoSystemExtInfoGroupRev2, cseHaNotification=cseHaNotification, cseFailSwCoreNotifyExtended=cseFailSwCoreNotifyExtended, cseSwCoresTable=cseSwCoresTable, ciscoSystemSwitchingModeOper=ciscoSystemSwitchingModeOper, ciscoSystemExtMIBComplianceRev8=ciscoSystemExtMIBComplianceRev8, cseSnmpErrorAddress=cseSnmpErrorAddress, cseSysAutoSync=cseSysAutoSync, ciscoSystemSwitchingModeAdmin=ciscoSystemSwitchingModeAdmin, ciscoSystemExtMIBComplianceRev2=ciscoSystemExtMIBComplianceRev2, ciscoSystemExtMIBCompliances=ciscoSystemExtMIBCompliances, ciscoSystemExtNotificationGroupSup1=ciscoSystemExtNotificationGroupSup1, ciscoSystemExtNotificationGroupSup2=ciscoSystemExtNotificationGroupSup2, ciscoSystemExtMIBComplianceRev9=ciscoSystemExtMIBComplianceRev9, ciscoSystemExtSwFailureGroup2=ciscoSystemExtSwFailureGroup2, cseSwCoresTimeCreated=cseSwCoresTimeCreated, cseSnmpErrorCode=cseSnmpErrorCode, ciscoSystemExtMIBComplianceRev5=ciscoSystemExtMIBComplianceRev5, cseMaintModeChangeNotify=cseMaintModeChangeNotify, cseHaRestartService=cseHaRestartService, ciscoSystemExtMIBConformance=ciscoSystemExtMIBConformance, ciscoSystemExtInfoGroup=ciscoSystemExtInfoGroup, cseHaNotificationPrefix=cseHaNotificationPrefix, ciscoSystemExtMIB=ciscoSystemExtMIB, ciscoSystemExtSwFailureControlGroup=ciscoSystemExtSwFailureControlGroup, cseFailNotificationPrefix=cseFailNotificationPrefix, cseSwCoresProcName=cseSwCoresProcName, ciscoSystemMaintModeGroup=ciscoSystemMaintModeGroup, cseSwCoresFileName=cseSwCoresFileName, PYSNMP_MODULE_ID=ciscoSystemExtMIB, ciscoSystemExtMIBGroups=ciscoSystemExtMIBGroups, cseHaRestartNotify=cseHaRestartNotify, cseHaRestartReason=cseHaRestartReason, CiscoMaintModeState=CiscoMaintModeState, cseFailSwCoreNotify=cseFailSwCoreNotify, ciscoHaGroup=ciscoHaGroup, ciscoSwFailureNotifControl=ciscoSwFailureNotifControl, cseSwCoresInstance=cseSwCoresInstance, cseSnmpErrorTable=cseSnmpErrorTable, cseSysAutoSyncState=cseSysAutoSyncState, ciscoSystemReloadGroup=ciscoSystemReloadGroup, cseSysUpTime=cseSysUpTime, ciscoSystemExtMIBNotifsPrefix=ciscoSystemExtMIBNotifsPrefix, ciscoSystemReloadObjectsGroup=ciscoSystemReloadObjectsGroup, cseSysFIPSModeActivation=cseSysFIPSModeActivation, ciscoSystemSwitchingModeObjectsGroup=ciscoSystemSwitchingModeObjectsGroup, ciscoSystemExtMIBComplianceRev3=ciscoSystemExtMIBComplianceRev3, ciscoSystemExtSwFailureGroup3=ciscoSystemExtSwFailureGroup3, cseShutDownNotify=cseShutDownNotify, cseSysCPUUtilization=cseSysCPUUtilization, ciscoSwFailureGroup=ciscoSwFailureGroup, cseSwCoresPID=cseSwCoresPID, ciscoSystemSwitchingModeGroup=ciscoSystemSwitchingModeGroup, ciscoSystemMaintModeNotifEnable=ciscoSystemMaintModeNotifEnable, ciscoSysInfoGroup=ciscoSysInfoGroup, cseHaShutDownReason=cseHaShutDownReason, cseHaRestartStateless=cseHaRestartStateless, ciscoSystemExtMIBObjects=ciscoSystemExtMIBObjects, ciscoSystemExtInfoGroupRev1=ciscoSystemExtInfoGroupRev1, cseSwCoresModule=cseSwCoresModule, ciscoSystemNormalModeNotifEnable=ciscoSystemNormalModeNotifEnable, ciscoSystemExtErrorGroup=ciscoSystemExtErrorGroup, cseFailNotification=cseFailNotification, cseSysTelnetServiceActivation=cseSysTelnetServiceActivation, ciscoSystemMaintModeNotificationGroup=ciscoSystemMaintModeNotificationGroup, cseSnmpErrorRequestId=cseSnmpErrorRequestId, ciscoSystemMaintModeNotifControl=ciscoSystemMaintModeNotifControl, cseSnmpErrorDescription=cseSnmpErrorDescription, cseMaintModeNotificationPrefix=cseMaintModeNotificationPrefix, cseSwCoresSlotNum=cseSwCoresSlotNum, cseSwCoresEntry=cseSwCoresEntry, cseMaintModeState=cseMaintModeState, ciscoSystemExtInfoGroupRev3=ciscoSystemExtInfoGroupRev3, cseSwCorePath=cseSwCorePath)
