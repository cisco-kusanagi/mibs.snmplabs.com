#
# PySNMP MIB module TIMETRA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, NotificationType, Integer32, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "NotificationType", "Integer32", "iso", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
timetraModules, = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraModules")
timetraTCMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 2))
timetraTCMIBModule.setRevisions(('1911-02-01 00:00', '1909-02-28 00:00', '1908-07-01 00:00', '1908-01-01 00:00', '1907-01-01 00:00', '1906-03-23 00:00', '1905-08-31 00:00', '1905-01-24 00:00', '1904-01-15 00:00', '1903-08-15 00:00', '1903-01-20 00:00', '1901-05-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraTCMIBModule.setRevisionsDescriptions(('Rev 9.0 1 Feb 2011 00:00 9.0 release of the TIMETRA-TC-MIB.', 'Rev 7.0 28 Feb 2009 00:00 7.0 release of the TIMETRA-TC-MIB.', 'Rev 6.1 01 Jul 2008 00:00 6.1 release of the TIMETRA-TC-MIB.', 'Rev 6.0 01 Jan 2008 00:00 6.0 release of the TIMETRA-TC-MIB.', 'Rev 5.0 01 Jan 2007 00:00 5.0 release of the TIMETRA-TC-MIB.', 'Rev 4.0 23 Mar 2006 00:00 4.0 release of the TIMETRA-TC-MIB.', 'Rev 3.0 31 Aug 2005 00:00 3.0 release of the TIMETRA-TC-MIB.', 'Rev 2.1 24 Jan 2005 00:00 2.1 release of the TIMETRA-TC-MIB.', 'Rev 2.0 15 Jan 2004 00:00 2.0 release of the TIMETRA-TC-MIB.', 'Rev 1.2 15 Aug 2003 00:00 1.2 release of the TIMETRA-TC-MIB.', 'Rev 1.0 20 Jan 2003 00:00 1.0 Release of the TIMETRA-TC-MIB.', 'Rev 0.1 14 Aug 2000 00:00 First version of the TIMETRA-TC-MIB.',))
if mibBuilder.loadTexts: timetraTCMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraTCMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timetraTCMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com')
if mibBuilder.loadTexts: timetraTCMIBModule.setDescription("This document is the SNMP MIB module for the SNMP Textual Conventions (TCs) used in the Alcatel-Lucent SROS manageability instrumentation. Copyright 2003-2014 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied `as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub- layer must remain constant at least from one re- initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'

class TmnxPortID(TextualConvention, Unsigned32):
    description = "A portid is an unique 32 bit number encoded as shown below. 32 30 | 29 26 | 25 22 | 21 16 | 15 1 | +-----+-------+-------+-------+-------+ |000 | slot | mda | port | zero | Physical Port +-----+-------+-------+-------+-------+ 32 30 | 29 26 | 25 22 | 21 16 | 15 1 | +-----+-------+-------+-------+-------+ |001 | slot | mda | port |channel| Channel +-----+-------+-------+-------+-------+ Slots, mdas (if present), ports, and channels are numbered starting with 1. 32 29 | 28 10 | 9 1 | +---------+-------------------+-------+ | 0 1 0 0 | zeros | ID | Virtual Port +---------+-------------------+-------+ 32 29 | 28 9 | 8 1 | +---------+---------------------+-----+ | 0 1 0 1 | zeros | ID | LAG Port +---------+---------------------+-----+ A card port number (cpn) has significance within the context of the card on which it resides(ie., cpn 2 may exist in one or more cards in the chassis). Whereas, portid is an unique/absolute port number (apn) within a given chassis. An 'invalid portid' is a TmnxPortID with a value of 0x1e000000 as represented below. 32 30 | 29 26 | 25 22 | 21 16 | 15 1 | +-----+-------+-------+-------+-------+ |zero | ones | zero | zero | zero | Invalid Port +-----+-------+-------+-------+-------+"
    status = 'current'

class TmnxEncapVal(TextualConvention, Unsigned32):
    description = 'The value of the label used to identify the entity using the specified encapsulation value on a specific port. The format of this object depends on the encapsulation type defined on this port. When the encapsulation is nullEncap the value of this object must be zero. 31 0 +--------+--------+--------+--------+ |00000000 00000000 00000000 00000000| +--------+--------+--------+--------+ When the encapsulation is dot1qEncap the value of this object is equal to the 12-bit IEEE 802.1Q VLAN ID. 31 0 +--------+--------+--------+--------+ |00000000 00000000 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is mplsEncap the value of this object is equal to the 20-bit LSP ID. 31 0 +--------+--------+--------+--------+ |00000000 0000XXXX XXXXXXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is frEncap, the value of this object is equal to the 10-bit Frame Relay DLCI. 31 0 +--------+--------+--------+--------+ |00000000 00000000 000000XX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is qinqEncap, the value of the outer 802.1Q VLAN ID is encoded in the least significant 16 bits, and the value of the inner VLAN ID is encoded in the most significant 16 bits. 31 0 +--------+--------+--------+--------+ |0000YYYY YYYYYYYY 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is atmEncap, the value of the ATM VCI is encoded in the least significant 16 bits, and the value of the ATM VPI is encoded in the next 12 bits. For ATM VCs, the top 3 bits are 000. The value of the ATM VCI is encoded in the least significant 16 bits, and the value of the ATM VPI is encoded in the next 12 bits. 31 0 +--------+--------+--------+--------+ |0000YYYY YYYYYYYY XXXXXXXX XXXXXXXX| +--------+--------+--------+--------+ For ATM capture VCs, bits 0 and 28 are 1. 31 0 +--------+--------+--------+--------+ |00010000 00000000 00000000 00000001| +--------+--------+--------+--------+ For ATM VPs, the top 3 bits are 010. The value of the ATM VPI is encoded in the least significant 12 bits. 31 0 +--------+--------+--------+--------+ |01000000 00000000 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ For ATM VP ranges, the top 3 bits are 100. The value of the start of the ATM VPI range is encoded in the least significant 12 bits, and the value of the end of the ATM VP range is encoded in the next 12 bits. 31 0 +--------+--------+--------+--------+ |10000000 YYYYYYYY YYYYXXXX XXXXXXXX| +--------+--------+--------+--------+ For ATM ports, the top 3 bits are 110, and the rest of the bits must be zero. 31 0 +--------+--------+--------+--------+ |11000000 00000000 00000000 00000000| +--------+--------+--------+--------+ For ATM CPs, the top 3 bits are 001. The value of the ATM CP is encoded in the least significant 13 bits. 31 0 +--------+--------+--------+--------+ |00100000 00000000 000XXXXX XXXXXXXX| +--------+--------+--------+--------+ When the encapsulation is wanMirrorEncap the value of this object is equal to the 12-bit value. 31 0 +--------+--------+--------+--------+ |00000000 00000000 0000XXXX XXXXXXXX| +--------+--------+--------+--------+ Some ports have a restrictions to the encapsulation types that they can support and hence impose restrictions on the respective formats defined above.'
    status = 'current'

class QTag(TextualConvention, Integer32):
    description = 'The QTag data type is a 12-bit integer tag used to identify a service. The values 0 and 4095 are not allowed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class QTagOrZero(TextualConvention, Unsigned32):
    description = "The data type QTagOrZero represents a VLAN tag. The value '0' indicates that no VLAN tag is provisioned, or that its value is unknown."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class QTagFullRange(TextualConvention, Unsigned32):
    description = 'The data type QTagFullRange represents a VLAN tag. A VLAN tag is 12 bits is size. The data type QTagFullRange covers the whole range of possible values. (0..4095 or 0x0 .. 0xFFF)'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

class QTagFullRangeOrNone(TextualConvention, Integer32):
    description = "The data type QTagFullRangeOrNone represents a VLAN tag. A VLAN tag is 12 bits is size. The data type QTagFullRange covers the whole range of possible values. (0..4095 or 0x0 .. 0xFFF). The value '-1' indicates the absense of a VLAN tag."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4095), )
class TmnxStrSapId(DisplayString):
    description = 'The value of TmnxStrSapId is a printable string which contains the owner SAP Id or equivalent on a remote system. The string should contain the printable string equivalent of the textual-conventions TmnxPortID and TmnxEncapVal in the format specified as TmnxPortID[:TmnxEncapVal]'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

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

class TmnxEnabledDisabledOrInherit(TextualConvention, Integer32):
    description = "The TmnxEnabledDisabledOrInherit data type is an enumerated integer that describes the values used to identify whether an entity is 'enabled', 'disabled' or inherits its state from another object that is usually in another mib table."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("inherit", 3))

class TNamedItem(DisplayString):
    description = 'The name of an item. When used as an index to a table, the item name uniquely identifies the instance. When used in a reference (TNamedItemOrEmpty) the item name entry must exist in the table. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TNamedItemOrEmpty(DisplayString):
    description = 'The name of an item, or an empty string. When used in a reference (TNamedItemOrEmpty) the item name entry must exist in the table. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TLNamedItem(DisplayString):
    description = 'The long name of an item. When used as an index to a table, the item name uniquely identifies the instance. When used in a reference (TLNamedItemOrEmpty) the item name entry must exist in the table. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TLNamedItemOrEmpty(DisplayString):
    description = 'The long name of an item, or an empty string. When used in a reference (TLNamedItemOrEmpty) the item name entry must exist in the table. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), )
class TItemDescription(DisplayString):
    description = 'Description for an item. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TItemLongDescription(DisplayString):
    description = 'Longer description for an item. Note, use only NVT ASCII displayable characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 160)

class TmnxVRtrID(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10240)

class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system. The number 0 will have special significance in the context the TC is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10240)

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
class BgpPeeringStatus(TextualConvention, Integer32):
    description = 'The status of the BGP peering session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("notApplicable", 0), ("installed", 1), ("notInstalled", 2), ("noEnhancedSubmgt", 3), ("wrongAntiSpoof", 4), ("parentItfDown", 5), ("hostInactive", 6), ("noDualHomingSupport", 7), ("invalidRadiusAttr", 8), ("noDynamicPeerGroup", 9), ("duplicatePeer", 10), ("maxPeersReached", 11), ("genError", 12))

class TmnxServId(TextualConvention, Unsigned32):
    description = 'A number used to identify a Service. This ID must be unique within the Service Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ValueRangeConstraint(2147483648, 2147483648), ValueRangeConstraint(2147483649, 2147483649), ValueRangeConstraint(2147483650, 2147483650), )
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
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), )
class TTmplPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a policy for template objects.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TSapIngressPolicyID(TPolicyID):
    description = 'The identification number of a SAP ingress policy.'
    status = 'current'

class TSapEgressPolicyID(TPolicyID):
    description = 'The identification number of a SAP egress policy.'
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), )
class TSdpIngressPolicyID(TPolicyID):
    description = 'The identification number of a SDP ingress network policy.'
    status = 'current'

class TSdpEgressPolicyID(TPolicyID):
    description = 'The identification number of a SDP egress network policy.'
    status = 'current'

class TQosQGrpInstanceIDorZero(TextualConvention, Unsigned32):
    description = "The identifcation number of a QoS queue group instance. The value of '0' indicates the system determined default value."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxTransitIpPolicyId(TextualConvention, Unsigned32):
    description = 'TmnxBsxTransitIpPolicyId identifies a transit IP policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxTransitIpPolicyIdOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxTransitIpPolicyId identifies a transit ip policy. The value '0' indicates an invalid transit IP policy."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxTransPrefPolicyId(TextualConvention, Unsigned32):
    description = 'TmnxBsxTransPrefPolicyId identifies a transit prefix policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxTransPrefPolicyIdOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxTransPrefPolicyId identifies a transit prefix policy. The value '0' indicates an invalid transit prefix policy."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxAarpId(TextualConvention, Unsigned32):
    description = 'TmnxBsxAarpId identifies an instance of the AA Redundancy Protocol (AARP).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxAarpIdOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxAarpIdOrZero identifies an instance of the AA Redundancy Protocol (AARP). The value of '0' indicates an invalid AARP instance."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxAarpServiceRefType(TextualConvention, Integer32):
    description = "TmnxBsxAarpServiceRefType identifies the role of the SAP or Spoke SDP service point being referenced by an AARP instance. This reference is made in the context of a AARP instance identified by TmnxBsxAarpIdOrZero. The service reference types are: none(0) - service reference type is not applicable. dualHomed(1) - the service reference point is a SAP or Spoke SDP connected into a dually homed network being protected by the AARP instance. shuntSubscriberSide(2) - the service reference point is a Spoke SDP acting as a subscriber side shunt used by the AARP instance. A subscriber side shunt carries the local from/to subscriber traffic when AA is performed remotely. shuntNetworkSide(3) - the service reference point is a Spoke SDP acting as a network side shunt used by the AARP instance. A network side shunt carries the local from/to network traffic when AA is performed remotely. For the case when TmnxBsxAarpIdOrZero refers to the invalid AARP instance '0', the service reference type is 'none(0)'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("dualHomed", 1), ("shuntSubscriberSide", 2), ("shuntNetworkSide", 3))

class TSapEgrEncapGrpQosPolicyIdOrZero(TextualConvention, Unsigned32):
    description = "TSapEgrEncapGrpQosPolicyIdOrZero identifies SAP egress Encapsulation group QoS policy. The value '0' indicates no QoS policy is set."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TSapEgrEncapGroupType(TextualConvention, Integer32):
    description = 'TSapEgrEncapGroupType identifies Encapsulation group type on SAP egress.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("isid", 1))

class TSapEgrEncapGroupActionType(TextualConvention, Integer32):
    description = 'TSapEgrEncapGroupActionType identifies Encapsulation group action type on SAP egress. It is used to create or destroy row entries in an associated table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("destroy", 2))

class TPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class TPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override of the adjustment to make to the size of each packet for accounting. A value of -128 indicates no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TIngressHsmdaPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each incoming packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class TEgressQPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-64, 32)

class TIngHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override of the adjustment to make to the size of each incoming packet for accounting. A value of -128 indicates no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TEgressHsmdaPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each outgoing packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class THsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    description = 'The identifcation number of a HSMDA counter. The value 0 indicates an undefined counter id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class THsmdaCounterIdOrZeroOrAll(TextualConvention, Integer32):
    description = 'The identifcation number of a HSMDA counter. The value (0) indicates an undefined counter id. The value (-1) is used to indicate all counters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgrHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override of the adjustment to make to the size of each outgoing packet for accounting. A value of -128 indicates no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TIngressHsmdaCounterId(TextualConvention, Unsigned32):
    description = 'The identifcation number of a HSMDA ingress counter.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TIngressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    description = 'The identifcation number of a HSMDA ingress counter. The value 0 indicates an undefined counter id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressHsmdaCounterId(TextualConvention, Unsigned32):
    description = 'The identifcation number of a HSMDA egress counter.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TEgressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    description = 'The identifcation number of a HSMDA egress counter. The value 0 indicates an undefined counter id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgrRateModType(TextualConvention, Integer32):
    description = 'The data type TEgrRateModType represents the type of egress-rate modification that is to be applied.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("aggRateLimit", 2), ("namedScheduler", 3))

