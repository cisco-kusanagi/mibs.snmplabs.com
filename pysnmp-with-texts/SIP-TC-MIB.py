#
# PySNMP MIB module SIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:04:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, IpAddress, TimeTicks, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Unsigned32, ObjectIdentity, MibIdentifier, Counter64, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "IpAddress", "TimeTicks", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter64", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 148))
sipTC.setRevisions(('2007-04-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sipTC.setRevisionsDescriptions(('Initial version of the IETF SIP-TC-MIB module. This version published as part of RFC 4780.',))
if mibBuilder.loadTexts: sipTC.setLastUpdated('200704200000Z')
if mibBuilder.loadTexts: sipTC.setOrganization('IETF Session Initiation Protocol Working Group')
if mibBuilder.loadTexts: sipTC.setContactInfo('SIP WG email: sip@ietf.org Co-editor Kevin Lingle Cisco Systems, Inc. postal: 7025 Kit Creek Road P.O. Box 14987 Research Triangle Park, NC 27709 USA email: klingle@cisco.com phone: +1 919 476 2029 Co-editor Joon Maeng email: jmaeng@austin.rr.com Co-editor Jean-Francois Mule CableLabs postal: 858 Coal Creek Circle Louisville, CO 80027 USA email: jf.mule@cablelabs.com phone: +1 303 661 9100 Co-editor Dave Walker email: drwalker@rogers.com')
if mibBuilder.loadTexts: sipTC.setDescription('Session Initiation Protocol (SIP) MIB TEXTUAL-CONVENTION module used by other SIP-related MIB Modules. Copyright (C) The IETF Trust (2007). This version of this MIB module is part of RFC 4780; see the RFC itself for full legal notices.')
class SipTCTransportProtocol(TextualConvention, Bits):
    reference = 'RFC 3261, Section 18 and RFC 4168'
    description = 'This convention is a bit map. Each bit represents a transport protocol. If a bit has value 1, then that selected transport protocol is in some way dependent on the context of the object using this convention. If a bit has value 0, then that transport protocol is not selected. Combinations of bits can be set when multiple transport protocols are selected. bit 0: a protocol other than those defined here bit 1: User Datagram Protocol bit 2: Transmission Control Protocol bit 3: Stream Control Transmission Protocol bit 4: Transport Layer Security Protocol over TCP bit 5: Transport Layer Security Protocol over SCTP '
    status = 'current'
    namedValues = NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5))

class SipTCEntityRole(TextualConvention, Bits):
    reference = 'RFC 3261, Section 6'
    description = "This convention defines the role of a SIP entity. Examples of SIP entities are proxies, user agents, redirect servers, registrars, or combinations of the above. User Agent (UA): A logical entity that can act as both a user agent client and user agent server. User Agent Client (UAC): A logical entity that creates a new request, and then uses the client transaction state machinery to send it. The role of UAC lasts only for the duration of that transaction. In other words, if a piece of software initiates a request, it acts as a UAC for the duration of that transaction. If it receives a request later, it assumes the role of a user agent server for the processing of that transaction. User Agent Server (UAS): A logical entity that generates a response to a SIP request. The response accepts, rejects, or redirects the request. This role lasts only for the duration of that transaction. In other words, if a piece of software responds to a request, it acts as a UAS for the duration of that transaction. If it generates a request later, it assumes the role of a user agent client for the processing of that transaction. Proxy, Proxy Server: An intermediary entity that acts as both a server and a client for the purpose of making requests on behalf of other clients. A proxy server primarily plays the role of routing, which means its job is to ensure that a request is sent to another entity 'closer' to the targeted user. Proxies are also useful for enforcing policy. A proxy interprets and, if necessary, rewrites specific parts of a request message before forwarding it. Redirect Server: A redirect server is a user agent server that generates 3xx responses to requests it receives, directing the client to contact an alternate set of URIs. Registrar: A registrar is a server that accepts REGISTER requests and places the information it receives in those requests into the location service for the domain it handles."
    status = 'current'
    namedValues = NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4))

class SipTCOptionTagHeaders(TextualConvention, Bits):
    reference = 'RFC 3261, Sections 19.2, 20.32, 20.29, 20.37, and 20.40'
    description = 'This convention defines the header fields that use the option tags per Section 19.2 of RFC 3261. These tags are used in Require (Section 20.32), Proxy-Require (Section 20.29), Supported (Section 20.37), and Unsupported (Section 20.40) header fields.'
    status = 'current'
    namedValues = NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3))

class SipTCMethodName(TextualConvention, OctetString):
    reference = 'RFC 3261, Section 27.4'
    description = 'This TEXTUAL-CONVENTION is a string that uniquely identifies a SIP method. The scope of uniqueness is the context of all defined SIP methods. Experimental support of extension methods is acceptable and expected. Extension methods are those defined in officially sanctioned by IANA. To support experimental extension methods, any object using this TEXTUAL-CONVENTION as syntax MAY return/accept a method identifier value other than those sanctioned by IANA. That system MUST ensure no collisions with officially assigned method names.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 100)

mibBuilder.exportSymbols("SIP-TC-MIB", PYSNMP_MODULE_ID=sipTC, SipTCOptionTagHeaders=SipTCOptionTagHeaders, SipTCEntityRole=SipTCEntityRole, SipTCTransportProtocol=SipTCTransportProtocol, SipTCMethodName=SipTCMethodName, sipTC=sipTC)
