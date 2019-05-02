#
# PySNMP MIB module Juniper-IP-Policy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IP-Policy-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter64, iso, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter64", "iso", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpPolicyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22))
juniIpPolicyAgent.setRevisions(('2003-02-05 14:58', '2002-09-06 16:54', '2001-05-01 20:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIpPolicyAgent.setRevisionsDescriptions(('Added support for IP route maps configuration.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIpPolicyAgent.setLastUpdated('200302051458Z')
if mibBuilder.loadTexts: juniIpPolicyAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIpPolicyAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIpPolicyAgent.setDescription('The agent capabilities definitions for the IP Policy component of the SNMP agent in the Juniper E-series family of products.')
juniIpPolicyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV1 = juniIpPolicyAgentV1.setProductRelease('Version 1 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component was supported in JUNOSe 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV1 = juniIpPolicyAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpPolicyAgentV1.setDescription('The MIB supported by the SNMP agent for the IP Policy application in JUNOSe. These capabilities became obsolete when support was added for the IP Named Access List.')
juniIpPolicyAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV2 = juniIpPolicyAgentV2.setProductRelease('Version 2 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV2 = juniIpPolicyAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpPolicyAgentV2.setDescription('The MIB supported by the SNMP agent for the IP Policy application in JUNOSe. These capabilities became obsolete when support was added for the IP ASP Access List, the IP Prefix List, the IP Prefix Tree, the IP Community List, the IP Extended Community List, IP Dynamic Route Redistribution, and the IP Route Map.')
juniIpPolicyAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV3 = juniIpPolicyAgentV3.setProductRelease('Version 3 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component was supported in JUNOSe 3.0 thru 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV3 = juniIpPolicyAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpPolicyAgentV3.setDescription('The MIB supported by the SNMP agent for the IP Policy application in JUNOSe. These capabilities became obsolete when support was added for the IP route maps configuration.')
juniIpPolicyAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV4 = juniIpPolicyAgentV4.setProductRelease('Version 4 of the IP Policy component of the JUNOSe SNMP agent.  This\n        version of the IP Policy component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpPolicyAgentV4 = juniIpPolicyAgentV4.setStatus('current')
if mibBuilder.loadTexts: juniIpPolicyAgentV4.setDescription('The MIB supported by the SNMP agent for the IP Policy application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-IP-Policy-CONF", PYSNMP_MODULE_ID=juniIpPolicyAgent, juniIpPolicyAgentV3=juniIpPolicyAgentV3, juniIpPolicyAgentV4=juniIpPolicyAgentV4, juniIpPolicyAgentV1=juniIpPolicyAgentV1, juniIpPolicyAgentV2=juniIpPolicyAgentV2, juniIpPolicyAgent=juniIpPolicyAgent)
