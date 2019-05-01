#
# PySNMP MIB module TPLINK-STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-STATICROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, Integer32, Bits, ModuleIdentity, TimeTicks, IpAddress, iso, NotificationType, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Integer32", "Bits", "ModuleIdentity", "TimeTicks", "IpAddress", "iso", "NotificationType", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkStaticRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 36))
tplinkStaticRouteMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkStaticRouteMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setDescription('Private MIB for static route configuration.')
tplinkStaticRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1))
tplinkStaticRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 2))
tpStaticRouteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1))
tpStaticRouteConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1), )
if mibBuilder.loadTexts: tpStaticRouteConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteConfigTable.setDescription('A list of static route entries.Route is choosing a best way to trasmit the data from the source to the destination.Static route is a special route,it is set by the administrator,and it is not automatically changed along with the change of network topo, so the static route is most used in the net which is small and has a fixed topo with virtues of simple,efficient and reliable.')
tpStaticRouteConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemDesIp"), (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemMask"), (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemNextIp"))
if mibBuilder.loadTexts: tpStaticRouteConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteConfigEntry.setDescription('The item can be added or removed .')
tpStaticRouteItemDesIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemDesIp.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteItemDesIp.setDescription('The ip Address of the packet should be arrived')
tpStaticRouteItemMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemMask.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteItemMask.setDescription('The mask of the ip.')
tpStaticRouteItemNextIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemNextIp.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteItemNextIp.setDescription('The next jump ip address which the packet would be sent to by the switch.')
tpStaticRouteItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemInterfaceName.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteItemInterfaceName.setDescription('The name of the VLAN interface.')
tpStaticRouteItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 5), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemStatus.setStatus('current')
if mibBuilder.loadTexts: tpStaticRouteItemStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. notInService(2),destory the entry. notReady(3),destory the entry. createAndGo(4),not being used createAndWait(5),creat a new entry destroy(6),destory the entry.')
mibBuilder.exportSymbols("TPLINK-STATICROUTE-MIB", tplinkStaticRouteNotifications=tplinkStaticRouteNotifications, tpStaticRouteConfigEntry=tpStaticRouteConfigEntry, tpStaticRouteItemMask=tpStaticRouteItemMask, MacAddress=MacAddress, tplinkStaticRouteMIBObjects=tplinkStaticRouteMIBObjects, PYSNMP_MODULE_ID=tplinkStaticRouteMIB, tplinkStaticRouteMIB=tplinkStaticRouteMIB, tpStaticRouteItemDesIp=tpStaticRouteItemDesIp, tpStaticRouteItemNextIp=tpStaticRouteItemNextIp, tpStaticRouteConfigTable=tpStaticRouteConfigTable, tpStaticRouteItemStatus=tpStaticRouteItemStatus, tpStaticRouteItemInterfaceName=tpStaticRouteItemInterfaceName, tpStaticRouteConfig=tpStaticRouteConfig)
