#
# PySNMP MIB module Juniper-Bridged-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridged-Ethernet-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, Bits, NotificationType, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Integer32, ModuleIdentity, Counter64, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "NotificationType", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter64", "IpAddress", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniBridgedEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5))
juniBridgedEthernetAgent.setRevisions(('2002-09-06 16:54', '2001-03-30 16:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniBridgedEthernetAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniBridgedEthernetAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniBridgedEthernetAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniBridgedEthernetAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniBridgedEthernetAgent.setDescription('The agent capabilities definitions for the Bridged Ethernet component of the SNMP agent in the Juniper E-series family of products.')
juniBridgedEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetAgentV1 = juniBridgedEthernetAgentV1.setProductRelease('Version 1 of the Bridged Ethernet component of the JUNOSe SNMP agent.\n        This version of the Bridged Ethernet component is supported in JUNOSe\n        2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgedEthernetAgentV1 = juniBridgedEthernetAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniBridgedEthernetAgentV1.setDescription('The MIB supported by the SNMP agent for the Bridged Ethernet application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Bridged-Ethernet-CONF", juniBridgedEthernetAgentV1=juniBridgedEthernetAgentV1, juniBridgedEthernetAgent=juniBridgedEthernetAgent, PYSNMP_MODULE_ID=juniBridgedEthernetAgent)
