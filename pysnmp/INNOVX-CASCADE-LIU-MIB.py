#
# PySNMP MIB module INNOVX-CASCADE-LIU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INNOVX-CASCADE-LIU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
casGroup, = mibBuilder.importSymbols("INNOVX-CORE-MIB", "casGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, Unsigned32, IpAddress, ObjectIdentity, Gauge32, Bits, Counter32, Counter64, iso, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "Bits", "Counter32", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adminGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 1))
configGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2))
alarmCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3))
diagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4))
statusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 5))
cascadeMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeMIBversion.setStatus('mandatory')
cascadeInService = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeInService.setStatus('mandatory')
cascadeSetFrameType = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("esf", 1), ("d4", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeSetFrameType.setStatus('mandatory')
cascadeOperFrameType = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("esf", 1), ("d4", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeOperFrameType.setStatus('mandatory')
cascadeLineCoding = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("b8zs", 1), ("ami", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLineCoding.setStatus('mandatory')
cascadeIntfType = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("ds1-auto-lbo", 1), ("ds1-zero-dB", 2), ("ds1-neg7pt5-dB", 3), ("ds1-neg15pt0-dB", 4), ("ds1-neg22pt5-dB", 5), ("dsx1-preeq130-ft", 6), ("dsx1-preeq260-ft", 7), ("dsx1-preeq390-ft", 8), ("dsx1-preeq530-ft", 9), ("dsx1-preeq655-ft", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeIntfType.setStatus('mandatory')
cascadeDS1IntfRcvLevel = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noSignal", 1), ("pos2toNeg7pt5-dB", 2), ("neg7pt5toNeg15-dB", 3), ("neg15toNeg22pt5-dB", 4), ("lessThanNeg22pt5-dB", 5), ("invalidDSX1intf", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeDS1IntfRcvLevel.setStatus('mandatory')
cascadeDropAndInsertTable = MibTable((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7), )
if mibBuilder.loadTexts: cascadeDropAndInsertTable.setStatus('mandatory')
channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1), ).setIndexNames((0, "INNOVX-CASCADE-LIU-MIB", "channelIndex"))
if mibBuilder.loadTexts: channelEntry.setStatus('mandatory')
channelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelIndex.setStatus('mandatory')
cascadeDropAndInsert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("clearChannel", 2), ("signallingChannel", 3), ("casChannel", 4), ("tsNotAvailable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeDropAndInsert.setStatus('mandatory')
cascadeBpvTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeBpvTrapSeverity.setStatus('mandatory')
cascadeBpvWindow = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneMinute", 1), ("fifteenMinutes", 2), ("oneHour", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeBpvWindow.setStatus('mandatory')
cascadeBpvThresh = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("thr1", 1), ("thr10", 2), ("thr100", 3), ("thr1000", 4), ("thr10000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeBpvThresh.setStatus('mandatory')
cascadeCrcTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeCrcTrapSeverity.setStatus('mandatory')
cascadeCrcWindow = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneMinute", 1), ("fifteenMinutes", 2), ("oneHour", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeCrcWindow.setStatus('mandatory')
cascadeCrcThresh = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("thr1", 1), ("thr10", 2), ("thr100", 3), ("thr1000", 4), ("thr10000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeCrcThresh.setStatus('mandatory')
cascadeLadTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLadTrapSeverity.setStatus('mandatory')
cascadeLadWindow = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneMinute", 1), ("fifteenMinutes", 2), ("oneHour", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLadWindow.setStatus('mandatory')
cascadeLadThresh = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("thr1", 1), ("thr10", 2), ("thr100", 3), ("thr1000", 4), ("thr10000", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLadThresh.setStatus('mandatory')
cascadeAisTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeAisTrapSeverity.setStatus('mandatory')
cascadeLosTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeLosTrapSeverity.setStatus('mandatory')
cascadeOofTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeOofTrapSeverity.setStatus('mandatory')
cascadeRcdYelTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeRcdYelTrapSeverity.setStatus('mandatory')
cascadeUssTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 3, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inhibit", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("info", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeUssTrapSeverity.setStatus('mandatory')
cascadeDiagTest = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cascadeLineLoopback", 1), ("cascadePayLoadLoopback", 2), ("cascadeStopTest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeDiagTest.setStatus('mandatory')
cascadeDiagTestDuration = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("testTime1Min", 1), ("testTime5Mins", 2), ("testTime10Mins", 3), ("testTime20Mins", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cascadeDiagTestDuration.setStatus('mandatory')
cascadeDiagTestStatus = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("statcascadeLineLoopback", 1), ("statcascadePayLoadLoopback", 2), ("statNoTestinProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadeDiagTestStatus.setStatus('mandatory')
cascadePortStatus = MibScalar((1, 3, 6, 1, 4, 1, 498, 22, 1, 4, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cascadePortStatus.setStatus('mandatory')
mibBuilder.exportSymbols("INNOVX-CASCADE-LIU-MIB", adminGroup=adminGroup, diagnostics=diagnostics, cascadeDiagTestDuration=cascadeDiagTestDuration, cascadeSetFrameType=cascadeSetFrameType, cascadeLadWindow=cascadeLadWindow, channelEntry=channelEntry, channelIndex=channelIndex, configGroup=configGroup, cascadeMIBversion=cascadeMIBversion, alarmCfgGroup=alarmCfgGroup, cascadeLadTrapSeverity=cascadeLadTrapSeverity, cascadeInService=cascadeInService, cascadeDropAndInsertTable=cascadeDropAndInsertTable, cascadeDiagTest=cascadeDiagTest, cascadePortStatus=cascadePortStatus, cascadeDiagTestStatus=cascadeDiagTestStatus, cascadeDS1IntfRcvLevel=cascadeDS1IntfRcvLevel, cascadeOperFrameType=cascadeOperFrameType, cascadeCrcTrapSeverity=cascadeCrcTrapSeverity, cascadeCrcThresh=cascadeCrcThresh, cascadeLosTrapSeverity=cascadeLosTrapSeverity, cascadeLineCoding=cascadeLineCoding, cascadeBpvWindow=cascadeBpvWindow, cascadeIntfType=cascadeIntfType, cascadeUssTrapSeverity=cascadeUssTrapSeverity, statusGroup=statusGroup, cascadeLadThresh=cascadeLadThresh, cascadeAisTrapSeverity=cascadeAisTrapSeverity, cascadeBpvThresh=cascadeBpvThresh, cascadeRcdYelTrapSeverity=cascadeRcdYelTrapSeverity, cascadeCrcWindow=cascadeCrcWindow, cascadeBpvTrapSeverity=cascadeBpvTrapSeverity, cascadeOofTrapSeverity=cascadeOofTrapSeverity, cascadeDropAndInsert=cascadeDropAndInsert)