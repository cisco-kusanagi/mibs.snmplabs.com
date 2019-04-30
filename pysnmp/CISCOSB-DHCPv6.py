#
# PySNMP MIB module CISCOSB-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-DHCPv6
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressType, InetAddress, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressIPv6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Gauge32, ObjectIdentity, Counter32, Bits, NotificationType, iso, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "Bits", "NotificationType", "iso", "ModuleIdentity", "Integer32")
MacAddress, TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('200604020000Z')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('Cisco Small Business')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-DHCPv6", rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6DuidEn=rlDhcpv6DuidEn, rlDhcpv6=rlDhcpv6, rlDhcpv6Common=rlDhcpv6Common, PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6Relay=rlDhcpv6Relay)
