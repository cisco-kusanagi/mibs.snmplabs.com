#
# PySNMP MIB module Unisphere-Data-VRRP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-VRRP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:33:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Counter64, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, iso, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter64", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "iso", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
vrrpNotificationGroup, vrrpOperGroup, vrrpStatsGroup, vrrpTrapGroup = mibBuilder.importSymbols("VRRP-MIB", "vrrpNotificationGroup", "vrrpOperGroup", "vrrpStatsGroup", "vrrpTrapGroup")
usdVrrpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53))
usdVrrpAgent.setRevisions(('2002-01-24 15:20',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdVrrpAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdVrrpAgent.setLastUpdated('200201241520Z')
if mibBuilder.loadTexts: usdVrrpAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdVrrpAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdVrrpAgent.setDescription('The agent capabilities definitions for the Virtual Router Redundancy Protocol (VRRP) component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdVrrpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVrrpAgentV1 = usdVrrpAgentV1.setProductRelease('Version 1 of the VRRP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the VRRP component is supported in the Unisphere\n        RX 3.4 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVrrpAgentV1 = usdVrrpAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdVrrpAgentV1.setDescription('The MIB supported by the SNMP agent for the VRRP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-VRRP-CONF", usdVrrpAgentV1=usdVrrpAgentV1, usdVrrpAgent=usdVrrpAgent, PYSNMP_MODULE_ID=usdVrrpAgent)
