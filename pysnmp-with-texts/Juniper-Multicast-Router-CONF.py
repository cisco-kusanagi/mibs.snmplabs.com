#
# PySNMP MIB module Juniper-Multicast-Router-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Multicast-Router-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Gauge32, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, IpAddress, Integer32, ObjectIdentity, Bits, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniMRouterAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55))
juniMRouterAgent.setRevisions(('2006-09-18 08:09', '2006-09-02 11:02', '2006-06-15 10:13', '2002-10-28 20:04', '2002-04-01 20:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniMRouterAgent.setRevisionsDescriptions(('Extended the ipMRouteInterfaceEntry Table, introduced traps and platform dependent rsMRoutePortTable.', 'Scalar attribute rsMcastRpfDisable is supported for the Juniper-MROUTER-MIB.', 'Extended the ipMRouteEntry Table', 'Replaced Unisphere names with Juniper names. Added support for the Juniper-MROUTER-MIB.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniMRouterAgent.setLastUpdated('200609180809Z')
if mibBuilder.loadTexts: juniMRouterAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniMRouterAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniMRouterAgent.setDescription('The agent capabilities definitions for the multicast router component of the SNMP agent in the Juniper E-series family of products.')
juniMRouterAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV1 = juniMRouterAgentV1.setProductRelease('Version 1 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component was supported in JUNOSe\n        4.1 and subsequent 4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV1 = juniMRouterAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniMRouterAgentV1.setDescription('The MIBs supported by the SNMP agent for the multicast router application in JUNOSe. These capabilities became obsolete when support was added for the Juniper-MROUTER-MIB.')
juniMRouterAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV2 = juniMRouterAgentV2.setProductRelease('Version 2 of the multicast router component of the JUNOSe SNMP agent.\n        These capabilities became obsolete when support was added to Juniper-MROUTER-MIB\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 5.0 and subsequent system releases upto 8.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV2 = juniMRouterAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniMRouterAgentV2.setDescription('The MIB supported by the SNMP agent for the multicast router application in JUNOSe. These capabilities became obsolete when juniMRouteConfGroup support was added to Juniper-MROUTER-MIB.')
juniMRouterAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV3 = juniMRouterAgentV3.setProductRelease('Version 3 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 8.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniMRouterAgentV3 = juniMRouterAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniMRouterAgentV3.setDescription('The MIB supported by the SNMP agent for the multicast router application in JUNOSe.These capabilities became obsolete when juniMcastGlobalConfGroup support was added to Juniper-MROUTER-MIB.')
uniMRouterAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV4 = uniMRouterAgentV4.setProductRelease('Version 4 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 8.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV4 = uniMRouterAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: uniMRouterAgentV4.setDescription('The MIB supported by the SNMP agent for the multicast router application in JUNOSe. These capabilities became obsolete when rsMRoutePortConfGroup support was added to Juniper-MROUTER-MIB.')
uniMRouterAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV5 = uniMRouterAgentV5.setProductRelease('Version 5 of the multicast router component of the JUNOSe SNMP agent.\n        This version of the multicast router component is supported in the\n        Juniper JUNOSe 8.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uniMRouterAgentV5 = uniMRouterAgentV5.setStatus('current')
if mibBuilder.loadTexts: uniMRouterAgentV5.setDescription('The MIB supported by the SNMP agent for the multicast router application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Multicast-Router-CONF", juniMRouterAgentV1=juniMRouterAgentV1, PYSNMP_MODULE_ID=juniMRouterAgent, juniMRouterAgent=juniMRouterAgent, juniMRouterAgentV3=juniMRouterAgentV3, uniMRouterAgentV4=uniMRouterAgentV4, juniMRouterAgentV2=juniMRouterAgentV2, uniMRouterAgentV5=uniMRouterAgentV5)
