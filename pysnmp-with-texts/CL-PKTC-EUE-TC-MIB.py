#
# PySNMP MIB module CL-PKTC-EUE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CL-PKTC-EUE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, Counter64, ObjectIdentity, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, TimeTicks, Integer32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "TimeTicks", "Integer32", "MibIdentifier", "Counter32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
pktcEUETCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1))
if mibBuilder.loadTexts: pktcEUETCMIB.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: pktcEUETCMIB.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: pktcEUETCMIB.setContactInfo('Sumanth Channabasappa Cable Television Laboratories, Inc. 858 Coal Creek Circle, Louisville, CO 80027, USA Phone: +1 303-661-9100 Email: mibs@cablelabs.com Acknowledgements: Thomas Clack, Broadcom - Primary author , and members of the PacketCable PACM Focus Team.')
if mibBuilder.loadTexts: pktcEUETCMIB.setDescription('This MIB module specifies the TEXTUAL CONVENTIONs for use in the definition of PacketCable E-UE MIB Objects.')
pktcEUETCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 0))
pktcEUETCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1))
pktcEUETCConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2))
pktcEUETCCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 1))
pktcEUETCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 2))
pktcEUETCUsageObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1))
class PktcEUETCID(TextualConvention, OctetString):
    description = " This TEXTUAL CONVENTION is being defined to contain identities that can be used within the PacketCable eUE data models. It specifies a hex string that can be used to represent the various identities. The types of possible identities are specified by the TEXTUAL CONVENTION 'PktcEUETCIDType'. The following rules apply: - All identities, except macaddress refer to either UEs or Users. Mac addresses are UE specific - When used as a pair, the public and private identities MUST be separated by a '#', with the private identity following the public identity."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1023)

class PktcEUETCIDType(TextualConvention, Integer32):
    description = " This TEXTUAL CONVENTION is being defined as a way of indicating an identity specified by MIB Objects utilizing the TEXTUAL CONVENTION 'PktcEUETCID'. The defined types include: - other(1) for types not described by the options provided below - gruu(2) for Globally Routable Unique URIs - publicIdentity(3) for Public Identities as defined by PacketCable - privateIdentity(4) for Private Identities as defined by PacketCable - publicPrivatePair(5) for Public and Private Identity pairs as defined by PacketCable - username(6) for username and password as defined by PacketCable - macaddress(7) for mac addresses - packetcableIdentity(8) for PacketCable specific types UE implementations must ensure that PktcEUETCIDType objects and any dependent objects (e.g., PktcEUETCID objects) are consistent. In general, the UE MUST generate an 'inconsistentValue' error if an attempt to change an PktcEUETCIDType object would, for example, lead to an undefined PktcEUETCID value. In particular, PktcEUETCIDType/PktcEUEID pairs MUST be changed together."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("gruu", 2), ("publicIdentity", 3), ("privateIdentity", 4), ("publicPrivatePair", 5), ("username", 6), ("macaddress", 7), ("packetcableIdentity", 8))

class PktcEUETCActStatus(TruthValue):
    description = " This TEXTUAL CONVENTION is being defined to indicate activation status as defined in PacketCable. A value of true(1) indicates a status of 'active'. A value of false(2) indicates a status of 'inactive'."
    status = 'current'

class PktcEUETCActStatusInfo(SnmpAdminString):
    description = ' This TEXTUAL CONVENTION is being defined to additional activation status information.'
    status = 'current'
    subtypeSpec = SnmpAdminString.subtypeSpec + ValueSizeConstraint(1, 31)

class PktcEUETCUsrElementIndexType(TextualConvention, Unsigned32):
    description = " This TEXTUAL CONVENTION is being defined to indicate any indices related to users, such as IMPUs and IMPIs as defined in PacketCable. Such an instance can be referenced across tables to indicate an association. The values assigned for objects of this type SHOULD be sequential starting with the value of 1 and incrementing by 1 for each User. A value of '0', if allowed MUST be specified in the DESCRIPTION of any MIB Object using this data type."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class PktcEUETCAppOrgIdentifier(TextualConvention, Unsigned32):
    reference = 'http://www.iana.org/assignments/enterprise-numbers'
    description = ' This TEXTUAL CONVENTION is being defined to identify the organization specifying the a particular application. Any MIB Object specified to be of this type MUST represent the IANA assigned Enterprise number. For CableLabs specified applications, it MUST be 4491.'
    status = 'current'

