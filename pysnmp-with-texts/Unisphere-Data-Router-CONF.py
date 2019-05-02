#
# PySNMP MIB module Unisphere-Data-Router-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Router-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdRouterVrfGroup, usdRouterGroup3, usdRouterGroup2, usdRouterGroup = mibBuilder.importSymbols("Unisphere-Data-ROUTER-MIB", "usdRouterVrfGroup", "usdRouterGroup3", "usdRouterGroup2", "usdRouterGroup")
usdRouterAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37))
usdRouterAgent.setRevisions(('2002-05-10 19:06', '2001-03-29 18:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdRouterAgent.setRevisionsDescriptions(('Added router context name support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdRouterAgent.setLastUpdated('200205101906Z')
if mibBuilder.loadTexts: usdRouterAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdRouterAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdRouterAgent.setDescription('The agent capabilities definitions for the Router component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdRouterAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV1 = usdRouterAgentV1.setProductRelease('Version 1 of the Router component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Router component was supported in the\n        Unisphere RX 1.3 and 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV1 = usdRouterAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdRouterAgentV1.setDescription('The MIB supported by the SNMP agent for the Router application in the Unisphere Routing Switch. These capabilities became obsolete when virtual router forwarder (VFR) support was added.')
usdRouterAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV2 = usdRouterAgentV2.setProductRelease('Version 2 of the Router component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Router component was supported in the\n        Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV2 = usdRouterAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdRouterAgentV2.setDescription('The MIB supported by the SNMP agent for the Router application in the Unisphere Routing Switch. These capabilities became obsolete when router context name support was added.')
usdRouterAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV3 = usdRouterAgentV3.setProductRelease('Version 3 of the Router component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Router component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterAgentV3 = usdRouterAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdRouterAgentV3.setDescription('The MIB supported by the SNMP agent for the Router application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Router-CONF", usdRouterAgent=usdRouterAgent, usdRouterAgentV2=usdRouterAgentV2, usdRouterAgentV3=usdRouterAgentV3, PYSNMP_MODULE_ID=usdRouterAgent, usdRouterAgentV1=usdRouterAgentV1)
