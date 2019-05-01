#
# PySNMP MIB module CISCO-TC-NO-U32 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TC-NO-U32
# Produced by pysmi-0.3.4 at Wed May  1 12:14:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoProducts, ciscoModules = mibBuilder.importSymbols("CISCO-SMI", "ciscoProducts", "ciscoModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, ObjectIdentity, ModuleIdentity, MibIdentifier, Integer32, TimeTicks, Counter64, NotificationType, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Integer32", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 1))
ciscoTextualConventions.setRevisions(('1997-03-13 00:00', '1997-03-13 00:00', '1996-08-14 00:00', '1996-07-08 00:00', '1995-06-07 00:00', '1998-10-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTextualConventions.setRevisionsDescriptions(('Added CountryCode textual convention.', 'Added SAPType textual convention.', 'Added InterfaceIndexOrZero textual convention.', 'Added new CiscoNetworkProtocol enumerations.', 'Miscellaneous updates/corrections, including making CiscoNetworkProtocol enumerations contiguous.', 'Added Port and IpProtocol textual conventions.',))
if mibBuilder.loadTexts: ciscoTextualConventions.setLastUpdated('9810280000Z')
if mibBuilder.loadTexts: ciscoTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTextualConventions.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTextualConventions.setDescription('This module defines textual conventions used throughout cisco enterprise mibs.')
class CiscoNetworkProtocol(TextualConvention, Integer32):
    description = 'Represents the different types of network layer protocols.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("unknown", 65535))

class CiscoNetworkAddress(TextualConvention, OctetString):
    description = 'Represents a network layer address. The length and format of the address is protocol dependent as follows: ip 4 octets decnet 2 octets pup obsolete chaos 2 octets xns 10 octets first 4 octets are the net number last 6 octets are the host number x121 appletalk 3 octets first 2 octets are the net number last octet is the host number clns lat vines 6 octets first 4 octets are the net number last 2 octets are the host number cons apollo 10 octets first 4 octets are the net number last 6 octets are the host number stun 8 octets novell 10 octets first 4 octets are the net number last 6 octets are the host number qllc 6 octets bstun 1 octet - bi-sync serial tunnel snapshot 1 octet atmIlmi 4 octets x25 pvc 2 octets (12 bits) '
    status = 'current'
    displayHint = '1x:'

class InterfaceIndexOrZero(TextualConvention, Integer32):
    description = 'Either the value 0, or the ifIndex value of an interface in the ifTable.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class SAPType(TextualConvention, Integer32):
    description = 'Service Access Point - is a term that denotes the means by which a user entity in layer n+1 accesses a service of a provider entity in layer n.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CountryCode(TextualConvention, OctetString):
    description = 'Represents a case-insensitive 2-letter country code taken from ISO-3166. Unrecognized countries are represented as empty string. '
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of entPhysicalIndex. If non-zero, the object is an entPhysicalIndex. If zero, no appropriate entPhysicalIndex exists. Any additional semantics are object specific.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CiscoRowOperStatus(TextualConvention, Integer32):
    description = "Represents the operational status of an table entry. This textual convention allows explicitly representing the states of rows dependent on rows in other tables. active(1) - Indicates this entry's RowStatus is active and the RowStatus for each dependency is active. activeDependencies(2) - Indicates that the RowStatus for each dependency is active, but the entry's RowStatus is not active. inactiveDependency(3) - Indicates that the RowStatus for at least one dependency is not active. missingDependency(4) - Indicates that at least one dependency does not exist in it's table. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class CiscoPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    description = 'The TCP or UDP port number range.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CiscoIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    description = 'IP protocol number range.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-TC-NO-U32", CiscoPort=CiscoPort, InterfaceIndexOrZero=InterfaceIndexOrZero, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, PYSNMP_MODULE_ID=ciscoTextualConventions, CountryCode=CountryCode, ciscoTextualConventions=ciscoTextualConventions, CiscoIpProtocol=CiscoIpProtocol, CiscoNetworkAddress=CiscoNetworkAddress, CiscoNetworkProtocol=CiscoNetworkProtocol, SAPType=SAPType, CiscoRowOperStatus=CiscoRowOperStatus)
