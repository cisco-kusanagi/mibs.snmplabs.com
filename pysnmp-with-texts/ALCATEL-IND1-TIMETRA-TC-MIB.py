#
# PySNMP MIB module ALCATEL-IND1-TIMETRA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-TIMETRA-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
timetraModules, = mibBuilder.importSymbols("ALCATEL-IND1-TIMETRA-GLOBAL-MIB", "timetraModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, Integer32, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, MibIdentifier, Counter64, iso, ObjectIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Integer32", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter64", "iso", "ObjectIdentity", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
timetraTCMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 2))
timetraTCMIBModule.setRevisions(('1908-01-01 00:00', '1907-01-01 00:00', '1906-03-23 00:00', '1905-08-31 00:00', '1905-01-24 00:00', '1904-01-15 00:00', '1903-08-15 00:00', '1903-01-20 00:00', '1901-05-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraTCMIBModule.setRevisionsDescriptions(('Rev 6.0 01 Jan 2008 00:00 6.0 release of the TIMETRA-TC-MIB.', 'Rev 5.0 01 Jan 2007 00:00 5.0 release of the TIMETRA-TC-MIB.', 'Rev 4.0 23 Mar 2006 00:00 4.0 release of the TIMETRA-TC-MIB.', 'Rev 3.0 31 Aug 2005 00:00 3.0 release of the TIMETRA-TC-MIB.', 'Rev 2.1 24 Jan 2005 00:00 2.1 release of the TIMETRA-TC-MIB.', 'Rev 2.0 15 Jan 2004 00:00 2.0 release of the TIMETRA-TC-MIB.', 'Rev 1.2 15 Aug 2003 00:00 1.2 release of the TIMETRA-TC-MIB.', 'Rev 1.0 20 Jan 2003 00:00 1.0 Release of the TIMETRA-TC-MIB.', 'Rev 0.1 14 Aug 2000 00:00 First version of the TIMETRA-TC-MIB.',))
if mibBuilder.loadTexts: timetraTCMIBModule.setLastUpdated('0801010000Z')
if mibBuilder.loadTexts: timetraTCMIBModule.setOrganization('Alcatel')
if mibBuilder.loadTexts: timetraTCMIBModule.setContactInfo('Alcatel 7x50 Support Web: http://www.alcatel.com/comps/pages/carrier_support.jhtml')
if mibBuilder.loadTexts: timetraTCMIBModule.setDescription("This document is the SNMP MIB module for the SNMP Textual Conventions (TCs) used in the Alcatel 7x50 manageability instrumentation. Copyright 2003-2008 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel's proprietary intellectual property. Alcatel retains all title and ownership in the Specification, including any revisions. Alcatel grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied `as is', and Alcatel makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub- layer must remain constant at least from one re- initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'

class TmnxPortID(TextualConvention, Unsigned32):
    description = "A portid is an unique 32 bit number encoded as shown below. 32 30 | 29 26 | 25 22 | 21 16 | 15 1 | +-----+-------+-------+-------+-------+ |000 | slot | mda | port | zero | Physical Port +-----+-------+-------+-------+-------+ 32 30 | 29 26 | 25 22 | 21 16 | 15 1 | +-----+-------+-------+-------+-------+ |001 | slot | mda | port |channel| Channel +-----+-------+-------+-------+-------+ Slots, mdas (if present), ports, and channels are numbered starting with 1. 32 29 | 28 10 | 9 1 | +---------+-------------------+-------+ | 0 1 0 0 | zeros | ID | Virtual Port +---------+-------------------+-------+ 32 29 | 28 9 | 8 1 | +---------+---------------------+-----+ | 0 1 0 1 | zeros | ID | LAG Port +---------+---------------------+-----+ A card port number (cpn) has significance within the context of the card on which it resides(ie., cpn 2 may exist in one or more cards in the chassis). Whereas, portid is an unique/absolute port number (apn) within a given chassis. An 'invalid portid' is a TmnxPortID with a value of 0x1e000000 as represented below. 32 30 | 29 26 | 25 22 | 21 16 | 15 1 | +-----+-------+-------+-------+-------+ |zero | ones | zero | zero | zero | Invalid Port +-----+-------+-------+-------+-------+"
    status = 'current'

class TmnxEncapVal(TextualConvention, Unsigned32):
    description = 'The value of the label used to identify the entity using the specified encapsulation value on a specific port. The format of this object depends on the encapsulation type defined on this port. When the encapsulation is nullEncap the value of this object must be zero. 31 0 +--------+--------+--------+--------+ |00000000 00000000 00000000 00000000| +--------+--------+--------+--------+ When the encapsulation is dot1qEncap the value of this object is equal to the 12-bit IEEE 802.1Q VLAN ID. 31 0 +--------+--------+--------+--------+ |00000000 00000000 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is mplsEncap the value of this object is equal to the 20-bit LSP ID. 31 0 +--------+--------+--------+--------+ |00000000 0000XXXX XXXXXXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is frEncap, the value of this object is equal to the 10-bit Frame Relay DLCI. 31 0 +--------+--------+--------+--------+ |00000000 00000000 000000XX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is qinqEncap, the value of the outer 802.1Q VLAN ID is encoded in the least significant 16 bits, and the value of the inner VLAN ID is encoded in the most significant 16 bits. 31 0 +--------+--------+--------+--------+ |0000YYYY YYYYYYYY 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is atmEncap, the value of the ATM VCI is encoded in the least significant 16 bits, and the value of the ATM VPI is encoded in the next 12 bits. For ATM VCs, the top 2 bits are 00. The value of the ATM VCI is encoded in the least significant 16 bits, and the value of the ATM VPI is encoded in the next 12 bits. 31 0 +--------+--------+--------+--------+ |0000YYYY YYYYYYYY XXXXXXXX XXXXXXXX| +--------+--------+--------+--------+ For ATM VPs, the top 2 bits are 01. The value of the ATM VPI is encoded in the least significant 12 bits. 31 0 +--------+--------+--------+--------+ |01000000 00000000 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ For ATM VP ranges, the top 2 bits are 10. The value of the start of the ATM VPI range is encoded in the least significant 12 bits, and the value of the end of the ATM VP range is encoded in the next 12 bits. 31 0 +--------+--------+--------+--------+ |10000000 YYYYYYYY YYYYXXXX XXXXXXXX| +--------+--------+--------+--------+ For ATM ports, the top 2 bits are 11, and the rest of the bits must be zero. 31 0 +--------+--------+--------+--------+ |11000000 00000000 00000000 00000000| +--------+--------+--------+--------+ When the encapsulation is wanMirrorEncap the value of this object is equal to the 12-bit value. 31 0 +--------+--------+--------+--------+ |00000000 00000000 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ Some ports have a restrictions to the encapsulation types that they can support and hence impose restrictions on the respective formats defined above.'
    status = 'current'

class QTag(TextualConvention, Integer32):
    description = 'The QTag data type is a 12-bit integer tag used to identify a service. The values 0 and 4095 are not allowed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class QTagOrZero(TextualConvention, Unsigned32):
    description = "The data type QTagOrZero represents a VLAN tag. The value '0' indicates that no VLAN tag is provisioned, or that its value is unknown."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class TmnxStrSapId(TextualConvention, OctetString):
    description = 'The value of TmnxStrSapId is a printable string which contains the owner SAP Id or equivalent on a remote system. The string should contain the printable string equivalent of the textual-conventions TmnxPortID and TmnxEncapVal in the format specified as TmnxPortID[:TmnxEncapVal]'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class IpAddressPrefixLength(TextualConvention, Integer32):
    reference = ''
    description = 'the number of bits to match in an IP address mask.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class TmnxActionType(TextualConvention, Integer32):
    description = "The TmnxActionType data type is an enumerated integer that describes the values used to support action or operation style commands. Setting a variable of this type to 'doAction' causes the action to occur. GETs and GETNEXTs on this variable return 'not-applicable'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("doAction", 1), ("notApplicable", 2))

class TmnxAdminState(TextualConvention, Integer32):
    description = 'The TmnxAdminState data type is an enumerated integer that describes the values used to identify the administratively desired state of functional modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noop", 1), ("inService", 2), ("outOfService", 3))

class TmnxOperState(TextualConvention, Integer32):
    description = 'The TmnxOperState data type is an enumerated integer that describes the values used to identify the current operational state of functional modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4))

class TmnxStatus(TextualConvention, Integer32):
    description = "The TmnxStatus data type is an enumerated integer that describes the values used to identify the current status of functional modules in the system such as OSPF and MPLS protocols. Setting this variable to 'create' causes instantiation of the feature in the system. Setting it to 'delete' removes the instance and all associated configuration information."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("delete", 2))

class TmnxEnabledDisabled(TextualConvention, Integer32):
    description = "The TmnxEnabledDisabled data type is an enumerated integer that describes the values used to identify whether an entity is 'enabled' or 'disabled'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TNamedItem(TextualConvention, OctetString):
    description = 'The name of an item. When used as an index to a table, the item name uniquely identifies the instance. When used in a reference (TNamedItemOrEmpty) the item name entry must exist in the table. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TNamedItemOrEmpty(TextualConvention, OctetString):
    description = 'The name of an item, or an empty string. When used in a reference (TNamedItemOrEmpty) the item name entry must exist in the table. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TItemDescription(TextualConvention, OctetString):
    description = 'Description for an item. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

class TItemLongDescription(TextualConvention, OctetString):
    description = 'Longer description for an item. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 160)

class TmnxVRtrID(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system. The number 0 will have special significance in the context the TC is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4096)

class TmnxBgpAutonomousSystem(TextualConvention, Integer32):
    reference = 'BGP4-MIB.bgpPeerRemoteAs'
    description = 'an autonomous system (AS) number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxBgpLocalPreference(TextualConvention, Unsigned32):
    reference = 'RFC 1771 section 4.3 Path Attributes e)'
    description = 'a local route preference value.'
    status = 'current'

class TmnxBgpPreference(TextualConvention, Unsigned32):
    reference = 'RFC 1771 section 4.3 Path Attributes e)'
    description = 'a route preference value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxCustId(TextualConvention, Unsigned32):
    description = 'A number used to identify a Customer or Subscriber. This ID must be unique within the Service Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class TmnxServId(TextualConvention, Unsigned32):
    description = 'A number used to identify a Service. This ID must be unique within the Service Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class ServiceAdminStatus(TextualConvention, Integer32):
    reference = ''
    description = 'ServiceAdminStatus data type is an enumerated integer that describes the values used to identify the administrative state of a service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ServiceOperStatus(TextualConvention, Integer32):
    reference = ''
    description = 'ServiceOperStatus data type is an enumerated integer that describes the values used to identify the current operational state of a service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class TPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TSapIngressPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a SAP ingress policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TSapEgressPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a SAP egress policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TPolicyStatementNameOrEmpty(TextualConvention, OctetString):
    description = 'The name of a policy statement, when an object refers to it.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TmnxVcType(TextualConvention, Integer32):
    description = "The value of TmnxVcType is an enumerated integer that indicates a Virtual Circuit (VC) type. 'frDlciMartini(1)' replaces the old 'frDlci' when used over martini tunnels."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10, 11, 17, 18, 19, 20, 21, 23, 25, 4096))
    namedValues = NamedValues(("frDlciMartini", 1), ("atmSdu", 2), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("atmVccCell", 9), ("atmVpcCell", 10), ("ipipe", 11), ("satopE1", 17), ("satopT1", 18), ("satopE3", 19), ("satopT3", 20), ("cesopsn", 21), ("cesopsnCas", 23), ("frDlci", 25), ("mirrorDest", 4096))

