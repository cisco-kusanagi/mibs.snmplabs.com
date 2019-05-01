#
# PySNMP MIB module Juniper-IGMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IGMP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibIdentifier, Unsigned32, Integer32, Gauge32, Counter64, NotificationType, iso, TimeTicks, Counter32, ObjectIdentity, IpAddress, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Integer32", "Gauge32", "Counter64", "NotificationType", "iso", "TimeTicks", "Counter32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIgmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19))
juniIgmpAgent.setRevisions(('2006-08-25 05:40', '2003-09-29 18:22', '2002-10-28 15:06', '2002-08-29 20:48', '2001-03-28 17:20',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIgmpAgent.setRevisionsDescriptions(('Added rsIgmpIfLocationType for support on REX platform and deprecated rsIgmpGroupsTable.', 'Juniper-IGMP-MIB: Added IGMP admin state support.', 'Juniper-IGMP-MIB: Replaced Unisphere names with Juniper names. Added support for interface addresses and multicast group limits.', 'IGMP-STD-MIB: Added support for the IETF IGMP MIB (RFC 2933).', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIgmpAgent.setLastUpdated('200608250540Z')
if mibBuilder.loadTexts: juniIgmpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIgmpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIgmpAgent.setDescription('The agent capabilities definitions for the Internet Group Management Protocol (IGMP) component of the SNMP agent in the Juniper E-series family of products.')
juniIgmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV1 = juniIgmpAgentV1.setProductRelease('Version 1 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component was supported in JUNOSe 3.0 thru 4.0 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV1 = juniIgmpAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIgmpAgentV1.setDescription('The MIB supported by the SNMP agent for the IGMP application in JUNOSe. These capabilities became obsolete when support was added for the IGMP-STD-MIB (RFC 2933).')
juniIgmpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV2 = juniIgmpAgentV2.setProductRelease('Version 2 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component was supported in JUNOSe 4.1 and subsequent 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV2 = juniIgmpAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniIgmpAgentV2.setDescription('The MIBs supported by the SNMP agent for the IGMP application in JUNOSe. These capabilities became obsolete when support was added to Juniper-IGMP-MIB for interface addresses and multicast group limits.')
juniIgmpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV3 = juniIgmpAgentV3.setProductRelease('Version 3 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component was supported in JUNOSe 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV3 = juniIgmpAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniIgmpAgentV3.setDescription('The MIBs supported by the SNMP agent for the IGMP application in JUNOSe. These capabilities became obsolete when support was added to Juniper-IGMP-MIB for the administrative state object.')
juniIgmpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV4 = juniIgmpAgentV4.setProductRelease('Version 4 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component is supported in JUNOSe 5.1 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV4 = juniIgmpAgentV4.setStatus('deprecated')
if mibBuilder.loadTexts: juniIgmpAgentV4.setDescription('The MIBs supported by the SNMP agent for the IGMP application in JUNOSe.')
juniIgmpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV5 = juniIgmpAgentV5.setProductRelease('Version 5 of the IGMP component of the JUNOSe SNMP agent.  This version\n        of the IGMP component is supported in JUNOSe 7.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIgmpAgentV5 = juniIgmpAgentV5.setStatus('current')
if mibBuilder.loadTexts: juniIgmpAgentV5.setDescription('The MIBs supported by the SNMP agent for the IGMP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-IGMP-CONF", juniIgmpAgentV5=juniIgmpAgentV5, juniIgmpAgentV2=juniIgmpAgentV2, juniIgmpAgentV1=juniIgmpAgentV1, juniIgmpAgentV4=juniIgmpAgentV4, juniIgmpAgent=juniIgmpAgent, juniIgmpAgentV3=juniIgmpAgentV3, PYSNMP_MODULE_ID=juniIgmpAgent)