class TPolicyStatementNameOrEmpty(TNamedItemOrEmpty):
    description = 'The name of a policy statement, when an object refers to it.'
    status = 'current'

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
class Dot1PPriorityMask(TextualConvention, Integer32):
    reference = ''
    description = 'IEEE 802.1p priority mask. zero is lowest, seven is highest.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

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
class TOperator(TextualConvention, Integer32):
    description = "The operator specifies the manner in which a couple of other MIB objects in the table are supposed to be used. Operator Value1 Value2 ---------------------------------------------------- none(0) Any(0) Any(0) eq(1) Specified Value Any(0) range(2) Starting Value Ending Value lt(3) Specified Value Any(0) gt(4) Specified Value Any(0) 'Any(0)' specifies that, this object can accept any values but would default to 0. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("eq", 1), ("range", 2), ("lt", 3), ("gt", 4))

class TTcpUdpPortOperator(TOperator):
    description = 'The operator used for checking on TCP/UDP ports values and ranges'
    status = 'current'

class TFrameType(TextualConvention, Integer32):
    description = 'The type of the frame for which this mac filter match criteria is defined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5))
    namedValues = NamedValues(("e802dot3", 0), ("e802dot2LLC", 1), ("e802dot2SNAP", 2), ("ethernetII", 3), ("atm", 5))

class TQueueId(TextualConvention, Integer32):
    description = 'The value of TQueueId specifies the identification number of a queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TQueueIdOrAll(TextualConvention, Integer32):
    description = "The value of TQueueIdOrAll specifies the identification number of a queue A value of zero (0) indicates that no specific queue identification has been assigned for this object. A value of (-1) indicates 'all queues'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressQueueId(TextualConvention, Integer32):
    description = 'The value of TIngressQueueId specifies the identification number of an ingress queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TIngressQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressMeterId(TextualConvention, Integer32):
    description = 'Ingress Meter Id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TSapIngressMeterId(TextualConvention, Integer32):
    description = 'Ingress Meter Id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TNetworkIngressMeterId(TextualConvention, Integer32):
    description = 'Ingress Meter Id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 16), )
class TEgressQueueId(TextualConvention, Integer32):
    description = 'The value of TEgressQueueId specifies the identification number of an egress queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TEgressQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TIngressHsmdaQueueId(TextualConvention, Integer32):
    description = 'The value of TIngressHsmdaQueueId specifies the identification number of a HSMDA ingress queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TIngressHsmdaQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressHsmdaQueueId(TextualConvention, Integer32):
    description = 'The value of TEgressHsmdaQueueId specifies the identification number of a HSMDA egress queue. A value of zero (0) indicates that no specific queue identification has been assigned for this object. When an object of type TEgressHsmdaQueueId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class THsmdaSchedulerPolicyGroupId(TextualConvention, Integer32):
    description = 'The value of THsmdaSchedulerPolicyGroupId specifies the identification number of a HSMDA scheduler policy group. A value of zero (0) indicates that no specific group identification has been assigned for this object. When an object of type THsmdaSchedulerPolicyGroupId is an SNMP table index, an index value of zero (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2), )
class THsmdaPolicyIncludeQueues(TextualConvention, Integer32):
    description = 'The value of THsmdaPolicyIncludeQueues specifies which queues are to be scheduled in the same class in a HSMDA scheduler.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("q1to2", 1), ("q1to3", 2))

class THsmdaPolicyScheduleClass(TextualConvention, Integer32):
    description = 'The value of THsmdaPolicyScheduleClass the class at which the queues specified by THsmdaPolicyIncludeQueues in a HSMDA scheduler.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

class TDSCPName(TNamedItem):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'

class TDSCPNameOrEmpty(TNamedItemOrEmpty):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'

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
class TFCName(TNamedItem):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'

class TFCNameOrEmpty(TNamedItemOrEmpty):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'

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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("sdp", 1), ("ldp", 2), ("rsvp", 3), ("gre", 4), ("bypass", 5), ("invalid", 6), ("bgp", 7))

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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TPortSchedulerPIRRate(TextualConvention, Integer32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 400000000), )
class TPortSchedulerCIR(TextualConvention, Integer32):
    description = 'The Committed Information Rate (CIR) rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 400000000), )
class TWeight(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TNonZeroWeight(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class TPolicerWeight(TextualConvention, Integer32):
    description = 'The relative weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class THsmdaWeight(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class THsmdaWrrWeight(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class THsmdaWeightClass(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))
    namedValues = NamedValues(("class1", 1), ("class2", 2), ("class4", 4), ("class8", 8))

class THsmdaWeightOverride(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the parent. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 100), )
class THsmdaWrrWeightOverride(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the parent. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 32), )
class TCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THPolCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 20000000), )
class TRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR rate. The value 'kbps' means the rate is specified in kbps. The value 'percent' means the rate is specified in percentage"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("kbps", 1), ("percent", 2))

class TBWRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR percent rate. The value 'kbps' means the rate is specified in kbps. The value 'percentPortLimit' means the rate is specified in percentage of port limit. The value 'percentLocalLimit' means the rate is specified in percentage of local limit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("kbps", 1), ("percentPortLimit", 2), ("percentLocalLimit", 3))

class TPolicerRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR percent rate. The value 'kbps' means the rate is specified in kbps. The value 'percentLocalLimit' means the rate is specified in percentage of local limit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("kbps", 1), ("percentLocalLimit", 2))

class TCIRRateOverride(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THPolCIRRateOverride(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 20000000), )
class TCIRPercentOverride(TextualConvention, Integer32):
    description = 'The CIR percentage rate specified in hundredths of a percent. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(0, 10000), )
class THsmdaCIRKRate(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaCIRKRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaCIRMRate(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Mbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000), )
class THsmdaCIRMRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Mbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000), )
class TPIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THPolVirtualSchePIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 800000000), )
class THPolVirtualScheCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 800000000), )
class TAdvCfgRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class TMaxDecRate(TextualConvention, Integer32):
    description = 'The Advanced Configuration policy Max-Decrement rate to be used in kbps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 100000000), )
class THPolPIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 20000000), )
class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    description = 'The secondary shaper PIR rate to be used in Mbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000), )
class TExpSecondaryShaperPIRRate(TextualConvention, Integer32):
    description = 'The expanded secondary shaper PIR rate to be used in Kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000000), )
class TExpSecondaryShaperClassRate(TextualConvention, Integer32):
    description = 'The expanded secondary shaper class PIR rate to be used in Kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000000), )
class TPIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THPolPIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 20000000), )
class TPIRPercentOverride(TextualConvention, Integer32):
    description = 'The PIR percentage rate specified in hundredths of a percent. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 10000), )
class TPIRRateOrZero(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. The value 0 means undefined rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaPIRKRate(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THsmdaPIRKRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Kbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THsmdaPIRMRate(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Mbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000), )
class THsmdaPIRMRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Mbps. The value -1 means maximum rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000), )
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
    namedValues = NamedValues(("ipv4Unicast", 0), ("ipv4Multicast", 1), ("ipv4UastMcast", 2), ("ipv4MplsLabel", 3), ("ipv4Vpn", 4), ("ipv6Unicast", 5), ("ipv6Multicast", 6), ("ipv6UcastMcast", 7), ("ipv6MplsLabel", 8), ("ipv6Vpn", 9), ("l2Vpn", 10), ("ipv4Mvpn", 11), ("msPw", 12), ("ipv4Flow", 13), ("mdtSafi", 14), ("routeTarget", 15), ("mcastVpnIpv4", 16))

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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("installed", 0), ("notYetInstalled", 1), ("wrongAntiSpoofType", 2), ("outOfMemory", 3), ("shadowed", 4), ("routeTableFull", 5), ("parentInterfaceDown", 6), ("hostInactive", 7), ("enhancedSubMgmtRequired", 8), ("deprecated1", 9), ("l2AwNotSupported", 10))

class TmnxAncpString(DisplayString):
    description = 'The TmnxAncpString data type contains a valid ancp string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 63)

class TmnxAncpStringOrZero(DisplayString):
    description = 'The TmnxAncpStringOrZero data type contains a valid ancp string. An empty string indicates that no ANCP string is defined.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 63)

class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    description = 'The data type TmnxMulticastAddrFamily denotes the family for multicast protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipv4Multicast", 0), ("ipv6Multicast", 1))

class TmnxAsciiSpecification(DisplayString):
    description = "The data type TmnxAsciiSpecification is a format string that specifies how to form a target ASCII string. The format is as follows: <ascii-specification> ::= <char-specification>+ <char-specification> ::= <ascii-char> | <char-origin> <char-origin> ::= '%' <origin> <ascii-char> refers to a printable ASCII character. Examples and supported char-origin specifiers are supplied with the object definitions."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class TmnxMacSpecification(DisplayString):
    description = "The data type TmnxMacSpecification is a string of ASCII characters that specifies how to format a string that represents a MAC address. The format is as follows: <mac-specification> ::= <alpha-string> [<delimiter-char>] <alpha-string> ::= <ucase-alpha>+ | <lcase-alpha>+ <ucase-alpha> ::= 'A' | 'B' | 'B' ... | 'Z' <lcase-alpha> ::= 'a' | 'b' | 'c' ... | 'z' <delimiter-char> any ASCII character that is not an <alpha-char> or a decimal digit Only the number of alphabetic characters and the case is relevant. Examples: 'ab:' 00:0c:f1:99:85:b8 Alcatel-Lucent SROS style 'XY-' 00-0C-F1-99-85-B8 IEEE canonical style 'mmmm.' 0002.03aa.abff Cisco style. 'xx' 000cf19985b8"
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 17)

class TmnxBinarySpecification(DisplayString):
    description = "The data type TmnxBinarySpecification is a string of ASCII characters that specifies how to form a binary number. The format is as follows: <binary-specification> ::= <bit-specification>+ <bit-specification> ::= '0' | '1' | <bit-origin> <bit-origin> ::= '*' <number-of-bits> <origin> <number-of-bits> ::= [1..32] Examples and supported bit-origin specifiers are supplied with the object definitions."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class TmnxDefSubIdSource(TextualConvention, Integer32):
    description = "The data type TmnxDefSubIdSource specifies what will be used as the default subscriber identification. This value is used in case no other source (like RADIUS) provides a subscriber identification string. If the value of this object is set to 'useSapId', the SAP-id will be used as the default subscriber identification string. If the value of this object is set to 'useAutoId', the auto-generated subscriber identification string, as defined in tmnxSubMgmtAutoSubIdObjs, is used as the default subscriber identification string. If the value of this object is set to 'useString', the value of the string contained in another object will be used as the default subscriber identification string; that object must be identified where this datatype is used."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("useSapId", 1), ("useString", 2), ("useAutoId", 3))

class TmnxSubIdentString(DisplayString):
    description = 'The data type TmnxSubIdentString denotes the subscriber identification string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSubIdentStringOrEmpty(DisplayString):
    description = 'The data type TmnxSubIdentStringOrEmpty denotes the subscriber identification string. The empty string denotes the absence of a subscriber identification string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubRadServAlgorithm(TextualConvention, Integer32):
    description = 'The TmnxSubRadServAlgorithm data type is an enumerated integer that indicates the algorithm used to access the list of configured RADIUS servers: - direct (1): The first server will be used as primary server for all requests, the second as secondary and so on. - roundRobin (2): The first server will be used as primary server for the first request, the second server as primary for the second request, and so on. If the router gets to the end of the list, it starts again with the first server. - hashBased (3): The server will be selected based on a specified hash value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("direct", 1), ("roundRobin", 2), ("hashBased", 3))

class TmnxSubRadiusAttrType(TextualConvention, Unsigned32):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS) section 5. Attributes'
    description = 'The TmnxSubRadiusAttrType data type contains a number that indicates a RADIUS attribute type.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxSubRadiusVendorId(TextualConvention, Unsigned32):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS) section 5.26. Vendor-Specific.'
    description = 'The TmnxSubRadiusVendorId data type contains a number that indicates a RADIUS Vendor-Id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class TmnxRadiusPendingReqLimit(TextualConvention, Unsigned32):
    description = 'The TmnxRadiusPendingReqLimit data type is a number that specifies the limit to the number of pending RADIUS request messages.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4096)

class TmnxRadiusServerOperState(TextualConvention, Integer32):
    description = 'The TmnxRadiusServerOperState data type is an enumerated integer that describes the values used to identify the operational state of a RADIUS server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4), ("overloaded", 5))

class TmnxSubProfileString(DisplayString):
    description = 'The data type TmnxSubProfileString denotes the subscriber profile string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSubProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxSubProfileStringOrEmpty denotes the subscriber profile string. The empty string denotes the absence of a subscriber profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSlaProfileString(DisplayString):
    description = 'The data type TmnxSlaProfileString denotes the SLA profile string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSlaProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxSlaProfileStringOrEmpty denotes the SLA profile string. The empty string denotes the absence of a SLA profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAppProfileString(DisplayString):
    description = 'The data type TmnxAppProfileString denotes the application profile string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxAppProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxAppProfileStringOrEmpty denotes the application profile string. The empty string denotes the absence of a application profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSubMgtIntDestIdOrEmpty(DisplayString):
    description = 'The data type TmnxSubMgtIntDestIdOrEmpty denotes the intermediate destination id. The empty string denotes the absence of an intermediate destination id.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtIntDestId(TmnxSubMgtIntDestIdOrEmpty):
    description = 'The data type TmnxSubMgtIntDestId denotes the intermediate destination id.'
    status = 'current'
    subtypeSpec = TmnxSubMgtIntDestIdOrEmpty.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxDefInterDestIdSource(TextualConvention, Integer32):
    description = "The data type TmnxDefInterDestIdSource specifies what will be used as the default intermediate destination identifier. This value is used in case no other source (like RADIUS) provides an intermediate destination identifier. If the value of this object is set to 'useString', the value of the string contained in another object will be used as the default intermediate destination identifier; that object must be identified where this datatype is used. If the value of this object is set to 'useTopQTag', the top q-tag of the ingress SAP will be used as the default subscriber intermediate destination identifier. If the value of this object is set to 'useVpi', the ATM VPI of the ingress SAP will be used as the default subscriber intermediate destination identifier."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("useString", 1), ("useTopQTag", 2), ("useVpi", 3))

class TmnxSubNasPortSuffixType(TextualConvention, Integer32):
    description = 'The TmnxSubNasPortSuffixType data type is an enumerated integer that specifies what suffix will be added to the RADIUS NAS-Port attribute: - none (0): No suffix will be added. - circuitId (1): If available, the circuit-id will be added. - remoteId (2): If available, the remote-id will be added.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("circuitId", 1), ("remoteId", 2))

class TmnxSubNasPortPrefixType(TextualConvention, Integer32):
    description = 'The TmnxSubNasPortPrefixType data type is an enumerated integer that specifies what prefix will be added to the RADIUS NAS-Port attribute: - none (0): No prefix will be added. - userString (1): A user configurable string will be added.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("userString", 1))

class TmnxSubNasPortTypeType(TextualConvention, Integer32):
    description = 'The TmnxSubNasPortTypeType data type is an enumerated integer that specifies what value will be put in the RADIUS NAS-Port-Type attribute: - standard (1): according to the RADIUS specification RFC 2865 section 5.41 NAS-Port-Type; - config (2): a configured value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("standard", 1), ("config", 2))

