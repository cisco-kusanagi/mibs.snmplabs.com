#
# PySNMP MIB module Unisphere-Data-IP-Tunnel-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-Tunnel-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, MibIdentifier, TimeTicks, Integer32, ObjectIdentity, Unsigned32, Counter64, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "TimeTicks", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIpTunnelInterfaceGroup, = mibBuilder.importSymbols("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelInterfaceGroup")
usdIpTunnelAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47))
usdIpTunnelAgent.setRevisions(('2001-03-29 22:13',))
if mibBuilder.loadTexts: usdIpTunnelAgent.setLastUpdated('200103292213Z')
if mibBuilder.loadTexts: usdIpTunnelAgent.setOrganization('Unisphere Networks, Inc.')
usdIpTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 47, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpTunnelAgentV1 = usdIpTunnelAgentV1.setProductRelease('Version 1 of the Ip Tunnel component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ip Tunnel component is supported in the\n        Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpTunnelAgentV1 = usdIpTunnelAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IP-Tunnel-CONF", usdIpTunnelAgent=usdIpTunnelAgent, usdIpTunnelAgentV1=usdIpTunnelAgentV1, PYSNMP_MODULE_ID=usdIpTunnelAgent)
