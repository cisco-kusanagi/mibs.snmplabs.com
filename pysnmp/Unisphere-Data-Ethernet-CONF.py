#
# PySNMP MIB module Unisphere-Data-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Ethernet-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
etherStatsGroup, etherStats100MbsGroup = mibBuilder.importSymbols("EtherLike-MIB", "etherStatsGroup", "etherStats100MbsGroup")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, TimeTicks, iso, Gauge32, NotificationType, MibIdentifier, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, ModuleIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "iso", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdVlanGroup, usdEthernetGroup, usdVlanSubIfGroup2, usdEthernetSubIfGroup, usdVlanSubIfGroup = mibBuilder.importSymbols("Unisphere-Data-ETHERNET-MIB", "usdVlanGroup", "usdEthernetGroup", "usdVlanSubIfGroup2", "usdEthernetSubIfGroup", "usdVlanSubIfGroup")
usdEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14))
usdEthernetAgent.setRevisions(('2002-04-05 20:33', '2001-10-25 21:36',))
if mibBuilder.loadTexts: usdEthernetAgent.setLastUpdated('200204052033Z')
if mibBuilder.loadTexts: usdEthernetAgent.setOrganization('Unisphere Networks, Inc.')
usdEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV1 = usdEthernetAgentV1.setProductRelease('Version 1 of the Ethernet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ethernet component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV1 = usdEthernetAgentV1.setStatus('obsolete')
usdEthernetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV2 = usdEthernetAgentV2.setProductRelease('Version 2 of the Ethernet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ethernet component was supported in the\n        Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV2 = usdEthernetAgentV2.setStatus('obsolete')
usdEthernetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV3 = usdEthernetAgentV3.setProductRelease('Version 3 of the Ethernet component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Ethernet component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdEthernetAgentV3 = usdEthernetAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Ethernet-CONF", usdEthernetAgentV3=usdEthernetAgentV3, usdEthernetAgentV2=usdEthernetAgentV2, usdEthernetAgent=usdEthernetAgent, PYSNMP_MODULE_ID=usdEthernetAgent, usdEthernetAgentV1=usdEthernetAgentV1)
