#
# PySNMP MIB module Unisphere-Data-SMDS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SMDS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, Counter64, Integer32, Bits, MibIdentifier, TimeTicks, NotificationType, iso, ObjectIdentity, IpAddress, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Integer32", "Bits", "MibIdentifier", "TimeTicks", "NotificationType", "iso", "ObjectIdentity", "IpAddress", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSmdsGroup, usdSmdsGroup2 = mibBuilder.importSymbols("Unisphere-Data-SMDS-MIB", "usdSmdsGroup", "usdSmdsGroup2")
usdSmdsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46))
usdSmdsAgent.setRevisions(('2001-09-20 14:57', '2001-03-30 14:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSmdsAgent.setRevisionsDescriptions(('Added support for major and sub interfaces.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdSmdsAgent.setLastUpdated('200109201457Z')
if mibBuilder.loadTexts: usdSmdsAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdSmdsAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSmdsAgent.setDescription('The agent capabilities definitions for the Switched Multimegabit Data Service (SMDS) management component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdSmdsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV1 = usdSmdsAgentV1.setProductRelease('Version 1 of the Switched Multimegabit Data Service (SMDS) management\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the SMDS component was supported in the Unisphere RX 3.1 thru 3.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV1 = usdSmdsAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdSmdsAgentV1.setDescription('The MIB supported by the SNMP agent for the SMDS application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for major and sub interfaces')
usdSmdsAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 46, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV2 = usdSmdsAgentV2.setProductRelease('Version 2 of the Switched Multimegabit Data Service (SMDS) management\n        component of the Unisphere Routing Switch SNMP agent.  This version of\n        the SMDS component is supported in the Unisphere RX 4.0 and subsequent\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSmdsAgentV2 = usdSmdsAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdSmdsAgentV2.setDescription('The MIB supported by the SNMP agent for the SMDS application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-SMDS-CONF", usdSmdsAgentV1=usdSmdsAgentV1, usdSmdsAgentV2=usdSmdsAgentV2, PYSNMP_MODULE_ID=usdSmdsAgent, usdSmdsAgent=usdSmdsAgent)
