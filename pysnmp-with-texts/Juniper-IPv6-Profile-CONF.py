#
# PySNMP MIB module Juniper-IPv6-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IPv6-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniProfileAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniProfileAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, MibIdentifier, TimeTicks, NotificationType, Gauge32, IpAddress, Counter64, Unsigned32, ObjectIdentity, Bits, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "MibIdentifier", "TimeTicks", "NotificationType", "Gauge32", "IpAddress", "Counter64", "Unsigned32", "ObjectIdentity", "Bits", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIpv6ProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5))
juniIpv6ProfileAgent.setRevisions(('2007-07-19 18:19', '2003-03-11 19:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIpv6ProfileAgent.setRevisionsDescriptions(('Added ND support on dynamic interface.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIpv6ProfileAgent.setLastUpdated('200707191819Z')
if mibBuilder.loadTexts: juniIpv6ProfileAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIpv6ProfileAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIpv6ProfileAgent.setDescription('The agent capabilities definitions for the IPv6 Profile component of the SNMP agent in the Juniper E-series family of products.')
juniIpv6ProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV1 = juniIpv6ProfileAgentV1.setProductRelease('Version 1 of the IPv6 Profile component of the JUNOSe SNMP agent.  This\n        version of the IPv6 Profile component is supported in JUNOSe 5.1 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV1 = juniIpv6ProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIpv6ProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the IPv6 Profile application in JUNOSe.')
juniIpv6ProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV2 = juniIpv6ProfileAgentV2.setProductRelease('Version 2 of the IPv6 Profile component of the JUNOSe SNMP agent.  This\n        version of the IPv6 Profile component is supported in JUNOSe 8.2 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpv6ProfileAgentV2 = juniIpv6ProfileAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniIpv6ProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the IPv6 Profile application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-IPv6-Profile-CONF", juniIpv6ProfileAgentV2=juniIpv6ProfileAgentV2, juniIpv6ProfileAgentV1=juniIpv6ProfileAgentV1, juniIpv6ProfileAgent=juniIpv6ProfileAgent, PYSNMP_MODULE_ID=juniIpv6ProfileAgent)
