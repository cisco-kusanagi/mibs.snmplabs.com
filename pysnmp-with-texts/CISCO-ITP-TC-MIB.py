#
# PySNMP MIB module CISCO-ITP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:03:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, IpAddress, Unsigned32, ModuleIdentity, Counter32, MibIdentifier, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "IpAddress", "Unsigned32", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 231))
ciscoItpTextualConventions.setRevisions(('2004-04-26 00:00', '2003-08-03 00:00', '2003-01-29 00:00', '2001-12-11 00:00', '2001-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpTextualConventions.setRevisionsDescriptions(('Updated CItpTcPointCodeType to allow M3UA and SUA point-code types.', 'Updated CItpTcPointCode textual convention to include descriptions for Japanese NTT and TTC variants.', 'Added textual convention used to support the ability to define multiple instances of the signalling points. The following textual conventions were added. CItpTcNetworkName CItpTcInstanceNumber CItpTcSls Also deprecated CItpTcGtaAddr and CItpTcGtaDisplayZB. Added CItpTcGtaLongAddr and CItpTcGtaLongDisplay. Added new enumerated value to CItpTcLinkType object for virtual link used to connect signalling points acting as gateways.', 'Added new enumerated value to CItpTcLinkType object for high speed link support. Add new enumerated value to the CItpTcSs7Variant object to support China national variant. A new textual convention has been added to address 0..15 range for Global Title addresses.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpTextualConventions.setLastUpdated('200404260000Z')
if mibBuilder.loadTexts: ciscoItpTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpTextualConventions.setContactInfo(' Cisco Systems, Inc Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpTextualConventions.setDescription('The defines textual conventions used by to manage devices related to the SS7 network. The relevant ITU documents describing this technology is the ITU Q series, including ITU Q.700: Introduction to CCITT Signalling System No. 7 and ITU Q.701 Functional description of the message transfer part (MTP) of Signalling System No. 7. Abbreviations: CDPA - Called Party Point Code CGPA - Calling Party Point Code CLLI - Common Language Location Codes CR - Connection Request message CREF - Connection Refusal message DPC - Destination Point Code ERR - Error message GTA - Global Title Address GTI - Global Title Indicator GTT - Global Title Translation LUDT - long unitdata message LUDTS - long unitdata service message M2PA - MTP2 Peer-to-Peer Adaptation Layer M3UA - MTP3-User Adaptation MAP - Mated Application Table MSU - Message Signal Unit MTP - Message Transport Protocol MTP2 - Layer 2 of Message Transport Protocol MTP3 - Layer 3 of Message Transport Protocol NAI - Nature of Address Indicator NP - Numbering Plan NTT - The Japanese Nippon Telephone & Telegraph OPC - Originating Point Code PC - Point Code RTN - Route Table Name RSR - Reset Request message SCCP - Signalling Connection Control Part SCTP - Stream Transmission Protocol(RFC 2960) SI - Signalling Indicator SP - Signalling Point SLC - Signalling Link Code SLS - Signalling Link Selector SSN - Subsystem Number SUA - SCCP-User Adaptation TFR - Transfer Restricted messages TT - Title Translation TTC - The Japanese Telecommunications Technology Committee UDT - unitdata message UDTS - unitdata service message XUDT - extended unitdata message XUDTS - extended unitdata service message ')
class CItpTcAclId(TextualConvention, Unsigned32):
    description = 'An numeric Identifier used to specify an access list used to permit and deny packets based on MTP3 information. Either the value 0 or the value of access list identifier. A value of zero indicates that an access list is not specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2700, 2999), )
class CItpTcCLLI(TextualConvention, OctetString):
    reference = 'Complete listings of geographical and geopolitical codes can be found in the BR 751-401-xxx series and BR 751-100-055, respectively.'
    description = 'Common Language Location Codes (CLLI Codes). An 11-character standardized geographic identifier that uniquely identifies the geographic location of telecommunication equipment. The CLLI code is supported as octet string containing administrative information in human-readable form. The use of control codes should be avoided. The use of newline should be avoided. The use of leading or trailing white space should be avoided.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 11)

class CItpTcDisplayPC(TextualConvention, OctetString):
    description = 'The Point Code in formatted based on the variant and the customer defined parameters.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 12)

class CItpTcEncodingSchemeValue(TextualConvention, Integer32):
    description = 'The encoding scheme value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class CItpTcGlobalTitleSelector(TextualConvention, Integer32):
    description = "Global Title Selector. 'nai' : Global title translation based on nature of address indicator. 'tt' : Global title translation based on translation type. 'ttNpEs' : Global title translation based on translation type, numbering plan value and Encoding Scheme Value. 'ttNpNaiEs' : Global title translation based on translation type, numbering plan, value, nature of address indicator and encoding scheme value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nai", 1), ("tt", 2), ("ttNpEs", 3), ("ttNpNaiEs", 4))

class CItpTcGlobalTitleSelectorName(TextualConvention, OctetString):
    description = 'The configured name associated with SCCP GTT Selector. An octet string specified by an administrator that must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 9)

class CItpTcGtaAddr(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT Global Title Address. An octet string specified by an administrator must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CItpTcGtaLongAddr(TextualConvention, OctetString):
    description = 'The configured hexadecimal digits in the SCCP GTT Global Title Address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CItpTcGtaDisplay(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT Global Title Address. It consists of ASCII representation of GTA hex digits. This textual convention has been deprecated and replaced by CItpTcGtaDisplayZB.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 15)

class CItpTcGtaDisplayZB(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT Global Title Address. It consists of ASCII representation of GTA hex digits.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 15)

class CItpTcGtaLongDisplay(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT Global Title Address. It consists of ASCII representation of GTA hex digits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CItpTcGtaDisplayLen(TextualConvention, Unsigned32):
    description = 'The SCCP GTT Global Title Address length.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class CItpTcGtaLongDisplayLen(TextualConvention, Unsigned32):
    description = 'The SCCP GTT Global Title Address length.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 64)

class CItpTcNetworkName(TextualConvention, OctetString):
    description = 'The network name is used to indicate the network in which this signalling point is participating. One or more instances of signalling points can exist in the same physical device. This identifier will be used to correlate instances of signalling points by network. When multiple instance support is not enable the network name will default to the null string. An octet string specified by an administrator that must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 19)

class CItpTcInstanceNumber(TextualConvention, Unsigned32):
    description = 'The instance number used to select a particular Signalling point.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcLinksetId(TextualConvention, OctetString):
    description = 'The configured name associated with an Signalling Point Linkset. An octet string specified by an administrator that must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 19)

class CItpTcLinkSLC(TextualConvention, Unsigned32):
    description = 'The Signalling Link Code. This is the link identifier within a linkset.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class CItpTcLinkType(TextualConvention, Integer32):
    description = "The link types. 'other' : This link is of some type not listed below. 'serial' : This link is a serial link transporting SS7 traffic. 'sctpIp' : This a SCTP/IP link transporting SS7 traffic. 'hsl' : This link is a high speed link using the ATM protocol for transporting SS7 traffic. 'virtual': This link is virtual link used to connect to instance of signalling point running on the same physical device. The link will be used to send and manage traffic between two signalling acting as a gateway."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("serial", 2), ("sctpIp", 3), ("hsl", 4), ("virtual", 5))

class CItpTcNAI(TextualConvention, Integer32):
    description = 'The SCCP GTT Network Address Indicator (NAI). The following values are generally used: Unknown Nature of Address (0), Subscriber Number (1), Reserved for national use (2), National Significant Number (3), International Number (4), Maximum NAI (127), Invalid NAI (253), Wild NAI (254).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcNetworkIndicator(TextualConvention, Integer32):
    description = "Network Indicator: international - International network national - National network reserved - Reserved for national use spare - Spare (for international use only) 'international' : International network 'internationalSpare' : International network spare 'national' : National network 'nationalSpare' : National network Spare"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("international", 0), ("internationatSpare", 1), ("national", 2), ("nationalSpare", 3))

class CItpTcNumberingPlan(TextualConvention, Integer32):
    description = 'The SCCP GTT Numbering Plan (NP). The following values are generally used: Unknown NP (0), ISDN/Telephony NP (1), Spare (2), Data NP (3), Telex NP (4), Maritime Mobile NP (5), Land Mobile NP (6), ISDN/Mobile NP (7), Private NP (8). Max NP (15), Invalid NP (253), Wild NP (254).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcPointCode(TextualConvention, Unsigned32):
    reference = 'The SS7 network node address as specified in the International Telecommunication Union standard Q.708: Specifications of Signalling System No. 7 - Numbering of International Signalling Point Codes, and by ANSI T1.111.8 Numbering of Signalling Point Codes. GF 001-9001 - Technical Specifications of Signalling System No. 7 for National Telephone Network of China.'
    description = 'The SS7 network node address as specified in the following references. The format of the Point code depends on the variant defined in the CgspSS7Variant object as follows. 33222222222211111111110000000000 10987654321098765432109876543210 ANSI: nnnnnnnn - Network cccccccc - Cluster mmmmmmmm - Member ITU: zzz - Zone aaaaaaaa - Area/Network iii - Identifier NTT: zzzzz - Zone aaaa - Area/Network iiiiiii - Identifier TTC: zzzzz - Zone aaaa - Area/Network iiiiiii - Identifier Note: The China variant has the same format as ANSI. This form of the point-code is not intended for for presentation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777216)

class CItpTcPointCodeMask(TextualConvention, Unsigned32):
    reference = 'The SS7 network node address as specified in the International Telecommunication Union standard Q.708: Specifications of Signalling System No. 7 - Numbering of International Signalling Point Codes, and by ANSI T1.111.8 Numbering of Signalling Point Codes.'
    description = 'A mask used to perform different operations on pointcodes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777216)

class CItpTcPointCodeType(TextualConvention, Integer32):
    description = "List of the possible Point Code types. 'primary' : The primary point used to communicate information on the Signalling point. 'additional' : Additional point codes. 'capability' : capability point codes. 'xua' : MTP3-User Adaptation point codes or SCCP-User Adaptation point codes."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primary", 1), ("additional", 2), ("capability", 3), ("xua", 4))

class CItpTcQos(TextualConvention, Unsigned32):
    description = 'The quality of service classification to be assigned to the IP packets used to transport the SS7 messages. The value can be from one to seven when selecting a Qos class or 255 to indicate the packet will not be assigned a Qos class. This value will be set to zero when cItpSpLinkType indicates that Quality of Service does not apply to this link.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )
class CItpTcRouteTableName(TextualConvention, OctetString):
    description = 'The configured name associated with an SP Route Table. An octet string specified by an administrator that must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 19)

class CItpTcServiceIndicator(TextualConvention, Integer32):
    reference = 'ITU Q.704 Signalling network functions and messages section 14.2.1 Service indicator.'
    description = "The list of possible Service Indicator values. This identifies the type of SS7 packet. The service indicator codes for the international Signalling network are allocated as follows: 'SNMM' : Signalling network management messages (SNMM) 'SNTM' : Signalling network testing and maintenance messages (SNTM) 'Spare2' : Spare 2 'SCCP' : SCCP 'TUP' : Telephone User Part (TUP) 'ISUP' : ISDN User Part (ISUP) 'DUPC' : Data User Part, call and circuit-related messages (DUPC) 'DUPF' : Data User Part, facility registration and cancellation messages (DUPF) 'MTUP' : Reserved for MTP Testing User Part (MTUP) 'BISUP' : Broadband ISDN User Part (BISUP) 'SISUP' : Satellite ISDN User Part (SISUP) 'Spare11' : Spare 11 'Spare12' : Spare 12 'Spare13' : Spare 13 'Spare14' : Spare 14 'Spare15' : Spare 15"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("snmm", 0), ("sntm", 1), ("spare2", 2), ("sccp", 3), ("tup", 4), ("isup", 5), ("dupc", 6), ("dupf", 7), ("mtup", 8), ("bisup", 9), ("sisup", 10), ("spare11", 11), ("spare12", 12), ("spare13", 13), ("spare14", 14), ("spare15", 15))

