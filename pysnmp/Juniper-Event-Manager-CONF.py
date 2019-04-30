#
# PySNMP MIB module Juniper-Event-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Event-Manager-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Gauge32, ObjectIdentity, Counter64, IpAddress, Counter32, Bits, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "Counter32", "Bits", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniEventManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62))
juniEventManagerAgent.setRevisions(('2003-10-30 14:43', '2003-05-12 14:22',))
if mibBuilder.loadTexts: juniEventManagerAgent.setLastUpdated('200310301443Z')
if mibBuilder.loadTexts: juniEventManagerAgent.setOrganization('Juniper Networks, Inc.')
juniEventManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV1 = juniEventManagerAgentV1.setProductRelease('Version 1 of the Event Manager component of the JUNOSe SNMP agent.\n        This version of the Event Manager component was supported in JUNOSe 5.1\n        and 5.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV1 = juniEventManagerAgentV1.setStatus('obsolete')
juniEventManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 62, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV2 = juniEventManagerAgentV2.setProductRelease('Version 2 of the Event Manager component of the JUNOSe SNMP agent.\n        This version of the Event Manager component is supported in JUNOSe 5.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEventManagerAgentV2 = juniEventManagerAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Event-Manager-CONF", juniEventManagerAgentV1=juniEventManagerAgentV1, juniEventManagerAgentV2=juniEventManagerAgentV2, juniEventManagerAgent=juniEventManagerAgent, PYSNMP_MODULE_ID=juniEventManagerAgent)