class PktcEUETCAppIdentifier(TextualConvention, Integer32):
    description = ' This TEXTUAL CONVENTION is being defined to identify the application id assigned by an organization. Each organization planning to specify an application MUST publish a registry which identifies each application and the corresponding ID that can be referenced.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 127)

class PktcEUETCUsrAppIndexType(TextualConvention, Unsigned32):
    description = " This TEXTUAL CONVENTION is being defined to indicate any indices related to PacketCable Applications. The values assigned for objects of this type SHOULD be sequential starting with the value of 1 and incrementing by 1 for each User. A value of '0', if allowed MUST be specified in the DESCRIPTION of any MIB Object using this data type."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class PktcEUETCCredsType(TextualConvention, Integer32):
    description = " This TEXTUAL CONVENTION represents credential types. Each definition of PktcEUETCCredsType MUST be accompanied by a definition of the textual convention PktcEUETCCreds. The specified types include: - other(1) An unknown credentials type. It MAY be used to indicate Credentials that are not in one of the formats defined below such as a vendor-specific format. - none(2) A non-existent credentials type. This value MUST be used if the value of the corresponding PktcEUETCCreds object is a zero-length string. It MAY be used when the credentials are no longer valid. - password(3) A password based credential. When this type is used the credential value contained in PktcEUETCCreds MUST be an ASCII string representing a user-readable password. - presharedKey(4) A pre-shared key based credential. When this type is used the credential value contained in PktcEUETCCreds MUST be interpreted as a pre-shared key represented as an octet string. - X509certificate(5) A certificate based credential. When this type is used the credential value contained in PktcEUETCCreds MUST be interpreted as a private key and an accompanying X.509 certificate. Implementations must ensure that objects with SYNTAX of 'PktcEUETCCredsType' and dependent objects with SYNTAX of 'PktcEUETCCreds' are consistent. In general, the UE MUST generate an 'inconsistentValue' error if an attempt to change an 'PktcEUETCCredsType' object would, for example, lead to an undefined 'PktcEUETCCreds' value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("password", 3), ("preSharedKey", 4), ("certificate", 5))

class PktcEUETCCreds(TextualConvention, OctetString):
    description = " This TEXTUAL CONVENTION allows for the definition of a credential. A PktcEUETCCreds value must always be associated with and interpreted within the context of a corresponding PktcEUETCCredsType. The value of a PktcEUETCCreds object must be consistent with the value of it's associated PktcEUETCCredsType object. Any attempt to SET an object when these values are not consistent must fail with an inconsistentValue error. An object of this type MUST be interpreted as follows (in network byte order): Bytes 0-1: Reserved. The application must define the usage of these bytes. Bytes 2-3: Indicate the length of the credential. Bytes 4-8191: Contain the credential value."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8192)

