#
# PySNMP MIB module HPN-ICF-NET-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-NET-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Bits, Counter32, Unsigned32, Counter64, Gauge32, IpAddress, iso, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter32", "Unsigned32", "Counter64", "Gauge32", "IpAddress", "iso", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfNetMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90))
hpnicfNetMan.setRevisions(('2008-04-16 17:00',))
if mibBuilder.loadTexts: hpnicfNetMan.setLastUpdated('200804161700Z')
if mibBuilder.loadTexts: hpnicfNetMan.setOrganization('')
hpnicfNMConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 1))
hpnicfNMMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 2))
hpnicfNMNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3))
hpnicfNMNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1))
hpnicfNMIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfNMIpAddressType.setStatus('current')
hpnicfNMIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfNMIpAddress.setStatus('current')
hpnicfNMCustomBuildInfo = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNMCustomBuildInfo.setStatus('current')
hpnicfNMSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfNMSerialNum.setStatus('current')
hpnicfNMNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2))
hpnicfNMNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2, 0))
hpnicfIpAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2, 0, 1)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddressType"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddress"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMCustomBuildInfo"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMSerialNum"))
if mibBuilder.loadTexts: hpnicfIpAddrChangeNotify.setStatus('current')
hpnicfNetManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4))
hpnicfNetManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 1))
hpnicfNetManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 1, 1)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfNMMonitorGroup"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfNetManCompliance = hpnicfNetManCompliance.setStatus('current')
hpnicfNetManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2))
hpnicfNMMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2, 1)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddressType"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddress"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMCustomBuildInfo"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfNMMonitorGroup = hpnicfNMMonitorGroup.setStatus('current')
hpnicfNMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2, 2)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfIpAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfNMNotificationGroup = hpnicfNMNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-NET-MAN-MIB", hpnicfNMNotifyObjects=hpnicfNMNotifyObjects, PYSNMP_MODULE_ID=hpnicfNetMan, hpnicfNMCustomBuildInfo=hpnicfNMCustomBuildInfo, hpnicfIpAddrChangeNotify=hpnicfIpAddrChangeNotify, hpnicfNMNotifyScalarObjects=hpnicfNMNotifyScalarObjects, hpnicfNetManCompliance=hpnicfNetManCompliance, hpnicfNMIpAddressType=hpnicfNMIpAddressType, hpnicfNMSerialNum=hpnicfNMSerialNum, hpnicfNetMan=hpnicfNetMan, hpnicfNetManConformance=hpnicfNetManConformance, hpnicfNMNotify=hpnicfNMNotify, hpnicfNetManCompliances=hpnicfNetManCompliances, hpnicfNMMonitorGroup=hpnicfNMMonitorGroup, hpnicfNMIpAddress=hpnicfNMIpAddress, hpnicfNMMonitorObjects=hpnicfNMMonitorObjects, hpnicfNMNotifyObjectsPrefix=hpnicfNMNotifyObjectsPrefix, hpnicfNMNotificationGroup=hpnicfNMNotificationGroup, hpnicfNetManGroups=hpnicfNetManGroups, hpnicfNMConfigObjects=hpnicfNMConfigObjects)
