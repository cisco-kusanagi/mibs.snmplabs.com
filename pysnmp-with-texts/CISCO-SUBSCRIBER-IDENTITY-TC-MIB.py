#
# PySNMP MIB module CISCO-SUBSCRIBER-IDENTITY-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SUBSCRIBER-IDENTITY-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Unsigned32, Gauge32, IpAddress, ObjectIdentity, Counter64, iso, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "iso", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSubscriberIdentityTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 782))
ciscoSubscriberIdentityTcMIB.setRevisions(('2011-12-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setLastUpdated('201112230000Z')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setDescription('This MIB module defines textual conventions describing subscriber session identities. A subscriber session identity consists of data associated with a subscriber session serving as credentials used to determine authority, status, rights, or entitlement to privileges.')
class SubSessionIdentity(TextualConvention, Integer32):
    description = "An enumerated integer-value describing a subscriber session identity: 'other' The implementation of the MIB module using this textual convention does not recognize the subscriber session identity. 'ifIndex' The ifIndex assigned to the interface representing the subscriber session. 'subscriberLabel' The arbitrary integer-value assigned by the system to uniquely identify the subscriber session within the scope of the system. 'macAddress' The subscriber's MAC address. 'nativeVrf' The name of the VRF on which the subscriber session originates. 'nativeIpAddress' The IP address assigned to the subscriber session on the customer-facing side of the system. 'domainVrf' The name of the VRF to which the system transfers the subscriber session traffic. 'domainIpAddress' The IP address assigned to the subscriber session on the service-facing side of the system. 'pbhk' The Port-Bundle Host Key (PBHK) uniquely identifying the subscriber session. A PBHK consists of a source IP address and a TCP port number. 'remoteId' The name identifying the 'calling station', access multiplexor, or access switch providing access to the subscriber. 'circuitId' The name identifying the circuit on the 'calling station', access multiplexor, or access switch that provides access to the subscriber. 'nasPort' An octet string identifying the port on the Network Access Server (NAS) that provides access to the subscriber. 'domain' The subscriber's domain name. 'username' The subscriber's username. 'acctSessionId' The subscriber's accounting session identifier. 'dnis' The Dialed Number Identification Service (DNIS) number (or called-party number) dialed by the subscriber. 'media' The type of media providing access to the subscriber. 'mlpNegotiated' Indicates whether the subscriber session was established using multi-link PPP negotiation. 'protocol' The type of protocol providing access to the subscriber. 'dhcpClass' The name of the class matching the DHCP DISCOVER message received from the subscriber. 'serviceName' The name identifying the service associated with the subscriber. 'tunnelName' The name of the VPDN used to carry the subscriber session."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("ifIndex", 2), ("subscriberLabel", 3), ("macAddress", 4), ("nativeVrf", 5), ("nativeIpAddress", 6), ("domainVrf", 7), ("domainIpAddress", 8), ("pbhk", 9), ("remoteId", 10), ("circuitId", 11), ("nasPort", 12), ("domain", 13), ("username", 14), ("acctSessionId", 15), ("dnis", 16), ("media", 17), ("mlpNegotiated", 18), ("protocol", 19), ("serviceName", 20), ("dhcpClass", 21), ("tunnelName", 22))

class SubSessionIdentities(TextualConvention, Bits):
    description = "A bit string describing a set of subscriber session identities: 'ifIndex' The ifIndex assigned to the interface representing the subscriber session. 'subscriberLabel' The arbitrary integer-value assigned by the system to uniquely identify the subscriber session within the scope of the system. 'macAddress' The subscriber's MAC address. 'nativeVrf' The name of the VRF on which the subscriber session originates. 'nativeIpAddress' The IP address assigned to the subscriber session on the customer-facing side of the system. 'domainVrf' The name of the VRF to which the system transfers the subscriber session traffic. 'domainIpAddress' The IP address assigned to the subscriber session on the service-facing side of the system. 'pbhk' The Port-Bundle Host Key (PBHK) uniquely identifying the subscriber session. A PBHK consists of a source IP address and a TCP port number. 'remoteId' The name identifying the 'calling station' or access multiplexor providing access to the subscriber. 'circuitId' The name identifying the circuit on the 'calling station', access multiplexor, or access switch that provides access to the subscriber. 'nasPort' An octet string identifying the port on the Network Access Server (NAS) that provides access to the subscriber. 'domain' The subscriber's domain name. 'username' The subscriber's username. 'dnis' The Dialed Number Identification Service (DNIS) number (or called-party number) dialed by the subscriber. 'acctSessionId' The subscriber's accounting session identifier. 'media' The type of media providing access to the subscriber. 'mlpNegotiated' Indicates whether the subscriber session was established using multi-link PPP negotiation. 'protocol' The type of protocol providing access to the subscriber. 'serviceName' The name identifying the service associated with the subscriber. 'dhcpClass' The name of the class matching the DHCP DISCOVER message received from the subscriber. 'tunnelName' The name of the VPDN used to carry the subscriber session."
    status = 'current'
    namedValues = NamedValues(("ifIndex", 0), ("subscriberLabel", 1), ("macAddress", 2), ("nativeVrf", 3), ("nativeIpAddress", 4), ("domainVrf", 5), ("domainIpAddress", 6), ("pbhk", 7), ("remoteId", 8), ("circuitId", 9), ("nasPort", 10), ("domain", 11), ("username", 12), ("acctSessionId", 13), ("dnis", 14), ("media", 15), ("mlpNegotiated", 16), ("protocol", 17), ("serviceName", 18), ("dhcpClass", 19), ("tunnelName", 20))

class SubscriberLabel(TextualConvention, Unsigned32):
    description = "A positive integer-value uniquely identifying a subscriber session within the scope of a system. The value '0' is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberVRF(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value identifying a VRF associated with a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberPbhk(TextualConvention, OctetString):
    description = "An octet string specifying a Port-Bundle Host Key (PBHK) identifying a subscriber. The octet string has the following format: Octets Field ------------------------------ 1-4 subscriber IP address 5-6 TCP port number Observe that the subscriber IP address is always an IPv4 address. The value '000000'H is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class SubscriberRemoteId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = "A string-value identifying the 'calling station', access multiplexor, or access switch providing access to a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberCircuitId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = "A string-value identifying the circuit on the 'calling station', access multiplexor, or access switch that provides access to the subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberNasPort(TextualConvention, OctetString):
    description = "An octet string identifying port on the Network Access Server (NAS) that provides access to the subscriber. The value '000000'H is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SubscriberDomain(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the domain associated with a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberUsername(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the username identifying a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberAcctSessionId(TextualConvention, Unsigned32):
    description = "An positive, integer-value specifying the accounting session ID assigned to a subscriber. The value '0' is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberDnis(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the Dialed Number Identification Service (DNIS) number (or called-party number) dialed by a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberMediaType(TextualConvention, Integer32):
    description = "An enumerated integer-value describing the type of media providing access to the subscriber: 'other' The implementation of the MIB module using this textual convention does not recognize the type of media providing access to the subscriber. 'async' An asynchronous serial line provides access to the subscriber. 'atm' An ATM network provides access to the subscriber. 'ethernet' An Ethernet-based network provides access to the subscriber. 'ip' An IP network provides access to the subscriber. 'isdn' An ISDN line provides access to the subscriber. 'mpls' An MPLS network provides access to the subscriber. 'sync' A synchronous serial line provides access to the subscriber. The value 'other' cannot be written to an instance of an object. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("async", 2), ("atm", 3), ("ethernet", 4), ("ip", 5), ("isdn", 6), ("mpls", 7), ("sync", 8))

class SubscriberProtocolType(TextualConvention, Integer32):
    description = "An enumerated integer-value describing the type of protocol providing access to the subscriber: 'other' The implementation of the MIB module using this textual convention does not recognize the type of protocol providing access to the subscriber. 'atom' Any Transport over MPLS (AToM) provides access to the subscriber. 'ip' The Internet Protocol (IP) provides access to the subscriber. 'psdn' A Public Switched Data Network (PSDN) provides access to the subscriber. 'ppp' The Point-to-Point Protocol (PPP) provides access to the subscriber. 'vpdn' A Virtual Private Data Network (VPDN) provides access to the subscriber. The value 'other' cannot be written to an instance of an object. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("atom", 2), ("ip", 3), ("psdn", 4), ("ppp", 5), ("vpdn", 6))

class SubscriberDhcpClass(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the name of the class matching the DHCP DISCOVER message received from the subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberTunnelName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = "A string-value specifying the name of the VPDN used to carry a subscriber's session. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberLocationName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the location associated with a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberServiceName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the subscriber service associated with a subscriber. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB (RFC-3411). The null string is not a valid value. However, it serves as a convenient value when an instance of an object using this textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-SUBSCRIBER-IDENTITY-TC-MIB", SubscriberAcctSessionId=SubscriberAcctSessionId, SubscriberLabel=SubscriberLabel, SubscriberProtocolType=SubscriberProtocolType, SubscriberCircuitId=SubscriberCircuitId, SubscriberRemoteId=SubscriberRemoteId, SubscriberDomain=SubscriberDomain, SubscriberTunnelName=SubscriberTunnelName, SubscriberServiceName=SubscriberServiceName, SubscriberLocationName=SubscriberLocationName, SubSessionIdentity=SubSessionIdentity, SubSessionIdentities=SubSessionIdentities, SubscriberVRF=SubscriberVRF, SubscriberDhcpClass=SubscriberDhcpClass, ciscoSubscriberIdentityTcMIB=ciscoSubscriberIdentityTcMIB, SubscriberMediaType=SubscriberMediaType, SubscriberNasPort=SubscriberNasPort, SubscriberDnis=SubscriberDnis, PYSNMP_MODULE_ID=ciscoSubscriberIdentityTcMIB, SubscriberUsername=SubscriberUsername, SubscriberPbhk=SubscriberPbhk)
