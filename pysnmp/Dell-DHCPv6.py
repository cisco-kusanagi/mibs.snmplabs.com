#
# PySNMP MIB module Dell-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-DHCPv6
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, Bits, Unsigned32, ModuleIdentity, iso, MibIdentifier, Integer32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "Bits", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "Integer32", "Counter32", "NotificationType")
RowStatus, DisplayString, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TruthValue", "TextualConvention")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
mibBuilder.exportSymbols("Dell-DHCPv6", PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6DuidEn=rlDhcpv6DuidEn, rlDhcpv6Relay=rlDhcpv6Relay, rlDhcpv6=rlDhcpv6)
