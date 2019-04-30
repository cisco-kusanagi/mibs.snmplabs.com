#
# PySNMP MIB module Unisphere-Data-PPP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pppIpConfigEntry, pppIpEntry = mibBuilder.importSymbols("PPP-IP-NCP-MIB", "pppIpConfigEntry", "pppIpEntry")
pppLqrExtnsEntry, pppLqrConfigEntry, pppLinkStatusEntry, pppLqrEntry, pppLinkConfigEntry = mibBuilder.importSymbols("PPP-LCP-MIB", "pppLqrExtnsEntry", "pppLqrConfigEntry", "pppLinkStatusEntry", "pppLqrEntry", "pppLinkConfigEntry")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress, Bits, Counter32, Unsigned32, TimeTicks, NotificationType, Gauge32, ModuleIdentity, Counter64, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress", "Bits", "Counter32", "Unsigned32", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "Counter64", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPppLcpGroup3, usdPppLcpGroup4, usdPppSummaryGroup, usdPppIpGroup3, usdPppMlPppGroup, usdPppSummaryLinkGroup, usdPppSummaryBasicGroup, usdPppSummaryNetworkGroup, usdPppIpGroup2, usdPppOsiGroup2, usdPppSessionGroup, usdPppMlPppGroup2 = mibBuilder.importSymbols("Unisphere-Data-PPP-MIB", "usdPppLcpGroup3", "usdPppLcpGroup4", "usdPppSummaryGroup", "usdPppIpGroup3", "usdPppMlPppGroup", "usdPppSummaryLinkGroup", "usdPppSummaryBasicGroup", "usdPppSummaryNetworkGroup", "usdPppIpGroup2", "usdPppOsiGroup2", "usdPppSessionGroup", "usdPppMlPppGroup2")
usdPppAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32))
usdPppAgent.setRevisions(('2002-05-09 21:03', '2002-05-08 20:25', '2001-04-10 18:23',))
if mibBuilder.loadTexts: usdPppAgent.setLastUpdated('200205092103Z')
if mibBuilder.loadTexts: usdPppAgent.setOrganization('Unisphere Networks, Inc.')
usdPppAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppAgentV1 = usdPppAgentV1.setProductRelease('Version 1 of the PPP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPP component was supported in the Unisphere\n        RX 2.4 thru 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppAgentV1 = usdPppAgentV1.setStatus('obsolete')
usdPppGeneralAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2))
if mibBuilder.loadTexts: usdPppGeneralAgent.setStatus('current')
usdPppGeneralAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV1 = usdPppGeneralAgentV1.setProductRelease('Version 1 of the general PPP component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP component was supported in the\n        Unisphere RX 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV1 = usdPppGeneralAgentV1.setStatus('obsolete')
usdPppGeneralAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV2 = usdPppGeneralAgentV2.setProductRelease('Version 2 of the general PPP component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV2 = usdPppGeneralAgentV2.setStatus('current')
usdPppMultiLinkAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3))
if mibBuilder.loadTexts: usdPppMultiLinkAgent.setStatus('current')
usdPppMultiLinkAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV1 = usdPppMultiLinkAgentV1.setProductRelease('Version 1 of the multi-link PPP component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPP component was supported in\n        the Unisphere RX 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV1 = usdPppMultiLinkAgentV1.setStatus('obsolete')
usdPppMultiLinkAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV2 = usdPppMultiLinkAgentV2.setProductRelease('Version 2 of the multi-link PPP component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPP component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV2 = usdPppMultiLinkAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PPP-CONF", usdPppAgent=usdPppAgent, usdPppMultiLinkAgent=usdPppMultiLinkAgent, usdPppMultiLinkAgentV2=usdPppMultiLinkAgentV2, usdPppGeneralAgentV1=usdPppGeneralAgentV1, usdPppGeneralAgent=usdPppGeneralAgent, usdPppAgentV1=usdPppAgentV1, usdPppGeneralAgentV2=usdPppGeneralAgentV2, PYSNMP_MODULE_ID=usdPppAgent, usdPppMultiLinkAgentV1=usdPppMultiLinkAgentV1)
