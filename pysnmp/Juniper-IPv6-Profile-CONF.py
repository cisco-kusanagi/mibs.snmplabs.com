#
# PySNMP MIB module Juniper-IPv6-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IPv6-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Bits, NotificationType, TimeTicks, Unsigned32, MibIdentifier, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Bits", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpv6ProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5))
juniIpv6ProfileAgent.setRevisions(('2007-07-19 18:19', '2003-03-11 19:23',))
if mibBuilder.loadTexts: juniIpv6ProfileAgent.setLastUpdated('200707191819Z')
if mibBuilder.loadTexts: juniIpv6ProfileAgent.setOrganization('Juniper Networks, Inc.')
juniIpv6ProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV1 = juniIpv6ProfileAgentV1.setProductRelease('Version 1 of the IPv6 Profile component of the JUNOSe SNMP agent.  This\n        version of the IPv6 Profile component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV1 = juniIpv6ProfileAgentV1.setStatus('obsolete')
juniIpv6ProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV2 = juniIpv6ProfileAgentV2.setProductRelease('Version 2 of the IPv6 Profile component of the JUNOSe SNMP agent.  This\n        version of the IPv6 Profile component is supported in JUNOSe 8.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV2 = juniIpv6ProfileAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-IPv6-Profile-CONF", juniIpv6ProfileAgentV1=juniIpv6ProfileAgentV1, juniIpv6ProfileAgentV2=juniIpv6ProfileAgentV2, juniIpv6ProfileAgent=juniIpv6ProfileAgent, PYSNMP_MODULE_ID=juniIpv6ProfileAgent)
