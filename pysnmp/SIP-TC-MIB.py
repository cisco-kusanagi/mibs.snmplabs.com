#
# PySNMP MIB module SIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, ModuleIdentity, iso, Counter32, ObjectIdentity, MibIdentifier, mib_2, TimeTicks, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "ModuleIdentity", "iso", "Counter32", "ObjectIdentity", "MibIdentifier", "mib-2", "TimeTicks", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 148))
sipTC.setRevisions(('2007-04-20 00:00',))
if mibBuilder.loadTexts: sipTC.setLastUpdated('200704200000Z')
if mibBuilder.loadTexts: sipTC.setOrganization('IETF Session Initiation Protocol Working Group')
class SipTCTransportProtocol(TextualConvention, Bits):
    reference = 'RFC 3261, Section 18 and RFC 4168'
    status = 'current'
    namedValues = NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5))

class SipTCEntityRole(TextualConvention, Bits):
    reference = 'RFC 3261, Section 6'
    status = 'current'
    namedValues = NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4))

class SipTCOptionTagHeaders(TextualConvention, Bits):
    reference = 'RFC 3261, Sections 19.2, 20.32, 20.29, 20.37, and 20.40'
    status = 'current'
    namedValues = NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3))

class SipTCMethodName(TextualConvention, OctetString):
    reference = 'RFC 3261, Section 27.4'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 100)

mibBuilder.exportSymbols("SIP-TC-MIB", SipTCEntityRole=SipTCEntityRole, PYSNMP_MODULE_ID=sipTC, SipTCOptionTagHeaders=SipTCOptionTagHeaders, SipTCTransportProtocol=SipTCTransportProtocol, SipTCMethodName=SipTCMethodName, sipTC=sipTC)
