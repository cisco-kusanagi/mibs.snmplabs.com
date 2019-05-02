#
# PySNMP MIB module CISCO-WAN-VISM-MG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-MG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, Counter32, iso, ModuleIdentity, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Bits, TimeTicks, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Bits", "TimeTicks", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismMgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 320))
ciscoWanVismMgCapability.setRevisions(('2000-07-17 00:00', '2000-03-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismMgCapability.setRevisionsDescriptions(('Added AGENT-CAPABILITIES macro for ', 'Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setLastUpdated('200003170000Z')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setDescription('The Agent Capabilities for CISCO-WAN-MG-MIB.')
ciscoWanVismMgCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgCapabilityV2R00.setDescription('CISCO-WAN-MG-MIB Capabilities')
ciscoWanVismMgCapabilityV2R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setProductRelease('VISM Release2.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgCapabilityV2R02.setDescription('CISCO-WAN-MG-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MG-CAPABILITY", ciscoWanVismMgCapabilityV2R00=ciscoWanVismMgCapabilityV2R00, PYSNMP_MODULE_ID=ciscoWanVismMgCapability, ciscoWanVismMgCapabilityV2R02=ciscoWanVismMgCapabilityV2R02, ciscoWanVismMgCapability=ciscoWanVismMgCapability)
