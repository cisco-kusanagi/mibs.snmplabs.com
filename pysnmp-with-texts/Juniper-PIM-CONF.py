#
# PySNMP MIB module Juniper-PIM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PIM-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, Counter64, Gauge32, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "Counter64", "Gauge32", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPimAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29))
juniPimAgent.setRevisions(('2002-09-06 16:54', '2001-11-15 22:38',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPimAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPimAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniPimAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPimAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPimAgent.setDescription('The agent capabilities definitions for the Protocol Independent Multicast (PIM) component of the SNMP agent in the Juniper E-series family of products.')
juniPimAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPimAgentV1 = juniPimAgentV1.setProductRelease('Version 1 of the PIM component of the JUNOSe SNMP agent.  This version\n        of the PIM component is supported in JUNOSe 3.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPimAgentV1 = juniPimAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniPimAgentV1.setDescription('The MIBs supported by the SNMP agent for the PIM application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-PIM-CONF", juniPimAgentV1=juniPimAgentV1, PYSNMP_MODULE_ID=juniPimAgent, juniPimAgent=juniPimAgent)
