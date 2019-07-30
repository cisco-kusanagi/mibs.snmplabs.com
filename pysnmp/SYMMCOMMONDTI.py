#
# PySNMP MIB module SYMMCOMMONDTI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMCOMMONDTI
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:10 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, iso, ModuleIdentity, NotificationType, Gauge32, IpAddress, Unsigned32, Bits, Integer32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "iso", "ModuleIdentity", "NotificationType", "Gauge32", "IpAddress", "Unsigned32", "Bits", "Integer32", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmDti = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7))
if mibBuilder.loadTexts: symmDti.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: symmDti.setOrganization('Symmetricom')
class EnaValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class TPModuleID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("sys", 1), ("imc", 2), ("ioc1", 3), ("ioc2", 4), ("exp0", 5), ("exp1", 6), ("exp2", 7), ("exp3", 8), ("exp4", 9), ("exp5", 10), ("exp6", 11), ("exp7", 12), ("exp8", 13), ("exp9", 14))

class OnValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

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

class DTIPortID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dtiin1", 1), ("dtiin2", 2), ("dtiout1", 3), ("dtiout2", 4))

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

dtiStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 1))
dtiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 2))
dtiConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 3))
if mibBuilder.loadTexts: dtiConformance.setStatus('current')
dtiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 3, 1))
dtiUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 7, 3, 2))
mibBuilder.exportSymbols("SYMMCOMMONDTI", TableRowChange=TableRowChange, TAntHeight=TAntHeight, dtiCompliances=dtiCompliances, PYSNMP_MODULE_ID=symmDti, EnaValue=EnaValue, DTIPortID=DTIPortID, DateAndTime=DateAndTime, dtiUocGroups=dtiUocGroups, TLatAndLon=TLatAndLon, TPModuleID=TPModuleID, TSsm=TSsm, symmDti=symmDti, dtiConfig=dtiConfig, OnValue=OnValue, OpMode=OpMode, ValidValue=ValidValue, ActionApply=ActionApply, OkValue=OkValue, dtiConformance=dtiConformance, dtiStatus=dtiStatus, YesValue=YesValue, ActiveValue=ActiveValue, TLocalTimeOffset=TLocalTimeOffset, MasterValidValue=MasterValidValue)
