#
# PySNMP MIB module CISCO-IMA-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMA-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
MilliSeconds, = mibBuilder.importSymbols("IMA-MIB", "MilliSeconds")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, Counter32, Integer32, Gauge32, MibIdentifier, Bits, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Integer32", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImaExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 524))
ciscoImaExtCapability.setRevisions(('2006-11-24 00:00', '2006-09-26 00:00', '2002-03-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImaExtCapability.setRevisionsDescriptions(('Added ciscoImaExtCapabilityV12R05 for Cisco 2800, 3700 and 3800 Series Routers.', 'Added ciscoImaExtAxsmeCapabilityV5R320 and ciscoImaExtCapabilityV5R320.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImaExtCapability.setLastUpdated('200611240000Z')
if mibBuilder.loadTexts: ciscoImaExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImaExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoImaExtCapability.setDescription('Agent Capabilities for CISCO-IMA-MIB.')
ciscoImaExtAxsmeCapabilityV3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV3R0 = ciscoImaExtAxsmeCapabilityV3R0.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV3R0 = ciscoImaExtAxsmeCapabilityV3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtAxsmeCapabilityV3R0.setDescription('Agent capabilities for CISCO-IMA-MIB for AXSME Service Module in MGX8850 Series.')
ciscoImaExtAxsmeCapabilityV5R320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV5R320 = ciscoImaExtAxsmeCapabilityV5R320.setProductRelease('MGX8850 Release 5.3.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV5R320 = ciscoImaExtAxsmeCapabilityV5R320.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtAxsmeCapabilityV5R320.setDescription('Agent capabilities for CISCO-IMA-MIB for AXSME Service Module in MGX8850 Series.')
ciscoImaExtCapabilityV5R320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV5R320 = ciscoImaExtCapabilityV5R320.setProductRelease('MGX8950  and MGX8850 Release 5.3.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV5R320 = ciscoImaExtCapabilityV5R320.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtCapabilityV5R320.setDescription('CISCO-IMA-MIB Capabilities for Service Module: MPSM155,MPSM16T1E1 and Processor Switch Module Enhanced (PXM1E) controller card.')
ciscoImaExtCapabilityV12R05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV12R05 = ciscoImaExtCapabilityV12R05.setProductRelease('IOS 12.5 for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV12R05 = ciscoImaExtCapabilityV12R05.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtCapabilityV12R05.setDescription('Agent capabilities for Cisco 3700 Series Access Routers and 2800, 3800 Series Integrated Services Routers.')
mibBuilder.exportSymbols("CISCO-IMA-EXT-CAPABILITY", ciscoImaExtAxsmeCapabilityV3R0=ciscoImaExtAxsmeCapabilityV3R0, ciscoImaExtCapabilityV12R05=ciscoImaExtCapabilityV12R05, ciscoImaExtCapabilityV5R320=ciscoImaExtCapabilityV5R320, ciscoImaExtCapability=ciscoImaExtCapability, PYSNMP_MODULE_ID=ciscoImaExtCapability, ciscoImaExtAxsmeCapabilityV5R320=ciscoImaExtAxsmeCapabilityV5R320)
