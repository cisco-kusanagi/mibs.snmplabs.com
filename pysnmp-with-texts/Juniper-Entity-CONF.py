#
# PySNMP MIB module Juniper-Entity-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Entity-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, Counter64, Unsigned32, IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, ObjectIdentity, iso, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter64", "Unsigned32", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniEntityAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13))
juniEntityAgent.setRevisions(('2002-09-06 16:54', '2001-04-27 13:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniEntityAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniEntityAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniEntityAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniEntityAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniEntityAgent.setDescription('The agent capabilities definitions for the physical and logical entity components of the SNMP agent in the Juniper E-series family of products.')
juniEntityAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV1 = juniEntityAgentV1.setProductRelease('Version 1 of the logical Entity component of the JUNOSe SNMP agent.\n        This version of the logical Entity component was supported in JUNOSe 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV1 = juniEntityAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniEntityAgentV1.setDescription('The MIB supported by the SNMP agent for the Router Agent (logical entity) application in JUNOSe. These capabilities became obsolete when support was add for the physical entity table, the physical entity contains table, and RFC 2737 enhancements to the logical entity table.')
juniEntityAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV2 = juniEntityAgentV2.setProductRelease('Version 2 of the physical and logical Entity components of the Juniper\n        JUNOSe SNMP agent.  This version of the physical and logical Entity\n        components is supported in JUNOSe 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV2 = juniEntityAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniEntityAgentV2.setDescription('The MIB supported by the SNMP agent for the System (physical entity) and Router Agent (logical entity) applications in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Entity-CONF", juniEntityAgentV2=juniEntityAgentV2, juniEntityAgentV1=juniEntityAgentV1, PYSNMP_MODULE_ID=juniEntityAgent, juniEntityAgent=juniEntityAgent)
