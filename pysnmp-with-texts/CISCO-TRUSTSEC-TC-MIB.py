#
# PySNMP MIB module CISCO-TRUSTSEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:14:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, TimeTicks, Gauge32, NotificationType, Counter32, ObjectIdentity, ModuleIdentity, Counter64, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "TimeTicks", "Gauge32", "NotificationType", "Counter32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCtsTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 694))
ciscoCtsTcMIB.setRevisions(('2013-06-06 00:00', '2012-01-30 00:00', '2009-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCtsTcMIB.setRevisionsDescriptions(('Added CtsSxpConnectionStatus.', 'Added CtsSgaclMonitorMode.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCtsTcMIB.setLastUpdated('201306060000Z')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setDescription('This module defines the textual conventions used within Cisco Trusted Security framework.')
class CtsSecurityGroupTag(TextualConvention, Unsigned32):
    description = 'Indicates the SGT (Security Group Tag) value. Semantics of a value zero CtsSecurityGroupTag are object-specific and must be defined as part of the description of any object which uses this syntax.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CtsAclName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of one ACL (Access Control List) or a list of ACLs using a single whitespace as the delimiter.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the CtsAclName convention. The latter defines a non-empty ACL name(s). This extension permits the additional value of empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsAclList(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of one or more ACLs. If there is multiple ACLs, each ACL name is separated by a single whitespace.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclListOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the CtsAclList convention. The latter defines a non-empty ACL name(s). This extension permits the additional value of empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPolicyName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of policy. A zero length string indicates no policy.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPasswordEncryptionType(TextualConvention, Integer32):
    description = "The type of encryption used for TrustSec passwords. 'other' - The read-only value 'other' indicates that the type of password encryption is not in one of the types defined below. 'none' - Indicates that the corresponding CtsPassword object is a zero-length string. 'clearText' - Indicates that the password is not encrypted 'typeSix' - Indicates that type-6 algorithm is used to encrypt the password 'typeSeven' - Indicates that type-7 algorithm is used to encrypt the password. Each definition of a concrete CtsPasswordEncryptionType value must be accompanied by a definition of a textual convention for use with that CtsPasswordEncryptionType. To support future extensions, the CtsPasswordEncryptionType textual convention SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that CtsPasswordEncryptionType object and any dependent objects (e.g. CtsPassword objects) are consistent. An inconsistentValue error must be generated if an attempt to change an CtsPasswordEncryptionType object would, for example, lead to an undefined CtsPassword value. In particular, CtsPasswordEncryptionType/CtsPassword pairs must be changed together if the encryption type changes. (e.g. from clearText(2) to typeSix(1))."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("clearText", 3), ("typeSix", 4), ("typeSeven", 5))

class CtsPassword(TextualConvention, OctetString):
    description = "A password for TrustSec functionality. A CtsPassword value is always interpreted within the context of an CtsPasswordEncryptionType value. Every usage of the CtsPassword textual convention is required to specify the CtsPasswordEncryptionType object which provides the context. It is suggested that the CtsPasswordEncryptionType is logically registered before the object(s) which use the CtsPassword textual convention if they appear in the same logical row. The value of an CtsPassword object must always be consistent with the value of the associated CtsPasswordEncryptionType object. Attempts to set an CtsPassword object to a value which is inconsistent with the associated CtsPasswordEncryptionType must fail with an inconsistentValue error. When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CtsGenerationId(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the generation identification associated with a TrustSec attribute such as downloaded SGACL, downloaded server list .etc... A zero length string indicates no generation identification.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CtsAcsAuthorityIdentity(TextualConvention, OctetString):
    description = 'The authority identity of an Access Control Server. A zero length of CtsAcsAuthorityIdentity indicates that the authority identity is not available.'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CtsCredentialRecordType(TextualConvention, Integer32):
    description = "The secret type of TrustSec credential record. 'simpleSecret' - Simple Secret credential. This type of credential record is constructed with symmetric key with associated meta-data. For example, credential password. 'pac' - Protected Access Credentials(PAC). A PAC record contains three components: PAC-key, PAC-opaque and PAC-info."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("simpleSecret", 1), ("pac", 2))

class CtsSgaclMonitorMode(TextualConvention, Integer32):
    description = "The SGACL monitor mode for the SGACL enforced traffic. 'on' - indicates that SGACL monitor is turned on. 'off' - indicates that SGACL monitor mode is turned off."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class CtsSxpConnectionStatus(TextualConvention, Integer32):
    description = "The status of SXP connection. 'other' - Any other state not covered by below enumerations. 'off' - The SXP connection has been disconnected. SGT mappings are no longer learnt through SXP connection in this state. SGT mappings already learnt through this connection will be deleted. 'on' - The SXP connection has been successfully established. SGT mappings are learnt through this SXP connection. 'pendingOn' - A request to establish SXP connection has been sent to the peer and is pending. 'deleteHoldDown' - The SXP connection is not operational and delete hold-down timer has been started. If the SXP connection does not recover before the expiration of the hold-down timer, the SGT mappings learnt on this connection will be deleted. If the SXP connection recovers before the expiration of the hold-down timer, the SGT mappings learnt on this connection will not be deleted."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("off", 2), ("on", 3), ("pendingOn", 4), ("deleteHoldDown", 5))

mibBuilder.exportSymbols("CISCO-TRUSTSEC-TC-MIB", CtsPasswordEncryptionType=CtsPasswordEncryptionType, CtsSgaclMonitorMode=CtsSgaclMonitorMode, CtsSxpConnectionStatus=CtsSxpConnectionStatus, CtsAclListOrEmpty=CtsAclListOrEmpty, CtsAclName=CtsAclName, CtsPassword=CtsPassword, ciscoCtsTcMIB=ciscoCtsTcMIB, CtsAclNameOrEmpty=CtsAclNameOrEmpty, CtsSecurityGroupTag=CtsSecurityGroupTag, CtsPolicyName=CtsPolicyName, CtsCredentialRecordType=CtsCredentialRecordType, PYSNMP_MODULE_ID=ciscoCtsTcMIB, CtsGenerationId=CtsGenerationId, CtsAclList=CtsAclList, CtsAcsAuthorityIdentity=CtsAcsAuthorityIdentity)
