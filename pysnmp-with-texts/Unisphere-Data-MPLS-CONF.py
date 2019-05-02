#
# PySNMP MIB module Unisphere-Data-MPLS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-MPLS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, iso, Bits, NotificationType, IpAddress, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ObjectIdentity, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "iso", "Bits", "NotificationType", "IpAddress", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdMplsMajorLayerConfGroup, usdMplsMinorLayerConfGroup, usdMplsTunnelProfileConfGroup, usdMplsLsrGlobalConfGroup, usdMplsExplicitPathConfGroup = mibBuilder.importSymbols("Unisphere-Data-MPLS-MIB", "usdMplsMajorLayerConfGroup", "usdMplsMinorLayerConfGroup", "usdMplsTunnelProfileConfGroup", "usdMplsLsrGlobalConfGroup", "usdMplsExplicitPathConfGroup")
usdMplsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51))
usdMplsAgent.setRevisions(('2001-12-05 21:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdMplsAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdMplsAgent.setLastUpdated('200112052141Z')
if mibBuilder.loadTexts: usdMplsAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdMplsAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdMplsAgent.setDescription('The agent capabilities definitions for the MultiProtocol Label Switching (MPLS) component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdMplsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdMplsAgentV1 = usdMplsAgentV1.setProductRelease('Version 1 of the MultiProtocol Label Switching (MPLS) component of the\n        Unisphere Routing Switch SNMP agent.  This version of the MPLS component\n        is supported in the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdMplsAgentV1 = usdMplsAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdMplsAgentV1.setDescription('The MIB supported by the SNMP agent for the MPLS application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-MPLS-CONF", usdMplsAgent=usdMplsAgent, PYSNMP_MODULE_ID=usdMplsAgent, usdMplsAgentV1=usdMplsAgentV1)
