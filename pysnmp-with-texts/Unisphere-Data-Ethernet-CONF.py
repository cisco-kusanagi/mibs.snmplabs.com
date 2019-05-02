#
# PySNMP MIB module Unisphere-Data-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Ethernet-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
etherStatsGroup, etherStats100MbsGroup = mibBuilder.importSymbols("EtherLike-MIB", "etherStatsGroup", "etherStats100MbsGroup")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, Integer32, Counter32, TimeTicks, Gauge32, iso, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "Integer32", "Counter32", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdVlanSubIfGroup2, usdEthernetSubIfGroup, usdVlanSubIfGroup, usdVlanGroup, usdEthernetGroup = mibBuilder.importSymbols("Unisphere-Data-ETHERNET-MIB", "usdVlanSubIfGroup2", "usdEthernetSubIfGroup", "usdVlanSubIfGroup", "usdVlanGroup", "usdEthernetGroup")
usdEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14))
usdEthernetAgent.setRevisions(('2002-04-05 20:33', '2001-10-25 21:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdEthernetAgent.setRevisionsDescriptions(('Added VLAN stack support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdEthernetAgent.setLastUpdated('200204052033Z')
if mibBuilder.loadTexts: usdEthernetAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdEthernetAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdEthernetAgent.setDescription('The agent capabilities definitions for the Ethernet component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV1 = usdEthernetAgentV1.setProductRelease('Version 1 of the Ethernet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ethernet component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV1 = usdEthernetAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdEthernetAgentV1.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in the Unisphere Routing Switch. These capabilities became obsolete when VLAN support was add.')
usdEthernetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV2 = usdEthernetAgentV2.setProductRelease('Version 2 of the Ethernet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ethernet component was supported in the\n        Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV2 = usdEthernetAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdEthernetAgentV2.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in the Unisphere Routing Switch. These capabilities became obsolete when VLAN stack support was added.')
usdEthernetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV3 = usdEthernetAgentV3.setProductRelease('Version 3 of the Ethernet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ethernet component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV3 = usdEthernetAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdEthernetAgentV3.setDescription('The MIBs supported by the SNMP agent for the Ethernet application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Ethernet-CONF", usdEthernetAgentV3=usdEthernetAgentV3, usdEthernetAgentV1=usdEthernetAgentV1, usdEthernetAgent=usdEthernetAgent, usdEthernetAgentV2=usdEthernetAgentV2, PYSNMP_MODULE_ID=usdEthernetAgent)
