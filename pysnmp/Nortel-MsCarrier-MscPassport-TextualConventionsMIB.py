#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-TextualConventionsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-TextualConventionsMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
Integer32, Unsigned32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "Integer32", "Unsigned32")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, Counter32, Unsigned32, Gauge32, Counter64, Integer32, iso, ModuleIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "Counter32", "Unsigned32", "Gauge32", "Counter64", "Integer32", "iso", "ModuleIdentity", "Bits", "NotificationType")
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
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", textualConventionsGroup=textualConventionsGroup, IntegerSequence=IntegerSequence, textualConventionsGroupCA01=textualConventionsGroupCA01, FixedPoint5=FixedPoint5, FixedPoint9=FixedPoint9, textualConventionsMIB=textualConventionsMIB, FixedPoint7=FixedPoint7, NonReplicated=NonReplicated, Hex=Hex, HexString=HexString, FixedPoint1=FixedPoint1, FixedPoint6=FixedPoint6, textualConventionsCapabilitiesCA01=textualConventionsCapabilitiesCA01, FixedPoint3=FixedPoint3, DigitString=DigitString, textualConventionsCapabilities=textualConventionsCapabilities, textualConventionsCapabilitiesCA=textualConventionsCapabilitiesCA, textualConventionsCapabilitiesCA01A=textualConventionsCapabilitiesCA01A, textualConventionsGroupCA=textualConventionsGroupCA, WildcardedDigitString=WildcardedDigitString, Gauge64=Gauge64, FixedPoint8=FixedPoint8, Unsigned64=Unsigned64, DashedHexString=DashedHexString, textualConventionsGroupCA01A=textualConventionsGroupCA01A, FixedPoint4=FixedPoint4, EnterpriseDateAndTime=EnterpriseDateAndTime, PassportCounter64=PassportCounter64, AsciiStringIndex=AsciiStringIndex, Link=Link, ExtendedAsciiString=ExtendedAsciiString, FixedPoint2=FixedPoint2, AsciiString=AsciiString)
