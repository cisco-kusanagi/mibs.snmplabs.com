#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-TextualConventionsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-TextualConventionsMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:28:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
Unsigned32, Integer32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "Unsigned32", "Integer32")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Bits, iso, NotificationType, Counter64, MibIdentifier, Unsigned32, ModuleIdentity, Gauge32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Bits", "iso", "NotificationType", "Counter64", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Gauge32", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
textualConventionsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2))
class PassportCounter64(Counter32):
    pass

class Hex(Unsigned32):
    pass

class Gauge64(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Unsigned64(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class DigitString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class WildcardedDigitString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class HexString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class AsciiString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class ExtendedAsciiString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class DashedHexString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class EnterpriseDateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), ValueSizeConstraint(5, 5), ValueSizeConstraint(8, 8), ValueSizeConstraint(10, 10), ValueSizeConstraint(13, 13), ValueSizeConstraint(16, 16), ValueSizeConstraint(19, 19), )
class Link(ObjectIdentifier):
    pass

class IntegerSequence(OctetString):
    pass

class FixedPoint1(Unsigned32):
    pass

class FixedPoint2(Unsigned32):
    pass

class FixedPoint3(Unsigned32):
    pass

class FixedPoint4(Unsigned32):
    pass

class FixedPoint5(Unsigned32):
    pass

class FixedPoint6(Unsigned32):
    pass

class FixedPoint7(Unsigned32):
    pass

class FixedPoint8(Unsigned32):
    pass

class FixedPoint9(Unsigned32):
    pass

class AsciiStringIndex(OctetString):
    pass

class NonReplicated(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("present", 1))

textualConventionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1))
textualConventionsGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1, 1))
textualConventionsGroupCA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1, 1, 2))
textualConventionsGroupCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1, 1, 2, 2))
textualConventionsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3))
textualConventionsCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3, 1))
textualConventionsCapabilitiesCA01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3, 1, 2))
textualConventionsCapabilitiesCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3, 1, 2, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", FixedPoint4=FixedPoint4, AsciiString=AsciiString, textualConventionsGroupCA=textualConventionsGroupCA, AsciiStringIndex=AsciiStringIndex, FixedPoint9=FixedPoint9, EnterpriseDateAndTime=EnterpriseDateAndTime, WildcardedDigitString=WildcardedDigitString, FixedPoint8=FixedPoint8, textualConventionsCapabilities=textualConventionsCapabilities, textualConventionsCapabilitiesCA01=textualConventionsCapabilitiesCA01, Gauge64=Gauge64, textualConventionsGroup=textualConventionsGroup, FixedPoint1=FixedPoint1, Link=Link, Hex=Hex, DigitString=DigitString, textualConventionsCapabilitiesCA=textualConventionsCapabilitiesCA, FixedPoint2=FixedPoint2, IntegerSequence=IntegerSequence, textualConventionsGroupCA01A=textualConventionsGroupCA01A, Unsigned64=Unsigned64, textualConventionsCapabilitiesCA01A=textualConventionsCapabilitiesCA01A, textualConventionsMIB=textualConventionsMIB, HexString=HexString, FixedPoint5=FixedPoint5, FixedPoint6=FixedPoint6, FixedPoint3=FixedPoint3, DashedHexString=DashedHexString, ExtendedAsciiString=ExtendedAsciiString, NonReplicated=NonReplicated, textualConventionsGroupCA01=textualConventionsGroupCA01, PassportCounter64=PassportCounter64, FixedPoint7=FixedPoint7)
