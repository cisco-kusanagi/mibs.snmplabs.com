#
# PySNMP MIB module Juniper-Entity-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Entity-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, IpAddress, MibIdentifier, NotificationType, Counter32, Unsigned32, TimeTicks, Bits, ModuleIdentity, Gauge32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "IpAddress", "MibIdentifier", "NotificationType", "Counter32", "Unsigned32", "TimeTicks", "Bits", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniEntityAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13))
juniEntityAgent.setRevisions(('2002-09-06 16:54', '2001-04-27 13:16',))
if mibBuilder.loadTexts: juniEntityAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniEntityAgent.setOrganization('Juniper Networks, Inc.')
juniEntityAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV1 = juniEntityAgentV1.setProductRelease('Version 1 of the logical Entity component of the JUNOSe SNMP agent.\n        This version of the logical Entity component was supported in JUNOSe 2.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV1 = juniEntityAgentV1.setStatus('obsolete')
juniEntityAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV2 = juniEntityAgentV2.setProductRelease('Version 2 of the physical and logical Entity components of the Juniper\n        JUNOSe SNMP agent.  This version of the physical and logical Entity\n        components is supported in JUNOSe 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniEntityAgentV2 = juniEntityAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Entity-CONF", PYSNMP_MODULE_ID=juniEntityAgent, juniEntityAgentV1=juniEntityAgentV1, juniEntityAgentV2=juniEntityAgentV2, juniEntityAgent=juniEntityAgent)
