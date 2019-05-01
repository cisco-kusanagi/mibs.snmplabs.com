#
# PySNMP MIB module Juniper-IP-Tunnel-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-Tunnel-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, IpAddress, ObjectIdentity, Unsigned32, Bits, ModuleIdentity, Integer32, NotificationType, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "Bits", "ModuleIdentity", "Integer32", "NotificationType", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIpTunnelAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47))
juniIpTunnelAgent.setRevisions(('2002-09-06 16:54', '2001-10-18 21:00', '2001-03-29 22:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIpTunnelAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added sequence numbers object.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIpTunnelAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniIpTunnelAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIpTunnelAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIpTunnelAgent.setDescription('The agent capabilities definitions for the IP Tunnel (GRE/DVMRP) MIB component of the SNMP agent in the Juniper E-series family of products.')
juniIpTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV1 = juniIpTunnelAgentV1.setProductRelease('Version 1 of the IP Tunnel component of the JUNOSe SNMP agent.  This\n        version of the IP Tunnel component is supported in JUNOSe 3.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV1 = juniIpTunnelAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpTunnelAgentV1.setDescription('The MIB supported by the SNMP agent for the IP Tunnel application in JUNOSe. These capabilities became obsolete when juniIpTunnelSequenceNumbers was added.')
juniIpTunnelAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV2 = juniIpTunnelAgentV2.setProductRelease('Version 2 of the IP Tunnel component of the JUNOSe SNMP agent.  This\n        version of the IP Tunnel component is supported in JUNOSe 4.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV2 = juniIpTunnelAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniIpTunnelAgentV2.setDescription('The MIB supported by the SNMP agent for the IP Tunnel application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-IP-Tunnel-CONF", juniIpTunnelAgentV2=juniIpTunnelAgentV2, PYSNMP_MODULE_ID=juniIpTunnelAgent, juniIpTunnelAgentV1=juniIpTunnelAgentV1, juniIpTunnelAgent=juniIpTunnelAgent)
