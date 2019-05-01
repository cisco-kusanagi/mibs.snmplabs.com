#
# PySNMP MIB module Unisphere-Data-Frame-Relay-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Frame-Relay-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
frPortGroup, frCircuitGroup = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "frPortGroup", "frCircuitGroup")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, MibIdentifier, Counter32, ModuleIdentity, NotificationType, TimeTicks, iso, Bits, Counter64, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter32", "ModuleIdentity", "NotificationType", "TimeTicks", "iso", "Bits", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdFrSubIfGroup, usdFrGroup = mibBuilder.importSymbols("Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfGroup", "usdFrGroup")
usdFrameRelayAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17))
usdFrameRelayAgent.setRevisions(('2001-04-18 19:26',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdFrameRelayAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdFrameRelayAgent.setLastUpdated('200104181926Z')
if mibBuilder.loadTexts: usdFrameRelayAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdFrameRelayAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdFrameRelayAgent.setDescription('The agent capabilities definitions for the Frame Relay component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdFrameRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFrameRelayAgentV1 = usdFrameRelayAgentV1.setProductRelease('Version 1 of the Frame Relay component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Frame Relay component is supported in\n        the Unisphere RX 1.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFrameRelayAgentV1 = usdFrameRelayAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdFrameRelayAgentV1.setDescription('The MIBs supported by the SNMP agent for the Frame Relay application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Frame-Relay-CONF", usdFrameRelayAgent=usdFrameRelayAgent, usdFrameRelayAgentV1=usdFrameRelayAgentV1, PYSNMP_MODULE_ID=usdFrameRelayAgent)
