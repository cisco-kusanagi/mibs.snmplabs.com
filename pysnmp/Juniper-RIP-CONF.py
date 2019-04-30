#
# PySNMP MIB module Juniper-RIP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RIP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, IpAddress, Integer32, TimeTicks, Gauge32, ObjectIdentity, Counter32, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniRipAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36))
juniRipAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 18:13',))
if mibBuilder.loadTexts: juniRipAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniRipAgent.setOrganization('Juniper Networks, Inc.')
juniRipAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRipAgentV1 = juniRipAgentV1.setProductRelease('Version 1 of the RIP component of the JUNOSe SNMP agent.  This version\n        of the RIP component is supported in JUNOSe 1.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRipAgentV1 = juniRipAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-RIP-CONF", PYSNMP_MODULE_ID=juniRipAgent, juniRipAgent=juniRipAgent, juniRipAgentV1=juniRipAgentV1)
