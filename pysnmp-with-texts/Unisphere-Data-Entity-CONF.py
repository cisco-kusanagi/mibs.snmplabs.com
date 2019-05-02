#
# PySNMP MIB module Unisphere-Data-Entity-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Entity-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalSerialNum, entityLogical2Group, entityLogicalGroup, entityPhysical2Group, entityMappingGroup, entAliasMappingIdentifier, entLPPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalSerialNum", "entityLogical2Group", "entityLogicalGroup", "entityPhysical2Group", "entityMappingGroup", "entAliasMappingIdentifier", "entLPPhysicalIndex")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Unsigned32, TimeTicks, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Bits, ObjectIdentity, IpAddress, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Unsigned32", "TimeTicks", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Bits", "ObjectIdentity", "IpAddress", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdEntityAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13))
usdEntityAgent.setRevisions(('2001-04-27 13:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdEntityAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdEntityAgent.setLastUpdated('200104271316Z')
if mibBuilder.loadTexts: usdEntityAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdEntityAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdEntityAgent.setDescription('The agent capabilities definitions for the physical and logical entity components of the SNMP agent in the Unisphere Routing Switch family of products.')
usdEntityAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV1 = usdEntityAgentV1.setProductRelease('Version 1 of the logical Entity component of the Unisphere Routing\n        Switch SNMP agent.  This version of the logical Entity component was\n        supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV1 = usdEntityAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdEntityAgentV1.setDescription('The MIB supported by the SNMP agent for the Router Agent (logical entity) application in the Unisphere Routing Switch. These capabilities became obsolete when support was add for the physical entity table, the physical entity contains table, and RFC 2737 enhancements to the logical entity table.')
usdEntityAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV2 = usdEntityAgentV2.setProductRelease('Version 2 of the physical and logical Entity components of the\n        Unisphere Routing Switch SNMP agent.  This version of the physical and\n        logical Entity components is supported in the Unisphere RX 3.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV2 = usdEntityAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdEntityAgentV2.setDescription('The MIB supported by the SNMP agent for the System (physical entity) and Router Agent (logical entity) applications in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Entity-CONF", usdEntityAgent=usdEntityAgent, usdEntityAgentV2=usdEntityAgentV2, usdEntityAgentV1=usdEntityAgentV1, PYSNMP_MODULE_ID=usdEntityAgent)
