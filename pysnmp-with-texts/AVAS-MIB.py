#
# PySNMP MIB module AVAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, enterprises, MibIdentifier, NotificationType, Gauge32, NotificationType, Counter32, ModuleIdentity, Integer32, TimeTicks, iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "enterprises", "MibIdentifier", "NotificationType", "Gauge32", "NotificationType", "Counter32", "ModuleIdentity", "Integer32", "TimeTicks", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
sniProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2))
sniAVAS = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24))
avasProc = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 1))
avasNet = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 2))
avasElem = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 3))
avasCond = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 4))
avasGlobalData = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 10))
avasTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 11))
avasPSumStat = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 50, 99, 255))).clone(namedValues=NamedValues(("missing", 1), ("ready", 2), ("running", 3), ("errorSystem", 4), ("errorNet", 5), ("errorSignon", 50), ("unknown", 99), ("undefined", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasPSumStat.setStatus('mandatory')
if mibBuilder.loadTexts: avasPSumStat.setDescription('Summary-State of Avas')
avasPUpamStat = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 255))).clone(namedValues=NamedValues(("started", 1), ("ready", 2), ("running", 3), ("ended", 4), ("abended", 5), ("stop", 6), ("hold", 7), ("shutdown", 8), ("kill", 9), ("unknown", 99), ("undefined", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasPUpamStat.setStatus('mandatory')
if mibBuilder.loadTexts: avasPUpamStat.setDescription('State of Process : UPAM-ZD')
avasPPlamStat = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 255))).clone(namedValues=NamedValues(("started", 1), ("ready", 2), ("running", 3), ("ended", 4), ("abended", 5), ("stop", 6), ("hold", 7), ("shutdown", 8), ("kill", 9), ("unknown", 99), ("undefined", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasPPlamStat.setStatus('mandatory')
if mibBuilder.loadTexts: avasPPlamStat.setDescription('State of Process PLAM-ZD')
avasPCentrStat = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 255))).clone(namedValues=NamedValues(("started", 1), ("ready", 2), ("running", 3), ("ended", 4), ("abended", 5), ("stop", 6), ("hold", 7), ("shutdown", 8), ("kill", 9), ("unknown", 99), ("undefined", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasPCentrStat.setStatus('mandatory')
if mibBuilder.loadTexts: avasPCentrStat.setDescription('State of CENTRAL-Process')
avasPAvakNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasPAvakNum.setStatus('mandatory')
if mibBuilder.loadTexts: avasPAvakNum.setDescription('The number of entries in the table avasPAvakTab')
avasPAvakTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6), )
if mibBuilder.loadTexts: avasPAvakTab.setStatus('mandatory')
if mibBuilder.loadTexts: avasPAvakTab.setDescription('The AVAS AVAK table')
avasPAvakTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1), ).setIndexNames((0, "AVAS-MIB", "avasPAvakTabIndex"))
if mibBuilder.loadTexts: avasPAvakTabEntry.setStatus('mandatory')
if mibBuilder.loadTexts: avasPAvakTabEntry.setDescription('An entry in the AVAS AVAK table')
avasPAvakTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasPAvakTabIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avasPAvakTabIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of avasPAvakTabNum')
avasPAvakJvName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasPAvakJvName.setStatus('mandatory')
if mibBuilder.loadTexts: avasPAvakJvName.setDescription('The Name of the Job-Variable for the AVAK')
avasPAvakState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 255))).clone(namedValues=NamedValues(("started", 1), ("ready", 2), ("running", 3), ("ended", 4), ("abended", 5), ("stop", 6), ("hold", 7), ("shutdown", 8), ("kill", 9), ("unknown", 99), ("undefined", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasPAvakState.setStatus('mandatory')
if mibBuilder.loadTexts: avasPAvakState.setDescription("State of AVAK. It's the value of the Job-Variable ")
avasNStateF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 6, 7, 8, 9, 100))).clone(namedValues=NamedValues(("problem", 1), ("error", 5), ("hold", 6), ("running", 7), ("waiting", 8), ("condwait", 9), ("all", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasNStateF.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStateF.setDescription('State-Flag for restriction in Show Table')
avasNPatF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasNPatF.setStatus('mandatory')
if mibBuilder.loadTexts: avasNPatF.setDescription('Name-Pattern for restriction in Show Table')
avasNNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNNum.setStatus('mandatory')
if mibBuilder.loadTexts: avasNNum.setDescription('The number of entries in the table avasNTab')
avasNTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4), )
if mibBuilder.loadTexts: avasNTab.setStatus('mandatory')
if mibBuilder.loadTexts: avasNTab.setDescription('The AVAS Net table')
avasNTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1), ).setIndexNames((0, "AVAS-MIB", "avasNTabIndex"))
if mibBuilder.loadTexts: avasNTabEntry.setStatus('mandatory')
if mibBuilder.loadTexts: avasNTabEntry.setDescription('An entry in the AVAS Net table')
avasNTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNTabIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avasNTabIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of avasNTabNum')
avasNName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNName.setStatus('mandatory')
if mibBuilder.loadTexts: avasNName.setDescription('The Name of the Net')
avasNStart = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNStart.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStart.setDescription('The Start-Time of the Net')
avasNState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 17, 21, 99))).clone(namedValues=NamedValues(("abended", 3), ("ended", 4), ("error", 5), ("hold", 6), ("running", 7), ("waiting", 8), ("condwait", 9), ("restarted", 10), ("resumed", 11), ("opwait", 12), ("ignored", 14), ("start", 17), ("shifted", 21), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNState.setStatus('mandatory')
if mibBuilder.loadTexts: avasNState.setDescription('The State of the Net')
avasNStateOfError = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 99))).clone(namedValues=NamedValues(("yes", 1), ("no", 2), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNStateOfError.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStateOfError.setDescription('An Element is of state Error')
avasNStateOfRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 99))).clone(namedValues=NamedValues(("yes", 1), ("no", 2), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNStateOfRestart.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStateOfRestart.setDescription('An Element is of state Restart')
avasNStateOfCondwait = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 99))).clone(namedValues=NamedValues(("yes", 1), ("no", 2), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNStateOfCondwait.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStateOfCondwait.setDescription('An Element is of state Condwait')
avasNStateOfHold = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 99))).clone(namedValues=NamedValues(("yes", 1), ("no", 2), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNStateOfHold.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStateOfHold.setDescription('An Element is of state Hold')
avasNAvak = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNAvak.setStatus('mandatory')
if mibBuilder.loadTexts: avasNAvak.setDescription('The AVAK of the Net')
avasNStartedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNStartedIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avasNStartedIndex.setDescription('The smallest index of the Net')
avasNText = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 2, 4, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasNText.setStatus('mandatory')
if mibBuilder.loadTexts: avasNText.setDescription('A short description of the Net')
avasEEStateF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 6, 7, 8, 13, 23))).clone(namedValues=NamedValues(("all", 1), ("abended", 3), ("error", 5), ("hold", 6), ("running-exec", 7), ("waiting", 8), ("skipped", 13), ("no-occure", 23)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasEEStateF.setStatus('mandatory')
if mibBuilder.loadTexts: avasEEStateF.setDescription('Element-State-Flag for restriction in Show Table')
avasEETypeF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("all", 1), ("net", 2), ("jva", 3), ("ext", 4), ("mod", 5), ("std", 6), ("job", 7), ("res", 8), ("val", 9), ("tim", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasEETypeF.setStatus('mandatory')
if mibBuilder.loadTexts: avasEETypeF.setDescription('Element-Type-Flag for restriction in Show Table')
avasEEFuncF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("all", 1), ("job", 2), ("proc", 3), ("comp", 4), ("add", 5), ("delete", 6), ("modify", 7), ("net", 8), ("wait", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasEEFuncF.setStatus('mandatory')
if mibBuilder.loadTexts: avasEEFuncF.setDescription('Element-Function-Flag for restriction in Show Table')
avasENStateF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 6, 7, 8, 9, 100))).clone(namedValues=NamedValues(("problem", 1), ("error", 5), ("hold", 6), ("running", 7), ("waiting", 8), ("condwait", 9), ("all", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasENStateF.setStatus('mandatory')
if mibBuilder.loadTexts: avasENStateF.setDescription('State-Flag for restriction in Show Table')
avasENPatF = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasENPatF.setStatus('mandatory')
if mibBuilder.loadTexts: avasENPatF.setDescription('Name-Pattern for restriction in Show Table')
avasENum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasENum.setStatus('mandatory')
if mibBuilder.loadTexts: avasENum.setDescription('The number of entries in the table avasETab')
avasETab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7), )
if mibBuilder.loadTexts: avasETab.setStatus('mandatory')
if mibBuilder.loadTexts: avasETab.setDescription('The AVAS Element table')
avasETabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1), ).setIndexNames((0, "AVAS-MIB", "avasETabIndex"))
if mibBuilder.loadTexts: avasETabEntry.setStatus('mandatory')
if mibBuilder.loadTexts: avasETabEntry.setDescription('An entry in the AVAS Element table')
avasETabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasETabIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avasETabIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of avasETabNum')
avasEName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEName.setStatus('mandatory')
if mibBuilder.loadTexts: avasEName.setDescription('The Name of the Element')
avasEFu = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 99))).clone(namedValues=NamedValues(("job", 2), ("proc", 3), ("comp", 4), ("add", 5), ("delete", 6), ("modify", 7), ("net", 8), ("wait", 9), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEFu.setStatus('mandatory')
if mibBuilder.loadTexts: avasEFu.setDescription('The Function of the Element')
avasEType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 99))).clone(namedValues=NamedValues(("net", 2), ("jva", 3), ("ext", 4), ("mod", 5), ("std", 6), ("job", 7), ("res", 8), ("val", 9), ("tim", 10), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEType.setStatus('mandatory')
if mibBuilder.loadTexts: avasEType.setDescription('The Type of the Element')
avasEInd = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEInd.setStatus('mandatory')
if mibBuilder.loadTexts: avasEInd.setDescription('The Index of the Element')
avasESynInd = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasESynInd.setStatus('mandatory')
if mibBuilder.loadTexts: avasESynInd.setDescription('The Index of the Element')
avasEState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 13, 14, 16, 18, 19, 20, 22, 23, 66, 99))).clone(namedValues=NamedValues(("created", 2), ("abended", 3), ("ended", 4), ("error", 5), ("hold", 6), ("running", 7), ("waiting", 8), ("skipped", 13), ("ignored", 14), ("executed", 16), ("no-plan", 18), ("deleted", 19), ("no-submit", 20), ("occurred", 22), ("no-occure", 23), ("error-cat", 66), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEState.setStatus('mandatory')
if mibBuilder.loadTexts: avasEState.setDescription('The State of the Element')
avasENet = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasENet.setStatus('mandatory')
if mibBuilder.loadTexts: avasENet.setDescription('The Net of the Element')
avasEDelSolution = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("start", 1), ("ignore", 2), ("cancel", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEDelSolution.setStatus('mandatory')
if mibBuilder.loadTexts: avasEDelSolution.setDescription('Delay-Solution for this element')
avasELatest = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasELatest.setStatus('mandatory')
if mibBuilder.loadTexts: avasELatest.setDescription('Latest Start/ Latest Occure')
avasEJva = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEJva.setStatus('mandatory')
if mibBuilder.loadTexts: avasEJva.setDescription('Name of the Condition-JV')
avasEJvaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 3, 7, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasEJvaValue.setStatus('mandatory')
if mibBuilder.loadTexts: avasEJvaValue.setDescription('Value of the Condition-JV')
avasCFlag = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("all", 1), ("free", 2), ("error", 3), ("share", 4), ("exclusiv", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avasCFlag.setStatus('mandatory')
if mibBuilder.loadTexts: avasCFlag.setDescription('Flag for restriction in Show Table')
avasCNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCNum.setStatus('mandatory')
if mibBuilder.loadTexts: avasCNum.setDescription('The number of entries in the table avasCTab')
avasCTab = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3), )
if mibBuilder.loadTexts: avasCTab.setStatus('mandatory')
if mibBuilder.loadTexts: avasCTab.setDescription('The AVAS Condition table')
avasCTabEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1), ).setIndexNames((0, "AVAS-MIB", "avasCTabIndex"))
if mibBuilder.loadTexts: avasCTabEntry.setStatus('mandatory')
if mibBuilder.loadTexts: avasCTabEntry.setDescription('An entry in the AVAS Condition table')
avasCTabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCTabIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avasCTabIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of avasCTabNum')
avasCName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCName.setStatus('mandatory')
if mibBuilder.loadTexts: avasCName.setDescription('The Name of the Condition Description')
avasCType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("net", 1), ("job", 2), ("res", 3), ("val", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCType.setStatus('mandatory')
if mibBuilder.loadTexts: avasCType.setDescription('The Type of the Condition Description')
avasCInd = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCInd.setStatus('mandatory')
if mibBuilder.loadTexts: avasCInd.setDescription('The Index of the Element')
avasCState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2), ("ended", 3), ("abended", 4), ("free", 5), ("error", 6), ("ignored", 7), ("no-plan", 8), ("no-submit", 9), ("skipped", 10), ("shared", 11), ("exclusiv", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCState.setStatus('mandatory')
if mibBuilder.loadTexts: avasCState.setDescription('The State of the Condition')
avasCValue = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("created", 1), ("ended", 2), ("abended", 3), ("ignored", 4), ("free", 5), ("error", 6), ("deleted", 7), ("no-plan", 8), ("no-submit", 9), ("skipped", 10), ("shared", 11), ("exclusiv", 12), ("value", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCValue.setStatus('mandatory')
if mibBuilder.loadTexts: avasCValue.setDescription('The Value of the Condition')
avasCCreateBy = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCCreateBy.setStatus('mandatory')
if mibBuilder.loadTexts: avasCCreateBy.setDescription('The Condition Description was created by ...')
avasCCreateDate = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCCreateDate.setStatus('mandatory')
if mibBuilder.loadTexts: avasCCreateDate.setDescription('Date of the Creation of Condition Description')
avasCUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCUpdate.setStatus('mandatory')
if mibBuilder.loadTexts: avasCUpdate.setDescription('Last Update of Condition Description')
avasCLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 24, 4, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasCLifeTime.setStatus('mandatory')
if mibBuilder.loadTexts: avasCLifeTime.setDescription('LifeTime of Condition Description')
avasagtVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 10, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasagtVersion.setStatus('mandatory')
if mibBuilder.loadTexts: avasagtVersion.setDescription('Version of Avas-Subagent')
avasSystemID = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 10, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasSystemID.setStatus('mandatory')
if mibBuilder.loadTexts: avasSystemID.setDescription('Avas-SystemID')
avasTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 1))
avasLastMsg = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avasLastMsg.setStatus('mandatory')
if mibBuilder.loadTexts: avasLastMsg.setDescription('Last Trap Message')
avasStateTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10))
avasMissing = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,301)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasMissing.setDescription('(UPAMZD || PLAMZD) not ready')
avasReady = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,302)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasReady.setDescription('(UPAMZD && PLAMZD) ready')
avasRunning = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,303)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasRunning.setDescription('min1 RCS (ready || running)')
avasErrorSystem = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,304)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasErrorSystem.setDescription('(UPAMZD || PLAMZD) abended')
avasErrorNet = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,305)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasErrorNet.setDescription('min1 net in error')
avasProblemNet = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,307)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasProblemNet.setDescription('min1 net in problem')
avasErrorSignon = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 10) + (0,350)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasErrorSignon.setDescription('SIGNON != ok')
avasProblemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11))
avasNetAbended = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,311)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasNetAbended.setDescription('Net abended')
avasNetError = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,312)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasNetError.setDescription('Net error')
avasNetRestarted = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,313)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasNetRestarted.setDescription('Net Restarted')
avasNetCancelled = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,314)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasNetCancelled.setDescription('Net Cancelled')
avasJobAbended = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,321)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasJobAbended.setDescription('Job abended')
avasJobError = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,322)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasJobError.setDescription('Job error')
avasJobRestarted = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,323)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasJobRestarted.setDescription('Job restarted')
avasJobCancelled = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,324)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasJobCancelled.setDescription('Job cancelled')
avasProcAbended = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,331)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasProcAbended.setDescription('Procedure abended')
avasProcError = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,332)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasProcError.setDescription('Procedure error')
avasProcRestarted = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,333)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasProcRestarted.setDescription('Procedure restarted')
avasProcCancelled = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,334)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasProcCancelled.setDescription('Procedure cancelled')
avasUJobAbended = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,341)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasUJobAbended.setDescription('Unix or NT Job abended')
avasUJobError = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,342)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasUJobError.setDescription('Unix or NT Job error')
avasUJobRestarted = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,343)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasUJobRestarted.setDescription('Unix or NT Job restarted')
avasUJobCancelled = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 24, 11, 11) + (0,344)).setObjects(("AVAS-MIB", "avasSystemID"), ("AVAS-MIB", "avasLastMsg"))
if mibBuilder.loadTexts: avasUJobCancelled.setDescription('Unix or NT Job cancelled')
mibBuilder.exportSymbols("AVAS-MIB", avasTrapData=avasTrapData, sniAVAS=sniAVAS, avasCTabIndex=avasCTabIndex, avasCTab=avasCTab, avasCUpdate=avasCUpdate, avasETabIndex=avasETabIndex, avasUJobAbended=avasUJobAbended, avasCName=avasCName, avasNName=avasNName, avasNStateOfHold=avasNStateOfHold, avasEFu=avasEFu, avasErrorSystem=avasErrorSystem, avasErrorSignon=avasErrorSignon, avasEDelSolution=avasEDelSolution, avasJobRestarted=avasJobRestarted, avasJobCancelled=avasJobCancelled, avasCCreateBy=avasCCreateBy, avasNStateOfCondwait=avasNStateOfCondwait, avasEState=avasEState, avasCInd=avasCInd, avasPAvakNum=avasPAvakNum, avasNText=avasNText, avasNetAbended=avasNetAbended, avasProcCancelled=avasProcCancelled, avasEInd=avasEInd, avasProcAbended=avasProcAbended, avasCTabEntry=avasCTabEntry, avasStateTraps=avasStateTraps, avasJobError=avasJobError, avasEName=avasEName, avasNAvak=avasNAvak, avasPPlamStat=avasPPlamStat, avasNStateOfError=avasNStateOfError, avasETabEntry=avasETabEntry, avasReady=avasReady, avasNNum=avasNNum, avasCValue=avasCValue, avasProcError=avasProcError, avasPAvakTabEntry=avasPAvakTabEntry, avasEJva=avasEJva, avasProblemTraps=avasProblemTraps, avasUJobCancelled=avasUJobCancelled, avasPAvakJvName=avasPAvakJvName, avasNStateF=avasNStateF, avasEETypeF=avasEETypeF, avasNetRestarted=avasNetRestarted, avasUJobError=avasUJobError, avasSystemID=avasSystemID, avasPSumStat=avasPSumStat, avasNState=avasNState, avasENet=avasENet, avasNStartedIndex=avasNStartedIndex, avasCState=avasCState, avasELatest=avasELatest, avasENStateF=avasENStateF, avasGlobalData=avasGlobalData, avasNetCancelled=avasNetCancelled, avasRunning=avasRunning, avasNTabIndex=avasNTabIndex, avasElem=avasElem, avasENum=avasENum, avasProcRestarted=avasProcRestarted, avasEEFuncF=avasEEFuncF, avasMissing=avasMissing, avasNPatF=avasNPatF, avasEType=avasEType, avasETab=avasETab, avasTraps=avasTraps, avasNetError=avasNetError, avasPAvakTabIndex=avasPAvakTabIndex, avasEJvaValue=avasEJvaValue, avasENPatF=avasENPatF, avasCFlag=avasCFlag, avasCond=avasCond, avasESynInd=avasESynInd, sniProductMibs=sniProductMibs, avasUJobRestarted=avasUJobRestarted, avasPAvakState=avasPAvakState, avasNTabEntry=avasNTabEntry, avasNTab=avasNTab, avasJobAbended=avasJobAbended, avasEEStateF=avasEEStateF, avasagtVersion=avasagtVersion, avasNet=avasNet, avasNStart=avasNStart, avasCNum=avasCNum, avasProc=avasProc, avasCType=avasCType, avasPCentrStat=avasPCentrStat, avasPAvakTab=avasPAvakTab, avasCCreateDate=avasCCreateDate, avasProblemNet=avasProblemNet, avasErrorNet=avasErrorNet, avasNStateOfRestart=avasNStateOfRestart, avasCLifeTime=avasCLifeTime, avasPUpamStat=avasPUpamStat, avasLastMsg=avasLastMsg, sni=sni)
