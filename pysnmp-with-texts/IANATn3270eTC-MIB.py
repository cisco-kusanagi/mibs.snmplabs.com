#
# PySNMP MIB module IANATn3270eTC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANATn3270eTC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, ModuleIdentity, Integer32, mib_2, Counter32, Counter64, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, MibIdentifier, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "mib-2", "Counter32", "Counter64", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "MibIdentifier", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaTn3270eTcMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 61))
ianaTn3270eTcMib.setRevisions(('2014-05-22 00:00', '2000-05-10 00:00', '1999-09-01 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaTn3270eTcMib.setRevisionsDescriptions(('Updated ICANN contact info.', 'Fix to import mib-2 instead of experimental.', 'Initial version transferred from the TN3270E working group to IANA.',))
if mibBuilder.loadTexts: ianaTn3270eTcMib.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaTn3270eTcMib.setOrganization('IANA')
if mibBuilder.loadTexts: ianaTn3270eTcMib.setContactInfo('Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Tel: +1 310-301-5800 E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaTn3270eTcMib.setDescription('This module defines a set of textual conventions for use by the TN3270E-MIB and the TN3270E-RT-MIB. Any additions or changes to the contents of this MIB module must first be discussed on the tn3270e working group list at: tn3270e&list.nih.gov and approved by one of the following TN3270E working group contacts: Ed Bailey (co-chair) - elbailey&us.ibm.com Michael Boe (co-chair) - mboe&cisco.com Ken White - kennethw&vnet.ibm.com Robert Moore - remoore&us.ibm.com The above list of contacts can be altered with the approval of the two co-chairs. The Textual Conventions defined within this MIB have no security issues associated with them unless explicitly stated in their corresponding DESCRIPTION clause.')
class IANATn3270eAddrType(TextualConvention, Integer32):
    description = 'The textual convention for defining the type of a client address. The enumeration value unknown(0) is also used to indicate that no actual address is present.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2))

class IANATn3270eAddress(TextualConvention, OctetString):
    description = 'Denotes a client address. The type of client address is determined by use of the IANATn3270eAddrType textual convention. The length in octets of a IANATn3270eAddress object is: IANATn3270eAddrType Address Length +++++++++++++++++++ ++++++++++++++ unknown(0) not specified or unknown; the actual length of the IANATn3270eAddress octet string indicates if an address is present ipv4(1) 4 OCTETS ipv6(2) 16 OCTETS This textual convention is similar to the TAddress TC defined by RFC1903 except that it allows a zero-length octet string and is not a full transport layer address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IANATn3270eClientType(TextualConvention, Integer32):
    description = "The textual convention for defining the set of enumerations used by tn3270eTcpConnClientIdFormat in the TN3270E-MIB: ENUMERATION OCTETs DESCRIPTION none(1) 0 Not specified other(2) 1..512 Implementation specific ipv4(3) 6 4-octet IP Address plus 2-octet TCP Port ipv6(4) 18 16-octet IPv6 Address plus 2-octet TCP Port domainName(5) 1..512 The DNS name of a client. truncDomainName(6) 1..512 The (truncated) DNS name of a client. string(7) 1..512 Unknown Utf8String certificate(8) 1..512 certificate userId(9) 1..8 Client's userid x509dn(10) 1..512 X.509 Distinguished Name Representation of a certificate(8) may be lead to a security exposure and is NOT RECOMMENDED without adequate security."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 1), ("other", 2), ("ipv4", 3), ("ipv6", 4), ("domainName", 5), ("truncDomainName", 6), ("string", 7), ("certificate", 8), ("userId", 9), ("x509dn", 10))

class IANATn3270Functions(TextualConvention, Bits):
    description = "This textual convention reflects the current set of TN3270 and TN3270E functions that can be negotiated between a server and its client: RFC856 transmitBinary The sender of this command REQUESTS permission to begin transmitting, or confirms that it will now begin transmitting characters which are to be interpreted as 8 bits of binary data by the receiver of the data. RFC860 timingMark The sender of this command REQUESTS that the receiver of this command return a WILL TIMING-MARK in the data stream at the 'appropriate place'. RFC885 endOfRecord The sender of this command requests permission to begin transmission of the Telnet END-OF-RECORD (EOR) code when transmitting data characters, or the sender of this command confirms it will now begin transmission of EORs with transmitted data characters. RFC1091 terminalType Sender is willing to send terminal type information in a subsequent sub-negotiation. RFC1041 tn3270Regime Sender is willing to send list of supported 3270 Regimes in a subsequent sub-negotiation. RFC2355 scsCtlCodes (Printer sessions only). Allows the use of the SNA Character Stream (SCS) and SCS control codes on the session. SCS is used with LU type 1 SNA sessions. dataStreamCtl (Printer sessions only). Allows the use of the standard 3270 data stream. This corresponds to LU type 3 SNA sessions. responses Provides support for positive and negative response handling. Allows the server to reflect to the client any and all definite, exception, and no response requests sent by the host application. bindImage Allows the server to send the SNA Bind image and Unbind notification to the client. sysreq Allows the client and server to emulate some (or all, depending on the server) of the functions of the SYSREQ key in an SNA environment."
    status = 'current'
    namedValues = NamedValues(("transmitBinary", 0), ("timemark", 1), ("endOfRecord", 2), ("terminalType", 3), ("tn3270Regime", 4), ("scsCtlCodes", 5), ("dataStreamCtl", 6), ("responses", 7), ("bindImage", 8), ("sysreq", 9))

class IANATn3270ResourceType(TextualConvention, Integer32):
    description = 'The type of resource defined by a resource pool. Refer to tn3270eResPoolTable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("terminal", 2), ("printer", 3), ("terminalOrPrinter", 4))

class IANATn3270DeviceType(TextualConvention, Integer32):
    description = 'This textual convention defines the list of device types that can be set, as defined by RFC 2355.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100))
    namedValues = NamedValues(("ibm3278d2", 1), ("ibm3278d2E", 2), ("ibm3278d3", 3), ("ibm3278d3E", 4), ("ibm3278d4", 5), ("ibm3278d4E", 6), ("ibm3278d5", 7), ("ibm3278d5E", 8), ("ibmDynamic", 9), ("ibm3287d1", 10), ("unknown", 100))

class IANATn3270eLogData(TextualConvention, OctetString):
    description = "An octet string representing log data as pertaining to either a TN3270 or TN3270E Session as reported from a TN3270E Server. Log data is stored in an octet string in time order (from earliest to latest). Each log element has the following form: +------+----+---------+------------+ !length!type!TimeStamp! data ! +------+----+---------+------------+ where length = one-octet length of the data portion of the trace element, not including the length, type, and TimeStamp fields type = one-octet code point characterizing the data. TimeStamp = A 4-octet field representing the number of TimeTicks since the TN3270E server was last activated. The server's last activation time is available in the tn3270eSrvrConfLastActTime object in the TN3270E MIB, which has the syntax DateAndTime. data = initial part of a PDU. length type 0-255 x'00' - unknown 0 x'01' - inactivity timer expired 0 x'02' - dynamic timer expired 0 x'03' - actlu req 0 x'04' - bind req 0 x'05' - clear req 0 x'06' - dactlu req 0 x'07' - warm actpu req 0 x'08' - sdt req 0 x'09' - unbind req 0 x'0A' - notify resp 0 x'0B' - reply PSID neg rsp 0 x'0C' - reply PSID pos rsp 0 x'0D' - unbind rsp 0 x'0E' - hierarchical reset 0 x'0F' - client connect req 0 x'10' - client disconnect req 0 x'11' - timingmark received 0 x'12' - flowControl timer expired 0 x'13' - neg rsp to host 0 x'14' - neg rsp from host 0 x'15' - data contention 0 x'16' - no buffer to send SNA data 0 x'17' - receive response while inbound 0 x'18' - client protocol error 0 x'19' - badClientSequenceReceived 1-255 x'1A' - utf8String 2 x'1B' - hexCode, implementation dependent Log element entries have a minimum length of 6 octets. The zero-length string indicates that no log data is available."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(6, 2048), )
mibBuilder.exportSymbols("IANATn3270eTC-MIB", IANATn3270ResourceType=IANATn3270ResourceType, IANATn3270eAddrType=IANATn3270eAddrType, IANATn3270eClientType=IANATn3270eClientType, IANATn3270eAddress=IANATn3270eAddress, IANATn3270Functions=IANATn3270Functions, ianaTn3270eTcMib=ianaTn3270eTcMib, IANATn3270eLogData=IANATn3270eLogData, PYSNMP_MODULE_ID=ianaTn3270eTcMib, IANATn3270DeviceType=IANATn3270DeviceType)
