#
# PySNMP MIB module SYMMCOMMON10M (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMON10M
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:08 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, Bits, TimeTicks, Counter32, NotificationType, IpAddress, iso, Integer32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "iso", "Integer32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmCommon10M = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4))
if mibBuilder.loadTexts: symmCommon10M.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: symmCommon10M.setOrganization('Symmetricom')
class EnaValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class TPModuleID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("sys", 1), ("imc", 2), ("ioc1", 3), ("ioc2", 4), ("exp0", 5), ("exp1", 6), ("exp2", 7), ("exp3", 8), ("exp4", 9), ("exp5", 10), ("exp6", 11), ("exp7", 12), ("exp8", 13), ("exp9", 14))

class OnValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class TPInputPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16)

class InputFrameType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("freq1544khz", 1), ("freq2048khz", 2), ("ccs", 3), ("cas", 4), ("d4", 5), ("esf", 6))

class TPSSMValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

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

class TableRowChange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("add", 1), ("delete", 2), ("modify", 3))

class PPS10MOutGenMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("squelch", 1), ("on", 2))

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

tenMInput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 1))
tenMInputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 1, 1))
tenMInputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 1, 2))
tenMOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 2))
tenMOutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 2, 1))
tenMOutputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 2, 2))
tenMInOutConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 3))
if mibBuilder.loadTexts: tenMInOutConformance.setStatus('current')
tenMInOutCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 3, 1))
tenMInOutUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 4, 3, 2))
mibBuilder.exportSymbols("SYMMCOMMON10M", PPS10MOutGenMode=PPS10MOutGenMode, ActiveValue=ActiveValue, TPSSMValue=TPSSMValue, tenMInputStatus=tenMInputStatus, tenMInputConfig=tenMInputConfig, tenMInOutCompliances=tenMInOutCompliances, tenMOutputStatus=tenMOutputStatus, TableRowChange=TableRowChange, InputQualityLevel=InputQualityLevel, TLatAndLon=TLatAndLon, tenMInOutConformance=tenMInOutConformance, tenMOutputConfig=tenMOutputConfig, InputFrameType=InputFrameType, TPModuleID=TPModuleID, EnaValue=EnaValue, TLocalTimeOffset=TLocalTimeOffset, OutputFrameType=OutputFrameType, YesValue=YesValue, TPOutputGeneration=TPOutputGeneration, tenMOutput=tenMOutput, PYSNMP_MODULE_ID=symmCommon10M, TSsm=TSsm, tenMInput=tenMInput, OkValue=OkValue, OnValue=OnValue, symmCommon10M=symmCommon10M, TPOutputType=TPOutputType, TAntHeight=TAntHeight, InputPriority=InputPriority, OpMode=OpMode, DateAndTime=DateAndTime, tenMInOutUocGroups=tenMInOutUocGroups, ActionApply=ActionApply, TPInputPriority=TPInputPriority, ValidValue=ValidValue)
