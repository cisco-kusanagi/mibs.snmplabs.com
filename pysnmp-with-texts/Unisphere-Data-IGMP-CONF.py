#
# PySNMP MIB module Unisphere-Data-IGMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IGMP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, IpAddress, Counter32, ModuleIdentity, TimeTicks, NotificationType, Unsigned32, Gauge32, Integer32, Counter64, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "NotificationType", "Unsigned32", "Gauge32", "Integer32", "Counter64", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIgmpProxyCacheGroup, usdIgmpProxyInterfaceGroup = mibBuilder.importSymbols("Unisphere-Data-IGMP-MIB", "usdIgmpProxyCacheGroup", "usdIgmpProxyInterfaceGroup")
usdIgmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19))
usdIgmpAgent.setRevisions(('2001-03-28 17:20',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdIgmpAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdIgmpAgent.setLastUpdated('200103281720Z')
if mibBuilder.loadTexts: usdIgmpAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdIgmpAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdIgmpAgent.setDescription('The agent capabilities definitions for the IGMP component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdIgmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpAgentV1 = usdIgmpAgentV1.setProductRelease('Version 1 of the IGMP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IGMP component is supported in the Unisphere\n        RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpAgentV1 = usdIgmpAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdIgmpAgentV1.setDescription('The MIB supported by the SNMP agent for the IGMP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-IGMP-CONF", usdIgmpAgentV1=usdIgmpAgentV1, usdIgmpAgent=usdIgmpAgent, PYSNMP_MODULE_ID=usdIgmpAgent)
