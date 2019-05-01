#
# PySNMP MIB module Juniper-Trace-Route-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Trace-Route-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, iso, Gauge32, NotificationType, TimeTicks, Bits, Unsigned32, Integer32, Counter32, MibIdentifier, IpAddress, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "NotificationType", "TimeTicks", "Bits", "Unsigned32", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniTraceRouteAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43))
juniTraceRouteAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 19:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniTraceRouteAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniTraceRouteAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniTraceRouteAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniTraceRouteAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniTraceRouteAgent.setDescription('The agent capabilities definitions for the Trace Route component of the SNMP agent in the Juniper E-series family of products.')
juniTraceRouteAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTraceRouteAgentV1 = juniTraceRouteAgentV1.setProductRelease('Version 1 of the Trace Route component of the JUNOSe SNMP agent.  This\n        version of the Trace Route component is supported in JUNOSe 3.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTraceRouteAgentV1 = juniTraceRouteAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniTraceRouteAgentV1.setDescription('The MIB supported by the SNMP agent for the Trace Route application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Trace-Route-CONF", juniTraceRouteAgentV1=juniTraceRouteAgentV1, juniTraceRouteAgent=juniTraceRouteAgent, PYSNMP_MODULE_ID=juniTraceRouteAgent)