class TmnxSubMgtOrgStrOrZero(DisplayString):
    description = 'The data type TmnxSubMgtOrgStrOrZero denotes the organization string. The empty string denotes the absence of an organization string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtOrgString(TmnxSubMgtOrgStrOrZero):
    description = 'The data type TmnxSubMgtOrgStrOrZero denotes the organization string.'
    status = 'current'
    subtypeSpec = TmnxSubMgtOrgStrOrZero.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxFilterProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxFilterProfileStringOrEmpty denotes the filter profile string. The empty string denotes the absence of a filter profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAccessLoopEncapDataLink(TextualConvention, Integer32):
    description = 'The data type TmnxAccessLoopEncapDataLink specifies the data link used by the subscriber on the DSL access loop.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("aal5", 0), ("ethernet", 1))

class TmnxAccessLoopEncaps1(TextualConvention, Integer32):
    description = 'The data type TmnxAccessLoopEncaps1 specifies the encapsulation used by the subscriber on the DSL access loop.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notAvailable", 0), ("untaggedEthernet", 1), ("singleTaggedEthernet", 2))

class TmnxAccessLoopEncaps2(TextualConvention, Integer32):
    description = 'The data type TmnxAccessLoopEncaps2 specifies the encapsulation used by the subscriber on the DSL access loop.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notAvailable", 0), ("pppoaLlc", 1), ("pppoaNull", 2), ("ipoaLlc", 3), ("ipoaNull", 4), ("ethernetOverAal5LlcFcs", 5), ("ethernetOverAal5LlcNoFcs", 6), ("ethernetOverAal5NullFcs", 7), ("ethernetOverAal5NullNoFcs", 8))

class TmnxSubAleOffsetMode(TextualConvention, Integer32):
    description = "The data type TmnxSubAleOffsetMode specifies the way the encapsulation offset of the subscriber in the DSL access loop is learned by the 7xxx system. This offset is used in 7xxx egress shaping, adjusting the subscriber aggregate rate to account for the fixed encapsulation offset and per packet variable expansion of the last mile for the specific session used by the subscriber host. The value 'none' disables the adjustment. While the value is 'auto', the encapsulation offset will be learned for example from the encapsulation type value signaled in the Access-loop-encapsulation sub-TLV in the Vendor-Specific PPPoE Tags or DHCP Relay Options [rfc4679]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("auto", 1))

class TmnxSubAleOffset(TextualConvention, Integer32):
    description = 'The data type TmnxSubAleOffset specifies the encapsulation offset value of the subscriber in the DSL access loop as used by the 7xxx system. This offset is used in 7xxx egress shaping in order to accurately shape the end user payload.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("none", 0), ("pppoaLlc", 1), ("pppoaNull", 2), ("pppoeoaLlc", 3), ("pppoeoaLlcFcs", 4), ("pppoeoaLlcTagged", 5), ("pppoeoaLlcTaggedFcs", 6), ("pppoeoaNull", 7), ("pppoeoaNullFcs", 8), ("pppoeoaNullTagged", 9), ("pppoeoaNullTaggedFcs", 10), ("ipoaLlc", 11), ("ipoaNull", 12), ("ipoeoaLlc", 13), ("ipoeoaLlcFcs", 14), ("ipoeoaLlcTagged", 15), ("ipoeoaLlcTaggedFcs", 16), ("ipoeoaNull", 17), ("ipoeoaNullFcs", 18), ("ipoeoaNullTagged", 19), ("ipoeoaNullTaggedFcs", 20), ("pppoe", 21), ("pppoeTagged", 22), ("ipoe", 23), ("ipoeTagged", 24))

class TmnxDhcpOptionType(TextualConvention, Integer32):
    description = "The data type TmnxDhcpOptionType represents how the value of this option is encoded: - 'ipv4 (1)' : this option contains an IPv4 address (4 octets) - 'ascii(2)' : this option contains seven-bit ASCII characters - 'hex (3)' : this option contains octets. It must be displayed in hexadecimal format because it contains non-printable characters. - 'ipv6 (4)' : this option contains an IPv6 address (16 octets) - 'domain (5)': this option contains a domain name that will be encoded as specified by RFC 1035 section 3.1."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ascii", 2), ("hex", 3), ("ipv6", 4), ("domain", 5))

class TmnxPppoeUserName(DisplayString):
    description = 'The data type TmnxPppoeUserName denotes the PPPoE username.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 128)

class TmnxPppoeUserNameOrEmpty(DisplayString):
    description = 'The data type TmnxPppoeUserNameOrEmpty denotes the PPPoE username.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 128)

class TCpmProtPolicyID(TextualConvention, Unsigned32):
    description = "The data type TCpmProtPolicyID represents the identification number of a CPM Protection policy. The value '0' indicates that no CPM Protection policy is provisioned."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TCpmProtPolicyIDOrDefault(TextualConvention, Integer32):
    description = "The data type TCpmProtPolicyIDOrDefault represents the identification number of a CPM Protection policy. The value of '-1' indicates the system determined default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 255), )
class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    description = 'This textual-convention uniquely identifies MLPPP Bundle QoS profile in the ingress and egress MLPPP QoS profile tables. The value 0 indicates default MLPPP QoS Profile as applicable to a given H/W'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TMcFrQoSProfileId(TextualConvention, Unsigned32):
    description = 'This textual-convention uniquely identifies Multi-class Frame-relay QoS profiles in the ingress and egress multi-class frame-relay QoS profile tables. The value 0 indicates a default QoS Profile as applicable to a given hardware.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxPppoeSessionId(TextualConvention, Unsigned32):
    description = 'The TmnxPppoeSessionId indicates the 16 bit wide PPPoE session Id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxPppoePadoDelay(TextualConvention, Unsigned32):
    description = 'The data type TmnxPppoePadoDelay specifies the delay timeout in deci-seconds before sending a PADO (PPPoE Active Discovery Offer).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 30), )
class TmnxPppoeSessionInfoOrigin(TextualConvention, Integer32):
    description = 'The TmnxPppoeSessionInfoOrigin indicates the originator of the provided information.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 0), ("default", 1), ("radius", 2), ("localUserDb", 3), ("dhcp", 4), ("midSessionChange", 5), ("tags", 6), ("l2tp", 7))

class TmnxPppoeSessionType(TextualConvention, Integer32):
    description = 'The TmnxPppoeSessionType indicates the type of PPPoE session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("local", 1), ("localWholesale", 2), ("localRetail", 3), ("l2tp", 4))

class TmnxPppNcpProtocol(TextualConvention, Integer32):
    description = 'The TmnxPppNcpProtocol data type represents the PPP Network Control Protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipcp", 1), ("ipv6cp", 2))

class TmnxMlpppEpClass(TextualConvention, Integer32):
    description = 'The TmnxMlpppEpClass type represents the address class of the MLPPP Endpoint Discriminator option.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("null", 0), ("local", 1), ("ipv4Address", 2), ("macAddress", 3), ("magicNumber", 4), ("directoryNumber", 5))

class TNetworkPolicyID(TPolicyID):
    description = 'the identification number of a network policy.'
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), )
class TItemScope(TextualConvention, Integer32):
    description = "This textual-convention determines some aspects of an item's behavior regarding creation and use, unused entry garbage collection, and automated promulgation by Element Management System to other systems in the service domain. TItemScope applies to SAP-ingress, SAP-egress, and Network policies, and to IP filters and MAC filters. exclusive: When the scope of an item is defined as exclusive, the item can only be applied once, for example to a single SAP. Attempting to assign the policy to a second SAP is not allowed and will result in an error. If the item is removed from the exclusive SAP, it will become available for assignment to another exclusive SAP. A non-applied exclusive scope policy is a candidate to be removed from the system by a TBD garbage collection command. The system default policies cannot be put into the exclusive scope. An error will be generated if scope exclusive is executed in any policies with a policy-id equal to 1. template: When the scope of an item is defined as template, the item can be applied any number of times. Policies with template scope will not be considered for deletion by a TBD garbage collection command; all items of scope 'template' must be deleted explicitly. The system default policies will always be scope template. An error will occur if a policy-id 1 is attempted to be set to scope exclusive."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("exclusive", 1), ("template", 2))

class TItemMatch(TextualConvention, Integer32):
    description = 'when set to off, the item is not matched. when set to false, packets without the item match the filter. when set to true, packets with the item match the filter.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("false", 2), ("true", 3))

class TPriority(TextualConvention, Integer32):
    description = 'the priority to apply to a packet'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("low", 1), ("high", 2))

class TPriorityOrDefault(TextualConvention, Integer32):
    description = 'the priority to apply to a packet. when set to default(3), the priority from the default-action is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("low", 1), ("high", 2), ("default", 3))

class TProfileUseDEOrNone(TextualConvention, Integer32):
    description = "This textual-convention specifies the profile marking of a packet. Value of 'in' specifies in-profile marking. Value of 'out' specifies out-profile marking. Value of 'de' specifies that the profile marking of the packet will be based on the DE (Drop-Eligible) bit of the packet. DE bit value of '0' specifies in-profile and DE bit value of '1' specifies out-profile marking. Value of 'none' specifies the profile marking of the packet will be inherited from the existing enqueuing priority derived from earlier matches in the classification hierarchy."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("in", 1), ("out", 2), ("de", 3))

class TPriorityOrUndefined(TextualConvention, Integer32):
    description = 'the priority to apply to a packet. when set to undefined(0), the priority is not applicable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("low", 1), ("high", 2))

class TProfile(TextualConvention, Integer32):
    description = 'the profile marking of a packet at the ingress.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("in", 1), ("out", 2))

class TProfileOrDei(TextualConvention, Integer32):
    description = 'the profile marking of a packet at the ingress.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 13))
    namedValues = NamedValues(("in", 1), ("out", 2), ("use-dei", 13))

class TDEProfile(TextualConvention, Integer32):
    description = "This textual-convention specifies the profile marking of a packet. Value of 'in' specifies the in-profile marking. Value of 'out' specifies the out-profile marking. Value of 'de' specifies that the profile marking will be based on the DE (Drop-Eligible) bit. DE bit-value of '0' specifies in-profile and DE bit value of '1' specifies out-profile marking."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("in", 1), ("out", 2), ("de", 3))

class TDEProfileOrDei(TextualConvention, Integer32):
    description = "This textual-convention specifies the profile marking of a packet. Value of 'in' specifies the in-profile marking. Value of 'out' specifies the out-profile marking. Value of 'de' specifies that the profile marking will be based on the DE (Drop-Eligible) bit. DE bit-value of '0' specifies in-profile and DE bit value of '1' specifies out-profile marking."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 13))
    namedValues = NamedValues(("in", 1), ("out", 2), ("de", 3), ("use-dei", 13))

class TProfileOrNone(TextualConvention, Integer32):
    description = 'Profile marking of a packet.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("in", 1), ("out", 2))

class TAdaptationRule(TextualConvention, Integer32):
    description = 'The adaptation rule to be applied to calcluate the operational values for the specified entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("max", 1), ("min", 2), ("closest", 3))

class TAdaptationRuleOverride(TextualConvention, Integer32):
    description = 'The adaptation rule to be applied to calcluate the operational values for the specified entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noOverride", 0), ("max", 1), ("min", 2), ("closest", 3))

class TRemarkType(TextualConvention, Integer32):
    description = 'The remarking to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("dscp", 2), ("precedence", 3))

class TPrecValue(TextualConvention, Integer32):
    description = 'The precedence bits as used in the IPv4 header. This constitutes of 3 bits and hence can hold the values from 0 to 7.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class TPrecValueOrNone(TextualConvention, Integer32):
    description = "The precedence bits as used in the IPv4 header. This constitutes of 3 bits and hence can hold the values from 0 to 7. The value '-1' specifies that the precedence value is undefined/unused."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TBurstSize(TextualConvention, Integer32):
    description = "The amount of buffer space (in kbytes) assigned to a queue. The value -1 means that the actual value is derived from the corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 131072), )
class TBurstSizeOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in kbytes) assigned to a queue. The value -1 means that the actual value is derived from the corresponding buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 131072), )
class TBurstPercent(TextualConvention, Integer32):
    description = 'The percentage of buffer space assigned to a queue that is reserved for some purpose.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TBurstHundredthsOfPercent(TextualConvention, Integer32):
    description = 'The percentage of buffer space assigned to a queue that is reserved for some purpose, defined to two decimal places.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

class TBurstPercentOrDefault(TextualConvention, Integer32):
    description = "The percentage of buffer space assigned to a queue that is reserved for some purpose. The value -1 means that the actual value is derived from the corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class TBurstPercentOrDefaultOverride(TextualConvention, Integer32):
    description = "The percentage of buffer space assigned to a queue that is reserved for some purpose. The value -1 means that the actual value is derived from the corresponding buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class TRatePercent(TextualConvention, Integer32):
    description = 'The percentage of maximum rate allowed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TPIRRatePercent(TextualConvention, Integer32):
    description = 'The percentage of maximum PIR rate allowed. A value of 0 is not acceptable, so the range begins at 1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class TLevel(TextualConvention, Integer32):
    description = 'The level of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TLevelOrDefault(TextualConvention, Integer32):
    description = 'The level of the specified entity while feeding into the parent. The value 0 is used to denote a default value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TQWeight(TextualConvention, Integer32):
    description = 'The Queue weight of the specified entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 100), )
class TMeterMode(TextualConvention, Integer32):
    description = 'Meter Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("priority", 1), ("profile", 2))

class TPlcyMode(TextualConvention, Integer32):
    description = 'Port scheduler Policy Mode '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("roundRobin", 1), ("weightedRoundRobin", 2), ("weightedDeficitRoundRobin", 3))

class TPlcyQuanta(TextualConvention, Integer32):
    description = 'Port scheduler Quanta'
    status = 'current'

class TQueueMode(TextualConvention, Integer32):
    description = "The mode in which the queue is operating. If the queue is operating in the 'priority' mode, it is capable of handling traffic differently with two distinct priorities. These priorities are assigned by the stages preceding the queueing framework in the system. When the queue is operating in the 'profile' mode, in other words the color aware mode, the queue tries to provide the appropriate bandwidth to the packets with different profiles. The profiles are assigned according to the configuration of the forwarding class or the sub-forwarding class. In 'priority' mode, the queue does not have the functionality to support the profiled traffic and in such cases the queue will have a degraded performance. However, the converse is not valid and a queue in 'profile' mode should be capable of supporting the different priorities of traffic."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("priority", 1), ("profile", 2))

class TEntryIndicator(TextualConvention, Unsigned32):
    description = 'Uniquely identifies an entry in a policy or filter table. The value 0 is not a valid entry-id. When used as insertion point the value 0 indicates that entries must be inserted at the very beginning, i.e.before the first entry defined.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TEntryId(TEntryIndicator):
    description = 'uniquely identifies an entry in a policy or filter table. to facilitate insertion of entries in the tables, we recommend assigning entry IDs by 10s: 10, 20, 30, etc. '
    status = 'current'
    subtypeSpec = TEntryIndicator.subtypeSpec + ValueRangeConstraint(1, 65535)

class TMatchCriteria(TextualConvention, Integer32):
    description = 'determines whether the entry matches traffic using IP match entries or MAC match entries.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ip", 1), ("mac", 2), ("none", 3), ("dscp", 4), ("dot1p", 5), ("prec", 6))

class TmnxMdaQos(TextualConvention, Integer32):
    description = 'TmnxMdaQos is an enumerated integer whose value specifies the Quality of Service support of a Media Dependent Adapter (MDA).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("mda", 1), ("hsmda1", 2), ("hsmda2", 3))

