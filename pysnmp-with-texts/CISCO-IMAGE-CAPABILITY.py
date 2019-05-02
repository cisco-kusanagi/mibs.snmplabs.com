#
# PySNMP MIB module CISCO-IMAGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, ObjectIdentity, iso, TimeTicks, Integer32, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, IpAddress, Counter64, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "TimeTicks", "Integer32", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "IpAddress", "Counter64", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoImageMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 580))
ciscoImageMIBCapability.setRevisions(('2009-03-26 00:00', '2003-09-15 00:00', '1995-01-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImageMIBCapability.setRevisionsDescriptions(('Added ciscoImageCapabilityGssV03R01 agent capabilities for Global Site Selector(GSS) release 3.1(0).', '-- Add the capabilities of IOS versions 12.1(19E) and 12.2(17SX) for Catalyst 6000/6500 and Cisco 7600 series devices. -- Add the capability of CatOS version 8.1(1).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImageMIBCapability.setLastUpdated('200903260000Z')
if mibBuilder.loadTexts: ciscoImageMIBCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImageMIBCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoImageMIBCapability.setDescription('Agent capabilities for CISCO-IMAGE-MIB.')
ciscoImageMIBCapabilityV10R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBCapabilityV10R01.setDescription('ciscoImageMIB capabilites')
ciscoImageCapabilityV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCapabilityV12R0119ECat6K.setDescription('CISCO-IMAGE-MIB capabilities.')
ciscoImageCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCapabilityV12R0217SXCat6K.setDescription('CISCO-IMAGE-MIB capabilities.')
ciscoImageCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCapabilityCatOSV08R0101.setDescription('CISCO-IMAGE-MIB capabilities.')
ciscoImageCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCapabilityGssV03R01.setDescription('CISCO-IMAGE-MIB capabilities for GSS 3.1(0)')
mibBuilder.exportSymbols("CISCO-IMAGE-CAPABILITY", ciscoImageCapabilityV12R0119ECat6K=ciscoImageCapabilityV12R0119ECat6K, ciscoImageCapabilityV12R0217SXCat6K=ciscoImageCapabilityV12R0217SXCat6K, ciscoImageMIBCapability=ciscoImageMIBCapability, ciscoImageCapabilityGssV03R01=ciscoImageCapabilityGssV03R01, ciscoImageCapabilityCatOSV08R0101=ciscoImageCapabilityCatOSV08R0101, PYSNMP_MODULE_ID=ciscoImageMIBCapability, ciscoImageMIBCapabilityV10R01=ciscoImageMIBCapabilityV10R01)
