#
# PySNMP MIB module Juniper-CLI-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-CLI-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, MibIdentifier, ObjectIdentity, Unsigned32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, NotificationType, Counter32, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "NotificationType", "Counter32", "Counter64", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniCliAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6))
juniCliAgent.setRevisions(('2007-10-10 09:22', '2002-09-06 16:54', '2001-03-27 22:30',))
if mibBuilder.loadTexts: juniCliAgent.setLastUpdated('200710100922Z')
if mibBuilder.loadTexts: juniCliAgent.setOrganization('Juniper Networks, Inc.')
juniCliAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV1 = juniCliAgentV1.setProductRelease('Version 1 of the CLI Security Management component of JUNOSe SNMP\n        agent.  This version of the CLI Security Management component is\n        supported in JUNOSe 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV1 = juniCliAgentV1.setStatus('obsolete')
juniCliAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV2 = juniCliAgentV2.setProductRelease('Version 2 of the CLI component of JUNOSe SNMP agent.\n        This version of the CLI component is supported in JUNOSe 9.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliAgentV2 = juniCliAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-CLI-CONF", juniCliAgent=juniCliAgent, juniCliAgentV1=juniCliAgentV1, juniCliAgentV2=juniCliAgentV2, PYSNMP_MODULE_ID=juniCliAgent)
