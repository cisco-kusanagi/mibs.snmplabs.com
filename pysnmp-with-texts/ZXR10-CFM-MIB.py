#
# PySNMP MIB module ZXR10-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-CFM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Unsigned32, Bits, Counter64, TimeTicks, ObjectIdentity, ModuleIdentity, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Unsigned32", "Bits", "Counter64", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress")
TextualConvention, RowStatus, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "MacAddress", "DisplayString")
zxr10, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10")
zxr10cfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 120))
zxr10cfmMIB.setRevisions(('2007-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zxr10cfmMIB.setRevisionsDescriptions(('Included in IEEE P802.1ag Draft 8.',))
if mibBuilder.loadTexts: zxr10cfmMIB.setLastUpdated('200701240000Z')
if mibBuilder.loadTexts: zxr10cfmMIB.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: zxr10cfmMIB.setContactInfo('WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: stds-802-1@ieee.org Contact: David Elie-Dit-Cosaque Alcatel North America 3400 W. Plano Pkwy. Plano, TX 75075, USA E-mail: david.elie_dit_cosaque@alcatel.com Contact: Norman Finn Cisco Systems 170 W. Tasman Drive SJ-03/2/2 San Jose, CA 95134, USA E-mail: nfinn@cisco.com ')
if mibBuilder.loadTexts: zxr10cfmMIB.setDescription('Connectivity Fault Management module for managing IEEE 802.1ag')
dot1agNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 0))
dot1agMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1))
dot1agCfmMd = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1))
dot1agCfmMa = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2))
dot1agCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3))
dot1agCfmGloPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 4))
class InterfaceIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the InterfaceIndex convention. The latter defines a greater than zero value used to identify an interface or interface sub-layer in the managed system. This extension permits the additional value of zero. the value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero might include situations where interface was unknown, or when none or all interfaces need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class VlanIdOrNone(TextualConvention, Integer32):
    description = "The VLAN-ID that uniquely identifies a specific VLAN, or no VLAN. The special value of zero is used to indicate that no VLAN-ID is present or used. This can be used in any situation where an object or a table entry must refer either to a specific VLAN, or to no VLAN. Note that a MIB object that is defined using this TEXTUAL-CONVENTION should clarify the meaning of 'no VLAN' (i.e., the special value 0)."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), )
class VlanId(TextualConvention, Integer32):
    reference = 'IEEE Std 802.1Q 2003 Edition, Virtual Bridged Local Area Networks.'
    description = 'The VLAN-ID that uniquely identifies a VLAN. This is the 12-bit VLAN-ID used in the VLAN Tag header. The range is defined by the REFERENCEd specification.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class Dot1agCfmMaintDomainNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5, Table 21-19'
    description = 'A value that represents a type (and thereby the format) of a Dot1agCfmMaintDomainName. The value can be one of the following: ieeeReserved(0) Reserved for definition by IEEE 802.1 recommend to not use zero unless absolutely needed. none(1) No format specified, usually because there is not (yet) a Maintenance Domain Name. In this case, a zero length OCTET STRING for the Domain Name field is acceptable. dnsLikeName(2) Domain Name like string, globally unique text string derived from a DNS name. macAddrAndUint(3) MAC address + 2-octet (unsigned) integer. charString(4) RFC2579 DisplayString, except that the character codes 0-31 (decimal) are not used. ieeeReserved(xx) Reserved for definition by IEEE 802.1 xx values can be [5..31] and [64..255] ituReserved(xx) Reserved for definition by ITU-T Y.1731 xx values range from [32..63]To support future extensions, the Dot1agCfmMaintDomainNameType textual convention SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that Dot1agCfmMaintDomainNameType objects and any dependent objects (e.g., Dot1agCfmMaintDomainName objects) are consistent. An inconsistentValue error must be generated if an attempt to change an Dot1agCfmMaintDomainNameType object would, for example, lead to an undefined Dot1agCfmMaintDomainName value. In particular, Dot1agCfmMaintDomainNameType/Dot1agCfmMaintDomainName pairs must be changed together if the nameType changes. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("dnsLikeName", 2), ("macAddressAndUint", 3), ("charString", 4))

class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    reference = '802.1ag clause 21.6.5'
    description = "Denotes a generic Maintenance Domain Name.A Dot1agC fmMaintDomainName value is always interpreted within the context of a Dot1agCfmMaintDomainNameType value. Every usage of the Dot1agCfmMaintDomainName textual convention is required to specify the Dot1agCfmMaintDomainNameType object that provides the context. It is suggested that the Dot1agCfmMaintDomainNameType object be logically registered before the object(s) that use the Dot1agCfmMaintDomainName textual convention, if they appear in the same logical row. The value of a Dot1agCfmMaintDomainName object must always be consistent with the value of the associated Dot1agCfmMaintDomainNameType object. Attempts to set an Dot1agCfmMaintDomainName object to a value inconsistent with the associated Dot1agCfmMaintDomainNameType must fail with an inconsistentValue error. When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, IETF STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers; otherwise the applicable constraints MUST be stated in the appropriate conceptual row DESCRIPTION clauses, or in the surrounding documentation if there is no single DESCRIPTION clause that is appropriate. A value of none(1) in the associated Dot1agCfmMaintDomainNameType object means that no Maintenance Domain name is present, and the contents of the Dot1agCfmMaintDomainName object are meaningless. See the DESCRIPTION of the Dot1agCfmMaintAssocNameType TEXTUAL-CONVENTION for a discussion of the length limits on the Maintenance Domain name and Maintenance Association name. "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 80)

class Dot1agCfmMaintAssocNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5.4, Table 21-20'
    description = 'A value that represents a type (and thereby the format) of a Dot1agCfmMaintAssocName. The value can be one of the following: ieeeReserved(0) Reserved for definition by IEEE 802.1 recommend to not use zero unless absolutely needed. primaryVid(1) Primary VLAN ID. 12 bits represented in a 2-octet integer: - 4 least significant bits of the first byte contains the 4 most significant bits of the 12 bits primary VID - second byte contains the 8 least significant bits of the primary VID 0 1 2 3 4 5 6 7 8 +-+-+-+-+-+-+-+-+ |0 0 0 0| (MSB) | +-+-+-+-+-+-+-+-+ | VID LSB | +-+-+-+-+-+-+-+-+ charString(2) RFC2579 DisplayString, except that the character codes 0-31 (decimal) are not used. (1..45) octets unsignedInt16 (3) 2-octet integer/big endian rfc2865VpnId(4) RFC 2685 VPN ID 3 octet VPN authority Organizationally Unique Identifier followed by 4 octet VPN index identifying VPN according to the OUI: 0 1 2 3 4 5 6 7 8 +-+-+-+-+-+-+-+-+ | VPN OUI (MSB) | +-+-+-+-+-+-+-+-+ | VPN OUI | +-+-+-+-+-+-+-+-+ | VPN OUI (LSB) | +-+-+-+-+-+-+-+-+ |VPN Index (MSB)| +-+-+-+-+-+-+-+-+ | VPN Index | +-+-+-+-+-+-+-+-+ | VPN Index | +-+-+-+-+-+-+-+-+ |VPN Index (LSB)| +-+-+-+-+-+-+-+-+ ieeeReserved(xx) Reserved for definition by IEEE 802.1 xx values can be [5..31] and [64..255] ituReserved(xx) Reserved for definition by ITU-T Y.1731 xx values range from [32..63] To support future extensions, the Dot1agCfmMaintAssocNameType textual convention SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that Dot1agCfmMaintAssocNameType objects and any dependent objects (e.g., Dot1agCfmMaintAssocName objects) are consistent. An inconsistentValue error must be generated if an attempt to change an Dot1agCfmMaintAssocNameType object would, for example, lead to an undefined Dot1agCfmMaintAssocName value. In particular, Dot1agCfmMaintAssocNameType/Dot1agCfmMaintAssocName pairs must be changed together if the nameType changes. The Maintenance Domain name and Maintenance Association name, when put together into the CCM PDU, MUST total 48 octets or less. If the Dot1agCfmMaintDomainNameType object contains none(1), then the Dot1agCfmMaintAssocName object MUST be 45 octets or less in length. Otherwise, the length of the Dot1agCfmMaintDomainName object plus the length of the Dot1agCfmMaintAssocName object, added together, MUST total less than or equal to 44 octets. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4))

