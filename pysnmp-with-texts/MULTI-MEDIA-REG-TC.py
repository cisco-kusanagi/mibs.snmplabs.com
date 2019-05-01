#
# PySNMP MIB module MULTI-MEDIA-REG-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MULTI-MEDIA-REG-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:15:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Bits, ObjectIdentity, TimeTicks, experimental, MibIdentifier, Counter64, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Bits", "ObjectIdentity", "TimeTicks", "experimental", "MibIdentifier", "Counter64", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
multimediaRegMib = ModuleIdentity((1, 3, 6, 1, 3, 323))
multimediaRegMib.setRevisions(('1998-05-29 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: multimediaRegMib.setRevisionsDescriptions(('The initial version of the mib.',))
if mibBuilder.loadTexts: multimediaRegMib.setLastUpdated('9805291200Z')
if mibBuilder.loadTexts: multimediaRegMib.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: multimediaRegMib.setContactInfo(' Dan Klenke Cisco Systems, Inc Postal: 170 West Tasman Drive San Jose, CA 95134-1706 E-mail: dklenke@Cisco.com')
if mibBuilder.loadTexts: multimediaRegMib.setDescription('Defines a set of Textual Conventions used within the set of MultiMedia MIB modules. Defines OBJECT IDENTIFIERs for rooting associated mib modules under this tree')
class MmUtf8String(TextualConvention, OctetString):
    description = 'To facilitate internationalization, this TC represents information taken from the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 character encoding scheme described in RFC 2044 [8]. For strings in 7-bit US- ASCII, there is no impact since the UTF-8 representation is identical to the US-ASCII encoding.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MmE164String(TextualConvention, OctetString):
    description = "A UTF-8 string limited to the character set defined for E.164, '0123456789*#,<quote>' "
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmTAddressTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the transport address contained in the TAddress textual convention. The values correlate to the TransportAddress defined in the H.225.0 V2 ITU protocol specification. The tag indicates how to interpret the value of a TAddress data type defined in this specification. All TAddress values are in network byte order TAddress size TAddress contents ipv4 6 octets IPv4 (4 octets), port (2 octets) ipv6 18 IPv6 (16), port (2) ipx 12 net (4), node (6), port (2) nsap 1-20 nsap(1-20) netbios 16 netbios(16) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4), ("netbios", 5))

class MmGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A 16 octet field containing a unique identifier. The identifier contains the following fields: 60 bit nanosecond time (octets 1-7, low 4 bits of octet 8) 4 bit version (hi 4 bits of octet 8) 3 octet 0 (a variant field) 1 octet hi 2bits 0, low 6bits clock sequence. 6 octet MAC Address See Reference for generation of this value. '
    status = 'current'
    displayHint = '8d-9,3x,1d,2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class MmAliasTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the Alias address contained in the MmAliasAddress data type. The values correlate to the AliasAddress defined in the H.225.0 V2 ITU protocol specification. The tag indicates how to interpret the value of an AliasAddress data type defined in that specification. AliasAddress contents other unknown e164 MmE164String h323Id MmUtf8String urlId MmUtf8String containing a URL transportId MmTAddressTag, TAddress emailId MmUtf8String containing e-mail address partyNumber contains PartyNumber '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class MmAliasAddress(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to AliasAddress defined in H.225.0. The value of an object of this type has the syntax and symantics identified by MmAliasTag. An object defined as MmAliasAddress must have a corresponding MmAliasTag object.'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class MmEndpointID(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to EndpointIdentifier defined in H.225.0.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to GatekeeperIdentifier defined in H.225.0.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmH225Crv(TextualConvention, Integer32):
    reference = 'ITU H225.0 Version 2'
    description = 'A data type corresponding to the Call Reference Value defined in H.225.0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

mmRtpRoot = ObjectIdentity((1, 3, 6, 1, 3, 323, 1))
if mibBuilder.loadTexts: mmRtpRoot.setStatus('current')
if mibBuilder.loadTexts: mmRtpRoot.setDescription('Subtree for root of Mm Rtp mib.')
mmH323Root = ObjectIdentity((1, 3, 6, 1, 3, 323, 2))
if mibBuilder.loadTexts: mmH323Root.setStatus('current')
if mibBuilder.loadTexts: mmH323Root.setDescription('Subtree for root of H323 mib modules.')
mmH320Root = ObjectIdentity((1, 3, 6, 1, 3, 323, 3))
if mibBuilder.loadTexts: mmH320Root.setStatus('current')
if mibBuilder.loadTexts: mmH320Root.setDescription('Subtree for root of H320 mib modules.')
mmH245Root = ObjectIdentity((1, 3, 6, 1, 3, 323, 4))
if mibBuilder.loadTexts: mmH245Root.setStatus('current')
if mibBuilder.loadTexts: mmH245Root.setDescription('Subtree for root of H245 mib modules.')
mibBuilder.exportSymbols("MULTI-MEDIA-REG-TC", PYSNMP_MODULE_ID=multimediaRegMib, MmEndpointID=MmEndpointID, MmH225Crv=MmH225Crv, mmH320Root=mmH320Root, MmUtf8String=MmUtf8String, MmAliasTag=MmAliasTag, mmRtpRoot=mmRtpRoot, mmH323Root=mmH323Root, MmE164String=MmE164String, mmH245Root=mmH245Root, multimediaRegMib=multimediaRegMib, MmGlobalIdentifier=MmGlobalIdentifier, MmAliasAddress=MmAliasAddress, MmTAddressTag=MmTAddressTag, MmGatekeeperID=MmGatekeeperID)
