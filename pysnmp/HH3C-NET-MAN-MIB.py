#
# PySNMP MIB module HH3C-NET-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-NET-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Bits, TimeTicks, Integer32, iso, Gauge32, Counter32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Bits", "TimeTicks", "Integer32", "iso", "Gauge32", "Counter32", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cNetMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 90))
hh3cNetMan.setRevisions(('2008-04-16 17:00',))
if mibBuilder.loadTexts: hh3cNetMan.setLastUpdated('200804161700Z')
if mibBuilder.loadTexts: hh3cNetMan.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cNMConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 1))
hh3cNMMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 2))
hh3cNMNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3))
hh3cNMNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1))
hh3cNMIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cNMIpAddressType.setStatus('current')
hh3cNMIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cNMIpAddress.setStatus('current')
hh3cNMCustomBuildInfo = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNMCustomBuildInfo.setStatus('current')
hh3cNMSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cNMSerialNum.setStatus('current')
hh3cNMNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2))
hh3cNMNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2, 0))
hh3cIpAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2, 0, 1)).setObjects(("HH3C-NET-MAN-MIB", "hh3cNMIpAddressType"), ("HH3C-NET-MAN-MIB", "hh3cNMIpAddress"), ("HH3C-NET-MAN-MIB", "hh3cNMCustomBuildInfo"), ("HH3C-NET-MAN-MIB", "hh3cNMSerialNum"))
if mibBuilder.loadTexts: hh3cIpAddrChangeNotify.setStatus('current')
hh3cNetManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4))
hh3cNetManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 1))
hh3cNetManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 1, 1)).setObjects(("HH3C-NET-MAN-MIB", "hh3cNMMonitorGroup"), ("HH3C-NET-MAN-MIB", "hh3cNMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cNetManCompliance = hh3cNetManCompliance.setStatus('current')
hh3cNetManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2))
hh3cNMMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2, 1)).setObjects(("HH3C-NET-MAN-MIB", "hh3cNMIpAddressType"), ("HH3C-NET-MAN-MIB", "hh3cNMIpAddress"), ("HH3C-NET-MAN-MIB", "hh3cNMCustomBuildInfo"), ("HH3C-NET-MAN-MIB", "hh3cNMSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cNMMonitorGroup = hh3cNMMonitorGroup.setStatus('current')
hh3cNMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2, 2)).setObjects(("HH3C-NET-MAN-MIB", "hh3cIpAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cNMNotificationGroup = hh3cNMNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-NET-MAN-MIB", hh3cNetManCompliance=hh3cNetManCompliance, hh3cNMNotifyScalarObjects=hh3cNMNotifyScalarObjects, hh3cNMConfigObjects=hh3cNMConfigObjects, hh3cNMIpAddressType=hh3cNMIpAddressType, hh3cNMNotifyObjects=hh3cNMNotifyObjects, hh3cNMMonitorObjects=hh3cNMMonitorObjects, hh3cNMSerialNum=hh3cNMSerialNum, hh3cNMNotificationGroup=hh3cNMNotificationGroup, hh3cNMNotify=hh3cNMNotify, hh3cNetMan=hh3cNetMan, hh3cIpAddrChangeNotify=hh3cIpAddrChangeNotify, hh3cNetManCompliances=hh3cNetManCompliances, PYSNMP_MODULE_ID=hh3cNetMan, hh3cNMCustomBuildInfo=hh3cNMCustomBuildInfo, hh3cNMMonitorGroup=hh3cNMMonitorGroup, hh3cNetManConformance=hh3cNetManConformance, hh3cNMIpAddress=hh3cNMIpAddress, hh3cNetManGroups=hh3cNetManGroups, hh3cNMNotifyObjectsPrefix=hh3cNMNotifyObjectsPrefix)
