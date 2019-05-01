#
# PySNMP MIB module CISCO-ENTITY-FRU-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-FRU-CONTROL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, iso, Unsigned32, Bits, ObjectIdentity, Gauge32, ModuleIdentity, TimeTicks, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Unsigned32", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "TimeTicks", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityFruControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 264))
ciscoEntityFruControlCapability.setRevisions(('2011-09-25 00:00', '2009-12-14 00:00', '2009-07-30 00:00', '2009-03-25 00:00', '2009-03-11 00:00', '2008-10-28 00:00', '2008-03-24 00:00', '2007-09-06 00:00', '2007-08-31 00:00', '2007-07-19 00:00', '2006-06-21 00:00', '2006-04-19 00:00', '2006-03-16 00:00', '2006-01-31 00:00', '2005-07-12 00:00', '2005-03-09 00:00', '2004-09-15 00:00', '2004-01-15 00:00', '2003-09-15 00:00', '2002-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityFruControlCapability.setRevisionsDescriptions(('Added capabilities ciscoEfcCapV15R0001SYPCat6K.', 'Added capability ciscoEfcCapV15R01TP39XXE', 'Added capabilities for ciscoEfcCapV12R04TP3925E, and ciscoEfcCapV12R04TP3945E', 'Added capabilities for ciscoEfcCapV12R04TP3845nv, ciscoEfcCapV12R04TP3825nv, ciscoEfcCapV12R04TP1941, ciscoEfcCapV12R04TP29XX, ciscoEfcCapV12R04TP3925 and ciscoEfcCapV12R04TP3945', 'The capability statement ciscoEfcCapIOSXRV3R08CRS1 has been added.', 'Added capabilities ciscoEfcCapV12R0233SXIPCat6K.', 'The capability statement ciscoEfcCapIOSXRV3R06CRS1 has been added.', 'Added capabilities ciscoEfcCapabilityV12R05TP32xx for 3200 platform.', 'Added capabilities ciscoEfcCapV12R0233SXHPCat6K.', 'Added capabilities ciscoEfcCapabilityV05R05PMGX8850 for MGX8850 platform.', '- Added capabilities ciscoEfcCapV12R05TP18xx and ciscoEfcCapV12R05TP2801 for IOS 12.4T on platforms 18xx and 2801.', '- Added Agent capabilities ciscoEfcCapACSWV03R000 for Cisco Application Control Engine (ACE).', '- Add VARIATIONs for notifications cefcModuleStatusChange, cefcPowerStatusChange, cefcFRUInserted and cefcFRURemoved in ciscoEfcCapabilityCatOSV08R0101, ciscoEfcCapabilityCatOSV08R0301 and ciscoEfcCapCatOSV08R0501.', '- Added ciscoEfcCapSanOSV21R1MDS9000 for SAN OS 2.1(1) on MDS 9000 series devices. - Added ciscoEfcCapSanOSV30R1MDS9000 for SAN OS 3.0(1) on MDS 9000 series devices.', '- Added ciscoEfcCapCatOSV08R0501.', '- Added capabilities ciscoEfcCapV12R04TP26XX ciscoEfcCapV12R04TP28XX, ciscoEfcCapV12R04TP3725, ciscoEfcCapV12R04TP3745, ciscoEfcCapV12R04TP3825, ciscoEfcCapV12R04TP3845, ciscoEfcCapV12R04TPIAD243X, ciscoEfcCapV12R04TPVG224 for IOS 12.4T on platforms 26xx, 28xx, 37xx, 38xx, IAD243x, VG224', '- Added ciscoEfcCapabilityV12R03P5XXX for IOS 12.3 on Access Server Platforms (AS5350, AS5400 and AS5850).', '- Added ciscoEfcCapV12RO217bSXACat6K. - Added ciscoEfcCapabilityCatOSV08R0301.', '- Added ciscoEfcCapabilityV12R0119ECat6K for IOS 12.1(19E) on Catalyst 6000/6500 and Cisco 7600 series devices. - Added ciscoEfcCapabilityV12RO217SXCat6K for IOS 12.2(17SX) on Catalyst 6000/6500 and Cisco 7600 series devices. - Added ciscoEfcCapabilityCatOSV08R0101 for Cisco CatOS 8.1(1).', 'Initial version of the MIB Module. - The ciscoEntityFruControlCapabilityV2R00 is for MGX8850 and BPX SES platform. - The ciscoEntityFRUControlCapabilityV12R00SGSR is for GSR platform.',))
if mibBuilder.loadTexts: ciscoEntityFruControlCapability.setLastUpdated('201109250000Z')
if mibBuilder.loadTexts: ciscoEntityFruControlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityFruControlCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityFruControlCapability.setDescription('The Agent Capabilities for CISCO-ENTITY-FRU-CONTROL-MIB.')
ciscoEntityFruControlCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityFruControlCapabilityV2R00 = ciscoEntityFruControlCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                          BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityFruControlCapabilityV2R00 = ciscoEntityFruControlCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityFruControlCapabilityV2R00.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB Capabilities')
ciscoEntityFRUControlCapabilityV12R00SGSR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityFRUControlCapabilityV12R00SGSR = ciscoEntityFRUControlCapabilityV12R00SGSR.setProductRelease('Cisco IOS 12.0S for GSR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityFRUControlCapabilityV12R00SGSR = ciscoEntityFRUControlCapabilityV12R00SGSR.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityFRUControlCapabilityV12R00SGSR.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities for GSR platform.')
ciscoEfcCapabilityV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12R0119ECat6K = ciscoEfcCapabilityV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12R0119ECat6K = ciscoEfcCapabilityV12R0119ECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityV12R0119ECat6K.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapabilityV12RO217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12RO217SXCat6K = ciscoEfcCapabilityV12RO217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12RO217SXCat6K = ciscoEfcCapabilityV12RO217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityV12RO217SXCat6K.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityCatOSV08R0101 = ciscoEfcCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityCatOSV08R0101 = ciscoEfcCapabilityCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityCatOSV08R0101.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapV12RO217bSXACat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12RO217bSXACat6K = ciscoEfcCapV12RO217bSXACat6K.setProductRelease('Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12RO217bSXACat6K = ciscoEfcCapV12RO217bSXACat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12RO217bSXACat6K.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityCatOSV08R0301 = ciscoEfcCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityCatOSV08R0301 = ciscoEfcCapabilityCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityCatOSV08R0301.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapabilityV12R03P5XXX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12R03P5XXX = ciscoEfcCapabilityV12R03P5XXX.setProductRelease('Cisco IOS 12.3 for Access Server Platforms\n                      AS5350, AS5400 and AS5850.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12R03P5XXX = ciscoEfcCapabilityV12R03P5XXX.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityV12R03P5XXX.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapV12R04TP3725 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3725 = ciscoEfcCapV12R04TP3725.setProductRelease('Cisco IOS 12.4T for c3725 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3725 = ciscoEfcCapV12R04TP3725.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3725.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapV12R04TP3745 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3745 = ciscoEfcCapV12R04TP3745.setProductRelease('Cisco IOS 12.4T for c3745 Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3745 = ciscoEfcCapV12R04TP3745.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3745.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP26XX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP26XX = ciscoEfcCapV12R04TP26XX.setProductRelease('Cisco IOS 12.4T for c26xx XM Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP26XX = ciscoEfcCapV12R04TP26XX.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP26XX.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TPIAD243X = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TPIAD243X = ciscoEfcCapV12R04TPIAD243X.setProductRelease('Cisco IOS 12.4T for IAD 243x Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TPIAD243X = ciscoEfcCapV12R04TPIAD243X.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TPIAD243X.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TPVG224 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TPVG224 = ciscoEfcCapV12R04TPVG224.setProductRelease('Cisco IOS 12.4T for VG224 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TPVG224 = ciscoEfcCapV12R04TPVG224.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TPVG224.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP2691 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP2691 = ciscoEfcCapV12R04TP2691.setProductRelease('Cisco IOS 12.4T for c2691 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP2691 = ciscoEfcCapV12R04TP2691.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP2691.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP28XX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP28XX = ciscoEfcCapV12R04TP28XX.setProductRelease('Cisco IOS 12.4T for c28xx Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP28XX = ciscoEfcCapV12R04TP28XX.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP28XX.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP3825 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3825 = ciscoEfcCapV12R04TP3825.setProductRelease('Cisco IOS 12.4T for c3825 Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3825 = ciscoEfcCapV12R04TP3825.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3825.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP3845 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3845 = ciscoEfcCapV12R04TP3845.setProductRelease('Cisco IOS 12.4T for c3845 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3845 = ciscoEfcCapV12R04TP3845.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3845.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapCatOSV08R0501 = ciscoEfcCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapCatOSV08R0501 = ciscoEfcCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapCatOSV08R0501.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapSanOSV21R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapSanOSV21R1MDS9000 = ciscoEfcCapSanOSV21R1MDS9000.setProductRelease('Cisco SanOS 2.1(1) on Cisco MDS 9000 series\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapSanOSV21R1MDS9000 = ciscoEfcCapSanOSV21R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapSanOSV21R1MDS9000.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapSanOSV30R1MDS9000 = ciscoEfcCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000 series\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapSanOSV30R1MDS9000 = ciscoEfcCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapSanOSV30R1MDS9000.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapACSWV03R000 = ciscoEfcCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapACSWV03R000 = ciscoEfcCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapACSWV03R000.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapV12R05TP18xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R05TP18xx = ciscoEfcCapV12R05TP18xx.setProductRelease('Cisco IOS 12.5T for c18xx Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R05TP18xx = ciscoEfcCapV12R05TP18xx.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R05TP18xx.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R05TP2801 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R05TP2801 = ciscoEfcCapV12R05TP2801.setProductRelease('Cisco IOS 12.5T for c2801 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R05TP2801 = ciscoEfcCapV12R05TP2801.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R05TP2801.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapabilityV05R05PMGX8850 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV05R05PMGX8850 = ciscoEfcCapabilityV05R05PMGX8850.setProductRelease('MGX8850 Release 5.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV05R05PMGX8850 = ciscoEfcCapabilityV05R05PMGX8850.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityV05R05PMGX8850.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB Capabilities for the following modules of MGX8850: AXSM-XG, MPSM-T3E3-155, MPSM-16-T1E1, PXM1E, PXM45, VXSM and VISM.')
ciscoEfcCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R0233SXHPCat6K = ciscoEfcCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R0233SXHPCat6K = ciscoEfcCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R0233SXHPCat6K.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapabilityV12R05TP32xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12R05TP32xx = ciscoEfcCapabilityV12R05TP32xx.setProductRelease('Cisco IOS 12.5T for Cisco 3200 series routers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapabilityV12R05TP32xx = ciscoEfcCapabilityV12R05TP32xx.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapabilityV12R05TP32xx.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities for 3220, 3250 and 3270 routers.')
ciscoEfcCapIOSXRV3R06CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapIOSXRV3R06CRS1 = ciscoEfcCapIOSXRV3R06CRS1.setProductRelease('Cisco IOS-XR Release 3.6 for CRS-1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapIOSXRV3R06CRS1 = ciscoEfcCapIOSXRV3R06CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapIOSXRV3R06CRS1.setDescription('Agent capabilities for IOS-XR Release 3.6 for CRS-1.')
ciscoEfcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R0233SXIPCat6K = ciscoEfcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R0233SXIPCat6K = ciscoEfcCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R0233SXIPCat6K.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
ciscoEfcCapIOSXRV3R08CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapIOSXRV3R08CRS1 = ciscoEfcCapIOSXRV3R08CRS1.setProductRelease('Cisco IOS-XR Release 3.8 for CRS-1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapIOSXRV3R08CRS1 = ciscoEfcCapIOSXRV3R08CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapIOSXRV3R08CRS1.setDescription('Agent capabilities for IOS-XR Release 3.8 for CRS-1.')
ciscoEfcCapV12R04TP3845nv = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3845nv = ciscoEfcCapV12R04TP3845nv.setProductRelease('Cisco IOS 12.4(22)YB1 for c3845nv Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3845nv = ciscoEfcCapV12R04TP3845nv.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3845nv.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP3825nv = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3825nv = ciscoEfcCapV12R04TP3825nv.setProductRelease('Cisco IOS 12.4(22)YB1 for c3825nv Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3825nv = ciscoEfcCapV12R04TP3825nv.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3825nv.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP1941 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP1941 = ciscoEfcCapV12R04TP1941.setProductRelease('Cisco IOS 12.4T for c1941 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP1941 = ciscoEfcCapV12R04TP1941.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP1941.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP29XX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP29XX = ciscoEfcCapV12R04TP29XX.setProductRelease('Cisco IOS 12.4T for c29xx Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP29XX = ciscoEfcCapV12R04TP29XX.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP29XX.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP3925 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3925 = ciscoEfcCapV12R04TP3925.setProductRelease('Cisco IOS 12.4T for c3925 Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3925 = ciscoEfcCapV12R04TP3925.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3925.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV12R04TP3945 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3945 = ciscoEfcCapV12R04TP3945.setProductRelease('Cisco IOS 12.4T for c3945 Platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV12R04TP3945 = ciscoEfcCapV12R04TP3945.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV12R04TP3945.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV15R01TP39XXE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV15R01TP39XXE = ciscoEfcCapV15R01TP39XXE.setProductRelease('Cisco IOS 15.1T for c3925SPE200/c3925SPE250\n                      c3945SPE200/c3945SPE250 Platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV15R01TP39XXE = ciscoEfcCapV15R01TP39XXE.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV15R01TP39XXE.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities')
ciscoEfcCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 264, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV15R0001SYPCat6K = ciscoEfcCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEfcCapV15R0001SYPCat6K = ciscoEfcCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEfcCapV15R0001SYPCat6K.setDescription('CISCO-ENTITY-FRU-CONTROL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-FRU-CONTROL-CAPABILITY", ciscoEfcCapV12R04TP3745=ciscoEfcCapV12R04TP3745, ciscoEfcCapV12R04TP3925=ciscoEfcCapV12R04TP3925, ciscoEfcCapV12RO217bSXACat6K=ciscoEfcCapV12RO217bSXACat6K, ciscoEfcCapV12R04TPIAD243X=ciscoEfcCapV12R04TPIAD243X, ciscoEfcCapV12R05TP2801=ciscoEfcCapV12R05TP2801, ciscoEfcCapIOSXRV3R08CRS1=ciscoEfcCapIOSXRV3R08CRS1, PYSNMP_MODULE_ID=ciscoEntityFruControlCapability, ciscoEfcCapabilityV12R0119ECat6K=ciscoEfcCapabilityV12R0119ECat6K, ciscoEfcCapACSWV03R000=ciscoEfcCapACSWV03R000, ciscoEfcCapV12R04TP2691=ciscoEfcCapV12R04TP2691, ciscoEfcCapV12R04TP1941=ciscoEfcCapV12R04TP1941, ciscoEfcCapV12R04TP28XX=ciscoEfcCapV12R04TP28XX, ciscoEfcCapSanOSV21R1MDS9000=ciscoEfcCapSanOSV21R1MDS9000, ciscoEntityFruControlCapability=ciscoEntityFruControlCapability, ciscoEfcCapV15R0001SYPCat6K=ciscoEfcCapV15R0001SYPCat6K, ciscoEfcCapabilityCatOSV08R0101=ciscoEfcCapabilityCatOSV08R0101, ciscoEfcCapV12R04TPVG224=ciscoEfcCapV12R04TPVG224, ciscoEfcCapV12R04TP3845=ciscoEfcCapV12R04TP3845, ciscoEfcCapCatOSV08R0501=ciscoEfcCapCatOSV08R0501, ciscoEfcCapV12R04TP26XX=ciscoEfcCapV12R04TP26XX, ciscoEfcCapabilityV05R05PMGX8850=ciscoEfcCapabilityV05R05PMGX8850, ciscoEfcCapV12R04TP3725=ciscoEfcCapV12R04TP3725, ciscoEfcCapV12R04TP3825=ciscoEfcCapV12R04TP3825, ciscoEntityFRUControlCapabilityV12R00SGSR=ciscoEntityFRUControlCapabilityV12R00SGSR, ciscoEfcCapSanOSV30R1MDS9000=ciscoEfcCapSanOSV30R1MDS9000, ciscoEfcCapV12R0233SXHPCat6K=ciscoEfcCapV12R0233SXHPCat6K, ciscoEfcCapV15R01TP39XXE=ciscoEfcCapV15R01TP39XXE, ciscoEfcCapIOSXRV3R06CRS1=ciscoEfcCapIOSXRV3R06CRS1, ciscoEfcCapV12R05TP18xx=ciscoEfcCapV12R05TP18xx, ciscoEfcCapabilityV12RO217SXCat6K=ciscoEfcCapabilityV12RO217SXCat6K, ciscoEfcCapV12R04TP29XX=ciscoEfcCapV12R04TP29XX, ciscoEfcCapV12R04TP3945=ciscoEfcCapV12R04TP3945, ciscoEfcCapV12R0233SXIPCat6K=ciscoEfcCapV12R0233SXIPCat6K, ciscoEfcCapabilityV12R05TP32xx=ciscoEfcCapabilityV12R05TP32xx, ciscoEfcCapV12R04TP3825nv=ciscoEfcCapV12R04TP3825nv, ciscoEntityFruControlCapabilityV2R00=ciscoEntityFruControlCapabilityV2R00, ciscoEfcCapabilityV12R03P5XXX=ciscoEfcCapabilityV12R03P5XXX, ciscoEfcCapabilityCatOSV08R0301=ciscoEfcCapabilityCatOSV08R0301, ciscoEfcCapV12R04TP3845nv=ciscoEfcCapV12R04TP3845nv)
