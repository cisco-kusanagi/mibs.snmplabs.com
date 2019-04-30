#
# PySNMP MIB module Unisphere-Data-Router-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Router-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, iso, Bits, IpAddress, MibIdentifier, Unsigned32, ObjectIdentity, ModuleIdentity, Gauge32, Counter32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "iso", "Bits", "IpAddress", "MibIdentifier", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Counter32", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdRouterGroup2, usdRouterGroup3, usdRouterGroup, usdRouterVrfGroup = mibBuilder.importSymbols("Unisphere-Data-ROUTER-MIB", "usdRouterGroup2", "usdRouterGroup3", "usdRouterGroup", "usdRouterVrfGroup")
usdRouterAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37))
usdRouterAgent.setRevisions(('2002-05-10 19:06', '2001-03-29 18:17',))
if mibBuilder.loadTexts: usdRouterAgent.setLastUpdated('200205101906Z')
if mibBuilder.loadTexts: usdRouterAgent.setOrganization('Unisphere Networks, Inc.')
usdRouterAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV1 = usdRouterAgentV1.setProductRelease('Version 1 of the Router component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Router component was supported in the\n        Unisphere RX 1.3 and 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV1 = usdRouterAgentV1.setStatus('obsolete')
usdRouterAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV2 = usdRouterAgentV2.setProductRelease('Version 2 of the Router component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Router component was supported in the\n        Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV2 = usdRouterAgentV2.setStatus('obsolete')
usdRouterAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV3 = usdRouterAgentV3.setProductRelease('Version 3 of the Router component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Router component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV3 = usdRouterAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Router-CONF", usdRouterAgent=usdRouterAgent, usdRouterAgentV1=usdRouterAgentV1, usdRouterAgentV2=usdRouterAgentV2, usdRouterAgentV3=usdRouterAgentV3, PYSNMP_MODULE_ID=usdRouterAgent)
