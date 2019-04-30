#
# PySNMP MIB module Juniper-Subscriber-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Subscriber-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
NotificationType, TimeTicks, MibIdentifier, IpAddress, iso, Counter32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Gauge32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "MibIdentifier", "IpAddress", "iso", "Counter32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniSubscriberAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45))
juniSubscriberAgent.setRevisions(('2002-09-06 16:54', '2002-05-10 20:17', '2001-03-30 15:25',))
if mibBuilder.loadTexts: juniSubscriberAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniSubscriberAgent.setOrganization('Juniper Networks, Inc.')
juniSubscriberAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV1 = juniSubscriberAgentV1.setProductRelease('Version 1 of the Subscriber component of the JUNOSe SNMP agent.  This\n        version of the Subscriber component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV1 = juniSubscriberAgentV1.setStatus('obsolete')
juniSubscriberAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV2 = juniSubscriberAgentV2.setProductRelease('Version 2 of the Subscriber component of the JUNOSe SNMP agent.  This\n        version of the Subscriber component is supported in JUNOSe 4.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberAgentV2 = juniSubscriberAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Subscriber-CONF", juniSubscriberAgentV1=juniSubscriberAgentV1, PYSNMP_MODULE_ID=juniSubscriberAgent, juniSubscriberAgentV2=juniSubscriberAgentV2, juniSubscriberAgent=juniSubscriberAgent)
