#
# PySNMP MIB module CISCO-MEMORY-POOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEMORY-POOL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, MibIdentifier, Integer32, iso, Bits, Counter64, Unsigned32, Counter32, NotificationType, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Integer32", "iso", "Bits", "Counter64", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMemoryPoolCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 338))
ciscoMemoryPoolCapability.setRevisions(('2006-05-02 00:00', '2005-10-26 00:00', '2003-08-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setRevisionsDescriptions(('Corrected existing Agent Capability for IOS XR release 2.0 CRS1', 'Added ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 agent capabilities for IOS XR release 2.0 CRS1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setLastUpdated('200605020000Z')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setDescription('The capabilities description of CISCO-MEMORY-POOL-MIB.')
ciscoMemoryPoolCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoMemoryPoolCapCatOSV08R0101.setDescription('CISCO-MEMORY-POOL-MIB capabilities.')
ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setDescription('CISCO-MEMORY-POOL-MIB capabilities for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-MEMORY-POOL-CAPABILITY", ciscoMemoryPoolCapCatOSV08R0101=ciscoMemoryPoolCapCatOSV08R0101, ciscoMemoryPoolCapabilityIOSXRV2R0CRS1=ciscoMemoryPoolCapabilityIOSXRV2R0CRS1, ciscoMemoryPoolCapability=ciscoMemoryPoolCapability, PYSNMP_MODULE_ID=ciscoMemoryPoolCapability)
