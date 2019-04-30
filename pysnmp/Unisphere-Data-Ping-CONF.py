#
# PySNMP MIB module Unisphere-Data-Ping-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Ping-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
pingNotificationsGroup, pingGroup, pingTimeStampGroup = mibBuilder.importSymbols("DISMAN-PING-MIB", "pingNotificationsGroup", "pingGroup", "pingTimeStampGroup")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, Counter32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, ObjectIdentity, IpAddress, Gauge32, TimeTicks, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "ObjectIdentity", "IpAddress", "Gauge32", "TimeTicks", "Integer32", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPingAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30))
usdPingAgent.setRevisions(('2001-03-29 14:14',))
if mibBuilder.loadTexts: usdPingAgent.setLastUpdated('200103291414Z')
if mibBuilder.loadTexts: usdPingAgent.setOrganization('Unisphere Networks, Inc.')
usdPingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPingAgentV1 = usdPingAgentV1.setProductRelease('Version 1 of the Ping component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Ping component is supported in the\n        Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPingAgentV1 = usdPingAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Ping-CONF", PYSNMP_MODULE_ID=usdPingAgent, usdPingAgentV1=usdPingAgentV1, usdPingAgent=usdPingAgent)
