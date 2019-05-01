#
# PySNMP MIB module Juniper-MPLS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-MPLS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter32, NotificationType, Integer32, Bits, ObjectIdentity, Gauge32, Counter64, Unsigned32, MibIdentifier, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "Integer32", "Bits", "ObjectIdentity", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniMplsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51))
juniMplsAgent.setRevisions(('2004-06-11 21:36', '2003-01-24 18:34', '2002-11-04 15:47', '2001-12-05 21:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniMplsAgent.setRevisionsDescriptions(('Added agent capabilities definitions for MPLS-LSR-STD-MIB.', 'Replaced Unisphere names with Juniper names. Added IP TTL Propagate object to the MPLS scalar group.', 'Added RowStatus support to the minor layer and the tunnel profile groups.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniMplsAgent.setLastUpdated('200406231509Z')
if mibBuilder.loadTexts: juniMplsAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniMplsAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniMplsAgent.setDescription('The agent capabilities definitions for the MultiProtocol Label Switching (MPLS) component of the SNMP agent in the Juniper E-series family of products.')
juniMplsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV1 = juniMplsAgentV1.setProductRelease('Version 1 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component was supported in\n        JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV1 = juniMplsAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniMplsAgentV1.setDescription('The MIB supported by the SNMP agent for the MPLS application in JUNOSe. These capabilities became obsolete when new RowStatus objects were added to the tables in juniMplsMinorLayerConfGroup and juniMplsTunnelProfileConfGroup.')
juniMplsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV2 = juniMplsAgentV2.setProductRelease('Version 2 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component was supported in\n        JUNOSe 4.1 and subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV2 = juniMplsAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniMplsAgentV2.setDescription('The MIB supported by the SNMP agent for the MPLS application in JUNOSe. These capabilities became obsolete when the IP TTL Propagate object was added to the MPLS scalar group.')
juniMplsAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV3 = juniMplsAgentV3.setProductRelease('Version 3 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV3 = juniMplsAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniMplsAgentV3.setDescription('The MIB supported by the SNMP agent for the MPLS application in JUNOSe. These capabilities became obsolete when some of the objects in that MIB became obsolete.')
juniMplsAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV4 = juniMplsAgentV4.setProductRelease('Version 4 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 6.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV4 = juniMplsAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniMplsAgentV4.setDescription('The MIB supported by the SNMP agent for the MPLS application in JUNOSe. These capabilities became obsolete when the MPLS-LSR-STD-MIB support is added.')
juniMplsAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV5 = juniMplsAgentV5.setProductRelease('Version 5 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 6.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV5 = juniMplsAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniMplsAgentV5.setDescription('The MIB supported by the SNMP agent for the MPLS application in JUNOSe.')
juniMplsAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV6 = juniMplsAgentV6.setProductRelease('Version 6 of the MultiProtocol Label Switching (MPLS) component of the\n        JUNOSe SNMP agent.  This version of the MPLS component is supported in\n        JUNOSe 7.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMplsAgentV6 = juniMplsAgentV6.setStatus('current')
if mibBuilder.loadTexts: juniMplsAgentV6.setDescription('The MIB supported by the SNMP agent for the MPLS application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-MPLS-CONF", juniMplsAgentV1=juniMplsAgentV1, juniMplsAgentV6=juniMplsAgentV6, juniMplsAgentV3=juniMplsAgentV3, juniMplsAgentV2=juniMplsAgentV2, juniMplsAgentV5=juniMplsAgentV5, PYSNMP_MODULE_ID=juniMplsAgent, juniMplsAgentV4=juniMplsAgentV4, juniMplsAgent=juniMplsAgent)
