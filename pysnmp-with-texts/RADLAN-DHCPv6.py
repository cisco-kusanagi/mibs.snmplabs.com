#
# PySNMP MIB module RADLAN-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DHCPv6
# Produced by pysmi-0.3.4 at Wed May  1 14:46:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, Unsigned32, Integer32, Counter64, iso, ModuleIdentity, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Unsigned32", "Integer32", "Counter64", "iso", "ModuleIdentity", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "MibIdentifier")
TruthValue, DisplayString, TextualConvention, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus", "MacAddress")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('')
if mibBuilder.loadTexts: rlDhcpv6.setContactInfo('')
if mibBuilder.loadTexts: rlDhcpv6.setDescription('The private MIB module definition for DHCP v6 features.')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setDescription('')
mibBuilder.exportSymbols("RADLAN-DHCPv6", rlDhcpv6DuidEn=rlDhcpv6DuidEn, rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6Relay=rlDhcpv6Relay, PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6=rlDhcpv6)
