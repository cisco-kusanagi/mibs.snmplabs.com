#
# PySNMP MIB module CISCO-DS3-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS3-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, Integer32, TimeTicks, ModuleIdentity, Counter32, MibIdentifier, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "ModuleIdentity", "Counter32", "MibIdentifier", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs3Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 265))
ciscoDs3Capability.setRevisions(('2004-05-06 00:00', '2003-12-22 00:00', '2003-03-12 00:00', '2002-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDs3Capability.setRevisionsDescriptions(('Modified MPSM agent capability description.', 'Added ciscoDs3CapabilityV5R00.', 'Added ciscoDs3CapabilityV4R00 for modules: 10 Gig. ATM Switch Service Module(AXSM-XG), AXSM Service Module Enhanced(AXSM-E) and Processor Switch Module Enhanced(PXM1E) controller card.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDs3Capability.setLastUpdated('200405060000Z')
if mibBuilder.loadTexts: ciscoDs3Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDs3Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoDs3Capability.setDescription('The Agent Capabilities for DS3-MIB(RFC 2496).')
ciscoDs3CapabilityV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityV2R0100.setDescription('DS3 MIB Capabilities for Following Modules: ATM Switch Service Module(AXSM). AXSM-E(AXSM Enhanced).')
ciscoDs3CapabilitySrmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilitySrmV3R00.setDescription('DS3 MIB Capabilities for Service Resource Module(SRM).')
ciscoDs3CapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityPxm1eV3R00.setDescription('DS3 MIB Capabilities for Processor Switch Module Enhanced (PXM1E) controller card.')
ciscoDs3CapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityV4R00.setDescription('DS3 MIB Capabilities for Modules: 10 Gig. ATM Switch Service Module(AXSM-XG), AXSM Service Module Enhanced(AXSM-E) and Processor Switch Module Enhanced(PXM1E) controller card.')
ciscoDs3CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityV5R00.setDescription('DS3 MIB capabilities for Voice Switch Service Module(VXSM) and MPSM in release 5.0.0')
mibBuilder.exportSymbols("CISCO-DS3-CAPABILITY", ciscoDs3Capability=ciscoDs3Capability, ciscoDs3CapabilitySrmV3R00=ciscoDs3CapabilitySrmV3R00, ciscoDs3CapabilityV5R00=ciscoDs3CapabilityV5R00, ciscoDs3CapabilityV4R00=ciscoDs3CapabilityV4R00, ciscoDs3CapabilityV2R0100=ciscoDs3CapabilityV2R0100, ciscoDs3CapabilityPxm1eV3R00=ciscoDs3CapabilityPxm1eV3R00, PYSNMP_MODULE_ID=ciscoDs3Capability)
