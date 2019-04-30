#
# PySNMP MIB module TPLINK-IPV6STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-IPV6STATICROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ObjectIdentity, iso, ModuleIdentity, Gauge32, Unsigned32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkIPv6StaticRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 53))
tplinkIPv6StaticRouteMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIPv6StaticRouteMIB.setOrganization('TPLINK')
tplinkIPv6StaticRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1))
tplinkIPv6StaticRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 2))
tpIPv6StaticRouteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1))
tpIPv6StaticRouteConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1), )
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigTable.setStatus('current')
tpIPv6StaticRouteConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemDesIp"), (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemPrefixLen"), (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemNexthop"))
if mibBuilder.loadTexts: tpIPv6StaticRouteConfigEntry.setStatus('current')
tpIPv6StaticRouteItemDesIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemDesIp.setStatus('current')
tpIPv6StaticRouteItemPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemPrefixLen.setStatus('current')
tpIPv6StaticRouteItemNexthop = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemNexthop.setStatus('current')
tpIPv6StaticRouteItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemInterfaceName.setStatus('current')
tpIPv6StaticRouteItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 5), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6StaticRouteItemStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IPV6STATICROUTE-MIB", tpIPv6StaticRouteItemPrefixLen=tpIPv6StaticRouteItemPrefixLen, tplinkIPv6StaticRouteMIBObjects=tplinkIPv6StaticRouteMIBObjects, tpIPv6StaticRouteConfigEntry=tpIPv6StaticRouteConfigEntry, tpIPv6StaticRouteConfig=tpIPv6StaticRouteConfig, tpIPv6StaticRouteItemInterfaceName=tpIPv6StaticRouteItemInterfaceName, tpIPv6StaticRouteItemNexthop=tpIPv6StaticRouteItemNexthop, tpIPv6StaticRouteItemDesIp=tpIPv6StaticRouteItemDesIp, tplinkIPv6StaticRouteNotifications=tplinkIPv6StaticRouteNotifications, tpIPv6StaticRouteItemStatus=tpIPv6StaticRouteItemStatus, tpIPv6StaticRouteConfigTable=tpIPv6StaticRouteConfigTable, MacAddress=MacAddress, PYSNMP_MODULE_ID=tplinkIPv6StaticRouteMIB, tplinkIPv6StaticRouteMIB=tplinkIPv6StaticRouteMIB)
