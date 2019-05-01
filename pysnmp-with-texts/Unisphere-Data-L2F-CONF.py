#
# PySNMP MIB module Unisphere-Data-L2F-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-L2F-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Bits, ObjectIdentity, Integer32, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Counter64, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdL2fMapGroup, usdL2fStatGroup, usdL2fStatusGroup, usdL2fConfigGroup = mibBuilder.importSymbols("Unisphere-Data-L2F-MIB", "usdL2fMapGroup", "usdL2fStatGroup", "usdL2fStatusGroup", "usdL2fConfigGroup")
usdL2fAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 49))
usdL2fAgent.setRevisions(('2001-04-13 13:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdL2fAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdL2fAgent.setLastUpdated('200104131337Z')
if mibBuilder.loadTexts: usdL2fAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdL2fAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdL2fAgent.setDescription('The agent capabilities definitions for the layer 2 forwarding protocol (L2F) component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdL2fAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 49, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2fAgentV1 = usdL2fAgentV1.setProductRelease('Version 1 of the L2F component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2F component is supported in the Unisphere\n        RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2fAgentV1 = usdL2fAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdL2fAgentV1.setDescription('The MIB supported by the SNMP agent for the L2F application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-L2F-CONF", usdL2fAgent=usdL2fAgent, PYSNMP_MODULE_ID=usdL2fAgent, usdL2fAgentV1=usdL2fAgentV1)
