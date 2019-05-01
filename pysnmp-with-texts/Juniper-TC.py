#
# PySNMP MIB module Juniper-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:01:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, Gauge32, Unsigned32, iso, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, MibIdentifier, Integer32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "iso", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 1))
juniTextualConventions.setRevisions(('2005-12-21 20:13', '2005-11-18 22:30', '2004-12-03 22:12', '2003-11-12 22:31', '2002-09-16 21:44', '2002-04-04 16:35', '2001-03-08 22:26', '1999-12-12 00:00', '1999-07-14 00:00', '1998-11-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniTextualConventions.setRevisionsDescriptions(('Added JuniNibbleConfig.', 'Added JuniTimeFilter.', 'Added JuniVrfGroupName.', 'Increased the size of JuniInterfaceLocation. Added JuniInterfaceLocationType and JuniInterfaceLocationValue.', 'Replaced Unisphere names with Juniper names. Added JuniInterfaceDescrFormat and JuniInterfaceLocation.', 'Increased the size limits on JuniName and JuniVrfName.', 'Added JuniVrfName and JuniSetMap.', 'Added JuniLogSeverity.', 'Added JuniAcctngAdminType and JuniAcctngOperType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniTextualConventions.setLastUpdated('200512212013Z')
if mibBuilder.loadTexts: juniTextualConventions.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniTextualConventions.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniTextualConventions.setDescription('Textual conventions defined and used by the Juniper Networks enterprise.')
class JuniEnable(TextualConvention, Integer32):
    description = "Enterprise-standard SYNTAX for MIB objects having enumerated value pair 'enable' and 'disable'. Used for both admin (configurable) and oper (read-only) objects."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class JuniName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    description = 'A virtual router text name of restricted length. Represents textual information taken from the NVT ASCII graphics character set (codes 32 through 126).'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JuniVrfName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    description = 'A VPN routing forwarding text name of restricted length. Represents textual information taken from the NVT ASCII graphics character set (codes 32 through 126).'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniNextIfIndex(TextualConvention, Integer32):
    description = 'Coordinate ifIndex value allocation for entries in an associated ifIndex-ed interface table, by first reading an ifIndex value from this object, then creating an entry, having that ifIndex value, in the associated interface table. The DESCRIPTION clause for an object of this type must identify the associated interface table. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an object of this type is read-only, and a SET of such an object returns a notWritable error.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JuniIpAddrLessIf(TextualConvention, IpAddress):
    description = "Compressed index representation to identify both numbered and unnumbered ('address-less') IP subnetworks. One approach is to identify such interfaces with a 2-tuple consisting of <IpAddress, ifIndex>, where only one of the pair is nonzero for a valid interface (IpAddress is nonzero for numbered interfaces, ifIndex is nonzero for unnumbered interfaces). As an alternative, this textual convention compresses the 2-tuple information into an IpAddress (32-bit) format a.b.c.d having the following interpretation: Format Interpretation IP Interface Type ------------------------------------------------------------------ 0.0.0.0 'null' value 'none' or 'wildcard', etc. a.b.c.d, a != 0 IP Address Numbered 0.b.c.d ifIndex Unnumbered For the unnumbered case, the value of the ifIndex is given by (b * 65536) + (c * 256) + (d) A side-effect of this approach is that ifIndex values for IP network interfaces must fall in the range 1..16777215 (i.e. 24 bits)."
    status = 'current'

class JuniTimeSlotMap(TextualConvention, OctetString):
    description = 'A bit map representing one or more timeslots of a DS1/E1 interface. Bits are numbered in descending order from 31-0 starting from the most significant bit of the first octet and ending with the least significant bit of the fourth octet. Bits 1-24 are relevant for DS1 interfaces, bits 0-31 are relevant for E1 interfaces. A bit is set if the associated timeslot is in use, and cleared if the associated timeslot is not in use.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class JuniAcctngAdminType(TextualConvention, Integer32):
    description = 'The desired administrative state for the collection of accounting records. The administrative domain governed by an object of JuniAcctngAdminType is defined in the MIB OBJECT description that uses this type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class JuniAcctngOperType(TextualConvention, Integer32):
    description = 'The operational state for the collection of accounting records. The administrative domain that an object of this type is reporting state for, is defined in the MIB object description that uses this type. The notSupported(2) state indicates that accounting data collection is not supported for the entity using an object of JuniAcctngOperType type. If an entity does not support accounting data collection, an object of JuniAcctngOperType type will report notSupported(2) regardless of the value set in the corresponding JuniAcctngAdminType. The disabled(0) state indicates that the corresponding JuniAcctngAdminType object has been set to disabled(0). If a data collection is in process, the value of JuniAcctngOperType will change to disabled(0) after the current collection completes. The enabled(1) state indicates that the corresponding JuniAcctngAdminType object has been set to enabled(1) and that the entity is ready to collect accounting records.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("notSupported", 2))

class JuniLogSeverity(TextualConvention, Integer32):
    description = "The log severity level. Lower numerical values correspond to higher severity levels. The value 'off' filters all severity levels."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("off", -1), ("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

class JuniSetMap(TextualConvention, OctetString):
    description = "A bitmap indicating which objects in a table entry have been explicitly configured. A 1 in a bit position indicates the corresponding table entry object has been explicitly configured. A 0 in a bit position indicates the corresponding table entry has NOT been explicitly configured (and typically contains the default setting defined in the DEFVAL clause for that object). Once set, a bit typically remains set until the table entry is destroyed. The semantics of an object of this type should specify by what circumstances, if any, bits in the map may be cleared. If an entry exists in a table but no entry objects have been configured, JuniSetMap will contain a zero-length string. The DESCRIPTION clause for an object having this SYNTAX should indicate which, if any, entry objects are excluded from representation in the JuniSetMap. Typically, index and RowStatus entry objects would not be represented. Bit positions correspond to table entry objects as follows: Objects in the table entry are numbered according to the last OID subidentifier of their object type as defined in the MIB. For example, an object in a table entry having OID 1.3.6.1.2.1.2.2.1.5 would be object number 5. (Instance-identifying OID subidentifiers are ignored.) Octets in the map are numbered 1..N beginning with the first octet. Bits in an octet are numbered 1..8 beginning with the MOST significant bit. Bit B in octet Q represents the entry object numbered E thus: E = (((Q - 1) * 8) + B) For example, the third most significant bit in the second octet represents the entry object numbered 11: ((((2 - 1) * 8) + 3) = 11 Conversely, the octet Q and bit B positions of the corresponding bit for a given entry object numbered E is determined by: Q = (((E - 1) / 8) + 1) (where '/' means integer division) B = (((E - 1) modulo 8) + 1) For example, the octet and bit positions of the entry object numbered 11 are: (((11 - 1) / 8) + 1) = 2 (octet number) (((11 - 1) modulo 8) + 1) = 3 (3rd most sig. bit) "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class JuniInterfaceDescrFormat(TextualConvention, Integer32):
    description = 'The interface description format setting. proprietary(0) Juniper encoding Example Column: IP 3/0.1, ATM 3/0.1, ATM 3/0 industryCommon(1) ATM 3/0.1, ATM3/0.1 ATM 3/0 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("proprietary", 0), ("industryCommon", 1))

class JuniInterfaceLocation(TextualConvention, OctetString):
    description = "An ASCII string representation of an interfaces location in the following forms: slot/port slot/adapter/port adapter/port Examples: 3/0, 12/0/1, 0/0 The form is determined by the physical architecture of the router platform. E.g., the ERX family of platforms (first generation E-series) requires the 'slot/port' form."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class JuniInterfaceLocationType(TextualConvention, Integer32):
    description = "Describes the platform-dependent interpretation of a JuniInterfaceLocationValue object: unknown - Unspecified/unknown slotPort - Two octets in length; 1st octet is 'slot', 2nd octet is 'port' slotAdapterPort - Three octets in length; 1st octet is 'slot', 2nd octet is 'adapter', 3rd octet is 'port' adapterPort - Two octets in length; 1st octet is 'adapter', 2nd octet is 'port' "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("slotPort", 1), ("slotAdapterPort", 2), ("adapterPort", 3))

class JuniInterfaceLocationValue(TextualConvention, OctetString):
    description = "The value of a platform-dependent interface location, represented as an OCTET STRING. A corresponding JuniInterfaceLocationType object will identify the mapping of octets to location elements, e.g. 'slot.port'. Note: When the value of an object having this syntax is encoded as a MIB table INDEX, the rules for encoding a variable-length OCTET STRING are observed."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class JuniVrfGroupName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    description = 'A VPN routing forwarding group name of restricted length. Represents textual information taken from the NVT ASCII graphics character set (codes 32 through 126).'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniTimeFilter(TextualConvention, TimeTicks):
    reference = 'Refer to RFC 2021 for the definition of the TimeFilter, its usage and implementation notes.'
    description = 'Used as an index to a table. A TimeFilter variable allows a GetNext or GetBulk request to find rows in a table for which the TimeFilter index variable is greater than or equal to a specified value. JuniTimeFilter is same as TimeFilter. Detailed description of TimeFilter variables, their implementation and use is documented in the RMON2 MIB.'
    status = 'current'

class JuniNibbleConfig(TextualConvention, Integer32):
    description = 'A configuration variable comprised of nibbles i.e. 4 bits, such that a client can supply a list of 0 to 8 selections. The least significant nibble is the first value of the list, and the most significant nibble is the last value. The value in each field ranges from 0 to 15, however the first nibble with value 0 indicates the end of the list. Repetition of values is not allowed. Segregation of values in not allowed. Example valid encoding: 0x00000321 0x00083E12 Not a valid encoding: 0x00000121- will return an error 0x01002001- will return an error.'
    status = 'current'

mibBuilder.exportSymbols("Juniper-TC", JuniAcctngOperType=JuniAcctngOperType, JuniInterfaceLocationType=JuniInterfaceLocationType, JuniLogSeverity=JuniLogSeverity, JuniName=JuniName, JuniVrfGroupName=JuniVrfGroupName, juniTextualConventions=juniTextualConventions, JuniNextIfIndex=JuniNextIfIndex, JuniTimeFilter=JuniTimeFilter, PYSNMP_MODULE_ID=juniTextualConventions, JuniInterfaceLocation=JuniInterfaceLocation, JuniTimeSlotMap=JuniTimeSlotMap, JuniEnable=JuniEnable, JuniSetMap=JuniSetMap, JuniVrfName=JuniVrfName, JuniInterfaceLocationValue=JuniInterfaceLocationValue, JuniIpAddrLessIf=JuniIpAddrLessIf, JuniNibbleConfig=JuniNibbleConfig, JuniAcctngAdminType=JuniAcctngAdminType, JuniInterfaceDescrFormat=JuniInterfaceDescrFormat)
