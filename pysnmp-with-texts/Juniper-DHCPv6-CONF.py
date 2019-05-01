#
# PySNMP MIB module Juniper-DHCPv6-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DHCPv6-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, Counter64, IpAddress, ModuleIdentity, Integer32, Bits, iso, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "IpAddress", "ModuleIdentity", "Integer32", "Bits", "iso", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDhcpv6Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 64))
juniDhcpv6Agent.setRevisions(('2003-05-08 17:55',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDhcpv6Agent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDhcpv6Agent.setLastUpdated('200305081755Z')
if mibBuilder.loadTexts: juniDhcpv6Agent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDhcpv6Agent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDhcpv6Agent.setDescription('The agent capabilities definitions for the DHCPv6 component of the SNMP agent in the Juniper E-series family of products.')
juniDhcpv6AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 64, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpv6AgentV1 = juniDhcpv6AgentV1.setProductRelease('Version 1 of the DHCPv6 component of the Juniper JUNOSe SNMP agent.\n        This version of the DHCPv6 component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpv6AgentV1 = juniDhcpv6AgentV1.setStatus('current')
if mibBuilder.loadTexts: juniDhcpv6AgentV1.setDescription('The MIB supported by the SNMP agent for the DHCPv6 application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-DHCPv6-CONF", juniDhcpv6Agent=juniDhcpv6Agent, juniDhcpv6AgentV1=juniDhcpv6AgentV1, PYSNMP_MODULE_ID=juniDhcpv6Agent)
