#
# PySNMP MIB module Unisphere-Data-OSPF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-OSPF-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ospfNbrGroup, ospfIfGroup, ospfHostGroup, ospfStubAreaGroup, ospfAreaGroup, ospfIfMetricGroup, ospfVirtNbrGroup, ospfExtLsdbGroup, ospfBasicGroup, ospfLsdbGroup, ospfAreaAggregateGroup, ospfVirtIfGroup = mibBuilder.importSymbols("OSPF-MIB", "ospfNbrGroup", "ospfIfGroup", "ospfHostGroup", "ospfStubAreaGroup", "ospfAreaGroup", "ospfIfMetricGroup", "ospfVirtNbrGroup", "ospfExtLsdbGroup", "ospfBasicGroup", "ospfLsdbGroup", "ospfAreaAggregateGroup", "ospfVirtIfGroup")
ospfPacketSrc, ospfTrapControlGroup, ospfPacketType, ospfConfigErrorType = mibBuilder.importSymbols("OSPF-TRAP-MIB", "ospfPacketSrc", "ospfTrapControlGroup", "ospfPacketType", "ospfConfigErrorType")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, TimeTicks, MibIdentifier, ModuleIdentity, Counter64, ObjectIdentity, Integer32, Bits, NotificationType, Gauge32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter64", "ObjectIdentity", "Integer32", "Bits", "NotificationType", "Gauge32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdOspfBasicGroup2, usdOspfIfGroup, usdOspfNbrGroup, usdOspfMd5VirtIntfGroup, usdOspfNetRangeGroup, usdOspfSummImportGroup, usdOspfVirtIfGroup, usdOspfBasicGroup, usdOspfAreaGroup, usdOspfMd5IntfGroup = mibBuilder.importSymbols("Unisphere-Data-OSPF-MIB", "usdOspfBasicGroup2", "usdOspfIfGroup", "usdOspfNbrGroup", "usdOspfMd5VirtIntfGroup", "usdOspfNetRangeGroup", "usdOspfSummImportGroup", "usdOspfVirtIfGroup", "usdOspfBasicGroup", "usdOspfAreaGroup", "usdOspfMd5IntfGroup")
usdOspfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28))
usdOspfAgent.setRevisions(('2001-12-06 15:12', '2001-03-29 13:34',))
if mibBuilder.loadTexts: usdOspfAgent.setLastUpdated('200112061512Z')
if mibBuilder.loadTexts: usdOspfAgent.setOrganization('Unisphere Networks, Inc.')
usdOspfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV1 = usdOspfAgentV1.setProductRelease('Version 1 of the OSPF component of the Unisphere Routing Switch SNMP\n        agent.  This version of the OSPF component was supported in the\n        Unisphere RX 2.x and 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV1 = usdOspfAgentV1.setStatus('obsolete')
usdOspfAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV2 = usdOspfAgentV2.setProductRelease('Version 2 of the OSPF component of the Unisphere Routing Switch SNMP\n        agent.  This version of the OSPF component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV2 = usdOspfAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-OSPF-CONF", usdOspfAgent=usdOspfAgent, PYSNMP_MODULE_ID=usdOspfAgent, usdOspfAgentV1=usdOspfAgentV1, usdOspfAgentV2=usdOspfAgentV2)
