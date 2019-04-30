#
# PySNMP MIB module IPSEC-ISAKMP-IKE-DOI-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPSEC-ISAKMP-IKE-DOI-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, ObjectIdentity, mib_2, IpAddress, Counter64, experimental, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Gauge32, TimeTicks, Integer32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ObjectIdentity", "mib-2", "IpAddress", "Counter64", "experimental", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-MIB", "watchguard")
ipsecIsakmpIkeDoiTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 100))
ipsecIsakmpIkeDoiTC.setRevisions(('1999-02-18 17:05', '1999-03-05 15:45', '1999-07-13 21:45', '1999-10-05 17:05', '1999-10-15 19:50',))
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setLastUpdated('9907132145Z')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setOrganization('Shiva')
class IpsecDoiSituation(TextualConvention, Unsigned32):
    reference = 'RFC 2407 sections 4.2 and 6.2'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpsecDoiSecProtocolId(TextualConvention, Integer32):
    reference = 'RFC 2407 section 4.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("protoIsakmp", 1), ("protoIpsecAh", 2), ("protoIpsecEsp", 3), ("protoIpcomp", 4))

class IpsecDoiTransformIdent(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.2 and 6.3'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("reserved", 0), ("keyIke", 1))

class IpsecDoiAhTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.3 and 6.4'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("reserved1", 1), ("ahMd5", 2), ("ahSha", 3), ("ahDes", 4))

class IpsecDoiEspTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.4 and 6.5'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("espDesIv64", 1), ("espDes", 2), ("esp3Des", 3), ("espRc5", 4), ("espIdea", 5), ("espCast", 6), ("espBlowfish", 7), ("esp3Idea", 8), ("espDesIv32", 9), ("espRc4", 10), ("espNull", 11))

class IpsecDoiAuthAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2407 section 4.5'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("hmacMd5", 1), ("hmacSha", 2), ("desMac", 3), ("kpdk", 4))

class IpsecDoiIpcompTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.5 and 6.6'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("ipcompOui", 1), ("ipcompDeflate", 2), ("ipcompLzs", 3))

class IpsecDoiEncapsulationMode(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("tunnel", 1), ("transport", 2))

class IpsecDoiIdentType(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.5, 4.6.2.1, and 6.9'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idUserFqdn", 3), ("idIpv4AddrSubnet", 4), ("idIpv6Addr", 5), ("idIpv6AddrSubnet", 6), ("idIpv4AddrRange", 7), ("idIpv6AddrRange", 8), ("idDerAsn1Dn", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

class IsakmpDOI(TextualConvention, Integer32):
    reference = 'RFC 2048 section 3.4.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("isakmp", 0), ("ipsecDOI", 1))

class IsakmpCertificateEncoding(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.9'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("pkcs7", 1), ("pgp", 2), ("dnsSignedKey", 3), ("x509Signature", 4), ("x509KeyExchange", 5), ("kerberosTokens", 6), ("crl", 7), ("arl", 8), ("spki", 9), ("x509Attribute", 10))

class IsakmpExchangeType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("base", 1), ("identityProtect", 2), ("authOnly", 3), ("aggressive", 4), ("informational", 5))

class IsakmpNotifyMessageType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.14.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
    namedValues = NamedValues(("reserved", 0), ("invalidPayloadType", 1), ("doiNotSupported", 2), ("situationNotSupported", 3), ("invalidCookie", 4), ("invalidMajorVersion", 5), ("invalidMinorVersion", 6), ("invalidExchangeType", 7), ("invalidFlags", 8), ("invalidMessageId", 9), ("invalidProtocolId", 10), ("invalidSpi", 11), ("invalidTransformId", 12), ("attributesNotSupported", 13), ("noProposalChosen", 14), ("badProposalSyntax", 15), ("payloadMalformed", 16), ("invalidKeyInformation", 17), ("invalidIdInformation", 18), ("invalidCertEncoding", 19), ("invalidCertificate", 20), ("certTypeUnsupported", 21), ("invalidCertAuthority", 22), ("invalidHashInformation", 23), ("authenticationFailed", 24), ("invalidSignature", 25), ("addressNotification", 26), ("notifySaLifetime", 27), ("certificateUnavailable", 28), ("unsupportedExchangeType", 29), ("unequalPayloadLengths", 30))

class IkeExchangeType(TextualConvention, Integer32):
    reference = 'RFC 2409 Appendix A, draft-ietf-ipsec-ike-01.txt appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 32, 33, 34))
    namedValues = NamedValues(("reserved", 0), ("base", 1), ("mainMode", 2), ("authOnly", 3), ("aggressive", 4), ("informational", 5), ("quickMode", 32), ("newGroupMode", 33), ("acknowledgedInfo", 34))

class IkeEncryptionAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("reserved", 0), ("desCbc", 1), ("ideaCbc", 2), ("blowfishCbc", 3), ("rc5R16B64Cbc", 4), ("tripleDesCbc", 5), ("castCbc", 6))

class IkeHashAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("md5", 1), ("sha", 2), ("tiger", 3))

