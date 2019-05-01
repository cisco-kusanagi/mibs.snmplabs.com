#
# PySNMP MIB module COM21-HCX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COM21-HCX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Unsigned32, Bits, TimeTicks, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, IpAddress, Integer32, Counter64, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Unsigned32", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "IpAddress", "Integer32", "Counter64", "NotificationType", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
com21 = MibIdentifier((1, 3, 6, 1, 4, 1, 1141))
com21Hcx = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2))
com21Stu = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 3))
com21Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 4))
com21Nmaps = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 5))
com21Reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 6))
class FrequencyKhz(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 800000)

class UpstrmFreqKhz(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(5000, 40000)

class Gain(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class StuGain(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(18, 58)

class EpochTime(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PrimServiceState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class Offset(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16383)

class AlarmSeverity(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5))

class Com21RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("create", 2), ("destroy", 3), ("deactive", 4))

mibBuilder.exportSymbols("COM21-HCX-MIB", FrequencyKhz=FrequencyKhz, Gain=Gain, AlarmSeverity=AlarmSeverity, UpstrmFreqKhz=UpstrmFreqKhz, Offset=Offset, com21Stu=com21Stu, com21=com21, Com21RowStatus=Com21RowStatus, com21Traps=com21Traps, com21Nmaps=com21Nmaps, com21Reg=com21Reg, StuGain=StuGain, PrimServiceState=PrimServiceState, EpochTime=EpochTime, com21Hcx=com21Hcx)
