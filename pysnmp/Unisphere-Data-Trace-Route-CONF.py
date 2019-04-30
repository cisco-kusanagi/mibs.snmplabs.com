#
# PySNMP MIB module Unisphere-Data-Trace-Route-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Trace-Route-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
traceRouteHopsTableGroup, traceRouteNotificationsGroup, traceRouteGroup, traceRouteTimeStampGroup = mibBuilder.importSymbols("DISMAN-TRACEROUTE-MIB", "traceRouteHopsTableGroup", "traceRouteNotificationsGroup", "traceRouteGroup", "traceRouteTimeStampGroup")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, iso, Counter64, NotificationType, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibIdentifier, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "iso", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibIdentifier", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdTraceRouteAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43))
usdTraceRouteAgent.setRevisions(('2001-03-29 19:07',))
if mibBuilder.loadTexts: usdTraceRouteAgent.setLastUpdated('200103291907Z')
if mibBuilder.loadTexts: usdTraceRouteAgent.setOrganization('Unisphere Networks, Inc.')
usdTraceRouteAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdTraceRouteAgentV1 = usdTraceRouteAgentV1.setProductRelease('Version 1 of the Trace Route component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Trace Route component is supported in\n        the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdTraceRouteAgentV1 = usdTraceRouteAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Trace-Route-CONF", PYSNMP_MODULE_ID=usdTraceRouteAgent, usdTraceRouteAgentV1=usdTraceRouteAgentV1, usdTraceRouteAgent=usdTraceRouteAgent)