class CItpTcSls(TextualConvention, Unsigned32):
    description = 'The Signalling Link Selector is a numeric value that contains the MTP3 packets to allow load balancing of traffic across a link within a linkset or combined linkset. Each linkset provides one or more tables used to map Signalling Link Selectors to Signalling Link Codes. The number of Signalling Link Selectors is 16 for ITU and 256 for ANSI.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcSs7Variant(TextualConvention, Integer32):
    reference = 'GF 001-9001 - Technical Specifications of Signalling System No. 7 for National Telephone Network of China.'
    description = "The list of SS7 variants. 'ANSI' : The ANSI variant of the SS7 specification. 'ITU' : The ITU variant of the SS7 specification. 'China' : The China national variant. This variant is a combination of ITU and ANSI. The protocol matches ITU except where the point-code has been expanded to ANSI format."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ansi", 1), ("itu", 2), ("china", 3))

class CItpTcSubSystemNumber(TextualConvention, Unsigned32):
    description = 'The SCCP Subsystem Number . A value of zero indicates that a subsystem is not specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 255), )
class CItpTcSubSystemNumberMask(TextualConvention, Unsigned32):
    description = 'The SCCP Subsystem Number Mask.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2, 255)

class CItpTcTableLoadStatus(TextualConvention, Integer32):
    description = "The status of the current or prior load operation. 'loadNotRequested' : load operations have not been requested. 'loadInProgress' : load request is active. 'loadComplete' : load request complete without errors. 'loadCompleteWithErrors' : Load request completed with some type of errors that prevented the adding of one or more entries. 'loadFailed' : Load request failed."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("loadNotRequested", 1), ("loadInProgress", 2), ("loadComplete", 3), ("loadCompleteWithErrors", 4), ("loadFailed", 5))

