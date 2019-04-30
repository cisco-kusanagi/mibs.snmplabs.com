#
# PySNMP MIB module Juniper-IP-Tunnel-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-Tunnel-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter64, ObjectIdentity, Gauge32, MibIdentifier, NotificationType, Bits, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpTunnelAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47))
juniIpTunnelAgent.setRevisions(('2002-09-06 16:54', '2001-10-18 21:00', '2001-03-29 22:13',))
if mibBuilder.loadTexts: juniIpTunnelAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniIpTunnelAgent.setOrganization('Juniper Networks, Inc.')
juniIpTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV1 = juniIpTunnelAgentV1.setProductRelease('Version 1 of the IP Tunnel component of the JUNOSe SNMP agent.  This\n        version of the IP Tunnel component is supported in JUNOSe 3.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV1 = juniIpTunnelAgentV1.setStatus('obsolete')
juniIpTunnelAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV2 = juniIpTunnelAgentV2.setProductRelease('Version 2 of the IP Tunnel component of the JUNOSe SNMP agent.  This\n        version of the IP Tunnel component is supported in JUNOSe 4.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpTunnelAgentV2 = juniIpTunnelAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-IP-Tunnel-CONF", PYSNMP_MODULE_ID=juniIpTunnelAgent, juniIpTunnelAgentV2=juniIpTunnelAgentV2, juniIpTunnelAgent=juniIpTunnelAgent, juniIpTunnelAgentV1=juniIpTunnelAgentV1)
