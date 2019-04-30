#
# PySNMP MIB module Unisphere-Data-MPLS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-MPLS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks, Counter32, Integer32, Bits, Counter64, NotificationType, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter32", "Integer32", "Bits", "Counter64", "NotificationType", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdMplsMinorLayerConfGroup, usdMplsExplicitPathConfGroup, usdMplsTunnelProfileConfGroup, usdMplsLsrGlobalConfGroup, usdMplsMajorLayerConfGroup = mibBuilder.importSymbols("Unisphere-Data-MPLS-MIB", "usdMplsMinorLayerConfGroup", "usdMplsExplicitPathConfGroup", "usdMplsTunnelProfileConfGroup", "usdMplsLsrGlobalConfGroup", "usdMplsMajorLayerConfGroup")
usdMplsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51))
usdMplsAgent.setRevisions(('2001-12-05 21:41',))
if mibBuilder.loadTexts: usdMplsAgent.setLastUpdated('200112052141Z')
if mibBuilder.loadTexts: usdMplsAgent.setOrganization('Unisphere Networks, Inc.')
usdMplsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdMplsAgentV1 = usdMplsAgentV1.setProductRelease('Version 1 of the MultiProtocol Label Switching (MPLS) component of the\n        Unisphere Routing Switch SNMP agent.  This version of the MPLS component\n        is supported in the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdMplsAgentV1 = usdMplsAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-MPLS-CONF", usdMplsAgentV1=usdMplsAgentV1, PYSNMP_MODULE_ID=usdMplsAgent, usdMplsAgent=usdMplsAgent)
