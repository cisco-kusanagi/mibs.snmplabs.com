#
# PySNMP MIB module ZYXEL-IPV6-STATIC-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-IPV6-STATIC-ROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, ModuleIdentity, iso, Integer32, TimeTicks, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ModuleIdentity", "iso", "Integer32", "TimeTicks", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelIpv6StaticRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37))
if mibBuilder.loadTexts: zyxelIpv6StaticRoute.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIpv6StaticRoute.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelIpv6StaticRoute.setContactInfo('')
if mibBuilder.loadTexts: zyxelIpv6StaticRoute.setDescription('The subtree for IPv6 static route')
zyxelIpv6StaticRouteSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1))
zyIpv6StaticRouteMaxNumberOfStaticRoutes = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIpv6StaticRouteMaxNumberOfStaticRoutes.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteMaxNumberOfStaticRoutes.setDescription('The maximum number of IPv6 Static Route entries that can be created.')
zyxelIpv6StaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2), )
if mibBuilder.loadTexts: zyxelIpv6StaticRouteTable.setStatus('current')
if mibBuilder.loadTexts: zyxelIpv6StaticRouteTable.setDescription('The table contains IPv6 static route configuration.')
zyxelIpv6StaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1), ).setIndexNames((0, "ZYXEL-IPV6-STATIC-ROUTE-MIB", "zyIpv6StaticRouteDestinationIpAddressType"), (0, "ZYXEL-IPV6-STATIC-ROUTE-MIB", "zyIpv6StaticRouteDestinationIpAddress"), (0, "ZYXEL-IPV6-STATIC-ROUTE-MIB", "zyIpv6StaticRouteDestinationAddressPrefixLength"))
if mibBuilder.loadTexts: zyxelIpv6StaticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelIpv6StaticRouteEntry.setDescription('An entry contains IPv6 static route configuration.')
zyIpv6StaticRouteDestinationIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: zyIpv6StaticRouteDestinationIpAddressType.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteDestinationIpAddressType.setDescription('This entry displays the type of IPv6 static route destination address.')
zyIpv6StaticRouteDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: zyIpv6StaticRouteDestinationIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteDestinationIpAddress.setDescription('This entry displays IPv6 static route destination address.')
zyIpv6StaticRouteDestinationAddressPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 3), Integer32())
if mibBuilder.loadTexts: zyIpv6StaticRouteDestinationAddressPrefixLength.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteDestinationAddressPrefixLength.setDescription('This entry displays the length of IPv6 static route destination address prefix.')
zyIpv6StaticRouteNextHopIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIpv6StaticRouteNextHopIpAddressType.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteNextHopIpAddressType.setDescription('This entry displays the address type of next hop address.')
zyIpv6StaticRouteNextHopIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIpv6StaticRouteNextHopIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteNextHopIpAddress.setDescription('This entry displays the IPv6 address of the next hop. The next hop is the neighbor of your switch that will forward the packet to the destination. ')
zyIpv6StaticRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIpv6StaticRouteIfIndex.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteIfIndex.setDescription('This entry displays the interface index of IPv6 static route entry.')
zyIpv6StaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyIpv6StaticRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyIpv6StaticRouteRowStatus.setDescription('This object allows entry to be created and deleted an IPv6 static route entry.')
mibBuilder.exportSymbols("ZYXEL-IPV6-STATIC-ROUTE-MIB", zyIpv6StaticRouteDestinationAddressPrefixLength=zyIpv6StaticRouteDestinationAddressPrefixLength, PYSNMP_MODULE_ID=zyxelIpv6StaticRoute, zyIpv6StaticRouteNextHopIpAddress=zyIpv6StaticRouteNextHopIpAddress, zyxelIpv6StaticRouteSetup=zyxelIpv6StaticRouteSetup, zyxelIpv6StaticRouteEntry=zyxelIpv6StaticRouteEntry, zyIpv6StaticRouteMaxNumberOfStaticRoutes=zyIpv6StaticRouteMaxNumberOfStaticRoutes, zyIpv6StaticRouteIfIndex=zyIpv6StaticRouteIfIndex, zyIpv6StaticRouteDestinationIpAddressType=zyIpv6StaticRouteDestinationIpAddressType, zyxelIpv6StaticRoute=zyxelIpv6StaticRoute, zyIpv6StaticRouteNextHopIpAddressType=zyIpv6StaticRouteNextHopIpAddressType, zyIpv6StaticRouteDestinationIpAddress=zyIpv6StaticRouteDestinationIpAddress, zyIpv6StaticRouteRowStatus=zyIpv6StaticRouteRowStatus, zyxelIpv6StaticRouteTable=zyxelIpv6StaticRouteTable)
