#
# PySNMP MIB module CISCO-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, ModuleIdentity, Bits, Gauge32, MibIdentifier, Counter32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Bits", "Gauge32", "MibIdentifier", "Counter32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoRFCapability.setRevisions(('2003-08-20 00:00', '2001-01-04 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFCapability.setRevisionsDescriptions(('Added ciscoRFCapabilityV12R0111bEXCat6k, ciscoRFCapabilityV12R0113ECat6k, and ciscoRFCapabilityCatOSV8R0101Cat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFCapability.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: ciscoRFCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-rf-mib@cisco.com ')
if mibBuilder.loadTexts: ciscoRFCapability.setDescription('Added agent Capabilities for CISCO-RF-MIB shipped as part of the Cisco IOS 12.1 release. ')
ciscoRFCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityV12R01.setDescription('Cisco RF MIB capabilities')
ciscoRFCapabilityV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11bEX) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityV12R0111bEXCat6k.setDescription('CISCO-RF-MIB capabilities.')
ciscoRFCapabilityV12R0113ECat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityV12R0113ECat6k.setDescription('CISCO-RF-MIB capabilities.')
ciscoRFCapabilityCatOSV8R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoRFCapabilityCatOSV8R0101Cat6K.setDescription('CISCO-RF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RF-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFCapability, ciscoRFCapabilityV12R0111bEXCat6k=ciscoRFCapabilityV12R0111bEXCat6k, ciscoRFCapabilityCatOSV8R0101Cat6K=ciscoRFCapabilityCatOSV8R0101Cat6K, ciscoRFCapability=ciscoRFCapability, ciscoRFCapabilityV12R01=ciscoRFCapabilityV12R01, ciscoRFCapabilityV12R0113ECat6k=ciscoRFCapabilityV12R0113ECat6k)
