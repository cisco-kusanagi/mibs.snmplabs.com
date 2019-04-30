#
# PySNMP MIB module Unisphere-Data-PIM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PIM-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
pimV2MIBGroup, pimNextHopGroup, pimV2CandidateRPMIBGroup, pimAssertGroup, pimV1MIBGroup, pimDenseV2MIBGroup = mibBuilder.importSymbols("PIM-MIB", "pimV2MIBGroup", "pimNextHopGroup", "pimV2CandidateRPMIBGroup", "pimAssertGroup", "pimV1MIBGroup", "pimDenseV2MIBGroup")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, Counter32, TimeTicks, iso, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "TimeTicks", "iso", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Unsigned32", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPimInterfaceGroup, usdPimUnicastRouteGroup, usdPimMRouteNextHopGroup, usdPimAutoRPCandGroup, usdPimAutoRPConfGroup, usdPimStaticRPConfGroup, usdPimRPSetGroup, usdPimGeneralGroup, usdPimSPTThresholdGroup, usdPimComponentGroup, usdPimMRouteConfGroup = mibBuilder.importSymbols("Unisphere-Data-PIM-MIB", "usdPimInterfaceGroup", "usdPimUnicastRouteGroup", "usdPimMRouteNextHopGroup", "usdPimAutoRPCandGroup", "usdPimAutoRPConfGroup", "usdPimStaticRPConfGroup", "usdPimRPSetGroup", "usdPimGeneralGroup", "usdPimSPTThresholdGroup", "usdPimComponentGroup", "usdPimMRouteConfGroup")
usdPimAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29))
usdPimAgent.setRevisions(('2001-11-15 22:38',))
if mibBuilder.loadTexts: usdPimAgent.setLastUpdated('200111152238Z')
if mibBuilder.loadTexts: usdPimAgent.setOrganization('Unisphere Networks, Inc.')
usdPimAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 29, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPimAgentV1 = usdPimAgentV1.setProductRelease('Version 1 of the PIM component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PIM component is supported in the Unisphere\n        RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPimAgentV1 = usdPimAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PIM-CONF", usdPimAgent=usdPimAgent, PYSNMP_MODULE_ID=usdPimAgent, usdPimAgentV1=usdPimAgentV1)