class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    reference = '802.1ag clauses 21.6.5.4, 21.6.5.5, 21.6.5.6'
    description = "Denotes a generic Maintenance Association Name. It is the part of the Maintenance Association Identifier which is unique within the Maintenance Domain Name and is appended to the Maintenance Domain Name to form the Maintenance Association Identifier (MAID). A Dot1agCfmMaintAssocName value is always interpreted within the context of a Dot1agCfmMaintAssocNameType value. Every usage of the Dot1agCfmMaintAssocName textual convention is required to specify the Dot1agCfmMaintAssocNameType object that provides the context. It is suggested that the Dot1agCfmMaintAssocNameType object be logically registered before the object(s) that use the Dot1agCfmMaintAssocName textual convention, if they appear in the same logical row. The value of a Dot1agCfmMaintAssocName object must always be consistent with the value of the associated Dot1agCfmMaintAssocNameType object. Attempts to set an Dot1agCfmMaintAssocName object to a value inconsistent with the associated Dot1agCfmMaintAssocNameType must fail with an inconsistentValue error. When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, IETF STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers; otherwise the applicable constraints MUST be stated in the appropriate conceptual row DESCRIPTION clauses, or in the surrounding documentation if there is no single DESCRIPTION clause that is appropriate. "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 80)

