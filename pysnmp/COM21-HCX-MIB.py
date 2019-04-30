#
# PySNMP MIB module COM21-HCX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COM21-HCX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, MibIdentifier, Unsigned32, ModuleIdentity, enterprises, ObjectIdentity, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "Unsigned32", "ModuleIdentity", "enterprises", "ObjectIdentity", "Bits", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("COM21-HCX-MIB", UpstrmFreqKhz=UpstrmFreqKhz, Gain=Gain, AlarmSeverity=AlarmSeverity, Offset=Offset, Com21RowStatus=Com21RowStatus, PrimServiceState=PrimServiceState, StuGain=StuGain, EpochTime=EpochTime, com21Traps=com21Traps, com21Hcx=com21Hcx, com21=com21, com21Nmaps=com21Nmaps, FrequencyKhz=FrequencyKhz, com21Stu=com21Stu, com21Reg=com21Reg)
