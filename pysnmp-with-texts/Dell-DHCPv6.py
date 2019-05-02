#
# PySNMP MIB module Dell-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-DHCPv6
# Produced by pysmi-0.3.4 at Wed May  1 12:55:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressType, InetAddressIPv6, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressIPv6", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Unsigned32, Gauge32, Integer32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Bits, MibIdentifier, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Unsigned32", "Gauge32", "Integer32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Bits", "MibIdentifier", "iso", "ObjectIdentity")
TruthValue, MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("Dell-DHCPv6", rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6=rlDhcpv6, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6DuidEn=rlDhcpv6DuidEn, PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6Relay=rlDhcpv6Relay)
