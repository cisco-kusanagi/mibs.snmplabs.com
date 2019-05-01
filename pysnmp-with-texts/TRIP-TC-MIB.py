#
# PySNMP MIB module TRIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRIP-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Unsigned32, Counter32, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, mib_2, ObjectIdentity, ModuleIdentity, Gauge32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Unsigned32", "Counter32", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "mib-2", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tripTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 115))
tripTC.setRevisions(('2004-09-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tripTC.setRevisionsDescriptions(('The initial version, Published as RFC 3872.',))
if mibBuilder.loadTexts: tripTC.setLastUpdated('200409020000Z')
if mibBuilder.loadTexts: tripTC.setOrganization('IETF IPTel Working Group. Mailing list: iptel@lists.bell-labs.com')
if mibBuilder.loadTexts: tripTC.setContactInfo('Co-editor David Zinman postal: 265 Ridley Blvd. Toronto ON, M5M 4N8 Canada email: dzinman@rogers.com phone: +1 416 433 4298 Co-editor: David Walker Sedna Wireless Inc. postal: 495 March Road, Suite 500 Ottawa, ON K2K 3G1 Canada email: david.walker@sedna-wireless.com phone: +1 613 878 8142 Co-editor Jianping Jiang Syndesis Limited postal: 30 Fulton Way Richmond Hill, ON L4B 1J5 Canada email: jjiang@syndesis.com phone: +1 905 886-7818 x2515 ')
if mibBuilder.loadTexts: tripTC.setDescription('Initial version of TRIP (Telephony Routing Over IP) MIB Textual Conventions module used by other TRIP-related MIB Modules. Copyright (C) The Internet Society (2004). This version of this MIB module is part of RFC 3872, see the RFC itself for full legal notices.')
class TripItad(TextualConvention, Unsigned32):
    description = 'The values for identifying the IP Telephony Administrative Domain (ITAD).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripId(TextualConvention, Unsigned32):
    description = 'The TRIP Identifier uniquely identifies a LS within its ITAD. It is a 4 octet unsigned integer that may, but not necessarily, represent the IPv4 address of a Location Server. Where bytes 1-4 of the Unsigned32 represent 1-4 bytes of the IPv4 address in network-byte order. For an IPv6 network, TripId will not represent the IPv6 address.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripAddressFamily(TextualConvention, Integer32):
    description = 'A type of address for a TRIP route. Address families defined within this MIB module are: Code Address Family 1 Decimal Routing Numbers 2 PentaDecimal Routing Numbers 3 E.164 Numbers 255 An other type of address family'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))
    namedValues = NamedValues(("decimal", 1), ("pentadecimal", 2), ("e164", 3), ("other", 255))

class TripAppProtocol(TextualConvention, Integer32):
    description = 'The application protocol used for communication with TRIP Location Servers. Protocols defined in this MIB Module are: Code Protocol 1 SIP 2 H.323-H.225.0-Q.931 3 H.323-H.225.0-RAS 4 H.323-H.225.0-Annex-G 255 An other type of application protocol'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))
    namedValues = NamedValues(("sip", 1), ("q931", 2), ("ras", 3), ("annexG", 4), ("other", 255))

class TripCommunityId(TextualConvention, Unsigned32):
    description = 'The range of legal values for a TRIP Community Identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripProtocolVersion(TextualConvention, Integer32):
    description = 'The version number of the TRIP protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class TripSendReceiveMode(TextualConvention, Integer32):
    description = 'The operational mode of the TRIP application. Possible values are: 1 - Send Receive mode 2 - Send only mode 3 - Receive Only mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sendReceive", 1), ("sendOnly", 2), ("receiveOnly", 3))

mibBuilder.exportSymbols("TRIP-TC-MIB", TripSendReceiveMode=TripSendReceiveMode, TripAppProtocol=TripAppProtocol, TripId=TripId, PYSNMP_MODULE_ID=tripTC, TripCommunityId=TripCommunityId, TripItad=TripItad, TripAddressFamily=TripAddressFamily, TripProtocolVersion=TripProtocolVersion, tripTC=tripTC)