class TAtmTdpDescrType(TextualConvention, Integer32):
    description = 'The TAtmTdpDescrType is an enumerated integer whose value indicates the types of cell loss priority to be used in conjunction with traffic parameters. The following values are outlined: Integer Value Interpretation ------------- ------------------------ clp0And1pcr PCR applies to CLP 0 and CLP 1 cell flows clp0And1pcrPlusClp0And1scr PCR applies to CLP 0 and CLP 1 cell flows. SCR applies to CLP 0 and CLP 1 cell flows. clp0And1pcrPlusClp0scr PCR applies to CLP 0 and CLP 1 cell flows. SCR applies to CLP 0 cell flows. clp0And1pcrPlusClp0scrTag PCR applies to CLP 0 and CLP 1 cell flows. SCR applies to CLP 0 cell flows. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("clp0And1pcr", 0), ("clp0And1pcrPlusClp0And1scr", 1), ("clp0And1pcrPlusClp0scr", 2), ("clp0And1pcrPlusClp0scrTag", 3))

class TDEValue(TextualConvention, Integer32):
    description = "This textual-convention specifies the DE (Drop Eligible) bit value. The value of '-1' means DE value is not specified."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1), )
class TQGroupType(TextualConvention, Integer32):
    description = 'This textual-convention specifies the type of the Queue-Group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("port", 0), ("vpls", 1))

class TQosOverrideType(TextualConvention, Integer32):
    description = 'This textual-convention specifies the type of the Qos Override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("queue", 1), ("policer", 2), ("aggRateLimit", 3), ("arbiter", 4), ("scheduler", 5))

class TmnxIPsecTunnelTemplateId(TextualConvention, Unsigned32):
    description = 'A number used to identify an entry in the tIPsecTnlTempTable.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2048)

class TmnxIPsecTunnelTemplateIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify an entry in the tIPsecTnlTempTable or zero.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2048)

class TmnxIpSecIsaOperFlags(TextualConvention, Bits):
    description = 'The value of TmnxIpSecIsaOperFlags specifies the operational flags that determine the status of the MDAs associated with IPsec ISA.'
    status = 'current'
    namedValues = NamedValues(("adminDown", 0), ("noActive", 1), ("noResources", 2))

class TmnxIkePolicyAuthMethod(TextualConvention, Integer32):
    description = 'TmnxIkePolicyAuthMethod data type is an enumerated integer that describes the type of authentication method used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("psk", 1), ("hybridX509XAuth", 2), ("plainX509XAuth", 3), ("plainPskXAuth", 4), ("cert", 5))

class TmnxIkePolicyOwnAuthMethod(TextualConvention, Integer32):
    description = 'TmnxIkePolicyOwnAuthMethod data type is an enumerated integer that describes the type of authentication method used for its own side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 5))
    namedValues = NamedValues(("symmetric", 0), ("psk", 1), ("cert", 5))

class TmnxRsvpDSTEClassType(TextualConvention, Unsigned32):
    description = 'TmnxRsvpDSTEClassType is an unsigned integer in the range of (0..7) that defines the class type (CT).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class TmnxAccPlcyQICounters(TextualConvention, Bits):
    description = 'This data type describes a set ingress counters for which accounting data can be collected associated with a given queue.'
    status = 'current'
    namedValues = NamedValues(("hpo", 0), ("lpo", 1), ("ucp", 2), ("hoo", 3), ("loo", 4), ("uco", 5), ("apo", 6), ("aoo", 7), ("hpd", 8), ("lpd", 9), ("hod", 10), ("lod", 11), ("ipf", 12), ("opf", 13), ("iof", 14), ("oof", 15))

class TmnxAccPlcyQECounters(TextualConvention, Bits):
    description = 'This data type describes a set egress counters for which accounting data can be collected associated with a given queue.'
    status = 'current'
    namedValues = NamedValues(("ipf", 0), ("ipd", 1), ("opf", 2), ("opd", 3), ("iof", 4), ("iod", 5), ("oof", 6), ("ood", 7))

class TmnxAccPlcyOICounters(TextualConvention, Bits):
    description = 'This data type describes a set ingress counters for which accounting data can be collected associated with a given counter.'
    status = 'current'
    namedValues = NamedValues(("apo", 0), ("aoo", 1), ("hpd", 2), ("lpd", 3), ("hod", 4), ("lod", 5), ("ipf", 6), ("opf", 7), ("iof", 8), ("oof", 9))

class TmnxAccPlcyOECounters(TextualConvention, Bits):
    description = 'This data type describes a set egress counters for which accounting data can be collected associated with a given counter.'
    status = 'current'
    namedValues = NamedValues(("ipf", 0), ("ipd", 1), ("opf", 2), ("opd", 3), ("iof", 4), ("iod", 5), ("oof", 6), ("ood", 7))

class TmnxAccPlcyAACounters(TextualConvention, Bits):
    description = 'This data type describes a set of AA (Application Assurance) counters for which accounting data can be collected.'
    status = 'current'
    namedValues = NamedValues(("any", 0), ("sfa", 1), ("nfa", 2), ("sfd", 3), ("nfd", 4), ("saf", 5), ("naf", 6), ("spa", 7), ("npa", 8), ("sba", 9), ("nba", 10), ("spd", 11), ("npd", 12), ("sbd", 13), ("nbd", 14), ("sdf", 15), ("mdf", 16), ("ldf", 17), ("tfd", 18), ("tfc", 19), ("sbm", 20), ("spm", 21), ("smt", 22), ("nbm", 23), ("npm", 24), ("nmt", 25))

class TmnxVdoGrpIdIndex(TextualConvention, Unsigned32):
    description = 'TmnxVdoGrpIdIndex data type describes the id of a TIMETRA-VIDEO-MIB::tmnxVdoGrpEntry and is the primary index for the table.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class TmnxVdoGrpId(TextualConvention, Unsigned32):
    description = 'TmnxVdoGrpId data type describes the identifier for a video group.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class TmnxVdoGrpIdOrInherit(TextualConvention, Integer32):
    description = "The data type describes the identifier for a video group. A value of '-1' indicates that identifier will be inherited from another object that is usually in another mib table."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4), )
class TmnxVdoFccServerMode(TextualConvention, Integer32):
    description = "The TmnxVdoFccServerMode data type is an enumerated integer that describes the mode of the Fast Channel Change (FCC) server. A value of 'burst' indicates that the FCC server is enabled and will send the channel at a nominally faster rate than the channel was received based on the TIMETRA-MCAST-PATH-MGMT-MIB::tmnxMcPathVdoPlcyFCCBurst setting. A value of 'dent' indicates that the FCC server will selectively discard frames from the original stream based on the value of TIMETRA-MCAST-PATH-MGMT-MIB::tmnxMcPathVdoPlcyFCCDentThd. A value of 'hybrid' indicates that the FCC server will use combination of 'burst' and 'dent' to send the unicast stream to the client. A value of 'none' indicates that FCC server is disabled."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("burst", 1), ("dent", 2), ("hybrid", 3))

class TmnxVdoPortNumber(TextualConvention, Unsigned32):
    description = 'The data type describes the port number of an Internet transport layer protocol.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1024, 5999), ValueRangeConstraint(6251, 65535), )
class TmnxVdoIfName(TNamedItem):
    description = 'The data type describes the name of a video interface. The name of a video interface must always start with a letter.'
    status = 'current'

class TmnxTimeInSec(TextualConvention, Unsigned32):
    description = 'The data type TmnxTimeInSec describes the Tarrif Time for the Charging Data Record (CDR).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 86400)

class TmnxMobProfName(TNamedItem):
    description = 'The data type TmnxMobProfName describes the name of a profile used by mobile gateways.'
    status = 'current'

class TmnxMobProfNameOrEmpty(TNamedItemOrEmpty):
    description = 'The data type TmnxMobProfNameOrEmpty describes the name of a profile used by mobile gateways.'
    status = 'current'

class TmnxMobProfIpTtl(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfIpTtl describes the Time-To-Live (TTL) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class TmnxMobDiaTransTimer(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobDiaTransTimer describes the diameter peer transaction timer value in seconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 180)

class TmnxMobDiaRetryCount(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobDiaRetryCount describes the diameter peer retry count value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8)

class TmnxMobDiaPeerHost(DisplayString):
    description = 'The data type TmnxMobDiaPeerHost describes the name of a destination realm, originating realm and originating host.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobGwId(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobGwId identifies mobile gateways.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxMobNode(DisplayString):
    description = 'The data type TmnxMobNode describes the name of a mobile gateway which consists of Mobile Country Code (MCC), Mobile Network Code (MNC), Region string, Group Id, Node Id. A mobile gateway name can be described as follows: <MCC>.<MNC>.<SGW|PGW>.<Region String>.<Group Id>.<Node Id> MCC : 3 digits (000-999) MNC : 2 or 3 digits Application Type : SGW or PGW (3 characters) Region String : 10 characters Group Id : 3 characters Node Id : 3 characters'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 30)

