#
# PySNMP MIB module Juniper-Router-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Router-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
IpAddress, Bits, Unsigned32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ObjectIdentity, MibIdentifier, Integer32, iso, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Unsigned32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ObjectIdentity", "MibIdentifier", "Integer32", "iso", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRouterAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37))
juniRouterAgent.setRevisions(('2004-05-06 20:30', '2004-01-26 15:53', '2003-04-24 14:16', '2002-05-10 19:06', '2001-03-29 18:17',))
if mibBuilder.loadTexts: juniRouterAgent.setLastUpdated('200405062030Z')
if mibBuilder.loadTexts: juniRouterAgent.setOrganization('Juniper Networks, Inc.')
juniRouterAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV1 = juniRouterAgentV1.setProductRelease('Version 1 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 1.3 and 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV1 = juniRouterAgentV1.setStatus('obsolete')
juniRouterAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV2 = juniRouterAgentV2.setProductRelease('Version 2 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV2 = juniRouterAgentV2.setStatus('obsolete')
juniRouterAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV3 = juniRouterAgentV3.setProductRelease('Version 3 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 4.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV3 = juniRouterAgentV3.setStatus('obsolete')
juniRouterAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV4 = juniRouterAgentV4.setProductRelease('Version 4 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component was supported in JUNOSe 5.0 and 5.1\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV4 = juniRouterAgentV4.setStatus('obsolete')
juniRouterAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV5 = juniRouterAgentV5.setProductRelease('Version 5 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component is supported in JUNOSe 5.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV5 = juniRouterAgentV5.setStatus('obsolete')
juniRouterAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV6 = juniRouterAgentV6.setProductRelease('Version 6 of the Router component of the JUNOSe SNMP agent.  This\n        version of the Router component is supported in JUNOSe 6.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRouterAgentV6 = juniRouterAgentV6.setStatus('current')
mibBuilder.exportSymbols("Juniper-Router-CONF", juniRouterAgent=juniRouterAgent, juniRouterAgentV5=juniRouterAgentV5, juniRouterAgentV2=juniRouterAgentV2, PYSNMP_MODULE_ID=juniRouterAgent, juniRouterAgentV4=juniRouterAgentV4, juniRouterAgentV6=juniRouterAgentV6, juniRouterAgentV3=juniRouterAgentV3, juniRouterAgentV1=juniRouterAgentV1)