pktcEUETCSampleID = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 2), PktcEUETCID())
if mibBuilder.loadTexts: pktcEUETCSampleID.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleID.setDescription(" Sample MIB Object for use of 'PktcEUETCID'.")
pktcEUETCSampleIDType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3), PktcEUETCIDType())
if mibBuilder.loadTexts: pktcEUETCSampleIDType.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleIDType.setDescription(" Sample MIB Object for use of 'PktcEUETCIDType'.")
pktcEUETCSampleActStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4), PktcEUETCActStatus())
if mibBuilder.loadTexts: pktcEUETCSampleActStatus.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleActStatus.setDescription(" Sample MIB Object for use of 'PktcEUETCActStatus'.")
pktcEUETCSampleUsrRef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 5), PktcEUETCUsrElementIndexType())
if mibBuilder.loadTexts: pktcEUETCSampleUsrRef.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleUsrRef.setDescription(" Sample MIB Object for use of 'PktcEUETCUsrRef'.")
pktcEUETCSampleCredsType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6), PktcEUETCCredsType())
if mibBuilder.loadTexts: pktcEUETCSampleCredsType.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleCredsType.setDescription(" Sample MIB Object for use of 'PktcEUETCCredsType'.")
pktcEUETCSampleCreds = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7), PktcEUETCCreds())
if mibBuilder.loadTexts: pktcEUETCSampleCreds.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleCreds.setDescription(" Sample MIB Object for use of 'PktcEUETCCreds'.")
pktcEUETCSampleAppRef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8), PktcEUETCUsrAppIndexType())
if mibBuilder.loadTexts: pktcEUETCSampleAppRef.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleAppRef.setDescription(" Sample MIB Object for use of 'PktcEUETCUsrRef'.")
pktcEUETCSampleActStatusInfo = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9), PktcEUETCActStatusInfo())
if mibBuilder.loadTexts: pktcEUETCSampleActStatusInfo.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCSampleActStatusInfo.setDescription(" Sample MIB Object for use of 'PktcEUETCActStatusInfo'.")
pktcEUETCAppIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 10), PktcEUETCAppIdentifier())
if mibBuilder.loadTexts: pktcEUETCAppIdentifier.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCAppIdentifier.setDescription(" Sample MIB Object for use of 'PktcEUETCActStatusInfo'.")
pktcEUETCAppOrgIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11), PktcEUETCAppOrgIdentifier())
if mibBuilder.loadTexts: pktcEUETCAppOrgIdentifier.setStatus('obsolete')
if mibBuilder.loadTexts: pktcEUETCAppOrgIdentifier.setDescription(" Sample MIB Object for use of 'PktcEUETCActStatusInfo'.")
pktcEUETCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUETCMIBCompliance = pktcEUETCMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pktcEUETCMIBCompliance.setDescription(' The compliance statement for implementations of the EUE TC MIB')
mibBuilder.exportSymbols("CL-PKTC-EUE-TC-MIB", pktcEUETCNotifications=pktcEUETCNotifications, pktcEUETCSampleID=pktcEUETCSampleID, PktcEUETCIDType=PktcEUETCIDType, pktcEUETCAppOrgIdentifier=pktcEUETCAppOrgIdentifier, PktcEUETCAppIdentifier=PktcEUETCAppIdentifier, PktcEUETCActStatus=PktcEUETCActStatus, pktcEUETCUsageObjs=pktcEUETCUsageObjs, pktcEUETCObjects=pktcEUETCObjects, pktcEUETCMIB=pktcEUETCMIB, pktcEUETCSampleIDType=pktcEUETCSampleIDType, PYSNMP_MODULE_ID=pktcEUETCMIB, pktcEUETCSampleActStatusInfo=pktcEUETCSampleActStatusInfo, pktcEUETCSampleAppRef=pktcEUETCSampleAppRef, PktcEUETCActStatusInfo=PktcEUETCActStatusInfo, PktcEUETCAppOrgIdentifier=PktcEUETCAppOrgIdentifier, pktcEUETCSampleActStatus=pktcEUETCSampleActStatus, pktcEUETCCompliances=pktcEUETCCompliances, PktcEUETCUsrAppIndexType=PktcEUETCUsrAppIndexType, PktcEUETCCreds=PktcEUETCCreds, pktcEUETCSampleCreds=pktcEUETCSampleCreds, pktcEUETCAppIdentifier=pktcEUETCAppIdentifier, PktcEUETCCredsType=PktcEUETCCredsType, PktcEUETCID=PktcEUETCID, pktcEUETCMIBCompliance=pktcEUETCMIBCompliance, pktcEUETCSampleUsrRef=pktcEUETCSampleUsrRef, pktcEUETCGroups=pktcEUETCGroups, pktcEUETCSampleCredsType=pktcEUETCSampleCredsType, pktcEUETCConformance=pktcEUETCConformance, PktcEUETCUsrElementIndexType=PktcEUETCUsrElementIndexType)