class TmnxMobBufferLimit(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobBufferLimit describes the buffer limit in bytes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobQueueLimit(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQueueLimit describes the queue limit in bytes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobRtrAdvtInterval(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobRtrAdvtInterval describes the router advertisement interval in minutes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 60)

class TmnxMobRtrAdvtLifeTime(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobRtrAdvtLifeTime describes the router advertisement life time in hours.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 24)

class TmnxMobAddrScheme(TextualConvention, Integer32):
    description = "The data type TmnxMobAddrScheme describes the addressing scheme. If the value is set to 'stateful', User Equipment (UE) uses DHCPv6 to get IPv6 address. If the value is set to 'stateless', UE uses ICMPv6 to get IPv6 address."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stateful", 1), ("stateless", 2))

class TmnxMobQciValue(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQciValue describes the QoS Class Identifier (QCI) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 9)

class TmnxMobQciValueOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQciValueOrZero describes the QoS Class Identifier (QCI) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArpValue(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobArpValue describes the Allocation and Retention Priority (ARP) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobArpValueOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobArpValueOrZero describes the Allocation and Retention Priority (ARP) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobApn(DisplayString):
    reference = '3GPP TS 23.003 Section 9.1'
    description = 'The data type TmnxMobApn describes the Access Point Name (APN) associated with an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 80)

class TmnxMobApnOrZero(DisplayString):
    description = 'The data type TmnxMobApnOrZero describes the Access Point Name (APN) associated with an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobImsi(TextualConvention, OctetString):
    description = 'The data type TmnxMobImsi describes the International Mobile Subscriber Identity (IMSI) of an User Equipment (UE). IMSI is defined as a number consisting of up to 15 BCD digits. The first 3 digits are the Mobile Country Code (MCC). The next 2 or 3 digits are the Mobile Network Code (MNC). The value of MCC determines whether the MNC is 2 digits or 3 digits. The remaining digits are the Mobile Subscriber Identification Number (MSIN). The internal representation of the IMSI is as follows: Bits 63-62 are reserved. Bits 61-60 indicate the length of the MNC field: 10 indicates a 2-digit MNC while 11 indicates a 3-digit MNC. Bits 59-0 hold the 15 IMSI BCD digits D1-15. When the total number of digits in the IMSI is less than 15, the nibble 0xf is used a filler. IMSI encoding for a 2-digit MNC: 63 55 47 39 0 +-----------+-----------+-----------+-------------------------+ | 0010| MCC1| MCC2| MCC3| MNC1| MNC2| MSIN (up to 10 digits) +-----------+-----------+-----------+-------------------------+ IMSI encoding for a 3-digit MNC: 63 55 47 39 35 0 +-----------+-----------+-----------+-------------------------+ | 0011| MCC1| MCC2| MCC3| MNC1| MNC2| MNC3| MSIN (up to 9 digits) +-----------+-----------+-----------+-------------------------+ Bits 63-56 of the IMSI are carried in octet number 1 of the octet string and bits 7-0 are carried in octet number 8 of the octet string.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobMsisdn(DisplayString):
    description = 'The data type TmnxMobMsisdn describes the Mobile Subscriber Integrated Services Digital Network (MSISDN) number of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class TmnxMobImei(DisplayString):
    description = 'The data type TmnxMobImei describes the International Mobile Equipment Identity (IMEI) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class TmnxMobNai(DisplayString):
    description = 'The data type TmnxMobNai describes the Network Address Identifier (NAI) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 72)

class TmnxMobMcc(DisplayString):
    description = 'The data type TmnxMobMcc describes the Mobile Country Code (MCC) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TmnxMobMnc(DisplayString):
    description = 'The data type TmnxMobMnc describes the Mobile Network Code (MNC) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobMccOrEmpty(DisplayString):
    description = 'The data type TmnxMobMccOrEmpty describes the Mobile Country Code (MCC) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 3), )
class TmnxMobMncOrEmpty(DisplayString):
    description = 'The data type TmnxMobMncOrEmpty describes the Mobile Network Code (MNC) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobUeState(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeState describes the state of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 1), ("active", 2), ("paging", 3), ("init", 4), ("suspend", 5), ("ddnDamp", 6))

class TmnxMobUeRat(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeRat describes the Radio Access Type (RAT) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("utran", 1), ("geran", 2), ("wlan", 3), ("gan", 4), ("hspa", 5), ("eutran", 6), ("ehrpd", 7), ("hrpd", 8), ("oneXrtt", 9), ("umb", 10))

class TmnxMobUeSubType(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeSubType describes the subscription type of User Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("homer", 1), ("roamer", 2), ("visitor", 3))

class TmnxMobPdnType(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnType describes the type of a Pakcet Data Network (PDN).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("ipv4v6", 3))

class TmnxMobPgwSigProtocol(TextualConvention, Integer32):
    description = 'The data type TmnxMobPgwSigProtocol describes the signaling protocol used on S5 or S8 reference point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gtp", 1), ("pmip", 2))

class TmnxMobPdnSessionState(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnSessionState describes the feedback signaling message (FSM) state of a Packet Data Network (PDN) session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("invalid", 0), ("init", 1), ("waitPcrfResponse", 2), ("waitPgwResponse", 3), ("waitEnodebUpdate", 4), ("connected", 5), ("ulDelPending", 6), ("dlDelPending", 7), ("idleMode", 8), ("pageMode", 9), ("dlHandover", 10), ("incomingHandover", 11), ("outgoingHandover", 12), ("stateMax", 13))

class TmnxMobPdnSessionEvent(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnSessionEvent describes the feedback signaling message (FSM) event of a Packet Data Network (PDN) session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("sessionInvalid", 0), ("gtpCreateSessReq", 1), ("gtpUpdateBearerReq", 2), ("gtpDeleteSessReq", 3), ("gtpDeleteBearerResp", 4), ("gtpUpdateBearerResp", 5), ("gtpModifyActiveToIdle", 6), ("gtpResrcAllocCmd", 7), ("gtpModifyQosCmd", 8), ("gtpX1eNodeBTeidUpdate", 9), ("gtpX2SrcSgwDeleteSessReq", 10), ("gtpS1CreateIndirectTunnel", 11), ("dlPktRecvIndication", 12), ("dlPktNotificationAck", 13), ("dlPktNotificationFail", 14), ("pcrfSessEstResp", 15), ("pcrfSessTerminateRsp", 16), ("pcrfProvQosRules", 17), ("pmipSessResp", 18), ("pmipSessUpdate", 19), ("pmipSessDeleteRsp", 20), ("pmipSessDeleteReq", 21), ("eventMax", 22))

class TmnxMobBearerId(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobBearerId describes the bearer identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobBearerType(TextualConvention, Integer32):
    description = 'The data type TmnxMobBearerType describes the type of a bearer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("dedicated", 2))

class TmnxMobQci(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQci describes the QoS Class Identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArp(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobArp describes the QoS parameter, Allocation and Retention Priority (ARP).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobSdf(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobSdf describes the number of Service Data Flows (SDFs).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobSdfFilter(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobSdfFilter describes a IP filter in a Service Data Flow (SDF) or Traffic Flow Template (TFT).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfFilterNum(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobSdfFilterNum describes the number of IP filters.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfRuleName(DisplayString):
    description = 'The data type TmnxMobSdfRuleName describes the policy rule name of a Service Data Flow (SDF).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TmnxMobSdfFilterDirection(TextualConvention, Integer32):
    description = 'The data type TmnxMobSdfFilterDirection describes the direction on which a Service Data Flow (SDF) filter rule is valid.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("preRel7", 0), ("downLink", 1), ("upLink", 2), ("biDir", 3))

class TmnxMobSdfFilterProtocol(TextualConvention, Integer32):
    description = 'The data type TmnxMobSdfFilterProtocol describes IPv4 protocol or IPv6 next header on which Service Data Flow (SDF) filter matches.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140))
    namedValues = NamedValues(("any", -1), ("ipv6HopByOpOpt", 0), ("icmp", 1), ("igmp", 2), ("ggp", 3), ("ip", 4), ("st", 5), ("tcp", 6), ("cbt", 7), ("egp", 8), ("igp", 9), ("bbnRccMon", 10), ("nvp2", 11), ("pup", 12), ("argus", 13), ("emcon", 14), ("xnet", 15), ("chaos", 16), ("udp", 17), ("mux", 18), ("dcnMeas", 19), ("hmp", 20), ("prm", 21), ("xnsIdp", 22), ("trunk1", 23), ("trunk2", 24), ("leaf1", 25), ("leaf2", 26), ("rdp", 27), ("irdp", 28), ("isoTp4", 29), ("netblt", 30), ("mfeNsp", 31), ("meritInp", 32), ("dccp", 33), ("pc3", 34), ("idpr", 35), ("xtp", 36), ("ddp", 37), ("idprCmtp", 38), ("tpplusplus", 39), ("il", 40), ("ipv6", 41), ("sdrp", 42), ("ipv6Route", 43), ("ipv6Frag", 44), ("idrp", 45), ("rsvp", 46), ("gre", 47), ("dsr", 48), ("bna", 49), ("esp", 50), ("ah", 51), ("iNlsp", 52), ("swipe", 53), ("narp", 54), ("mobile", 55), ("tlsp", 56), ("skip", 57), ("ipv6Icmp", 58), ("ipv6NoNxt", 59), ("ipv6Opts", 60), ("anyHostIntl", 61), ("cftp", 62), ("anyLocalNet", 63), ("satExpak", 64), ("kryptolan", 65), ("rvd", 66), ("ippc", 67), ("anyDFS", 68), ("satMon", 69), ("visa", 70), ("ipcv", 71), ("cpnx", 72), ("cphb", 73), ("wsn", 74), ("pvp", 75), ("brSatMon", 76), ("sunNd", 77), ("wbMon", 78), ("wbExpak", 79), ("isoIp", 80), ("vmtp", 81), ("secureVmpt", 82), ("vines", 83), ("ttp", 84), ("nsfnetIgp", 85), ("dgp", 86), ("tcf", 87), ("eiGrp", 88), ("ospfIgp", 89), ("spriteRpc", 90), ("larp", 91), ("mtp", 92), ("ax25", 93), ("ipip", 94), ("micp", 95), ("sccSp", 96), ("etherIp", 97), ("encap", 98), ("anyPEC", 99), ("gmtp", 100), ("ifmp", 101), ("pnni", 102), ("pim", 103), ("aris", 104), ("scps", 105), ("qnx", 106), ("activeNet", 107), ("ipComp", 108), ("snp", 109), ("compaqPeer", 110), ("ipxInIp", 111), ("vrrp", 112), ("pgm", 113), ("any0hop", 114), ("l2tp", 115), ("ddx", 116), ("iatp", 117), ("stp", 118), ("srp", 119), ("uti", 120), ("smp", 121), ("sm", 122), ("ptp", 123), ("isis", 124), ("fire", 125), ("crtp", 126), ("crudp", 127), ("sscopmce", 128), ("iplt", 129), ("sps", 130), ("pipe", 131), ("sctp", 132), ("fc", 133), ("rsvpE2eIgnore", 134), ("mobHeader", 135), ("udpLite", 136), ("mplsInIp", 137), ("manet", 138), ("hip", 139), ("shim6", 140))

class TmnxMobPathMgmtState(TextualConvention, Integer32):
    description = "The data type TmnxMobPathMgmtState describes the state of a path for a reference point. A value of 'reqTimeOut' indicates that the peer is not replying to the Echo Request messages the SGW is sending out."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 0), ("up", 1), ("reqTimeOut", 2), ("fault", 3), ("idle", 4), ("restart", 5))

class TmnxMobDiaPathMgmtState(TextualConvention, Integer32):
    description = 'The data type TmnxMobDiaPathMgmtState describes the state of a path for a diameter connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("shutDown", 0), ("shuttingDown", 1), ("inactive", 2), ("active", 3))

class TmnxMobDiaDetailPathMgmtState(TextualConvention, Integer32):
    description = 'The data type TmnxMobDiaDetailPathMgmtState describes the detail state of a path for a diameter connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("error", 0), ("idle", 1), ("closed", 2), ("localShutdown", 3), ("remoteClosing", 4), ("waitConnAck", 5), ("waitCea", 6), ("open", 7), ("openCoolingDown", 8), ("waitDns", 9))

class TmnxMobGwType(TextualConvention, Integer32):
    description = 'The data type TmnxMobGwType describes the mobile gateway type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("wlanGw", 3))

class TmnxMobChargingProfile(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobChargingProfile describes the charging trigger rules applied for generating Charging Data Records (CDR) for subscribers.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobChargingProfileOrInherit(TextualConvention, Integer32):
    description = "The data type TmnxMobChargingProfileOrInherit describes the charging trigger rules applied for generating Charging Data Records (CDR) for subscribers. A value of '-1' indicates that identifier will be inherited from another object that is usually in another mib table."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TmnxMobAuthType(TextualConvention, Integer32):
    description = 'The data type TmnxMobAuthType describes the authentication type used by mobile gateways.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("radius", 1), ("diameter", 2))

class TmnxMobAuthUserName(TextualConvention, Integer32):
    description = 'The data type TmnxMobAuthUserName describes the user name used in authentication requests by mobile gateways.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("pco", 3))

class TmnxMobProfGbrRate(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfGbrRate describes the Guaranteed Bit Rate (GBR) value in kilo-bits per second(kbps).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobProfMbrRate(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfMbrRate describes the Maximum Bit Rate (MBR) value in kilo-bits per second(kbps).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobPeerType(TextualConvention, Integer32):
    description = 'The data type TmnxMobPeerType describes the type of the mobile gateway peer as Serving Gateway (SGW), Packet Data Network Gateway (PGW) or High Rate Packet Data (HRPD) Serving Gateway (HSGW).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("hsgw", 3))

class TmnxMobRfAcctLevel(TextualConvention, Integer32):
    description = 'TmnxMobRfAcctLevel data type is an enumerated integer that describes the accounting level.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdnLevel", 1), ("qciLevel", 2))

class TmnxMobProfPolReportingLevel(TextualConvention, Integer32):
    description = 'TmnxMobProfPolReportingLevel data type is an enumerated integer that describes the Reporting level for the Policy and Charging Control (PCC) rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("servId", 1), ("ratingGrp", 2))

class TmnxMobProfPolChargingMethod(TextualConvention, Integer32):
    description = "TmnxMobProfPolChargingMethod data type is an enumerated integer that describes the Charging Method for the Policy and Charging Control (PCC) rule. A variable of this type could be set to 'online' charging method, 'offline' charging method or 'both'. If the variable is set to 'profChargingMtd' the charging method is set to 'offline' if 'tmnxMobProfPgwChrgOffLineState' is set to 'enabled', the charging method is set to 'online' if 'tmnxMobProfPgwChrgGyState' is set to 'enabled' and the charging method is set to 'both' if both 'tmnxMobProfPgwChrgOffLineState' and 'tmnxMobProfPgwChrgGyState' are set to 'enabled'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("profChargingMtd", 0), ("online", 1), ("offline", 2), ("both", 3))

class TmnxMobProfPolMeteringMethod(TextualConvention, Integer32):
    description = 'TmnxMobProfPolMeteringMethod data type is an enumerated integer that describes the Metering Method for the Policy and Charging Control (PCC) rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("timeBased", 1), ("volBased", 2), ("both", 3))

class TmnxMobServerState(TextualConvention, Integer32):
    description = 'The data type TmnxMobServerState describes the state of a server connected with a mobile gateway.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class TmnxMobChargingBearerType(TextualConvention, Integer32):
    description = 'The data type TmnxMobChargingBearerType describes the type of a bearer context used in charging applications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("home", 1), ("visiting", 2), ("roaming", 3))

class TmnxMobChargingLevel(TextualConvention, Integer32):
    description = 'The data type TmnxMobChargingLevel describes the level where the charging is done.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdn", 1), ("bearer", 2))

class TmnxMobIpCanType(TextualConvention, Integer32):
    description = 'The data type TmnxMobIpCanType describes the type of Internet Protocol Connectivity Access Network (IP-CAN) session as Evolved Packet Core (epc3gpp) or GPRS (gprs3gpp).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("epc3gpp", 1), ("gprs3gpp", 2))

class TmnxMobStaticPolPrecedence(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobStaticPolPrecedence describes the precedence value for a static policy configured in the system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65536)

class TmnxMobStaticPolPrecedenceOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobStaticPolPrecedence describes the precedence value for a static policy configured in the system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxMobDualStackPref(TextualConvention, Integer32):
    description = "The data type TmnxMobDualStackPref describes the preference in a dual IP stack. The value 'useCplane' specifies that the value is inherited from the preference in a dual IP stack on control plane."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("useCplane", 3))

class TmnxMobDfPeerId(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobDfPeerId identifies Delivery Function (DF) peer for the mobile gateways.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxMobLiTarget(TextualConvention, OctetString):
    description = 'The data type TmnxMobLiTarget describes the target for the interception. The target can be of type International Mobile Subscriber Identity (IMSI), Mobile Subscriber Integrated Services Digital Network (MSISDN) or International Mobile Equipment Identity (IMEI). IMSI is defined as a number consisting of up to 15 BCD digits. The first 3 digits are the Mobile Country Code (MCC). The next 2 or 3 digits are the Mobile Network Code (MNC). The value of MCC determines whether the MNC is 2 digits or 3 digits. The remaining digits are the Mobile Subscriber Identification Number (MSIN). The internal representation of the IMSI is as follows: Bits 63-62 are reserved. Bits 61-60 indicate the length of the MNC field: 10 indicates a 2-digit MNC while 11 indicates a 3-digit MNC. Bits 59-0 hold the 15 IMSI BCD digits D1-15. When the total number of digits in the IMSI is less than 15, the nibble 0xf is used a filler. IMSI encoding for a 2-digit MNC: 63 55 47 39 0 +-----------+-----------+-----------+-------------------------+ | 0010| MCC1| MCC2| MCC3| MNC1| MNC2| MSIN (up to 10 digits) +-----------+-----------+-----------+-------------------------+ IMSI encoding for a 3-digit MNC: 63 55 47 39 35 0 +-----------+-----------+-----------+-------------------------+ | 0011| MCC1| MCC2| MCC3| MNC1| MNC2| MNC3| MSIN (up to 9 digits) +-----------+-----------+-----------+-------------------------+ Bits 63-56 of the IMSI are carried in octet number 1 of the octet string and bits 7-0 are carried in octet number 8 of the octet string.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobLiTargetType(TextualConvention, Integer32):
    description = 'The data type TmnxMobLiTargetType describes the types of target in Lawful Interception (LI).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("imei", 3))

class TmnxReasContextVal(TextualConvention, Unsigned32):
    description = 'The value of the label used to identify the entity using the specified context value on a specific port. 31 0 +--------+--------+--------+--------+ |00000000 00000000 00000000 000XXXXX| +--------+--------+--------+--------+ The value of this object is encoded in the least significant 5 bits and represents the context value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class TmnxVdoStatInt(TextualConvention, Integer32):
    description = "The data type TmnxVdoStatInt is an enumerated integer that specifies the time duration for which the video statistics are being counted. Setting a variable of this type to 'current' causes the time duration to be set to one second which is the least allowed value. A value of 'interval' makes it necessary for some other MIB object to actually quantify the time interval."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("current", 1), ("interval", 2))

class TmnxVdoOutputFormat(TextualConvention, Integer32):
    description = "The data type TmnxVdoOutputFormat is an enumerated integer that specifies the output format of the video stream. Setting a variable of this type to 'udp' causes the video stream to be of type 'udp' whereas setting a value of 'rtp-udp' causes the video stream to be of type 'rtp-udp'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("rtp-udp", 2))

class TmnxVdoAnalyzerAlarm(TextualConvention, Integer32):
    description = "The data type TmnxVdoAnalyzerAlarm is an enumerated integer that specifies the severity of the analyzer state alarm. Setting a variable of this type to 'none' indicates no error level. A value of 'tnc' indicates a TNC (Tech Non-Conformance) error level.A value of 'qos' indicates a QOS (Quality of Service) error level. A value of 'poa' indicates a POA (Program off Air) error level."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tnc", 1), ("qos", 2), ("poa", 3))

class TmnxVdoAnalyzerAlarmStates(TextualConvention, OctetString):
    description = "The data type TmnxVdoAnalyzerAlarmStates is an octet string that represents the analyzer state for the past 10 seconds. Setting a variable of this type to 'good'(00) indicates either there was no alarm during that second or the state of the stream has been cleared from a prior errored state. A value of 'tnc'(01)indicates a TNC (Tech Non-Conformance) error occured during that second. A value of 'qos'(02) indicates a QOS (Quality of Service) error occured during that second. A value of 'poa'(03) indicates a POA (Program off Air) error occured during that second. Since the octet string is 10 bytes long, the 10th byte indicates the most recent state of the stream. Below is how an example stream would appear. Each byte in the stream holds an alarm state for a second. good (00), -- stream was good during 1st second tnc (01), -- stream had tnc error during 2nd second qos (02), -- stream had qos error during 3rd second qos (02), -- stream had qos error during 4th second qos (02), -- stream had qos error during 5th second good (00), -- stream error was cleared during 6th second good (00), -- stream was good during 7th second tnc (01), -- stream had tnc error during 8nd second poa (03), -- stream had poa error during 9th second good (00) -- stream error was cleared during 10th second."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class SvcISID(TextualConvention, Integer32):
    description = 'The SvcISID specifies a 24 bit (0..16777215) service instance identifier for the service. As part of the Provider Backbone Bridging frames, it is used at the destination PE as a demultiplexor field. The value of -1 is used to indicate the value of this object is un-specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 16777215), )
class TIngPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on ingress side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class TIngPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on ingress side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TEgrPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on egress side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TEgrPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on egress side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TFIRRate(TextualConvention, Integer32):
    description = 'The static fair rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TBurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue. The value -1 means that the actual value is derived from the corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 134217728), )
class THSMDABurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a HSMDA queue. The value -1 means that the actual value is derived from the corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2688000), )
class THSMDAQueueBurstLimit(TextualConvention, Integer32):
    description = "An explicit shaping burst size of a HSMDA queue. The value -1 means that the actual value is derived from the corresponding queue's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 1000000), )
class TClassBurstLimit(TextualConvention, Integer32):
    description = "An explicit shaping burst size for a class. The value -1 means that the actual value is derived from the corresponding class's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 327680), )
class TPlcrBurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue by policer. The value -1 means that the actual value is derived from the corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4194304), )
class TBurstSizeBytesOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue. The value -1 means that the actual value is derived from the corresponding buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 134217728), )
class THSMDABurstSizeBytesOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a HSMDA queue. The value -1 means that the actual value is derived from the corresponding buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2688000), )
class TPlcrBurstSizeBytesOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue by policer. The value -1 means that the actual value is derived from the corresponding buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4194304), )
class TmnxBfdSessOperState(TextualConvention, Integer32):
    description = 'The TmnxBfdSessOperState data type is an enumerated integer that describes the values used to identify the operational state of a BFD session the instance is relying upon for its fast triggering mechanism.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("connected", 2), ("broken", 3), ("peerDetectsDown", 4), ("notConfigured", 5), ("noResources", 6))

