#
# PySNMP MIB module Juniper-IKE-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IKE-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, Bits, MibIdentifier, IpAddress, iso, NotificationType, Counter32, TimeTicks, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibIdentifier", "IpAddress", "iso", "NotificationType", "Counter32", "TimeTicks", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIkeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66))
juniIkeAgent.setRevisions(('2004-01-23 15:21', '2003-10-23 20:17',))
if mibBuilder.loadTexts: juniIkeAgent.setLastUpdated('200401231521Z')
if mibBuilder.loadTexts: juniIkeAgent.setOrganization('Juniper Networks, Inc.')
juniIkeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV1 = juniIkeAgentV1.setProductRelease('Version 1 of the IKE component of the JUNOSe SNMP agent.  This version\n        of the IKE component was supported in JUNOSe 5.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV1 = juniIkeAgentV1.setStatus('obsolete')
juniIkeAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV2 = juniIkeAgentV2.setProductRelease('Version 2 of the IKE component of the JUNOSe SNMP agent.  This version\n        of the IKE component is supported in JUNOSe 6.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV2 = juniIkeAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-IKE-CONF", juniIkeAgentV1=juniIkeAgentV1, juniIkeAgent=juniIkeAgent, juniIkeAgentV2=juniIkeAgentV2, PYSNMP_MODULE_ID=juniIkeAgent)
