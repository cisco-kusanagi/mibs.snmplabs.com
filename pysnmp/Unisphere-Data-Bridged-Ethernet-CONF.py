#
# PySNMP MIB module Unisphere-Data-Bridged-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Bridged-Ethernet-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, ModuleIdentity, Counter32, ObjectIdentity, IpAddress, Gauge32, Counter64, MibIdentifier, TimeTicks, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdBridgedEthernetGroup2, = mibBuilder.importSymbols("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetGroup2")
usdBridgedEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5))
usdBridgedEthernetAgent.setRevisions(('2001-03-30 16:45',))
if mibBuilder.loadTexts: usdBridgedEthernetAgent.setLastUpdated('200103301645Z')
if mibBuilder.loadTexts: usdBridgedEthernetAgent.setOrganization('Unisphere Networks, Inc.')
usdBridgedEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdBridgedEthernetAgentV1 = usdBridgedEthernetAgentV1.setProductRelease('Version 1 of the Bridged Ethernet component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Bridged Ethernet component is\n        supported in the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdBridgedEthernetAgentV1 = usdBridgedEthernetAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Bridged-Ethernet-CONF", usdBridgedEthernetAgentV1=usdBridgedEthernetAgentV1, usdBridgedEthernetAgent=usdBridgedEthernetAgent, PYSNMP_MODULE_ID=usdBridgedEthernetAgent)
