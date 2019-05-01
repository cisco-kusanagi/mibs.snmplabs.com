#
# PySNMP MIB module CISCO-WLAN-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WLAN-MAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:21:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Counter32, NotificationType, Unsigned32, iso, ModuleIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Integer32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "NotificationType", "Unsigned32", "iso", "ModuleIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Integer32", "ObjectIdentity", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoWlanManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 415))
ciscoWlanManMIB.setRevisions(('2004-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWlanManMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWlanManMIB.setLastUpdated('200403220000Z')
if mibBuilder.loadTexts: ciscoWlanManMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoWlanManMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS Email: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoWlanManMIB.setDescription('This MIB module provides network management and configuration support for IEEE 802.11 Wireless LAN devices. ACRONYMS HTTP Hypertext Transfer Protocol.')
ciscoWlanManMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 0))
ciscoWlanManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1))
ciscoWlanManMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2))
cwmDeviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1))
cwmNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 2))
cwmHttpServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmHttpServerEnabled.setStatus('current')
if mibBuilder.loadTexts: cwmHttpServerEnabled.setDescription("This object enables the HTTP Web server as follows: 'true' - HTTP Web server function is enabled, 'false' - HTTP Web server function is disabled.")
cwmTelnetLoginEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setStatus('current')
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setDescription("This object enables the telnet console login as follows: 'true' - telnet console login is enabled, 'false' - telnet console login is disabled.")
ciscoWlanManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1))
ciscoWlanManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2))
ciscoWlanManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmWirelessDeviceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanManMIBCompliance = ciscoWlanManMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWlanManMIBCompliance.setDescription('The compliance statement for the ciscoWlanManMIB module.')
cwmWirelessDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmHttpServerEnabled"), ("CISCO-WLAN-MAN-MIB", "cwmTelnetLoginEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWirelessDeviceGroup = cwmWirelessDeviceGroup.setStatus('current')
if mibBuilder.loadTexts: cwmWirelessDeviceGroup.setDescription('Configuration for Wireless LAN Access Points and bridges.')
mibBuilder.exportSymbols("CISCO-WLAN-MAN-MIB", cwmWirelessDeviceGroup=cwmWirelessDeviceGroup, cwmHttpServerEnabled=cwmHttpServerEnabled, cwmTelnetLoginEnabled=cwmTelnetLoginEnabled, ciscoWlanManMIBObjects=ciscoWlanManMIBObjects, ciscoWlanManMIB=ciscoWlanManMIB, cwmNetworkConfig=cwmNetworkConfig, ciscoWlanManMIBConform=ciscoWlanManMIBConform, PYSNMP_MODULE_ID=ciscoWlanManMIB, ciscoWlanManMIBNotifs=ciscoWlanManMIBNotifs, cwmDeviceConfig=cwmDeviceConfig, ciscoWlanManMIBGroups=ciscoWlanManMIBGroups, ciscoWlanManMIBCompliance=ciscoWlanManMIBCompliance, ciscoWlanManMIBCompliances=ciscoWlanManMIBCompliances)