class TmnxIngPolicerStatMode(TextualConvention, Integer32):
    description = 'TmnxIngPolicerStatMode specifies the mode of statistics collected by this ingress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPrioNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPrioCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCapCIR", 8), ("offeredLimitedCapCIR", 9))

class TmnxIngPolicerStatModeOverride(TextualConvention, Integer32):
    description = 'TmnxIngPolicerStatModeOverride specifies the override mode of statistics collected by this ingress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noOverride", -1), ("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPrioNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPrioCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCapCIR", 8), ("offeredLimitedCapCIR", 9))

class TmnxEgrPolicerStatMode(TextualConvention, Integer32):
    description = 'TmnxEgrPolicerStatMode specifies the mode of statistics collected by this egress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredProfileCIR", 4), ("offeredLimitedCapCIR", 5), ("offeredProfileCapCIR", 6))

class TmnxEgrPolicerStatModeOverride(TextualConvention, Integer32):
    description = 'TmnxEgrPolicerStatModeOverride specifies the override mode of statistics collected by this egress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noOverride", -1), ("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredProfileCIR", 4), ("offeredLimitedCapCIR", 5), ("offeredProfileCapCIR", 6))

class TmnxTlsGroupId(TextualConvention, Unsigned32):
    description = 'A number used to identify a TLS Group. This ID must be unique within that Service Domain.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4094)

class TSubHostId(TextualConvention, Unsigned32):
    description = 'A number used to uniquely identify a subscriber host in the system'
    status = 'current'

class TDirection(TextualConvention, Integer32):
    description = 'TDirection denotes a direction.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("both", 0), ("ingress", 1), ("egress", 2))

class TBurstLimit(TextualConvention, Integer32):
    description = 'An explicit shaping burst size for a queue. The value of -1 specifies system default value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 14000000), )
class TMacFilterType(TextualConvention, Integer32):
    description = 'A type containing the possible types of MAC filters provided by the system'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("isid", 2), ("vid", 3))

class TmnxPwGlobalId(TextualConvention, Unsigned32):
    description = 'A number used to identify a global pseudo-wire routing identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxPwGlobalIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a global pseudo-wire routing identifier or zero.'
    status = 'current'

class TmnxPwPathHopId(TextualConvention, Unsigned32):
    description = 'A number used to identify a specific hop associated with pseudo-wire routing path.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxPwPathHopIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a specific hop associated with pseudo-wire routing path.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxSpokeSdpId(TextualConvention, Unsigned32):
    description = 'A number used to identify a multi-segment pseudo-wire provider-edge identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxSpokeSdpIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a multi-segment pseudo-wire provider-edge identifier.'
    status = 'current'

class TmnxMsPwPeSignaling(TextualConvention, Integer32):
    description = 'A number used to identify a multi-segment pseudo-wire provider-edge signaling type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("master", 2))

class TmnxLdpFECType(TextualConvention, Integer32):
    description = 'TmnxLdpFECType determines the kind of FEC that the label mapping, withdraw, release and request messages are referring to.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 128, 129, 130))
    namedValues = NamedValues(("addrWildcard", 1), ("addrPrefix", 2), ("addrHost", 3), ("vll", 128), ("vpws", 129), ("vpls", 130))

class TmnxSvcOperGrpCreationOrigin(TextualConvention, Integer32):
    description = 'A number used to identify creation origin for the service operational group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("mvrp", 2))

class TmnxOperGrpHoldUpTime(TextualConvention, Unsigned32):
    description = 'TmnxOperGrpHoldUpTime indicates time-interval in seconds for the service operational-group hold uptime.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class TmnxOperGrpHoldDownTime(TextualConvention, Unsigned32):
    description = 'TmnxOperGrpHoldDownTime indicates time-interval in seconds for the service operational-group hold down time.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class TmnxSrrpPriorityStep(TextualConvention, Integer32):
    description = 'TmnxSrrpPriorityStep indicates the range of the priority steps used by the operational group to monitor SRRP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10)

class TmnxAiiType(TextualConvention, Integer32):
    description = 'TmnxAiiType indicates LDP FEC 129 Attachment Individual Identifier (AII) type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("aiiType1", 1), ("aiiType2", 2))

class ServObjDesc(DisplayString):
    description = 'ASCII string used to describe various service objects.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TMplsLspExpProfMapID(TPolicyID):
    description = 'The identification number of a MPLS LSP EXP profile.'
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ValueRangeConstraint(1, 65535)

class TSysResource(TextualConvention, Integer32):
    description = 'The resource allocated for a particular application. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 11), )
class TmnxSpbFid(TextualConvention, Integer32):
    description = 'TmnxSpbFid indicates Shortest Path Bridging forwarding database identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

class TmnxSpbFidOrZero(TextualConvention, Integer32):
    description = 'TmnxSpbFid indicates Shortest Path Bridging forwarding database identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class TmnxSpbBridgePriority(TextualConvention, Integer32):
    description = 'TmnxSpbFid indicates the bridge priority for Shortest Path Bridging.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxSlopeMap(TextualConvention, Integer32):
    description = 'TmnxSlopeMap indicates the mapping style of the slope.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("low", 1), ("high", 2), ("highLow", 3))

class TmnxCdrType(TextualConvention, Integer32):
    description = 'The TmnxCdrType is an enumerated integer that describes the current charging type in Charging Data Record (CDR). pgwCdr - indicates Packet data network Gateway CDR gCdr - indicates Gateway GPRS Support Node (GGSN) CDR, where GPRS stands for General Packet Radio Service. eGCdr - indicates Enhanced Gateway GPRS Support Node (GGSN) CDR.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pgwCdr", 1), ("gCdr", 2), ("eGCdr", 3))

class TmnxThresholdGroupType(TextualConvention, Integer32):
    description = 'The TmnxThresholdGroupType is an enumerated integer that describes the group type in threshold based monitoring. brMgmtLimit - indicates the group for bearer management limit brMgmtCfSuccess - indicates the group for bearer management call flow success brMgmtCfFailure - indicates the group for bearer management call flow failure brMgmtTraffic - indicates the group for bearer management traffic pathMgmt - indicates the group for path management cpmSystem - indicates the group for the system of control plane module mgIsmSystem - indicates the group for the system of mobile gateway integrated service module'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("brMgmtLimit", 1), ("brMgmtCfSuccess", 2), ("brMgmtCfFailure", 3), ("brMgmtTraffic", 4), ("pathMgmt", 5), ("cpmSystem", 6), ("mgIsmSystem", 7))

class TmnxMobUeId(TextualConvention, OctetString):
    description = 'The data type TmnxMobUeId describes the identity of an User Equipment. TmnxMobUeId can be of the following types: International Mobile Subscriber Identity (IMSI), International Mobile station Equipment Identity (IMEI), Mobile Subscriber Integrated Services Digital network Number (MSISDN). IMSI, IMEI, MSISDN are defined in 3GPP TS 23.003. IMSI is defined as a number consisting of up to 15 BCD digits. The first 3 digits are the Mobile Country Code (MCC). The next 2 or 3 digits are the Mobile Network Code (MNC). The value of MCC determines whether the MNC is 2 digits or 3 digits. The remaining digits are the Mobile Subscriber Identification Number (MSIN). IMEI is defined as a number consisting of up to 16 BCD digits. The first 8 digits consists of Type Allocation Code (TAC). The next 6 digits consist of Serial Number (SNR) which could be followed by a Check Digit (CD) or Spare Digit (SD) of size 1 digit or by a Software Version Number (SVN) of size 2 digits. MSISDN is defined as a number consisting of 9 to 15 BCD digits. MSISDN consists of Country Code (CC) followed by National Destination Code (NDC) and Subscriber Number (SN). Bits 63-56 of the IMSI or IMEI or MSISDN are carried in octet number 1 of the octet string and bits 7-0 are carried in octet number 8 of the octet string. The internal representation of the IMSI is as follows: Bits 63-62 are reserved. Bits 61-60 indicate the length of the MNC field: 10 indicates a 2-digit MNC while 11 indicates a 3-digit MNC. Bits 59-0 hold the 15 IMSI BCD digits D1-15. When the total number of digits in the IMSI is less than 15, the nibble 0xf is used a filler. IMSI encoding for a 2-digit MNC: 63 55 47 39 0 +-----------+-----------+-----------+-------------------------+ | 0010| MCC1| MCC2| MCC3| MNC1| MNC2| MSIN (up to 10 digits) +-----------+-----------+-----------+-------------------------+ IMSI encoding for a 3-digit MNC: 63 55 47 39 35 0 +-----------+-----------+-----------+-------------------------+ | 0011| MCC1| MCC2| MCC3| MNC1| MNC2| MNC3| MSIN (up to 9 digits) +-----------+-----------+-----------+-------------------------+ The internal representation of the IMEI and MSISDN is as follows: IMEI encoding: 63 55 31 7 0 +-----------+-----------+----------------------+-------+ | TAC | SNR | SNV | |N2|N1|N4|N3|N6|N5|N8|N7|N10|N9|N12|N11|N14|N13|N16|N15| +-----------+-----------+-----------+------------------+ MSISDN encoding: 63 55 31 7 0 +-----------+-----------+----------------------+-------+ | CC | NDC | SN | |N2|N1|N4|N3|N6|N5|N8|N7|N10|N9|N12|N11|N14|N13|N16|N15| +-----------+-----------+-----------+------------------+ When the total number of digits in the IMEI or MSISDN is less than 15, the nibble 0x0 is used a filler. In each byte both nibbles are swapped and it is stored as shown in the above format. For example, in the format N3 & N4 present the nibble number 3 and 4 respectively and they are stored in reverse order. When the total number of digits are odd in IMEI and MSISDB, the last digit will be paired with nibble 0xf.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobUeIdType(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeIdType describes the types of identification for User Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("imsi", 0), ("imei", 1), ("msisdn", 2))

class TmnxMobImsiStr(DisplayString):
    reference = '3GPP TS 23.003 Numbering, addressing and identification, section 2.2 Composition of IMSI.'
    description = 'The data type TmnxMobImsiStr describes the International Mobile Subscriber Identity (IMSI) of a User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(9, 15), )
class TmnxVpnIpBackupFamily(TextualConvention, Bits):
    description = 'The value of TmnxVpnIpBackupFamily specifies the respective vpn family for which backup paths would be enabled.'
    status = 'current'
    namedValues = NamedValues(("ipv4", 0), ("ipv6", 1))

class TmnxTunnelGroupId(TextualConvention, Unsigned32):
    description = 'The value of TmnxTunnelGroupId specifies the tunnel-group identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxTunnelGroupIdOrZero(TextualConvention, Unsigned32):
    description = 'The value of TmnxTunnelGroupId specifies the tunnel-group identifier including zero indicating that group-id is not specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobRatingGrpState(TextualConvention, Integer32):
    description = 'The data type TmnxMobRatingGrpState describes the state of a rating group. allowFlow - Allow the traffic to flow disallowFlow - Disallow the traffic to Flow redWebPortal - Redirect the traffic to web portal allowResRules - Allow restricted rules iom1stPktTrigger - Get the trigger from on IOM on arrival of 1st packet dis1stPktTrigger - Disable 1st packet trigger and allow the traffic creditsToppedUp - Credits topped up waitForFpt - Unblocked and waiting for First Packet Trigger (FPT)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("allowFlow", 1), ("disallowFlow", 2), ("redWebPortal", 3), ("allowResRules", 4), ("iom1stPktTrigger", 5), ("dis1stPktTrigger", 6), ("creditsToppedUp", 7), ("waitForFpt", 8))

class TmnxMobPresenceState(TextualConvention, Integer32):
    description = 'The data type TmnxMobPresenceState describes the whether the given field is present.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("absent", 0), ("present", 1))

class TmnxMobPdnGyChrgTriggerType(TextualConvention, Integer32):
    description = "The data type TmnxMobPdnGyChrgTriggerType describes type of the trigger activated by the Online Charging System (OCS). sgsnIpAddrRecvd - Change in Serving GPRS Support Node (SGSN) IP address qosRecvd - Change in Quality of Service (QoS) locRecvd - Location Change ratRecvd - Router Advertisement Trigger (RAT) Change qosTrfClsRecvd - Change in QoS Traffic class qosRlbClsRecvd - Change in QoS Reliability class qosDlyClsRecvd - Change in QoS Delay class qosPeakThrptRecvd - Change in QoS Peak Throughput qosPrcClsRecvd - Change in QoS Precedence class qosMeanTrptRecvd - Change in QoS Mean Throughput qosMxBtRtUplnkRecvd - Change in QoS MBR for Uplink qosMxBtRtDllnkRecvd - Change in QoS MBR for Downlink qosResBerRecvd - Change in QoS Residual Bit Error Rate (BER) qosSduErrRatRecvd - Change in QoS Service Data Unit (SDU) Error Ratio class qosTransDelayRecvd - Change in QoS Transfer Delay qosTrfHndPriRecvd - Change in QoS Traffic Handling Priority qosGrtBtRtUplnkRecvd - Change in QoS Guaranteed Bit Rate (GBR) for Uplink qosGrtBtRtDllnkRecvd - Change in QoS GBR for Downlink locMccRecvd - Change in Location Mobile Country Code (MCC) locMncRecvd - Change in Location Mobile Network Code (MNC) locRacRecvd - Change in Location Routing Area Code (RAC) locLacRecvd - Change in Location Location Area Code (LAC) locCellIdRecvd - Change in Location Cell ID medCompRecvd - Change in Media Composition partcNmbRecvd - Change in Participants' number thrldPartcNmbRecvd - Change in Threshold of Participants' number usrPartcTypeRecvd - Change in User Participating Type servCondRecvd - Change in Service Condition servNodeRecvd - Change in Service Node usrCsgInfoRecvd - Change in User Closed Subscription Group (CSG) Information"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("sgsnIpAddrRecvd", 0), ("qosRecvd", 1), ("locRecvd", 2), ("ratRecvd", 3), ("qosTrfClsRecvd", 4), ("qosRlbClsRecvd", 5), ("qosDlyClsRecvd", 6), ("qosPeakThrptRecvd", 7), ("qosPrcClsRecvd", 8), ("qosMeanTrptRecvd", 9), ("qosMxBtRtUplnkRecvd", 10), ("qosMxBtRtDllnkRecvd", 11), ("qosResBerRecvd", 12), ("qosSduErrRatRecvd", 13), ("qosTransDelayRecvd", 14), ("qosTrfHndPriRecvd", 15), ("qosGrtBtRtUplnkRecvd", 16), ("qosGrtBtRtDllnkRecvd", 17), ("locMccRecvd", 18), ("locMncRecvd", 19), ("locRacRecvd", 20), ("locLacRecvd", 21), ("locCellIdRecvd", 22), ("medCompRecvd", 23), ("partcNmbRecvd", 24), ("thrldPartcNmbRecvd", 25), ("usrPartcTypeRecvd", 26), ("servCondRecvd", 27), ("servNodeRecvd", 28), ("usrCsgInfoRecvd", 29))

