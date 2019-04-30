#
# PySNMP MIB module CISCO-MEMORY-POOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEMORY-POOL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, IpAddress, iso, Bits, MibIdentifier, Counter32, Integer32, ObjectIdentity, NotificationType, ModuleIdentity, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "iso", "Bits", "MibIdentifier", "Counter32", "Integer32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoMemoryPoolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 48))
ciscoMemoryPoolMIB.setRevisions(('2013-09-18 00:00', '2001-07-31 00:00', '1996-02-01 00:00',))
if mibBuilder.loadTexts: ciscoMemoryPoolMIB.setLastUpdated('201309180000Z')
if mibBuilder.loadTexts: ciscoMemoryPoolMIB.setOrganization('Cisco Systems, Inc.')
class CiscoMemoryPoolTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

ciscoMemoryPoolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 1))
ciscoMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1), )
if mibBuilder.loadTexts: ciscoMemoryPoolTable.setStatus('current')
ciscoMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1), ).setIndexNames((0, "CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolType"))
if mibBuilder.loadTexts: ciscoMemoryPoolEntry.setStatus('current')
ciscoMemoryPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 1), CiscoMemoryPoolTypes())
if mibBuilder.loadTexts: ciscoMemoryPoolType.setStatus('current')
ciscoMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolName.setStatus('current')
ciscoMemoryPoolAlternate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolAlternate.setStatus('current')
ciscoMemoryPoolValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolValid.setStatus('current')
ciscoMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUsed.setStatus('current')
ciscoMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 6), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolFree.setStatus('current')
ciscoMemoryPoolLargestFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 7), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolLargestFree.setStatus('current')
ciscoMemoryPoolLowMemoryNotifThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 8), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryNotifThreshold.setStatus('current')
ciscoMemoryPoolUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2), )
if mibBuilder.loadTexts: ciscoMemoryPoolUtilizationTable.setStatus('current')
ciscoMemoryPoolUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1), )
ciscoMemoryPoolEntry.registerAugmentions(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilizationEntry"))
ciscoMemoryPoolUtilizationEntry.setIndexNames(*ciscoMemoryPoolEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoMemoryPoolUtilizationEntry.setStatus('current')
ciscoMemoryPoolUtilization1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilization1Min.setStatus('current')
ciscoMemoryPoolUtilization5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilization5Min.setStatus('current')
ciscoMemoryPoolUtilization10Min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilization10Min.setStatus('current')
ciscoMemoryPoolLowMemoryNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryNotifEnable.setStatus('current')
ciscoMemoryPoolNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 2))
ciscoMemoryPoolMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0))
ciscoMemoryPoolLowMemoryNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0, 1)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"))
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryNotif.setStatus('current')
ciscoMemoryPoolLowMemoryRecoveryNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0, 2)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"))
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryRecoveryNotif.setStatus('current')
ciscoMemoryPoolConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 3))
ciscoMemoryPoolCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1))
ciscoMemoryPoolGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2))
ciscoMemoryPoolCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 1)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCompliance = ciscoMemoryPoolCompliance.setStatus('deprecated')
ciscoMemoryPoolComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 2)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolGroup"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolComplianceRev1 = ciscoMemoryPoolComplianceRev1.setStatus('deprecated')
ciscoMemoryPoolComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 3)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolGroupRev1"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilizationGroup"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolNotificationGroup"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolNotificationCtrlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolComplianceRev2 = ciscoMemoryPoolComplianceRev2.setStatus('current')
ciscoMemoryPoolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 1)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolAlternate"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolValid"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolFree"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLargestFree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolGroup = ciscoMemoryPoolGroup.setStatus('deprecated')
ciscoMemoryPoolUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 2)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization1Min"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization5Min"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization10Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolUtilizationGroup = ciscoMemoryPoolUtilizationGroup.setStatus('current')
ciscoMemoryPoolNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 3)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotif"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryRecoveryNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolNotificationGroup = ciscoMemoryPoolNotificationGroup.setStatus('current')
ciscoMemoryPoolNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 4)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolNotificationCtrlGroup = ciscoMemoryPoolNotificationCtrlGroup.setStatus('current')
ciscoMemoryPoolGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 5)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolAlternate"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolValid"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolFree"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLargestFree"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotifThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolGroupRev1 = ciscoMemoryPoolGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEMORY-POOL-MIB", ciscoMemoryPoolUtilizationGroup=ciscoMemoryPoolUtilizationGroup, ciscoMemoryPoolGroup=ciscoMemoryPoolGroup, ciscoMemoryPoolAlternate=ciscoMemoryPoolAlternate, ciscoMemoryPoolNotifications=ciscoMemoryPoolNotifications, ciscoMemoryPoolConformance=ciscoMemoryPoolConformance, ciscoMemoryPoolLowMemoryNotifThreshold=ciscoMemoryPoolLowMemoryNotifThreshold, ciscoMemoryPoolUtilization10Min=ciscoMemoryPoolUtilization10Min, ciscoMemoryPoolFree=ciscoMemoryPoolFree, ciscoMemoryPoolName=ciscoMemoryPoolName, ciscoMemoryPoolLargestFree=ciscoMemoryPoolLargestFree, ciscoMemoryPoolUtilizationEntry=ciscoMemoryPoolUtilizationEntry, ciscoMemoryPoolComplianceRev2=ciscoMemoryPoolComplianceRev2, ciscoMemoryPoolCompliance=ciscoMemoryPoolCompliance, ciscoMemoryPoolLowMemoryNotif=ciscoMemoryPoolLowMemoryNotif, ciscoMemoryPoolUtilization1Min=ciscoMemoryPoolUtilization1Min, ciscoMemoryPoolValid=ciscoMemoryPoolValid, ciscoMemoryPoolUtilizationTable=ciscoMemoryPoolUtilizationTable, ciscoMemoryPoolComplianceRev1=ciscoMemoryPoolComplianceRev1, ciscoMemoryPoolMIB=ciscoMemoryPoolMIB, CiscoMemoryPoolTypes=CiscoMemoryPoolTypes, ciscoMemoryPoolNotificationGroup=ciscoMemoryPoolNotificationGroup, ciscoMemoryPoolTable=ciscoMemoryPoolTable, ciscoMemoryPoolEntry=ciscoMemoryPoolEntry, ciscoMemoryPoolMIBNotificationPrefix=ciscoMemoryPoolMIBNotificationPrefix, ciscoMemoryPoolUsed=ciscoMemoryPoolUsed, ciscoMemoryPoolObjects=ciscoMemoryPoolObjects, ciscoMemoryPoolGroupRev1=ciscoMemoryPoolGroupRev1, ciscoMemoryPoolUtilization5Min=ciscoMemoryPoolUtilization5Min, ciscoMemoryPoolType=ciscoMemoryPoolType, ciscoMemoryPoolLowMemoryNotifEnable=ciscoMemoryPoolLowMemoryNotifEnable, ciscoMemoryPoolCompliances=ciscoMemoryPoolCompliances, ciscoMemoryPoolLowMemoryRecoveryNotif=ciscoMemoryPoolLowMemoryRecoveryNotif, PYSNMP_MODULE_ID=ciscoMemoryPoolMIB, ciscoMemoryPoolGroups=ciscoMemoryPoolGroups, ciscoMemoryPoolNotificationCtrlGroup=ciscoMemoryPoolNotificationCtrlGroup)
