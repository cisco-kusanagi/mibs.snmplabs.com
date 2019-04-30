#
# PySNMP MIB module Juniper-DHCPv6-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DHCPv6-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, MibIdentifier, ModuleIdentity, Counter32, Integer32, IpAddress, TimeTicks, Gauge32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "Integer32", "IpAddress", "TimeTicks", "Gauge32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDhcpv6Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 64))
juniDhcpv6Agent.setRevisions(('2003-05-08 17:55',))
if mibBuilder.loadTexts: juniDhcpv6Agent.setLastUpdated('200305081755Z')
if mibBuilder.loadTexts: juniDhcpv6Agent.setOrganization('Juniper Networks, Inc.')
juniDhcpv6AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 64, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpv6AgentV1 = juniDhcpv6AgentV1.setProductRelease('Version 1 of the DHCPv6 component of the Juniper JUNOSe SNMP agent.\n        This version of the DHCPv6 component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpv6AgentV1 = juniDhcpv6AgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-DHCPv6-CONF", juniDhcpv6AgentV1=juniDhcpv6AgentV1, PYSNMP_MODULE_ID=juniDhcpv6Agent, juniDhcpv6Agent=juniDhcpv6Agent)
