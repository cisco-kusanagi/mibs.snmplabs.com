#
# PySNMP MIB module Unisphere-Data-Subscriber-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Subscriber-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, MibIdentifier, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter32, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibIdentifier", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter32", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSubscriberLocalGroup2, usdSubscriberLocalGroup = mibBuilder.importSymbols("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscriberLocalGroup2", "usdSubscriberLocalGroup")
usdSubscriberAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45))
usdSubscriberAgent.setRevisions(('2002-05-10 20:17', '2001-03-30 15:25',))
if mibBuilder.loadTexts: usdSubscriberAgent.setLastUpdated('200205102017Z')
if mibBuilder.loadTexts: usdSubscriberAgent.setOrganization('Unisphere Networks, Inc.')
usdSubscriberAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberAgentV1 = usdSubscriberAgentV1.setProductRelease('Version 1 of the Subscriber component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Subscriber component was supported in\n        the Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberAgentV1 = usdSubscriberAgentV1.setStatus('obsolete')
usdSubscriberAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 45, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberAgentV2 = usdSubscriberAgentV2.setProductRelease('Version 2 of the Subscriber component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Subscriber component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberAgentV2 = usdSubscriberAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Subscriber-CONF", usdSubscriberAgentV1=usdSubscriberAgentV1, usdSubscriberAgent=usdSubscriberAgent, usdSubscriberAgentV2=usdSubscriberAgentV2, PYSNMP_MODULE_ID=usdSubscriberAgent)
