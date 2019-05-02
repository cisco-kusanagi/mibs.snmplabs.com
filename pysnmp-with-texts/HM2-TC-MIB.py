#
# PySNMP MIB module HM2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:31:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter64, Bits, Integer32, Counter32, ObjectIdentity, enterprises, TimeTicks, ModuleIdentity, NotificationType, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter64", "Bits", "Integer32", "Counter32", "ObjectIdentity", "enterprises", "TimeTicks", "ModuleIdentity", "NotificationType", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2TcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 1))
hm2TcMib.setRevisions(('2011-03-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2TcMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2TcMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2TcMib.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2TcMib.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2TcMib.setDescription('Textual conventions used throughout the various Hirschmann MIB modules. Copyright (C) 2011. All Rights Reserved.')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
hm2ConfigurationMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11))
hm2PlatformMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12))
class HmEnabledStatus(TextualConvention, Integer32):
    description = 'Status of a feature'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class HmActionValue(TextualConvention, Integer32):
    description = 'Trigger a action on the device. Reading the variable normally returns noop. The processing state and the termination result can be monitored with SNMP Protocol Extension MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noop", 1), ("action", 2))

class HmTimeHHMM24(TextualConvention, OctetString):
    description = 'The time in hh:mm format: range for hh: 0 to 23 range for mm: 0 to 59'
    status = 'current'
    displayHint = '5a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

class HmTimeSeconds1970(TextualConvention, Unsigned32):
    description = 'Time in seconds since Jan, 1st, 1970.'
    status = 'current'

class HmLargeDisplayString(TextualConvention, OctetString):
    description = "Represents textual information taken from the NVT ASCII character set, as defined in pages 4, 10-11 of RFC 854. To summarize RFC 854, the NVT ASCII repertoire specifies: - the use of character codes 0-127 (decimal) - the graphics characters (32-126) are interpreted as US ASCII - NUL, LF, CR, BEL, BS, HT, VT and FF have the special meanings specified in RFC 854 - the other 25 codes have no standard interpretation - the sequence 'CR LF' means newline - the sequence 'CR NUL' means carriage-return - an 'LF' not preceded by a 'CR' means moving to the same column on the next line. - the sequence 'CR x' for any x other than LF or NUL is illegal. (Note that this also means that a string may end with either 'CR LF' or 'CR NUL', but not with CR.) Any object defined using this syntax may not exceed 2048 characters in length."
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("HM2-TC-MIB", HmTimeSeconds1970=HmTimeSeconds1970, HmLargeDisplayString=HmLargeDisplayString, hm2PlatformMibs=hm2PlatformMibs, hirschmann=hirschmann, hm2TcMib=hm2TcMib, hm2ConfigurationMibs=hm2ConfigurationMibs, HmActionValue=HmActionValue, PYSNMP_MODULE_ID=hm2TcMib, HmTimeHHMM24=HmTimeHHMM24, HmEnabledStatus=HmEnabledStatus)
