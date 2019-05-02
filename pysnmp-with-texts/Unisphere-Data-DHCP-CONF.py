#
# PySNMP MIB module Unisphere-Data-DHCP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DHCP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, Unsigned32, Gauge32, TimeTicks, Counter32, IpAddress, MibIdentifier, Integer32, NotificationType, Bits, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Gauge32", "TimeTicks", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "Bits", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDhcpProxyGroup, usdDhcpRelayGroup2, usdDhcpRelayGroup, usdDhcpLocalServerGroup2, usdDhcpLocalServerGroup = mibBuilder.importSymbols("Unisphere-Data-DHCP-MIB", "usdDhcpProxyGroup", "usdDhcpRelayGroup2", "usdDhcpRelayGroup", "usdDhcpLocalServerGroup2", "usdDhcpLocalServerGroup")
usdDhcpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8))
usdDhcpAgent.setRevisions(('2002-05-10 19:37', '2001-03-30 18:46',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdDhcpAgent.setRevisionsDescriptions(('Added local server reservation and cable modem support. Refined agent info enable into agent circuit ID enable and agent remote ID enable.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdDhcpAgent.setLastUpdated('200205101937Z')
if mibBuilder.loadTexts: usdDhcpAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdDhcpAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdDhcpAgent.setDescription('The agent capabilities definitions for the DHCP component of the SNMP agent in the Unisphere Data Routing Switch family of products. The DHCP application has subcomponents that run independently of each other and therefore have separate agent capabilities definitions.')
usdDhcpRelayAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1))
if mibBuilder.loadTexts: usdDhcpRelayAgent.setStatus('current')
if mibBuilder.loadTexts: usdDhcpRelayAgent.setDescription('The DHCP relay subcomponent of the DHCP application. MIB support for each subcomponent can run independently of the other subcomponents.')
usdDhcpRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV1 = usdDhcpRelayAgentV1.setProductRelease('Version 1 of the DHCP relay subcomponent of the Unisphere Routing\n        Switch SNMP agent.  This version of the DHCP relay subcomponent is\n        supported in the Unisphere RX 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV1 = usdDhcpRelayAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdDhcpRelayAgentV1.setDescription('The MIB supported by the SNMP agent for the DHCP application in the Unisphere Routing Switch. These capabilities became obsolete when the agent info enable was refined.')
usdDhcpRelayAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV2 = usdDhcpRelayAgentV2.setProductRelease('Version 2 of the DHCP relay subcomponent of the Unisphere Routing\n        Switch SNMP agent.  This version of the DHCP relay subcomponent is\n        supported in the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV2 = usdDhcpRelayAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdDhcpRelayAgentV2.setDescription('The MIB supported by the SNMP agent for the DHCP application in the Unisphere Routing Switch.')
usdDhcpProxyAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2))
if mibBuilder.loadTexts: usdDhcpProxyAgent.setStatus('current')
if mibBuilder.loadTexts: usdDhcpProxyAgent.setDescription('The DHCP proxy subcomponent of the DHCP application. MIB support for each subcomponent can run independently of the other subcomponents.')
usdDhcpProxyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpProxyAgentV1 = usdDhcpProxyAgentV1.setProductRelease('Version 1 of the DHCP proxy subcomponent of the Unisphere Routing\n        Switch SNMP agent.  This version of the DHCP proxy subcomponent is\n        supported in the Unisphere RX 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpProxyAgentV1 = usdDhcpProxyAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdDhcpProxyAgentV1.setDescription('The MIB supported by the SNMP agent for the DHCP application in the Unisphere Routing Switch.')
usdDhcpLocalServerAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3))
if mibBuilder.loadTexts: usdDhcpLocalServerAgent.setStatus('current')
if mibBuilder.loadTexts: usdDhcpLocalServerAgent.setDescription('The DHCP local server subcomponent of the DHCP application. MIB support for each subcomponent can run independently of the other subcomponents.')
usdDhcpLocalServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV1 = usdDhcpLocalServerAgentV1.setProductRelease('Version 1 of the DHCP local server subcomponent of the Unisphere\n        Routing Switch SNMP agent.  This version of the DHCP local server\n        subcomponent was supported in the Unisphere RX 3.1 and subsequent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV1 = usdDhcpLocalServerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdDhcpLocalServerAgentV1.setDescription('The MIB supported by the SNMP agent for the DHCP application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for reservations and cable modems.')
usdDhcpLocalServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV2 = usdDhcpLocalServerAgentV2.setProductRelease('Version 2 of the DHCP local server subcomponent of the Unisphere\n        Routing Switch SNMP agent.  This version of the DHCP local server\n        subcomponent is supported in the Unisphere RX 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV2 = usdDhcpLocalServerAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdDhcpLocalServerAgentV2.setDescription('The MIB supported by the SNMP agent for the DHCP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-DHCP-CONF", usdDhcpRelayAgent=usdDhcpRelayAgent, PYSNMP_MODULE_ID=usdDhcpAgent, usdDhcpRelayAgentV1=usdDhcpRelayAgentV1, usdDhcpProxyAgentV1=usdDhcpProxyAgentV1, usdDhcpProxyAgent=usdDhcpProxyAgent, usdDhcpAgent=usdDhcpAgent, usdDhcpRelayAgentV2=usdDhcpRelayAgentV2, usdDhcpLocalServerAgentV2=usdDhcpLocalServerAgentV2, usdDhcpLocalServerAgentV1=usdDhcpLocalServerAgentV1, usdDhcpLocalServerAgent=usdDhcpLocalServerAgent)
