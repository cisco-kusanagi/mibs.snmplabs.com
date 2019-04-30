#
# PySNMP MIB module CISCO-DOT11-RADIO-DIAGNOSTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-RADIO-DIAGNOSTIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, NotificationType, IpAddress, Integer32, Bits, MibIdentifier, TimeTicks, ObjectIdentity, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "NotificationType", "IpAddress", "Integer32", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoDot11RadioDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 105))
ciscoDot11RadioDiagMIB.setRevisions(('2003-12-23 00:00', '2003-05-08 00:00',))
if mibBuilder.loadTexts: ciscoDot11RadioDiagMIB.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoDot11RadioDiagMIB.setOrganization('Cisco System Inc.')
cDot11RadioDiagMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 0))
cDot11RadioDiagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 1))
cDot11RadioDiagConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1))
cDot11RadioDiagTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11RadioDiagTable.setStatus('current')
cDot11RadioDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11RadioDiagEntry.setStatus('current')
cDot11RadioDiagTempChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(100, 100), ValueRangeConstraint(104, 104), ValueRangeConstraint(108, 108), ValueRangeConstraint(112, 112), ValueRangeConstraint(116, 116), ValueRangeConstraint(120, 120), ValueRangeConstraint(124, 124), ValueRangeConstraint(128, 128), ValueRangeConstraint(132, 132), ValueRangeConstraint(136, 136), ValueRangeConstraint(140, 140), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempChannel.setStatus('current')
cDot11RadioDiagTempTxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempTxPowerLevel.setStatus('current')
cDot11RadioDiagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("apRadioDiscovery", 2), ("siteSurveyTempSettings", 3), ("siteSurveyNonTempSettings", 4))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagMode.setStatus('current')
cDot11RadioDiagSettingsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagSettingsEnabled.setStatus('current')
cDot11RadioDiagTempClientTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempClientTxPower.setStatus('current')
cDot11RadioDiagTempDataRateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 126))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cDot11RadioDiagTempDataRateSet.setStatus('current')
cDot11RadioDiagMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 2))
cDot11RadioDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1))
cDot11RadioDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2))
cDot11RadioDiagMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1, 1)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagConfigGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagMIBCompliance = cDot11RadioDiagMIBCompliance.setStatus('deprecated')
cDot11RadioDiagMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1, 2)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagConfigGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagMIBComplianceRev1 = cDot11RadioDiagMIBComplianceRev1.setStatus('current')
cDot11RadioDiagConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2, 1)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempChannel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempTxPowerLevel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagMode"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagSettingsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagConfigGlobalGroup = cDot11RadioDiagConfigGlobalGroup.setStatus('deprecated')
cDot11RadioDiagConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2, 2)).setObjects(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempChannel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempTxPowerLevel"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagMode"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagSettingsEnabled"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempClientTxPower"), ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempDataRateSet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11RadioDiagConfigGroupRev1 = cDot11RadioDiagConfigGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", cDot11RadioDiagMIBConform=cDot11RadioDiagMIBConform, cDot11RadioDiagMIBNotifs=cDot11RadioDiagMIBNotifs, cDot11RadioDiagMIBComplianceRev1=cDot11RadioDiagMIBComplianceRev1, cDot11RadioDiagEntry=cDot11RadioDiagEntry, cDot11RadioDiagMode=cDot11RadioDiagMode, cDot11RadioDiagConfigGroupRev1=cDot11RadioDiagConfigGroupRev1, cDot11RadioDiagConfigGlobal=cDot11RadioDiagConfigGlobal, PYSNMP_MODULE_ID=ciscoDot11RadioDiagMIB, cDot11RadioDiagTempDataRateSet=cDot11RadioDiagTempDataRateSet, cDot11RadioDiagMIBGroups=cDot11RadioDiagMIBGroups, ciscoDot11RadioDiagMIB=ciscoDot11RadioDiagMIB, cDot11RadioDiagMIBCompliances=cDot11RadioDiagMIBCompliances, cDot11RadioDiagMIBCompliance=cDot11RadioDiagMIBCompliance, cDot11RadioDiagSettingsEnabled=cDot11RadioDiagSettingsEnabled, cDot11RadioDiagTable=cDot11RadioDiagTable, cDot11RadioDiagTempClientTxPower=cDot11RadioDiagTempClientTxPower, cDot11RadioDiagConfigGlobalGroup=cDot11RadioDiagConfigGlobalGroup, cDot11RadioDiagMIBObjects=cDot11RadioDiagMIBObjects, cDot11RadioDiagTempTxPowerLevel=cDot11RadioDiagTempTxPowerLevel, cDot11RadioDiagTempChannel=cDot11RadioDiagTempChannel)
