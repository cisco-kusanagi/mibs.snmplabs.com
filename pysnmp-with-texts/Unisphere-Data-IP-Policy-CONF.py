#
# PySNMP MIB module Unisphere-Data-IP-Policy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-Policy-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Counter32, Unsigned32, ModuleIdentity, TimeTicks, Gauge32, Bits, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Gauge32", "Bits", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIpPrefixListRowStatus, usdIpRouteMapGroup, usdIpPrefixTreePolicy, usdIpCommunityListExtended, usdIpRedistributeGroup, usdIpAspAccessListGroup, usdIpCommunityListRowStatus, usdIpRedistributeRowStatus, usdIpNamedAccessListGroup, usdIpAccessListGroup, usdIpAspAccessRowStatus, usdIpPrefixTreeGroup, usdIpExtCommunityListGroup, usdIpRedistributeRouteMapName, usdIpCommunityListGroup, usdIpExtCommunityListExpression, usdIpExtCommunityListRowStatus, usdIpDynRedistributeRowStatus, usdIpAspAccessPolicy, usdIpPrefixListLeValue, usdIpPrefixListGeValue, usdIpPrefixTreeDescription, usdIpPrefixListPolicy, usdIpExtCommunityListPolicy, usdIpCommunityListExpression, usdIpRedistributeState, usdIpAspAccessExpression, usdIpDynRedistributeState, usdIpPrefixTreeRowStatus, usdIpPrefixListDescription, usdIpPrefixListGroup, usdIpCommunityListPolicy = mibBuilder.importSymbols("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixListRowStatus", "usdIpRouteMapGroup", "usdIpPrefixTreePolicy", "usdIpCommunityListExtended", "usdIpRedistributeGroup", "usdIpAspAccessListGroup", "usdIpCommunityListRowStatus", "usdIpRedistributeRowStatus", "usdIpNamedAccessListGroup", "usdIpAccessListGroup", "usdIpAspAccessRowStatus", "usdIpPrefixTreeGroup", "usdIpExtCommunityListGroup", "usdIpRedistributeRouteMapName", "usdIpCommunityListGroup", "usdIpExtCommunityListExpression", "usdIpExtCommunityListRowStatus", "usdIpDynRedistributeRowStatus", "usdIpAspAccessPolicy", "usdIpPrefixListLeValue", "usdIpPrefixListGeValue", "usdIpPrefixTreeDescription", "usdIpPrefixListPolicy", "usdIpExtCommunityListPolicy", "usdIpCommunityListExpression", "usdIpRedistributeState", "usdIpAspAccessExpression", "usdIpDynRedistributeState", "usdIpPrefixTreeRowStatus", "usdIpPrefixListDescription", "usdIpPrefixListGroup", "usdIpCommunityListPolicy")
usdIpPolicyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22))
usdIpPolicyAgent.setRevisions(('2001-05-01 20:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdIpPolicyAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdIpPolicyAgent.setLastUpdated('200105012013Z')
if mibBuilder.loadTexts: usdIpPolicyAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdIpPolicyAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdIpPolicyAgent.setDescription('The agent capabilities definitions for the IP Policy component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdIpPolicyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV1 = usdIpPolicyAgentV1.setProductRelease('Version 1 of the IP Policy component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Policy component was supported in\n        the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV1 = usdIpPolicyAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdIpPolicyAgentV1.setDescription('The MIB supported by the SNMP agent for the IP Policy application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for the IP Named Access List.')
usdIpPolicyAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV2 = usdIpPolicyAgentV2.setProductRelease('Version 2 of the IP Policy component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Policy component was supported in\n        the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV2 = usdIpPolicyAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdIpPolicyAgentV2.setDescription('The MIB supported by the SNMP agent for the IP Policy application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for the IP ASP Access List, the IP Prefix List, the IP Prefix Tree, the IP Community List, the IP Extended Community List, IP Dynamic Route Redistribution, and the IP Route Map.')
usdIpPolicyAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV3 = usdIpPolicyAgentV3.setProductRelease('Version 3 of the IP Policy component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Policy component is supported in the\n        Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV3 = usdIpPolicyAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdIpPolicyAgentV3.setDescription('The MIB supported by the SNMP agent for the IP Policy application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-IP-Policy-CONF", usdIpPolicyAgentV1=usdIpPolicyAgentV1, usdIpPolicyAgent=usdIpPolicyAgent, PYSNMP_MODULE_ID=usdIpPolicyAgent, usdIpPolicyAgentV2=usdIpPolicyAgentV2, usdIpPolicyAgentV3=usdIpPolicyAgentV3)
