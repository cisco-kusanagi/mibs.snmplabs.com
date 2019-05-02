#
# PySNMP MIB module GDCMACRO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GDCMACRO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:37:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, TimeTicks, Integer32, Unsigned32, Gauge32, ModuleIdentity, ObjectIdentity, IpAddress, NotificationType, MibIdentifier, Counter32, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "TimeTicks", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gdc = MibIdentifier((1, 3, 6, 1, 4, 1, 498))
class SCinstance(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16842752, 33619968, 50397184, 67174400, 83951616, 100728832, 117506048, 134283264, 151060480, 167837696, 184614912, 201392128, 218169344, 234946560, 251723776, 258500992, 285278208, 302055424, 318832640, 335609856, 352387072, 369164288, 385941504, 402718720, 419495936, 436273152, 453050368, 469827584, 486604800, 503382016, 520159232, 536936448))
    namedValues = NamedValues(("slot1", 16842752), ("slot2", 33619968), ("slot3", 50397184), ("slot4", 67174400), ("slot5", 83951616), ("slot6", 100728832), ("slot7", 117506048), ("slot8", 134283264), ("slot9", 151060480), ("slot10", 167837696), ("slot11", 184614912), ("slot12", 201392128), ("slot13", 218169344), ("slot14", 234946560), ("slot15", 251723776), ("slot16", 258500992), ("slot17", 285278208), ("slot18", 302055424), ("slot19", 318832640), ("slot20", 335609856), ("slot21", 352387072), ("slot22", 369164288), ("slot23", 385941504), ("slot24", 402718720), ("slot25", 419495936), ("slot26", 436273152), ("slot27", 453050368), ("slot28", 469827584), ("slot29", 486604800), ("slot30", 503382016), ("slot31", 520159232), ("slot32", 536936448))

mibBuilder.exportSymbols("GDCMACRO-MIB", SCinstance=SCinstance, gdc=gdc)
