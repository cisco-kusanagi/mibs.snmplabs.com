#
# PySNMP MIB module Juniper-Router-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Router-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, Unsigned32, MibIdentifier, NotificationType, Gauge32, ModuleIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "Unsigned32", "MibIdentifier", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRouterAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37))
juniRouterAgent.setRevisions(('2004-05-06 20:30', '2004-01-26 15:53', '2003-04-24 14:16', '2002-05-10 19:06', '2001-03-29 18:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRouterAgent.setRevisionsDescriptions(('Added RLI-870 Virtual Router and Vrf count support.', 'Added support for global export map and export map filter.', 'Replaced Unisphere names with Juniper names. Added SNMPv3 context engine ID support.', 'Added router context name support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniRouterAgent.setLastUpdated('200405062030Z')
if mibBuilder.loadTexts: juniRouterAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRouterAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniRouterAgent.setDescription('The agent capabilities definitions for the Router component of the SNMP agent in the Juniper E-series family of products.')
juniRouterAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV1 = juniRouterAgentV1.setProductRelease('Version 1 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 1.3 and 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV1 = juniRouterAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniRouterAgentV1.setDescription('The MIB supported by the SNMP agent for the Router application in JUNOSe. These capabilities became obsolete when virtual router forwarder (VFR) support was added.')
juniRouterAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV2 = juniRouterAgentV2.setProductRelease('Version 2 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV2 = juniRouterAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniRouterAgentV2.setDescription('The MIB supported by the SNMP agent for the Router application in JUNOSe. These capabilities became obsolete when router context name support was added.')
juniRouterAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV3 = juniRouterAgentV3.setProductRelease('Version 3 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 4.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV3 = juniRouterAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniRouterAgentV3.setDescription('The MIB supported by the SNMP agent for the Router application in JUNOSe. These capabilities became obsolete when router context engine ID support was added.')
juniRouterAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV4 = juniRouterAgentV4.setProductRelease('Version 4 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 5.0 and 5.1\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV4 = juniRouterAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniRouterAgentV4.setDescription('The MIB supported by the SNMP agent for the Router application in JUNOSe. These capabilities became obsolete when global export map and export map filter support was added.')
juniRouterAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV5 = juniRouterAgentV5.setProductRelease('Version 5 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component is supported in JUNOSe 5.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV5 = juniRouterAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniRouterAgentV5.setDescription('The MIB supported by the SNMP agent for the Router application in JUNOSe.')
juniRouterAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV6 = juniRouterAgentV6.setProductRelease('Version 6 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component is supported in JUNOSe 6.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV6 = juniRouterAgentV6.setStatus('current')
if mibBuilder.loadTexts: juniRouterAgentV6.setDescription('The MIB supported by the SNMP agent for the Router application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Router-CONF", juniRouterAgentV6=juniRouterAgentV6, juniRouterAgentV2=juniRouterAgentV2, juniRouterAgentV4=juniRouterAgentV4, juniRouterAgentV1=juniRouterAgentV1, juniRouterAgentV3=juniRouterAgentV3, PYSNMP_MODULE_ID=juniRouterAgent, juniRouterAgent=juniRouterAgent, juniRouterAgentV5=juniRouterAgentV5)
