#
# PySNMP MIB module Juniper-DNS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DNS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, iso, TimeTicks, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, MibIdentifier, Gauge32, Bits, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "TimeTicks", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "MibIdentifier", "Gauge32", "Bits", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDnsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9))
juniDnsAgent.setRevisions(('2003-09-11 17:52', '2002-09-06 16:54', '2001-03-27 23:00',))
if mibBuilder.loadTexts: juniDnsAgent.setLastUpdated('200309111752Z')
if mibBuilder.loadTexts: juniDnsAgent.setOrganization('Juniper Networks, Inc.')
juniDnsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV1 = juniDnsAgentV1.setProductRelease('Version 1 of the DNS component of the JUNOSe SNMP agent.  This version\n        of the DNS component was supported in JUNOSe 3.0 thru 5.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV1 = juniDnsAgentV1.setStatus('obsolete')
juniDnsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV2 = juniDnsAgentV2.setProductRelease('Version 2 of the DNS component of the JUNOSe SNMP agent.  This version\n        of the DNS component is supported in JUNOSe 5.2 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV2 = juniDnsAgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-DNS-CONF", juniDnsAgent=juniDnsAgent, PYSNMP_MODULE_ID=juniDnsAgent, juniDnsAgentV1=juniDnsAgentV1, juniDnsAgentV2=juniDnsAgentV2)
