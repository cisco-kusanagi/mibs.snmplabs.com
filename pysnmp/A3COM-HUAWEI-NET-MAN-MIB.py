#
# PySNMP MIB module A3COM-HUAWEI-NET-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-NET-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Integer32, Counter32, Gauge32, ObjectIdentity, Counter64, TimeTicks, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cNetMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90))
h3cNetMan.setRevisions(('2008-04-16 17:00',))
if mibBuilder.loadTexts: h3cNetMan.setLastUpdated('200804161700Z')
if mibBuilder.loadTexts: h3cNetMan.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cNMConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 1))
h3cNMMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 2))
h3cNMNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3))
h3cNMNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1))
h3cNMIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cNMIpAddressType.setStatus('current')
h3cNMIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cNMIpAddress.setStatus('current')
h3cNMCustomBuildInfo = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cNMCustomBuildInfo.setStatus('current')
h3cNMSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cNMSerialNum.setStatus('current')
h3cNMNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 2))
h3cNMNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 2, 0))
h3cIpAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 3, 2, 0, 1)).setObjects(("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddressType"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddress"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMCustomBuildInfo"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMSerialNum"))
if mibBuilder.loadTexts: h3cIpAddrChangeNotify.setStatus('current')
h3cNetManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4))
h3cNetManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 1))
h3cNetManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 1, 1)).setObjects(("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMMonitorGroup"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cNetManCompliance = h3cNetManCompliance.setStatus('current')
h3cNetManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 2))
h3cNMMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 2, 1)).setObjects(("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddressType"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMIpAddress"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMCustomBuildInfo"), ("A3COM-HUAWEI-NET-MAN-MIB", "h3cNMSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cNMMonitorGroup = h3cNMMonitorGroup.setStatus('current')
h3cNMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 90, 4, 2, 2)).setObjects(("A3COM-HUAWEI-NET-MAN-MIB", "h3cIpAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cNMNotificationGroup = h3cNMNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-NET-MAN-MIB", h3cNMNotifyScalarObjects=h3cNMNotifyScalarObjects, h3cNMConfigObjects=h3cNMConfigObjects, h3cNetManGroups=h3cNetManGroups, h3cNMSerialNum=h3cNMSerialNum, h3cNMNotify=h3cNMNotify, PYSNMP_MODULE_ID=h3cNetMan, h3cNetManCompliance=h3cNetManCompliance, h3cNetMan=h3cNetMan, h3cNMIpAddress=h3cNMIpAddress, h3cNMMonitorObjects=h3cNMMonitorObjects, h3cNMCustomBuildInfo=h3cNMCustomBuildInfo, h3cNetManConformance=h3cNetManConformance, h3cNMNotifyObjectsPrefix=h3cNMNotifyObjectsPrefix, h3cNMMonitorGroup=h3cNMMonitorGroup, h3cIpAddrChangeNotify=h3cIpAddrChangeNotify, h3cNMIpAddressType=h3cNMIpAddressType, h3cNetManCompliances=h3cNetManCompliances, h3cNMNotificationGroup=h3cNMNotificationGroup, h3cNMNotifyObjects=h3cNMNotifyObjects)