class TmnxMobPdnRefPointType(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnRefPointType describes the types of reference point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("gn", 3), ("s2a", 4), ("gp", 5))

class TmnxQosBytesHex(TextualConvention, OctetString):
    description = 'Represents the QoS bytes that has been requested for the bearer context of an User Equipment (UE).'
    status = 'current'
    displayHint = '2x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class TSiteOperStatus(TextualConvention, Integer32):
    description = 'TSiteOperStatus data type is an enumerated integer that describes the values used to identify the current operational state of a site.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("outOfResource", 3))

class TmnxSpbFdbLocale(TextualConvention, Integer32):
    description = 'TmnxSpbFdbLocale data type is an enumerated integer that describes the values used to indicate source of forwarding data-base (FDB) entry for Shortest Path Bridging (SPB).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("local", 1), ("sap", 2), ("sdp", 3), ("unknown", 4))

class TmnxSpbFdbState(TextualConvention, Integer32):
    description = 'TmnxSpbFdbState data type is an enumerated integer that describes the values used to indicate state of the forwarding data-base FDB entry for Shortest Path Bridging (SPB).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ok", 0), ("addModPending", 1), ("delPending", 2), ("sysFdbLimit", 3), ("noFateShared", 4), ("svcFdbLimit", 5), ("noUcast", 6))

class TmnxMobServRefPointType(TextualConvention, Integer32):
    description = 'The data type TmnxMobServRefPointType describes the types of reference point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("s2a", 4))

class TmnxMobAccessType(TextualConvention, Integer32):
    description = 'The data type TmnxMobAccessType describes the various access types. eps - evolved packet system. gprs - general packet radio services. non3gpp - trusted non-3gpp network such as evolved High Rate Packet Data (eHRPD) and untrusted non-3gpp network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eps", 1), ("gprs", 2), ("non3gpp", 3))

class TmnxMobUeStrPrefix(DisplayString):
    description = 'The data type TmnxMobUeStrPrefix describes the prefix for International Mobile Subscriber Identity (IMSI) or Mobile Subscriber Integrated Services Digital Network (MSISDN) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(4, 15)

class TmnxCdrDiagnosticAction(TextualConvention, Integer32):
    description = 'The TmnxCdrDiagnosticAction is an enumerated integer that describes whether the Diagnostics should be included or excluded in the Charging Data Record (CDR).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("included", 1), ("excluded", 2))

class TmnxMplsTpGlobalID(TextualConvention, Unsigned32):
    reference = "RFC 6370, 'MPLS Transport Profile (MPLS-TP) Identifiers', Section 3, 'Uniquely Identifying an Operator - the Global_ID'."
    description = 'The value of TmnxMplsTpGlobalID specifies the MPLS-TP global identifier.'
    status = 'current'

class TmnxMplsTpNodeID(TextualConvention, Unsigned32):
    reference = "RFC 6370, 'MPLS Transport Profile (MPLS-TP) Identifiers', Section 4, 'Node and Interface Identifiers'."
    description = 'The value of TmnxMplsTpNodeID specifies the MPLS-TP node identifier.'
    status = 'current'

class TmnxMplsTpTunnelType(TextualConvention, Integer32):
    description = 'The type of this MPLS-TP tunnel entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("mplsTpStatic", 1))

class TmnxVwmCardType(TextualConvention, Integer32):
    description = 'The TmnxVwmCardType data type is an enumerated integer that describes the values used to identify the VWM Shelf Card type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44))
    namedValues = NamedValues(("not-provisioned", 0), ("not-equipped", 1), ("sfc1A", 2), ("sfc1B", 3), ("sfc1C", 4), ("sfc1D", 5), ("sfc1E", 6), ("sfc1F", 7), ("sfc1G", 8), ("sfc1H", 9), ("sfc2AandB", 10), ("sfc2CandD", 11), ("sfc2EandF", 12), ("sfc2GandH", 13), ("sfc4A-D", 14), ("sfc4E-H", 15), ("sfc8", 16), ("sfd8A-R", 17), ("sfd8B-R", 18), ("sfd8C-R", 19), ("sfd8D-R", 20), ("sfd4A-R", 21), ("sfd4B-R", 22), ("sfd4C-R", 23), ("sfd4D-R", 24), ("sfd4E-R", 25), ("sfd4F-R", 26), ("sfd4G-R", 27), ("sfd4H-R", 28), ("sfd2A-R", 29), ("sfd2B-R", 30), ("sfd2C-R", 31), ("sfd2D-R", 32), ("sfd2E-R", 33), ("sfd2F-R", 34), ("sfd2G-R", 35), ("sfd2H-R", 36), ("sfd2I-R", 37), ("sfd2L-R", 38), ("sfd2M-R", 39), ("sfd2N-R", 40), ("sfd2O-R", 41), ("sfd2P-R", 42), ("sfd2Q-R", 43), ("sfd2R-R", 44))

