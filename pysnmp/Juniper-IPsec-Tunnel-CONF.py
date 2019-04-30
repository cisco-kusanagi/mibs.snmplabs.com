#
# PySNMP MIB module Juniper-IPsec-Tunnel-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IPsec-Tunnel-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, NotificationType, ObjectIdentity, Unsigned32, TimeTicks, Integer32, IpAddress, Counter32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "NotificationType", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "IpAddress", "Counter32", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpsecTunnelAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65))
juniIpsecTunnelAgent.setRevisions(('2005-03-17 16:08',))
if mibBuilder.loadTexts: juniIpsecTunnelAgent.setLastUpdated('200503171608Z')
if mibBuilder.loadTexts: juniIpsecTunnelAgent.setOrganization('Juniper Networks, Inc.')
juniIpsecTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV1 = juniIpsecTunnelAgentV1.setProductRelease('Version 1 of the IP Security Tunnel component of the JUNOSe SNMP agent.\n        This version of the IP Security Tunnel component is supported in JUNOSe\n        5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV1 = juniIpsecTunnelAgentV1.setStatus('obsolete')
juniIpsecTunnelAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV2 = juniIpsecTunnelAgentV2.setProductRelease('Version 2 of the IP Security Tunnel component of the JUNOSe SNMP agent.\n        This version of the IP Security Tunnel component is supported in JUNOSe\n        7.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV2 = juniIpsecTunnelAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-IPsec-Tunnel-CONF", juniIpsecTunnelAgent=juniIpsecTunnelAgent, juniIpsecTunnelAgentV1=juniIpsecTunnelAgentV1, PYSNMP_MODULE_ID=juniIpsecTunnelAgent, juniIpsecTunnelAgentV2=juniIpsecTunnelAgentV2)