class CItpTcTimerMtp2T01(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Alignment ready timer. The default and valid range is dependant on the value of variant. Min Max Def ------ ------ ------ ANSI 12500 16000 13000 ITU 40000 50000 40000 The SYNTAX statement allows values for both the ANSI, ITU variants and MTP2 Peer-to-Peer Adaptation Layer.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(5000, 150000)

class CItpTcTimerMtp2T02(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Not aligned timer. The default and valid range is dependant on the value of variant. This timer is only applicable if cItpTcLinkType is serial. A get on this object will return a zero if the link is not serial. Min Max Def ------ ------ ------ ANSI 5000 14000 11500 ITU 5000 150000 5000 The SYNTAX statement allows values for both the ANSI and ITU variants.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 150000), )
class CItpTcTimerMtp2T03(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Aligned timer. The default and valid range is dependant on the value of variant. This timer is only applicable if cItpTcLinkType is serial. A get on this object will return a zero if the link is not serial. Min Max Def ------ ------ ------ ANSI 5000 14000 11500 ITU 1000 2000 1500 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1000, 14000), )
class CItpTcTimerMtp2T04E(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Proving period timer emergency timer. The default and valid range is dependant on the value of variant. This timer is only applicable if cItpTcLinkType is serial. A get on this object will return a zero if the link is not serial. Min Max Def ------ ------ ------ ANSI 540 660 600 ITU 400 600 500 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(400, 660), )
class CItpTcTimerMtp2T04N(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Proving period timer normal timer. The default and valid range is dependant on the value of variant. This timer is only applicable if cItpTcLinkType is serial. A get on this object will return a zero if the link is not serial. Min Max Def ------ ------ ------ ANSI 2007 2530 2300 ITU 7500 9500 8200 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2007, 9500), )
class CItpTcTimerMtp2T05(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Sending SIB timer. The default and valid range is dependant on the value of variant. This timer is only applicable if cItpTcLinkType is serial. A get on this object will return a zero if the link is not serial. Min Max Def ------ ------ ------ ANSI 80 120 80 ITU 80 120 100 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(80, 120), )
class CItpTcTimerMtp2T06(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Remote congestion timer. The default and valid range is dependant on the value of variant. Min Max Def ------ ------ ------ ANSI 1000 6000 1000 ITU 3000 6000 3000 The SYNTAX statement allows values for both the ANSI, ITU variants and MTP2 Peer-to-Peer Adaptation Layer.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 6000)

