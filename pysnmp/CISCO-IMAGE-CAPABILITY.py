#
# PySNMP MIB module CISCO-IMAGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, iso, MibIdentifier, Gauge32, Unsigned32, IpAddress, TimeTicks, Bits, ObjectIdentity, ModuleIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "iso", "MibIdentifier", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoImageMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 580))
ciscoImageMIBCapability.setRevisions(('2009-03-26 00:00', '2003-09-15 00:00', '1995-01-25 00:00',))
if mibBuilder.loadTexts: ciscoImageMIBCapability.setLastUpdated('200903260000Z')
if mibBuilder.loadTexts: ciscoImageMIBCapability.setOrganization('Cisco Systems, Inc.')
ciscoImageMIBCapabilityV10R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setStatus('current')
ciscoImageCapabilityV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setStatus('current')
ciscoImageCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setStatus('current')
ciscoImageCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setStatus('current')
ciscoImageCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-CAPABILITY", ciscoImageMIBCapability=ciscoImageMIBCapability, ciscoImageCapabilityV12R0217SXCat6K=ciscoImageCapabilityV12R0217SXCat6K, ciscoImageCapabilityGssV03R01=ciscoImageCapabilityGssV03R01, ciscoImageCapabilityV12R0119ECat6K=ciscoImageCapabilityV12R0119ECat6K, PYSNMP_MODULE_ID=ciscoImageMIBCapability, ciscoImageMIBCapabilityV10R01=ciscoImageMIBCapabilityV10R01, ciscoImageCapabilityCatOSV08R0101=ciscoImageCapabilityCatOSV08R0101)
