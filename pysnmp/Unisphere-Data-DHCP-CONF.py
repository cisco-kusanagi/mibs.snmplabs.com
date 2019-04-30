#
# PySNMP MIB module Unisphere-Data-DHCP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DHCP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Unsigned32, Gauge32, ModuleIdentity, Bits, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Unsigned32", "Gauge32", "ModuleIdentity", "Bits", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDhcpLocalServerGroup2, usdDhcpLocalServerGroup, usdDhcpRelayGroup, usdDhcpProxyGroup, usdDhcpRelayGroup2 = mibBuilder.importSymbols("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerGroup2", "usdDhcpLocalServerGroup", "usdDhcpRelayGroup", "usdDhcpProxyGroup", "usdDhcpRelayGroup2")
usdDhcpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8))
usdDhcpAgent.setRevisions(('2002-05-10 19:37', '2001-03-30 18:46',))
if mibBuilder.loadTexts: usdDhcpAgent.setLastUpdated('200205101937Z')
if mibBuilder.loadTexts: usdDhcpAgent.setOrganization('Unisphere Networks, Inc.')
usdDhcpRelayAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1))
if mibBuilder.loadTexts: usdDhcpRelayAgent.setStatus('current')
usdDhcpRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV1 = usdDhcpRelayAgentV1.setProductRelease('Version 1 of the DHCP relay subcomponent of the Unisphere Routing\n        Switch SNMP agent.  This version of the DHCP relay subcomponent is\n        supported in the Unisphere RX 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV1 = usdDhcpRelayAgentV1.setStatus('obsolete')
usdDhcpRelayAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV2 = usdDhcpRelayAgentV2.setProductRelease('Version 2 of the DHCP relay subcomponent of the Unisphere Routing\n        Switch SNMP agent.  This version of the DHCP relay subcomponent is\n        supported in the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpRelayAgentV2 = usdDhcpRelayAgentV2.setStatus('current')
usdDhcpProxyAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2))
if mibBuilder.loadTexts: usdDhcpProxyAgent.setStatus('current')
usdDhcpProxyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpProxyAgentV1 = usdDhcpProxyAgentV1.setProductRelease('Version 1 of the DHCP proxy subcomponent of the Unisphere Routing\n        Switch SNMP agent.  This version of the DHCP proxy subcomponent is\n        supported in the Unisphere RX 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpProxyAgentV1 = usdDhcpProxyAgentV1.setStatus('current')
usdDhcpLocalServerAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3))
if mibBuilder.loadTexts: usdDhcpLocalServerAgent.setStatus('current')
usdDhcpLocalServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV1 = usdDhcpLocalServerAgentV1.setProductRelease('Version 1 of the DHCP local server subcomponent of the Unisphere\n        Routing Switch SNMP agent.  This version of the DHCP local server\n        subcomponent was supported in the Unisphere RX 3.1 and subsequent 3.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV1 = usdDhcpLocalServerAgentV1.setStatus('obsolete')
usdDhcpLocalServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV2 = usdDhcpLocalServerAgentV2.setProductRelease('Version 2 of the DHCP local server subcomponent of the Unisphere\n        Routing Switch SNMP agent.  This version of the DHCP local server\n        subcomponent is supported in the Unisphere RX 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDhcpLocalServerAgentV2 = usdDhcpLocalServerAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-DHCP-CONF", usdDhcpLocalServerAgent=usdDhcpLocalServerAgent, usdDhcpProxyAgent=usdDhcpProxyAgent, usdDhcpLocalServerAgentV2=usdDhcpLocalServerAgentV2, usdDhcpRelayAgentV1=usdDhcpRelayAgentV1, usdDhcpAgent=usdDhcpAgent, usdDhcpRelayAgentV2=usdDhcpRelayAgentV2, usdDhcpProxyAgentV1=usdDhcpProxyAgentV1, PYSNMP_MODULE_ID=usdDhcpAgent, usdDhcpRelayAgent=usdDhcpRelayAgent, usdDhcpLocalServerAgentV1=usdDhcpLocalServerAgentV1)
