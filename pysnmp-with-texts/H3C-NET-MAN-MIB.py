#
# PySNMP MIB module H3C-NET-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-NET-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, ObjectIdentity, Integer32, IpAddress, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, MibIdentifier, Bits, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "ObjectIdentity", "Integer32", "IpAddress", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "MibIdentifier", "Bits", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cNetMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90))
h3cNetMan.setRevisions(('2008-04-16 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cNetMan.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cNetMan.setLastUpdated('200804161700Z')
if mibBuilder.loadTexts: h3cNetMan.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cNetMan.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cNetMan.setDescription('This MIB file is to provide the object definition of the network management parameters. These parameters are used to identify devices. It is useful for devices management in a dynamic address assignment network.')
h3cNMConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 1))
h3cNMMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 2))
h3cNMNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3))
h3cNMNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 1))
h3cNMIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cNMIpAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cNMIpAddressType.setDescription('The IP address type of specified interface on the device.')
h3cNMIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cNMIpAddress.setStatus('current')
if mibBuilder.loadTexts: h3cNMIpAddress.setDescription('The IP address of specified interface on the device.')
h3cNMCustomBuildInfo = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cNMCustomBuildInfo.setStatus('current')
if mibBuilder.loadTexts: h3cNMCustomBuildInfo.setDescription('The customer-required information of devices, for example, OUI (Organizational Unique Identifier).')
h3cNMSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cNMSerialNum.setStatus('current')
if mibBuilder.loadTexts: h3cNMSerialNum.setDescription('The serial number used by NMS (Network Management Station) for mapping IP address and device.')
h3cNMNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 2))
h3cNMNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 2, 0))
h3cIpAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 3, 2, 0, 1)).setObjects(("H3C-NET-MAN-MIB", "h3cNMIpAddressType"), ("H3C-NET-MAN-MIB", "h3cNMIpAddress"), ("H3C-NET-MAN-MIB", "h3cNMCustomBuildInfo"), ("H3C-NET-MAN-MIB", "h3cNMSerialNum"))
if mibBuilder.loadTexts: h3cIpAddrChangeNotify.setStatus('current')
if mibBuilder.loadTexts: h3cIpAddrChangeNotify.setDescription('This notification will be generated when the IP address of active management interface is changed. The change maybe originate from NMS, DHCP server or administrator. The management interfaces are the interfaces that assigned by administrator, which can be used to manage device, but may be inactive for link fault or IP address (IPv4 or IPv6) missing. The active management interface means an active interface, the IP address of which can be used for network management. This notification announces useful management IP address change. So it is triggered by significative IP address change. Suppose that two management interfaces on a device, Interface-A and Interface-B. Initially both interfaces are down and assigned no IP address. Configure Interface-A as the primary monitored interface, Interface-B as the secondary. Significative IP address change in following cases: 1. If Interface-A is assigned an IP address primarily, and it is linking up, then Interface-B will be ignored. A notification will be triggered, appending IP address of Interface-A. 2. If Interface-B is assigned an IP address primarily, and it is linking up, then Interface-A will be ignored. A notification will be triggered, appending IP address of Interface-B. 3. If IP address of that interface, which had its IP address announced to NMS, is changed since last notification triggered, then another notification will be sent to NMS. 4. Suppore that Interface-A was linked up and assigned an IP address primarily. If for some unknown reason, Interface-A is down or loses IP address, and Interface-B is assigned an IP address which is different with that announced to NMS before, then a notification will be triggered, appending the new IP address that Interface-B assigned. 5. A notification appending new IP address that Interface-A assigned will be triggered, if 4 occurs to Interface-B.')
h3cNetManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 4))
h3cNetManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 4, 1))
h3cNetManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 4, 1, 1)).setObjects(("H3C-NET-MAN-MIB", "h3cNMMonitorGroup"), ("H3C-NET-MAN-MIB", "h3cNMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cNetManCompliance = h3cNetManCompliance.setStatus('current')
if mibBuilder.loadTexts: h3cNetManCompliance.setDescription('The statement of compliance for those implementing the network management MIB.')
h3cNetManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 4, 2))
h3cNMMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 4, 2, 1)).setObjects(("H3C-NET-MAN-MIB", "h3cNMIpAddressType"), ("H3C-NET-MAN-MIB", "h3cNMIpAddress"), ("H3C-NET-MAN-MIB", "h3cNMCustomBuildInfo"), ("H3C-NET-MAN-MIB", "h3cNMSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cNMMonitorGroup = h3cNMMonitorGroup.setStatus('current')
if mibBuilder.loadTexts: h3cNMMonitorGroup.setDescription('A collection of objects in net management monitor group.')
h3cNMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 90, 4, 2, 2)).setObjects(("H3C-NET-MAN-MIB", "h3cIpAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cNMNotificationGroup = h3cNMNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: h3cNMNotificationGroup.setDescription('A collection of objects in net management notification group.')
mibBuilder.exportSymbols("H3C-NET-MAN-MIB", h3cNMConfigObjects=h3cNMConfigObjects, h3cNetManCompliances=h3cNetManCompliances, h3cNetMan=h3cNetMan, h3cNetManCompliance=h3cNetManCompliance, PYSNMP_MODULE_ID=h3cNetMan, h3cNMNotifyObjectsPrefix=h3cNMNotifyObjectsPrefix, h3cNetManGroups=h3cNetManGroups, h3cNMIpAddress=h3cNMIpAddress, h3cNMCustomBuildInfo=h3cNMCustomBuildInfo, h3cNetManConformance=h3cNetManConformance, h3cNMNotifyObjects=h3cNMNotifyObjects, h3cNMNotificationGroup=h3cNMNotificationGroup, h3cNMNotify=h3cNMNotify, h3cIpAddrChangeNotify=h3cIpAddrChangeNotify, h3cNMSerialNum=h3cNMSerialNum, h3cNMIpAddressType=h3cNMIpAddressType, h3cNMMonitorObjects=h3cNMMonitorObjects, h3cNMMonitorGroup=h3cNMMonitorGroup, h3cNMNotifyScalarObjects=h3cNMNotifyScalarObjects)
