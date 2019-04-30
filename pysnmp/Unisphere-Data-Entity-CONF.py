#
# PySNMP MIB module Unisphere-Data-Entity-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Entity-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entityLogicalGroup, entityLogical2Group, entityMappingGroup, entityPhysical2Group, entPhysicalSerialNum, entLPPhysicalIndex, entAliasMappingIdentifier = mibBuilder.importSymbols("ENTITY-MIB", "entityLogicalGroup", "entityLogical2Group", "entityMappingGroup", "entityPhysical2Group", "entPhysicalSerialNum", "entLPPhysicalIndex", "entAliasMappingIdentifier")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, IpAddress, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso, MibIdentifier, Gauge32, Counter64, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "IpAddress", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdEntityAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13))
usdEntityAgent.setRevisions(('2001-04-27 13:16',))
if mibBuilder.loadTexts: usdEntityAgent.setLastUpdated('200104271316Z')
if mibBuilder.loadTexts: usdEntityAgent.setOrganization('Unisphere Networks, Inc.')
usdEntityAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV1 = usdEntityAgentV1.setProductRelease('Version 1 of the logical Entity component of the Unisphere Routing\n        Switch SNMP agent.  This version of the logical Entity component was\n        supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV1 = usdEntityAgentV1.setStatus('obsolete')
usdEntityAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV2 = usdEntityAgentV2.setProductRelease('Version 2 of the physical and logical Entity components of the\n        Unisphere Routing Switch SNMP agent.  This version of the physical and\n        logical Entity components is supported in the Unisphere RX 3.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEntityAgentV2 = usdEntityAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Entity-CONF", usdEntityAgentV2=usdEntityAgentV2, usdEntityAgent=usdEntityAgent, PYSNMP_MODULE_ID=usdEntityAgent, usdEntityAgentV1=usdEntityAgentV1)
