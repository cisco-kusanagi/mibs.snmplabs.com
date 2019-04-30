#
# PySNMP MIB module Unisphere-Data-Frame-Relay-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Frame-Relay-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
frCircuitGroup, frPortGroup = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "frCircuitGroup", "frPortGroup")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Unsigned32, ModuleIdentity, NotificationType, IpAddress, Counter32, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Unsigned32", "ModuleIdentity", "NotificationType", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdFrGroup, usdFrSubIfGroup = mibBuilder.importSymbols("Unisphere-Data-FRAME-RELAY-MIB", "usdFrGroup", "usdFrSubIfGroup")
usdFrameRelayAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17))
usdFrameRelayAgent.setRevisions(('2001-04-18 19:26',))
if mibBuilder.loadTexts: usdFrameRelayAgent.setLastUpdated('200104181926Z')
if mibBuilder.loadTexts: usdFrameRelayAgent.setOrganization('Unisphere Networks, Inc.')
usdFrameRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFrameRelayAgentV1 = usdFrameRelayAgentV1.setProductRelease('Version 1 of the Frame Relay component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Frame Relay component is supported in\n        the Unisphere RX 1.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFrameRelayAgentV1 = usdFrameRelayAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Frame-Relay-CONF", usdFrameRelayAgentV1=usdFrameRelayAgentV1, usdFrameRelayAgent=usdFrameRelayAgent, PYSNMP_MODULE_ID=usdFrameRelayAgent)
