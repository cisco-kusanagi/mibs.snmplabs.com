#
# PySNMP MIB module ONEACCESS-GDOI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-GDOI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, iso, Bits, TimeTicks, Counter64, IpAddress, Gauge32, MibIdentifier, Unsigned32, NotificationType, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "iso", "Bits", "TimeTicks", "Counter64", "IpAddress", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacExpIMGdoiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224))
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setLastUpdated('1404151200Z')
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setOrganization('ONE ACCESS')
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 54 Fax: (+33) 01 41 87 74 39 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setDescription('This MIB module defines objects for managing the GDOI protocol')
class OacGdoiIdentificationType(TextualConvention, Integer32):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry"
    description = "A textual convention indicating the type of value used to identify a GDOI entity (i.e. Group, or Group Member). Following are the Identification Type Values: ID Type Value ------- ----- ID_KEY_ID 1 -- groupNumber ID_IPV4_ADDR 2 -- ipv4Address Following are the mappings to the type values above: 'keyID' : group number key identifier. 'ipv4' : IPv4 address."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("keyID", 1), ("ipv4", 2))

class OacGdoiIdentificationValue(TextualConvention, OctetString):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry"
    description = 'A textual convention indicating the actual value of used to identify a GDOI entity (i.e. Group or Group Member). The value of the oacGdoiIdentificationValue object can be parsed based on the value of the associated oacGdoiIdentificationType object'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class OacGdoiSPI(TextualConvention, OctetString):
    reference = 'RFC 3547 - Section: 5.3. SA KEK Payload'
    description = 'A textual convention indicating a SPI (Security Parameter Index)'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class OacGdoiKEKEncryptionAlgorithm(TextualConvention, Integer32):
    reference = "IANA IKEv2 Parameters Section: Encryption Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters IANA 'Magic Numbers' for ISAMP Protocol Section: IPSEC ESP Transform Identifiers http://www.iana.org/assignments/isakmp-registry RFC 2407 - Section: 4.4.4. IPSEC ESP Transform Identifiers RFC 3547 - Section: 5.3.3. KEK_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4106, 4309, 4543, 5282, 5529"
    description = 'A textual convention indicating the identifier of the KEK encryption algorithm being used'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enc-des", 1), ("enc-3des", 2), ("enc-aes", 3))

