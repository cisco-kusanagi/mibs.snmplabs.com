#
# PySNMP MIB module Unisphere-Data-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, MibIdentifier, Counter32, IpAddress, iso, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, ModuleIdentity, TimeTicks, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Counter32", "IpAddress", "iso", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType")
TruthValue, RowStatus, DateAndTime, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DateAndTime", "TimeStamp", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdLogSeverity, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdLogSeverity")
usdLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28))
usdLogMIB.setRevisions(('2001-03-16 19:02', '2000-03-27 05:00', '1999-11-08 00:00',))
if mibBuilder.loadTexts: usdLogMIB.setLastUpdated('200103161902Z')
if mibBuilder.loadTexts: usdLogMIB.setOrganization('Unisphere Networks, Inc.')
class UsdLogCatName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class UsdLogVerbosity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("low", 0), ("medium", 1), ("high", 2))

class UsdLogSyslogFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("local0", 0), ("local1", 1), ("local2", 2), ("local3", 3), ("local4", 4), ("local5", 5), ("local6", 6), ("local7", 7))

usdLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1))
usdLogDestinations = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1))
usdLogCategories = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2))
usdLogMessages = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3))
usdLogDestSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1))
usdLogDestConsole = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2))
usdLogDestNvFile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3))
usdLogDestSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 1), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestSyslogSeverity.setStatus('obsolete')
usdLogDestSyslogAddress = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestSyslogAddress.setStatus('obsolete')
usdLogSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3), )
if mibBuilder.loadTexts: usdLogSyslogTable.setStatus('current')
usdLogSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1), ).setIndexNames((0, "Unisphere-Data-LOG-MIB", "usdLogSyslogIpAddress"))
if mibBuilder.loadTexts: usdLogSyslogEntry.setStatus('current')
usdLogSyslogIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: usdLogSyslogIpAddress.setStatus('current')
usdLogSyslogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdLogSyslogRowStatus.setStatus('current')
usdLogSyslogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 3), UsdLogSeverity().clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdLogSyslogSeverity.setStatus('current')
usdLogSyslogFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 1, 3, 1, 4), UsdLogSyslogFacility().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdLogSyslogFacility.setStatus('current')
usdLogDestConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 2, 1), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestConsoleSeverity.setStatus('current')
usdLogDestNvFileSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 1, 3, 1), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogDestNvFileSeverity.setStatus('current')
usdLogCatScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 1))
usdLogCatTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2), )
if mibBuilder.loadTexts: usdLogCatTable.setStatus('current')
usdLogCatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-LOG-MIB", "usdLogCatIndex"))
if mibBuilder.loadTexts: usdLogCatEntry.setStatus('current')
usdLogCatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: usdLogCatIndex.setStatus('current')
usdLogCatName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 2), UsdLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatName.setStatus('current')
usdLogCatDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatDescr.setStatus('current')
usdLogCatEngineering = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatEngineering.setStatus('current')
usdLogCatDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatDiscards.setStatus('current')
usdLogCatSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 6), UsdLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogCatSeverity.setStatus('current')
usdLogCatVerbosity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 2, 1, 7), UsdLogVerbosity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogCatVerbosity.setStatus('current')
usdLogCatNameTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3), )
if mibBuilder.loadTexts: usdLogCatNameTable.setStatus('current')
usdLogCatNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1), ).setIndexNames((1, "Unisphere-Data-LOG-MIB", "usdLogCatNameName"))
if mibBuilder.loadTexts: usdLogCatNameEntry.setStatus('current')
usdLogCatNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 1), UsdLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatNameName.setStatus('current')
usdLogCatNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogCatNameIndex.setStatus('current')
usdLogMsgScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1))
usdLogMsgCapacity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 1), Integer32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgCapacity.setStatus('current')
usdLogMsgLastSeqNumber = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgLastSeqNumber.setStatus('current')
usdLogMsgTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2), )
if mibBuilder.loadTexts: usdLogMsgTable.setStatus('current')
usdLogMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1), ).setIndexNames((0, "Unisphere-Data-LOG-MIB", "usdLogMsgSysUpTimeStamp"), (0, "Unisphere-Data-LOG-MIB", "usdLogMsgSequenceNumber"))
if mibBuilder.loadTexts: usdLogMsgEntry.setStatus('current')
usdLogMsgSysUpTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 1), TimeStamp())
if mibBuilder.loadTexts: usdLogMsgSysUpTimeStamp.setStatus('current')
usdLogMsgSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: usdLogMsgSequenceNumber.setStatus('current')
usdLogMsgCatName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 3), UsdLogCatName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgCatName.setStatus('current')
usdLogMsgCatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgCatIndex.setStatus('current')
usdLogMsgSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 5), UsdLogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgSeverity.setStatus('current')
usdLogMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgText.setStatus('current')
usdLogMsgDateAndTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 1, 3, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdLogMsgDateAndTimeStamp.setStatus('current')
usdLogTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2))
usdLogMsgThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdLogMsgThreshold.setStatus('current')
usdLogTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0))
usdLogMsgThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 0, 1)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"), ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
if mibBuilder.loadTexts: usdLogMsgThresholdTrap.setStatus('current')
usdLogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4))
usdLogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1))
usdLogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2))
usdLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 1)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogCompliance = usdLogCompliance.setStatus('obsolete')
usdLogCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 1, 2)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogGroup2"), ("Unisphere-Data-LOG-MIB", "usdLogTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogCompliance2 = usdLogCompliance2.setStatus('current')
usdLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 1)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogDestSyslogSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogDestSyslogAddress"), ("Unisphere-Data-LOG-MIB", "usdLogDestConsoleSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogDestNvFileSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatName"), ("Unisphere-Data-LOG-MIB", "usdLogCatDescr"), ("Unisphere-Data-LOG-MIB", "usdLogCatEngineering"), ("Unisphere-Data-LOG-MIB", "usdLogCatDiscards"), ("Unisphere-Data-LOG-MIB", "usdLogCatSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatVerbosity"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameName"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatName"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgText"), ("Unisphere-Data-LOG-MIB", "usdLogMsgDateAndTimeStamp"), ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogGroup = usdLogGroup.setStatus('obsolete')
usdLogGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 2)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogSyslogRowStatus"), ("Unisphere-Data-LOG-MIB", "usdLogSyslogSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogSyslogFacility"), ("Unisphere-Data-LOG-MIB", "usdLogDestConsoleSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogDestNvFileSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatName"), ("Unisphere-Data-LOG-MIB", "usdLogCatDescr"), ("Unisphere-Data-LOG-MIB", "usdLogCatEngineering"), ("Unisphere-Data-LOG-MIB", "usdLogCatDiscards"), ("Unisphere-Data-LOG-MIB", "usdLogCatSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogCatVerbosity"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameName"), ("Unisphere-Data-LOG-MIB", "usdLogCatNameIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCapacity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgLastSeqNumber"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatName"), ("Unisphere-Data-LOG-MIB", "usdLogMsgCatIndex"), ("Unisphere-Data-LOG-MIB", "usdLogMsgSeverity"), ("Unisphere-Data-LOG-MIB", "usdLogMsgText"), ("Unisphere-Data-LOG-MIB", "usdLogMsgDateAndTimeStamp"), ("Unisphere-Data-LOG-MIB", "usdLogMsgThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogGroup2 = usdLogGroup2.setStatus('current')
usdLogTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 28, 4, 2, 3)).setObjects(("Unisphere-Data-LOG-MIB", "usdLogMsgThresholdTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogTrapGroup = usdLogTrapGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-LOG-MIB", usdLogGroup=usdLogGroup, usdLogMsgText=usdLogMsgText, usdLogDestNvFile=usdLogDestNvFile, usdLogCatNameIndex=usdLogCatNameIndex, usdLogMessages=usdLogMessages, usdLogMsgSeverity=usdLogMsgSeverity, usdLogMsgEntry=usdLogMsgEntry, UsdLogVerbosity=UsdLogVerbosity, usdLogMIBCompliances=usdLogMIBCompliances, usdLogMIBConformance=usdLogMIBConformance, usdLogCatDiscards=usdLogCatDiscards, usdLogCatVerbosity=usdLogCatVerbosity, usdLogMsgSysUpTimeStamp=usdLogMsgSysUpTimeStamp, usdLogCatSeverity=usdLogCatSeverity, usdLogCatNameTable=usdLogCatNameTable, usdLogMsgLastSeqNumber=usdLogMsgLastSeqNumber, usdLogCategories=usdLogCategories, usdLogMsgScalars=usdLogMsgScalars, usdLogDestConsoleSeverity=usdLogDestConsoleSeverity, usdLogCompliance2=usdLogCompliance2, usdLogCatIndex=usdLogCatIndex, usdLogMsgTable=usdLogMsgTable, usdLogCatScalars=usdLogCatScalars, usdLogDestSyslogAddress=usdLogDestSyslogAddress, usdLogCatName=usdLogCatName, usdLogGroup2=usdLogGroup2, usdLogSyslogRowStatus=usdLogSyslogRowStatus, usdLogDestConsole=usdLogDestConsole, usdLogSyslogEntry=usdLogSyslogEntry, usdLogCatDescr=usdLogCatDescr, usdLogCatNameName=usdLogCatNameName, PYSNMP_MODULE_ID=usdLogMIB, usdLogCatEntry=usdLogCatEntry, usdLogCatTable=usdLogCatTable, usdLogCatEngineering=usdLogCatEngineering, usdLogCatNameEntry=usdLogCatNameEntry, usdLogMsgCatName=usdLogMsgCatName, usdLogMsgDateAndTimeStamp=usdLogMsgDateAndTimeStamp, usdLogSyslogFacility=usdLogSyslogFacility, usdLogTrapPrefix=usdLogTrapPrefix, usdLogMsgThresholdTrap=usdLogMsgThresholdTrap, usdLogSyslogTable=usdLogSyslogTable, usdLogObjects=usdLogObjects, usdLogSyslogSeverity=usdLogSyslogSeverity, usdLogMIBGroups=usdLogMIBGroups, usdLogSyslogIpAddress=usdLogSyslogIpAddress, usdLogDestSyslog=usdLogDestSyslog, usdLogDestNvFileSeverity=usdLogDestNvFileSeverity, usdLogMsgCapacity=usdLogMsgCapacity, usdLogDestinations=usdLogDestinations, usdLogCompliance=usdLogCompliance, usdLogMsgThreshold=usdLogMsgThreshold, usdLogMIB=usdLogMIB, usdLogTrapControl=usdLogTrapControl, usdLogMsgCatIndex=usdLogMsgCatIndex, usdLogTrapGroup=usdLogTrapGroup, UsdLogCatName=UsdLogCatName, usdLogDestSyslogSeverity=usdLogDestSyslogSeverity, UsdLogSyslogFacility=UsdLogSyslogFacility, usdLogMsgSequenceNumber=usdLogMsgSequenceNumber)
