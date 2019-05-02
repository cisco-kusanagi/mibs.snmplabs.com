#
# PySNMP MIB module Juniper-DNS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DNS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, iso, MibIdentifier, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Unsigned32, Counter32, IpAddress, Bits, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "MibIdentifier", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Unsigned32", "Counter32", "IpAddress", "Bits", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniDnsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9))
juniDnsAgent.setRevisions(('2003-09-11 17:52', '2002-09-06 16:54', '2001-03-27 23:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDnsAgent.setRevisionsDescriptions(('Added IPv6 address support.', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDnsAgent.setLastUpdated('200309111752Z')
if mibBuilder.loadTexts: juniDnsAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDnsAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDnsAgent.setDescription('The agent capabilities definitions for the DNS component of the SNMP agent in the Juniper E-series family of products.')
juniDnsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV1 = juniDnsAgentV1.setProductRelease('Version 1 of the DNS component of the JUNOSe SNMP agent.  This version\n        of the DNS component was supported in JUNOSe 3.0 thru 5.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV1 = juniDnsAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDnsAgentV1.setDescription('The MIB supported by the SNMP agent for the DNS application in JUNOSe. These capabilities became obsolete when IPv6 address support was added.')
juniDnsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV2 = juniDnsAgentV2.setProductRelease('Version 2 of the DNS component of the JUNOSe SNMP agent.  This version\n        of the DNS component is supported in JUNOSe 5.2 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsAgentV2 = juniDnsAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniDnsAgentV2.setDescription('The MIB supported by the SNMP agent for the DNS application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-DNS-CONF", juniDnsAgent=juniDnsAgent, PYSNMP_MODULE_ID=juniDnsAgent, juniDnsAgentV2=juniDnsAgentV2, juniDnsAgentV1=juniDnsAgentV1)
