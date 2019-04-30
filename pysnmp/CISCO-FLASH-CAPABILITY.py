#
# PySNMP MIB module CISCO-FLASH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLASH-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
NotificationType, ObjectIdentity, Bits, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, TimeTicks, IpAddress, ModuleIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Bits", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "TimeTicks", "IpAddress", "ModuleIdentity", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoFlashCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 222))
ciscoFlashCapability.setRevisions(('2008-01-18 00:00', '2004-04-01 00:00', '2003-10-21 00:00', '2001-09-25 12:34',))
if mibBuilder.loadTexts: ciscoFlashCapability.setLastUpdated('200801180000Z')
if mibBuilder.loadTexts: ciscoFlashCapability.setOrganization('Cisco Systems, Inc.')
ciscoFlashCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setStatus('current')
ciscoFlashCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setStatus('current')
ciscoFlashCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setStatus('current')
ciscoFlashMibCapCatOSV7R0501Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setProductRelease('Cisco CatOS 7.5(1) on  Catalyst 4000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setStatus('current')
ciscoFlashMibCapCatOSV7R0501Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setStatus('current')
ciscoFlashMibCapV12R0113ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500 and Cisco\n                7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setStatus('current')
ciscoFlashMibCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1)on Catalyst 6000/6500\n                and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setStatus('current')
ciscoFlashMibCapXRV03R06PCRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLASH-CAPABILITY", ciscoFlashCapabilityV12R00S=ciscoFlashCapabilityV12R00S, ciscoFlashMibCapXRV03R06PCRS1=ciscoFlashMibCapXRV03R06PCRS1, ciscoFlashCapability=ciscoFlashCapability, ciscoFlashMibCapV12R0113ECat6K=ciscoFlashMibCapV12R0113ECat6K, ciscoFlashMibCapCatOSV08R0301=ciscoFlashMibCapCatOSV08R0301, ciscoFlashCapabilityV12R02=ciscoFlashCapabilityV12R02, ciscoFlashMibCapCatOSV7R0501Cat6k=ciscoFlashMibCapCatOSV7R0501Cat6k, PYSNMP_MODULE_ID=ciscoFlashCapability, ciscoFlashMibCapCatOSV7R0501Cat4k=ciscoFlashMibCapCatOSV7R0501Cat4k, ciscoFlashCapabilityV12R01=ciscoFlashCapabilityV12R01)
