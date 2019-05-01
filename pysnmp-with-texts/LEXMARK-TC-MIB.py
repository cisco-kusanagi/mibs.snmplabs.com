#
# PySNMP MIB module LEXMARK-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEXMARK-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
lexmarkModules, = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmarkModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, NotificationType, ObjectIdentity, Counter64, Integer32, Counter32, iso, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "NotificationType", "ObjectIdentity", "Counter64", "Integer32", "Counter32", "iso", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lexmarkTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 2))
lexmarkTCMIB.setRevisions(('2010-12-20 23:00', '2009-11-24 20:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lexmarkTCMIB.setRevisionsDescriptions(('Version 1.0.0 of the LEXMARK-TC-MIB', 'Version 0.0.1 Initial release of LEXMARK-TC-MIB',))
if mibBuilder.loadTexts: lexmarkTCMIB.setLastUpdated('201012202300Z')
if mibBuilder.loadTexts: lexmarkTCMIB.setOrganization('Lexmark International, Inc.')
if mibBuilder.loadTexts: lexmarkTCMIB.setContactInfo('snmpmib@lexmark.com')
if mibBuilder.loadTexts: lexmarkTCMIB.setDescription('Textual conventions and enumerations used by Lexmark MIBs Copyright 2009 Lexmark International')
class UnitsTC(TextualConvention, Integer32):
    description = 'Units of measure used by the corresponding counter'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 21, 22, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("items", 3), ("sides", 4), ("sheets", 5), ("millimeters", 16), ("centimeters", 17), ("meters", 18), ("inches", 19), ("feet", 20), ("grams", 21), ("ounces", 22), ("nanoseconds", 32), ("microseconds", 33), ("milliseconds", 34), ("seconds", 35), ("minutes", 36), ("hours", 37), ("days", 38), ("weeks", 39), ("months", 40), ("years", 41))

class PaperSizeTC(TextualConvention, Integer32):
    description = 'Paper sizes. bit 5 - envelope bit 6 - ISO size bit 7 - JIS size 1 -> 31 - US Papers 32 -> 63 - US Envelopes 64 -> 95 - ISO papers 96 -> 127 - ISO envelopes 128 -> 160 - JIS papers 161 -> 192 - JIS envelopes '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32, 33, 34, 35, 36, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 136, 137, 138, 139, 140, 141, 142))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("universal", 3), ("custom", 4), ("letter", 8), ("legal", 9), ("executive", 10), ("folio", 11), ("statement", 12), ("oficio", 13), ("tabloid", 14), ("businessCard", 15), ("idCard", 16), ("card3x5", 17), ("card4x6", 18), ("bookOriginal", 19), ("hagaki", 20), ("envelope7threequarters", 32), ("envelope9", 33), ("envelope10", 34), ("envelopeDL", 35), ("envelopeOther", 36), ("isoA0", 64), ("isoA1", 65), ("isoA2", 66), ("isoA3", 67), ("isoA4", 68), ("isoA5", 69), ("isoA6", 70), ("isoB0", 72), ("isoB1", 73), ("isoB2", 74), ("isoB3", 75), ("isoB4", 76), ("isoB5", 77), ("isoB6", 78), ("isoC0", 80), ("isoC1", 81), ("isoC2", 82), ("isoC3", 83), ("isoC4", 84), ("isoC5", 85), ("isoC6", 86), ("isoEnvelopeA0", 96), ("isoEnvelopeA1", 97), ("isoEnvelopeA2", 98), ("isoEnvelopeA3", 99), ("isoEnvelopeA4", 100), ("isoEnvelopeA5", 101), ("isoEnvelopeA6", 102), ("isoEnvelopeB0", 104), ("isoEnvelopeB1", 105), ("isoEnvelopeB2", 106), ("isoEnvelopeB3", 107), ("isoEnvelopeB4", 108), ("isoEnvelopeB5", 109), ("isoEnvelopeB6", 110), ("isoEnvelopeC0", 112), ("isoEnvelopeC1", 113), ("isoEnvelopeC2", 114), ("isoEnvelopeC3", 115), ("isoEnvelopeC4", 116), ("isoEnvelopeC5", 117), ("isoEnvelopeC6", 118), ("jisB0", 136), ("jisB1", 137), ("jisB2", 138), ("jisB3", 139), ("jisB4", 140), ("jisB5", 141), ("jisB6", 142))

