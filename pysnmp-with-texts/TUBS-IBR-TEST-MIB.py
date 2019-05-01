#
# PySNMP MIB module TUBS-IBR-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-TEST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, TimeTicks, Bits, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, IpAddress, ObjectIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "TimeTicks", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
testMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 7))
testMIB.setRevisions(('2000-02-09 00:00', '1998-10-09 17:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: testMIB.setRevisionsDescriptions(('Updated IMPORTS and minor stylistic fixes.', 'The initial revision of this module.',))
if mibBuilder.loadTexts: testMIB.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: testMIB.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: testMIB.setContactInfo('Juergen Schoenwaelder TU Braunschweig Bueltenweg 74/75 38106 Braunschweig Germany Tel: +49 531 391 3283 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: testMIB.setDescription('A MIB module which is only used for testing purposes.')
class OctalValue(TextualConvention, Integer32):
    description = 'This TC is used to test DISPLAY-HINT interpretation. It is not intended to be used in any OBJECT-TYPE definition.'
    status = 'current'
    displayHint = 'o'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class HexValue(TextualConvention, Integer32):
    description = 'This TC is used to test DISPLAY-HINT interpretation. It is not intended to be used in any OBJECT-TYPE definition.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BinaryValue(TextualConvention, Integer32):
    description = 'This TC is used to test DISPLAY-HINT interpretation. It is not intended to be used in any OBJECT-TYPE definition.'
    status = 'current'
    displayHint = 'b'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Dot3Value(TextualConvention, Integer32):
    description = 'This TC is used to test DISPLAY-HINT interpretation. It is not intended to be used in any OBJECT-TYPE definition.'
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NumValue(TextualConvention, OctetString):
    description = 'This TC is used to test DISPLAY-HINT interpretation. It is not intended to be used in any OBJECT-TYPE definition.'
    status = 'current'
    displayHint = '1d-1x-1o-1b'

mibBuilder.exportSymbols("TUBS-IBR-TEST-MIB", testMIB=testMIB, NumValue=NumValue, OctalValue=OctalValue, BinaryValue=BinaryValue, PYSNMP_MODULE_ID=testMIB, Dot3Value=Dot3Value, HexValue=HexValue)
