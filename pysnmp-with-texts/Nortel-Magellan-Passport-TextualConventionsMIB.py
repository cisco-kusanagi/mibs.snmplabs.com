#
# PySNMP MIB module Nortel-Magellan-Passport-TextualConventionsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-TextualConventionsMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:26:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
Integer32, Unsigned32 = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "Integer32", "Unsigned32")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Unsigned32, IpAddress, Counter32, Bits, iso, ModuleIdentity, Gauge32, ObjectIdentity, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Unsigned32", "IpAddress", "Counter32", "Bits", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
textualConventionsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2))
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

textualConventionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 1))
textualConventionsGroupBC = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 1, 3))
textualConventionsGroupBC02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 1, 3, 2))
textualConventionsGroupBC02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 1, 3, 2, 2))
textualConventionsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 3))
textualConventionsCapabilitiesBC = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 3, 3))
textualConventionsCapabilitiesBC02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 3, 3, 2))
textualConventionsCapabilitiesBC02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 2, 3, 3, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", WildcardedDigitString=WildcardedDigitString, textualConventionsGroupBC=textualConventionsGroupBC, FixedPoint1=FixedPoint1, textualConventionsCapabilities=textualConventionsCapabilities, Gauge64=Gauge64, Hex=Hex, textualConventionsCapabilitiesBC02=textualConventionsCapabilitiesBC02, IntegerSequence=IntegerSequence, FixedPoint3=FixedPoint3, FixedPoint8=FixedPoint8, FixedPoint9=FixedPoint9, FixedPoint4=FixedPoint4, AsciiStringIndex=AsciiStringIndex, AsciiString=AsciiString, FixedPoint2=FixedPoint2, textualConventionsCapabilitiesBC02A=textualConventionsCapabilitiesBC02A, textualConventionsGroup=textualConventionsGroup, DashedHexString=DashedHexString, FixedPoint7=FixedPoint7, FixedPoint5=FixedPoint5, Link=Link, FixedPoint6=FixedPoint6, textualConventionsGroupBC02A=textualConventionsGroupBC02A, textualConventionsGroupBC02=textualConventionsGroupBC02, ExtendedAsciiString=ExtendedAsciiString, EnterpriseDateAndTime=EnterpriseDateAndTime, textualConventionsCapabilitiesBC=textualConventionsCapabilitiesBC, HexString=HexString, DigitString=DigitString, NonReplicated=NonReplicated, Unsigned64=Unsigned64, textualConventionsMIB=textualConventionsMIB)