mibBuilder.exportSymbols("TIMETRA-TC-MIB", TmnxMobStaticPolPrecedence=TmnxMobStaticPolPrecedence, TmnxSpokeSdpId=TmnxSpokeSdpId, timetraTCMIBModule=timetraTCMIBModule, TmnxMobUeRat=TmnxMobUeRat, TmnxMobDiaTransTimer=TmnxMobDiaTransTimer, TProfileUseDEOrNone=TProfileUseDEOrNone, TmnxPwPathHopId=TmnxPwPathHopId, TmnxMobMncOrEmpty=TmnxMobMncOrEmpty, TmnxMobServRefPointType=TmnxMobServRefPointType, TmnxVdoGrpId=TmnxVdoGrpId, TTmplPolicyID=TTmplPolicyID, TmnxMobLiTarget=TmnxMobLiTarget, TmnxSubAleOffset=TmnxSubAleOffset, TmnxVdoAnalyzerAlarmStates=TmnxVdoAnalyzerAlarmStates, TPolicyStatementNameOrEmpty=TPolicyStatementNameOrEmpty, TmnxIkePolicyOwnAuthMethod=TmnxIkePolicyOwnAuthMethod, TEntryIndicator=TEntryIndicator, TmnxAccessLoopEncaps2=TmnxAccessLoopEncaps2, THPolPIRRateOverride=THPolPIRRateOverride, TmnxMobPathMgmtState=TmnxMobPathMgmtState, TmnxMobChargingLevel=TmnxMobChargingLevel, TmnxMobGwType=TmnxMobGwType, TmnxMplsTpNodeID=TmnxMplsTpNodeID, TEgressQPerPacketOffset=TEgressQPerPacketOffset, TmnxIgmpVersion=TmnxIgmpVersion, TmnxEnabledDisabledOrInherit=TmnxEnabledDisabledOrInherit, TmnxMobRtrAdvtLifeTime=TmnxMobRtrAdvtLifeTime, TIpOption=TIpOption, TSecondaryShaper10GPIRRate=TSecondaryShaper10GPIRRate, THsmdaPIRMRateOverride=THsmdaPIRMRateOverride, TmnxTunnelGroupId=TmnxTunnelGroupId, TIngressHsmdaCounterId=TIngressHsmdaCounterId, TPlcyQuanta=TPlcyQuanta, TSdpEgressPolicyID=TSdpEgressPolicyID, TmnxSubNasPortSuffixType=TmnxSubNasPortSuffixType, TmnxBsxTransPrefPolicyId=TmnxBsxTransPrefPolicyId, TRateType=TRateType, TmnxBsxAarpIdOrZero=TmnxBsxAarpIdOrZero, THsmdaCIRKRateOverride=THsmdaCIRKRateOverride, TWeight=TWeight, TIngPolicerIdOrNone=TIngPolicerIdOrNone, TmnxMobAddrScheme=TmnxMobAddrScheme, TmnxMobMsisdn=TmnxMobMsisdn, TProfileOrDei=TProfileOrDei, TmnxLdpFECType=TmnxLdpFECType, TPriorityOrDefault=TPriorityOrDefault, TmnxSpokeSdpIdOrZero=TmnxSpokeSdpIdOrZero, TPlcrBurstSizeBytes=TPlcrBurstSizeBytes, TmnxMobPdnType=TmnxMobPdnType, TmnxMobLiTargetType=TmnxMobLiTargetType, TmnxTunnelType=TmnxTunnelType, TMeterMode=TMeterMode, TEgressHsmdaCounterIdOrZero=TEgressHsmdaCounterIdOrZero, TmnxMobBearerId=TmnxMobBearerId, THSMDABurstSizeBytesOverride=THSMDABurstSizeBytesOverride, TmnxSubRadServAlgorithm=TmnxSubRadServAlgorithm, TmnxIngPolicerStatModeOverride=TmnxIngPolicerStatModeOverride, TmnxTimeInSec=TmnxTimeInSec, TmnxDhcpOptionType=TmnxDhcpOptionType, TmnxAccessLoopEncapDataLink=TmnxAccessLoopEncapDataLink, TmnxBgpRouteTarget=TmnxBgpRouteTarget, TmnxMsPwPeSignaling=TmnxMsPwPeSignaling, ServObjDesc=ServObjDesc, TmnxVcId=TmnxVcId, TBurstPercentOrDefaultOverride=TBurstPercentOrDefaultOverride, TmnxBsxTransPrefPolicyIdOrZero=TmnxBsxTransPrefPolicyIdOrZero, TAdvCfgRate=TAdvCfgRate, TLevel=TLevel, TmnxCdrType=TmnxCdrType, TExpSecondaryShaperPIRRate=TExpSecondaryShaperPIRRate, THPolCIRRateOverride=THPolCIRRateOverride, TmnxMobChargingProfileOrInherit=TmnxMobChargingProfileOrInherit, TmnxSpbFdbLocale=TmnxSpbFdbLocale, InterfaceIndex=InterfaceIndex, TOperator=TOperator, TPortSchedulerPIR=TPortSchedulerPIR, TmnxFilterProfileStringOrEmpty=TmnxFilterProfileStringOrEmpty, TmnxBsxAarpServiceRefType=TmnxBsxAarpServiceRefType, TQWeight=TQWeight, TmnxIngPolicerStatMode=TmnxIngPolicerStatMode, TmnxActionType=TmnxActionType, TmnxDHCP6MsgType=TmnxDHCP6MsgType, TmnxOspfInstance=TmnxOspfInstance, TPerPacketOffset=TPerPacketOffset, THsmdaWrrWeightOverride=THsmdaWrrWeightOverride, TIngHsmdaPerPacketOffsetOvr=TIngHsmdaPerPacketOffsetOvr, TPolicerWeight=TPolicerWeight, TNamedItemOrEmpty=TNamedItemOrEmpty, TmnxIgmpGroupFilterMode=TmnxIgmpGroupFilterMode, TCpmProtPolicyIDOrDefault=TCpmProtPolicyIDOrDefault, TmnxMldGroupFilterMode=TmnxMldGroupFilterMode, TmnxPppNcpProtocol=TmnxPppNcpProtocol, TAdaptationRule=TAdaptationRule, TmnxMobAuthType=TmnxMobAuthType, TCpmProtPolicyID=TCpmProtPolicyID, TmnxIpSecIsaOperFlags=TmnxIpSecIsaOperFlags, TmnxMobArpValue=TmnxMobArpValue, TmnxReasContextVal=TmnxReasContextVal, THsmdaWeightOverride=THsmdaWeightOverride, TmnxSubProfileString=TmnxSubProfileString, IpAddressPrefixLength=IpAddressPrefixLength, TDEProfile=TDEProfile, THPolVirtualSchePIRRate=THPolVirtualSchePIRRate, TEgressHsmdaQueueId=TEgressHsmdaQueueId, TLevelOrDefault=TLevelOrDefault, TmnxOperGrpHoldUpTime=TmnxOperGrpHoldUpTime, TmnxPppoeUserNameOrEmpty=TmnxPppoeUserNameOrEmpty, THsmdaPIRKRateOverride=THsmdaPIRKRateOverride, TmnxMobDualStackPref=TmnxMobDualStackPref, TmnxIkePolicyAuthMethod=TmnxIkePolicyAuthMethod, TmnxAccPlcyOICounters=TmnxAccPlcyOICounters, TCIRRateOverride=TCIRRateOverride, TRatePercent=TRatePercent, TQosOverrideType=TQosOverrideType, TmnxTunnelID=TmnxTunnelID, TItemMatch=TItemMatch, TmnxSlaProfileString=TmnxSlaProfileString, PYSNMP_MODULE_ID=timetraTCMIBModule, BgpPeeringStatus=BgpPeeringStatus, TMplsLspExpProfMapID=TMplsLspExpProfMapID, TmnxPppoeSessionInfoOrigin=TmnxPppoeSessionInfoOrigin, TmnxServId=TmnxServId, TmnxSubProfileStringOrEmpty=TmnxSubProfileStringOrEmpty, TmnxSubRadiusVendorId=TmnxSubRadiusVendorId, TmnxVRtrIDOrZero=TmnxVRtrIDOrZero, TIpProtocol=TIpProtocol, TDEValue=TDEValue, TCIRPercentOverride=TCIRPercentOverride, TmnxBgpAutonomousSystem=TmnxBgpAutonomousSystem, TPrecValueOrNone=TPrecValueOrNone, TmnxMobPdnGyChrgTriggerType=TmnxMobPdnGyChrgTriggerType, TSapEgrEncapGroupActionType=TSapEgrEncapGroupActionType, TmnxSubMgtOrgStrOrZero=TmnxSubMgtOrgStrOrZero, TmnxAsciiSpecification=TmnxAsciiSpecification, THsmdaCIRMRateOverride=THsmdaCIRMRateOverride, TmnxCdrDiagnosticAction=TmnxCdrDiagnosticAction, THsmdaPolicyIncludeQueues=THsmdaPolicyIncludeQueues, TmnxStatus=TmnxStatus, TAdaptationRuleOverride=TAdaptationRuleOverride, TmnxAccPlcyQICounters=TmnxAccPlcyQICounters, TFCSet=TFCSet, TmnxTunnelGroupIdOrZero=TmnxTunnelGroupIdOrZero, THsmdaCIRKRate=THsmdaCIRKRate, TmnxAccPlcyOECounters=TmnxAccPlcyOECounters, TPrecValue=TPrecValue, TBWRateType=TBWRateType, TmnxMobBearerType=TmnxMobBearerType, SvcISID=SvcISID, TmnxMdaQos=TmnxMdaQos, TmnxVdoPortNumber=TmnxVdoPortNumber, TmnxMobApnOrZero=TmnxMobApnOrZero, TmnxMobPdnRefPointType=TmnxMobPdnRefPointType, TmnxVcType=TmnxVcType, TmnxVwmCardType=TmnxVwmCardType, TmnxVdoAnalyzerAlarm=TmnxVdoAnalyzerAlarm, TmnxPortID=TmnxPortID, TNetworkPolicyID=TNetworkPolicyID, TmnxMobPdnSessionEvent=TmnxMobPdnSessionEvent, TmnxAncpString=TmnxAncpString, TmnxQosBytesHex=TmnxQosBytesHex, TmnxSpbFidOrZero=TmnxSpbFidOrZero, TLNamedItem=TLNamedItem, TmnxMobDfPeerId=TmnxMobDfPeerId, TmnxMobArp=TmnxMobArp, TmnxMobStaticPolPrecedenceOrZero=TmnxMobStaticPolPrecedenceOrZero, TBurstPercentOrDefault=TBurstPercentOrDefault, TEntryId=TEntryId, TSubHostId=TSubHostId, TIngressQueueId=TIngressQueueId, TEgressHsmdaPerPacketOffset=TEgressHsmdaPerPacketOffset, TmnxMobProfPolChargingMethod=TmnxMobProfPolChargingMethod, TmnxSlaProfileStringOrEmpty=TmnxSlaProfileStringOrEmpty, TmnxAppProfileString=TmnxAppProfileString, TmnxPwGlobalId=TmnxPwGlobalId, TmnxMobUeSubType=TmnxMobUeSubType, TmnxMobProfMbrRate=TmnxMobProfMbrRate, ServiceOperStatus=ServiceOperStatus, TPIRPercentOverride=TPIRPercentOverride, TmnxEgrPolicerStatMode=TmnxEgrPolicerStatMode, TmnxMobPeerType=TmnxMobPeerType, TSapEgressPolicyID=TSapEgressPolicyID, THSMDABurstSizeBytes=THSMDABurstSizeBytes, TSapIngressMeterId=TSapIngressMeterId, TmnxVpnIpBackupFamily=TmnxVpnIpBackupFamily, THsmdaPIRKRate=THsmdaPIRKRate, TmnxAncpStringOrZero=TmnxAncpStringOrZero, TmnxBsxAarpId=TmnxBsxAarpId, TmnxBGPFamilyType=TmnxBGPFamilyType, TmnxBfdSessOperState=TmnxBfdSessOperState, THPolPIRRate=THPolPIRRate, ServiceAccessPoint=ServiceAccessPoint, TmnxMobIpCanType=TmnxMobIpCanType, THsmdaWrrWeight=THsmdaWrrWeight, TmnxSrrpPriorityStep=TmnxSrrpPriorityStep, TmnxBsxTransitIpPolicyId=TmnxBsxTransitIpPolicyId, TmnxRadiusPendingReqLimit=TmnxRadiusPendingReqLimit, TmnxManagedRouteStatus=TmnxManagedRouteStatus, TPIRRateOrZero=TPIRRateOrZero, TPortSchedulerCIR=TPortSchedulerCIR, TQueueIdOrAll=TQueueIdOrAll, TNetworkIngressMeterId=TNetworkIngressMeterId, TmnxAiiType=TmnxAiiType, TDSCPNameOrEmpty=TDSCPNameOrEmpty, TQosQGrpInstanceIDorZero=TQosQGrpInstanceIDorZero, TmnxSubMgtIntDestId=TmnxSubMgtIntDestId, TBurstSize=TBurstSize, TPortSchedulerPIRRate=TPortSchedulerPIRRate, TmnxSpbBridgePriority=TmnxSpbBridgePriority, TmnxSubNasPortTypeType=TmnxSubNasPortTypeType, THPolCIRRate=THPolCIRRate, ServiceAdminStatus=ServiceAdminStatus, TmnxMobNode=TmnxMobNode, TmnxMobProfName=TmnxMobProfName, THsmdaWeightClass=THsmdaWeightClass, TmnxMobQci=TmnxMobQci, Dot1PPriority=Dot1PPriority, TBurstLimit=TBurstLimit, TmnxBsxTransitIpPolicyIdOrZero=TmnxBsxTransitIpPolicyIdOrZero, TmnxMldGroupType=TmnxMldGroupType, TBurstSizeBytesOverride=TBurstSizeBytesOverride, Dot1PPriorityMask=Dot1PPriorityMask, TmnxVdoIfName=TmnxVdoIfName, TmnxMobQueueLimit=TmnxMobQueueLimit, TmnxMobSdfFilterDirection=TmnxMobSdfFilterDirection, TEgressQueueId=TEgressQueueId, TDSCPValue=TDSCPValue, TQueueId=TQueueId, TmnxMldVersion=TmnxMldVersion, TMlpppQoSProfileId=TMlpppQoSProfileId, TmnxEncapVal=TmnxEncapVal, TIngressHsmdaQueueId=TIngressHsmdaQueueId, TmnxMobImsiStr=TmnxMobImsiStr, TmnxMobMcc=TmnxMobMcc, TmnxMobSdfFilterProtocol=TmnxMobSdfFilterProtocol, TmnxVcIdOrNone=TmnxVcIdOrNone, TFCNameOrEmpty=TFCNameOrEmpty, TmnxMobQciValueOrZero=TmnxMobQciValueOrZero, TmnxPppoeUserName=TmnxPppoeUserName, QTagOrZero=QTagOrZero, QTagFullRangeOrNone=QTagFullRangeOrNone, TProfileOrNone=TProfileOrNone, TEgrRateModType=TEgrRateModType, THsmdaSchedulerPolicyGroupId=THsmdaSchedulerPolicyGroupId, TDSCPName=TDSCPName, TBurstSizeBytes=TBurstSizeBytes, TPIRRate=TPIRRate, TmnxMobGwId=TmnxMobGwId, TmnxEnabledDisabled=TmnxEnabledDisabled, TmnxVPNRouteDistinguisher=TmnxVPNRouteDistinguisher, THsmdaPolicyScheduleClass=THsmdaPolicyScheduleClass, TmnxOperGrpHoldDownTime=TmnxOperGrpHoldDownTime, TmnxAccessLoopEncaps1=TmnxAccessLoopEncaps1, TRemarkType=TRemarkType, TmnxPwPathHopIdOrZero=TmnxPwPathHopIdOrZero)
mibBuilder.exportSymbols("TIMETRA-TC-MIB", TmnxMplsTpTunnelType=TmnxMplsTpTunnelType, TmnxMobDiaRetryCount=TmnxMobDiaRetryCount, TmnxMobApn=TmnxMobApn, QTagFullRange=QTagFullRange, TmnxRadiusServerOperState=TmnxRadiusServerOperState, TmnxEgrPolicerStatModeOverride=TmnxEgrPolicerStatModeOverride, TmnxMlpppEpClass=TmnxMlpppEpClass, TmnxVRtrID=TmnxVRtrID, TPlcyMode=TPlcyMode, TQueueMode=TQueueMode, TPIRRateOverride=TPIRRateOverride, TmnxMplsTpGlobalID=TmnxMplsTpGlobalID, TTcpUdpPort=TTcpUdpPort, TFCType=TFCType, TmnxMobArpValueOrZero=TmnxMobArpValueOrZero, TmnxAdminState=TmnxAdminState, TmnxBgpLocalPreference=TmnxBgpLocalPreference, TmnxMobChargingBearerType=TmnxMobChargingBearerType, TEgrHsmdaPerPacketOffsetOvr=TEgrHsmdaPerPacketOffsetOvr, TmnxOperState=TmnxOperState, TClassBurstLimit=TClassBurstLimit, TPolicyID=TPolicyID, TIngressMeterId=TIngressMeterId, TmnxVdoGrpIdIndex=TmnxVdoGrpIdIndex, TIngressHsmdaCounterIdOrZero=TIngressHsmdaCounterIdOrZero, TmnxSvcOperGrpCreationOrigin=TmnxSvcOperGrpCreationOrigin, TBurstSizeOverride=TBurstSizeOverride, TItemScope=TItemScope, TmnxIPsecTunnelTemplateId=TmnxIPsecTunnelTemplateId, TmnxIgmpGroupType=TmnxIgmpGroupType, TIngPolicerId=TIngPolicerId, TmnxMobUeStrPrefix=TmnxMobUeStrPrefix, TMacFilterType=TMacFilterType, TmnxMobProfPolReportingLevel=TmnxMobProfPolReportingLevel, TEgrPolicerIdOrNone=TEgrPolicerIdOrNone, TmnxSubNasPortPrefixType=TmnxSubNasPortPrefixType, TmnxMobSdfFilterNum=TmnxMobSdfFilterNum, TmnxMobAuthUserName=TmnxMobAuthUserName, TmnxMobPgwSigProtocol=TmnxMobPgwSigProtocol, TmnxStrSapId=TmnxStrSapId, TmnxAccPlcyAACounters=TmnxAccPlcyAACounters, TmnxAccPlcyQECounters=TmnxAccPlcyQECounters, TmnxMobSdfRuleName=TmnxMobSdfRuleName, TPIRRatePercent=TPIRRatePercent, TmnxMobNai=TmnxMobNai, TmnxBinarySpecification=TmnxBinarySpecification, TmnxSpbFid=TmnxSpbFid, TmnxMobMnc=TmnxMobMnc, TmnxMobProfNameOrEmpty=TmnxMobProfNameOrEmpty, TmnxVdoGrpIdOrInherit=TmnxVdoGrpIdOrInherit, TEgrPolicerId=TEgrPolicerId, TmnxVRtrMplsLspID=TmnxVRtrMplsLspID, TmnxMobDiaPeerHost=TmnxMobDiaPeerHost, TNamedItem=TNamedItem, TmnxPwGlobalIdOrZero=TmnxPwGlobalIdOrZero, TmnxVdoStatInt=TmnxVdoStatInt, TProfile=TProfile, TDSCPValueOrNone=TDSCPValueOrNone, TmnxMobProfGbrRate=TmnxMobProfGbrRate, TDSCPFilterActionValue=TDSCPFilterActionValue, TmnxSubIdentString=TmnxSubIdentString, TDirection=TDirection, TmnxMobRtrAdvtInterval=TmnxMobRtrAdvtInterval, TmnxDefSubIdSource=TmnxDefSubIdSource, TDEProfileOrDei=TDEProfileOrDei, TMatchCriteria=TMatchCriteria, TmnxAppProfileStringOrEmpty=TmnxAppProfileStringOrEmpty, TmnxMobUeIdType=TmnxMobUeIdType, TmnxMobProfPolMeteringMethod=TmnxMobProfPolMeteringMethod, TSysResource=TSysResource, TmnxMulticastAddrFamily=TmnxMulticastAddrFamily, TmnxVdoOutputFormat=TmnxVdoOutputFormat, TBurstHundredthsOfPercent=TBurstHundredthsOfPercent, TmnxThresholdGroupType=TmnxThresholdGroupType, TmnxMobUeId=TmnxMobUeId, TmnxSubMgtOrgString=TmnxSubMgtOrgString, THsmdaPIRMRate=THsmdaPIRMRate, TBurstPercent=TBurstPercent, TmnxMobDiaPathMgmtState=TmnxMobDiaPathMgmtState, TPriority=TPriority, TmnxMobAccessType=TmnxMobAccessType, TmnxMobRfAcctLevel=TmnxMobRfAcctLevel, TItemLongDescription=TItemLongDescription, TmnxRsvpDSTEClassType=TmnxRsvpDSTEClassType, TmnxVdoFccServerMode=TmnxVdoFccServerMode, THSMDAQueueBurstLimit=THSMDAQueueBurstLimit, TmnxMobBufferLimit=TmnxMobBufferLimit, TCIRRate=TCIRRate, TmnxMobImei=TmnxMobImei, TmnxMobSdfFilter=TmnxMobSdfFilter, TmnxTlsGroupId=TmnxTlsGroupId, TPolicerRateType=TPolicerRateType, TmnxMobMccOrEmpty=TmnxMobMccOrEmpty, TmnxSubIdentStringOrEmpty=TmnxSubIdentStringOrEmpty, TSapIngressPolicyID=TSapIngressPolicyID, TExpSecondaryShaperClassRate=TExpSecondaryShaperClassRate, THsmdaWeight=THsmdaWeight, TAtmTdpDescrType=TAtmTdpDescrType, TPriorityOrUndefined=TPriorityOrUndefined, TLspExpValue=TLspExpValue, TmnxSubAleOffsetMode=TmnxSubAleOffsetMode, TmnxSubMgtIntDestIdOrEmpty=TmnxSubMgtIntDestIdOrEmpty, TLNamedItemOrEmpty=TLNamedItemOrEmpty, TmnxMobPdnSessionState=TmnxMobPdnSessionState, TmnxMobRatingGrpState=TmnxMobRatingGrpState, TSdpIngressPolicyID=TSdpIngressPolicyID, TmnxSpbFdbState=TmnxSpbFdbState, TIngressHsmdaPerPacketOffset=TIngressHsmdaPerPacketOffset, TFIRRate=TFIRRate, TmnxPppoeSessionId=TmnxPppoeSessionId, TmnxIPsecTunnelTemplateIdOrZero=TmnxIPsecTunnelTemplateIdOrZero, TMcFrQoSProfileId=TMcFrQoSProfileId, TMaxDecRate=TMaxDecRate, THsmdaCounterIdOrZero=THsmdaCounterIdOrZero, TmnxPppoePadoDelay=TmnxPppoePadoDelay, SdpBindId=SdpBindId, TmnxMobProfIpTtl=TmnxMobProfIpTtl, TItemDescription=TItemDescription, TPerPacketOffsetOvr=TPerPacketOffsetOvr, TmnxMobDiaDetailPathMgmtState=TmnxMobDiaDetailPathMgmtState, TmnxSubRadiusAttrType=TmnxSubRadiusAttrType, TmnxMobPresenceState=TmnxMobPresenceState, TSapEgrEncapGrpQosPolicyIdOrZero=TSapEgrEncapGrpQosPolicyIdOrZero, TmnxMobServerState=TmnxMobServerState, TmnxMacSpecification=TmnxMacSpecification, TmnxCustId=TmnxCustId, TmnxMobSdf=TmnxMobSdf, TmnxMobImsi=TmnxMobImsi, TSapEgrEncapGroupType=TSapEgrEncapGroupType, TmnxMobUeState=TmnxMobUeState, TTcpUdpPortOperator=TTcpUdpPortOperator, THsmdaCIRMRate=THsmdaCIRMRate, TmnxBgpPreference=TmnxBgpPreference, TmnxMobQciValue=TmnxMobQciValue, TmnxDefInterDestIdSource=TmnxDefInterDestIdSource, TEgressHsmdaCounterId=TEgressHsmdaCounterId, TFrameType=TFrameType, TNonZeroWeight=TNonZeroWeight, TmnxPppoeSessionType=TmnxPppoeSessionType, THsmdaCounterIdOrZeroOrAll=THsmdaCounterIdOrZeroOrAll, QTag=QTag, TmnxMobChargingProfile=TmnxMobChargingProfile, TPlcrBurstSizeBytesOverride=TPlcrBurstSizeBytesOverride, TFCName=TFCName, TmnxSlopeMap=TmnxSlopeMap, TSiteOperStatus=TSiteOperStatus, THPolVirtualScheCIRRate=THPolVirtualScheCIRRate, TQGroupType=TQGroupType)
