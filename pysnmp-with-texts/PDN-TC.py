#
# PySNMP MIB module PDN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:38:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Unsigned32, iso, IpAddress, Counter32, NotificationType, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Unsigned32", "iso", "IpAddress", "Counter32", "NotificationType", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdyn = MibIdentifier((1, 3, 6, 1, 4, 1, 1795))
class VnidMode(TextualConvention, Integer32):
    description = 'This object describes the configuration mode for VNIDs and ports. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("implicit", 1), ("explicit", 2), ("notagging", 3))

class ClientState(TextualConvention, Integer32):
    description = ' The configuration type for a client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class VnidTaggingState(TextualConvention, Integer32):
    description = ' This object indicates whether VNID tagging is activated or de-activated.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class VnidRange(TextualConvention, Integer32):
    description = ' The valid range for VNID IDs'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2, 4000)

class SwitchState(TextualConvention, Integer32):
    description = ' This object indicates whether an object state is in the enabled or disabled state '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class ResetStates(TextualConvention, Integer32):
    description = 'This object defines the enumerations of values that can be applied to the reset object'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noOp", 1), ("reset", 2), ("resetToFactoryDefaults", 3))

class ResultTypes(TextualConvention, Integer32):
    description = 'This object defines the enumerations for the result of an operation '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("success", 2), ("failure", 3), ("inProgress", 4))

class InitiatorTypes(TextualConvention, Integer32):
    description = 'This object defines the enumerations for the result of an operation '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noop", 1), ("telnet", 2), ("console", 3), ("snmp", 4))

class NTPMode(TextualConvention, Integer32):
    description = 'This object describes the mode NTP will operate in'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unicast", 1), ("broadcast", 2))

class DNSServerType(TextualConvention, Integer32):
    description = 'This object describes the DNS server Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class MibOidType(TextualConvention, Integer32):
    description = 'This Object describes the type of a mib object Scalar - Single Instance Object Table - Multi-instance Object Mib - A Mib. Section - A Section Within A MIB'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("scalar", 1), ("table", 2), ("mib", 3), ("section", 4))

class SocketType(TextualConvention, Integer32):
    description = 'This object describes the type of socket'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("stream", 2), ("datagram", 3), ("rawProtocol", 4), ("reliableMessageDelivery", 5), ("sequencedPacket", 6))

class SocketFamily(TextualConvention, Integer32):
    description = 'This object describes the socket Family'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("unknown", 1), ("unix", 2), ("darpaInternet", 3), ("darpaIMP", 4), ("pUP", 5), ("cHAOSFamily", 6), ("xeroxNovell", 7), ("nBS", 8), ("eCMA", 9), ("dATAKIT", 10), ("cCITT", 11), ("sNA", 12), ("dECnet", 13), ("directDataLinkInterface", 14), ("dECLAT", 15), ("nSCHyperChannel", 16), ("appleTalk", 17), ("netqorkInterfaceTap", 18), ("iEEE8020ISO8802", 19), ("oSI", 20), ("x25", 21), ("oSIAFI47IDI4", 22), ("uSGovermentOSI", 23))

class SocketState(TextualConvention, Integer32):
    description = 'This object describes the state of a stream socket'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("closed", 1), ("listen", 2), ("sYNSent", 3), ("sYNRCVD", 4), ("established", 5), ("closeWait", 6), ("fINWait", 7), ("closing", 8), ("lastAck", 9), ("fINWait2", 10), ("timeWait", 11))

