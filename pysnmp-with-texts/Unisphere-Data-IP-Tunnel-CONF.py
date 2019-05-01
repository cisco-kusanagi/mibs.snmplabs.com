#
# PySNMP MIB module Unisphere-Data-IP-Tunnel-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-Tunnel-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, Gauge32, NotificationType, Bits, IpAddress, iso, Unsigned32, TimeTicks, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "NotificationType", "Bits", "IpAddress", "iso", "Unsigned32", "TimeTicks", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIpTunnelInterfaceGroup, = mibBuilder.importSymbols("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelInterfaceGroup")
usdIpTunnelAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47))
usdIpTunnelAgent.setRevisions(('2001-03-29 22:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdIpTunnelAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdIpTunnelAgent.setLastUpdated('200103292213Z')
if mibBuilder.loadTexts: usdIpTunnelAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdIpTunnelAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdIpTunnelAgent.setDescription('The agent capabilities definitions for the IP Tunnel (GRE/DVMRP) MIB component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdIpTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpTunnelAgentV1 = usdIpTunnelAgentV1.setProductRelease('Version 1 of the Ip Tunnel component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ip Tunnel component is supported in the\n        Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpTunnelAgentV1 = usdIpTunnelAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdIpTunnelAgentV1.setDescription('The MIB supported by the SNMP agent for the Ip Tunnel application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-IP-Tunnel-CONF", PYSNMP_MODULE_ID=usdIpTunnelAgent, usdIpTunnelAgentV1=usdIpTunnelAgentV1, usdIpTunnelAgent=usdIpTunnelAgent)
