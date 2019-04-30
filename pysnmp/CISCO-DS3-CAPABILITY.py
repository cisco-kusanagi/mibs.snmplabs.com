#
# PySNMP MIB module CISCO-DS3-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS3-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, MibIdentifier, Counter32, IpAddress, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Counter64, iso, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Counter32", "IpAddress", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Counter64", "iso", "NotificationType", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs3Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 265))
ciscoDs3Capability.setRevisions(('2004-05-06 00:00', '2003-12-22 00:00', '2003-03-12 00:00', '2002-05-01 00:00',))
if mibBuilder.loadTexts: ciscoDs3Capability.setLastUpdated('200405060000Z')
if mibBuilder.loadTexts: ciscoDs3Capability.setOrganization('Cisco Systems, Inc.')
ciscoDs3CapabilityV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setStatus('current')
ciscoDs3CapabilitySrmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setStatus('current')
ciscoDs3CapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setStatus('current')
ciscoDs3CapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setStatus('current')
ciscoDs3CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS3-CAPABILITY", ciscoDs3CapabilitySrmV3R00=ciscoDs3CapabilitySrmV3R00, ciscoDs3CapabilityV4R00=ciscoDs3CapabilityV4R00, ciscoDs3Capability=ciscoDs3Capability, ciscoDs3CapabilityV5R00=ciscoDs3CapabilityV5R00, PYSNMP_MODULE_ID=ciscoDs3Capability, ciscoDs3CapabilityPxm1eV3R00=ciscoDs3CapabilityPxm1eV3R00, ciscoDs3CapabilityV2R0100=ciscoDs3CapabilityV2R0100)
