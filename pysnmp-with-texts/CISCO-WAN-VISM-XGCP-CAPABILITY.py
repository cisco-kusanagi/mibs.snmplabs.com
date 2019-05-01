#
# PySNMP MIB module CISCO-WAN-VISM-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-XGCP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, iso, TimeTicks, Counter64, NotificationType, IpAddress, Integer32, MibIdentifier, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "TimeTicks", "Counter64", "NotificationType", "IpAddress", "Integer32", "MibIdentifier", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 322))
ciscoWanVismXgcpCapability.setRevisions(('2002-02-27 00:00', '2002-01-21 00:00', '2001-08-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setRevisionsDescriptions(('Fix bug CSCdw32263 where xgcpRestartDelay returns illegal value', 'Changed INCLUDES fields in order to pass SMIC compiler', 'Added ciscoWanVismXgcpCapabilityV2R01 AGENT-CAPABILITIES.',))
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setLastUpdated('200202270000Z')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setDescription('The Agent Capabilities for XGCP-MIB.')
ciscoWanVismXgcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV2R00.setDescription('XGCP MIB Capabilities')
ciscoWanVismXgcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV2R01.setDescription('XGCP MIB Capabilities')
ciscoWanVismXgcpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV3R00.setDescription('XGCP MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-XGCP-CAPABILITY", ciscoWanVismXgcpCapabilityV3R00=ciscoWanVismXgcpCapabilityV3R00, ciscoWanVismXgcpCapability=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapabilityV2R01=ciscoWanVismXgcpCapabilityV2R01, PYSNMP_MODULE_ID=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapabilityV2R00=ciscoWanVismXgcpCapabilityV2R00)
