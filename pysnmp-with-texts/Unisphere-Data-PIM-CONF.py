#
# PySNMP MIB module Unisphere-Data-PIM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PIM-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
pimNextHopGroup, pimAssertGroup, pimDenseV2MIBGroup, pimV2MIBGroup, pimV2CandidateRPMIBGroup, pimV1MIBGroup = mibBuilder.importSymbols("PIM-MIB", "pimNextHopGroup", "pimAssertGroup", "pimDenseV2MIBGroup", "pimV2MIBGroup", "pimV2CandidateRPMIBGroup", "pimV1MIBGroup")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, ObjectIdentity, iso, Bits, Counter64, ModuleIdentity, MibIdentifier, Counter32, Unsigned32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "iso", "Bits", "Counter64", "ModuleIdentity", "MibIdentifier", "Counter32", "Unsigned32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPimInterfaceGroup, usdPimUnicastRouteGroup, usdPimStaticRPConfGroup, usdPimGeneralGroup, usdPimSPTThresholdGroup, usdPimMRouteNextHopGroup, usdPimAutoRPConfGroup, usdPimAutoRPCandGroup, usdPimMRouteConfGroup, usdPimComponentGroup, usdPimRPSetGroup = mibBuilder.importSymbols("Unisphere-Data-PIM-MIB", "usdPimInterfaceGroup", "usdPimUnicastRouteGroup", "usdPimStaticRPConfGroup", "usdPimGeneralGroup", "usdPimSPTThresholdGroup", "usdPimMRouteNextHopGroup", "usdPimAutoRPConfGroup", "usdPimAutoRPCandGroup", "usdPimMRouteConfGroup", "usdPimComponentGroup", "usdPimRPSetGroup")
usdPimAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29))
usdPimAgent.setRevisions(('2001-11-15 22:38',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPimAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPimAgent.setLastUpdated('200111152238Z')
if mibBuilder.loadTexts: usdPimAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdPimAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPimAgent.setDescription('The agent capabilities definitions for the Protocol Independent Multicast (PIM) component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdPimAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPimAgentV1 = usdPimAgentV1.setProductRelease('Version 1 of the PIM component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PIM component is supported in the Unisphere\n        RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPimAgentV1 = usdPimAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPimAgentV1.setDescription('The MIBs supported by the SNMP agent for the PIM application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-PIM-CONF", usdPimAgentV1=usdPimAgentV1, usdPimAgent=usdPimAgent, PYSNMP_MODULE_ID=usdPimAgent)