class Dot1agCfmMDLevel(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    description = "Integer identifying the Maintenance Domain Level (MD Level). Higher numbers correspond to higher Maintenance Domains, those with the greatest physical reach, with the highest values for customers' CFM PDUs. Lower numbers correspond to lower Maintenance Domains, those with more limited physical reach, with the lowest values for CFM PDUs protecting single bridges or physical links. "
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class Dot1agCfmMpDirection(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.3.2:c'
    description = 'Indicates the direction in which the Maintenance association (MEP or MIP) faces on the bridge port: down(1) Sends Continuity Check Messages away from the MAC Relay Entity. up(2) Sends Continuity Check Messages towards the MAC Relay Entity. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class Dot1agCfmHighestDefectPri(TextualConvention, Integer32):
    reference = '802.1ag clause 20.1.2, 12.14.7.7.2:c and 20.33.9'
    description = 'An enumerated value, equal to the contents of the variable highestDefect (20.33.9 and Table 20-1), indicating the highest-priority defect that has been present since the MEP Fault Notification Generator State Machine was last in the FNG_RESET state, either: none(0) no defects since FNG_RESET defRDICCM(1) DefRDICCM defMACstatus(2) DefMACstatus defRemoteCCM(3) DefRemoteCCM defErrorCCM(4) DefErrorCCM defXconCCM(5) DefXconCCM The value 0 is used for no defects so that additional higher priority values can be added, if needed, at a later time, and so that these values correspond with those in Dot1agCfmLowestAlarmPri. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("defRDICCM", 1), ("defMACstatus", 2), ("defRemoteCCM", 3), ("defErrorCCM", 4), ("defXconCCM", 5))

class Dot1agCfmLowestAlarmPri(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:k and 20.9.5'
    description = 'An integer value specifying the lowest priority defect that is allowed to generate a Fault Alarm (20.9.5), either: allDef(1) DefRDICCM, DefMACstatus, DefRemoteCCM, DefErrorCCM, and DefXconCCM; macRemErrXcon(2) Only DefMACstatus, DefRemoteCCM, DefErrorCCM, and DefXconCCM (default); remErrXcon(3) Only DefRemoteCCM, DefErrorCCM, and DefXconCCM; errXcon(4) Only DefErrorCCM and DefXconCCM; xcon(5) Only DefXconCCM; or noXcon(6) No defects DefXcon or lower are to be reported; '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("allDef", 1), ("macRemErrXcon", 2), ("remErrXcon", 3), ("errXcon", 4), ("xcon", 5), ("noXcon", 6))

class Dot1agCfmSessionId(TextualConvention, Unsigned32):
    reference = '802.1ag clauses 3.19 and 19.2.1'
    description = 'Maintenance association End Point Identifier (MEPID): A small integer, unique over a given Maintenance Association, identifying a specific MEP. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 128)

class Dot1agCfmMhfCreation(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.5.1.3:c and 22.2.3'
    description = 'Indicates if the Management Entity can create MHFs. The valid values are: defMHFnone(1) No MHFs can be created for this VID. defMHFdefault(2) MHFs can be created on this VID on any Bridge port through which this VID can pass. defMHFexplicit(3) MHFs can be created for this VID only on Bridge ports through which this VID can pass, and only if a MEP is created at some lower MD Level. defMHFdefer(4) The creation of MHFs is determined by the corresponding Maintenance Domain variable (dot1agCfmMaMhfCreation). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3), ("defMHFdefer", 4))

class Dot1agCfmIdPermission(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.6.1.3:d and 21.5.3'
    description = 'Indicates what, if anything, is to be included in the Sender ID TLV transmitted in CCMs, LBMs, LTMs, and LTRs. The valid values are: sendIdNone(1) The Sender ID TLV is not to be sent. sendIdChassis(2) The Chassis ID Length, Chassis ID Subtype, and Chassis ID fields of the Sender ID TLV are to be sent. sendIdManage(3) The Management Address Length and Management Address of the Sender ID TLV are to be sent. sendIdChassisManage(4) The Chassis ID Length, Chassis ID Subtype, Chassis ID, Management Address Length and Management Address fields are all to be sent. sendIdDefer(5) The contents of the Sender ID TLV are determined by the corresponding Maintenance Domain variable (dot1agCfmMaIdPermission). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4), ("sendIdDefer", 5))

class Dot1agCfmSpeed(TextualConvention, Integer32):
    description = 'Fast or slow. If it is fast, do by hareware.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fastSpeed", 0), ("slowSpeed", 1))

class Dot1agCfmCcmInterval(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.1.3:e, 20.8.1 and 21.6.1.3'
    description = "Indicates the interval at which CCMs are sent by a MEP. The possible values are: intervalInvalid(0) No CCMs are sent (disabled). interval300Hz(1) CCMs are sent every 3 1/3 milliseconds (300Hz). interval10ms(2) CCMs are sent every 10 milliseconds. interval100ms(3) CCMs are sent every 100 milliseconds. interval1s(4) CCMs are sent every 1 second. interval10s(5) CCMs are sent every 10 seconds. interval1min(6) CCMs are sent every minute. interval10min(7) CCMs are sent every 10 minutes. Note: enumerations start at zero to match the 'CCM Interval field' protocol field. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("intervalInvalid", 0), ("interval300Hz", 1), ("interval10ms", 2), ("interval100ms", 3), ("interval1s", 4), ("interval10s", 5), ("interval1min", 6), ("interval10min", 7))

class Dot1agCfmFngState(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:f and 20.35'
    description = 'Indicates the diferent states of the MEP Fault Notification Generator State Machine. fngReset(1) No defect has been present since the dot1agCfmMepFngResetTime timer expired, or since the state machine was last reset. fngDefect(2) A defect is present, but not for a long enough time to be reported (dot1agCfmMepFngAlarmTime). fngReportDefect(3) A momentary state during which the defect is reported by sending a dot1agCfmFaultAlarm notification, if that action is enabled. fngDefectReported(4) A defect is present, and some defect has been reported. fngDefectClearing(5) No defect is present, but the dot1agCfmMepFngResetTime timer has not yet expired. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fngReset", 1), ("fngDefect", 2), ("fngReportDefect", 3), ("fngDefectReported", 4), ("fngDefectClearing", 5))

class Dot1agCfmRelayActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.5, 21.9.5, and Table 21-27'
    description = 'Possible values the Relay action field can take.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlyHit", 1), ("rlyFdb", 2), ("rlyMpdb", 3))

class Dot1agCfmIngressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.6, 21.9.8.1, and Table 21-30 '
    description = 'Possible values returned in the ingress action field.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ingOk", 1), ("ingDown", 2), ("ingBlocked", 3), ("ingVid", 4))

class Dot1agCfmEgressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:o, 20.36.2.10, 21.9.9.1, and Table 21-32'
    description = 'Possible values returned in the egress action field'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("egrOK", 1), ("egrDown", 2), ("egrBlocked", 3), ("egrVid", 4))

class Dot1afCfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a new Index in a table. The special value of 0 indicates that no more new entries can be created in the relevant table. When a MIB is used for configuration, an object with this SYNTAX always contains a legal value (if non-zero) for an index that is not currently used in the relevant table. The Command Generator (Network Management Application) reads this variable and uses the (non-zero) value read when creating a new row with an SNMP SET. When the SET is performed, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation-specific algorithm. If the value is in use, however, the SET fails. The Network Management Application must then re-read this variable to obtain a new usable value. An OBJECT-TYPE definition using this SYNTAX MUST specify the relevant table for which the object is providing this functionality. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Dot1agCfmMepDefects(TextualConvention, Bits):
    reference = '802.1ag clauses 12.14.7.1.3:o, 12.14.7.1.3:p, 12.14.7.1.3:q, 12.14.7.1.3:r, and 12.14.7.1.3:s.'
    description = 'A MEP can detect and report a number of defects, and multiple defects can be present at the same time. These defects are: bDefRDICCM(0) A remote MEP is reported the RDI bit in its last CCM. bDefMACstatus(1) Either some remote MEP is reporting its Interface Status TLV as not isUp, or all remote MEPs are reporting a Port Status TLV that contains some value other than psUp. bDefRemoteCCM(2) The MEP is not receiving valid CCMs from at least one of the remote MEPs. bDefErrorCCM(3) The MEP has received at least one invalid CCM whose CCM Interval has not yet timed out. bDefXconCCM(4) The MEP has received at least one CCM from either another MAID or a lower MD Level whose CCM Interval has not yet timed out. '
    status = 'current'
    namedValues = NamedValues(("bDefRDICCM", 0), ("bDefMACstatus", 1), ("bDefRemoteCCM", 2), ("bDefErrorCCM", 3), ("bDefXconCCM", 4))

class Dot1agCfmLbrTransId(TextualConvention, Unsigned32):
    reference = ' '
    description = ' '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

dot1agCfmMdTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 1), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdTableNextIndex.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdTableNextIndex.setDescription('This object contains an unused value for dot1agCfmMdIndex in the dot1agCfmMdTable, or a zero to indicate that none exist. ')
dot1agCfmMdTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2), )
if mibBuilder.loadTexts: dot1agCfmMdTable.setReference('802.1ag clauses 3.22 and 18.1')
if mibBuilder.loadTexts: dot1agCfmMdTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdTable.setDescription('The Maintenance Domain table. Each row in the table represents a different Maintenance Domain. A Maintenance Domain is described in 802.1ag (3.22) as the network or the part of the network for which faults in connectivity are to be managed. The boundary of a Maintenance Domain is defined by a set of DSAPs, each of which can become a point of connectivity to a service instance. ')
dot1agCfmMdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"))
if mibBuilder.loadTexts: dot1agCfmMdEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdEntry.setDescription('The Maintenance Domain table entry. This entry is not lost upon reboot. It is backed up by stable storage. ')
dot1agCfmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: dot1agCfmMdIndex.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdIndex.setDescription('The index to the Maintenance Domain table. dot1agCfmMdTableNextIndex needs to be inspected to find an available index for row-creation. Referential integrity is required i.e. the index needs to be persistent upon a reboot or restart of a device. The index can never be reused for other Maintenance Domain. The index value should keep increasing up to the time that they wrap around. This is to facilitate access control based on OID. ')
dot1agCfmMdFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 2), Dot1agCfmMaintDomainNameType().clone('charString')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdFormat.setReference('802.1ag clause 21.6.5.1')
if mibBuilder.loadTexts: dot1agCfmMdFormat.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdFormat.setDescription('The type (and thereby format) of the Maintenance Domain Name.')
dot1agCfmMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 3), Dot1agCfmMaintDomainName().clone('DEFAULT')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdName.setReference('802.1ag clauses 3.24, 12.14.5, and 21.6.5.3')
if mibBuilder.loadTexts: dot1agCfmMdName.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdName.setDescription('The Maintenance Domain name. The type/format of this object is determined by the value of the dot1agCfmMdNameType object. Each Maintenance Domain has unique name amongst all those used or available to a service provider or operator. It facilitates easy identification of administrative responsibility for each Maintenance Domain. Clause 3.24 defines a Maintenance Domain name as the identifier, unique over the domain for which CFM is to protect against accidental concatenation of Service Instances, of a particular Maintenance Domain. ')
dot1agCfmMdMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 4), Dot1agCfmMDLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdMdLevel.setReference('802.1ag clause 12.14.5.1.3:b')
if mibBuilder.loadTexts: dot1agCfmMdMdLevel.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdMdLevel.setDescription('The Maintenance Domain Level.')
dot1agCfmMdMhfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 5), Dot1agCfmMhfCreation().clone('defMHFnone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdMhfCreation.setReference('802.1ag clause 12.14.5.1.3:c')
if mibBuilder.loadTexts: dot1agCfmMdMhfCreation.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdMhfCreation.setDescription('Enumerated value indicating whether the management entity can create MHFs (MIP Half Function) for this Maintenance Domain. ')
dot1agCfmMdMhfIdPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 6), Dot1agCfmIdPermission().clone('sendIdNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdMhfIdPermission.setReference('802.1ag clause 12.14.5.1.3:d')
if mibBuilder.loadTexts: dot1agCfmMdMhfIdPermission.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdMhfIdPermission.setDescription('Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MPs configured in this Maintenance Domain. Since, in this variable, there is no encompassing Maintenance Domain, the value sendIdDefer takes the meaning of sendIdChassisManage. ')
dot1agCfmMdMaTableNextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 7), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdMaTableNextIndex.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdMaTableNextIndex.setDescription('Value to be used as the index of the MA table entries for this Maintenance Domain when the management entity wants to create a new row in the MA table. ')
dot1agCfmMdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 1, 2, 1, 8), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdRowStatus.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMdRowStatus.setDescription('The status of the row. The writable columns in a row can not be changed if the row is active. All columns must have a valid value before a row can be activated. ')
dot1agCfmMaTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1), )
if mibBuilder.loadTexts: dot1agCfmMaTable.setReference('802.1ag clause 18.2')
if mibBuilder.loadTexts: dot1agCfmMaTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaTable.setDescription('The Maintenance Association table. Each row in the table represents an MA. An MA is a set of MEPs, each configured with a single service instance. Creation of a Service Instance establishes a connectionless association among the selected DSAPs. Configuring a Maintenance association End Point (MEP) at each of the DSAPs creates a Maintenance Association (MA) to monitor that connectionless connectivity. The MA is identified by a Short MA Name that is unique within the Maintenance Domain and chosen to facilitate easy identification of the Service Instance. Together, the Maintenance Domain Name and the Short MA Name form the Maintenance Association Identifier (MAID) that is carried in CFM Messages to identify incorrect connectivity among Service Instances. A small integer, the Maintenance association End Point Identifier (MEPID), identifies each MEP among those configured on a single MA (802.1ag clauses 3.17 and 18.2). This table uses two indices, first index is the index of the Maintenance Domain table. The writable objects in this table need to be persistent upon reboot or restart of a device. ')
dot1agCfmMaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"))
if mibBuilder.loadTexts: dot1agCfmMaEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaEntry.setDescription('The MA table entry.')
dot1agCfmMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: dot1agCfmMaIndex.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaIndex.setDescription('Index of the MA table dot1agCfmMdMaTableNextIndex needs to be inspected to find an available index for row-creation. ')
dot1agCfmMaPrimaryVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 2), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaPrimaryVlanId.setReference('802.1ag clause 12.14.6.1.3:b')
if mibBuilder.loadTexts: dot1agCfmMaPrimaryVlanId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaPrimaryVlanId.setDescription('The Primary VLAN ID with which the Maintenance Association is associated, or 0 if the MA is not attached to any VID. If the MA is associated with more than one VID, the dot1agCfmVlanTable lists them. ')
dot1agCfmMaFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 3), Dot1agCfmMaintAssocNameType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaFormat.setReference('802.1ag clauses 21.6.5.4')
if mibBuilder.loadTexts: dot1agCfmMaFormat.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaFormat.setDescription('The type (and thereby format) of the Maintenance Association Name. ')
dot1agCfmMaName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 4), Dot1agCfmMaintAssocName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaName.setReference('802.1ag clauses 21.6.5.6, and Table 21-20')
if mibBuilder.loadTexts: dot1agCfmMaName.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaName.setDescription('The Short Maintenance Association name. The type/format of this object is determined by the value of the dot1agCfmMaNameType object. ')
dot1agCfmMaMhfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 5), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaMhfCreation.setReference('802.1ag clause 12.14.6.1.3:c')
if mibBuilder.loadTexts: dot1agCfmMaMhfCreation.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaMhfCreation.setDescription('Indicates if the Management entity can create MHFs (MIP Half Function) for this MA. ')
dot1agCfmMaIdPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 6), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaIdPermission.setReference('802.1ag clause 12.14.6.1.3:d')
if mibBuilder.loadTexts: dot1agCfmMaIdPermission.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaIdPermission.setDescription('Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MPs configured in this MA. ')
dot1agCfmMaCcmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 7), Dot1agCfmCcmInterval().clone('interval1s')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaCcmInterval.setReference('802.1ag clause 12.14.6.1.3:e')
if mibBuilder.loadTexts: dot1agCfmMaCcmInterval.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaCcmInterval.setDescription('Interval between CCM transmissions to be used by all MEPs in the MA. ')
dot1agCfmMaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaRowStatus.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaRowStatus.setDescription('The status of the row. The writable columns in a row can not be changed if the row is active. All columns must have a valid value before a row can be activated. ')
dot1agCfmMASpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 1, 1, 9), Dot1agCfmSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMASpeed.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMASpeed.setDescription('Fast or slow. If it is fast, do by hareware.')
dot1agCfmMaVlanListTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2), )
if mibBuilder.loadTexts: dot1agCfmMaVlanListTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaVlanListTable.setDescription('List of Vlan. ')
dot1agCfmMaVlanListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaVlanListIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMaVlanListEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaVlanListEntry.setDescription('The known Vlan table entry.')
dot1agCfmMaVlanListIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: dot1agCfmMaVlanListIdentifier.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaVlanListIdentifier.setDescription('VlanId')
dot1agCfmMaVlanListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaVlanListRowStatus.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaVlanListRowStatus.setDescription('The status of the row. Read SNMPv2-TC (RFC1903) for an explanation of the possible values this object can take. ')
dot1agCfmMaMepListTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3), )
if mibBuilder.loadTexts: dot1agCfmMaMepListTable.setReference('802.1ag clause 12.14.6.1.3:g')
if mibBuilder.loadTexts: dot1agCfmMaMepListTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaMepListTable.setDescription('List of MEPIDs (in any bridge) that belong to the same MA. Clause 12.14.6.1.3 specifies that a list of MEPIDs in all bridges in that MA, but since SNMP SMI does not allow to state in a MIB that an object in a table is an array, the information has to be stored in another table with two indices, being the first index, the index of the table that contains the list or array. ')
dot1agCfmMaMepListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaMepListSessionId"))
if mibBuilder.loadTexts: dot1agCfmMaMepListEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaMepListEntry.setDescription('The known MEPS table entry.')
dot1agCfmMaMepListSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3, 1, 1), Dot1agCfmSessionId())
if mibBuilder.loadTexts: dot1agCfmMaMepListSessionId.setReference('802.1ag clause 12.14.6.1.3:g')
if mibBuilder.loadTexts: dot1agCfmMaMepListSessionId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaMepListSessionId.setDescription('MEPID')
dot1agCfmMaMepListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 2, 3, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaMepListRowStatus.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMaMepListRowStatus.setDescription('The status of the row. Read SNMPv2-TC (RFC1903) for an explanation of the possible values this object can take. ')
dot1agCfmMepTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1), )
if mibBuilder.loadTexts: dot1agCfmMepTable.setReference('802.1ag clauses 12.14.7 and 19.2')
if mibBuilder.loadTexts: dot1agCfmMepTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepTable.setDescription("The Maintenance Association End Point (MEP) table. Each row in the table represents a different MEP. A MEP is an actively managed CFM entity, associated with a specific DSAP of a Service Instance, which can generate and receive CFM PDUs and track any responses. It is an end point of a single Maintenance Association, and is an endpoint of a separate Maintenance Entity for each of the other MEPs in the same Maintenance Association (802.1ag clause 3.18). This table uses three indices. The first two indices are the indices of the Maintenance Domain and MA tables, the reason being that a MEP is always related to an MA and Maintenance Domain. The Transmit Loopback table. Entries in this table are created/removed at the same time than entries in the MEP table are created/removed. The MEP table also stores all the managed objects for sending LBM and LTM. *LBM Managed objects LBM Managed objects in the MEP table enables the management entity to initiate transmission of Loopback messages. It will signal the MEP that it should transmit some number of Loopback messages and detect the detection (or lack thereof) of the corresponding Loopback messages. Steps to use entries in this table: 1) Wait for dot1agCfmMepTransmitLbmStatus value to be 'ready'. To do this do this sequence: a. an SNMP GET for both SnmpSetSerialNo and dot1agCfmMepTransmitLbmStatus objects (in same SNMP PDU). b. Check if value for dot1agCfmMepTransmitLbmStatus is 'ready' - if not, wait x seconds, go to step a above. - if yes, save the value of SnmpSetSerialNo and go to step 2) below 2) Change dot1agCfmMepTransmitLbmStatus value from 'ready' to 'notReady' to ensure no other management entity will use the service. In order to not disturb a possible other NMS do this by sending an SNMP SET for both SnmpSetSerialNo and dot1agCfmMepTransmitLbmStatus objects (in same SNMP PDU, and make sure SNmpSetSerialNo is the first varBind). For the SnmpSetSerialNo varBind, use the value that you obtained in step 1)a.. This ensures that two cooperating NMSes will not step on each others toes. 3) Setup the different data to be sent (number of messages, optional TLVs,...). 4) Record the current values of dot1agCfmMepLbrIn, dot1agCfmMepLbrInOutOfOrder, and dot1agCfmMepLbrBadMsdu. 6) Change dot1agCfmMepTransmitLbmStatus value from 'notReady' to 'transmit' to initiate transmission of Loopback messages. 7) Check the value of dot1agCfmMepTransmitLbmResultOK to find out if the operation was successfully initiated or not. 8) Monitor the value of dot1agCfmMepTransmitLbmMessages. When it reaches 0, the last LBM has been transmitted. Wait an additional 5 seconds to ensure that all LBRs have been returned. 9) Compare dot1agCfmMepLbrIn, dot1agCfmMepLbrInOutOfOrder, and dot1agCfmMepLbrBadMsdu to their old values from step 4, above, to get the results of the test. 10) Change the dot1agCfmMepTransmitLbmStatus value back to 'ready' to allow other management entities to use the table. *LTM Managed objects The LTM Managed objects in the MEP table are used in a manner similar to that described for LBM transmission, above. Upon successfully initiating the transmission, the variables dot1agCfmMepTransmitLtmSeqNumber and dot1agCfmMepTransmitLtmEgressIdentifier return the information required to recover the results of the LTM from the dot1agCfmLtrTable. ")
dot1agCfmMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmSessionId"))
if mibBuilder.loadTexts: dot1agCfmMepEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepEntry.setDescription('The MEP table entry')
dot1agCfmSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 1), Dot1agCfmSessionId())
if mibBuilder.loadTexts: dot1agCfmSessionId.setReference('802.1ag clauses 3.19, 19.2 and 12.14.7')
if mibBuilder.loadTexts: dot1agCfmSessionId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmSessionId.setDescription('Integer that is unique among all the MEPs in the same MA. Other definition is: a small integer, unique over a given Maintenance Association, identifying a specific Maintenance association End Point (3.19). MEP Identifier is also known as the MEPID. ')
dot1agCfmMepIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepIfIndex.setReference('802.1ag clause 12.14.7.1.3:b')
if mibBuilder.loadTexts: dot1agCfmMepIfIndex.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepIfIndex.setDescription('This object is the interface index of the interface either a bridge port, or an aggregated IEEE 802.1 link within a bridge port, to which the MEP is attached. Upon a restart of the system, the system SHALL, if necessary, change the value of this variable so that it indexes the entry in the interface table with the same value of ifAlias that it indexed before the system restart. If no such entry exists, then the system SHALL set this variable to 0. ')
dot1agCfmMepDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 3), Dot1agCfmMpDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDirection.setReference('802.1ag clauses 12.14.7.1.3:c and 19.2')
if mibBuilder.loadTexts: dot1agCfmMepDirection.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDirection.setDescription('The direction in which the MEP faces on the Bridge port.')
dot1agCfmMepPrimaryVid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepPrimaryVid.setReference('802.1ag clauses 12.14.7.1.3:d')
if mibBuilder.loadTexts: dot1agCfmMepPrimaryVid.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepPrimaryVid.setDescription("An integer indicating the Primary VID of the MEP, always one of the VIDs assigned to the MEP's MA. The value 0 indicates that either the Primary VID is that of the MEP's MA, or that the MEP's MA is associated with no VID.")
dot1agCfmMepActive = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepActive.setReference('802.1ag clauses 12.14.7.1.3:e and 20.9.1')
if mibBuilder.loadTexts: dot1agCfmMepActive.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepActive.setDescription('Administrative state of the MEP A Boolean indicating the administrative state of the MEP. True indicates that the MEP is to function normally, and false that it is to cease functioning.')
dot1agCfmMepFngState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 6), Dot1agCfmFngState().clone('fngReset')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepFngState.setReference('802.1ag clauses 12.14.7.1.3:f and 20.35')
if mibBuilder.loadTexts: dot1agCfmMepFngState.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepFngState.setDescription('Current state of the MEP Fault Notification Generator State Machine. ')
dot1agCfmMepCciEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCciEnabled.setReference('802.1ag clauses 12.14.7.1.3:g and 20.10.1')
if mibBuilder.loadTexts: dot1agCfmMepCciEnabled.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepCciEnabled.setDescription('If set to true, the MEP will generate CCM messages.')
dot1agCfmMepCcmLtmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCcmLtmPriority.setReference('802.1ag clause 12.14.7.1.3:h')
if mibBuilder.loadTexts: dot1agCfmMepCcmLtmPriority.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepCcmLtmPriority.setDescription('The priority value for CCMs and LTMs transmitted by the MEP. Default Value in the highest priority value allowed to pass through the bridge port for any of this MEPs VIDs. The management entity can obtain the default value for this variable from the priority regeneration table by extracting the highest priority value in this table on this MEPs bridge port. (1 is lowest, then 2, then 0, then 3-7). ')
dot1agCfmMepMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepMacAddress.setReference('802.1ag clause 12.14.7.1.3:i and 19.4')
if mibBuilder.loadTexts: dot1agCfmMepMacAddress.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepMacAddress.setDescription('MAC address of the MEP.')
dot1agCfmMepLowPrDef = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 10), Dot1agCfmLowestAlarmPri().clone('macRemErrXcon')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLowPrDef.setReference('802.1ag clause 12.14.7.1.3:k and 20.9.5 and Table 20-1')
if mibBuilder.loadTexts: dot1agCfmMepLowPrDef.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLowPrDef.setDescription('An integer value specifying the lowest priority defect that is allowed to generate fault alarm. ')
dot1agCfmMepHighestPrDefect = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 11), Dot1agCfmHighestDefectPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepHighestPrDefect.setReference('802.1ag clause 12.14.7.1.3:n 20.33.9 and Table 21-1')
if mibBuilder.loadTexts: dot1agCfmMepHighestPrDefect.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepHighestPrDefect.setDescription('The highest priority defect that has been present since the MEPs Fault Notification Generator State Machine was last in the FNG_RESET state. ')
dot1agCfmMepDefects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 12), Dot1agCfmMepDefects()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDefects.setReference('.1ag clauses 12.14.7.1.3:o, 12.14.7.1.3:p, 12.14.7.1.3:q, 12.14.7.1.3:r, 12.14.7.1.3:s, 20.21.3, 20.23.3, 20.33.5, 20.33.6, 20.33.7.')
if mibBuilder.loadTexts: dot1agCfmMepDefects.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDefects.setDescription('A vector of Boolean error conditions from Table 20-1, any of which may be true: DefRDICCM(0) DefMACstatus(1) DefRemoteCCM(2) DefErrorCCM(3) DefXconCCM(4) ')
dot1agCfmMepCciSentCcms = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCciSentCcms.setReference('802.1ag clauses 12.14.7.1.3:w and 20.10.2')
if mibBuilder.loadTexts: dot1agCfmMepCciSentCcms.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepCciSentCcms.setDescription('Total number of Continuity Check messages transmitted.')
dot1agCfmMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepId.setDescription('Session Id')
dot1agCfmMepMEPAttachType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepMEPAttachType.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepMEPAttachType.setDescription('MEP AttachType')
dot1agCfmMepTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTunnelId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepTunnelId.setDescription('Tunnel Id')
dot1agCfmMepLMFlage = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLMFlage.setReference('')
if mibBuilder.loadTexts: dot1agCfmMepLMFlage.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLMFlage.setDescription('LMFlage')
dot1agCfmMepDMFlage = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDMFlage.setReference('')
if mibBuilder.loadTexts: dot1agCfmMepDMFlage.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDMFlage.setDescription('DMFlage')
dot1agCfmMepPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepPortName.setReference('802.1ag clause 12.14.7.1.3:b')
if mibBuilder.loadTexts: dot1agCfmMepPortName.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepPortName.setDescription(' Mep Port Name ')
dot1agCfmMepLbrIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrIn.setReference('802.1ag clause 12.14.7.1.3:y and 20.31.1')
if mibBuilder.loadTexts: dot1agCfmMepLbrIn.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLbrIn.setDescription('Total number of valid, in-order Loopback Replies received.')
dot1agCfmMepLbrInOutOfOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrInOutOfOrder.setReference('802.1ag clause 12.14.7.1.3:z and 20.31.1')
if mibBuilder.loadTexts: dot1agCfmMepLbrInOutOfOrder.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLbrInOutOfOrder.setDescription('The total number of valid, out-of-order Loopback Replies received. ')
dot1agCfmMepLbrBadMsdu = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrBadMsdu.setReference('802.1ag clause 12.14.7.1.3:aa 20.2.3')
if mibBuilder.loadTexts: dot1agCfmMepLbrBadMsdu.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLbrBadMsdu.setDescription('(optional) The total number of LBRs received whose mac_service_data_unit did not match (except for the OpCode) that of the corresponding LBM (20.2.3). ')
dot1agCfmMepLtmNextSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLtmNextSeqNumber.setReference('802.1ag clause 12.14.7.1.3:ab and 20.36.1')
if mibBuilder.loadTexts: dot1agCfmMepLtmNextSeqNumber.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLtmNextSeqNumber.setDescription('Next transaction identifier/sequence number to be sent in a Linktrace message. This sequence number can be zero because it wraps around. ')
dot1agCfmMepUnexpLtrIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepUnexpLtrIn.setReference('802.1ag clause 12.14.7.1.3:ac 20.39.1')
if mibBuilder.loadTexts: dot1agCfmMepUnexpLtrIn.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepUnexpLtrIn.setDescription('The total number of unexpected LTRs received (20.39.1). ')
dot1agCfmMepLbrOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrOut.setReference('802.1ag clause 12.14.7.1.3:ad and 20.26.2')
if mibBuilder.loadTexts: dot1agCfmMepLbrOut.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepLbrOut.setDescription('Total number of Loopback Replies transmitted.')
dot1agCfmMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 1, 1, 26), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepRowStatus.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepRowStatus.setDescription('The status of the row. The writable columns in a row can not be changed if the row is active. All columns must have a valid value before a row can be activated. ')
dot1agCfmLtrTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2), )
if mibBuilder.loadTexts: dot1agCfmLtrTable.setReference('802.1ag clause 12.14.7.5')
if mibBuilder.loadTexts: dot1agCfmLtrTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrTable.setDescription('This table extends the MEP table and contains a list of Linktrace replies received by a specific MEP in response to a linktrace message. SNMP SMI does not allow to state in a MIB that an object in a table is an array. The solution is to take the index (or indices) of the first table and add one or more indices. ')
dot1agCfmLtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmLtrSeqNumber"), (0, "ZXR10-CFM-MIB", "dot1agCfmLtrReceiveOrder"))
if mibBuilder.loadTexts: dot1agCfmLtrEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrEntry.setDescription('The Linktrace Reply table entry.')
dot1agCfmLtrSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrSeqNumber.setReference('802.1ag clause 12.14.7.5.2:b')
if mibBuilder.loadTexts: dot1agCfmLtrSeqNumber.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrSeqNumber.setDescription("Transaction identifier/Sequence number returned by a previous transmit linktrace message command, indicating which LTM's response is going to be returned. ")
dot1agCfmLtrReceiveOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrReceiveOrder.setReference('802.1ag clause 12.14.7.5.2:c')
if mibBuilder.loadTexts: dot1agCfmLtrReceiveOrder.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrReceiveOrder.setDescription('trace route index. ')
dot1agCfmLtrTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTtl.setReference('802.1ag clause 12.14.7.5 and 20.36.2.2')
if mibBuilder.loadTexts: dot1agCfmLtrTtl.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrTtl.setDescription('TTL field value for a returned LTR.')
dot1agCfmLtrForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrForwarded.setReference('802.1ag clauses 12.14.7.5.3:c and 20.36.2.1')
if mibBuilder.loadTexts: dot1agCfmLtrForwarded.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrForwarded.setDescription("Indicates if a LTM was forwarded by the responding MP, as returned in the 'FwdYes' flag of the flags field. ")
dot1agCfmLtrTerminalMep = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTerminalMep.setReference('802.1ag clauses 12.14.7.5.3:d and 20.36.2.1')
if mibBuilder.loadTexts: dot1agCfmLtrTerminalMep.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrTerminalMep.setDescription('A boolean value stating whether the forwarded LTM reached a MEP enclosing its MA, as returned in the Terminal MEP flag of the Flags field. ')
dot1agCfmLtrLastEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrLastEgressIdentifier.setReference('802.1ag clauses 12.14.7.5.3:e and 20.36.2.3')
if mibBuilder.loadTexts: dot1agCfmLtrLastEgressIdentifier.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrLastEgressIdentifier.setDescription('An octet field holding the Last Egress Identifier returned in the LTR Egress Identifier TLV of the LTR. The Last Egress Identifier identifies the MEP Linktrace Initiator that originated, or the Linktrace Responder that forwarded, the LTM to which this LTR is the response. This is the same value as the Egress Identifier TLV of that LTM. ')
dot1agCfmLtrNextEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrNextEgressIdentifier.setReference('802.1ag clauses 12.14.7.5.3:f and 20.36.2.4')
if mibBuilder.loadTexts: dot1agCfmLtrNextEgressIdentifier.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrNextEgressIdentifier.setDescription('An octet field holding the Next Egress Identifier returned in the LTR Egress Identifier TLV of the LTR. The Next Egress Identifier Identifies the Linktrace Responder that transmitted this LTR, and can forward the LTM to the next hop. This is the same value as the Egress Identifier TLV of the forwarded LTM, if any. If the FwdYes bit of the Flags field is false, the contents of this field are undefined, i.e. any value can be transmitted, and the field is ignored by the receiver. ')
dot1agCfmLtrRelay = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 8), Dot1agCfmRelayActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrRelay.setReference('802.1ag clauses 12.14.7.5.3:g and 20.36.2.5')
if mibBuilder.loadTexts: dot1agCfmLtrRelay.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrRelay.setDescription('Value returned in the Relay Action field.')
dot1agCfmLtrIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 9), Dot1agCfmIngressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngress.setReference('802.1ag clauses 12.14.7.5.3:k and 20.36.2.6')
if mibBuilder.loadTexts: dot1agCfmLtrIngress.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrIngress.setDescription('The value returned in the Ingress Action Field of the LTM.')
dot1agCfmLtrIngressMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressMac.setReference('802.1ag clauses 12.14.7.5.3:l and 20.36.2.7')
if mibBuilder.loadTexts: dot1agCfmLtrIngressMac.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrIngressMac.setDescription('MAC address returned in the ingress MAC address field.')
dot1agCfmLtrEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 11), Dot1agCfmEgressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgress.setReference('802.1ag clauses 12.14.7.5.3:o and 20.36.2.10')
if mibBuilder.loadTexts: dot1agCfmLtrEgress.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrEgress.setDescription('The value returned in the Egress Action Field of the LTM.')
dot1agCfmLtrEgressMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressMac.setReference('802.1ag clauses 12.14.7.5.3:p and 20.36.2.11')
if mibBuilder.loadTexts: dot1agCfmLtrEgressMac.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLtrEgressMac.setDescription('MAC address returned in the egress MAC address field.')
dot1agCfmMepDbTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3), )
if mibBuilder.loadTexts: dot1agCfmMepDbTable.setReference('802.1ag clause 19.2.15')
if mibBuilder.loadTexts: dot1agCfmMepDbTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDbTable.setDescription('The MEP Database. A database, maintained by every MEP, that maintains received information about other MEPs in the Maintenance Domain. The SMI does not allow to state in a MIB that an object in a table is an array. The solution is to take the index (or indices) of the first table and add one or more indices. ')
dot1agCfmMepDbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMepDbRSessionId"))
if mibBuilder.loadTexts: dot1agCfmMepDbEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDbEntry.setDescription('The MEP Database table entry.')
dot1agCfmMepDbRSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 1), Dot1agCfmSessionId())
if mibBuilder.loadTexts: dot1agCfmMepDbRSessionId.setReference('802.1ag clause 12.14.7.6.2:b')
if mibBuilder.loadTexts: dot1agCfmMepDbRSessionId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDbRSessionId.setDescription('Maintenance association End Point Identifier of a remote MEP whose information from the MEP Database is to be returned. ')
dot1agCfmMepDbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbMacAddress.setReference('802.1ag clause 12.14.7.6.3:d and 20.19.7')
if mibBuilder.loadTexts: dot1agCfmMepDbMacAddress.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDbMacAddress.setDescription('The MAC address of the remote MEP.')
dot1agCfmMepDbRdi = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRdi.setReference('802.1ag clauses 12.14.7.6.3:e and 20.19.2')
if mibBuilder.loadTexts: dot1agCfmMepDbRdi.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDbRdi.setDescription('State of the RDI bit in the last received CCM (true for RDI=1), or false if none has been received. ')
dot1agCfmMepDbId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMepDbId.setDescription('Session Id')
dot1agCfmLbrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 4))
dot1agCfmLbrTransId = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 4, 1), Dot1agCfmLbrTransId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLbrTransId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLbrTransId.setDescription(' ')
dot1agCfmLbrPrintInfo = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLbrPrintInfo.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmLbrPrintInfo.setDescription(' ')
dot1agCfmMipTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5), )
if mibBuilder.loadTexts: dot1agCfmMipTable.setReference('802.1ag clauses 12.14.7 and 19.2')
if mibBuilder.loadTexts: dot1agCfmMipTable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMipTable.setDescription(' MIP Table ')
dot1agCfmMipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1), ).setIndexNames((0, "ZXR10-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZXR10-CFM-MIB", "dot1agCfmMipSessionId"))
if mibBuilder.loadTexts: dot1agCfmMipEntry.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMipEntry.setDescription('The MIP table entry')
dot1agCfmMipSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMipSessionId.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMipSessionId.setDescription('Session Id')
dot1agCfmMipName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMipName.setReference('802.1ag clause 12.14.7.1.3:b')
if mibBuilder.loadTexts: dot1agCfmMipName.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMipName.setDescription(' Mip Name ')
dot1agCfmMipPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMipPortName.setReference('802.1ag clause 12.14.7.1.3:b')
if mibBuilder.loadTexts: dot1agCfmMipPortName.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmMipPortName.setDescription(' Mip Port Name ')
dot1agCfmGlobalIsEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 120, 1, 4, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmGlobalIsEnable.setReference(' ')
if mibBuilder.loadTexts: dot1agCfmGlobalIsEnable.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmGlobalIsEnable.setDescription(' ')
dot1agCfmFaultAlarm = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 120, 0, 1)).setObjects(("ZXR10-CFM-MIB", "dot1agCfmMepHighestPrDefect"))
if mibBuilder.loadTexts: dot1agCfmFaultAlarm.setStatus('current')
if mibBuilder.loadTexts: dot1agCfmFaultAlarm.setDescription("A MEP has a persistent defect condition. A notification (fault alarm) is sent to the management entity with the OID of the MEP that has detected the fault. Whenever a MEP has a persistent defect, it may or may not generate a Fault Alarm to warn the system administrator of the problem, as controlled by the MEP Fault Notification Generator State Machine and associated Managed Objects. Only the highest-priority defect, as shown in Table 20-1, is reported in the Fault Alarm. If a defect with a higher priority is raised after a Fault Alarm has been issued, another Fault Alarm is issued. The management entity receiving the notification can identify the system from the network source address of the notification, and can identify the MEP reporting the defect by the indices in the OID of the dot1agCfmMepHighestPrDefect variable in the notification: dot1agCfmMdIndex - Also the index of the MEP's Maintenance Domain table entry (dot1agCfmMdTable). dot1agCfmMaIndex - Also an index (with the MD table index) of the MEP's Maintenance Association table entry (dot1agCfmMaTable). dot1agCfmSessionId - MEP Identifier and final index into the MEP table (dot1agCfmMepTable). ")
if mibBuilder.loadTexts: dot1agCfmFaultAlarm.setReference('802.1ag clause 12.14.7.7')
mibBuilder.exportSymbols("ZXR10-CFM-MIB", dot1agCfmMepMacAddress=dot1agCfmMepMacAddress, dot1agNotifications=dot1agNotifications, dot1agCfmMaVlanListTable=dot1agCfmMaVlanListTable, Dot1agCfmIdPermission=Dot1agCfmIdPermission, dot1agCfmMaMepListTable=dot1agCfmMaMepListTable, dot1agCfmMepLbrOut=dot1agCfmMepLbrOut, dot1agCfmMdMhfIdPermission=dot1agCfmMdMhfIdPermission, Dot1agCfmEgressActionFieldValue=Dot1agCfmEgressActionFieldValue, dot1agCfmMepPrimaryVid=dot1agCfmMepPrimaryVid, Dot1agCfmMaintDomainNameType=Dot1agCfmMaintDomainNameType, dot1agCfmMaIdPermission=dot1agCfmMaIdPermission, dot1agCfmMepLowPrDef=dot1agCfmMepLowPrDef, dot1agCfmMepDefects=dot1agCfmMepDefects, dot1agCfmMepCciSentCcms=dot1agCfmMepCciSentCcms, dot1agCfmMdName=dot1agCfmMdName, dot1agCfmMipEntry=dot1agCfmMipEntry, dot1agCfmMepDbRSessionId=dot1agCfmMepDbRSessionId, dot1agCfmMep=dot1agCfmMep, VlanIdOrNone=VlanIdOrNone, dot1agCfmMepLbrIn=dot1agCfmMepLbrIn, dot1agCfmMepUnexpLtrIn=dot1agCfmMepUnexpLtrIn, dot1agCfmLtrSeqNumber=dot1agCfmLtrSeqNumber, InterfaceIndexOrZero=InterfaceIndexOrZero, dot1agCfmLbrInfo=dot1agCfmLbrInfo, dot1agCfmMepLMFlage=dot1agCfmMepLMFlage, dot1agCfmMaMepListSessionId=dot1agCfmMaMepListSessionId, Dot1agCfmMepDefects=Dot1agCfmMepDefects, dot1agCfmMepLtmNextSeqNumber=dot1agCfmMepLtmNextSeqNumber, zxr10cfmMIB=zxr10cfmMIB, PYSNMP_MODULE_ID=zxr10cfmMIB, dot1agCfmLtrEgressMac=dot1agCfmLtrEgressMac, dot1agCfmGlobalIsEnable=dot1agCfmGlobalIsEnable, dot1agCfmMd=dot1agCfmMd, dot1agCfmLtrReceiveOrder=dot1agCfmLtrReceiveOrder, dot1agCfmMepActive=dot1agCfmMepActive, Dot1agCfmMDLevel=Dot1agCfmMDLevel, dot1agMIBObjects=dot1agMIBObjects, Dot1agCfmMhfCreation=Dot1agCfmMhfCreation, dot1agCfmMaPrimaryVlanId=dot1agCfmMaPrimaryVlanId, dot1agCfmMaVlanListRowStatus=dot1agCfmMaVlanListRowStatus, Dot1agCfmLbrTransId=Dot1agCfmLbrTransId, dot1agCfmLtrForwarded=dot1agCfmLtrForwarded, Dot1agCfmMaintAssocName=Dot1agCfmMaintAssocName, dot1agCfmMepMEPAttachType=dot1agCfmMepMEPAttachType, VlanId=VlanId, dot1agCfmMepLbrBadMsdu=dot1agCfmMepLbrBadMsdu, dot1agCfmLtrIngressMac=dot1agCfmLtrIngressMac, dot1agCfmLbrTransId=dot1agCfmLbrTransId, dot1agCfmMipSessionId=dot1agCfmMipSessionId, dot1agCfmMepDbEntry=dot1agCfmMepDbEntry, dot1agCfmGloPara=dot1agCfmGloPara, dot1agCfmMASpeed=dot1agCfmMASpeed, dot1agCfmMdRowStatus=dot1agCfmMdRowStatus, Dot1agCfmSpeed=Dot1agCfmSpeed, Dot1agCfmRelayActionFieldValue=Dot1agCfmRelayActionFieldValue, dot1agCfmMaEntry=dot1agCfmMaEntry, dot1agCfmLtrTable=dot1agCfmLtrTable, dot1agCfmSessionId=dot1agCfmSessionId, dot1agCfmLtrEntry=dot1agCfmLtrEntry, dot1agCfmMa=dot1agCfmMa, dot1agCfmMepId=dot1agCfmMepId, dot1agCfmMipPortName=dot1agCfmMipPortName, dot1agCfmMepIfIndex=dot1agCfmMepIfIndex, Dot1afCfmIndexIntegerNextFree=Dot1afCfmIndexIntegerNextFree, dot1agCfmLtrTerminalMep=dot1agCfmLtrTerminalMep, dot1agCfmMdTable=dot1agCfmMdTable, dot1agCfmMaVlanListIdentifier=dot1agCfmMaVlanListIdentifier, dot1agCfmLtrRelay=dot1agCfmLtrRelay, Dot1agCfmLowestAlarmPri=Dot1agCfmLowestAlarmPri, Dot1agCfmMaintAssocNameType=Dot1agCfmMaintAssocNameType, dot1agCfmMepCcmLtmPriority=dot1agCfmMepCcmLtmPriority, dot1agCfmMepLbrInOutOfOrder=dot1agCfmMepLbrInOutOfOrder, dot1agCfmLtrTtl=dot1agCfmLtrTtl, Dot1agCfmFngState=Dot1agCfmFngState, Dot1agCfmMaintDomainName=Dot1agCfmMaintDomainName, dot1agCfmMaTable=dot1agCfmMaTable, dot1agCfmMepDbRdi=dot1agCfmMepDbRdi, dot1agCfmMepCciEnabled=dot1agCfmMepCciEnabled, dot1agCfmMepDbId=dot1agCfmMepDbId, dot1agCfmLtrLastEgressIdentifier=dot1agCfmLtrLastEgressIdentifier, dot1agCfmMepDMFlage=dot1agCfmMepDMFlage, dot1agCfmMdFormat=dot1agCfmMdFormat, dot1agCfmMdMaTableNextIndex=dot1agCfmMdMaTableNextIndex, dot1agCfmMaMepListEntry=dot1agCfmMaMepListEntry, Dot1agCfmIngressActionFieldValue=Dot1agCfmIngressActionFieldValue, dot1agCfmMaVlanListEntry=dot1agCfmMaVlanListEntry, dot1agCfmMaMepListRowStatus=dot1agCfmMaMepListRowStatus, dot1agCfmMepTable=dot1agCfmMepTable, dot1agCfmMaName=dot1agCfmMaName, dot1agCfmMepTunnelId=dot1agCfmMepTunnelId, dot1agCfmLbrPrintInfo=dot1agCfmLbrPrintInfo, dot1agCfmMepPortName=dot1agCfmMepPortName, dot1agCfmMepDbTable=dot1agCfmMepDbTable, dot1agCfmMepRowStatus=dot1agCfmMepRowStatus, dot1agCfmFaultAlarm=dot1agCfmFaultAlarm, dot1agCfmMdTableNextIndex=dot1agCfmMdTableNextIndex, dot1agCfmMdIndex=dot1agCfmMdIndex, dot1agCfmMepDirection=dot1agCfmMepDirection, dot1agCfmMepFngState=dot1agCfmMepFngState, Dot1agCfmSessionId=Dot1agCfmSessionId, Dot1agCfmCcmInterval=Dot1agCfmCcmInterval, dot1agCfmMdMdLevel=dot1agCfmMdMdLevel, dot1agCfmLtrIngress=dot1agCfmLtrIngress, dot1agCfmMdMhfCreation=dot1agCfmMdMhfCreation, dot1agCfmMepDbMacAddress=dot1agCfmMepDbMacAddress, Dot1agCfmHighestDefectPri=Dot1agCfmHighestDefectPri, dot1agCfmMaIndex=dot1agCfmMaIndex, dot1agCfmMaFormat=dot1agCfmMaFormat, dot1agCfmMdEntry=dot1agCfmMdEntry, dot1agCfmLtrNextEgressIdentifier=dot1agCfmLtrNextEgressIdentifier, dot1agCfmMaRowStatus=dot1agCfmMaRowStatus, dot1agCfmLtrEgress=dot1agCfmLtrEgress, dot1agCfmMepHighestPrDefect=dot1agCfmMepHighestPrDefect, dot1agCfmMaMhfCreation=dot1agCfmMaMhfCreation, Dot1agCfmMpDirection=Dot1agCfmMpDirection, dot1agCfmMipTable=dot1agCfmMipTable, dot1agCfmMipName=dot1agCfmMipName, dot1agCfmMaCcmInterval=dot1agCfmMaCcmInterval, dot1agCfmMepEntry=dot1agCfmMepEntry)
