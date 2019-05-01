#
# PySNMP MIB module CISCO-WAN-VISM-SRCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-SRCP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, iso, Counter32, Integer32, MibIdentifier, ModuleIdentity, Bits, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "iso", "Counter32", "Integer32", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismSrcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 321))
ciscoWanVismSrcpCapability.setRevisions(('2000-07-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setRevisionsDescriptions(('added ciscoWanVismSrcpCapabilityV2R01 macro ',))
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setLastUpdated('200109080000Z')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setDescription('The Agent Capabilities for CISCO-WAN-SRCP-MIB.')
ciscoWanVismSrcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R00 = ciscoWanVismSrcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R00 = ciscoWanVismSrcpCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapabilityV2R00.setDescription('SRCP MIB Capabilities')
ciscoWanVismSrcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R01 = ciscoWanVismSrcpCapabilityV2R01.setProductRelease('VISM release 2.0.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R01 = ciscoWanVismSrcpCapabilityV2R01.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapabilityV2R01.setDescription('SRCP MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-SRCP-CAPABILITY", ciscoWanVismSrcpCapability=ciscoWanVismSrcpCapability, ciscoWanVismSrcpCapabilityV2R00=ciscoWanVismSrcpCapabilityV2R00, ciscoWanVismSrcpCapabilityV2R01=ciscoWanVismSrcpCapabilityV2R01, PYSNMP_MODULE_ID=ciscoWanVismSrcpCapability)
