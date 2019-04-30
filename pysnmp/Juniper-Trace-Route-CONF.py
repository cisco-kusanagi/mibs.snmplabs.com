#
# PySNMP MIB module Juniper-Trace-Route-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Trace-Route-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, Unsigned32, Integer32, Gauge32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Integer32", "Gauge32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniTraceRouteAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43))
juniTraceRouteAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 19:07',))
if mibBuilder.loadTexts: juniTraceRouteAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniTraceRouteAgent.setOrganization('Juniper Networks, Inc.')
juniTraceRouteAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTraceRouteAgentV1 = juniTraceRouteAgentV1.setProductRelease('Version 1 of the Trace Route component of the JUNOSe SNMP agent.  This\n        version of the Trace Route component is supported in JUNOSe 3.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTraceRouteAgentV1 = juniTraceRouteAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Trace-Route-CONF", juniTraceRouteAgent=juniTraceRouteAgent, PYSNMP_MODULE_ID=juniTraceRouteAgent, juniTraceRouteAgentV1=juniTraceRouteAgentV1)
