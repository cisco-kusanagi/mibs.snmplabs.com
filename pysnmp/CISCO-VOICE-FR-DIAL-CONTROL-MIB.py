#
# PySNMP MIB module CISCO-VOICE-FR-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-FR-DIAL-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "CvcGUid")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Unsigned32, IpAddress, Bits, ModuleIdentity, NotificationType, iso, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Unsigned32", "IpAddress", "Bits", "ModuleIdentity", "NotificationType", "iso", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceFrDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 36))
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setLastUpdated('9804140000Z')
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvfrdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1))
cvFrCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1))
cvFrCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1), )
if mibBuilder.loadTexts: cvFrCallHistoryTable.setStatus('current')
cvFrCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvFrCallHistoryEntry.setStatus('current')
cvFrCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryConnectionId.setStatus('current')
cvFrCallHistoryDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryDlci.setStatus('current')
cvFrCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryLowerIfName.setStatus('current')
cvFrCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistorySessionTarget.setStatus('current')
cvfrdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3))
cvfrdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1))
cvfrdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2))
cvfrdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvfrdcMIBCompliance = cvfrdcMIBCompliance.setStatus('current')
cvFrCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryConnectionId"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryDlci"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryLowerIfName"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvFrCallHistoryGroup = cvFrCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-FR-DIAL-CONTROL-MIB", cvFrCallHistorySessionTarget=cvFrCallHistorySessionTarget, cvFrCallHistoryDlci=cvFrCallHistoryDlci, cvfrdcMIBCompliance=cvfrdcMIBCompliance, cvFrCallHistoryTable=cvFrCallHistoryTable, cvFrCallHistory=cvFrCallHistory, cvFrCallHistoryEntry=cvFrCallHistoryEntry, cvFrCallHistoryConnectionId=cvFrCallHistoryConnectionId, cvFrCallHistoryLowerIfName=cvFrCallHistoryLowerIfName, cvFrCallHistoryGroup=cvFrCallHistoryGroup, cvfrdcMIBObjects=cvfrdcMIBObjects, cvfrdcMIBGroups=cvfrdcMIBGroups, cvfrdcMIBConformance=cvfrdcMIBConformance, ciscoVoiceFrDialControlMIB=ciscoVoiceFrDialControlMIB, PYSNMP_MODULE_ID=ciscoVoiceFrDialControlMIB, cvfrdcMIBCompliances=cvfrdcMIBCompliances)
