#
# PySNMP MIB module Juniper-IS-IS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IS-IS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, iso, ObjectIdentity, Unsigned32, NotificationType, IpAddress, Integer32, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Unsigned32", "NotificationType", "IpAddress", "Integer32", "MibIdentifier", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIsisAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23))
juniIsisAgent.setRevisions(('2002-09-06 16:54', '2002-04-04 20:37', '2001-04-24 19:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIsisAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added MPLS support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIsisAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniIsisAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIsisAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIsisAgent.setDescription('The agent capabilities definitions for the intermediate system to intermediate system (IS-IS) protocol management component of the SNMP agent in the Juniper E-series family of products.')
juniIsisAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV1 = juniIsisAgentV1.setProductRelease('Version 1 of the IS-IS component of the JUNOSe SNMP agent.  This\n        version of the IS-IS component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV1 = juniIsisAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIsisAgentV1.setDescription('The MIB supported by the SNMP agent for the intermediate system to intermediate system (IS-IS) protocol application in JUNOSe. These capabilities became obsolete when the juniIsisCircState object was added.')
juniIsisAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV2 = juniIsisAgentV2.setProductRelease('Version 2 of the IS-IS component of the JUNOSe SNMP agent.  This\n        version of the IS-IS component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV2 = juniIsisAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniIsisAgentV2.setDescription('The MIB supported by the SNMP agent for the intermediate system to intermediate system (IS-IS) protocol application in JUNOSe. These capabilities became obsolete when MPLS support was added.')
juniIsisAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV3 = juniIsisAgentV3.setProductRelease('Version 3 of the IS-IS component of the JUNOSe SNMP agent.  This\n        version of the IS-IS component is supported in JUNOSe 4.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV3 = juniIsisAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniIsisAgentV3.setDescription('The MIB supported by the SNMP agent for the intermediate system to intermediate system (IS-IS) protocol application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-IS-IS-CONF", juniIsisAgentV1=juniIsisAgentV1, juniIsisAgent=juniIsisAgent, juniIsisAgentV3=juniIsisAgentV3, juniIsisAgentV2=juniIsisAgentV2, PYSNMP_MODULE_ID=juniIsisAgent)
