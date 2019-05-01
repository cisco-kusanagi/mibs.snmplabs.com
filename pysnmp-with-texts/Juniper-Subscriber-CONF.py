#
# PySNMP MIB module Juniper-Subscriber-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Subscriber-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, Integer32, Gauge32, Bits, iso, ModuleIdentity, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Gauge32", "Bits", "iso", "ModuleIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSubscriberAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45))
juniSubscriberAgent.setRevisions(('2002-09-06 16:54', '2002-05-10 20:17', '2001-03-30 15:25',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSubscriberAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added local authentication support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniSubscriberAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniSubscriberAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSubscriberAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniSubscriberAgent.setDescription('The agent capabilities definitions for the Subscriber component of the SNMP agent in the Juniper E-series family of products.')
juniSubscriberAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV1 = juniSubscriberAgentV1.setProductRelease('Version 1 of the Subscriber component of the JUNOSe SNMP agent.  This\n        version of the Subscriber component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV1 = juniSubscriberAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniSubscriberAgentV1.setDescription('The MIB supported by the SNMP agent for subscriber capabilities in JUNOSe. These capabilities became obsolete when local authentication support was added.')
juniSubscriberAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV2 = juniSubscriberAgentV2.setProductRelease('Version 2 of the Subscriber component of the JUNOSe SNMP agent.  This\n        version of the Subscriber component is supported in JUNOSe 4.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV2 = juniSubscriberAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniSubscriberAgentV2.setDescription('The MIB supported by the SNMP agent for subscriber capabilities in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Subscriber-CONF", PYSNMP_MODULE_ID=juniSubscriberAgent, juniSubscriberAgent=juniSubscriberAgent, juniSubscriberAgentV2=juniSubscriberAgentV2, juniSubscriberAgentV1=juniSubscriberAgentV1)