class CItpTcTimerMtp2T07(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link. ANSI T1.111.3 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Excessive delay of acknowledgement timer. The default and valid range is dependant on the value of variant(). This timer is only applicable if cItpTcLinkType is serial. A get on this object will return a zero if the link is not serial. Min Max Def ------ ------ ------ ANSI 500 2000 1000 ITU 500 2000 1000 The SYNTAX statement allows values for both the ANSI and ITU variants.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 6000), )
class CItpTcTimerMtp3T01(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Delay to avoid message mis-sequencing on changeover. Ranges by variant. Min Max Def ------ ------ ------ ANSI 500 1200 800 ITU 500 1200 800 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T02(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for changeover acknowledgement. Ranges by variant. Min Max Def ------ ------ ------ ANSI 700 2000 1400 ITU 700 2000 1400 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(700, 2000)

class CItpTcTimerMtp3T03(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Time controlled diversion-delay to avoid mis-sequencing on change back. Ranges by variant. Min Max Def ------ ------ ------ ANSI 500 1200 800 ITU 500 1200 800 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T04(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for change back acknowledgement (first attempt). Ranges by variant. Min Max Def ------ ------ ------ ANSI 500 1200 800 ITU 500 1200 800 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T05(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for change back acknowledgement (second attempt). Ranges by variant. Min Max Def ------ ------ ------ ANSI 500 1200 800 ITU 500 1200 800 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T06(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Delay to avoid message mis-sequencing on controlled rerouting. Ranges by variant. Min Max Def ------ ------ ------ ANSI 500 1200 800 ITU 500 1200 800 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T07(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for Signalling data link connection acknowledgement. Ranges by variant. Min Max Def ------ ------ ------ ANSI 1000 2000 1500 ITU 1000 2000 1500 The SYNTAX statement allows values for both the ANSI and ITU variants. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1000, 2000), )
class CItpTcTimerMtp3T08(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Transfer prohibited inhibition timer (transient solution). Ranges by variant. Min Max Def ------ ------ ------ ANSI 800 1200 1000 ITU 800 1200 1000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1200)

class CItpTcTimerMtp3T10(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting to repeat Signalling routeset test message. Ranges by variant. Min Max Def ------ ------ ------ ANSI 30000 60000 45000 ITU 30000 60000 45000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(30000, 60000)

class CItpTcTimerMtp3T11(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Transfer restricted timer. (This is one way of implementing the function described in 13.4/Q.704 and mainly intended to simplify SPs.). Ranges by variant. Min Max Def ------ ------ ------ ANSI 30000 90000 60000 ITU 30000 90000 60000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(30000, 90000)

class CItpTcTimerMtp3T12(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for uninhibit acknowledgement. Ranges by variant. Min Max Def ------ ------ ------ ANSI 800 1500 1150 ITU 800 1500 1150 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1500)

class CItpTcTimerMtp3T13(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for force uninhibit. Ranges by variant. Min Max Def ------ ------ ------ ANSI 800 1500 1150 ITU 800 1500 1150 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1500)

class CItpTcTimerMtp3T14(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for inhibition acknowledgement. Ranges by variant. Min Max Def ------ ------ ------ ANSI 2000 3000 2500 ITU 2000 3000 2500 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2000, 3000)

class CItpTcTimerMtp3T15(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting to start Signalling routeset congestion test. Ranges by variant. Min Max Def ------ ------ ------ ANSI 2000 3000 2500 ITU 2000 3000 2500 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2000, 3000)

class CItpTcTimerMtp3T16(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for routeset congestion status update. Ranges by variant. Min Max Def ------ ------ ------ ANSI 1400 2000 1700 ITU 1400 2000 1700 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1400, 2000)

class CItpTcTimerMtp3T17(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Delay to avoid oscillation of initial alignment failure and link restart. Ranges by variant. Min Max Def ------ ------ ------ ANSI 800 1500 1150 ITU 800 1500 1150 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1500)

class CItpTcTimerMtp3T18(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: Repeat TFR once by response method ITU: MTP restart link supervision Min Max Def ------ ------ ------ ANSI 2000 20000 11000 ITU 1000 31000 30000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 31000)

class CItpTcTimerMtp3T19(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: failed craft timer referral timer ITU: supervision timer during MTP restart Min Max Def ------ ------ ------ ANSI 480000 600000 540000 ITU 67000 69000 68000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(67000, 600000)

class CItpTcTimerMtp3T20(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: waiting to repeat local inhibit test ITU: MTP restart timer at the Signalling point Min Max Def ------ ------ ------ ANSI 90000 120000 105000 ITU 1000 61000 60000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 120000)

class CItpTcTimerMtp3T21(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: waiting to repeat remote inhibit test) ITU: MTP restart timer at adjacent Signalling point Min Max Def ------ ------ ------ ANSI 90000 120000 105000 ITU 63000 65000 64000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(63000, 120000)

class CItpTcTimerMtp3T22(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: restarting SP waiting for Signalling links avail ITU: local inhibit test timer Min Max Def ------ ------ ------ ANSI 36000 60000 30000 ITU 80000 360000 300000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(36000, 360000)

class CItpTcTimerMtp3T23(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: restarting SP waiting to receive all TRA msgs ITU: remote inhibit test timer Min Max Def ------ ------ ------ ANSI 9000 60000 30000 ITU 80000 360000 300000 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(9000, 360000)

class CItpTcTimerMtp3T24(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the variant. ANSI: restarting SP waiting to broadcast all TRA msgs ITU: stabilizing timer after local processor outage Min Max Def ------ ------ ------ ANSI 9000 60000 30000 ITU 500 500 500 The SYNTAX statement allows values for both the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 60000)

class CItpTcTimerMtp3T25(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer at Signalling Point (SP) adjacent to restarting SP, waiting for traffic restart allowed message. Ranges by variant. Min Max Def ------ ------ ------ ANSI 30000 35000 30000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30000, 35000), )
class CItpTcTimerMtp3T26(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer at restarting SP waiting to repeat traffic restart waiting message. Ranges by variant. Min Max Def ------ ------ ------ ANSI 12000 15000 12000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(12000, 15000), )
class CItpTcTimerMtp3T27(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Minimum duration of unavailability for full restart. Ranges by variant. Min Max Def ------ ------ ------ ANSI 2000 50000 4000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 50000), )
class CItpTcTimerMtp3T28(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer at SP adjacent to restarting SP waiting for traffic restart waiting message. Ranges by variant. Min Max Def ------ ------ ------ ANSI 3000 35000 30000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3000, 35000), )
class CItpTcTimerMtp3T29(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer started when TRA sent in response to unexpected TRA or TRW. Ranges by variant. Min Max Def ------ ------ ------ ANSI 60000 65000 63000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60000, 65000), )
class CItpTcTimerMtp3T30(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer to limit sending of TFPs and TFRs in response to unexpected TRA or TRW. Ranges by variant. Min Max Def ------ ------ ------ ANSI 30000 35000 33000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30000, 35000), )
class CItpTcTimerMtp3T31(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'False link congestion detection timer. Ranges by variant. Min Max Def ------ ------ ------ ANSI 10000 120000 60000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10000, 120000), )
class CItpTcTimerMtp3T32(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Link oscillation timer - Procedure A. Ranges by variant. Min Max Def ------ ------ ------ ANSI 5000 120000 60000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 120000), )
class CItpTcTimerMtp3T33(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Probation timer for link oscillation - Procedure B. Ranges by variant. Min Max Def ------ ------ ------ ANSI 60000 600000 300000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60000, 600000), )
class CItpTcTimerMtp3T34(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Suspension timer for link oscillation - Procedure B. Ranges by variant. Min Max Def ------ ------ ------ ANSI 5000 120000 60000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 120000), )
class CItpTcTimerLinkTest(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Signalling Link test acknowledgement timer. Min Max Def ------ ------ ------ ANSI 4000 12000 8000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4000, 12000), )
class CItpTcTimerLinkMessage(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Interval timer for sending test messages. Min Max Def ------ ------ ------ ANSI 30000 90000 60000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30000, 90000), )
class CItpTcTimerLinkActRetry(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages. ANSI T1.111 Telecommunications - Signalling system No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Link activation retry timer. Min Max Def ------ ------ ------ ANSI 60000 90000 60000 This timer is not used when the variant is ITU. A value of zero indicates a value is not defined for a particular variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60000, 90000), )
class CItpTcTranslationType(TextualConvention, Integer32):
    description = "The Translation Type for SCCP GTT GTA specifies Title Translation or Subsystem Number (SSN) 'tt' : The GTT GTA has specified Title Translation 'ssn' : The GTT GTA has specified Subsystem Number."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tt", 1), ("ssn", 2))

