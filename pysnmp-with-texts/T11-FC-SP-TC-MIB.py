#
# PySNMP MIB module T11-FC-SP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T11-FC-SP-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Counter32, MibIdentifier, NotificationType, ObjectIdentity, mib_2, Unsigned32, Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity", "mib-2", "Unsigned32", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11FcTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 175))
t11FcTcMIB.setRevisions(('2008-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11FcTcMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC 5324.',))
if mibBuilder.loadTexts: t11FcTcMIB.setLastUpdated('200808200000Z')
if mibBuilder.loadTexts: t11FcTcMIB.setOrganization('This MIB module was developed through the coordinated effort of two organizations: T11 began the development and the IETF (in the IMSS Working Group) finished it.')
if mibBuilder.loadTexts: t11FcTcMIB.setContactInfo(' Claudio DeSanti Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 USA EMail: cds@cisco.com Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 USA Email: kzm@cisco.com')
if mibBuilder.loadTexts: t11FcTcMIB.setDescription('This MIB module defines Textual Conventions for use in the multiple MIB modules, which together define the instrumentation for an implementation of the Fibre Channel Security Protocols (FC-SP) specification. This MIB module also defines Object Identities (for use as possible values of MIB objects with syntax AutonomousType), including OIDs for the Cryptographic Algorithms defined in FC-SP. Copyright (C) The IETF Trust (2008). This version of this MIB module is part of RFC 5324; see the RFC itself for full legal notices.')
t11FcSpIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1))
t11FcSpAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1))
class T11FcSpPolicyHashFormat(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 7.1.3.1 and table 106. - FIPS PUB 180-2.'
    description = "Identifies a cryptographic hash function used to create a hash value that summarizes an FC-SP Policy Object. Each definition of an object with this TC as its syntax must be accompanied by a corresponding definition of an object with T11FcSpPolicyHashValue as its syntax, and containing the hash value. The first two cryptographic hash functions are: Hash Type Hash Tag Hash Length (Bytes) SHA-1 '00000001'h 20 SHA-256 '00000002'h 32 "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class T11FcSpPolicyHashValue(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 7.1.3.1 and table 106.'
    description = 'Represents the value of the cryptographic hash function of an FC-SP Policy Object. Each definition of an object with this TC as its syntax must be accompanied by a corresponding definition of an object with T11FcSpPolicyHashFormat as its syntax. The corresponding object identifies the cryptographic hash function used to create the hash value.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class T11FcSpHashCalculationStatus(TextualConvention, Integer32):
    description = "When some kind of 'database' is defined in a set of read-write MIB objects, it is common that multiple changes in the data need to be made at the same time. So, if hash values are maintained for that data, those hash values are only correct if and when they are re-calculated after every change. In such circumstances, the use of an object with this syntax allows the re-calculation of the hash values to be deferred until all changes have been made, and therefore the calculation need only be done once after all changes, rather than repeatedly/after each individual change. The definition of an object defined using this TC is required to specify which one or more instances of which MIB objects contain the hash values operated upon (or whose status is given) by the value of this TC. When read, the value of an object with this syntax is either: correct -- the identified MIB object instance(s) contain the correct hash values; or stale -- the identified MIB object instance(s) contain stale (possibly incorrect) values. Writing a value of 'calculate' is a request to re-calculate and update the values of the corresponding instances of the identified MIB objects. Writing a value of 'correct' or 'stale' to this object is an error (e.g., 'wrongValue')."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("calculate", 1), ("correct", 2), ("stale", 3))

class T11FcSpAuthRejectReasonCode(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 17, 48, 52.'
    description = 'A reason code contained in an AUTH_Reject message, or in an SW_RJT (rejecting an AUTH_ILS), or in an LS_RJT (rejecting an AUTH-ELS).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("authFailure", 1), ("logicalError", 2), ("logicalBusy", 3), ("authILSNotSupported", 4), ("authELSNotSupported", 5), ("notLoggedIn", 6))

class T11FcSpAuthRejReasonCodeExp(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Tables 18, 48, 52.'
    description = 'A reason code explanation contained in an AUTH_Reject message, or in an SW_RJT (rejecting an AUTH_ILS), or in an LS_RJT (rejecting an AUTH-ELS).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("authMechanismNotUsable", 1), ("dhGroupNotUsable", 2), ("hashFunctionNotUsable", 3), ("authTransactionAlreadyStarted", 4), ("authenticationFailed", 5), ("incorrectPayload", 6), ("incorrectAuthProtocolMessage", 7), ("restartAuthProtocol", 8), ("authConcatNotSupported", 9), ("unsupportedProtocolVersion", 10), ("logicalBusy", 11), ("authILSNotSupported", 12), ("authELSNotSupported", 13), ("notLoggedIn", 14))

class T11FcSpHashFunctions(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 14.'
    description = 'A set of zero, one, or more hash functions defined for use in FC-SP.'
    status = 'current'
    namedValues = NamedValues(("md5", 0), ("sha1", 1))

class T11FcSpSignFunctions(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, tables 38 & 39.'
    description = 'A set of zero, one, or more signature functions defined for signing certificates for use with FCAP in FC-SP.'
    status = 'current'
    namedValues = NamedValues(("rsaSha1", 0))

class T11FcSpDhGroups(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 15.'
    description = 'A set of zero, one, or more DH Groups defined for use in FC-SP.'
    status = 'current'
    namedValues = NamedValues(("null", 0), ("group1024", 1), ("group1280", 2), ("group1536", 3), ("group2048", 4), ("group3072", 5), ("group4096", 6), ("group6144", 7), ("group8192", 8))

class T11FcSpPolicyObjectType(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 102.'
    description = 'A value that identifies the type of an FC-SP Policy Object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("summary", 1), ("switchMemberList", 2), ("nodeMemberList", 3), ("switchConnectivity", 4), ("ipMgmtList", 5), ("attribute", 6))

class T11FcSpPolicyNameType(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 103.'
    description = "The format and usage of a companion object having T11FcSpPolicyName as its syntax. Six of the values indicate the same format, i.e., they differ only in semantics. That common format is a Fibre Channel 'Name_Identifier', i.e., the same syntax as 'FcNameIdOrZero (SIZE(8))'. These six are three pairs of one restricted and one unrestricted. Each usage of this syntax must specify what the meaning of 'restricted' is for that usage and how the characteristics and behavior of restricted names differ from unrestricted names. The six are: 'nodeName' - a Node_Name, which is the Name_Identifier associated with a Fibre Channel Node. 'restrictedNodeName' - a Restricted Node_Name. 'portName' - the Name_Identifier associated with a Fibre Channel Port. 'restrictedPortName' - a Restricted Port_Name. 'wildcard' - a Wildcard value that is used to identify 'all others' (typically, all other members of a Policy Object, not all other Policy Objects). 'restrictedWildcard' - a Restricted Wildcard value. Other possible values are: 'alphaNumericName' - the value begins with an ASCII letter (upper or lower case) followed by (0 ... 63) characters from the set: lower case letters, upper case letters, digits, and the four symbols: dollar-sign ($), dash (-), caret (^), and underscore (_). 'ipv6AddressRange' - two IPv6 addresses in network byte order, the numerically smallest first and the numerically largest second; total length is 32 bytes. 'ipv4AddressRange' - two IPv4 addresses in network byte order, the numerically smallest first and the numerically largest second; total length is 8 bytes."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("nodeName", 1), ("restrictedNodeName", 2), ("portName", 3), ("restrictedPortName", 4), ("wildcard", 5), ("restrictedWildcard", 6), ("alphaNumericName", 7), ("ipv6AddressRange", 8), ("ipv4AddressRange", 9))

class T11FcSpPolicyName(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 103.'
    description = "A syntax used, when defining Policy Objects, for the name of something. An object that uses this syntax always identifies a companion object with syntax T11FcSpPolicyNameType such that the companion object specifies the format and usage of the object with this syntax. When the companion object has the value 'wildcard' or 'restrictedWildcard', the value of the T11FcSpPolicyName object is: '0000000000000000'h."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class T11FcSpAlphaNumName(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 103.'
    description = "A syntax used when defining Policy Objects for the name of something, where the name is always in the format specified by: T11FcSpPolicyNameType = 'alphaNumericName' "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class T11FcSpAlphaNumNameOrAbsent(TextualConvention, OctetString):
    description = 'An extension of the T11FcSpAlphaNumName TC with one additional possible value: the zero-length string to indicate the absence of a name.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class T11FcSaDirection(TextualConvention, Integer32):
    description = 'The direction of frame transmission on a Security Association. Note that Security Associations are unidirectional, but they always exist as part of an SA pair of the same type in opposite directions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ingress", 1), ("egress", 2))

class T11FcSpiIndex(TextualConvention, Unsigned32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 4.7.2 and 4.7.3.'
    description = 'An SPI (Security Parameter Index) value is carried in the SPI field of a frame protected by the ESP_Header. An SPI is also carried in the SAID field of a Common Transport Information Unit (CT_IU) protected by CT_Authentication. An SPI value identifies the Security Association on which the frame is being transmitted.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class T11FcSpPrecedence(TextualConvention, Unsigned32):
    description = 'The precedence of a Traffic Selector. If a frame matches with two or more Traffic Selectors, then the match that takes precedence is the one with the Traffic Selector having the numerically smallest precedence value. Note that precedence values are not necessarily contiguous.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class T11FcRoutingControl(TextualConvention, OctetString):
    reference = '- Fibre Channel - Framing and Signaling-2 (FC-FS-2), ANSI INCITS 424-2007, Project T11/1619-D, February 2007, section 9.3. - Fibre Channel - Generic Services-5 (FC-GS-5), ANSI INCITS 427-2006, sections 4.5.2.4.2, 4.5.2.4.3 and table 12.'
    description = "A value stored in the R_CTL (Routing Control) 8-bit field of an FC-2 frame containing routing and information bits to categorize the frame function. For FC-2 frames, an R_CTL value typically distinguishes between control versus data frames and/or solicited versus unsolicited frames, and in combination with the TYPE field (see T11FcSpType), identifies a particular link-layer service/protocol using FC-2. For CT_Authentication, the information field in the R_CTL field contains '02'h for Request CT_IUs and '03'h for Response CT_IUs. The comparison of two values having this syntax is done by treating each string as an 8-bit numeric value."
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class T11FcSpType(TextualConvention, OctetString):
    reference = '- Fibre Channel - Framing and Signaling-2 (FC-FS-2), ANSI INCITS 424-2007, Project T11/1619-D, February 2007, section 9.6. - Fibre Channel - Generic Services-5 (FC-GS-5), ANSI INCITS 427-2006, sections 4.3.2.4 and 4.3.2.5.'
    description = "A value, or combination of values, contained in a frame header used in identifying the link layer service/protocol of a frame. The value is always two octets: - for FC-2 frames, the first octet is zero and the second octet contains the Data structure type (TYPE) value defined by FC-FS-2. The TYPE value is used in combination with T11FcRoutingControl to identify a link layer service/protocol. - for Common Transport Information Units (CT_IUs), the first octet contains a GS_Type value and the second octet contains a GS_Subtype value, defined by FC-GS-5. The comparison of two values having this syntax is done by treating each string as the numeric value obtained by numerically combining the individual octet's value as follows: (256 * 1st-octet) + 2nd-octet "
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class T11FcSpTransforms(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Appendix A.3.1, tables A.23, A.24, A.25, A.26.'
    description = 'A list of the standardized transforms that are defined by FC-SP for use with ESP_Header, CT_Authentication, and/or IKEv2 Support.'
    status = 'current'
    namedValues = NamedValues(("encrNull", 0), ("encrAesCbc", 1), ("encrAesCtr", 2), ("encrAesGcm", 3), ("encr3Des", 4), ("prfHmacMd5", 5), ("prfHmacSha1", 6), ("prfAesCbc", 7), ("authHmacMd5L96", 8), ("authHmacSha1L96", 9), ("authHmacMd5L128", 10), ("authHmacSha1L160", 11), ("encrNullAuthAesGmac", 12), ("dhGroups1024bit", 13), ("dhGroups2048bit", 14))

class T11FcSpSecurityProtocolId(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 6.3.2.2 and table 67.'
    description = 'A Security Protocol identifier to identify the protocol by which traffic is to be protected, e.g., ESP_Header or CT_Authentication.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("espHeader", 1), ("ctAuth", 2))

class T11FcSpLifetimeLeft(TextualConvention, Unsigned32):
    description = 'This TC is used for one object of an associated pair of objects. The object with this syntax specifies a remaining lifetime of something, e.g., of an SA, where the lifetime is given in the units specified by the other object of the pair which has T11FcSpLifetimeLeftUnits as its syntax.'
    status = 'current'

class T11FcSpLifetimeLeftUnits(TextualConvention, Integer32):
    description = 'An object, defined using T11FcSpLifetimeLeft TC as its syntax, is required to be one of an associated pair of objects such that the other object of the pair is defined with this T11FcSpLifetimeLeftUnits TC as its syntax and with its value specifying the units of the remaining lifetime given by the value of the T11FcSpLifetimeLeft object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("seconds", 1), ("kiloBytes", 2), ("megaBytes", 3), ("gigaBytes", 4), ("teraBytes", 5), ("petaBytes", 6), ("exaBytes", 7), ("zettaBytes", 8), ("yottaBytes", 9))

t11FcSpEncryptAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1, 1))
t11FcSpEncrNull = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 1))
if mibBuilder.loadTexts: t11FcSpEncrNull.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrNull.setDescription('The ENCR_NULL algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrNull.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 70.')
t11FcSpEncrAesCbc = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 2))
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setDescription('The ENCR_AES_CBC algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 70.')
t11FcSpEncrAesCtr = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 3))
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setDescription('The ENCR_AES_CTR algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 70.')
t11FcSpEncrAesGcm = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 4))
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setDescription('The ENCR_AES_GCM algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 70.')
t11FcSpEncr3Des = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 5))
if mibBuilder.loadTexts: t11FcSpEncr3Des.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncr3Des.setDescription('The ENCR_3DES algorithm.')
if mibBuilder.loadTexts: t11FcSpEncr3Des.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 70.')
t11FcSpAuthAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1, 2))
t11FcSpAuthNull = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 1))
if mibBuilder.loadTexts: t11FcSpAuthNull.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthNull.setDescription('The AUTH_NONE algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthNull.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 72.')
t11FcSpAuthHmacMd5L96 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 2))
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setDescription('The AUTH_HMAC_MD5_96 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 72.')
t11FcSpAuthHmacSha1L96 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 3))
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setDescription('The AUTH_HMAC_SHA1_96 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 72.')
t11FcSpAuthHmacMd5L128 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 4))
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setDescription('The AUTH_HMAC_MD5_128 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 72.')
t11FcSpAuthHmacSha1L160 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 5))
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setDescription('The AUTH_HMAC_SHA1_160 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 72.')
t11FcSpEncrNullAuthAesGmac = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 6))
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setDescription('The ENCR_NULL_AUTH_AES_GMAC algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 70.')
mibBuilder.exportSymbols("T11-FC-SP-TC-MIB", PYSNMP_MODULE_ID=t11FcTcMIB, T11FcRoutingControl=T11FcRoutingControl, t11FcSpIdentities=t11FcSpIdentities, T11FcSpLifetimeLeft=T11FcSpLifetimeLeft, T11FcSpHashFunctions=T11FcSpHashFunctions, T11FcSpPolicyNameType=T11FcSpPolicyNameType, t11FcSpEncrAesCbc=t11FcSpEncrAesCbc, T11FcSpPolicyHashValue=T11FcSpPolicyHashValue, t11FcSpEncrNull=t11FcSpEncrNull, T11FcSpTransforms=T11FcSpTransforms, T11FcSpSecurityProtocolId=T11FcSpSecurityProtocolId, T11FcSpPolicyObjectType=T11FcSpPolicyObjectType, t11FcSpAlgorithms=t11FcSpAlgorithms, T11FcSpPolicyName=T11FcSpPolicyName, t11FcSpEncrNullAuthAesGmac=t11FcSpEncrNullAuthAesGmac, t11FcSpAuthHmacMd5L96=t11FcSpAuthHmacMd5L96, T11FcSpAuthRejReasonCodeExp=T11FcSpAuthRejReasonCodeExp, t11FcSpEncr3Des=t11FcSpEncr3Des, T11FcSaDirection=T11FcSaDirection, t11FcSpEncrAesCtr=t11FcSpEncrAesCtr, t11FcSpAuthHmacSha1L160=t11FcSpAuthHmacSha1L160, T11FcSpType=T11FcSpType, t11FcSpAuthNull=t11FcSpAuthNull, T11FcSpAlphaNumName=T11FcSpAlphaNumName, T11FcSpAlphaNumNameOrAbsent=T11FcSpAlphaNumNameOrAbsent, T11FcSpHashCalculationStatus=T11FcSpHashCalculationStatus, T11FcSpSignFunctions=T11FcSpSignFunctions, T11FcSpLifetimeLeftUnits=T11FcSpLifetimeLeftUnits, T11FcSpDhGroups=T11FcSpDhGroups, t11FcSpAuthHmacMd5L128=t11FcSpAuthHmacMd5L128, T11FcSpPolicyHashFormat=T11FcSpPolicyHashFormat, t11FcSpEncryptAlgorithms=t11FcSpEncryptAlgorithms, T11FcSpAuthRejectReasonCode=T11FcSpAuthRejectReasonCode, t11FcSpEncrAesGcm=t11FcSpEncrAesGcm, t11FcSpAuthAlgorithms=t11FcSpAuthAlgorithms, t11FcSpAuthHmacSha1L96=t11FcSpAuthHmacSha1L96, t11FcTcMIB=t11FcTcMIB, T11FcSpiIndex=T11FcSpiIndex, T11FcSpPrecedence=T11FcSpPrecedence)
