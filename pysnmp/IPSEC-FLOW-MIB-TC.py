#
# PySNMP MIB module IPSEC-FLOW-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPSEC-FLOW-MIB-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Bits, Gauge32, MibIdentifier, Unsigned32, Integer32, Counter32, NotificationType, ObjectIdentity, IpAddress, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Bits", "Gauge32", "MibIdentifier", "Unsigned32", "Integer32", "Counter32", "NotificationType", "ObjectIdentity", "IpAddress", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "experimental")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipsecFlowMibTC = ModuleIdentity((1, 3, 6, 1, 3, 170))
if mibBuilder.loadTexts: ipsecFlowMibTC.setLastUpdated('200302171158Z')
if mibBuilder.loadTexts: ipsecFlowMibTC.setOrganization('Tivoli Systems and Cisco Systems')
class ControlProtocol(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("cpNone", 1), ("cpIkev1", 2), ("cpIkev2", 3), ("cpKink", 4), ("cpOther", 5))

class Phase1PeerIdentityType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idDn", 3), ("idIpv6Addr", 4), ("idUserFqdn", 5), ("idIpv4AddrSubnet", 6), ("idIpv6AddrSubnet", 7), ("idIpv4AddrRange", 8), ("idIpv6AddrRange", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

class IkeNegoMode(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("main", 1), ("aggressive", 2))

class IkeHashAlgo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("reserved", 0), ("md5", 1), ("sha", 2), ("tiger", 3), ("sha256", 4), ("sha384", 5), ("sha512", 6))

class IkeAuthMethod(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("reserved", 0), ("preSharedKey", 1), ("dssSignature", 2), ("rsaSignature", 3), ("rsaEncryption", 4), ("revRsaEncryption", 5), ("elGamalEncryption", 6), ("revElGamalEncryption", 7), ("ecsdaSignature", 8), ("gssApiV1", 9), ("gssApiV2", 10))

class DiffHellmanGrp(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 8, 10, 12))
    namedValues = NamedValues(("reserved", 0), ("modp768", 1), ("modp1024", 2), ("ec2nGP155", 3), ("ec2nGP185", 4), ("modp1536", 5), ("ec2nGF163", 6), ("ec2nGF283", 8), ("ec2nGF409", 10), ("ec2nGF571", 12))

class EncapMode(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("tunnel", 1), ("transport", 2))

class EncryptAlgo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("reserved", 0), ("espDes", 1), ("esp3des", 2), ("espRc5", 3), ("espIdea", 4), ("espCast", 5), ("espBlowfish", 6), ("esp3idea", 7), ("espRc4", 8), ("espNull", 9), ("espAes", 10))

class Spi(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(256, 4294967295)

class AuthAlgo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("reserved", 0), ("hmacMd5", 2), ("hmacSha", 3), ("desMac", 4), ("hmacSha256", 5), ("hmacSha384", 6), ("hmacSha512", 7), ("ripemd", 8))

class CompAlgo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("compOui", 1), ("compDeflate", 2), ("compLzs", 3), ("compLzjh", 4))

class EndPtType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idUserFqdn", 3), ("idIpv4AddrSubnet", 4), ("idIpv6Addr", 5), ("idIpv6AddrSubnet", 6), ("idIpv4AddrRange", 7), ("idIpv6AddrRange", 8), ("idDerAsn1Dn", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

mibBuilder.exportSymbols("IPSEC-FLOW-MIB-TC", IkeHashAlgo=IkeHashAlgo, EncryptAlgo=EncryptAlgo, AuthAlgo=AuthAlgo, ipsecFlowMibTC=ipsecFlowMibTC, ControlProtocol=ControlProtocol, EndPtType=EndPtType, Phase1PeerIdentityType=Phase1PeerIdentityType, DiffHellmanGrp=DiffHellmanGrp, CompAlgo=CompAlgo, IkeAuthMethod=IkeAuthMethod, PYSNMP_MODULE_ID=ipsecFlowMibTC, Spi=Spi, EncapMode=EncapMode, IkeNegoMode=IkeNegoMode)
