#
# PySNMP MIB module URI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/URI-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:55:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, TimeTicks, Counter32, Integer32, mib_2, NotificationType, MibIdentifier, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "Integer32", "mib-2", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uriTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 164))
uriTcMIB.setRevisions(('2007-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: uriTcMIB.setRevisionsDescriptions(('Initial revision, published as RFC 5017. Copyright (C) The IETF Trust (2007). This version of this MIB module is part of RFC 5017; see the RFC itself for full legal notices.',))
if mibBuilder.loadTexts: uriTcMIB.setLastUpdated('200709100000Z')
if mibBuilder.loadTexts: uriTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
if mibBuilder.loadTexts: uriTcMIB.setContactInfo('EMail: ops-area@ietf.org Home page: http://www.ops.ietf.org/')
if mibBuilder.loadTexts: uriTcMIB.setDescription('This MIB module defines textual conventions for representing URIs, as defined by RFC 3986 STD 66.')
class Uri(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    description = "A Uniform Resource Identifier (URI) as defined by STD 66. Objects using this TEXTUAL-CONVENTION MUST be in US-ASCII encoding, and MUST be normalized as described by RFC 3986 Sections 6.2.1, 6.2.2.1, and 6.2.2.2. All unnecessary percent-encoding is removed, and all case-insensitive characters are set to lowercase except for hexadecimal digits, which are normalized to uppercase as described in Section 6.2.2.1. The purpose of this normalization is to help provide unique URIs. Note that this normalization is not sufficient to provide uniqueness. Two URIs that are textually distinct after this normalization may still be equivalent. Objects using this TEXTUAL-CONVENTION MAY restrict the schemes that they permit. For example, 'data:' and 'urn:' schemes might not be appropriate. A zero-length URI is not a valid URI. This can be used to express 'URI absent' where required, for example when used as an index field. Where this TEXTUAL-CONVENTION is used for an index field, it MUST be subtyped to restrict its length. There is an absolute limit of 128 subids for an OID, and it is not efficient to have OIDs whose length approaches this limit."
    status = 'current'
    displayHint = '1a'

class Uri255(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    description = "A Uniform Resource Identifier (URI) as defined by STD 66. Objects using this TEXTUAL-CONVENTION MUST be in US-ASCII encoding, and MUST be normalized as described by RFC 3986 Sections 6.2.1, 6.2.2.1, and 6.2.2.2. All unnecessary percent-encoding is removed, and all case-insensitive characters are set to lowercase except for hexadecimal digits, which are normalized to uppercase as described in Section 6.2.2.1. The purpose of this normalization is to help provide unique URIs. Note that this normalization is not sufficient to provide uniqueness. Two URIs that are textually distinct after this normalization may still be equivalent. Objects using this TEXTUAL-CONVENTION MAY restrict the schemes that they permit. For example, 'data:' and 'urn:' schemes might not be appropriate. A zero-length URI is not a valid URI. This can be used to express 'URI absent' where required, for example when used as an index field. STD 66 URIs are of unlimited length. Objects using this TEXTUAL-CONVENTION impose a length limit on the URIs that they can represent. Where no length restriction is required, objects SHOULD use the 'Uri' TEXTUAL-CONVENTION instead. Objects used as indices SHOULD subtype the 'Uri' TEXTUAL-CONVENTION."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Uri1024(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    description = "A Uniform Resource Identifier (URI) as defined by STD 66. Objects using this TEXTUAL-CONVENTION MUST be in US-ASCII encoding, and MUST be normalized as described by RFC 3986 Sections 6.2.1, 6.2.2.1, and 6.2.2.2. All unnecessary percent-encoding is removed, and all case-insensitive characters are set to lowercase except for hexadecimal digits, which are normalized to uppercase as described in Section 6.2.2.1. The purpose of this normalization is to help provide unique URIs. Note that this normalization is not sufficient to provide uniqueness. Two URIs that are textually distinct after this normalization may still be equivalent. Objects using this TEXTUAL-CONVENTION MAY restrict the schemes that they permit. For example, 'data:' and 'urn:' schemes might not be appropriate. A zero-length URI is not a valid URI. This can be used to express 'URI absent' where required, for example when used as an index field. STD 66 URIs are of unlimited length. Objects using this TEXTUAL-CONVENTION impose a length limit on the URIs that they can represent. Where no length restriction is required, objects SHOULD use the 'Uri' TEXTUAL-CONVENTION instead. Objects used as indices SHOULD subtype the 'Uri' TEXTUAL-CONVENTION."
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("URI-TC-MIB", PYSNMP_MODULE_ID=uriTcMIB, Uri255=Uri255, Uri1024=Uri1024, uriTcMIB=uriTcMIB, Uri=Uri)
