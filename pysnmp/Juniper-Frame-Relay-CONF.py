#
# PySNMP MIB module Juniper-Frame-Relay-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Frame-Relay-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibIdentifier, Counter32, NotificationType, ModuleIdentity, Counter64, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, TimeTicks, IpAddress, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "TimeTicks", "IpAddress", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniFrameRelayAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17))
juniFrameRelayAgent.setRevisions(('2002-09-27 15:58', '2001-04-18 19:26',))
if mibBuilder.loadTexts: juniFrameRelayAgent.setLastUpdated('200209271558Z')
if mibBuilder.loadTexts: juniFrameRelayAgent.setOrganization('Juniper Networks, Inc.')
juniFrameRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV1 = juniFrameRelayAgentV1.setProductRelease('Version 1 of the Frame Relay component of the JUNOSe SNMP agent.  This\n        version of the Frame Relay component was supported in JUNOSe 1.0 thru\n        4.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV1 = juniFrameRelayAgentV1.setStatus('obsolete')
juniFrameRelayAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV2 = juniFrameRelayAgentV2.setProductRelease('Version 2 of the Frame Relay component of the JUNOSe SNMP agent.  This\n        version of the Frame Relay component is supported in JUNOSe 5.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFrameRelayAgentV2 = juniFrameRelayAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Frame-Relay-CONF", juniFrameRelayAgent=juniFrameRelayAgent, juniFrameRelayAgentV2=juniFrameRelayAgentV2, PYSNMP_MODULE_ID=juniFrameRelayAgent, juniFrameRelayAgentV1=juniFrameRelayAgentV1)
