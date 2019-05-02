#
# PySNMP MIB module TPLINK-IPV6STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-IPV6STATICROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, ModuleIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, Integer32, MibIdentifier, IpAddress, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "Integer32", "MibIdentifier", "IpAddress", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkIPv6StaticRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 53))
tplinkIPv6StaticRouteMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setDescription('Private MIB for IPv6 static route configuration.')
tplinkIPv6StaticRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1))
tplinkIPv6StaticRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 2))
tpIPv6StaticRouteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1))
tpIPv6StaticRouteConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1), )
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigTable.setDescription('A list of static route entries.Route is choosing a best way to trasmit the data from the source to the destination.Static route is a special route,it is set by the administrator,and it is not automatically changed along with the change of network topo, so the static route is most used in the net which is small and has a fixed topo with virtues of simple,efficient and reliable.')
tpIPv6StaticRouteConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemDesIp"), (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemPrefixLen"), (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemNexthop"))
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigEntry.setDescription('The item can be added or removed .')
tpIPv6StaticRouteItemDesIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemDesIp.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteItemDesIp.setDescription('The ip Address of the packet should be arrived')
tpIPv6StaticRouteItemPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemPrefixLen.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteItemPrefixLen.setDescription('The mask of the ip.')
tpIPv6StaticRouteItemNexthop = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemNexthop.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteItemNexthop.setDescription('The next jump ip address which the packet would be sent to by the switch.')
tpIPv6StaticRouteItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemInterfaceName.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteItemInterfaceName.setDescription('The name of the VLAN interface.')
tpIPv6StaticRouteItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 5), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemStatus.setStatus('current')
if mibBuilder.loadTexts: tpIPv6StaticRouteItemStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. notInService(2),destory the entry. notReady(3),destory the entry. createAndGo(4),not being used createAndWait(5),creat a new entry destroy(6),destory the entry.')
mibBuilder.exportSymbols("TPLINK-IPV6STATICROUTE-MIB", tpIPv6StaticRouteItemPrefixLen=tpIPv6StaticRouteItemPrefixLen, tpIPv6StaticRouteConfigEntry=tpIPv6StaticRouteConfigEntry, tpIPv6StaticRouteConfig=tpIPv6StaticRouteConfig, tplinkIPv6StaticRouteMIBObjects=tplinkIPv6StaticRouteMIBObjects, PYSNMP_MODULE_ID=tplinkIPv6StaticRouteMIB, tplinkIPv6StaticRouteMIB=tplinkIPv6StaticRouteMIB, tpIPv6StaticRouteConfigTable=tpIPv6StaticRouteConfigTable, tpIPv6StaticRouteItemStatus=tpIPv6StaticRouteItemStatus, tpIPv6StaticRouteItemInterfaceName=tpIPv6StaticRouteItemInterfaceName, tpIPv6StaticRouteItemDesIp=tpIPv6StaticRouteItemDesIp, tpIPv6StaticRouteItemNexthop=tpIPv6StaticRouteItemNexthop, tplinkIPv6StaticRouteNotifications=tplinkIPv6StaticRouteNotifications, MacAddress=MacAddress)
