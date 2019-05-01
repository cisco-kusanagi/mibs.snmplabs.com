#
# PySNMP MIB module IPSEC-ISAKMP-IKE-DOI-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPSEC-ISAKMP-IKE-DOI-TC
# Produced by pysmi-0.3.4 at Wed May  1 13:56:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, TimeTicks, ObjectIdentity, Bits, experimental, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, MibIdentifier, iso, Unsigned32, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "TimeTicks", "ObjectIdentity", "Bits", "experimental", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "MibIdentifier", "iso", "Unsigned32", "Gauge32", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-MIB", "watchguard")
ipsecIsakmpIkeDoiTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 100))
ipsecIsakmpIkeDoiTC.setRevisions(('1999-02-18 17:05', '1999-03-05 15:45', '1999-07-13 21:45', '1999-10-05 17:05', '1999-10-15 19:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setRevisionsDescriptions(('Added IsakmpDOI TEXTUAL-CONVENTION.', 'Changed CONTACT-INFO.', 'Put in real experimental branch number for module.', 'Added exchange types, tracked IKE standard. Split IkeNotifyMessageType off of IsakmpNotifyMessageType.', 'Removed stray comma in IsakmpNotifyMessageType.',))
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setLastUpdated('9907132145Z')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setOrganization('Shiva')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setContactInfo('John Shriver Intel Corporation 28 Crosby Drive Bedford, MA 01730 Phone: +1-781-687-1329 E-mail: John.Shriver@intel.com')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setDescription('The MIB module which defines the textual conventions used in IPSEC MIBs. This includes Internet DOI numbers defined in RFC 2407, ISAKMP numbers defined in RFC 2408, and IKE numbers defined in RFC 2409. These Textual Conventions are defined in a seperate MIB module since they are protocol numbers managed by the IANA. Revision control after publication will be under the authority of the IANA.')
class IpsecDoiSituation(TextualConvention, Unsigned32):
    reference = 'RFC 2407 sections 4.2 and 6.2'
    description = 'The IPSEC DOI Situation provides information that can be used by the responder to make a policy determination about how to process the incoming Security Association request. It is a four (4) octet bitmask, with the following values: sitIdentityOnly 0x01 sitSecrecy 0x02 sitIntegrity 0x04 The upper two bits (0x80000000 and 0x40000000) are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpsecDoiSecProtocolId(TextualConvention, Integer32):
    reference = 'RFC 2407 section 4.4.1'
    description = 'These are the IPSEC DOI values for the Protocol-Id field in an ISAKMP Proposal Payload, and in all Notification Payloads. They are also used as the Protocol-ID In the Notification Payload and the Delete Payload. The values 249-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("protoIsakmp", 1), ("protoIpsecAh", 2), ("protoIpsecEsp", 3), ("protoIpcomp", 4))

class IpsecDoiTransformIdent(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.2 and 6.3'
    description = 'The IPSEC DOI ISAKMP Transform Identifier is an 8-bit value which identifies a key exchange protocol to be used for the negotiation. It is used in the Transform-Id field of an IKE Phase I Transform Payload. The values 249-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("reserved", 0), ("keyIke", 1))

class IpsecDoiAhTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.3 and 6.4'
    description = 'The IPSEC DOI AH Transform Identifier is an 8-bit value which identifies a particular algorithm to be used to provide integrity protection for AH. It is used in the Tranform-ID field of a ISAKMP Transform Payload for the IPSEC DOI, when the Protocol-Id of the associated Proposal Payload is 2 (AH). The values 249-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("reserved1", 1), ("ahMd5", 2), ("ahSha", 3), ("ahDes", 4))

class IpsecDoiEspTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.4 and 6.5'
    description = 'The IPSEC DOI ESP Transform Identifier is an 8-bit value which identifies a particular algorithm to be used to provide secrecy protection for ESP. It is used in the Tranform-ID field of a ISAKMP Transform Payload for the IPSEC DOI, when the Protocol-Id of the associated Proposal Payload is 2 (AH), 3 (ESP), and 4 (IPCOMP). The values 249-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("espDesIv64", 1), ("espDes", 2), ("esp3Des", 3), ("espRc5", 4), ("espIdea", 5), ("espCast", 6), ("espBlowfish", 7), ("esp3Idea", 8), ("espDesIv32", 9), ("espRc4", 10), ("espNull", 11))

class IpsecDoiAuthAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2407 section 4.5'
    description = 'The ESP Authentication Algorithm used in the IPSEC DOI as a SA Attributes definition in the Transform Payload of Phase II of an IKE negotiation. This set of values defines the AH authentication algorithm, when the associated Proposal Payload has a Protocol-ID of 2 (AH). This set of values defines the ESP authentication algorithm, when the associated Proposal Payload has a Protocol-ID of 3 (ESP). Values 5-61439 are reserved to IANA. Values 61440-65535 are for private use. In a MIB, a value of 0 indicates that ESP has been negotiated without authentication.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("hmacMd5", 1), ("hmacSha", 2), ("desMac", 3), ("kpdk", 4))

class IpsecDoiIpcompTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.5 and 6.6'
    description = 'The IPSEC DOI IPCOMP Transform Identifier is an 8-bit value which identifies a particular algorithm to be used to provide IP-level compression before ESP. It is used in the Tranform-ID field of a ISAKMP Transform Payload for the IPSEC DOI, when the Protocol-Id of the associated Proposal Payload is 4 (IPCOMP). The values 1-47 are reserved for algorithms for which an RFC has been approved for publication. The values 48-63 are reserved for private use amongst cooperating systems. The values 64-255 are reserved for future expansion.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("ipcompOui", 1), ("ipcompDeflate", 2), ("ipcompLzs", 3))

class IpsecDoiEncapsulationMode(TextualConvention, Integer32):
    description = 'The Encapsulation Mode used as an IPSEC DOI SA Attributes definition in the Transform Payload of a Phase II IKE negotiation. This set of values defines encapsulation modes used for AH, ESP, and IPCOMP when the associated Proposal Payload has a Protocol-ID of 3 (ESP). Values 3-61439 are reserved to IANA. Values 61440-65535 are for private use.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("tunnel", 1), ("transport", 2))

class IpsecDoiIdentType(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.5, 4.6.2.1, and 6.9'
    description = 'The IPSEC DOI Identification Type is an 8-bit value which is used in the ID Type field as a discriminant for interpretation of the variable-length Identification Payload. The values 249-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idUserFqdn", 3), ("idIpv4AddrSubnet", 4), ("idIpv6Addr", 5), ("idIpv6AddrSubnet", 6), ("idIpv4AddrRange", 7), ("idIpv6AddrRange", 8), ("idDerAsn1Dn", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

class IsakmpDOI(TextualConvention, Integer32):
    reference = 'RFC 2048 section 3.4.'
    description = 'These are the domain of interpretation values for the ISAKMP Protocol. They are a 32-bit value used in the Domain of Interpretation field of the Security Association Payload. Values 2-4294967295 are reserved to the IANA.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("isakmp", 0), ("ipsecDOI", 1))

class IsakmpCertificateEncoding(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.9'
    description = 'These are the values for the types of certificate-related information contained in the Certificate Data field of a Certificate Payload. They are used in the Cert Encoding field of the Certificate Payload. Values 11-255 are reserved.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("pkcs7", 1), ("pgp", 2), ("dnsSignedKey", 3), ("x509Signature", 4), ("x509KeyExchange", 5), ("kerberosTokens", 6), ("crl", 7), ("arl", 8), ("spki", 9), ("x509Attribute", 10))

class IsakmpExchangeType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.1'
    description = 'These are the values used for the exchange types in the ISAKMP header. Values up to 31 are reserved for future DOI-independent assignment for ISAKMP. The values 240-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("base", 1), ("identityProtect", 2), ("authOnly", 3), ("aggressive", 4), ("informational", 5))

class IsakmpNotifyMessageType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.14.1'
    description = 'These are the values for the types of notification messages. They are used as the Notify Message Type field in the Notification Payload. This textual convention merges the types for error types (in the range 1-16386) and for notification types (in the range 16384-65535). The values 16001-16383 are reserved for private use as error types amongst cooperating systems. The values 24576-32767 are reserved for use in each DOI. Each DOI should have a clone of this textual convention adding local values. The values 32768-40958 are reserved for private use as notification types amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
    namedValues = NamedValues(("reserved", 0), ("invalidPayloadType", 1), ("doiNotSupported", 2), ("situationNotSupported", 3), ("invalidCookie", 4), ("invalidMajorVersion", 5), ("invalidMinorVersion", 6), ("invalidExchangeType", 7), ("invalidFlags", 8), ("invalidMessageId", 9), ("invalidProtocolId", 10), ("invalidSpi", 11), ("invalidTransformId", 12), ("attributesNotSupported", 13), ("noProposalChosen", 14), ("badProposalSyntax", 15), ("payloadMalformed", 16), ("invalidKeyInformation", 17), ("invalidIdInformation", 18), ("invalidCertEncoding", 19), ("invalidCertificate", 20), ("certTypeUnsupported", 21), ("invalidCertAuthority", 22), ("invalidHashInformation", 23), ("authenticationFailed", 24), ("invalidSignature", 25), ("addressNotification", 26), ("notifySaLifetime", 27), ("certificateUnavailable", 28), ("unsupportedExchangeType", 29), ("unequalPayloadLengths", 30))

class IkeExchangeType(TextualConvention, Integer32):
    reference = 'RFC 2409 Appendix A, draft-ietf-ipsec-ike-01.txt appendix A'
    description = 'These are the values used for the exchange types in the ISAKMP header. The values 32-239 are DOI-specific, these values are for the IPSec DOI used by IKE. The values 240-255 are reserved for private use amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 32, 33, 34))
    namedValues = NamedValues(("reserved", 0), ("base", 1), ("mainMode", 2), ("authOnly", 3), ("aggressive", 4), ("informational", 5), ("quickMode", 32), ("newGroupMode", 33), ("acknowledgedInfo", 34))

class IkeEncryptionAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for encryption algorithms negotiated for the ISAKMP SA by IKE in Phase I. These are values for SA Attrbute type Encryption Algorithm (1). Values 7-65000 are reserved to IANA. Values 65001-65535 are for private use among mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("reserved", 0), ("desCbc", 1), ("ideaCbc", 2), ("blowfishCbc", 3), ("rc5R16B64Cbc", 4), ("tripleDesCbc", 5), ("castCbc", 6))

class IkeHashAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for hash algorithms negotiated for the ISAKMP SA by IKE in Phase I. These are values for SA Attrbute type Hash Algorithm (2). Values 4-65000 are reserved to IANA. Values 65001-65535 are for private use among mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("md5", 1), ("sha", 2), ("tiger", 3))

class IkeAuthMethod(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A, draft-ietf-ipsec-ike-01.txt appendix A'
    description = 'Values for authentication methods negotiated for the ISAKMP SA by IKE in Phase I. These are values for SA Attrbute type Authentication Method (3). Values 6-65000 are reserved to IANA. Values 65001-65535 are for private use among mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("reserved", 0), ("preSharedKey", 1), ("dssSignatures", 2), ("rsaSignatures", 3), ("encryptionWithRsa", 4), ("revisedEncryptionWithRsa", 5), ("encryptionWithElGamal", 6), ("revisedEncryptionWithElGamal", 7))

class IkeGroupDescription(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A, draft-ietf-ipsec-ike-01.txt appendix A'
    description = 'Values for Oakley key computation groups for Diffie-Hellman exchange negotiated for the ISAKMP SA by IKE in Phase I. They are also used in Phase II when perfect forward secrecy is in use. These are values for SA Attrbute type Group Description (4).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("modp768", 1), ("modp1024", 2), ("ec2nGalois2P155", 3), ("ec2nGalois2P185", 4), ("modp1536", 5))

class IkeGroupType(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for Oakley key computation group types negotiated for the ISAKMP SA by IKE in Phase I. They are also used in Phase II when perfect forward secrecy is in use. These are values for SA Attribute type Group Type (5).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("modp", 1), ("ecp", 2), ("ec2n", 3))

class IkePrf(TextualConvention, Unsigned32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for Pseudo-Random Functions used with with the hash algorithm negotiated for the ISAKMP SA by IKE in Phase I. There are currently no pseudo-random functions defined, the default HMAC is always used. These are values for SA Attribute type PRF (13). Values 1-65000 are reserved to IANA. Values 65001-65535 are for private use among mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IkeNotifyMessageType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.14.1 and RFC 2407 sections 4.6.3 and 6.10'
    description = 'These are the values for the types of notification messages. They are used as the Notify Message Type field in the Notification Payload. This textual convention merges the types for error types (in the range 1-16386) and for notification types (in the range 16384-65535). This textual convention is a merge of values defined by ISAKMP with the additional values defined in the IPSEC DOI. The values 16001-16383 are reserved for private use as error types amongst cooperating systems. The values 32001-32767 are reserved for private use as notification types amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 24576, 24577, 24578))
    namedValues = NamedValues(("reserved", 0), ("invalidPayloadType", 1), ("doiNotSupported", 2), ("situationNotSupported", 3), ("invalidCookie", 4), ("invalidMajorVersion", 5), ("invalidMinorVersion", 6), ("invalidExchangeType", 7), ("invalidFlags", 8), ("invalidMessageId", 9), ("invalidProtocolId", 10), ("invalidSpi", 11), ("invalidTransformId", 12), ("attributesNotSupported", 13), ("noProposalChosen", 14), ("badProposalSyntax", 15), ("payloadMalformed", 16), ("invalidKeyInformation", 17), ("invalidIdInformation", 18), ("invalidCertEncoding", 19), ("invalidCertificate", 20), ("certTypeUnsupported", 21), ("invalidCertAuthority", 22), ("invalidHashInformation", 23), ("authenticationFailed", 24), ("invalidSignature", 25), ("addressNotification", 26), ("notifySaLifetime", 27), ("certificateUnavailable", 28), ("unsupportedExchangeType", 29), ("unequalPayloadLengths", 30), ("responderLifetime", 24576), ("replayStatus", 24577), ("initialContact", 24578))

mibBuilder.exportSymbols("IPSEC-ISAKMP-IKE-DOI-TC", IpsecDoiSituation=IpsecDoiSituation, IkePrf=IkePrf, IkeExchangeType=IkeExchangeType, IkeGroupType=IkeGroupType, IkeNotifyMessageType=IkeNotifyMessageType, ipsecIsakmpIkeDoiTC=ipsecIsakmpIkeDoiTC, IpsecDoiAhTransform=IpsecDoiAhTransform, IsakmpNotifyMessageType=IsakmpNotifyMessageType, IpsecDoiEncapsulationMode=IpsecDoiEncapsulationMode, IsakmpDOI=IsakmpDOI, IpsecDoiIpcompTransform=IpsecDoiIpcompTransform, IkeAuthMethod=IkeAuthMethod, IkeEncryptionAlgorithm=IkeEncryptionAlgorithm, IsakmpExchangeType=IsakmpExchangeType, IsakmpCertificateEncoding=IsakmpCertificateEncoding, IkeHashAlgorithm=IkeHashAlgorithm, IpsecDoiEspTransform=IpsecDoiEspTransform, IpsecDoiSecProtocolId=IpsecDoiSecProtocolId, IpsecDoiIdentType=IpsecDoiIdentType, PYSNMP_MODULE_ID=ipsecIsakmpIkeDoiTC, IpsecDoiTransformIdent=IpsecDoiTransformIdent, IpsecDoiAuthAlgorithm=IpsecDoiAuthAlgorithm, IkeGroupDescription=IkeGroupDescription)
