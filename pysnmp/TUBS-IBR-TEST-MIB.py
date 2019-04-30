#
# PySNMP MIB module TUBS-IBR-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-TEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, iso, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, Counter64, Unsigned32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "iso", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "Counter64", "Unsigned32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
testMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 7))
testMIB.setRevisions(('2000-02-09 00:00', '1998-10-09 17:11',))
if mibBuilder.loadTexts: testMIB.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: testMIB.setOrganization('TU Braunschweig')
class OctalValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'o'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class HexValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BinaryValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'b'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Dot3Value(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NumValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d-1x-1o-1b'

mibBuilder.exportSymbols("TUBS-IBR-TEST-MIB", BinaryValue=BinaryValue, testMIB=testMIB, PYSNMP_MODULE_ID=testMIB, OctalValue=OctalValue, Dot3Value=Dot3Value, NumValue=NumValue, HexValue=HexValue)
