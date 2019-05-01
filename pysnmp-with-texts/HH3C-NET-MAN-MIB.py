#
# PySNMP MIB module HH3C-NET-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-NET-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, IpAddress, Unsigned32, Gauge32, MibIdentifier, TimeTicks, Bits, Counter64, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Unsigned32", "Gauge32", "MibIdentifier", "TimeTicks", "Bits", "Counter64", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cNetMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 90))
hh3cNetMan.setRevisions(('2008-04-16 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cNetMan.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: hh3cNetMan.setLastUpdated('200804161700Z')
if mibBuilder.loadTexts: hh3cNetMan.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cNetMan.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: hh3cNetMan.setDescription('This MIB file is to provide the object definition of the network management parameters. These parameters are used to identify devices. It is useful for devices management in a dynamic address assignment network.')
hh3cNMConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 1))
hh3cNMMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 2))
hh3cNMNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3))
hh3cNMNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1))
hh3cNMIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cNMIpAddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cNMIpAddressType.setDescription('The IP address type of specified interface on the device.')
hh3cNMIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cNMIpAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cNMIpAddress.setDescription('The IP address of specified interface on the device.')
hh3cNMCustomBuildInfo = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNMCustomBuildInfo.setStatus('current')
if mibBuilder.loadTexts: hh3cNMCustomBuildInfo.setDescription('The customer-required information of devices, for example, OUI (Organizational Unique Identifier).')
hh3cNMSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cNMSerialNum.setStatus('current')
if mibBuilder.loadTexts: hh3cNMSerialNum.setDescription('The serial number used by NMS (Network Management Station) for mapping IP address and device.')
hh3cNMNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2))
hh3cNMNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2, 0))
hh3cIpAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 90, 3, 2, 0, 1)).setObjects(("HH3C-NET-MAN-MIB", "hh3cNMIpAddressType"), ("HH3C-NET-MAN-MIB", "hh3cNMIpAddress"), ("HH3C-NET-MAN-MIB", "hh3cNMCustomBuildInfo"), ("HH3C-NET-MAN-MIB", "hh3cNMSerialNum"))
if mibBuilder.loadTexts: hh3cIpAddrChangeNotify.setStatus('current')
if mibBuilder.loadTexts: hh3cIpAddrChangeNotify.setDescription('This notification will be generated when the IP address of active management interface is changed. The change maybe originate from NMS, DHCP server or administrator. The management interfaces are the interfaces that assigned by administrator, which can be used to manage device, but may be inactive for link fault or IP address (IPv4 or IPv6) missing. The active management interface means an active interface, the IP address of which can be used for network management. This notification announces useful management IP address change. So it is triggered by significative IP address change. Suppose that two management interfaces on a device, Interface-A and Interface-B. Initially both interfaces are down and assigned no IP address. Configure Interface-A as the primary monitored interface, Interface-B as the secondary. Significative IP address change in following cases: 1. If Interface-A is assigned an IP address primarily, and it is linking up, then Interface-B will be ignored. A notification will be triggered, appending IP address of Interface-A. 2. If Interface-B is assigned an IP address primarily, and it is linking up, then Interface-A will be ignored. A notification will be triggered, appending IP address of Interface-B. 3. If IP address of that interface, which had its IP address announced to NMS, is changed since last notification triggered, then another notification will be sent to NMS. 4. Suppore that Interface-A was linked up and assigned an IP address primarily. If for some unknown reason, Interface-A is down or loses IP address, and Interface-B is assigned an IP address which is different with that announced to NMS before, then a notification will be triggered, appending the new IP address that Interface-B assigned. 5. A notification appending new IP address that Interface-A assigned will be triggered, if 4 occurs to Interface-B.')
hh3cNetManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4))
hh3cNetManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 1))
hh3cNetManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 1, 1)).setObjects(("HH3C-NET-MAN-MIB", "hh3cNMMonitorGroup"), ("HH3C-NET-MAN-MIB", "hh3cNMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cNetManCompliance = hh3cNetManCompliance.setStatus('current')
if mibBuilder.loadTexts: hh3cNetManCompliance.setDescription('The statement of compliance for those implementing the network management MIB.')
hh3cNetManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2))
hh3cNMMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2, 1)).setObjects(("HH3C-NET-MAN-MIB", "hh3cNMIpAddressType"), ("HH3C-NET-MAN-MIB", "hh3cNMIpAddress"), ("HH3C-NET-MAN-MIB", "hh3cNMCustomBuildInfo"), ("HH3C-NET-MAN-MIB", "hh3cNMSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cNMMonitorGroup = hh3cNMMonitorGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cNMMonitorGroup.setDescription('A collection of objects in net management monitor group.')
hh3cNMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25506, 2, 90, 4, 2, 2)).setObjects(("HH3C-NET-MAN-MIB", "hh3cIpAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cNMNotificationGroup = hh3cNMNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cNMNotificationGroup.setDescription('A collection of objects in net management notification group.')
mibBuilder.exportSymbols("HH3C-NET-MAN-MIB", hh3cNMMonitorGroup=hh3cNMMonitorGroup, hh3cNMSerialNum=hh3cNMSerialNum, hh3cNMNotifyScalarObjects=hh3cNMNotifyScalarObjects, hh3cIpAddrChangeNotify=hh3cIpAddrChangeNotify, hh3cNMCustomBuildInfo=hh3cNMCustomBuildInfo, hh3cNetManCompliances=hh3cNetManCompliances, hh3cNMNotify=hh3cNMNotify, hh3cNetManConformance=hh3cNetManConformance, hh3cNetManCompliance=hh3cNetManCompliance, hh3cNetMan=hh3cNetMan, hh3cNMNotificationGroup=hh3cNMNotificationGroup, hh3cNetManGroups=hh3cNetManGroups, hh3cNMNotifyObjects=hh3cNMNotifyObjects, hh3cNMConfigObjects=hh3cNMConfigObjects, hh3cNMMonitorObjects=hh3cNMMonitorObjects, hh3cNMIpAddress=hh3cNMIpAddress, hh3cNMNotifyObjectsPrefix=hh3cNMNotifyObjectsPrefix, hh3cNMIpAddressType=hh3cNMIpAddressType, PYSNMP_MODULE_ID=hh3cNetMan)