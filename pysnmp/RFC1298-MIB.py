#
# PySNMP MIB module RFC1298-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1298-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, NotificationType, ObjectIdentity, iso, Integer32, Gauge32, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, Counter32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "ObjectIdentity", "iso", "Integer32", "Gauge32", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
transportDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 7))
ipxTransportDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 7, 1))
class IpxTransportAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

mibBuilder.exportSymbols("RFC1298-MIB", novell=novell, transportDomains=transportDomains, IpxTransportAddress=IpxTransportAddress, ipxTransportDomain=ipxTransportDomain)
