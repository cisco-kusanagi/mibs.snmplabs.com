#
# PySNMP MIB module Unisphere-Data-Bridged-Ethernet-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Bridged-Ethernet-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, TimeTicks, IpAddress, ModuleIdentity, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Bits, ObjectIdentity, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "IpAddress", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Bits", "ObjectIdentity", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdBridgedEthernetGroup2, = mibBuilder.importSymbols("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetGroup2")
usdBridgedEthernetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5))
usdBridgedEthernetAgent.setRevisions(('2001-03-30 16:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdBridgedEthernetAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdBridgedEthernetAgent.setLastUpdated('200103301645Z')
if mibBuilder.loadTexts: usdBridgedEthernetAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdBridgedEthernetAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdBridgedEthernetAgent.setDescription('The agent capabilities definitions for the Bridged Ethernet component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdBridgedEthernetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdBridgedEthernetAgentV1 = usdBridgedEthernetAgentV1.setProductRelease('Version 1 of the Bridged Ethernet component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Bridged Ethernet component is\n        supported in the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdBridgedEthernetAgentV1 = usdBridgedEthernetAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdBridgedEthernetAgentV1.setDescription('The MIB supported by the SNMP agent for the Bridged Ethernet application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Bridged-Ethernet-CONF", PYSNMP_MODULE_ID=usdBridgedEthernetAgent, usdBridgedEthernetAgentV1=usdBridgedEthernetAgentV1, usdBridgedEthernetAgent=usdBridgedEthernetAgent)
