#
# PySNMP MIB module Juniper-IPsec-Tunnel-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IPsec-Tunnel-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, Counter32, Bits, MibIdentifier, Integer32, IpAddress, ObjectIdentity, NotificationType, Gauge32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter32", "Bits", "MibIdentifier", "Integer32", "IpAddress", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpsecTunnelAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65))
juniIpsecTunnelAgent.setRevisions(('2005-03-17 16:08',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIpsecTunnelAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIpsecTunnelAgent.setLastUpdated('200503171608Z')
if mibBuilder.loadTexts: juniIpsecTunnelAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIpsecTunnelAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIpsecTunnelAgent.setDescription('The agent capabilities definitions for the IP Security Tunnel component of the SNMP agent in the Juniper E-series family of products.')
juniIpsecTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV1 = juniIpsecTunnelAgentV1.setProductRelease('Version 1 of the IP Security Tunnel component of the JUNOSe SNMP agent.\n        This version of the IP Security Tunnel component is supported in JUNOSe\n        5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV1 = juniIpsecTunnelAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpsecTunnelAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the IP Security Tunnel application.')
juniIpsecTunnelAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 65, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV2 = juniIpsecTunnelAgentV2.setProductRelease('Version 2 of the IP Security Tunnel component of the JUNOSe SNMP agent.\n        This version of the IP Security Tunnel component is supported in JUNOSe\n        7.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpsecTunnelAgentV2 = juniIpsecTunnelAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniIpsecTunnelAgentV2.setDescription('The MIB supported by the JUNOSe SNMP agent for the IP Security Tunnel application.')
mibBuilder.exportSymbols("Juniper-IPsec-Tunnel-CONF", PYSNMP_MODULE_ID=juniIpsecTunnelAgent, juniIpsecTunnelAgentV2=juniIpsecTunnelAgentV2, juniIpsecTunnelAgentV1=juniIpsecTunnelAgentV1, juniIpsecTunnelAgent=juniIpsecTunnelAgent)
