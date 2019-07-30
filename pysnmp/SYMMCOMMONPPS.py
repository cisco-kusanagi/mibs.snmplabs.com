#
# PySNMP MIB module SYMMCOMMONPPS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMONPPS
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:13 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Integer32, MibIdentifier, IpAddress, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Unsigned32, ObjectIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Integer32", "MibIdentifier", "IpAddress", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmPPS = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5))
if mibBuilder.loadTexts: symmPPS.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: symmPPS.setOrganization('Symmetricom')
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

class MasterValidValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

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

ppsInput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 1))
ppsInputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 1, 1))
ppsInputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 1, 2))
ppsOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 2))
ppsOutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 2, 1))
ppsOutputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 2, 2))
ppsConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 3))
if mibBuilder.loadTexts: ppsConformance.setStatus('current')
ppsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 3, 1))
ppsUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 5, 3, 2))
mibBuilder.exportSymbols("SYMMCOMMONPPS", TPSSMValue=TPSSMValue, OutputFrameType=OutputFrameType, PPS10MOutGenMode=PPS10MOutGenMode, ppsOutput=ppsOutput, ActionApply=ActionApply, ppsInput=ppsInput, ValidValue=ValidValue, ppsConformance=ppsConformance, TPOutputType=TPOutputType, TLocalTimeOffset=TLocalTimeOffset, ppsInputStatus=ppsInputStatus, YesValue=YesValue, InputFrameType=InputFrameType, DateAndTime=DateAndTime, OpMode=OpMode, symmPPS=symmPPS, EnaValue=EnaValue, TPModuleID=TPModuleID, ppsUocGroups=ppsUocGroups, OnValue=OnValue, TPInputPriority=TPInputPriority, TPOutputGeneration=TPOutputGeneration, TSsm=TSsm, ppsCompliances=ppsCompliances, TableRowChange=TableRowChange, TLatAndLon=TLatAndLon, OkValue=OkValue, ppsInputConfig=ppsInputConfig, ppsOutputStatus=ppsOutputStatus, ppsOutputConfig=ppsOutputConfig, TAntHeight=TAntHeight, PYSNMP_MODULE_ID=symmPPS, ActiveValue=ActiveValue, MasterValidValue=MasterValidValue)
