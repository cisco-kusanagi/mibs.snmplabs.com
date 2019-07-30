#
# PySNMP MIB module SYMMCOMMONPPSTOD (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMONPPSTOD
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:15 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, NotificationType, MibIdentifier, TimeTicks, Bits, Gauge32, ObjectIdentity, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "Gauge32", "ObjectIdentity", "Integer32", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmPPSTOD = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3))
if mibBuilder.loadTexts: symmPPSTOD.setLastUpdated('201509301433Z')
if mibBuilder.loadTexts: symmPPSTOD.setOrganization('Symmetricom')
class EnaValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class TODPortType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("normal", 1), ("error", 2))

class TPModuleID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("sys", 1), ("imc", 2), ("ioc1", 3), ("ioc2", 4), ("exp0", 5), ("exp1", 6), ("exp2", 7), ("exp3", 8), ("exp4", 9), ("exp5", 10), ("exp6", 11), ("exp7", 12), ("exp8", 13), ("exp9", 14))

class OnValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class TPOutputType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("outputGeneral", 1), ("output10Mhz", 2), ("outputPPS", 3))

class TPOutputGeneration(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("warmup", 1), ("freerun", 2), ("fastlock", 3), ("normal", 4))

class OutputFrameType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("freq1544khz", 1), ("freq2048khz", 2), ("ccs", 3), ("cas", 4), ("d4", 5), ("esf", 6))

class ActionApply(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("apply", 1), ("nonapply", 2))

class OpMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("manual", 2))

class ActiveValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class InputQualityLevel(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("prcprs", 1), ("unkstu", 2), ("typeiist2", 3), ("typei", 4), ("typevtnc", 5), ("typeiiist3e", 6), ("typeivst3", 7), ("opt3smc", 8), ("dus", 9))

class InputPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4)

class YesValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

class OkValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fault", 2))

class ValidValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valid", 1), ("invalid", 2), ("nurture", 3))

class TODInputFrameType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("chinaMobile", 1), ("ntp4", 2))

class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

ppstodInput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1))
ppstodInputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1))
ppstodInputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: ppstodInputStatusTable.setStatus('current')
ppstodInputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPPSTOD", "ppstodInputStatusIndex"))
if mibBuilder.loadTexts: ppstodInputStatusEntry.setStatus('current')
ppstodInputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: ppstodInputStatusIndex.setStatus('current')
ppstodInputPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 2), TODPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputPortStatus.setStatus('current')
ppstodInputPPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputPPSStatus.setStatus('current')
ppstodInputPhaseOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputPhaseOffset.setStatus('current')
ppstodInputClockSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputClockSourceType.setStatus('current')
ppstodInputClockSourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputClockSourceStatus.setStatus('current')
ppstodInputAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputAccuracy.setStatus('current')
ppstodInputAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputAlarm.setStatus('current')
ppstodInputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2))
ppstodInputTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1), )
if mibBuilder.loadTexts: ppstodInputTable.setStatus('current')
ppstodInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPPSTOD", "ppstodInputIndex"))
if mibBuilder.loadTexts: ppstodInputEntry.setStatus('current')
ppstodInputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ppstodInputIndex.setStatus('current')
ppstodInputCableDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ppstodInputCableDelay.setStatus('current')
ppstodInputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 6), TODInputFrameType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ppstodInputFormat.setStatus('current')
ppstodInputManualLeapSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ppstodInputManualLeapSeconds.setStatus('current')
ppstodOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2))
ppstodOutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2, 1))
ppstodOutputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2, 2))
ppstodConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3))
if mibBuilder.loadTexts: ppstodConformance.setStatus('current')
ppstodCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 1))
ppstodBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 1, 1)).setObjects(("SYMMCOMMONPPSTOD", "ppstodInputConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppstodBasicCompliance = ppstodBasicCompliance.setStatus('current')
ppstodUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 2))
ppstodInputConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 2, 1)).setObjects(("SYMMCOMMONPPSTOD", "ppstodInputCableDelay"), ("SYMMCOMMONPPSTOD", "ppstodInputFormat"), ("SYMMCOMMONPPSTOD", "ppstodInputManualLeapSeconds"), ("SYMMCOMMONPPSTOD", "ppstodInputPortStatus"), ("SYMMCOMMONPPSTOD", "ppstodInputPPSStatus"), ("SYMMCOMMONPPSTOD", "ppstodInputClockSourceType"), ("SYMMCOMMONPPSTOD", "ppstodInputPhaseOffset"), ("SYMMCOMMONPPSTOD", "ppstodInputClockSourceStatus"), ("SYMMCOMMONPPSTOD", "ppstodInputAccuracy"), ("SYMMCOMMONPPSTOD", "ppstodInputAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppstodInputConfigGroup = ppstodInputConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMCOMMONPPSTOD", ppstodInputStatusIndex=ppstodInputStatusIndex, ppstodOutputStatus=ppstodOutputStatus, ppstodConformance=ppstodConformance, ActiveValue=ActiveValue, ppstodInputPhaseOffset=ppstodInputPhaseOffset, TPOutputGeneration=TPOutputGeneration, OpMode=OpMode, ppstodInputPPSStatus=ppstodInputPPSStatus, DateAndTime=DateAndTime, TPModuleID=TPModuleID, ActionApply=ActionApply, ppstodInputStatus=ppstodInputStatus, ppstodInputIndex=ppstodInputIndex, ppstodInputStatusEntry=ppstodInputStatusEntry, TSsm=TSsm, InputPriority=InputPriority, ppstodInputAccuracy=ppstodInputAccuracy, TAntHeight=TAntHeight, ppstodInputEntry=ppstodInputEntry, ppstodOutputConfig=ppstodOutputConfig, OutputFrameType=OutputFrameType, symmPPSTOD=symmPPSTOD, TODPortType=TODPortType, TODInputFrameType=TODInputFrameType, ppstodInputStatusTable=ppstodInputStatusTable, TLocalTimeOffset=TLocalTimeOffset, ppstodInputManualLeapSeconds=ppstodInputManualLeapSeconds, ppstodUocGroups=ppstodUocGroups, PYSNMP_MODULE_ID=symmPPSTOD, ppstodInputConfigGroup=ppstodInputConfigGroup, ppstodBasicCompliance=ppstodBasicCompliance, OnValue=OnValue, ppstodCompliances=ppstodCompliances, ValidValue=ValidValue, ppstodInputConfig=ppstodInputConfig, OkValue=OkValue, TLatAndLon=TLatAndLon, ppstodOutput=ppstodOutput, TPOutputType=TPOutputType, ppstodInputAlarm=ppstodInputAlarm, EnaValue=EnaValue, ppstodInputClockSourceStatus=ppstodInputClockSourceStatus, ppstodInputFormat=ppstodInputFormat, ppstodInput=ppstodInput, YesValue=YesValue, ppstodInputPortStatus=ppstodInputPortStatus, ppstodInputCableDelay=ppstodInputCableDelay, ppstodInputTable=ppstodInputTable, InputQualityLevel=InputQualityLevel, ppstodInputClockSourceType=ppstodInputClockSourceType)
