#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-SAS-IEEE8021-CFM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
dot1agCfmMepEntry, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMepEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, iso, Counter64, Integer32, MibIdentifier, ObjectIdentity, NotificationType, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "iso", "Counter64", "Integer32", "MibIdentifier", "ObjectIdentity", "NotificationType", "TimeTicks", "Unsigned32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
timetraSASModules, timetraSASObjs, timetraSASConfs = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASModules", "timetraSASObjs", "timetraSASConfs")
timetraSASIEEE8021CfmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 11))
timetraSASIEEE8021CfmMIBModule.setRevisions(('1910-01-01 00:00',))
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setLastUpdated('0902280000Z')
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setOrganization('Alcatel')
tmnxSASDot1agMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11))
tmnxSASDot1agMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7))
tmnxSASDot1agCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1))
tmnxSASDot1agNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2))
tmnxSASDot1agNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2, 1))
tmnxDot1agCfmMepExtnTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1), )
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnTable.setStatus('current')
tmnxDot1agCfmMepExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1), )
dot1agCfmMepEntry.registerAugmentions(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepExtnEntry"))
tmnxDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnEntry.setStatus('current')
tmnxDot1agCfmMepSendAisOnPortDown = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxDot1agCfmMepSendAisOnPortDown.setStatus('current')
tmnxDot1agCfmMepControlSapTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxDot1agCfmMepControlSapTag.setStatus('current')
tmnxSASDot1agCfmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1))
tmnxSASDot1agCfmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2))
tmnxSASDot1agCfmComplianceV2v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1, 2)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxSASDot1agCfmMepGroupV2v0"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmComplianceV2v0 = tmnxSASDot1agCfmComplianceV2v0.setStatus('current')
tmnxSASDot1agCfmMepGroupV2v0 = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 1)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmMepGroupV2v0 = tmnxSASDot1agCfmMepGroupV2v0.setStatus('current')
tmnxSASDot1agCfmMepGroupV4v0 = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 2)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"), ("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepControlSapTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmMepGroupV4v0 = tmnxSASDot1agCfmMepGroupV4v0.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-CFM-MIB", tmnxSASDot1agNotifications=tmnxSASDot1agNotifications, tmnxDot1agCfmMepExtnEntry=tmnxDot1agCfmMepExtnEntry, tmnxSASDot1agCfmCompliances=tmnxSASDot1agCfmCompliances, tmnxSASDot1agNotificationsPrefix=tmnxSASDot1agNotificationsPrefix, tmnxSASDot1agCfmMep=tmnxSASDot1agCfmMep, tmnxDot1agCfmMepControlSapTag=tmnxDot1agCfmMepControlSapTag, tmnxDot1agCfmMepSendAisOnPortDown=tmnxDot1agCfmMepSendAisOnPortDown, tmnxSASDot1agCfmMepGroupV2v0=tmnxSASDot1agCfmMepGroupV2v0, tmnxSASDot1agCfmMepGroupV4v0=tmnxSASDot1agCfmMepGroupV4v0, tmnxSASDot1agMIBObjs=tmnxSASDot1agMIBObjs, tmnxSASDot1agMIBConformance=tmnxSASDot1agMIBConformance, PYSNMP_MODULE_ID=timetraSASIEEE8021CfmMIBModule, timetraSASIEEE8021CfmMIBModule=timetraSASIEEE8021CfmMIBModule, tmnxDot1agCfmMepExtnTable=tmnxDot1agCfmMepExtnTable, tmnxSASDot1agCfmGroups=tmnxSASDot1agCfmGroups, tmnxSASDot1agCfmComplianceV2v0=tmnxSASDot1agCfmComplianceV2v0)
