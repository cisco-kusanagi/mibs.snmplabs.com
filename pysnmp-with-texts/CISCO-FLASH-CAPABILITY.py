#
# PySNMP MIB module CISCO-FLASH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLASH-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:58:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, IpAddress, TimeTicks, Counter32, ObjectIdentity, iso, Counter64, Gauge32, MibIdentifier, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "Counter32", "ObjectIdentity", "iso", "Counter64", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFlashCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 222))
ciscoFlashCapability.setRevisions(('2008-01-18 00:00', '2004-04-01 00:00', '2003-10-21 00:00', '2001-09-25 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlashCapability.setRevisionsDescriptions(('Added ciscoFlashMibCapXRV03R06PCRS1 agent capability statement.', 'Added ciscoFlashMibCapCatOSV08R0301.', 'Added ciscoFlashMibCapCatOSV7R0501Cat6k, and ciscoFlashMibCapV12R0113ECat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFlashCapability.setLastUpdated('200801180000Z')
if mibBuilder.loadTexts: ciscoFlashCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlashCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlashCapability.setDescription('Agent capabilities for CISCO-FLASH-MIB')
ciscoFlashCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashCapabilityV12R00S.setDescription('CISCO-FLASH-MIB capabilities')
ciscoFlashCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashCapabilityV12R01.setDescription('CISCO-FLASH-MIB capabilities')
ciscoFlashCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashCapabilityV12R02.setDescription('CISCO-FLASH-MIB capabilities')
ciscoFlashMibCapCatOSV7R0501Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setProductRelease('Cisco CatOS 7.5(1) on  Catalyst 4000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashMibCapCatOSV7R0501Cat4k.setDescription('CISCO-FLASH-MIB capabilities.')
ciscoFlashMibCapCatOSV7R0501Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashMibCapCatOSV7R0501Cat6k.setDescription('CISCO-FLASH-MIB capabilities.')
ciscoFlashMibCapV12R0113ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500 and Cisco\n                7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashMibCapV12R0113ECat6K.setDescription('CISCO-FLASH-MIB capabilities.')
ciscoFlashMibCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1)on Catalyst 6000/6500\n                and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashMibCapCatOSV08R0301.setDescription('CISCO-FLASH-MIB capabilities.')
ciscoFlashMibCapXRV03R06PCRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoFlashMibCapXRV03R06PCRS1.setDescription('CISCO-FLASH-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-FLASH-CAPABILITY", PYSNMP_MODULE_ID=ciscoFlashCapability, ciscoFlashMibCapCatOSV7R0501Cat4k=ciscoFlashMibCapCatOSV7R0501Cat4k, ciscoFlashCapabilityV12R00S=ciscoFlashCapabilityV12R00S, ciscoFlashMibCapCatOSV7R0501Cat6k=ciscoFlashMibCapCatOSV7R0501Cat6k, ciscoFlashCapability=ciscoFlashCapability, ciscoFlashMibCapV12R0113ECat6K=ciscoFlashMibCapV12R0113ECat6K, ciscoFlashCapabilityV12R01=ciscoFlashCapabilityV12R01, ciscoFlashMibCapXRV03R06PCRS1=ciscoFlashMibCapXRV03R06PCRS1, ciscoFlashCapabilityV12R02=ciscoFlashCapabilityV12R02, ciscoFlashMibCapCatOSV08R0301=ciscoFlashMibCapCatOSV08R0301)
