#
# PySNMP MIB module CISCO-WAN-OPTIMIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-OPTIMIZATION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, Integer32, IpAddress, TimeTicks, Bits, ModuleIdentity, Counter64, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "IpAddress", "TimeTicks", "Bits", "ModuleIdentity", "Counter64", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanOptimizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 611))
ciscoWanOptimizationCapability.setRevisions(('2015-11-09 00:00', '2015-10-05 00:00', '2012-06-23 00:00', '2012-06-22 00:00',))
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setLastUpdated('201511090000Z')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanOptimizationCapabilityWAASV4R4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV4R4 = ciscoWanOptimizationCapabilityWAASV4R4.setProductRelease('OS=WAAS\n                     OSVERSION=V4R4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV4R4 = ciscoWanOptimizationCapabilityWAASV4R4.setStatus('current')
ciscoWanOptimizationCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV5R0 = ciscoWanOptimizationCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V5R0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV5R0 = ciscoWanOptimizationCapabilityWAASV5R0.setStatus('current')
ciscoWanOptimizationCapabilityWAASV6R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV6R0 = ciscoWanOptimizationCapabilityWAASV6R0.setProductRelease('OS=WAAS\n                     OSVERSION=V6R0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV6R0 = ciscoWanOptimizationCapabilityWAASV6R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-OPTIMIZATION-CAPABILITY", ciscoWanOptimizationCapabilityWAASV6R0=ciscoWanOptimizationCapabilityWAASV6R0, ciscoWanOptimizationCapabilityWAASV5R0=ciscoWanOptimizationCapabilityWAASV5R0, ciscoWanOptimizationCapabilityWAASV4R4=ciscoWanOptimizationCapabilityWAASV4R4, PYSNMP_MODULE_ID=ciscoWanOptimizationCapability, ciscoWanOptimizationCapability=ciscoWanOptimizationCapability)
