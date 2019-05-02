#
# PySNMP MIB module Unisphere-Data-OSPF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-OSPF-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ospfExtLsdbGroup, ospfVirtIfGroup, ospfVirtNbrGroup, ospfIfGroup, ospfAreaAggregateGroup, ospfBasicGroup, ospfIfMetricGroup, ospfLsdbGroup, ospfAreaGroup, ospfStubAreaGroup, ospfNbrGroup, ospfHostGroup = mibBuilder.importSymbols("OSPF-MIB", "ospfExtLsdbGroup", "ospfVirtIfGroup", "ospfVirtNbrGroup", "ospfIfGroup", "ospfAreaAggregateGroup", "ospfBasicGroup", "ospfIfMetricGroup", "ospfLsdbGroup", "ospfAreaGroup", "ospfStubAreaGroup", "ospfNbrGroup", "ospfHostGroup")
ospfConfigErrorType, ospfPacketType, ospfTrapControlGroup, ospfPacketSrc = mibBuilder.importSymbols("OSPF-TRAP-MIB", "ospfConfigErrorType", "ospfPacketType", "ospfTrapControlGroup", "ospfPacketSrc")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, TimeTicks, Unsigned32, MibIdentifier, IpAddress, Counter64, NotificationType, ObjectIdentity, iso, Bits, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Unsigned32", "MibIdentifier", "IpAddress", "Counter64", "NotificationType", "ObjectIdentity", "iso", "Bits", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdOspfBasicGroup2, usdOspfSummImportGroup, usdOspfNetRangeGroup, usdOspfIfGroup, usdOspfNbrGroup, usdOspfAreaGroup, usdOspfMd5IntfGroup, usdOspfBasicGroup, usdOspfMd5VirtIntfGroup, usdOspfVirtIfGroup = mibBuilder.importSymbols("Unisphere-Data-OSPF-MIB", "usdOspfBasicGroup2", "usdOspfSummImportGroup", "usdOspfNetRangeGroup", "usdOspfIfGroup", "usdOspfNbrGroup", "usdOspfAreaGroup", "usdOspfMd5IntfGroup", "usdOspfBasicGroup", "usdOspfMd5VirtIntfGroup", "usdOspfVirtIfGroup")
usdOspfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28))
usdOspfAgent.setRevisions(('2001-12-06 15:12', '2001-03-29 13:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdOspfAgent.setRevisionsDescriptions(('New objects were added to the Unisphere-Data-OSPF-MIB usdOspfBasicGroup2.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdOspfAgent.setLastUpdated('200112061512Z')
if mibBuilder.loadTexts: usdOspfAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdOspfAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdOspfAgent.setDescription('The agent capabilities definitions for the Open Shortest Path First (OSPF) routing protocol component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdOspfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV1 = usdOspfAgentV1.setProductRelease('Version 1 of the OSPF component of the Unisphere Routing Switch SNMP\n        agent.  This version of the OSPF component was supported in the\n        Unisphere RX 2.x and 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV1 = usdOspfAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdOspfAgentV1.setDescription('The MIBs supported by the SNMP agent for the OSPF application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added to the usdOspfBasicGroup.')
usdOspfAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV2 = usdOspfAgentV2.setProductRelease('Version 2 of the OSPF component of the Unisphere Routing Switch SNMP\n        agent.  This version of the OSPF component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdOspfAgentV2 = usdOspfAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdOspfAgentV2.setDescription('The MIBs supported by the SNMP agent for the OSPF application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-OSPF-CONF", usdOspfAgentV1=usdOspfAgentV1, PYSNMP_MODULE_ID=usdOspfAgent, usdOspfAgent=usdOspfAgent, usdOspfAgentV2=usdOspfAgentV2)
