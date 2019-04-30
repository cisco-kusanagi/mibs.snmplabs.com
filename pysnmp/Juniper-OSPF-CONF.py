#
# PySNMP MIB module Juniper-OSPF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-OSPF-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, NotificationType, TimeTicks, IpAddress, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, ModuleIdentity, Counter32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "NotificationType", "TimeTicks", "IpAddress", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "ModuleIdentity", "Counter32", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniOspfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28))
juniOspfAgent.setRevisions(('2002-09-06 16:54', '2001-12-06 15:12', '2001-03-29 13:34',))
if mibBuilder.loadTexts: juniOspfAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniOspfAgent.setOrganization('Juniper Networks, Inc.')
juniOspfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV1 = juniOspfAgentV1.setProductRelease('Version 1 of the OSPF component of the JUNOSe SNMP agent.  This version\n        of the OSPF component was supported in JUNOSe 2.x and 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV1 = juniOspfAgentV1.setStatus('obsolete')
juniOspfAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV2 = juniOspfAgentV2.setProductRelease('Version 2 of the OSPF component of the JUNOSe SNMP agent.  This version\n        of the OSPF component is supported in JUNOSe 4.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniOspfAgentV2 = juniOspfAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-OSPF-CONF", PYSNMP_MODULE_ID=juniOspfAgent, juniOspfAgentV1=juniOspfAgentV1, juniOspfAgentV2=juniOspfAgentV2, juniOspfAgent=juniOspfAgent)
