#
# PySNMP MIB module A3COM-HUAWEI-VO-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VO-TYPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, ObjectIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, MibIdentifier, Counter64, Unsigned32, Bits, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "Unsigned32", "Bits", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class CodecType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("g711a", 1), ("g711u", 2), ("g723r53", 3), ("g723r63", 4), ("g729r8", 5), ("g729a", 6), ("g726r16", 7), ("g726r24", 8), ("g726r32", 9), ("g726r40", 10))

mibBuilder.exportSymbols("A3COM-HUAWEI-VO-TYPE-MIB", CodecType=CodecType)
