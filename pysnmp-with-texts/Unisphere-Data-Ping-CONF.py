#
# PySNMP MIB module Unisphere-Data-Ping-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Ping-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pingGroup, pingTimeStampGroup, pingNotificationsGroup = mibBuilder.importSymbols("DISMAN-PING-MIB", "pingGroup", "pingTimeStampGroup", "pingNotificationsGroup")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, NotificationType, IpAddress, Bits, Unsigned32, Counter64, MibIdentifier, ModuleIdentity, iso, Integer32, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "NotificationType", "IpAddress", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "iso", "Integer32", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPingAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30))
usdPingAgent.setRevisions(('2001-03-29 14:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPingAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPingAgent.setLastUpdated('200103291414Z')
if mibBuilder.loadTexts: usdPingAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdPingAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPingAgent.setDescription('The agent capabilities definitions for the Ping component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdPingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPingAgentV1 = usdPingAgentV1.setProductRelease('Version 1 of the Ping component of the Unisphere Routing Switch SNMP\n        agent.  This version of the Ping component is supported in the\n        Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPingAgentV1 = usdPingAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdPingAgentV1.setDescription('The MIB supported by the SNMP agent for the Ping application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Ping-CONF", usdPingAgent=usdPingAgent, usdPingAgentV1=usdPingAgentV1, PYSNMP_MODULE_ID=usdPingAgent)
