#
# PySNMP MIB module IPV6-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV6-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:17:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Gauge32, Counter64, IpAddress, ObjectIdentity, NotificationType, iso, Counter32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "iso", "Counter32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order. This object is obsoleted by INET-ADDRESS-MIB::InetAddress.'
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class Ipv6AddressPrefix(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 address prefixes. This is a binary string of up to 16 octets in network byte-order. This object is obsoleted by INET-ADDRESS-MIB::InetAddress.'
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 address interface identifiers. This is a binary string of up to 8 octets in network byte-order. This object is obsoleted by IP-MIB::Ipv6AddressIfIdentifierTC.'
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Ipv6IfIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero for each internetwork-layer interface in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each internetwork-layer interface must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization. This object is obsoleted by IF-MIB::InterfaceIndex."
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the Ipv6IfIndex convention. The latter defines a greater than zero value used to identify an IPv6 interface in the managed system. This extension permits the additional value of zero. The value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero might include situations where interface was unknown, or when none or all interfaces need to be referenced. This object is obsoleted by IF-MIB::InterfaceIndexOrZero.'
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("IPV6-TC", Ipv6Address=Ipv6Address, Ipv6IfIndex=Ipv6IfIndex, Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero)
