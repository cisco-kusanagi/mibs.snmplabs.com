#
# PySNMP MIB module TPLINK-STATICROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-STATICROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, Integer32, ModuleIdentity, Counter32, Counter64, NotificationType, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32", "Counter64", "NotificationType", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkStaticRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 36))
tplinkStaticRouteMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkStaticRouteMIB.setOrganization('TPLINK')
tplinkStaticRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1))
tplinkStaticRouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 2))
tpStaticRouteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1))
tpStaticRouteConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1), )
if mibBuilder.loadTexts: tpStaticRouteConfigTable.setStatus('current')
tpStaticRouteConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemDesIp"), (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemMask"), (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemNextIp"))
if mibBuilder.loadTexts: tpStaticRouteConfigEntry.setStatus('current')
tpStaticRouteItemDesIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemDesIp.setStatus('current')
tpStaticRouteItemMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemMask.setStatus('current')
tpStaticRouteItemNextIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemNextIp.setStatus('current')
tpStaticRouteItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticRouteItemInterfaceName.setStatus('current')
tpStaticRouteItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 5), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticRouteItemStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-STATICROUTE-MIB", tpStaticRouteItemMask=tpStaticRouteItemMask, tpStaticRouteItemDesIp=tpStaticRouteItemDesIp, tpStaticRouteItemNextIp=tpStaticRouteItemNextIp, tplinkStaticRouteNotifications=tplinkStaticRouteNotifications, tpStaticRouteConfigTable=tpStaticRouteConfigTable, PYSNMP_MODULE_ID=tplinkStaticRouteMIB, tplinkStaticRouteMIB=tplinkStaticRouteMIB, MacAddress=MacAddress, tpStaticRouteConfigEntry=tpStaticRouteConfigEntry, tpStaticRouteItemStatus=tpStaticRouteItemStatus, tpStaticRouteConfig=tpStaticRouteConfig, tpStaticRouteItemInterfaceName=tpStaticRouteItemInterfaceName, tplinkStaticRouteMIBObjects=tplinkStaticRouteMIBObjects)
