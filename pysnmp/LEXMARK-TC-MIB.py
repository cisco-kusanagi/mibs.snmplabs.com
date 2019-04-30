#
# PySNMP MIB module LEXMARK-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEXMARK-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
lexmarkModules, = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmarkModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, iso, Counter64, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, IpAddress, Gauge32, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "iso", "Counter64", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lexmarkTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 2))
lexmarkTCMIB.setRevisions(('2010-12-20 23:00', '2009-11-24 20:40',))
if mibBuilder.loadTexts: lexmarkTCMIB.setLastUpdated('201012202300Z')
if mibBuilder.loadTexts: lexmarkTCMIB.setOrganization('Lexmark International, Inc.')
class UnitsTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 21, 22, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("items", 3), ("sides", 4), ("sheets", 5), ("millimeters", 16), ("centimeters", 17), ("meters", 18), ("inches", 19), ("feet", 20), ("grams", 21), ("ounces", 22), ("nanoseconds", 32), ("microseconds", 33), ("milliseconds", 34), ("seconds", 35), ("minutes", 36), ("hours", 37), ("days", 38), ("weeks", 39), ("months", 40), ("years", 41))

class PaperSizeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32, 33, 34, 35, 36, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 136, 137, 138, 139, 140, 141, 142))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("universal", 3), ("custom", 4), ("letter", 8), ("legal", 9), ("executive", 10), ("folio", 11), ("statement", 12), ("oficio", 13), ("tabloid", 14), ("businessCard", 15), ("idCard", 16), ("card3x5", 17), ("card4x6", 18), ("bookOriginal", 19), ("hagaki", 20), ("envelope7threequarters", 32), ("envelope9", 33), ("envelope10", 34), ("envelopeDL", 35), ("envelopeOther", 36), ("isoA0", 64), ("isoA1", 65), ("isoA2", 66), ("isoA3", 67), ("isoA4", 68), ("isoA5", 69), ("isoA6", 70), ("isoB0", 72), ("isoB1", 73), ("isoB2", 74), ("isoB3", 75), ("isoB4", 76), ("isoB5", 77), ("isoB6", 78), ("isoC0", 80), ("isoC1", 81), ("isoC2", 82), ("isoC3", 83), ("isoC4", 84), ("isoC5", 85), ("isoC6", 86), ("isoEnvelopeA0", 96), ("isoEnvelopeA1", 97), ("isoEnvelopeA2", 98), ("isoEnvelopeA3", 99), ("isoEnvelopeA4", 100), ("isoEnvelopeA5", 101), ("isoEnvelopeA6", 102), ("isoEnvelopeB0", 104), ("isoEnvelopeB1", 105), ("isoEnvelopeB2", 106), ("isoEnvelopeB3", 107), ("isoEnvelopeB4", 108), ("isoEnvelopeB5", 109), ("isoEnvelopeB6", 110), ("isoEnvelopeC0", 112), ("isoEnvelopeC1", 113), ("isoEnvelopeC2", 114), ("isoEnvelopeC3", 115), ("isoEnvelopeC4", 116), ("isoEnvelopeC5", 117), ("isoEnvelopeC6", 118), ("jisB0", 136), ("jisB1", 137), ("jisB2", 138), ("jisB3", 139), ("jisB4", 140), ("jisB5", 141), ("jisB6", 142))

class PaperTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 32, 33, 34, 35, 36, 37))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("plain", 3), ("cardstock", 4), ("transparancy", 5), ("recycled", 6), ("labels", 7), ("vinylLabels", 8), ("bond", 9), ("letterhead", 10), ("preprinted", 11), ("colored", 12), ("light", 13), ("heavy", 14), ("roughOrCotton", 15), ("envelope", 16), ("customtype1", 32), ("customtype2", 33), ("customtype3", 34), ("customtype4", 35), ("customtype5", 36), ("customtype6", 37))

class AdminStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("other", 3), ("up", 4), ("disabled", 5))

class StatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 22, 33, 34, 35, 36, 37, 38, 97, 98, 99, 100, 101, 102))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("ok", 3), ("offline", 4), ("warning", 5), ("broken", 6), ("disabledUnknown", 17), ("disabledOther", 18), ("disabledOk", 19), ("disabledOffline", 20), ("disabledWarning", 21), ("disabledBroken", 22), ("unlicensedUnknown", 33), ("unlicensedOther", 34), ("unlicensedOk", 35), ("unlicensedOffline", 36), ("unlicensedWarning", 37), ("unlicensedBroken", 38), ("licensedUnknown", 97), ("licensedOther", 98), ("licensedOk", 99), ("licensedOffline", 100), ("licensedWarning", 101), ("licensedBroken", 102))

class KeyValueTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("LEXMARK-TC-MIB", PaperSizeTC=PaperSizeTC, lexmarkTCMIB=lexmarkTCMIB, UnitsTC=UnitsTC, StatusTC=StatusTC, AdminStatusTC=AdminStatusTC, PYSNMP_MODULE_ID=lexmarkTCMIB, KeyValueTC=KeyValueTC, PaperTypeTC=PaperTypeTC)
