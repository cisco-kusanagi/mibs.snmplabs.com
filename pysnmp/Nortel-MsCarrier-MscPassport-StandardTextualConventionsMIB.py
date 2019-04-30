#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, MibIdentifier, ModuleIdentity, Counter32, Unsigned32, Gauge32, Counter64, iso, Integer32, IpAddress, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter32", "Unsigned32", "Gauge32", "Counter64", "iso", "Integer32", "IpAddress", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
standardTextualConventionsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6))
class Gauge32(Gauge32):
    pass

class Counter32(Counter32):
    pass

class Unsigned32(Gauge32):
    pass

class Integer32(Integer32):
    pass

class NsapAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(1, 1), ValueSizeConstraint(4, 21), )
class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class TestAndIncr(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AutonomousType(ObjectIdentifier):
    pass

class VariablePointer(ObjectIdentifier):
    pass

class RowPointer(ObjectIdentifier):
    pass

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class StorageType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("volatile", 2), ("nonVolatile", 3), ("permanent", 4), ("readOnly", 5))

class IANAifType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54))
    namedValues = NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("iso88023Csmacd", 7), ("iso88024TokenBus", 8), ("iso88025TokenRing", 9), ("iso88026Man", 10), ("starLan", 11), ("proteon10Mbit", 12), ("proteon80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26), ("nsip", 27), ("fslip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54))

class InterfaceIndex(Integer32):
    pass

class FddiTimeNano(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FddiTimeMilli(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FddiResourceId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class FddiSMTStationIdType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class FddiMACLongAddressType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

class DLCI(Integer32):
    pass

class AreaID(IpAddress):
    pass

class RouterID(IpAddress):
    pass

class Metric(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class BigMetric(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

class Status(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class Validation(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class HelloRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class UpToMaxAge(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3600)

class DesignatedRouterPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TOSType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 31)

class X121Address(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 17)

standardTextualConventionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1))
standardTextualConventionsGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1, 1))
standardTextualConventionsGroupCA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1, 1, 2))
standardTextualConventionsGroupCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1, 1, 2, 2))
standardTextualConventionsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3))
standardTextualConventionsCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3, 1))
standardTextualConventionsCapabilitiesCA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3, 1, 2))
standardTextualConventionsCapabilitiesCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3, 1, 2, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", MacAddress=MacAddress, RowStatus=RowStatus, TAddress=TAddress, BridgeId=BridgeId, HelloRange=HelloRange, Status=Status, standardTextualConventionsCapabilitiesCA01A=standardTextualConventionsCapabilitiesCA01A, standardTextualConventionsGroupCA=standardTextualConventionsGroupCA, FddiTimeMilli=FddiTimeMilli, NsapAddress=NsapAddress, standardTextualConventionsGroupCA01=standardTextualConventionsGroupCA01, Counter32=Counter32, InterfaceIndex=InterfaceIndex, standardTextualConventionsCapabilities=standardTextualConventionsCapabilities, BigMetric=BigMetric, Timeout=Timeout, DisplayString=DisplayString, TimeStamp=TimeStamp, PhysAddress=PhysAddress, AutonomousType=AutonomousType, StorageType=StorageType, VariablePointer=VariablePointer, FddiTimeNano=FddiTimeNano, TimeInterval=TimeInterval, Integer32=Integer32, Unsigned32=Unsigned32, FddiSMTStationIdType=FddiSMTStationIdType, Metric=Metric, TOSType=TOSType, IANAifType=IANAifType, UpToMaxAge=UpToMaxAge, standardTextualConventionsGroupCA01A=standardTextualConventionsGroupCA01A, DLCI=DLCI, DateAndTime=DateAndTime, TestAndIncr=TestAndIncr, standardTextualConventionsCapabilitiesCA=standardTextualConventionsCapabilitiesCA, FddiMACLongAddressType=FddiMACLongAddressType, standardTextualConventionsMIB=standardTextualConventionsMIB, FddiResourceId=FddiResourceId, standardTextualConventionsGroup=standardTextualConventionsGroup, RowPointer=RowPointer, DesignatedRouterPriority=DesignatedRouterPriority, Validation=Validation, Gauge32=Gauge32, TruthValue=TruthValue, X121Address=X121Address, RouterID=RouterID, standardTextualConventionsCapabilitiesCA01=standardTextualConventionsCapabilitiesCA01, AreaID=AreaID, PositiveInteger=PositiveInteger)
