#
# PySNMP MIB module ENTERASYS-UPN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-UPN-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, NotificationType, Counter64, Bits, Counter32, MibIdentifier, TimeTicks, Unsigned32, Gauge32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "NotificationType", "Counter64", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysUpnTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 44))
etsysUpnTcMIB.setRevisions(('2004-02-03 22:00', '2004-02-03 15:33',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysUpnTcMIB.setRevisionsDescriptions(('Changed naming from StationIdentifier to StationAddress to align naming with ongoing work in the IETF.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysUpnTcMIB.setLastUpdated('200402032200Z')
if mibBuilder.loadTexts: etsysUpnTcMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: etsysUpnTcMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysUpnTcMIB.setDescription("This MIB module defines textual conventions related to the management of User Personalized Networks. The conventions defined below are applicable for use in all Enterasys Networks' MIB definitions.")
class StationAddressType(TextualConvention, Integer32):
    reference = 'STD0058 (RFC2579), Textual Conventions for SMIv2. RFC3291, Textual Conventions for Internet Network Addresses.'
    description = 'A value representing a network address that can be used to identify a station on the network. unknown(0) An unknown address type. This value MUST be used if the value of the corresponding StationAddress object is a zero-length string. It may also be used to indicate an station address which is not in one of the formats defined below. ipv4(1) An IPv4 address as defined by the InetAddressIPv4 textual convention as defined in RFC3291. ipv6(2) An IPv6 address as defined by the StationAddressIPv6 textual convention below. mac(3) An 802.3 MAC layer address, i.e. an Ethernet address, defined by the MacAddress textual convention as defined in RFC2579. dns(16) A DNS domain name as defined by the InetAddressDNS textual convention as defined in RFC3291. Each definition of a concrete StationAddressType value must be accompanied by a definition of a textual convention for use with that StationAddressType. The StationAddressType textual convention SHOULD NOT be subtyped in object type definitions to support future extensions. It MAY be subtyped in compliance statements in order to require only a subset of these address types for a compliant implementation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("mac", 3), ("dns", 16))

class StationAddress(TextualConvention, OctetString):
    description = "Denotes a generic Internet address. An StationAddress value is always interpreted within the context of an StationAddressType value. Every usage of the StationAddress textual convention is required to specify the StationAddressType object which provides the context. It is suggested that the StationAddressType object is logically registered before the object(s) which use the StationAddress textual convention if they appear in the same logical row. The value of an StationAddress object must always be consistent with the value of the associated StationAddressType object. Attempts to set an StationAddress object to a value which is inconsistent with the associated StationAddressType must fail with an inconsistentValue error. When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class StationAddressIPv6(TextualConvention, OctetString):
    description = 'Represents an IPv6 network address: octets contents encoding 1-16 IPv6 address network-byte order 17-20 scope identifier network-byte order The corresponding InetAddressType value is ipv6(2). The scope identifier (bytes 17-20) MUST NOT be present for global IPv6 addresses. For non-global IPv6 addresses (e.g. link-local or site-local addresses), the scope identifier MUST always be present. It contains a link identifier for link-local and a site identifier for site-local IPv6 addresses. The scope identifier MUST disambiguate identical address values. For link-local addresses, the scope identifier will typically be the interface index (ifIndex as defined in the IF-MIB, RFC 2233) of the interface on which the address is configured. The scope identifier may contain the special value 0 which refers to the default scope. The default scope may be used in cases where the valid scope identifier is not known (e.g., a management application needs to write a site-local StationIdIPv6 address without knowing the site identifier value). The default scope SHOULD NOT be used as an easy way out in cases where the scope identifier for a non-global IPv6 is known.'
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
mibBuilder.exportSymbols("ENTERASYS-UPN-TC-MIB", etsysUpnTcMIB=etsysUpnTcMIB, PYSNMP_MODULE_ID=etsysUpnTcMIB, StationAddress=StationAddress, StationAddressIPv6=StationAddressIPv6, StationAddressType=StationAddressType)