class CItpTcURL(TextualConvention, OctetString):
    description = 'The URL used to load a configuration file. An octet string specified by an administrator that must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CItpTcXuaName(TextualConvention, OctetString):
    description = 'The configured name associated with M3UA/SUA ASP or AS name. An octet string specified by an administrator that must be in human-readable form. The names must conform to the allowed characters that can be specified via Command Line Interface(CLI). The names cannot contain control character and should not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

mibBuilder.exportSymbols("CISCO-ITP-TC-MIB", CItpTcTimerMtp3T15=CItpTcTimerMtp3T15, CItpTcLinksetId=CItpTcLinksetId, CItpTcGtaDisplay=CItpTcGtaDisplay, CItpTcTimerMtp3T24=CItpTcTimerMtp3T24, CItpTcSs7Variant=CItpTcSs7Variant, CItpTcPointCode=CItpTcPointCode, CItpTcTimerLinkMessage=CItpTcTimerLinkMessage, CItpTcTimerMtp3T23=CItpTcTimerMtp3T23, CItpTcServiceIndicator=CItpTcServiceIndicator, CItpTcTimerMtp3T25=CItpTcTimerMtp3T25, CItpTcTableLoadStatus=CItpTcTableLoadStatus, CItpTcTimerMtp3T07=CItpTcTimerMtp3T07, CItpTcTimerMtp3T02=CItpTcTimerMtp3T02, CItpTcSls=CItpTcSls, CItpTcPointCodeType=CItpTcPointCodeType, CItpTcTimerLinkActRetry=CItpTcTimerLinkActRetry, CItpTcTimerMtp3T21=CItpTcTimerMtp3T21, CItpTcGlobalTitleSelector=CItpTcGlobalTitleSelector, CItpTcTimerMtp3T08=CItpTcTimerMtp3T08, CItpTcTimerMtp3T28=CItpTcTimerMtp3T28, CItpTcTimerMtp3T05=CItpTcTimerMtp3T05, CItpTcTimerMtp3T16=CItpTcTimerMtp3T16, ciscoItpTextualConventions=ciscoItpTextualConventions, CItpTcNAI=CItpTcNAI, CItpTcInstanceNumber=CItpTcInstanceNumber, PYSNMP_MODULE_ID=ciscoItpTextualConventions, CItpTcGtaDisplayLen=CItpTcGtaDisplayLen, CItpTcTimerMtp2T07=CItpTcTimerMtp2T07, CItpTcTimerMtp3T01=CItpTcTimerMtp3T01, CItpTcTimerMtp3T18=CItpTcTimerMtp3T18, CItpTcNumberingPlan=CItpTcNumberingPlan, CItpTcTimerMtp3T26=CItpTcTimerMtp3T26, CItpTcTimerMtp3T29=CItpTcTimerMtp3T29, CItpTcTimerMtp3T33=CItpTcTimerMtp3T33, CItpTcTimerMtp2T04E=CItpTcTimerMtp2T04E, CItpTcRouteTableName=CItpTcRouteTableName, CItpTcSubSystemNumberMask=CItpTcSubSystemNumberMask, CItpTcGlobalTitleSelectorName=CItpTcGlobalTitleSelectorName, CItpTcTimerMtp3T17=CItpTcTimerMtp3T17, CItpTcGtaDisplayZB=CItpTcGtaDisplayZB, CItpTcTimerMtp3T31=CItpTcTimerMtp3T31, CItpTcLinkSLC=CItpTcLinkSLC, CItpTcTimerMtp3T03=CItpTcTimerMtp3T03, CItpTcSubSystemNumber=CItpTcSubSystemNumber, CItpTcTimerMtp3T30=CItpTcTimerMtp3T30, CItpTcTimerMtp2T04N=CItpTcTimerMtp2T04N, CItpTcTimerMtp3T20=CItpTcTimerMtp3T20, CItpTcTimerMtp3T34=CItpTcTimerMtp3T34, CItpTcPointCodeMask=CItpTcPointCodeMask, CItpTcTimerMtp3T06=CItpTcTimerMtp3T06, CItpTcAclId=CItpTcAclId, CItpTcTimerMtp3T10=CItpTcTimerMtp3T10, CItpTcGtaLongDisplay=CItpTcGtaLongDisplay, CItpTcEncodingSchemeValue=CItpTcEncodingSchemeValue, CItpTcXuaName=CItpTcXuaName, CItpTcTimerMtp2T03=CItpTcTimerMtp2T03, CItpTcLinkType=CItpTcLinkType, CItpTcTimerMtp3T19=CItpTcTimerMtp3T19, CItpTcNetworkIndicator=CItpTcNetworkIndicator, CItpTcTimerMtp3T32=CItpTcTimerMtp3T32, CItpTcTimerMtp2T01=CItpTcTimerMtp2T01, CItpTcDisplayPC=CItpTcDisplayPC, CItpTcCLLI=CItpTcCLLI, CItpTcTimerMtp3T22=CItpTcTimerMtp3T22, CItpTcTimerMtp3T27=CItpTcTimerMtp3T27, CItpTcGtaLongAddr=CItpTcGtaLongAddr, CItpTcTimerMtp2T06=CItpTcTimerMtp2T06, CItpTcNetworkName=CItpTcNetworkName, CItpTcGtaLongDisplayLen=CItpTcGtaLongDisplayLen, CItpTcTranslationType=CItpTcTranslationType, CItpTcTimerLinkTest=CItpTcTimerLinkTest, CItpTcTimerMtp3T11=CItpTcTimerMtp3T11, CItpTcTimerMtp2T02=CItpTcTimerMtp2T02, CItpTcGtaAddr=CItpTcGtaAddr, CItpTcTimerMtp2T05=CItpTcTimerMtp2T05, CItpTcURL=CItpTcURL, CItpTcTimerMtp3T04=CItpTcTimerMtp3T04, CItpTcQos=CItpTcQos, CItpTcTimerMtp3T12=CItpTcTimerMtp3T12, CItpTcTimerMtp3T13=CItpTcTimerMtp3T13, CItpTcTimerMtp3T14=CItpTcTimerMtp3T14)
