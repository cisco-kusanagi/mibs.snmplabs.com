#
# PySNMP MIB module Juniper-SMDS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-SMDS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Bits, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Bits", "iso", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSmdsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46))
juniSmdsAgent.setRevisions(('2002-09-06 16:54', '2001-09-20 14:57', '2001-03-30 14:30',))
if mibBuilder.loadTexts: juniSmdsAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniSmdsAgent.setOrganization('Juniper Networks, Inc.')
juniSmdsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV1 = juniSmdsAgentV1.setProductRelease('Version 1 of the Switched Multimegabit Data Service (SMDS) management\n        component of the JUNOSe SNMP agent.  This version of the SMDS component\n        was supported in JUNOSe 3.1 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV1 = juniSmdsAgentV1.setStatus('obsolete')
juniSmdsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV2 = juniSmdsAgentV2.setProductRelease('Version 2 of the Switched Multimegabit Data Service (SMDS) management\n        component of the JUNOSe SNMP agent.  This version of the SMDS component\n        is supported in JUNOSe 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSmdsAgentV2 = juniSmdsAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-SMDS-CONF", juniSmdsAgentV1=juniSmdsAgentV1, juniSmdsAgent=juniSmdsAgent, juniSmdsAgentV2=juniSmdsAgentV2, PYSNMP_MODULE_ID=juniSmdsAgent)
