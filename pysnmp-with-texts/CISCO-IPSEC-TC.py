#
# PySNMP MIB module CISCO-IPSEC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSEC-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:56:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, Gauge32, iso, Integer32, Counter64, MibIdentifier, Counter32, IpAddress, ObjectIdentity, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Gauge32", "iso", "Integer32", "Counter64", "MibIdentifier", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIPsecTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 422))
ciscoIPsecTc.setRevisions(('2004-07-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPsecTc.setRevisionsDescriptions((' Initial version of this module. ',))
if mibBuilder.loadTexts: ciscoIPsecTc.setLastUpdated('200407220000Z')
if mibBuilder.loadTexts: ciscoIPsecTc.setOrganization('Cisco Systems Inc. and Tivoli Systems Inc.')
if mibBuilder.loadTexts: ciscoIPsecTc.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tivoli Systems Research Triangle Park, NC Tel: +1 800 553-NETS E-mail: cs-ipsecmib@external.cisco.com bret_harrison@tivoli.com ')
if mibBuilder.loadTexts: ciscoIPsecTc.setDescription(' This MIB module defines the textual conventions used in the IPsec suite of MIBs. This includes Internet DOI numbers defined in RFC 2407, ISAKMP numbers defined in RFC 2408, and IKE numbers defined in RFC 2409. ')
class CCryptoMD5Hash(TextualConvention, OctetString):
    description = 'This type denotes a 128-bit MD5 output string of an input string'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class CIKEIsakmpDoi(TextualConvention, Integer32):
    description = 'The Domain of Interpretation of the IKE implementation. This type is used to implement distinctions between the configuration of the IKE implementation for distinct Phase 2 protocols that use IKE. Description of enum constants of this type: isakmpDoiIPsec: Denotes that IPsec protocol is used in Phase-2 isakmpDoiFcsp: Denotes that FC-SP protocol is used in Phase-2 isakmpDoiCps: Denotes that Cps protocol is used in Phase-2 isakmpDoiFcCtAuth: Denotes that Fc-Ct-Auth protocol is used in Phase-2 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("isakmpDoiUnknown", 1), ("isakmpDoiOther", 2), ("isakmpDoiIPsec", 3), ("isakmpDoiFcsp", 4), ("isakmpDoiCps", 5), ("isakmpDoiFcCtAuth", 6))

class CIKELifetime(TextualConvention, Unsigned32):
    description = ' This type corresponds to the lifetime of ISAKMP security associations. The unit of information is seconds. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(60, 86400)

class CIKELifesize(TextualConvention, Unsigned32):
    description = ' This type corresponds to the lifesize of a ISAKMP security association in the number of kilobytes of data that has been processed by the security association. The unit of information is kilobytes. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2560, 4294967295)

class CIPsecEncryptionKeySize(TextualConvention, Unsigned32):
    description = " This type is used by objects that denote the size in bits of key of an encryption transform. The value of 0 has been allowed to provide for 'NULL' encryption transforms. "
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CIPsecControlProtocol(TextualConvention, Integer32):
    description = " The protocol used for keying and control in IPsec connections. The value of 'cpManual' indicates manual administration of IPsec tunnels. This enumeration will be expanded as new keying protocols are standardized. The value 'cpAll' does not denote a specific keying protocol; it has been defined only as a convenience to facilitate aggregation of metrics across all control protocols. Description of enum constants of this type: cpManual: Denotes manual keying (i.e., no signaling). cpIkev1: Denotes keying signaling using IKEv1 protocol. cpIkev2: Denotes keying signaling using IKEv2 protocol. cpKink: Denotes keying signaling using KINK. cpPhoturis: Denotes keying signaling using Photuris. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("cpUnknown", 1), ("cpAll", 2), ("cpOther", 3), ("cpManual", 4), ("cpIkev1", 5), ("cpIkev2", 6), ("cpKink", 7), ("cpPhoturis", 8))

class CIPsecProtocol(TextualConvention, Integer32):
    reference = 'rfc2402, rfc2406 and rfc2409'
    description = ' A protocol used for encapsulating the Phase-2 tunneled traffic. The enumerations correspond to Authentication Header, Encapsulating Security Payload and IP compression protocols. The enum constants used in this denote the standard IPsec protocols, viz., Authentication Header (AH), ESP and IP compression. Description of enum constants of this type: ipsecProtAh: Denotes IPsec Authentication Header (AH) protocol. ipsecProtEsp: Denotes IPsec Encapsulating Security Payload (ESP) protocol. ipsecProtIPcomp: Denotes IPsec Packet Compression protocol. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ipsecProtUnknown", 1), ("ipsecProtAh", 2), ("ipsecProtEsp", 3), ("ipsecProtIPcomp", 4))

class CIPsecPhase1PeerIdentityType(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The type of IPsec Phase-1 peer identity. The peer may be identified by one of the ID types defined in IPSEC DOI. Description of enum constants of this type: idIpv4Addr: IPv4 address idFqdn: Fully QUalified Domain Name idDn: Represents the binary DER encoding of the identity. idIpv6Addr: IPv6 address idUserFqdn: User FQDN (such as an email address). idIpv4AddrSubnet: IPv4 subnet specification (comprising a subnet identifier and a subnet mask). idIpv6AddrSubnet: IPv6 subnet specification (comprising a subnet identifier and a subnet mask). idIpv4AddrRange: A range of IPv4 addresses (comprising a starting address and an ending address) idIpv6AddrRange: A range of IPv6 addresses (comprising a starting address and an ending address) idDerAsn1Gn: The ASN.1 encoded general number. idKeyId: This is the symbolic name (key identifier). idWwn: World Wide Number or the encoding of the layer-2 address used by MDS switches. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("idOther", 1), ("idIpv4Addr", 2), ("idFqdn", 3), ("idDn", 4), ("idIpv6Addr", 5), ("idUserFqdn", 6), ("idIpv4AddrSubnet", 7), ("idIpv6AddrSubnet", 8), ("idIpv4AddrRange", 9), ("idIpv6AddrRange", 10), ("idDerAsn1Gn", 11), ("idKeyId", 12), ("idWwn", 13))

class CIPsecIkeNegoMode(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The negotiation mode used by IKE protocol in Phase-1. The type enumerates constants to denote the two distinct modes of operation of ISAKMP-based IPsec signaling in Phase-2, viz., Main Mode (mainMode) and Aggressive Mode (aggressiveMode). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mainMode", 1), ("aggressiveMode", 2))

class CIPsecIkeHashAlgorithm(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The hash algorithm used in IPsec Phase-1 IKE negotiations. Description of enum constants of this type: md5: Hash payload using MD5 algorithm. sha: Hash payload using 96-bit SHA-1 algorithm as defined in FIPS 180-1. tiger: Hash payload using Tiger hash algorithm. sha256: Hash payload using 256-bit key SHA-1 algorithm. sha384: Hash payload using 384-bit key SHA-1 algorithm. sha512: Hash payload using 512-bit key SHA-1 algorithm. aesMac Hash payload using AES-XCBC-MAC-96 algorithm. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 1), ("other", 2), ("md5", 3), ("sha", 4), ("tiger", 5), ("sha256", 6), ("sha384", 7), ("sha512", 8), ("aesMac", 9))

class CIPsecIkeAuthMethod(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The authentication method used in IPsec Phase-1 IKE negotiations. Description of enum constants of this type: preSharedKey: Peer authentication using pre-shared keys. rsaSignature: Peer authentication using digital signatures. rsaEncryption: Peer authentication using encrypted nonces. revRsaEncryption: Peer authentication using revised RSA encryption. dssSignature: Peer authentication using DSS signatures. elGamalEncryption: Peer authentication using El Gamal. revElGamalEncryption: Peer authentication using revised El Gamal. ecdsaSignature: Peer authentication using Elliptic Curve Digital Signatures. gssApiV1: Peer authentication using Generic Security Services API v1. gssApiV2: Peer authentication using Generic Security Services API v2. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("preSharedKey", 2), ("rsaSignature", 3), ("rsaEncryption", 4), ("revRsaEncryption", 5), ("dssSignature", 6), ("elGamalEncryption", 7), ("revElGamalEncryption", 8), ("ecsdaSignature", 9), ("gssApiV1", 10), ("gssApiV2", 11))

class CIPsecDiffHellmanGrp(TextualConvention, Integer32):
    reference = 'rfc2408, rfc2409 and rfc3526'
    description = " An indication of whether a Diffie Hellman Group has been specified to be used in negotiations and the type of group as follows. 'notDH' -- indicates no use of a Diffie Hellman 'modp768' -- 768-bit MODP 'modp1024' -- 1024-bit MODP 'modp1536' -- 1536-bit MODP group 'ec2nGP155' -- EC2N group on GP[2^155] 'ec2nGP185' -- EC2N group on GP[2^185] 'ec2nGF163' -- EC2N group over GF[2^163] 'ec2nGF283' -- EC2N group over GF[2^283] 'ec2nGF409' -- EC2N group over GF[2^409] 'ec2nGF571' -- EC2N group over GF[2^571] 'modp2048' -- 2048-bit MODP group "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("notDH", 2), ("modp768", 3), ("modp1024", 4), ("ec2nGP155", 5), ("ec2nGP185", 6), ("modp1536", 7), ("ec2nGF163", 8), ("ec2nGF283", 9), ("ec2nGF409", 10), ("ec2nGF571", 11), ("modp2048", 12))

class CIPsecEncapMode(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The encapsulation mode used by an IPsec Phase-2 Tunnel. The type enumerates values to denote the two modes of encapsulation of payload used by IPsec, viz., transport mode (encapTunnel) and tunnel mode (encapTransport). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("encapTunnel", 1), ("encapTransport", 2))

class CIPsecTransform(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The transform to be used by an IPsec Phase-2 protocol (ESP or AH or IPCP). Description of enum constants of this type: xformAhRFC1829: Authentication Header per RFC1829 xformAhMD5: Authentication Header using MD5 xformAhSHA1: Authentication Header using SHA1 xformEspNULL: ESP with NULL encryption. xformEspDES: ESP with DES encryption. xformEsp3DES: ESP with 3DES encryption. xformEspAES128: ESP with AES encryption using CBC mode (128-bit key). xformEspAES192: ESP with AES encryption using CBC mode (192-bit key). xformEspAES256: ESP with AES encryption using CBC mode (256-bit key). xformEspMD5: ESP with MD5 hash. xformEspSHA1: ESP with SHA-1 hash. xformCompLZS: IP compression using LZS. xformEspRc5: Payload encryption using RC5. xformEspIdea: Payload encryption using International Data Encryption Algorithm. xformEspCast: Payload encryption using CAST. xformEspTwofish: Payload encryption using TwoFish. xformEspBlowfish: Payload encryption using BlowFish. xformEsp3idea: Payload encryption using International Data Encryption Algorithm. xformEspRc4: Payload encryption using RC4. xformEspDesMac: ESP with DES MAC hash. xformEspHmacSha256: ESP with HMAC SHA-1 hash (256-bit key). xformEspHmacSha384: ESP with HMAC SHA-1 has (384-bit key). xformEspHmacSha512: ESP with HMAC SHA-1 has (512-bit key). xformEspRipemd: ESP with RIPEMD cryptographic hash. xformAHDesMac: AH with DES MAC hash. xformAHHmacSha256: AH with HMAC SHA-1 hash (256-bit key). xformAHHmacSha384: AH with HMAC SHA-1 hash (384-bit key). xformAHHmacSha512: AH with HMAC SHA-1 hash (512-bit key). xformAHRipemd: AH with RIPEMD cryptographic hash. xformEspAESXCbcMac: ESP with AES XCBC MAC authentication. xformAHAESXCbcMac: AH with AES XCBC MAC authentication. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("xformNONE", 1), ("xformOTHER", 2), ("xformAhRFC1829", 3), ("xformAhMD5", 4), ("xformAhSHA1", 5), ("xformEspNULL", 6), ("xformEspDES", 7), ("xformEsp3DES", 8), ("xformEspAES128", 9), ("xformEspAES192", 10), ("xformEspAES256", 11), ("xformEspMD5", 12), ("xformEspSHA1", 13), ("xformCompLZS", 14), ("xformEspAESCtr128", 15), ("xformEspAESCtr192", 16), ("xformEspAESCtr256", 17), ("xformEspRc5", 18), ("xformEspIdea", 19), ("xformEspCast", 20), ("xformEspTwofish", 21), ("xformEspBlowfish", 22), ("xformEsp3idea", 23), ("xformEspRc4", 24), ("xformEspDesMac", 25), ("xformEspHmacSha256", 26), ("xformEspHmacSha384", 27), ("xformEspHmacSha512", 28), ("xformEspRipemd", 29), ("xformAHDesMac", 30), ("xformAHHmacSha256", 31), ("xformAHHmacSha384", 32), ("xformAHHmacSha512", 33), ("xformAHRipemd", 34), ("xformEspAESXCbcMac", 35), ("xformAHAESXCbcMac", 36))

class CIPsecSecuritySuite(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = ' The combination of IPsec Phase-2 protocols. suiteConfEsp: Confidentiality using ESP. suiteIntegEsp: Confidentiality and Integrity check using ESP. suiteIntegAh: Integrity check with AH. suiteConfComp: Confidentiality using ESP; Packet compression. suiteIntegEspComp: Packet Integrity using ESP; Packet compression. suiteIntegAhComp: Packet Integrity using AH; Packet compression. suiteConfAh: Confidentiality using ESP; Packet Integrity using AH. suiteConfAhComp: Confidentiality using ESP; Packet Integrity using AH; Packet compression. suiteIntegEspAh: Packet Integrity using ESP and AH. suiteIntegEspAhComp: Packet Integrity using ESP and AH; Packet compression. suiteConfIntegEsp: Confidentiality and Packet Integrity using ESP. suiteConfIntegEspComp: Confidentiality and Packet Integrity using ESP; Packet compression. suiteConfIntegEspAh: Confidentiality using ESP; Packet Integrity using ESP and AH. suiteConfIntegEspAhComp: Confidentiality using ESP; Packet Integrity using ESP and AH; Packet compression. suiteOther: A suite that does not fit any of the above definitions. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("suiteOther", 1), ("suiteConfEsp", 2), ("suiteIntegEsp", 3), ("suiteIntegAh", 4), ("suiteConfComp", 5), ("suiteIntegEspComp", 6), ("suiteIntegAhComp", 7), ("suiteConfAh", 8), ("suiteConfAhComp", 9), ("suiteIntegEspAh", 10), ("suiteIntegEspAhComp", 11), ("suiteConfIntegEsp", 12), ("suiteConfIntegEspComp", 13), ("suiteConfIntegEspAh", 14), ("suiteConfIntegEspAhComp", 15))

class CIPsecNATTraversalMode(TextualConvention, Integer32):
    description = " The encapsulation mode used to implement NAT traversal. Both 'EncapMode' and 'NATTraversalMode' are attributes of a Phase-2 IPsec tunnel. Value of an object of this type is constrained based on the value of its tunnel encapsulation mode: if the tunnel encapsulation mode is 'encapTransport', then the value of this attribute may be one of 'natEncapNone' or 'natEncapNATT'. Description of enum constants of this type: natEncapIPsecOverUdp: IPsec encapsulation over UDP. natEncapIPsecOverTcp: IPsec encapsulation over TCP. natEncapNATT: IPsec encapsulation over NAT-T protocol. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("natEncapNone", 1), ("natEncapOther", 2), ("natEncapIPsecOverUdp", 3), ("natEncapIPsecOverTcp", 4), ("natEncapNATT", 5))

class CIPsecEncryptAlgorithm(TextualConvention, Integer32):
    description = " The encryption algorithm used in negotiations. Since payload encryption is done by the ESP protocol, these enums are prefixed with 'esp'. Description of enum constants of this type: espDes: Payload encryption using 56-bit key DES. esp3des: Payload encryption using 168-bit 3DES. espRc5: Payload encryption using RC5. espIdea: Payload encryption using International Data Encryption Algorithm. espCast: Payload encryption using CAST. espTwofish: Payload encryption using TwoFish. espBlowfish: Payload encryption using BlowFish. esp3idea: Payload encryption using International Data Encryption Algorithm. espRc4: Payload encryption using RC4. espNull: NULL Payload encryption. espAes128: espAes192: espAes256: Payload encryption using AES CBC mode and keysizes of 128, 192 and 256 bit keys. espAesCtr128: espAesCtr192: espAesCtr256: Payload encryption using AES CTR mode and keysizes of 128, 192 and 256 bit keys. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("none", 1), ("other", 2), ("espDes", 3), ("esp3des", 4), ("espRc5", 5), ("espIdea", 6), ("espCast", 7), ("espTwofish", 8), ("espBlowfish", 9), ("esp3idea", 10), ("espRc4", 11), ("espNull", 12), ("espAes128", 13), ("espAes192", 14), ("espAes256", 15), ("espAesCtr128", 16), ("espAesCtr192", 17), ("espAesCtr256", 18))

class CIPsecSpi(TextualConvention, Unsigned32):
    description = ' The type of the SPI (Security Parameter Index) associated with IPsec Phase-2 security associations. '
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(256, 4294967295)

class CIPsecAuthAlgorithm(TextualConvention, Integer32):
    description = ' The authentication algorithm used by a security association of an IPsec Phase-2 Tunnel. Description of enum constants of this type: hmacMd5: Hash validation using HMAC MD5. hmacSha: Hash validation using HMAC SHA-1. desMac: Hash validation using DES as MAC. hmacSha256: Hash validation using 256-bit SHA-1. hmacSha384: Hash validation using 384-bit SHA-1. hmacSha512: Hash validation using 512-bit SHA-1. ripemd: Hash validation using RIPEMD cryptographic hash function. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 1), ("other", 2), ("hmacMd5", 3), ("hmacSha", 4), ("desMac", 5), ("hmacSha256", 6), ("hmacSha384", 7), ("hmacSha512", 8), ("ripemd", 9))

class CIPsecCompAlgorithm(TextualConvention, Integer32):
    description = ' The compression algorithm used by a security association of an IPsec Phase-2 Tunnel. Description of enum constants of this type: compOui: IP payload compression using a proprietary algorithm identified using an Organization Unique Identifier (OUI). compDeflate: IP payload compression using deflate algorithm. compLzs: IP payload compression using LZS algorithm. compLzjh: IP payload compression using LZJH algorithm. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("other", 2), ("compOui", 3), ("compDeflate", 4), ("compLzs", 5), ("compLzjh", 6))

class CIPsecEndPtType(TextualConvention, Integer32):
    description = " The type of identity use to specify an IPsec End Point. For a description of the enum values, please refer to the description of type 'CIPsecPhase1PeerIdentityType'. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("idIpv4Addr", 2), ("idIpv4AddrRange", 3), ("idIpv4AddrSubnet", 4), ("idFqdn", 5), ("idUserFqdn", 6), ("idIpv6Addr", 7), ("idIpv6AddrRange", 8), ("idIpv6AddrSubnet", 9), ("idDerAsn1Dn", 10), ("idDerAsn1Gn", 11), ("idKeyId", 12))

class CIPsecPhase2SaDirection(TextualConvention, Integer32):
    reference = 'rfc2409'
    description = ' Phase-2 IPsec security associations are simplex. This textual convention is used as the type of attribute(s) of a Phase-2 security association. Description of enum constants of this type: saDirectionIn: The IPsec security association is used to process incoming traffic. saDirectionOut: The IPsec security association is used to process outgoing traffic. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("saDirectionUnknown", 1), ("saDirectionIn", 2), ("saDirectionOut", 3))

class CIPsecPhase1TunnelIndex(TextualConvention, Unsigned32):
    description = ' The index of the IPsec Phase-1 (IKE) Tunnel Table. An index of this type is a number which begins at 1 and is incremented with each tunnel that is created. The value of this object will wrap at 2,147,483,647. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CIPsecPhase1TunnelIndexOrZero(TextualConvention, Unsigned32):
    description = " This type defines a range of values for index of the IPsec Phase-1 (IKE) Tunnel Table, including the invalid index '0'. An object of this type is used to implement a soft reference to an IKE tunnel. The value of zero is used to denote the fact that the reference points to a non-existent IKE tunnel. "
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CIPsecPhase2TunnelIndex(TextualConvention, Unsigned32):
    description = ' The type of the index of the IPsec Phase-2 Tunnel Table. An index of this type is a number which begins at one and is incremented with each tunnel that is created. The value of this object will wrap at 2,147,483,647. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CIPsecPmtu(TextualConvention, Unsigned32):
    description = ' The type of the Path MTU (Maximum Transmission Unit) of an IPsec Phase-2 Tunnel. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(68, 1500)

class CIPsecLifetime(TextualConvention, Unsigned32):
    description = ' This type corresponds to the lifetime in seconds of IPsec Phase-2 security associations. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(120, 86400), )
class CIPsecLifesize(TextualConvention, Unsigned32):
    description = ' This type corresponds to the life-size of a Phase-2 security association in the number of kilobytes of data that has been processed by the security association. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2560, 4294967295), )
class CIPsecTunnelIdleTime(TextualConvention, Unsigned32):
    description = ' This type corresponds to the time interval specified in seconds during which no traffic has been processed by a Phase-2 security association. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 86400), )
class CIPsecNumCryptoMaps(TextualConvention, Gauge32):
    description = ' Integral units representing count of cryptomaps. '
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CIPsecTunnelStatus(TextualConvention, Integer32):
    description = ' This type represents the status of an IPsec Phase-1 or Phase-2 Tunnel. Objects of this type may be used to bring down the tunnel they represent by setting value of the object to destroy(5). Objects of this type cannot be used to create a tunnel. Description of enum constants of this type: initializePhase1: The tunnel is initializing Phase 1 operations (applies only to IKE tunnels). awaitXauth: The tunnel has concluded peer authentication successfully and is awaiting the completion of extended Authentication (applies only to IKE tunnels). awaitCommit: The tunnel has concluded initialization and is awaiting a signal (commit bit) from the peer to start operations. active: The tunnel is active. destroy: This value is used in SNMP SET operations to tear down the specified tunnel. rekey: This value is used in SNMP SET operations to force a rekeying. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initializePhase1", 1), ("awaitXauth", 2), ("awaitCommit", 3), ("active", 4), ("destroy", 5), ("rekey", 6))

class CIPsecCryptomapType(TextualConvention, Integer32):
    description = ' The type of a cryptomap entry. Cryptomap is a unit of IOS IPSec policy specification. Description of enum constants of this type: cryptomapTypeMANUAL: The cryptomap entry uses manual keying. cryptomapTypeISAKMP: The cryptomap entry uses IKE protocol for keying. cryptomapTypeDYNAMIC: The cryptomap entry is dynamically instantiated. cryptomapTypeDYNAMICDISCOVERY: The cryptomap entry is dynamically instantiated and uses tunnel endpoint discovery to identify the peer during tunnel setup. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cryptomapTypeNONE", 1), ("cryptomapTypeMANUAL", 2), ("cryptomapTypeISAKMP", 3), ("cryptomapTypeCET", 4), ("cryptomapTypeDYNAMIC", 5), ("cryptomapTypeDYNAMICDISCOVERY", 6))

class CIPsecCryptomapSetBindStatus(TextualConvention, Integer32):
    description = " The status of the binding of a cryptomap set to the specified interface. The value when queried is always 'attached'. When set to 'detached', the cryptomap set if detached from the specified interface. Setting the value to 'attached' will result in SNMP General Error. Description of enum constants of this type: attached: The cryptomap set is attached to an interface. detached: The cryptomap set is not attached to any interface. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("attached", 2), ("detached", 3))

class CIPsecIkePRFAlgorithm(TextualConvention, Integer32):
    description = ' The Pseudo Random Function algorithm used in IPsec Phase-1 IKEv2 negotiations. Description of enum constants of this type: prfHmacMd5: HMAC version of MDS. prfHmacSha1: HMAC version of SHA-1 algorithm '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("other", 2), ("prfHmacMd5", 3), ("prfHmacSha1", 4))

mibBuilder.exportSymbols("CISCO-IPSEC-TC", CIPsecCompAlgorithm=CIPsecCompAlgorithm, CIPsecControlProtocol=CIPsecControlProtocol, CIPsecEncapMode=CIPsecEncapMode, CIPsecPhase2SaDirection=CIPsecPhase2SaDirection, CIPsecPhase1TunnelIndex=CIPsecPhase1TunnelIndex, CCryptoMD5Hash=CCryptoMD5Hash, CIKELifetime=CIKELifetime, CIPsecTunnelIdleTime=CIPsecTunnelIdleTime, CIPsecCryptomapSetBindStatus=CIPsecCryptomapSetBindStatus, CIPsecLifesize=CIPsecLifesize, CIPsecEndPtType=CIPsecEndPtType, CIPsecTransform=CIPsecTransform, CIPsecLifetime=CIPsecLifetime, CIPsecNATTraversalMode=CIPsecNATTraversalMode, CIPsecSpi=CIPsecSpi, CIPsecPhase2TunnelIndex=CIPsecPhase2TunnelIndex, CIKELifesize=CIKELifesize, PYSNMP_MODULE_ID=ciscoIPsecTc, CIPsecTunnelStatus=CIPsecTunnelStatus, CIPsecPmtu=CIPsecPmtu, CIPsecIkeAuthMethod=CIPsecIkeAuthMethod, CIPsecNumCryptoMaps=CIPsecNumCryptoMaps, CIPsecPhase1TunnelIndexOrZero=CIPsecPhase1TunnelIndexOrZero, CIPsecCryptomapType=CIPsecCryptomapType, CIPsecIkeNegoMode=CIPsecIkeNegoMode, CIPsecSecuritySuite=CIPsecSecuritySuite, CIPsecIkePRFAlgorithm=CIPsecIkePRFAlgorithm, CIPsecEncryptionKeySize=CIPsecEncryptionKeySize, CIPsecDiffHellmanGrp=CIPsecDiffHellmanGrp, CIPsecPhase1PeerIdentityType=CIPsecPhase1PeerIdentityType, CIPsecProtocol=CIPsecProtocol, CIPsecIkeHashAlgorithm=CIPsecIkeHashAlgorithm, CIKEIsakmpDoi=CIKEIsakmpDoi, CIPsecAuthAlgorithm=CIPsecAuthAlgorithm, CIPsecEncryptAlgorithm=CIPsecEncryptAlgorithm, ciscoIPsecTc=ciscoIPsecTc)