class OacGdoiHashAlogrithm(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Pseudo-random Function Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4615, 4868'
    description = 'A textual convention indicating the identifier of the hash algorithm being used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha1", 2))

class OacGdoiSignatureMethod(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Integrity Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 2407 - Section: 4.5. IPSEC Security Assoc. Attributes RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4494, 4543, 4595, 4868'
    description = 'A textual convention indicating the identifier of the integirty algorithm being used'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rsa", 1), ("dss", 2), ("ecdss", 3))

oacGdoiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1))
oacGdoiGroupTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1), )
if mibBuilder.loadTexts: oacGdoiGroupTable.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGroupTable.setDescription('A table of information regarding GDOI Groups in use on the network device being queried.')
oacGdoiGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"))
if mibBuilder.loadTexts: oacGdoiGroupEntry.setReference('RFC 3547 - Sections: 5.1.1. Identification Type Values 5.1.1.1. ID_KEY_ID RFC 4306 - Section: 3.5. Identification Payloads')
if mibBuilder.loadTexts: oacGdoiGroupEntry.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGroupEntry.setDescription('An entry containing GDOI Group information, uniquely identified by the GDOI Group ID.')
oacGdoiGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupName.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGroupName.setDescription('The string-readable name configured for or given to a GDOI Group.')
oacGdoiGroupIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 2), OacGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupIdType.setReference('RFC 3547 - Sections: 5.1.1. Identification Type Values 5.1.1.1. ID_KEY_ID RFC 4306 - Section: 3.5. Identification Payloads')
if mibBuilder.loadTexts: oacGdoiGroupIdType.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGroupIdType.setDescription('The Identification Type Value used to parse a GDOI Group ID. The GDOI RFC 3547 defines the types that can be used as a GDOI Group ID, and RFC 4306 defines all valid types that can be used as an identifier.')
oacGdoiGroupIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupIdValue.setReference('RFC 3547 - Sections: 5.1.1. Identification Type Values 5.1.1.1. ID_KEY_ID RFC 4306 - Section: 3.5. Identification Payloads')
if mibBuilder.loadTexts: oacGdoiGroupIdValue.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGroupIdValue.setDescription("The value of a Group ID with its type indicated by the oacGdoiGroupIdType. Use the oacGdoiGroupIdType to parse the Group ID correctly. This Group ID value is sent as the 'Identification Data' field of the Identification Payload for a GDOI GROUPKEY-PULL exchange.")
oacGdoiGm = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2))
oacGdoiPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3))
oacGdoiGmTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2), )
if mibBuilder.loadTexts: oacGdoiGmTable.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmTable.setDescription('A table of information regarding GDOI Group Members (GMs) locally configured on the network device being queried. Note that Local Group Members may or may not be registered to a Key Server in its GDOI Group on the same network device being queried.')
oacGdoiGmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"), (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmActiveKEK"))
if mibBuilder.loadTexts: oacGdoiGmEntry.setReference('RFC 3547 - Sections: 1. Introduction 3.3. Initiator Operations 4.8. Group Member Operations')
if mibBuilder.loadTexts: oacGdoiGmEntry.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmEntry.setDescription('An entry containing Local GDOI Group Member information, uniquely identified by Group & GM IDs. Because the Group Member is Local to the network device being queried, TEKs installed for this Group Member can be queried as well.')
oacGdoiGmIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 1), OacGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmIdType.setReference('RFC 3547 - Sections: 5.3. SA KEK payload 5.4.1. PROTO_IPSEC_ESP RFC 4306 - Section: 3.5. Identification Payloads')
if mibBuilder.loadTexts: oacGdoiGmIdType.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmIdType.setDescription("The Identification Type Value used to parse the identity information for a Initiator or Group Member. RFC 4306 defines all valid types that can be used as an identifier. These identification types are sent as the 'SRC ID Type' and 'DST ID Type' of the KEK and TEK payloads for GDOI GROUPKEY-PULL and GROUPKEY-PUSH exchanges.")
oacGdoiGmIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 2), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmIdValue.setReference('RFC 3547 - Sections: 5.3. SA KEK payload 5.4.1. PROTO_IPSEC_ESP')
if mibBuilder.loadTexts: oacGdoiGmIdValue.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmIdValue.setDescription("The value of the identity information for a Group Member with its type indicated by the oacGdoiGmIdType. Use the oacGdoiGmIdType to parse the Group Member ID correctly. This Group Member ID value is sent as the 'SRC Identification Data' and 'DST Identification Data' of the KEK and TEK payloads for GDOI GROUPKEY-PULL and GROUPKEY-PUSH exchanges.")
oacGdoiGmRegKeyServerIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmRegKeyServerIdValue.setReference('RFC 3547 - Sections: 5.3. SA KEK payload 5.4.1. PROTO_IPSEC_ESP')
if mibBuilder.loadTexts: oacGdoiGmRegKeyServerIdValue.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmRegKeyServerIdValue.setDescription("The value of the identity information for this Group Member's registered Key Server with its type indicated by the oacGdoiGmRegKeyServerIdType. Use the oacGdoiGmRegKeyServerIdType to parse the registered Key Server's ID correctly. This Key Server ID value is sent as the 'SRC Identification Data' and 'DST Identification Data' of the KEK and TEK payloads for GDOI GROUPKEY-PULL and GROUPKEY-PUSH exchanges.")
oacGdoiGmActiveKEK = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 4), OacGdoiSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmActiveKEK.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmActiveKEK.setDescription('The SPI of the Key Encryption Key (KEK) that is currently being used by the Group Member to authenticate & decrypt a rekey from a GROUPKEY-PUSH message.')
oacGdoiGmRekeysReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 5), Counter32()).setUnits('GROUPKEY-PUSH Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmRekeysReceived.setReference('RFC 3547 - Sections: 3.2. Messages 3.3. Initiator Operations 4. GROUPKEY-PUSH Message 4.8. Group Member Operations 5.6. Sequence Number Payload')
if mibBuilder.loadTexts: oacGdoiGmRekeysReceived.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmRekeysReceived.setDescription("The sequence number of the last rekey successfully received from this Group Member's registered Key Server.")
oacGdoiGmKekTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2), )
if mibBuilder.loadTexts: oacGdoiGmKekTable.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekTable.setDescription('A table of information regarding GDOI Key Encryption Key (KEK) Security Associations (SAs) currently installed for GDOI entities acting as Group Members on the network device being queried. There is one entry in this table for each KEK SA that has been installed and not yet deleted. Each KEK SA is uniquely identified by a SPI at any given time.')
oacGdoiGmKekEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"), (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmKekSPI"))
if mibBuilder.loadTexts: oacGdoiGmKekEntry.setReference('RFC 3547 - Sections: 1. Introduction 3.2. Messages 4. GROUPKEY-PUSH Message 5.3. SA KEK Payload 5.3.1. KEK Attributes 5.5. Key Download Payload')
if mibBuilder.loadTexts: oacGdoiGmKekEntry.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekEntry.setDescription("An entry containing the attributes associated with a GDOI KEK SA, uniquely identified by the Group ID, Group Member (GM) ID, & SPI value assigned by the GM's registered Key Server to the KEK. There will be at least one KEK SA entry for each GM & two KEK SA entries for a given GM only during a KEK rekey when a new KEK is received & installed. The KEK SPI is unique for every KEK for a given Group Member.")
oacGdoiGmKekSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 1), OacGdoiSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSPI.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekSPI.setDescription("The value of the Security Parameter Index (SPI) of a KEK SA. The SPI must be the ISAKMP Header cookie pair where the first 8 octets become the 'Initiator Cookie' field of the GROUPKEY-PUSH message ISAKMP HDR, and the second 8 octets become the 'Responder Cookie' in the same HDR. As described above, these cookies are assigned by the GCKS.")
oacGdoiGmKekSrcIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 2), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSrcIdValue.setReference('RFC 3547 - Sections: 5.3. SA KEK payload')
if mibBuilder.loadTexts: oacGdoiGmKekSrcIdValue.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekSrcIdValue.setDescription("The value of the identity information for the source of a KEK SA with its type indicated by the oacGdoiGmKekSrcIdType. Use the oacGdoiGmKekSrcIdType to parse the KEK Source ID correctly. This ID value is sent as the 'SRC Identification Data' of a KEK payload.")
oacGdoiGmKekDstIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekDstIdValue.setReference('RFC 3547 - Sections: 5.3. SA KEK payload')
if mibBuilder.loadTexts: oacGdoiGmKekDstIdValue.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekDstIdValue.setDescription("The value of the identity information for the destination of a KEK SA (multicast rekey address) with its type indicated by oacGdoiGmKekDstIdType. Use the oacGdoiGmKekDstIdType to parse the KEK Dest. ID correctly. This ID value is sent as the 'DST Identification Data' of a KEK payload.")
oacGdoiGmKekEncryptAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 4), OacGdoiKEKEncryptionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekEncryptAlg.setReference('RFC 3547 - Section 5.3.3. KEK_ALGORITHM')
if mibBuilder.loadTexts: oacGdoiGmKekEncryptAlg.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekEncryptAlg.setDescription('The value of the KEK_ALGORITHM which specifies the encryption algorithm used with the KEK SA. A GDOI implementaiton must support KEK_ALG_3DES. Following are the KEK encryption algoritm values defined in the GDOI RFC 3547, however the oacGdoiEncryptionAlgorithm TC defines all possible values. Algorithm Type Value -------------- ----- KEK_ALG_DES 1 KEK_ALG_3DES 2 KEK_ALG_AES 3')
oacGdoiGmKekEncryptKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 5), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekEncryptKeyLength.setReference('RFC 3547 - Section: 5.3.4. KEK_KEY_LENGTH')
if mibBuilder.loadTexts: oacGdoiGmKekEncryptKeyLength.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekEncryptKeyLength.setDescription('The value of the KEK_KEY_LENGTH which specifies the KEK Algorithm key length (in bits).')
oacGdoiGmKekSigHashAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 6), OacGdoiHashAlogrithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigHashAlg.setReference('RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM')
if mibBuilder.loadTexts: oacGdoiGmKekSigHashAlg.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekSigHashAlg.setDescription('The value of the SIG_HASH_ALGORITHM which specifies the SIG payload hash algorithm. This is not required (i.e. could have a value of zero) if the SIG_ALGORITHM is SIG_ALG_DSS or SIG_ALG_ECDSS, which imply SIG_HASH_SHA1 (i.e. must have a value of zero or SIG_HASH_SHA1)')
oacGdoiGmKekSigAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 7), OacGdoiSignatureMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigAlg.setReference('RFC 3547 - Section: 5.3.7. SIG_ALGORITHM')
if mibBuilder.loadTexts: oacGdoiGmKekSigAlg.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekSigAlg.setDescription('The value of the SIG_ALGORITHM which specifies the SIG payload signature algorithm. A GDOI implementation must support SIG_ALG_RSA')
oacGdoiGmKekSigKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 8), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigKeyLength.setReference('RFC 3547 - Section 5.3.8. SIG_KEY_LENGTH')
if mibBuilder.loadTexts: oacGdoiGmKekSigKeyLength.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekSigKeyLength.setDescription('The value of the SIG_KEY_LENGTH which specifies the length of the SIG payload key.')
oacGdoiGmKekOriginalLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 9), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekOriginalLifetime.setReference('RFC 3547 - Section 5.3.5. KEK_KEY_LIFETIME')
if mibBuilder.loadTexts: oacGdoiGmKekOriginalLifetime.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekOriginalLifetime.setDescription('The value of the KEK_KEY_LIFETIME which specifies the maximum time for which a KEK is valid. The GCKS may refresh the KEK at any time before the end of the valid period. The value is a four (4) octet (32-bit) number defining a valid time period in seconds.')
oacGdoiGmKekRemainingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 10), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekRemainingLifetime.setReference('RFC 3547 - Section 5.3.5. KEK_KEY_LIFETIME')
if mibBuilder.loadTexts: oacGdoiGmKekRemainingLifetime.setStatus('current')
if mibBuilder.loadTexts: oacGdoiGmKekRemainingLifetime.setDescription('The value of the remaining time for which a KEK is valid. The value is a four (4) octet (32-bit) number which begins at the value of oacGdoiGmKekOriginalLifetime and counts down to 0 in seconds. If the lifetime has already expired, this value should remain at zero (0) until the GCKS refreshes the KEK.')
mibBuilder.exportSymbols("ONEACCESS-GDOI-MIB", oacGdoiGmKekEntry=oacGdoiGmKekEntry, OacGdoiSPI=OacGdoiSPI, oacGdoiGmKekTable=oacGdoiGmKekTable, oacGdoiGmKekEncryptKeyLength=oacGdoiGmKekEncryptKeyLength, oacGdoiGmKekOriginalLifetime=oacGdoiGmKekOriginalLifetime, oacGdoiGmActiveKEK=oacGdoiGmActiveKEK, oacGdoiGmRekeysReceived=oacGdoiGmRekeysReceived, oacGdoiGmKekEncryptAlg=oacGdoiGmKekEncryptAlg, oacGdoiGmIdType=oacGdoiGmIdType, PYSNMP_MODULE_ID=oacExpIMGdoiMIB, oacGdoiGroupTable=oacGdoiGroupTable, oacGdoiGmKekSPI=oacGdoiGmKekSPI, OacGdoiHashAlogrithm=OacGdoiHashAlogrithm, OacGdoiIdentificationValue=OacGdoiIdentificationValue, OacGdoiSignatureMethod=OacGdoiSignatureMethod, oacExpIMGdoiMIB=oacExpIMGdoiMIB, OacGdoiIdentificationType=OacGdoiIdentificationType, oacGdoiGm=oacGdoiGm, oacGdoiGmKekSigKeyLength=oacGdoiGmKekSigKeyLength, oacGdoiGmEntry=oacGdoiGmEntry, oacGdoiPolicy=oacGdoiPolicy, oacGdoiGmIdValue=oacGdoiGmIdValue, oacGdoiMIBObjects=oacGdoiMIBObjects, OacGdoiKEKEncryptionAlgorithm=OacGdoiKEKEncryptionAlgorithm, oacGdoiGmKekSigHashAlg=oacGdoiGmKekSigHashAlg, oacGdoiGmKekRemainingLifetime=oacGdoiGmKekRemainingLifetime, oacGdoiGroupIdValue=oacGdoiGroupIdValue, oacGdoiGmRegKeyServerIdValue=oacGdoiGmRegKeyServerIdValue, oacGdoiGroupIdType=oacGdoiGroupIdType, oacGdoiGmKekDstIdValue=oacGdoiGmKekDstIdValue, oacGdoiGroupEntry=oacGdoiGroupEntry, oacGdoiGroupName=oacGdoiGroupName, oacGdoiGmTable=oacGdoiGmTable, oacGdoiGmKekSrcIdValue=oacGdoiGmKekSrcIdValue, oacGdoiGmKekSigAlg=oacGdoiGmKekSigAlg)