class PaperTypeTC(TextualConvention, Integer32):
    description = 'Paper types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 32, 33, 34, 35, 36, 37))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("plain", 3), ("cardstock", 4), ("transparancy", 5), ("recycled", 6), ("labels", 7), ("vinylLabels", 8), ("bond", 9), ("letterhead", 10), ("preprinted", 11), ("colored", 12), ("light", 13), ("heavy", 14), ("roughOrCotton", 15), ("envelope", 16), ("customtype1", 32), ("customtype2", 33), ("customtype3", 34), ("customtype4", 35), ("customtype5", 36), ("customtype6", 37))

class AdminStatusTC(TextualConvention, Integer32):
    description = 'The administrative status for the item. This is the desired state for the object as set by the administrator. The types of unknown and other are for reporting only and should not be supported for setting. Definitions: up - The desired state of this item is active and running. disabled - The desired state of this item is disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("other", 3), ("up", 4), ("disabled", 5))

class StatusTC(TextualConvention, Integer32):
    description = 'The status of an item. The bottom 4 bits will describe operational status and higher bits will be anded with this to determine the current status. Bitmap: - bit 0-3 - General status - bit 4 - Disabled. Set only if the item has been disabled by the admin. Cleared otherwise. - bit 5 - Optional license required. Set only if this item requires an optional license for operation. - bit 6 - License state. 0 = unlicensed, 1 = licensed. This bit may only be set if bit 5 is also set (licensed required)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 22, 33, 34, 35, 36, 37, 38, 97, 98, 99, 100, 101, 102))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("ok", 3), ("offline", 4), ("warning", 5), ("broken", 6), ("disabledUnknown", 17), ("disabledOther", 18), ("disabledOk", 19), ("disabledOffline", 20), ("disabledWarning", 21), ("disabledBroken", 22), ("unlicensedUnknown", 33), ("unlicensedOther", 34), ("unlicensedOk", 35), ("unlicensedOffline", 36), ("unlicensedWarning", 37), ("unlicensedBroken", 38), ("licensedUnknown", 97), ("licensedOther", 98), ("licensedOk", 99), ("licensedOffline", 100), ("licensedWarning", 101), ("licensedBroken", 102))

class KeyValueTC(TextualConvention, OctetString):
    description = "A key=value; delimited string to hold various pieces of data. Each data item should consist of a key (as defined in the table below), followed by an equal sign ('='), followed by a semi-colon. The last item in the list should have a semi-colon. If it is necessary to use and equal or a semi-colon as part of the data, it should be delimited via the \\ character (ie \\= or \\;) Data should NOT be localized, all values should be in English. This will allow parsing by automated tools. Keynames should be planned to be case insensitive. The following list shows defined keys. Keys not in this list should NOT be used. If a key is needed that is not in the list, it should be added to the list. This will avoid key overlap. Keys may be anywhere from 2 chars to 8 chars. Shorter keys will allow for more possible data. Defined key list SrvCode The yyy.xx Service code associated with an error. PJLCode The PJL Code associated with an error. FixedID The fixed ID of the alert Triplet NPA triplet of the alert SerNum The serial number of the item PartNum The part number of the item Color The color of the item. Primarily for use with toner. Level Percent of supply that is left. PapSize The size of the paper referred to. This should use the pwg standard size names. PapType The type of the paper referred to. This should use the pwg standard type names. TrayName The name of the input tray referred to. BinNum The number of the output bin referred to. PctComp The percentage complete of the operation. Actions Actions that can be performed for this IR, Known Values: Reset, Continue, Cancel, Change Paper If multiple items are there, comma delimit. Cap The capacity of tray in sheets Offset The value of offset or jogging support Known Values: Y, N Y is for Yes, N is for No Staple The value of the staple support. This represents how many staples are used for normal stapling Punch The hole punch mode supported by tray Known Values: 2, 3, 4 If multiple support, comma delimit Fold The value of fold support Known Values: Y, N Y is for Yes, N is for No BookStaple The value of booklet staple support. This represents how may staples are used for booklet stapling IntName Internal device name Examples: If this string was being used to describe a 'Load Paper' event, the resulting string might look like 'TrayName=Tray 1;PapSize=na_letter_8.5x11in;PapType=stationary;' A string for a toner low event might look like 'Color=black;SerNum=12345678;Level=10%'"
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("LEXMARK-TC-MIB", AdminStatusTC=AdminStatusTC, StatusTC=StatusTC, PaperTypeTC=PaperTypeTC, PaperSizeTC=PaperSizeTC, PYSNMP_MODULE_ID=lexmarkTCMIB, lexmarkTCMIB=lexmarkTCMIB, KeyValueTC=KeyValueTC, UnitsTC=UnitsTC)
