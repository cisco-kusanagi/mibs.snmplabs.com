#
# PySNMP MIB module Unisphere-Data-Trace-Route-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Trace-Route-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:33:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
traceRouteGroup, traceRouteTimeStampGroup, traceRouteHopsTableGroup, traceRouteNotificationsGroup = mibBuilder.importSymbols("DISMAN-TRACEROUTE-MIB", "traceRouteGroup", "traceRouteTimeStampGroup", "traceRouteHopsTableGroup", "traceRouteNotificationsGroup")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, Gauge32, MibIdentifier, Bits, Counter32, ObjectIdentity, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "Counter32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdTraceRouteAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43))
usdTraceRouteAgent.setRevisions(('2001-03-29 19:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdTraceRouteAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdTraceRouteAgent.setLastUpdated('200103291907Z')
if mibBuilder.loadTexts: usdTraceRouteAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdTraceRouteAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdTraceRouteAgent.setDescription('The agent capabilities definitions for the Trace Route component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdTraceRouteAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdTraceRouteAgentV1 = usdTraceRouteAgentV1.setProductRelease('Version 1 of the Trace Route component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Trace Route component is supported in\n        the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdTraceRouteAgentV1 = usdTraceRouteAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdTraceRouteAgentV1.setDescription('The MIB supported by the SNMP agent for the Trace Route application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Trace-Route-CONF", usdTraceRouteAgent=usdTraceRouteAgent, usdTraceRouteAgentV1=usdTraceRouteAgentV1, PYSNMP_MODULE_ID=usdTraceRouteAgent)
