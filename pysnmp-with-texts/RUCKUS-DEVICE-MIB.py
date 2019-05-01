#
# PySNMP MIB module RUCKUS-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-DEVICE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ruckusCommonDeviceModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonDeviceModule")
RuckusCountryCode, = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusCountryCode")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, TimeTicks, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, IpAddress, Counter64, MibIdentifier, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "iso", "Unsigned32", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ruckusDeviceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1))
if mibBuilder.loadTexts: ruckusDeviceMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusDeviceMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusDeviceMIB.setContactInfo('Ruckus Wireless Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200.')
if mibBuilder.loadTexts: ruckusDeviceMIB.setDescription('Ruckus device management mib.')
ruckusDeviceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1))
ruckusDeviceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1))
ruckusDeviceTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 2))
ruckusDeviceIPInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3))
ruckusDeviceWanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4))
ruckusDeviceEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 2))
ruckusDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceName.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceName.setDescription('Specifies name of the device. Show the same value as model name.')
ruckusDeviceReboot = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceReboot.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceReboot.setDescription('Setting this object to true(1) would cause to reboot the device. Always returns false(2) on read.')
ruckusDeviceRebootWithDefaults = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceRebootWithDefaults.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceRebootWithDefaults.setDescription('This allows the product to revert to factory defaults.')
ruckusDeviceCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 4), RuckusCountryCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceCountryCode.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceCountryCode.setDescription('Specifies the country code. Example ISO country codes: CA,US,HK,IL,CN,JP,TW.')
ruckusDeviceGPS = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceGPS.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceGPS.setDescription('Specifies GPS coordinates of the device. (e.g. 37.3881,-122.0258)')
ruckusDeviceNEId = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceNEId.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceNEId.setDescription('NE Id.')
ruckusDeviceLocation = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceLocation.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceLocation.setDescription('Location of the device. Show the intstallation position.')
ruckusDeviceTrapDestination = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceTrapDestination.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceTrapDestination.setDescription('Specifies primary trap destination IPv6 or IPv4 address.')
ruckusDeviceTrapDestination2 = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceTrapDestination2.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceTrapDestination2.setDescription('Specifies secondary trap destination IPv6 or IPv4 address.')
ruckusDevicePrimaryDNS = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDevicePrimaryDNS.setStatus('current')
if mibBuilder.loadTexts: ruckusDevicePrimaryDNS.setDescription('Specifies primary DNS IP address.')
ruckusDeviceSecondaryDNS = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceSecondaryDNS.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceSecondaryDNS.setDescription('Specifies secondary DNS IP address.')
ruckusDevicePrimaryDNSIPV6 = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDevicePrimaryDNSIPV6.setStatus('current')
if mibBuilder.loadTexts: ruckusDevicePrimaryDNSIPV6.setDescription('Specifies primary DNS IPV6 address.')
ruckusDeviceSecondaryDNSIPV6 = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceSecondaryDNSIPV6.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceSecondaryDNSIPV6.setDescription('Specifies secondary DNS IPV6 address.')
ruckusDeviceWanTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1), )
if mibBuilder.loadTexts: ruckusDeviceWanTable.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanTable.setDescription('Specifies each wan table.')
ruckusDeviceWanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusDeviceWanEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanEntry.setDescription('Specifies each wan entry.')
ruckusDeviceWanIPAddrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("static", 2), ("dhcp", 3), ("pppoe", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPAddrMode.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPAddrMode.setDescription('Specifies how the wan gets its IP address. none - bridging static - Statically assigned IP address dhcp - Using DHCP protocol pppoe - Using PPPoE protocol when ipaddr mode from dhcp to static,the relative nodes should be set together , including:ruckusDeviceWanIPAddr,ruckusDeviceWanNetmask,ruckusDeviceWanGateway ')
ruckusDeviceWanIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPAddr.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPAddr.setDescription('This is writable only if the ruckusDeviceWanIPAddrMode is set to static(2).')
ruckusDeviceWanName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusDeviceWanName.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanName.setDescription('Specifies the name of the wan interface.')
ruckusDeviceWanNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanNetmask.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanNetmask.setDescription('Specifies the ip address mask if the ruckusDeviceWanIPAddrMode is set to static(2).')
ruckusDeviceWanGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanGateway.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanGateway.setDescription('Specifies the gateway ipaddr if the ruckusDeviceWanIPAddrMode is set to static(2).')
ruckusDeviceWanIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ("dualstack", 3))).clone('ipv6')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPVersion.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPVersion.setDescription('Specifies the system ip version,ipv4 or ipv6 or dualstack. ipv4 - only support IPV4 ipv6 - only support IPV6 dualstack - support IPV4 and IPV6')
ruckusDeviceWanIPV6AddrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto-configuration", 1), ("static", 2))).clone('auto-configuration')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPV6AddrMode.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPV6AddrMode.setDescription('Specifies how the wan gets its IPV6 address. auto-configuration - auto get ipv6 address by RFC about IPV6 static - Statically assigned IPV6 address when ipv6addr mode from auto-configuration to static,the relative nodes should be set together , including:ruckusDeviceWanIPV6Addr,ruckusDeviceWanIPV6PrefixLen,ruckusDeviceWanIPV6Gateway ')
ruckusDeviceWanIPV6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPV6Addr.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPV6Addr.setDescription('This is writable only if the ruckusDeviceWanIPAddrMode is set to static(2).')
ruckusDeviceWanIPV6PrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPV6PrefixLen.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPV6PrefixLen.setDescription('Specifies the ip v6 address prefix length if the ruckusDeviceWanIPV6AddrMode is set to static(2).')
ruckusDeviceWanIPV6Gateway = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusDeviceWanIPV6Gateway.setStatus('current')
if mibBuilder.loadTexts: ruckusDeviceWanIPV6Gateway.setDescription('Specifies the gateway ipv6 address if the ruckusDeviceWanIPV6AddrMode is set to static(2).')
mibBuilder.exportSymbols("RUCKUS-DEVICE-MIB", ruckusDeviceTrapInfo=ruckusDeviceTrapInfo, PYSNMP_MODULE_ID=ruckusDeviceMIB, ruckusDeviceObjects=ruckusDeviceObjects, ruckusDeviceWanGateway=ruckusDeviceWanGateway, ruckusDeviceWanIPAddr=ruckusDeviceWanIPAddr, ruckusDeviceWanIPV6Addr=ruckusDeviceWanIPV6Addr, ruckusDeviceLocation=ruckusDeviceLocation, ruckusDeviceWanName=ruckusDeviceWanName, ruckusDeviceTrapDestination=ruckusDeviceTrapDestination, ruckusDeviceTrapDestination2=ruckusDeviceTrapDestination2, ruckusDevicePrimaryDNSIPV6=ruckusDevicePrimaryDNSIPV6, ruckusDeviceSecondaryDNS=ruckusDeviceSecondaryDNS, ruckusDeviceReboot=ruckusDeviceReboot, ruckusDeviceWanIPV6PrefixLen=ruckusDeviceWanIPV6PrefixLen, ruckusDeviceMIB=ruckusDeviceMIB, ruckusDeviceEvents=ruckusDeviceEvents, ruckusDeviceNEId=ruckusDeviceNEId, ruckusDeviceWanIPV6Gateway=ruckusDeviceWanIPV6Gateway, ruckusDeviceWanEntry=ruckusDeviceWanEntry, ruckusDeviceRebootWithDefaults=ruckusDeviceRebootWithDefaults, ruckusDeviceInfo=ruckusDeviceInfo, ruckusDeviceSecondaryDNSIPV6=ruckusDeviceSecondaryDNSIPV6, ruckusDeviceGPS=ruckusDeviceGPS, ruckusDeviceWanTable=ruckusDeviceWanTable, ruckusDeviceName=ruckusDeviceName, ruckusDeviceWanIPVersion=ruckusDeviceWanIPVersion, ruckusDeviceWanIPV6AddrMode=ruckusDeviceWanIPV6AddrMode, ruckusDeviceWanIPAddrMode=ruckusDeviceWanIPAddrMode, ruckusDeviceIPInfo=ruckusDeviceIPInfo, ruckusDeviceWanNetmask=ruckusDeviceWanNetmask, ruckusDeviceCountryCode=ruckusDeviceCountryCode, ruckusDevicePrimaryDNS=ruckusDevicePrimaryDNS, ruckusDeviceWanInfo=ruckusDeviceWanInfo)