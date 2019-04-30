#
# PySNMP MIB module Unisphere-Data-COPS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-COPS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, Unsigned32, Bits, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, TimeTicks, Integer32, Counter64, ModuleIdentity, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Bits", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdCopsProtocolGroup, usdCopsProtocolGroup2 = mibBuilder.importSymbols("Unisphere-Data-COPS-MIB", "usdCopsProtocolGroup", "usdCopsProtocolGroup2")
usdCopsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7))
usdCopsAgent.setRevisions(('2002-01-14 19:36', '2001-03-27 22:45',))
if mibBuilder.loadTexts: usdCopsAgent.setLastUpdated('200201141936Z')
if mibBuilder.loadTexts: usdCopsAgent.setOrganization('Unisphere Networks, Inc.')
usdCopsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV1 = usdCopsAgentV1.setProductRelease('Version 1 of the COPS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the COPS component was supported in the\n        Unisphere RX 2.x and 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV1 = usdCopsAgentV1.setStatus('current')
usdCopsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV2 = usdCopsAgentV2.setProductRelease('Version 2 of the COPS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the COPS component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsAgentV2 = usdCopsAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-COPS-CONF", usdCopsAgentV2=usdCopsAgentV2, PYSNMP_MODULE_ID=usdCopsAgent, usdCopsAgentV1=usdCopsAgentV1, usdCopsAgent=usdCopsAgent)
