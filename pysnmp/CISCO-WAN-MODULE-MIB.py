#
# PySNMP MIB module CISCO-WAN-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-MODULE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, ModuleIdentity, Counter32, Counter64, NotificationType, IpAddress, MibIdentifier, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32", "Counter64", "NotificationType", "IpAddress", "MibIdentifier", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 145))
ciscoWanModuleMIB.setRevisions(('2002-09-11 00:00', '2001-07-20 00:00', '1999-10-22 00:00',))
if mibBuilder.loadTexts: ciscoWanModuleMIB.setLastUpdated('200209110000Z')
if mibBuilder.loadTexts: ciscoWanModuleMIB.setOrganization('Cisco Systems, Inc.')
cwmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1))
cwmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1))
cwmStatsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2))
class StatisticsLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("levelOne", 1), ("levelTwo", 2), ("levelThree", 3))

cwmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1), )
if mibBuilder.loadTexts: cwmConfigTable.setStatus('current')
cwmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-MODULE-MIB", "cwmIndex"))
if mibBuilder.loadTexts: cwmConfigEntry.setStatus('current')
cwmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cwmIndex.setStatus('current')
cwmIngressSCTFileId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmIngressSCTFileId.setStatus('current')
cwmIngressSCTFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmIngressSCTFileName.setStatus('current')
cwmAutoLineDiagEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmAutoLineDiagEnable.setStatus('current')
cwmSCTFileVerCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmSCTFileVerCfg.setStatus('current')
cwmSCTFileVerOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmSCTFileVerOpr.setStatus('current')
cwmUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmUploadCounter.setStatus('current')
cwmStatConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1), )
if mibBuilder.loadTexts: cwmStatConfigTable.setStatus('current')
cwmStatConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-MODULE-MIB", "cwmIndex"))
if mibBuilder.loadTexts: cwmStatConfigEntry.setStatus('current')
cwmStatBucketInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10, 15, 20, 30, 60))).clone(namedValues=NamedValues(("five", 5), ("ten", 10), ("fifteen", 15), ("twenty", 20), ("thirty", 30), ("sixty", 60))).clone('fifteen')).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatBucketInterval.setStatus('current')
cwmStatCollectionInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 5))).clone(namedValues=NamedValues(("default", 0), ("one", 1), ("five", 5))).clone('default')).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatCollectionInterval.setStatus('current')
cwmStatCollectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatCollectionStatus.setStatus('current')
cwmStatCurrentLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 4), StatisticsLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmStatCurrentLevel.setStatus('current')
cwmStatLevelConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 5), StatisticsLevel().clone('levelOne')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatLevelConfigured.setStatus('current')
cwmStatMaximumConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmStatMaximumConnections.setStatus('current')
ciscoWanModuleMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 2))
ciscoWanModuleMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 2, 0))
ciscoWanModuleMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3))
ciscoWanModuleMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1))
ciscoWanModuleMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2))
ciscoWanModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 1)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBCompliance = ciscoWanModuleMIBCompliance.setStatus('deprecated')
ciscoWanModuleMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 2)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"), ("CISCO-WAN-MODULE-MIB", "cwmConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBComplianceRev1 = ciscoWanModuleMIBComplianceRev1.setStatus('deprecated')
ciscoWanModuleMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 3)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"), ("CISCO-WAN-MODULE-MIB", "cwmConfigGroup2"), ("CISCO-WAN-MODULE-MIB", "cwmUploadGroup"), ("CISCO-WAN-MODULE-MIB", "cwmStatConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBComplianceRev2 = ciscoWanModuleMIBComplianceRev2.setStatus('current')
cwmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 1)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileId"), ("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileName"), ("CISCO-WAN-MODULE-MIB", "cwmAutoLineDiagEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmConfigGroup = cwmConfigGroup.setStatus('current')
cwmStatConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 2)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmStatBucketInterval"), ("CISCO-WAN-MODULE-MIB", "cwmStatCurrentLevel"), ("CISCO-WAN-MODULE-MIB", "cwmStatLevelConfigured"), ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionStatus"), ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionInterval"), ("CISCO-WAN-MODULE-MIB", "cwmStatMaximumConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmStatConfigGroup = cwmStatConfigGroup.setStatus('current')
cwmConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 3)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerCfg"), ("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmConfigGroup2 = cwmConfigGroup2.setStatus('current')
cwmUploadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 4)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmUploadCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmUploadGroup = cwmUploadGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-MODULE-MIB", cwmStatCollectionStatus=cwmStatCollectionStatus, StatisticsLevel=StatisticsLevel, ciscoWanModuleMIBCompliances=ciscoWanModuleMIBCompliances, ciscoWanModuleMIBComplianceRev2=ciscoWanModuleMIBComplianceRev2, ciscoWanModuleMIBNotificationPrefix=ciscoWanModuleMIBNotificationPrefix, cwmStatCurrentLevel=cwmStatCurrentLevel, cwmUploadCounter=cwmUploadCounter, cwmConfigEntry=cwmConfigEntry, ciscoWanModuleMIBComplianceRev1=ciscoWanModuleMIBComplianceRev1, cwmIngressSCTFileId=cwmIngressSCTFileId, cwmConfigTable=cwmConfigTable, ciscoWanModuleMIBConformance=ciscoWanModuleMIBConformance, cwmAutoLineDiagEnable=cwmAutoLineDiagEnable, PYSNMP_MODULE_ID=ciscoWanModuleMIB, cwmStatConfigEntry=cwmStatConfigEntry, cwmStatConfigTable=cwmStatConfigTable, cwmMIBObjects=cwmMIBObjects, cwmUploadGroup=cwmUploadGroup, cwmConfig=cwmConfig, cwmIngressSCTFileName=cwmIngressSCTFileName, ciscoWanModuleMIBGroups=ciscoWanModuleMIBGroups, cwmSCTFileVerCfg=cwmSCTFileVerCfg, ciscoWanModuleMIB=ciscoWanModuleMIB, cwmSCTFileVerOpr=cwmSCTFileVerOpr, cwmStatLevelConfigured=cwmStatLevelConfigured, cwmStatMaximumConnections=cwmStatMaximumConnections, ciscoWanModuleMIBNotifications=ciscoWanModuleMIBNotifications, cwmConfigGroup=cwmConfigGroup, cwmStatsConfig=cwmStatsConfig, cwmConfigGroup2=cwmConfigGroup2, cwmStatCollectionInterval=cwmStatCollectionInterval, ciscoWanModuleMIBCompliance=ciscoWanModuleMIBCompliance, cwmIndex=cwmIndex, cwmStatBucketInterval=cwmStatBucketInterval, cwmStatConfigGroup=cwmStatConfigGroup)
