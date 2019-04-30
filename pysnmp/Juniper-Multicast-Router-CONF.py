#
# PySNMP MIB module Juniper-Multicast-Router-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Multicast-Router-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Unsigned32, NotificationType, IpAddress, ModuleIdentity, iso, Integer32, TimeTicks, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "IpAddress", "ModuleIdentity", "iso", "Integer32", "TimeTicks", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniMRouterAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55))
juniMRouterAgent.setRevisions(('2006-09-18 08:09', '2006-09-02 11:02', '2006-06-15 10:13', '2002-10-28 20:04', '2002-04-01 20:17',))
if mibBuilder.loadTexts: juniMRouterAgent.setLastUpdated('200609180809Z')
if mibBuilder.loadTexts: juniMRouterAgent.setOrganization('Juniper Networks, Inc.')
juniMRouterAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV1 = juniMRouterAgentV1.setProductRelease('Version 1 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component was supported in JUNOSe\n        4.1 and subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV1 = juniMRouterAgentV1.setStatus('obsolete')
juniMRouterAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV2 = juniMRouterAgentV2.setProductRelease('Version 2 of the multicast router component of the JUNOSe SNMP agent.\n        These capabilities became obsolete when support was added to Juniper-MROUTER-MIB\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 5.0 and subsequent system releases upto 8.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV2 = juniMRouterAgentV2.setStatus('obsolete')
juniMRouterAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV3 = juniMRouterAgentV3.setProductRelease('Version 3 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 8.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV3 = juniMRouterAgentV3.setStatus('obsolete')
uniMRouterAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV4 = uniMRouterAgentV4.setProductRelease('Version 4 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 8.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV4 = uniMRouterAgentV4.setStatus('obsolete')
uniMRouterAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV5 = uniMRouterAgentV5.setProductRelease('Version 5 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 8.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV5 = uniMRouterAgentV5.setStatus('current')
mibBuilder.exportSymbols("Juniper-Multicast-Router-CONF", uniMRouterAgentV5=uniMRouterAgentV5, juniMRouterAgentV1=juniMRouterAgentV1, juniMRouterAgentV3=juniMRouterAgentV3, PYSNMP_MODULE_ID=juniMRouterAgent, uniMRouterAgentV4=uniMRouterAgentV4, juniMRouterAgentV2=juniMRouterAgentV2, juniMRouterAgent=juniMRouterAgent)
