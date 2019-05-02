#
# PySNMP MIB module IPSEC-FLOW-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPSEC-FLOW-MIB-TC
# Produced by pysmi-0.3.4 at Wed May  1 13:56:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, ModuleIdentity, Counter32, Integer32, NotificationType, Bits, Gauge32, IpAddress, Counter64, MibIdentifier, iso, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter32", "Integer32", "NotificationType", "Bits", "Gauge32", "IpAddress", "Counter64", "MibIdentifier", "iso", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipsecFlowMibTC = ModuleIdentity((1, 3, 6, 1, 3, 170))
if mibBuilder.loadTexts: ipsecFlowMibTC.setLastUpdated('200302171158Z')
if mibBuilder.loadTexts: ipsecFlowMibTC.setOrganization('Tivoli Systems and Cisco Systems')
if mibBuilder.loadTexts: ipsecFlowMibTC.setContactInfo('Tivoli Systems Research Triangle Park, NC Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipsecmib@external.cisco.com bret_harrison@tivoli.com')
if mibBuilder.loadTexts: ipsecFlowMibTC.setDescription('This MIB module defines the textual conventions used in the IPsec Flow Monitoring MIB. This includes Internet DOI numbers defined in RFC 2407, ISAKMP numbers defined in RFC 2408, and IKE numbers defined in RFC 2409. Revision control of this document after publication will be under the authority of the IANA.')
class ControlProtocol(TextualConvention, Integer32):
    description = 'The protocol used for keying and control. The value of cp_none indicate manual administration of IPsec tunnels. This enumeration will be expanded as new keying protocols are standardized.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("cpNone", 1), ("cpIkev1", 2), ("cpIkev2", 3), ("cpKink", 4), ("cpOther", 5))

class Phase1PeerIdentityType(TextualConvention, Integer32):
    description = 'The type of IPsec Phase-1 peer identity. The peer may be identified by one of the ID types defined in IPSEC DOI. id_dn represent the binary DER encoding of the identity.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idDn", 3), ("idIpv6Addr", 4), ("idUserFqdn", 5), ("idIpv4AddrSubnet", 6), ("idIpv6AddrSubnet", 7), ("idIpv4AddrRange", 8), ("idIpv6AddrRange", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

class IkeNegoMode(TextualConvention, Integer32):
    description = 'The IPsec Phase-1 IKE negotiation mode.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("main", 1), ("aggressive", 2))

class IkeHashAlgo(TextualConvention, Integer32):
    description = 'The hash algorithm used in IPsec Phase-1 IKE negotiations.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("reserved", 0), ("md5", 1), ("sha", 2), ("tiger", 3), ("sha256", 4), ("sha384", 5), ("sha512", 6))

class IkeAuthMethod(TextualConvention, Integer32):
    description = 'The authentication method used in IPsec Phase-1 IKE negotiations.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("reserved", 0), ("preSharedKey", 1), ("dssSignature", 2), ("rsaSignature", 3), ("rsaEncryption", 4), ("revRsaEncryption", 5), ("elGamalEncryption", 6), ("revElGamalEncryption", 7), ("ecsdaSignature", 8), ("gssApiV1", 9), ("gssApiV2", 10))

class DiffHellmanGrp(TextualConvention, Integer32):
    description = 'The Diffie Hellman Group used in negotiations. reserved -- reserved groups modp768 -- 768-bit MODP modp1024 -- 1024-bit MODP modp1536 -- 1536-bit MODP group ec2nGP155 -- EC2N group on GP[2^155] ec2nGP185 -- EC2N group on GP[2^185] ec2nGF163 -- EC2N group over GF[2^163] ec2nGF283 -- EC2N group over GF[2^283] ec2nGF409 -- EC2N group over GF[2^409] ec2nGF571 -- EC2N group over GF[2^571] '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 8, 10, 12))
    namedValues = NamedValues(("reserved", 0), ("modp768", 1), ("modp1024", 2), ("ec2nGP155", 3), ("ec2nGP185", 4), ("modp1536", 5), ("ec2nGF163", 6), ("ec2nGF283", 8), ("ec2nGF409", 10), ("ec2nGF571", 12))

class EncapMode(TextualConvention, Integer32):
    description = 'The encapsulation mode used by an IPsec Phase-2 Tunnel.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("tunnel", 1), ("transport", 2))

class EncryptAlgo(TextualConvention, Integer32):
    description = 'The encryption algorithm used in negotiations.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("reserved", 0), ("espDes", 1), ("esp3des", 2), ("espRc5", 3), ("espIdea", 4), ("espCast", 5), ("espBlowfish", 6), ("esp3idea", 7), ("espRc4", 8), ("espNull", 9), ("espAes", 10))

class Spi(TextualConvention, Integer32):
    description = 'The type of the SPI associated with IPsec Phase-2 security associations.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(256, 4294967295)

class AuthAlgo(TextualConvention, Integer32):
    description = 'The authentication algorithm used by a security association of an IPsec Phase-2 Tunnel.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("reserved", 0), ("hmacMd5", 2), ("hmacSha", 3), ("desMac", 4), ("hmacSha256", 5), ("hmacSha384", 6), ("hmacSha512", 7), ("ripemd", 8))

class CompAlgo(TextualConvention, Integer32):
    description = 'The compression algorithm used by a security association of an IPsec Phase-2 Tunnel.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("compOui", 1), ("compDeflate", 2), ("compLzs", 3), ("compLzjh", 4))

class EndPtType(TextualConvention, Integer32):
    description = 'The type of identity use to specify an IPsec End Point.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idUserFqdn", 3), ("idIpv4AddrSubnet", 4), ("idIpv6Addr", 5), ("idIpv6AddrSubnet", 6), ("idIpv4AddrRange", 7), ("idIpv6AddrRange", 8), ("idDerAsn1Dn", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

mibBuilder.exportSymbols("IPSEC-FLOW-MIB-TC", Spi=Spi, ipsecFlowMibTC=ipsecFlowMibTC, IkeHashAlgo=IkeHashAlgo, Phase1PeerIdentityType=Phase1PeerIdentityType, EncapMode=EncapMode, EncryptAlgo=EncryptAlgo, IkeAuthMethod=IkeAuthMethod, DiffHellmanGrp=DiffHellmanGrp, ControlProtocol=ControlProtocol, AuthAlgo=AuthAlgo, PYSNMP_MODULE_ID=ipsecFlowMibTC, CompAlgo=CompAlgo, IkeNegoMode=IkeNegoMode, EndPtType=EndPtType)
