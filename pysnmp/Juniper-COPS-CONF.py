#
# PySNMP MIB module Juniper-COPS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-COPS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, MibIdentifier, ObjectIdentity, Gauge32, NotificationType, Integer32, Counter32, TimeTicks, ModuleIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "Counter32", "TimeTicks", "ModuleIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniCopsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7))
juniCopsAgent.setRevisions(('2002-09-06 16:54', '2002-01-14 19:36', '2001-03-27 22:45',))
if mibBuilder.loadTexts: juniCopsAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniCopsAgent.setOrganization('Juniper Networks, Inc.')
juniCopsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV1 = juniCopsAgentV1.setProductRelease('Version 1 of the COPS component of the JUNOSe SNMP agent.  This version\n        of the COPS component was supported in JUNOSe 2.x and 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV1 = juniCopsAgentV1.setStatus('current')
juniCopsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV2 = juniCopsAgentV2.setProductRelease('Version 2 of the COPS component of the JUNOSe SNMP agent.  This version\n        of the COPS component is supported in JUNOSe 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCopsAgentV2 = juniCopsAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-COPS-CONF", juniCopsAgentV2=juniCopsAgentV2, juniCopsAgent=juniCopsAgent, PYSNMP_MODULE_ID=juniCopsAgent, juniCopsAgentV1=juniCopsAgentV1)
