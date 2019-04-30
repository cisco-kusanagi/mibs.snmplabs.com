#
# PySNMP MIB module Unisphere-Data-IP-Policy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-Policy-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter64, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, Unsigned32, NotificationType, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "Unsigned32", "NotificationType", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIpPrefixTreePolicy, usdIpCommunityListExpression, usdIpAccessListGroup, usdIpPrefixListGroup, usdIpPrefixListGeValue, usdIpCommunityListPolicy, usdIpRedistributeRowStatus, usdIpPrefixListLeValue, usdIpRedistributeState, usdIpRedistributeRouteMapName, usdIpPrefixTreeRowStatus, usdIpDynRedistributeState, usdIpExtCommunityListGroup, usdIpPrefixTreeGroup, usdIpPrefixListDescription, usdIpExtCommunityListPolicy, usdIpRouteMapGroup, usdIpPrefixListPolicy, usdIpDynRedistributeRowStatus, usdIpRedistributeGroup, usdIpAspAccessListGroup, usdIpExtCommunityListExpression, usdIpAspAccessRowStatus, usdIpCommunityListGroup, usdIpCommunityListExtended, usdIpAspAccessExpression, usdIpAspAccessPolicy, usdIpNamedAccessListGroup, usdIpExtCommunityListRowStatus, usdIpCommunityListRowStatus, usdIpPrefixListRowStatus, usdIpPrefixTreeDescription = mibBuilder.importSymbols("Unisphere-Data-IP-POLICY-MIB", "usdIpPrefixTreePolicy", "usdIpCommunityListExpression", "usdIpAccessListGroup", "usdIpPrefixListGroup", "usdIpPrefixListGeValue", "usdIpCommunityListPolicy", "usdIpRedistributeRowStatus", "usdIpPrefixListLeValue", "usdIpRedistributeState", "usdIpRedistributeRouteMapName", "usdIpPrefixTreeRowStatus", "usdIpDynRedistributeState", "usdIpExtCommunityListGroup", "usdIpPrefixTreeGroup", "usdIpPrefixListDescription", "usdIpExtCommunityListPolicy", "usdIpRouteMapGroup", "usdIpPrefixListPolicy", "usdIpDynRedistributeRowStatus", "usdIpRedistributeGroup", "usdIpAspAccessListGroup", "usdIpExtCommunityListExpression", "usdIpAspAccessRowStatus", "usdIpCommunityListGroup", "usdIpCommunityListExtended", "usdIpAspAccessExpression", "usdIpAspAccessPolicy", "usdIpNamedAccessListGroup", "usdIpExtCommunityListRowStatus", "usdIpCommunityListRowStatus", "usdIpPrefixListRowStatus", "usdIpPrefixTreeDescription")
usdIpPolicyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22))
usdIpPolicyAgent.setRevisions(('2001-05-01 20:13',))
if mibBuilder.loadTexts: usdIpPolicyAgent.setLastUpdated('200105012013Z')
if mibBuilder.loadTexts: usdIpPolicyAgent.setOrganization('Unisphere Networks, Inc.')
usdIpPolicyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV1 = usdIpPolicyAgentV1.setProductRelease('Version 1 of the IP Policy component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Policy component was supported in\n        the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV1 = usdIpPolicyAgentV1.setStatus('obsolete')
usdIpPolicyAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV2 = usdIpPolicyAgentV2.setProductRelease('Version 2 of the IP Policy component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Policy component was supported in\n        the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV2 = usdIpPolicyAgentV2.setStatus('obsolete')
usdIpPolicyAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV3 = usdIpPolicyAgentV3.setProductRelease('Version 3 of the IP Policy component of the Unisphere Routing Switch\n        SNMP agent.  This version of the IP Policy component is supported in the\n        Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpPolicyAgentV3 = usdIpPolicyAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IP-Policy-CONF", usdIpPolicyAgent=usdIpPolicyAgent, PYSNMP_MODULE_ID=usdIpPolicyAgent, usdIpPolicyAgentV3=usdIpPolicyAgentV3, usdIpPolicyAgentV2=usdIpPolicyAgentV2, usdIpPolicyAgentV1=usdIpPolicyAgentV1)
