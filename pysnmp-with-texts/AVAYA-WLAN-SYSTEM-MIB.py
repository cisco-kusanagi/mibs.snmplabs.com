#
# PySNMP MIB module AVAYA-WLAN-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYA-WLAN-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, Integer32, NotificationType, Counter32, Counter64, Bits, IpAddress, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "Integer32", "NotificationType", "Counter32", "Counter64", "Bits", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
avayaWlanMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "avayaWlanMibs")
avayaWlanSystemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 7, 16))
avayaWlanSystemMib.setRevisions(('2010-05-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avayaWlanSystemMib.setRevisionsDescriptions(('v1: Initial version.',))
if mibBuilder.loadTexts: avayaWlanSystemMib.setLastUpdated('201005250000Z')
if mibBuilder.loadTexts: avayaWlanSystemMib.setOrganization('Avaya, Inc')
if mibBuilder.loadTexts: avayaWlanSystemMib.setContactInfo('Avaya, Inc')
if mibBuilder.loadTexts: avayaWlanSystemMib.setDescription("Avaya WLAN System MIB Copyright 2010 Avaya, Inc. All rights reserved. This Avaya SNMP Management Information Base Specification (Specification) embodies Avaya's confidential and proprietary intellectual property. Avaya retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Avaya makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
avWlanSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 7, 16, 1))
avWlanSystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1))
avWlanSystemStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2))
avWlanSystemConfigScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1))
avWlanSystemConfigWirelessEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avWlanSystemConfigWirelessEnabled.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemConfigWirelessEnabled.setDescription('This is used to enable wireless feature (control and data together in first release). System Interface and TcpUdpBasePort will be taken as parameters to this action. Disable will purge all status and statistics related to wireless functionality. A value of true(1) means enabled.')
avWlanSystemConfigSystemInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avWlanSystemConfigSystemInetAddressType.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemConfigSystemInetAddressType.setDescription('This object indicates the type of address contained in the object avWlanSystemConfigSystemInetAddress.')
avWlanSystemConfigSystemInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avWlanSystemConfigSystemInetAddress.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemConfigSystemInetAddress.setDescription('This address is the one to be used by the WC and/or MS for connecting to APs and Peer WCs and/or MS. All tunnels are also terminated on this address. Captive Portal Web Server is also hosted on this address. Wireless feature should be disabled and enabled for changing this value. There is no default value and this configuration is mandatory to enable a WC and/or an MS to participate in a WLAN Domain.')
avWlanSystemConfigTcpUdpBasePort = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(49152, 64983)).clone(61000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avWlanSystemConfigTcpUdpBasePort.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemConfigTcpUdpBasePort.setDescription('All WLAN System Protocols (e.g. AP, MS, WC control channel, access and mobility tunnels etc.) use different TCP and UDP port numbers. These ports are based at different fixed offsets from a base port allowing administrator to create simple firewall rules by opening a contiguous ip port range for WLAN communication. Currently a range of 16 ports starting from this base port will be used. The base port must be same on all WCs and/or MS in a domain. This is an optional configuration and all WCs can be left operating at the default value. Changing this configuration will require to disable and enable wireless feature.')
avWlanSystemStatusScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1))
avWlanSystemStatusOperationalStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("enablePending", 2), ("disabled", 3), ("disablePending", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avWlanSystemStatusOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemStatusOperationalStatus.setDescription('Indicates the current operating status of the wireless system.')
avWlanSystemStatusOperationalStatusDisableReason = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("adminDisabled", 2), ("routingDisabled", 3), ("badSystemInetAddress", 4), ("badTcpUdpBasePort", 5), ("wirelessSystemError", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avWlanSystemStatusOperationalStatusDisableReason.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemStatusOperationalStatusDisableReason.setDescription('This object indicates the reason why the operational status is disabled.')
avWlanSystemStatusWlanSystemAddrType = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avWlanSystemStatusWlanSystemAddrType.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemStatusWlanSystemAddrType.setDescription('The type of address contained in avWlanSystemStatusWlanSystemAddr. Currently only unknown(0), ipv4(1), and ipv6(2) are allowed. When the wireless mode is in the disabled state, the value of this object will be unknown(0).')
avWlanSystemStatusWlanSystemAddr = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 4), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avWlanSystemStatusWlanSystemAddr.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemStatusWlanSystemAddr.setDescription('This object represents the WC/WS WLAN System IP address. When the wireless mode is in disabled state, the value of this object will be empty.')
avWlanSystemStatusOperationalRole = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("wcp", 1), ("wsp", 2), ("wcpAndwsp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avWlanSystemStatusOperationalRole.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemStatusOperationalRole.setDescription("The current operational role of the WLAN system running on this device. Only applicable when the value of the avWlanSystemStatusOperationalStatus is 'enabled(1)'. The meaning of the values is: wcp(1) - device is running Control plane only wsp(2) - device is running Data plane only wcpAndwsp(3) - device is running both Control and Data planes ")
avWlanSystemStatusWlanVersion = MibScalar((1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avWlanSystemStatusWlanVersion.setStatus('current')
if mibBuilder.loadTexts: avWlanSystemStatusWlanVersion.setDescription('Reflects the current WLAN MIB version implemented by this device. Not to be confused with the software version of the device. Primarily meant to be used by the WLAN management applications.')
mibBuilder.exportSymbols("AVAYA-WLAN-SYSTEM-MIB", PYSNMP_MODULE_ID=avayaWlanSystemMib, avWlanSystemConfig=avWlanSystemConfig, avWlanSystemStatusScalars=avWlanSystemStatusScalars, avWlanSystemStatusOperationalStatus=avWlanSystemStatusOperationalStatus, avWlanSystemStatusOperationalStatusDisableReason=avWlanSystemStatusOperationalStatusDisableReason, avWlanSystemConfigTcpUdpBasePort=avWlanSystemConfigTcpUdpBasePort, avWlanSystemStatusWlanVersion=avWlanSystemStatusWlanVersion, avWlanSystemConfigScalars=avWlanSystemConfigScalars, avWlanSystemConfigWirelessEnabled=avWlanSystemConfigWirelessEnabled, avWlanSystemStatusWlanSystemAddrType=avWlanSystemStatusWlanSystemAddrType, avWlanSystemStatus=avWlanSystemStatus, avWlanSystemStatusOperationalRole=avWlanSystemStatusOperationalRole, avWlanSystemStatusWlanSystemAddr=avWlanSystemStatusWlanSystemAddr, avWlanSystemObjects=avWlanSystemObjects, avWlanSystemConfigSystemInetAddressType=avWlanSystemConfigSystemInetAddressType, avWlanSystemConfigSystemInetAddress=avWlanSystemConfigSystemInetAddress, avayaWlanSystemMib=avayaWlanSystemMib)