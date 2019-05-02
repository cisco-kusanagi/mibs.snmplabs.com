#
# PySNMP MIB module Juniper-Ha-Redundancy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Ha-Redundancy-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Counter64, ObjectIdentity, Integer32, Gauge32, IpAddress, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Counter64", "ObjectIdentity", "Integer32", "Gauge32", "IpAddress", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniHaRedundancyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 69))
juniHaRedundancyAgent.setRevisions(('2004-02-02 16:46',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniHaRedundancyAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniHaRedundancyAgent.setLastUpdated('200402021646Z')
if mibBuilder.loadTexts: juniHaRedundancyAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniHaRedundancyAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniHaRedundancyAgent.setDescription('The agent capabilities definitions for the Ha Redundancy component of the SNMP agent in the Juniper E-series family of products.')
juniHaRedundancyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 69, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHaRedundancyAgentV1 = juniHaRedundancyAgentV1.setProductRelease('Version 1 of the Ha Redundancy component of the JUNOSe SNMP agent.\n        This version of the Ha Redundancy component is supported in JUNOSe 6.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHaRedundancyAgentV1 = juniHaRedundancyAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniHaRedundancyAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the Ha Redundancy application.')
mibBuilder.exportSymbols("Juniper-Ha-Redundancy-CONF", juniHaRedundancyAgentV1=juniHaRedundancyAgentV1, PYSNMP_MODULE_ID=juniHaRedundancyAgent, juniHaRedundancyAgent=juniHaRedundancyAgent)
