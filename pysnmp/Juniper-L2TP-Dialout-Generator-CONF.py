#
# PySNMP MIB module Juniper-L2TP-Dialout-Generator-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-L2TP-Dialout-Generator-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, MibIdentifier, iso, Unsigned32, ModuleIdentity, TimeTicks, Counter32, Counter64, Bits, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "iso", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "Counter64", "Bits", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniL2tpDialoutGeneratorAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 59))
juniL2tpDialoutGeneratorAgent.setRevisions(('2002-11-21 14:51',))
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setLastUpdated('200211211451Z')
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setOrganization('Juniper Networks, Inc.')
juniL2tpDialoutGeneratorAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 59, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpDialoutGeneratorAgentV1 = juniL2tpDialoutGeneratorAgentV1.setProductRelease('Version 1 of the L2TP Dialout Generator component of the JUNOSe SNMP\n        agent.  This version of the L2TP Dialout Generator component is\n        supported in JUNOSe 5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpDialoutGeneratorAgentV1 = juniL2tpDialoutGeneratorAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-L2TP-Dialout-Generator-CONF", juniL2tpDialoutGeneratorAgent=juniL2tpDialoutGeneratorAgent, PYSNMP_MODULE_ID=juniL2tpDialoutGeneratorAgent, juniL2tpDialoutGeneratorAgentV1=juniL2tpDialoutGeneratorAgentV1)
