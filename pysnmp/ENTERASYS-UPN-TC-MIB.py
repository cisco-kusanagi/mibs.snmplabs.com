#
# PySNMP MIB module ENTERASYS-UPN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-UPN-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Gauge32, Counter64, MibIdentifier, TimeTicks, Counter32, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysUpnTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 44))
etsysUpnTcMIB.setRevisions(('2004-02-03 22:00', '2004-02-03 15:33',))
if mibBuilder.loadTexts: etsysUpnTcMIB.setLastUpdated('200402032200Z')
if mibBuilder.loadTexts: etsysUpnTcMIB.setOrganization('Enterasys Networks, Inc.')
class StationAddressType(TextualConvention, Integer32):
    reference = 'STD0058 (RFC2579), Textual Conventions for SMIv2. RFC3291, Textual Conventions for Internet Network Addresses.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("mac", 3), ("dns", 16))

class StationAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class StationAddressIPv6(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
mibBuilder.exportSymbols("ENTERASYS-UPN-TC-MIB", StationAddressIPv6=StationAddressIPv6, StationAddressType=StationAddressType, etsysUpnTcMIB=etsysUpnTcMIB, StationAddress=StationAddress, PYSNMP_MODULE_ID=etsysUpnTcMIB)
