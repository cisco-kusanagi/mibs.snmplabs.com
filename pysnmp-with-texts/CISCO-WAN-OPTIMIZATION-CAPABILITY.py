#
# PySNMP MIB module CISCO-WAN-OPTIMIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-OPTIMIZATION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, TimeTicks, Unsigned32, IpAddress, MibIdentifier, Counter64, NotificationType, ModuleIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanOptimizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 611))
ciscoWanOptimizationCapability.setRevisions(('2015-11-09 00:00', '2015-10-05 00:00', '2012-06-23 00:00', '2012-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setRevisionsDescriptions(('Added CIFS and Video AO objects to the list of Not-supported objects in ciscoWanOptimizationCapabilityWAASV6R0 agent.', 'Added ciscoWanOptimizationCapabilityWAASV6R0 agent for CISCO-WAN-OPTIMIZATION-MIB', 'Added ciscoWanOptimizationCapabilityWAASV5R0 agent for CISCO-WAN-OPTIMIZATION-CAPABILITY MIB.', 'Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setLastUpdated('201511090000Z')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-waas@cisco.com')
if mibBuilder.loadTexts: ciscoWanOptimizationCapability.setDescription('Agent capabilities for CISCO-WAN-OPTIMIZATION MIB')
ciscoWanOptimizationCapabilityWAASV4R4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV4R4 = ciscoWanOptimizationCapabilityWAASV4R4.setProductRelease('OS=WAAS\n                     OSVERSION=V4R4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV4R4 = ciscoWanOptimizationCapabilityWAASV4R4.setStatus('current')
if mibBuilder.loadTexts: ciscoWanOptimizationCapabilityWAASV4R4.setDescription('Agent capabilities for CISCO-WAN-OPTIMIZATION-MIB of WAAS V4R4')
ciscoWanOptimizationCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV5R0 = ciscoWanOptimizationCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V5R0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV5R0 = ciscoWanOptimizationCapabilityWAASV5R0.setStatus('current')
if mibBuilder.loadTexts: ciscoWanOptimizationCapabilityWAASV5R0.setDescription('Agent capability for CISCO-WAN-OPTIMIZATION-MIB of WAAS V5R0')
ciscoWanOptimizationCapabilityWAASV6R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 611, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV6R0 = ciscoWanOptimizationCapabilityWAASV6R0.setProductRelease('OS=WAAS\n                     OSVERSION=V6R0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanOptimizationCapabilityWAASV6R0 = ciscoWanOptimizationCapabilityWAASV6R0.setStatus('current')
if mibBuilder.loadTexts: ciscoWanOptimizationCapabilityWAASV6R0.setDescription('Agent capability for CISCO-WAN-OPTIMIZATION-MIB of WAAS V6R0')
mibBuilder.exportSymbols("CISCO-WAN-OPTIMIZATION-CAPABILITY", ciscoWanOptimizationCapabilityWAASV5R0=ciscoWanOptimizationCapabilityWAASV5R0, ciscoWanOptimizationCapability=ciscoWanOptimizationCapability, PYSNMP_MODULE_ID=ciscoWanOptimizationCapability, ciscoWanOptimizationCapabilityWAASV4R4=ciscoWanOptimizationCapabilityWAASV4R4, ciscoWanOptimizationCapabilityWAASV6R0=ciscoWanOptimizationCapabilityWAASV6R0)
