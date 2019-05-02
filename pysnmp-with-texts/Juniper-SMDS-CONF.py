#
# PySNMP MIB module Juniper-SMDS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SMDS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Counter32, iso, Unsigned32, IpAddress, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "iso", "Unsigned32", "IpAddress", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSmdsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46))
juniSmdsAgent.setRevisions(('2002-09-06 16:54', '2001-09-20 14:57', '2001-03-30 14:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSmdsAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added support for major and sub interfaces.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSmdsAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniSmdsAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSmdsAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSmdsAgent.setDescription('The agent capabilities definitions for the Switched Multimegabit Data Service (SMDS) management component of the SNMP agent in the Juniper E-series family of products.')
juniSmdsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV1 = juniSmdsAgentV1.setProductRelease('Version 1 of the Switched Multimegabit Data Service (SMDS) management\n        component of the JUNOSe SNMP agent.  This version of the SMDS component\n        was supported in JUNOSe 3.1 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV1 = juniSmdsAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSmdsAgentV1.setDescription('The MIB supported by the SNMP agent for the SMDS application in JUNOSe. These capabilities became obsolete when support was added for major and sub interfaces')
juniSmdsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV2 = juniSmdsAgentV2.setProductRelease('Version 2 of the Switched Multimegabit Data Service (SMDS) management\n        component of the JUNOSe SNMP agent.  This version of the SMDS component\n        is supported in JUNOSe 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV2 = juniSmdsAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniSmdsAgentV2.setDescription('The MIB supported by the SNMP agent for the SMDS application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-SMDS-CONF", juniSmdsAgent=juniSmdsAgent, PYSNMP_MODULE_ID=juniSmdsAgent, juniSmdsAgentV1=juniSmdsAgentV1, juniSmdsAgentV2=juniSmdsAgentV2)
