#
# PySNMP MIB module Juniper-MPLS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-MPLS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Gauge32, ModuleIdentity, NotificationType, MibIdentifier, iso, Bits, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Gauge32", "ModuleIdentity", "NotificationType", "MibIdentifier", "iso", "Bits", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniMplsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51))
juniMplsAgent.setRevisions(('2004-06-11 21:36', '2003-01-24 18:34', '2002-11-04 15:47', '2001-12-05 21:41',))
if mibBuilder.loadTexts: juniMplsAgent.setLastUpdated('200406231509Z')
if mibBuilder.loadTexts: juniMplsAgent.setOrganization('Juniper Networks, Inc.')
juniMplsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV1 = juniMplsAgentV1.setProductRelease('Version 1 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component was supported in\n        JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV1 = juniMplsAgentV1.setStatus('obsolete')
juniMplsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV2 = juniMplsAgentV2.setProductRelease('Version 2 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component was supported in\n        JUNOSe 4.1 and subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV2 = juniMplsAgentV2.setStatus('obsolete')
juniMplsAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV3 = juniMplsAgentV3.setProductRelease('Version 3 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV3 = juniMplsAgentV3.setStatus('obsolete')
juniMplsAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV4 = juniMplsAgentV4.setProductRelease('Version 4 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 6.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV4 = juniMplsAgentV4.setStatus('obsolete')
juniMplsAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV5 = juniMplsAgentV5.setProductRelease('Version 5 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV5 = juniMplsAgentV5.setStatus('obsolete')
juniMplsAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV6 = juniMplsAgentV6.setProductRelease('Version 6 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 7.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV6 = juniMplsAgentV6.setStatus('current')
mibBuilder.exportSymbols("Juniper-MPLS-CONF", juniMplsAgentV1=juniMplsAgentV1, juniMplsAgentV5=juniMplsAgentV5, juniMplsAgentV2=juniMplsAgentV2, juniMplsAgent=juniMplsAgent, juniMplsAgentV4=juniMplsAgentV4, juniMplsAgentV3=juniMplsAgentV3, juniMplsAgentV6=juniMplsAgentV6, PYSNMP_MODULE_ID=juniMplsAgent)
