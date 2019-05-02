#
# PySNMP MIB module Unisphere-Data-PPP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
pppIpConfigEntry, pppIpEntry = mibBuilder.importSymbols("PPP-IP-NCP-MIB", "pppIpConfigEntry", "pppIpEntry")
pppLqrExtnsEntry, pppLinkStatusEntry, pppLinkConfigEntry, pppLqrEntry, pppLqrConfigEntry = mibBuilder.importSymbols("PPP-LCP-MIB", "pppLqrExtnsEntry", "pppLinkStatusEntry", "pppLinkConfigEntry", "pppLqrEntry", "pppLqrConfigEntry")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, iso, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "iso", "Counter32", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPppMlPppGroup, usdPppMlPppGroup2, usdPppSummaryBasicGroup, usdPppLcpGroup3, usdPppSessionGroup, usdPppSummaryGroup, usdPppOsiGroup2, usdPppIpGroup2, usdPppSummaryLinkGroup, usdPppSummaryNetworkGroup, usdPppLcpGroup4, usdPppIpGroup3 = mibBuilder.importSymbols("Unisphere-Data-PPP-MIB", "usdPppMlPppGroup", "usdPppMlPppGroup2", "usdPppSummaryBasicGroup", "usdPppLcpGroup3", "usdPppSessionGroup", "usdPppSummaryGroup", "usdPppOsiGroup2", "usdPppIpGroup2", "usdPppSummaryLinkGroup", "usdPppSummaryNetworkGroup", "usdPppLcpGroup4", "usdPppIpGroup3")
usdPppAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32))
usdPppAgent.setRevisions(('2002-05-09 21:03', '2002-05-08 20:25', '2001-04-10 18:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPppAgent.setRevisionsDescriptions(('Added new objects to the LCP, IP and multi-link groups in the Unisphere-Data-PPP-MIB.', 'Created separate capabilities for multi-link PPP.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPppAgent.setLastUpdated('200205092103Z')
if mibBuilder.loadTexts: usdPppAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdPppAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPppAgent.setDescription('The agent capabilities definitions for the point-to-point protocol (PPP) component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdPppAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppAgentV1 = usdPppAgentV1.setProductRelease('Version 1 of the PPP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPP component was supported in the Unisphere\n        RX 2.4 thru 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppAgentV1 = usdPppAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppAgentV1.setDescription('The MIBs supported by the SNMP agent for the PPP application in the Unisphere Routing Switch. These capabilities became obsolete when the multilink capabilities were separated out.')
usdPppGeneralAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2))
if mibBuilder.loadTexts: usdPppGeneralAgent.setStatus('current')
if mibBuilder.loadTexts: usdPppGeneralAgent.setDescription('The registration group of agent capabilities for the general functionality of the PPP application which provides management support for basic (non-multi-link) PPP interfaces via SNMP.')
usdPppGeneralAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV1 = usdPppGeneralAgentV1.setProductRelease('Version 1 of the general PPP component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP component was supported in the\n        Unisphere RX 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV1 = usdPppGeneralAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppGeneralAgentV1.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in the Unisphere Routing Switch. These capabilities became obsolete when new LCP and IP objects were added to the Unisphere-Data-PPP-MIB.')
usdPppGeneralAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV2 = usdPppGeneralAgentV2.setProductRelease('Version 2 of the general PPP component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppGeneralAgentV2 = usdPppGeneralAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdPppGeneralAgentV2.setDescription('The MIBs supported by the SNMP agent for the basic PPP application in the Unisphere Routing Switch.')
usdPppMultiLinkAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3))
if mibBuilder.loadTexts: usdPppMultiLinkAgent.setStatus('current')
if mibBuilder.loadTexts: usdPppMultiLinkAgent.setDescription('The registration group of agent capabilities for the multi-link functionality of the PPP application which provides management support for multi-link PPP interfaces via SNMP.')
usdPppMultiLinkAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV1 = usdPppMultiLinkAgentV1.setProductRelease('Version 1 of the multi-link PPP component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPP component was supported in\n        the Unisphere RX 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV1 = usdPppMultiLinkAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppMultiLinkAgentV1.setDescription('The MIB groups supported by the SNMP agent for the PPP application in the Unisphere Routing Switch.. These capabilities became obsolete when new multi-link objects were added to the Unisphere-Data-PPP-MIB')
usdPppMultiLinkAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV2 = usdPppMultiLinkAgentV2.setProductRelease('Version 2 of the multi-link PPP component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPP component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppMultiLinkAgentV2 = usdPppMultiLinkAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdPppMultiLinkAgentV2.setDescription('The MIB groups supported by the SNMP agent for the PPP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-PPP-CONF", usdPppAgentV1=usdPppAgentV1, usdPppAgent=usdPppAgent, PYSNMP_MODULE_ID=usdPppAgent, usdPppGeneralAgentV1=usdPppGeneralAgentV1, usdPppMultiLinkAgentV2=usdPppMultiLinkAgentV2, usdPppGeneralAgent=usdPppGeneralAgent, usdPppMultiLinkAgentV1=usdPppMultiLinkAgentV1, usdPppMultiLinkAgent=usdPppMultiLinkAgent, usdPppGeneralAgentV2=usdPppGeneralAgentV2)
