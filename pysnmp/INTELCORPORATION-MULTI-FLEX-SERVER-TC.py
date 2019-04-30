#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
regModule, = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "regModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Gauge32, ObjectIdentity, Bits, MibIdentifier, Unsigned32, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
multiFlexServerTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 2))
multiFlexServerTcModule.setRevisions(('2008-05-28 02:00', '2008-05-07 02:40', '2007-08-16 13:30', '2007-08-15 19:00', '2007-07-10 17:00', '2007-06-07 20:30', '2007-06-07 13:30', '2007-05-23 19:00', '2007-05-21 12:00', '2007-03-12 18:30', '2007-02-22 17:00', '2007-01-05 10:50', '2006-12-28 13:10', '2006-11-07 07:01',))
if mibBuilder.loadTexts: multiFlexServerTcModule.setLastUpdated('200805280200Z')
if mibBuilder.loadTexts: multiFlexServerTcModule.setOrganization('Intel Corporation')
class Index(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class INT32withException(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16))

class PowerLedStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -4, -1, 0, 1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("identify", -4), ("dataNotAvailable", -1), ("off", 0), ("standby", 1), ("on", 2), ("forcedOff", 3), ("hardReset", 4))

class FaultLedStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -4, -1, 0, 1, 2))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("identify", -4), ("dataNotAvailable", -1), ("normal", 0), ("degraded", 1), ("fault", 2))

class PresenceLedStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -3, -1, 0, 15, 30, 60, 120))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("alwaysOn", -3), ("dataNotAvailable", -1), ("off", 0), ("fifteenSeconds", 15), ("thirtySeconds", 30), ("sixtySeconds", 60), ("twoMinutes", 120))

class FeatureSet(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, 0, 1))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("unsupported", 0), ("supported", 1))

class Presence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -4, -2, 0, 1))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("identify", -4), ("timedout", -2), ("absent", 0), ("present", 1))

class Power(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0))
    namedValues = NamedValues(("unknown", -1), ("passive", 0))

class IdromBinary16(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class JackType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("other", 1), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14))

class TimeFilter(TextualConvention, TimeTicks):
    status = 'current'

class PortList(TextualConvention, OctetString):
    status = 'current'

class VlanIndex(TextualConvention, Unsigned32):
    status = 'current'

class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-TC", Power=Power, EnabledStatus=EnabledStatus, PYSNMP_MODULE_ID=multiFlexServerTcModule, PowerLedStates=PowerLedStates, PortList=PortList, TimeFilter=TimeFilter, multiFlexServerTcModule=multiFlexServerTcModule, FeatureSet=FeatureSet, JackType=JackType, VlanIndex=VlanIndex, FaultLedStates=FaultLedStates, INT32withException=INT32withException, IdromBinary16=IdromBinary16, Presence=Presence, PresenceLedStates=PresenceLedStates, Index=Index)
