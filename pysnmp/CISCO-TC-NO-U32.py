#
# PySNMP MIB module CISCO-TC-NO-U32 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TC-NO-U32
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoModules, ciscoProducts = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules", "ciscoProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter64, TimeTicks, NotificationType, MibIdentifier, Counter32, Integer32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter64", "TimeTicks", "NotificationType", "MibIdentifier", "Counter32", "Integer32", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 1))
ciscoTextualConventions.setRevisions(('1997-03-13 00:00', '1997-03-13 00:00', '1996-08-14 00:00', '1996-07-08 00:00', '1995-06-07 00:00', '1998-10-28 00:00',))
if mibBuilder.loadTexts: ciscoTextualConventions.setLastUpdated('9810280000Z')
if mibBuilder.loadTexts: ciscoTextualConventions.setOrganization('Cisco Systems, Inc.')
class CiscoNetworkProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("unknown", 65535))

class CiscoNetworkAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'

class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class SAPType(TextualConvention, Integer32):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CountryCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CiscoRowOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class CiscoPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CiscoIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-TC-NO-U32", CiscoIpProtocol=CiscoIpProtocol, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, InterfaceIndexOrZero=InterfaceIndexOrZero, CiscoPort=CiscoPort, SAPType=SAPType, CiscoRowOperStatus=CiscoRowOperStatus, PYSNMP_MODULE_ID=ciscoTextualConventions, CountryCode=CountryCode, CiscoNetworkAddress=CiscoNetworkAddress, ciscoTextualConventions=ciscoTextualConventions, CiscoNetworkProtocol=CiscoNetworkProtocol)