class IkeAuthMethod(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A, draft-ietf-ipsec-ike-01.txt appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("reserved", 0), ("preSharedKey", 1), ("dssSignatures", 2), ("rsaSignatures", 3), ("encryptionWithRsa", 4), ("revisedEncryptionWithRsa", 5), ("encryptionWithElGamal", 6), ("revisedEncryptionWithElGamal", 7))

class IkeGroupDescription(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A, draft-ietf-ipsec-ike-01.txt appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("modp768", 1), ("modp1024", 2), ("ec2nGalois2P155", 3), ("ec2nGalois2P185", 4), ("modp1536", 5))

class IkeGroupType(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("modp", 1), ("ecp", 2), ("ec2n", 3))

class IkePrf(TextualConvention, Unsigned32):
    reference = 'RFC 2409 appendix A'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IkeNotifyMessageType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.14.1 and RFC 2407 sections 4.6.3 and 6.10'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 24576, 24577, 24578))
    namedValues = NamedValues(("reserved", 0), ("invalidPayloadType", 1), ("doiNotSupported", 2), ("situationNotSupported", 3), ("invalidCookie", 4), ("invalidMajorVersion", 5), ("invalidMinorVersion", 6), ("invalidExchangeType", 7), ("invalidFlags", 8), ("invalidMessageId", 9), ("invalidProtocolId", 10), ("invalidSpi", 11), ("invalidTransformId", 12), ("attributesNotSupported", 13), ("noProposalChosen", 14), ("badProposalSyntax", 15), ("payloadMalformed", 16), ("invalidKeyInformation", 17), ("invalidIdInformation", 18), ("invalidCertEncoding", 19), ("invalidCertificate", 20), ("certTypeUnsupported", 21), ("invalidCertAuthority", 22), ("invalidHashInformation", 23), ("authenticationFailed", 24), ("invalidSignature", 25), ("addressNotification", 26), ("notifySaLifetime", 27), ("certificateUnavailable", 28), ("unsupportedExchangeType", 29), ("unequalPayloadLengths", 30), ("responderLifetime", 24576), ("replayStatus", 24577), ("initialContact", 24578))

mibBuilder.exportSymbols("IPSEC-ISAKMP-IKE-DOI-TC", IkeAuthMethod=IkeAuthMethod, ipsecIsakmpIkeDoiTC=ipsecIsakmpIkeDoiTC, IpsecDoiEncapsulationMode=IpsecDoiEncapsulationMode, IpsecDoiIpcompTransform=IpsecDoiIpcompTransform, IkeGroupDescription=IkeGroupDescription, IkeHashAlgorithm=IkeHashAlgorithm, IkeNotifyMessageType=IkeNotifyMessageType, IpsecDoiTransformIdent=IpsecDoiTransformIdent, IsakmpCertificateEncoding=IsakmpCertificateEncoding, IpsecDoiEspTransform=IpsecDoiEspTransform, IpsecDoiSituation=IpsecDoiSituation, IpsecDoiIdentType=IpsecDoiIdentType, IkePrf=IkePrf, IkeExchangeType=IkeExchangeType, IpsecDoiAhTransform=IpsecDoiAhTransform, IsakmpExchangeType=IsakmpExchangeType, IkeEncryptionAlgorithm=IkeEncryptionAlgorithm, IsakmpDOI=IsakmpDOI, IkeGroupType=IkeGroupType, IpsecDoiSecProtocolId=IpsecDoiSecProtocolId, IpsecDoiAuthAlgorithm=IpsecDoiAuthAlgorithm, IsakmpNotifyMessageType=IsakmpNotifyMessageType, PYSNMP_MODULE_ID=ipsecIsakmpIkeDoiTC)
