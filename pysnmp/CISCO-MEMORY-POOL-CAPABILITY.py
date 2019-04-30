#
# PySNMP MIB module CISCO-MEMORY-POOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEMORY-POOL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, NotificationType, Bits, ObjectIdentity, Integer32, Unsigned32, Counter64, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Bits", "ObjectIdentity", "Integer32", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMemoryPoolCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 338))
ciscoMemoryPoolCapability.setRevisions(('2006-05-02 00:00', '2005-10-26 00:00', '2003-08-07 00:00',))
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setLastUpdated('200605020000Z')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setOrganization('Cisco Systems, Inc.')
ciscoMemoryPoolCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setStatus('current')
ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEMORY-POOL-CAPABILITY", ciscoMemoryPoolCapCatOSV08R0101=ciscoMemoryPoolCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoMemoryPoolCapability, ciscoMemoryPoolCapability=ciscoMemoryPoolCapability, ciscoMemoryPoolCapabilityIOSXRV2R0CRS1=ciscoMemoryPoolCapabilityIOSXRV2R0CRS1)
