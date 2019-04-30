#
# PySNMP MIB module Juniper-Ping-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Ping-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, Integer32, NotificationType, iso, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Bits, IpAddress, Counter32, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "iso", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Bits", "IpAddress", "Counter32", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPingAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30))
juniPingAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 14:14',))
if mibBuilder.loadTexts: juniPingAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniPingAgent.setOrganization('Juniper Networks, Inc.')
juniPingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPingAgentV1 = juniPingAgentV1.setProductRelease('Version 1 of the Ping component of the JUNOSe SNMP agent.  This version\n        of the Ping component is supported in JUNOSe 3.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPingAgentV1 = juniPingAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Ping-CONF", PYSNMP_MODULE_ID=juniPingAgent, juniPingAgentV1=juniPingAgentV1, juniPingAgent=juniPingAgent)
