#
# PySNMP MIB module Juniper-IS-IS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IS-IS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, Counter64, Gauge32, TimeTicks, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter64", "Gauge32", "TimeTicks", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniIsisAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23))
juniIsisAgent.setRevisions(('2002-09-06 16:54', '2002-04-04 20:37', '2001-04-24 19:30',))
if mibBuilder.loadTexts: juniIsisAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniIsisAgent.setOrganization('Juniper Networks, Inc.')
juniIsisAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV1 = juniIsisAgentV1.setProductRelease('Version 1 of the IS-IS component of the JUNOSe SNMP agent.  This\n        version of the IS-IS component was supported in JUNOSe 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV1 = juniIsisAgentV1.setStatus('obsolete')
juniIsisAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV2 = juniIsisAgentV2.setProductRelease('Version 2 of the IS-IS component of the JUNOSe SNMP agent.  This\n        version of the IS-IS component was supported in JUNOSe 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV2 = juniIsisAgentV2.setStatus('current')
juniIsisAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV3 = juniIsisAgentV3.setProductRelease('Version 3 of the IS-IS component of the JUNOSe SNMP agent.  This\n        version of the IS-IS component is supported in JUNOSe 4.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIsisAgentV3 = juniIsisAgentV3.setStatus('current')
mibBuilder.exportSymbols("Juniper-IS-IS-CONF", juniIsisAgentV3=juniIsisAgentV3, PYSNMP_MODULE_ID=juniIsisAgent, juniIsisAgentV2=juniIsisAgentV2, juniIsisAgentV1=juniIsisAgentV1, juniIsisAgent=juniIsisAgent)