class TmnxVcId(TextualConvention, Unsigned32):
    description = 'A 32 bit number is used to identify a VC(Virtual Circuit). The VC ID cannot be 0.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxVcIdOrNone(TextualConvention, Unsigned32):
    description = 'A 32 bit number is used to identify a VC(Virtual Circuit). A value of 0 indicates no VC ID is configured or available.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class Dot1PPriority(TextualConvention, Integer32):
    reference = ''
    description = 'IEEE 802.1p priority. zero is lowest, seven is highest. -1 means not set'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class ServiceAccessPoint(TextualConvention, Integer32):
    reference = 'assigned numbers: http://www.iana.org/assignments/ieee-802-numbers'
    description = '802.2 LLC SAP value, Source and Destination.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TLspExpValue(TextualConvention, Integer32):
    reference = ''
    description = 'MPLS Experimental bits. -1 means not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TIpProtocol(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/protocol-numbers'
    description = 'IP protocol number. well known protocol numbers include ICMP(1), TCP(6), UDP(17). -1 means value not set. -2 indicates protocol wildcard for UDP and TCP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TIpOption(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/ip-parameters'
    description = 'IP packet options octet. explanation of the octet bits: IP OPTION NUMBERS The Internet Protocol (IP) has provision for optional header fields identified by an option type field. Options 0 and 1 are exactly one octet which is their type field. All other options have their one octet type field, followed by a one octet length field, followed by length-2 octets of option data. The option type field is sub-divided into a one bit copied flag, a two bit class field, and a five bit option number. These taken together form an eight bit value for the option type field. IP options are commonly refered to by this value. Copy Class Number Value Name Reference ---- ----- ------ ----- ------------------------------- --------- 0 0 0 0 EOOL - End of Options List [RFC791,JBP] 0 0 1 1 NOP - No Operation [RFC791,JBP] 1 0 2 130 SEC - Security [RFC1108] 1 0 3 131 LSR - Loose Source Route [RFC791,JBP] 0 2 4 68 TS - Time Stamp [RFC791,JBP] 1 0 5 133 E-SEC - Extended Security [RFC1108] 1 0 6 134 CIPSO - Commercial Security [???] 0 0 7 7 RR - Record Route [RFC791,JBP] 1 0 8 136 SID - Stream ID [RFC791,JBP] 1 0 9 137 SSR - Strict Source Route [RFC791,JBP] 0 0 10 10 ZSU - Experimental Measurement [ZSu] 0 0 11 11 MTUP - MTU Probe [RFC1191]* 0 0 12 12 MTUR - MTU Reply [RFC1191]* 1 2 13 205 FINN - Experimental Flow Control [Finn] 1 0 14 142 VISA - Expermental Access Control [Estrin] 0 0 15 15 ENCODE - ??? [VerSteeg] 1 0 16 144 IMITD - IMI Traffic Descriptor [Lee] 1 0 17 145 EIP - Extended Internet Protocol[RFC1385] 0 2 18 82 TR - Traceroute [RFC1393] 1 0 19 147 ADDEXT - Address Extension [Ullmann IPv7] 1 0 20 148 RTRALT - Router Alert [RFC2113] 1 0 21 149 SDB - Selective Directed Broadcast[Graff] 1 0 22 150 NSAPA - NSAP Addresses [Carpenter] 1 0 23 151 DPS - Dynamic Packet State [Malis] 1 0 24 152 UMP - Upstream Multicast Pkt. [Farinacci] [Note, an asterisk (*) denotes an obsoleted IP Option Number.] '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TTcpUdpPort(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/port-numbers'
    description = 'The number of a TCP or UDP port. Well known port numbers include ftp-data(20), ftp(21), telnet(23), smtp(25), http(80), pop3(110), nntp(119), snmp(161), snmptrap(162), etc.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TTcpUdpPortOperator(TextualConvention, Integer32):
    description = "The operator specifies the manner in which a couple of other MIB objects in the table are supposed to be used. Operator Value1 Value2 ---------------------------------------------------- none(0) Any(0) Any(0) eq(1) Specified Value Any(0) range(2) Starting Value Ending Value lt(3) Specified Value Any(0) gt(4) Specified Value Any(0) 'Any(0)' specifies that, this object can accept any values but would default to 0. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("eq", 1), ("range", 2), ("lt", 3), ("gt", 4))

class TFrameType(TextualConvention, Integer32):
    description = 'The type of the frame for which this mac filter match criteria is defined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("e802dot3", 0), ("e802dot2LLC", 1), ("e802dot2SNAP", 2), ("ethernetII", 3))

class TQueueId(TextualConvention, Integer32):
    description = 'The value of TQueueId specifies the identification number of a queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressQueueId(TextualConvention, Integer32):
    description = 'The value of TIngressQueueId specifies the identification number of an ingress queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TIngressQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TEgressQueueId(TextualConvention, Integer32):
    description = 'The value of TEgressQueueId specifies the identification number of an egress queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TEgressQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TDSCPName(TextualConvention, OctetString):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TDSCPNameOrEmpty(TextualConvention, OctetString):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TDSCPValue(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class TDSCPValueOrNone(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point (DSCP). A value of -1 means that no DSCP value is configured or available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
class TDSCPFilterActionValue(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point. -1 means not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TFCName(TextualConvention, OctetString):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TFCNameOrEmpty(TextualConvention, OctetString):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TFCSet(TextualConvention, Bits):
    description = 'This data type describes a set of Forwarding Classes.'
    status = 'current'
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TFCType(TextualConvention, Integer32):
    description = 'This data type enumerates the Forwarding Classes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TmnxTunnelType(TextualConvention, Integer32):
    description = 'The type of this tunnel entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("sdp", 1), ("ldp", 2), ("rsvp", 3), ("gre", 4), ("bypass", 5), ("invalid", 6))

class TmnxTunnelID(TextualConvention, Unsigned32):
    description = 'The identifying value for a BGP-VPRN tunnel. Depending on the tunnel type the associated tunnel-id may be an sdp-id, an lsp-id or zero(0).'
    status = 'current'

class TmnxBgpRouteTarget(TextualConvention, OctetString):
    description = 'TmnxBgpRouteTarget is an readable string that specifies the extended community name to be accepted by a Route Reflector Server or advertised by the router when reflecting any routes. I.e, it does not apply to routes that are not reflected by the router.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxVPNRouteDistinguisher(TextualConvention, OctetString):
    description = 'The VPRN route distinguisher is a 8-octet object. It contains a 2-octet type field followed by a 6-octet value field. The type field specify how to interpret the value field. Type 0 specifies two subfields as a 2-octet administrative field and a 4-octet assigned number subfield. Type 1 specifies two subfields as a 4-octet administrative field which must contain an IP address and a 2-octet assigned number subfield. Type 2 specifies two subfields as a 4-octet administrative field which contains a 4-octet AS number and a 2-octet assigned number subfield.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SdpBindId(TextualConvention, OctetString):
    description = 'The value used to uniquely identify an SDP Binding. The first four octets correspond to the zero-extended 16-bit SDP ID, while the remaining four octets correspond to the 32-bit VC ID, both encoded in network byte order.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxVRtrMplsLspID(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each Label Switched Path in the managed system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TPortSchedulerPIR(TextualConvention, Integer32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 40000000), )
class TPortSchedulerCIR(TextualConvention, Integer32):
    description = 'The Committed Information Rate (CIR) rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 40000000), )
class TWeight(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class TPIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    description = 'The secondary shaper PIR rate to be used in Mbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000), )
class TPIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TPIRRateOrZero(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. The value 0 means undefined rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class TmnxDHCP6MsgType(TextualConvention, Integer32):
    description = 'The DHCP6 messagetype.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("dhcp6MsgTypeSolicit", 1), ("dhcp6MsgTypeAdvertise", 2), ("dhcp6MsgTypeRequest", 3), ("dhcp6MsgTypeConfirm", 4), ("dhcp6MsgTypeRenew", 5), ("dhcp6MsgTypeRebind", 6), ("dhcp6MsgTypeReply", 7), ("dhcp6MsgTypeRelease", 8), ("dhcp6MsgTypeDecline", 9), ("dhcp6MsgTypeReconfigure", 10), ("dhcp6MsgTypeInfoRequest", 11), ("dhcp6MsgTypeRelayForw", 12), ("dhcp6MsgTypeRelayReply", 13), ("dhcp6MsgTypeMaxValue", 14))

class TmnxOspfInstance(TextualConvention, Unsigned32):
    description = 'A number used to identify an instance of OSPF.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class TmnxBGPFamilyType(TextualConvention, Bits):
    description = 'The value of TmnxBGPFamilyType specifies the AFI-SAFI family for BGP peer.'
    status = 'current'
    namedValues = NamedValues(("ipv4Unicast", 0), ("ipv4Multicast", 1), ("ipv4UastMcast", 2), ("ipv4MplsLabel", 3), ("ipv4Vpn", 4), ("ipv6Unicast", 5), ("ipv6Multicast", 6), ("ipv6UcastMcast", 7), ("ipv6MplsLabel", 8), ("ipv6Vpn", 9))

class TmnxIgmpGroupFilterMode(TextualConvention, Integer32):
    description = "The data type TmnxIgmpGroupFilterMode describes the filter-mode of a group. In 'include(1)' mode, reception of packets sent to the specified multicast address is requested only from those IPv4 Source addresses listed in the corresponding source-list. In 'exclude(2)' mode, reception of packets sent to the given multicast address is requested from all IPv4 Source addresses, except those listed in the corresponding source-list (if any)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxIgmpGroupType(TextualConvention, Integer32):
    description = 'The data type TmnxIgmpGroupType describes how a multicast group is learned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxIgmpVersion(TextualConvention, Integer32):
    description = "The data type TmnxIgmpVersion denotes the version of the IGMP protocol: - 'version1(1)': means version 1 of the IGMP protocol - 'version2(2)': means version 2 of the IGMP protocol - 'version3(3)': means version 3 of the IGMP protocol."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("version1", 1), ("version2", 2), ("version3", 3))

class TmnxMldGroupFilterMode(TextualConvention, Integer32):
    description = "The data type TmnxMldGroupFilterMode describes the filter-mode of a group. In 'include(1)' mode, reception of packets sent to the specified multicast address is requested only from those IPv6 source addresses listed in the corresponding source-list. In 'exclude(2)' mode, reception of packets sent to the given multicast address is requested from all IPv6 source addresses, except those listed in the corresponding source-list (if any)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxMldGroupType(TextualConvention, Integer32):
    description = 'The data type TmnxMldGroupType describes how a multicast group is learned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxMldVersion(TextualConvention, Integer32):
    description = "The data type TmnxMldVersion denotes the version of the MLD protocol: - 'version1(1)': means version 1 of the MLD protocol - 'version2(2)': means version 2 of the MLD protocol"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("version1", 1), ("version2", 2))

class TmnxManagedRouteStatus(TextualConvention, Integer32):
    description = 'The data type TmnxManagedRouteStatus denotes the status of a Managed Route.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("installed", 0), ("notYetInstalled", 1), ("wrongAntiSpoofType", 2), ("outOfMemory", 3), ("shadowed", 4), ("routeTableFull", 5), ("parentInterfaceDown", 6))

class TmnxAncpString(TextualConvention, OctetString):
    description = 'The TmnxAncpString data type contains a valid ancp string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

class TmnxAncpStringOrZero(TextualConvention, OctetString):
    description = 'The TmnxAncpStringOrZero data type contains a valid ancp string. An empty string indicates that no ANCP string is defined.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 63)

class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    description = 'The data type TmnxMulticastAddrFamily denotes the family for multicast protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipv4Multicast", 0), ("ipv6Multicast", 1))

class TmnxSubIdentString(TextualConvention, OctetString):
    description = 'The data type TmnxSubIdentString denotes the subscriber identification string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSubIdentStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSubIdentStringOrEmpty denotes the subscriber identification string. The empty string denotes the absence of a subscriber identification string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubProfileString(TextualConvention, OctetString):
    description = 'The data type TmnxSubProfileString denotes the subscriber profile string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSubProfileStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSubProfileStringOrEmpty denotes the subscriber profile string. The empty string denotes the absence of a subscriber profile.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSlaProfileString(TextualConvention, OctetString):
    description = 'The data type TmnxSlaProfileString denotes the SLA profile string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSlaProfileStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSlaProfileStringOrEmpty denotes the SLA profile string. The empty string denotes the absence of a SLA profile.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAppProfileString(TextualConvention, OctetString):
    description = 'The data type TmnxAppProfileString denotes the application profile string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxAppProfileStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxAppProfileStringOrEmpty denotes the application profile string. The empty string denotes the absence of a application profile.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSubMgtIntDestIdOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSubMgtIntDestIdOrEmpty denotes the intermediate destination id. The empty string denotes the absence of an intermediate destination id.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtIntDestId(TextualConvention, OctetString):
    description = 'The data type TmnxSubMgtIntDestId denotes the intermediate destination id.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxDhcpOptionType(TextualConvention, Integer32):
    description = "The data type TmnxDhcpOptionType represents how the value of this option is encoded: - 'ipv4 (1)': this option contains an IPv4 address (4 octets) - 'ascii(2)': this option contains seven-bit ASCII characters - 'hex (3)': this option contains octets. It must be displayed in hexadecimal format because it contains non-printable characters."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ascii", 2), ("hex", 3))

class TmnxDhcpVendorOption(TextualConvention, Bits):
    description = 'This value specifies what is encoded in the Alcatel vendor specific sub-option of option 82.'
    status = 'current'
    namedValues = NamedValues(("systemId", 0), ("clientMac", 1), ("serviceId", 2), ("sapId", 3))

class TmnxPppoeUserNameOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxPppoeUserNameOrEmpty denotes the PPPoE username.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class TCpmProtPolicyID(TextualConvention, Unsigned32):
    description = "The data type TCpmProtPolicyID represents the identification number of a CPM Protection policy. The value '0' indicates that no CPM Protection policy is provisioned."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    description = 'This textual-convention uniquely identifies MLPPP Bundle QoS profile in the ingress and egress MLPPP QoS profile tables. The value 0 indicates default MLPPP QoS Profile as applicable to a given H/W'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("ALCATEL-IND1-TIMETRA-TC-MIB", TmnxAncpStringOrZero=TmnxAncpStringOrZero, TmnxBgpRouteTarget=TmnxBgpRouteTarget, TPortSchedulerPIR=TPortSchedulerPIR, TDSCPValueOrNone=TDSCPValueOrNone, TmnxSubMgtIntDestId=TmnxSubMgtIntDestId, TmnxSlaProfileStringOrEmpty=TmnxSlaProfileStringOrEmpty, TItemDescription=TItemDescription, TCIRRate=TCIRRate, timetraTCMIBModule=timetraTCMIBModule, TmnxIgmpGroupFilterMode=TmnxIgmpGroupFilterMode, TmnxSubProfileStringOrEmpty=TmnxSubProfileStringOrEmpty, TmnxDhcpOptionType=TmnxDhcpOptionType, TFCSet=TFCSet, TDSCPFilterActionValue=TDSCPFilterActionValue, TNamedItem=TNamedItem, TmnxStatus=TmnxStatus, ServiceAdminStatus=ServiceAdminStatus, TFCType=TFCType, TmnxBgpPreference=TmnxBgpPreference, TCpmProtPolicyID=TCpmProtPolicyID, TPIRRateOrZero=TPIRRateOrZero, ServiceOperStatus=ServiceOperStatus, TmnxMldGroupFilterMode=TmnxMldGroupFilterMode, TmnxVRtrIDOrZero=TmnxVRtrIDOrZero, TmnxServId=TmnxServId, TmnxVRtrID=TmnxVRtrID, TFCNameOrEmpty=TFCNameOrEmpty, TmnxIgmpVersion=TmnxIgmpVersion, TItemLongDescription=TItemLongDescription, TNamedItemOrEmpty=TNamedItemOrEmpty, TmnxSubProfileString=TmnxSubProfileString, TDSCPValue=TDSCPValue, TIpOption=TIpOption, TPIRRate=TPIRRate, TmnxMldVersion=TmnxMldVersion, TmnxDhcpVendorOption=TmnxDhcpVendorOption, TmnxSubIdentString=TmnxSubIdentString, TDSCPName=TDSCPName, TmnxPortID=TmnxPortID, QTag=QTag, TmnxTunnelType=TmnxTunnelType, TEgressQueueId=TEgressQueueId, TmnxAdminState=TmnxAdminState, TDSCPNameOrEmpty=TDSCPNameOrEmpty, TmnxVPNRouteDistinguisher=TmnxVPNRouteDistinguisher, TLspExpValue=TLspExpValue, TmnxStrSapId=TmnxStrSapId, InterfaceIndex=InterfaceIndex, TmnxSlaProfileString=TmnxSlaProfileString, TmnxBgpAutonomousSystem=TmnxBgpAutonomousSystem, TSapEgressPolicyID=TSapEgressPolicyID, QTagOrZero=QTagOrZero, TQueueId=TQueueId, TmnxActionType=TmnxActionType, TmnxOperState=TmnxOperState, TmnxAppProfileString=TmnxAppProfileString, TmnxCustId=TmnxCustId, TmnxTunnelID=TmnxTunnelID, TmnxAncpString=TmnxAncpString, TSecondaryShaper10GPIRRate=TSecondaryShaper10GPIRRate, TmnxMldGroupType=TmnxMldGroupType, TmnxMulticastAddrFamily=TmnxMulticastAddrFamily, TmnxVRtrMplsLspID=TmnxVRtrMplsLspID, TmnxVcId=TmnxVcId, TmnxEncapVal=TmnxEncapVal, TPolicyID=TPolicyID, TmnxEnabledDisabled=TmnxEnabledDisabled, TFCName=TFCName, TmnxVcType=TmnxVcType, ServiceAccessPoint=ServiceAccessPoint, TmnxVcIdOrNone=TmnxVcIdOrNone, TmnxManagedRouteStatus=TmnxManagedRouteStatus, TPortSchedulerCIR=TPortSchedulerCIR, TmnxSubIdentStringOrEmpty=TmnxSubIdentStringOrEmpty, TmnxOspfInstance=TmnxOspfInstance, TIpProtocol=TIpProtocol, TmnxAppProfileStringOrEmpty=TmnxAppProfileStringOrEmpty, TPolicyStatementNameOrEmpty=TPolicyStatementNameOrEmpty, TTcpUdpPort=TTcpUdpPort, TmnxSubMgtIntDestIdOrEmpty=TmnxSubMgtIntDestIdOrEmpty, TFrameType=TFrameType, Dot1PPriority=Dot1PPriority, TMlpppQoSProfileId=TMlpppQoSProfileId, TmnxIgmpGroupType=TmnxIgmpGroupType, TSapIngressPolicyID=TSapIngressPolicyID, TPIRRateOverride=TPIRRateOverride, TmnxBGPFamilyType=TmnxBGPFamilyType, SdpBindId=SdpBindId, TmnxPppoeUserNameOrEmpty=TmnxPppoeUserNameOrEmpty, TTcpUdpPortOperator=TTcpUdpPortOperator, TmnxDHCP6MsgType=TmnxDHCP6MsgType, PYSNMP_MODULE_ID=timetraTCMIBModule, TWeight=TWeight, TmnxBgpLocalPreference=TmnxBgpLocalPreference, TIngressQueueId=TIngressQueueId, IpAddressPrefixLength=IpAddressPrefixLength)
