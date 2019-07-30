#
# PySNMP MIB module SYMMCOMMONPPSTOD (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMONPPSTOD
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:54 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, TimeTicks, ObjectIdentity, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, Bits, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ObjectIdentity", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Bits", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmPPSTOD = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3))
if mibBuilder.loadTexts: symmPPSTOD.setLastUpdated('201509301433Z')
if mibBuilder.loadTexts: symmPPSTOD.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmPPSTOD.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com ')
if mibBuilder.loadTexts: symmPPSTOD.setDescription('Symmetricom, Inc. Common PPS/TOD input/output status and configuration ')
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
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

ppstodInput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1))
ppstodInputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1))
ppstodInputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: ppstodInputStatusTable.setStatus('current')
if mibBuilder.loadTexts: ppstodInputStatusTable.setDescription('Description.')
ppstodInputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPPSTOD", "ppstodInputStatusIndex"))
if mibBuilder.loadTexts: ppstodInputStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ppstodInputStatusEntry.setDescription('Description.')
ppstodInputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: ppstodInputStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ppstodInputStatusIndex.setDescription('Description.')
ppstodInputPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 2), TODPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputPortStatus.setStatus('current')
if mibBuilder.loadTexts: ppstodInputPortStatus.setDescription('Description.')
ppstodInputPPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputPPSStatus.setStatus('current')
if mibBuilder.loadTexts: ppstodInputPPSStatus.setDescription('Description.')
ppstodInputPhaseOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputPhaseOffset.setStatus('current')
if mibBuilder.loadTexts: ppstodInputPhaseOffset.setDescription('Description.')
ppstodInputClockSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputClockSourceType.setStatus('current')
if mibBuilder.loadTexts: ppstodInputClockSourceType.setDescription('Description.')
ppstodInputClockSourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputClockSourceStatus.setStatus('current')
if mibBuilder.loadTexts: ppstodInputClockSourceStatus.setDescription('Description.')
ppstodInputAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputAccuracy.setStatus('current')
if mibBuilder.loadTexts: ppstodInputAccuracy.setDescription('Description.')
ppstodInputAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ppstodInputAlarm.setStatus('current')
if mibBuilder.loadTexts: ppstodInputAlarm.setDescription('Description.')
ppstodInputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2))
ppstodInputTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1), )
if mibBuilder.loadTexts: ppstodInputTable.setStatus('current')
if mibBuilder.loadTexts: ppstodInputTable.setDescription('The pps-tod configuration table.')
ppstodInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMCOMMONPPSTOD", "ppstodInputIndex"))
if mibBuilder.loadTexts: ppstodInputEntry.setStatus('current')
if mibBuilder.loadTexts: ppstodInputEntry.setDescription('The entry of pps-tod table.')
ppstodInputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ppstodInputIndex.setStatus('current')
if mibBuilder.loadTexts: ppstodInputIndex.setDescription('Description.')
ppstodInputCableDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ppstodInputCableDelay.setStatus('current')
if mibBuilder.loadTexts: ppstodInputCableDelay.setDescription('The input cable delay value. The valid setting is 0-999999. ')
ppstodInputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 6), TODInputFrameType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ppstodInputFormat.setStatus('current')
if mibBuilder.loadTexts: ppstodInputFormat.setDescription('TOD input format can be following chinaMobile(1) NTP-4(2) NotAvailable(0)')
ppstodInputManualLeapSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ppstodInputManualLeapSeconds.setStatus('current')
if mibBuilder.loadTexts: ppstodInputManualLeapSeconds.setDescription('ManualLeap second')
ppstodOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2))
ppstodOutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2, 1))
ppstodOutputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 2, 2))
ppstodConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3))
if mibBuilder.loadTexts: ppstodConformance.setStatus('current')
if mibBuilder.loadTexts: ppstodConformance.setDescription('This subtree contains conformance statements for the Symmetricom PPS-TOD MIB. ')
ppstodCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 1))
ppstodBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 1, 1)).setObjects(("SYMMCOMMONPPSTOD", "ppstodInputConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppstodBasicCompliance = ppstodBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: ppstodBasicCompliance.setDescription('The compliance statement for SNMP entities which have PPS-TOD status and configuration of input/output.')
ppstodUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 2))
ppstodInputConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 3, 3, 2, 1)).setObjects(("SYMMCOMMONPPSTOD", "ppstodInputCableDelay"), ("SYMMCOMMONPPSTOD", "ppstodInputFormat"), ("SYMMCOMMONPPSTOD", "ppstodInputManualLeapSeconds"), ("SYMMCOMMONPPSTOD", "ppstodInputPortStatus"), ("SYMMCOMMONPPSTOD", "ppstodInputPPSStatus"), ("SYMMCOMMONPPSTOD", "ppstodInputClockSourceType"), ("SYMMCOMMONPPSTOD", "ppstodInputPhaseOffset"), ("SYMMCOMMONPPSTOD", "ppstodInputClockSourceStatus"), ("SYMMCOMMONPPSTOD", "ppstodInputAccuracy"), ("SYMMCOMMONPPSTOD", "ppstodInputAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ppstodInputConfigGroup = ppstodInputConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ppstodInputConfigGroup.setDescription('A collection of objects providing information applicable to PPS-TOD configuration group.')
mibBuilder.exportSymbols("SYMMCOMMONPPSTOD", ppstodInputStatus=ppstodInputStatus, ppstodOutputConfig=ppstodOutputConfig, TPOutputGeneration=TPOutputGeneration, TAntHeight=TAntHeight, YesValue=YesValue, TODInputFrameType=TODInputFrameType, OkValue=OkValue, TPOutputType=TPOutputType, ppstodInputManualLeapSeconds=ppstodInputManualLeapSeconds, ActiveValue=ActiveValue, EnaValue=EnaValue, TLatAndLon=TLatAndLon, ppstodInputPPSStatus=ppstodInputPPSStatus, ppstodInputTable=ppstodInputTable, symmPPSTOD=symmPPSTOD, ppstodInputStatusEntry=ppstodInputStatusEntry, ppstodInputAlarm=ppstodInputAlarm, ppstodInputClockSourceType=ppstodInputClockSourceType, TPModuleID=TPModuleID, ppstodOutputStatus=ppstodOutputStatus, ppstodCompliances=ppstodCompliances, TLocalTimeOffset=TLocalTimeOffset, InputQualityLevel=InputQualityLevel, TSsm=TSsm, OpMode=OpMode, ppstodInputPhaseOffset=ppstodInputPhaseOffset, ppstodInputAccuracy=ppstodInputAccuracy, ppstodInputFormat=ppstodInputFormat, ppstodUocGroups=ppstodUocGroups, ppstodInputIndex=ppstodInputIndex, ppstodInputStatusIndex=ppstodInputStatusIndex, ppstodOutput=ppstodOutput, OnValue=OnValue, ppstodInputClockSourceStatus=ppstodInputClockSourceStatus, PYSNMP_MODULE_ID=symmPPSTOD, ppstodInputConfig=ppstodInputConfig, ppstodInputPortStatus=ppstodInputPortStatus, ppstodInputConfigGroup=ppstodInputConfigGroup, TODPortType=TODPortType, ppstodBasicCompliance=ppstodBasicCompliance, ppstodInput=ppstodInput, ppstodConformance=ppstodConformance, ActionApply=ActionApply, ppstodInputEntry=ppstodInputEntry, OutputFrameType=OutputFrameType, ppstodInputCableDelay=ppstodInputCableDelay, InputPriority=InputPriority, ValidValue=ValidValue, DateAndTime=DateAndTime, ppstodInputStatusTable=ppstodInputStatusTable)