class DomainName(DisplayString):
    description = "The domain name space is a tree structure. Each node and leaf on the tree corresponds to a resource set (which may be empty). The domain system makes no distinctions between the uses of the interior nodes and leaves, and this memo uses the term 'node' to refer to both. Each node has a label, which is zero to 63 octets in length. Brother nodes may not have the same label, although the same label can be used for nodes which are not brothers. One label is reserved, and that is the null (i.e., zero length) label used for the root. The domain name of a node is the list of the labels on the path from the node to the root of the tree. By convention, the labels that compose a domain name are printed or read left to right, from the most specific (lowest, farthest from the root) to the least specific (highest, closest to the root). Internally, programs that manipulate domain names should represent them as sequences of labels, where each label is a length octet followed by an octet string. Because all domain names end at the root, which has a null string for a label, these internal representations can use a length byte of zero to terminate a domain name. By convention, domain names can be stored with arbitrary case, but domain name comparisons for all present domain functions are done in a case-insensitive manner, assuming an ASCII character set, and a high order zero bit. This means that you are free to create a node with label 'A' or a node with label 'a', but not both as brothers; you could refer to either using 'a' or 'A'. When you receive a domain name or label, you should preserve its case. The rationale for this choice is that we may someday need to add full binary domain names for new services; existing services would not be changed. When a user needs to type a domain name, the length of each label is omitted and the labels are separated by dots ('.'). Since a complete domain name ends with the root label, this leads to a printed form which ends in a dot. We use this property to distinguish between: character string which represents a complete domain name (often called 'absolute'). For example, 'poneria.ISI.EDU.' - a character string that represents the starting labels of a domain name which is incomplete, and should be completed by local software using knowledge of the local domain (often called 'relative'). For example, 'poneria' used in the ISI.EDU domain. Relative names are either taken relative to a well known origin, or to a list of domains used as a search list. Relative names appear mostly at the user interface, where their interpretation varies from implementation to implementation, and in master files, where they are relative to a single origin domain name. The most common interpretation uses the root '.' as either the single origin or as one of the members of the search list, so a multi-label relative name is often one where the trailing dot has been omitted to save typing. To simplify implementations, the total number of octets that represent a domain name (i.e., the sum of all label octets and label lengths) is limited to 255. A domain is identified by a domain name, and consists of that part of the domain name space that is at or below the domain name which specifies the domain. A domain is a subdomain of another domain if it is contained within that domain. This relationship can be tested by seeing if the subdomain's name ends with the containing domain's name. For example, A.B.C.D is a subdomain of B.C.D, C.D, D, and '.' "
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class SnmpAdminString(TextualConvention, OctetString):
    description = 'An octet string containing administrative information, preferably in human-readable form. To facilitate internationalization, this information is represented using the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 transformation format described in [RFC2044]. Since additional code points are added by amendments to the 10646 standard from time to time, implementations must be prepared to encounter any code point from 0x00000000 to 0x7fffffff. The use of control codes should be avoided. When it is necessary to represent a newline, the control code sequence CR LF should be used. The use of leading or trailing white space should be avoided. For code points not directly supported by user interface hardware or software, an alternative means of entry and display, such as hexadecimal, may be provided. For information encoded in 7-bit US-ASCII, the UTF-8 encoding is identical to the US-ASCII encoding. Note that when this TC is used for an object that is used or envisioned to be used as an index, then a SIZE restriction must be specified so that the number of sub-identifiers for any object instance does not exceed the limit of 128, as defined by [RFC1905]. '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class InetAddressType(TextualConvention, Integer32):
    description = 'This object describes the type of address configured for a interface'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class ManagementType(TextualConvention, Integer32):
    description = 'This object is used to specify the type of management. This can be either Inband Management or OutBand Management.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inband", 1), ("outband", 2))

class IdslClockMode(TextualConvention, Integer32):
    description = 'This object indicates the network clock mode set for the secondary network clock. IDSL portcards with a port configured as an NT will be set to portCardDriveClockOnboard(4), both driving the backplane and using the clock for the other Local Timing transceivers on the card. Port cards with only LT ports configured will receive a clock from the backplane using portCardSinkClock(2). portCardDriveClock(3) will drive the backplane alone.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("triState", 1), ("portCardSinkClock", 2), ("portCardDriveClock", 3), ("portCardDriveClockOnboard", 4))

mibBuilder.exportSymbols("PDN-TC", ClientState=ClientState, SocketType=SocketType, NTPMode=NTPMode, DomainName=DomainName, SnmpAdminString=SnmpAdminString, VnidTaggingState=VnidTaggingState, InitiatorTypes=InitiatorTypes, SocketState=SocketState, IdslClockMode=IdslClockMode, InetAddressType=InetAddressType, VnidMode=VnidMode, SwitchState=SwitchState, pdyn=pdyn, VnidRange=VnidRange, ResetStates=ResetStates, ManagementType=ManagementType, ResultTypes=ResultTypes, DNSServerType=DNSServerType, SocketFamily=SocketFamily, MibOidType=MibOidType)
