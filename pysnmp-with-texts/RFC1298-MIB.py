#
# PySNMP MIB module RFC1298-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1298-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:56:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, iso, enterprises, Counter32, TimeTicks, Counter64, Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "iso", "enterprises", "Counter32", "TimeTicks", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
transportDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 7))
ipxTransportDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 7, 1))
class IpxTransportAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

mibBuilder.exportSymbols("RFC1298-MIB", transportDomains=transportDomains, IpxTransportAddress=IpxTransportAddress, novell=novell, ipxTransportDomain=ipxTransportDomain)
