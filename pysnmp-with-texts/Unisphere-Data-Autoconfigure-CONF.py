#
# PySNMP MIB module Unisphere-Data-Autoconfigure-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Autoconfigure-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Integer32, Bits, ModuleIdentity, Counter32, Gauge32, MibIdentifier, NotificationType, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Integer32", "Bits", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usdAutoConfGroup, = mibBuilder.importSymbols("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfGroup")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdAutoConfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44))
usdAutoConfAgent.setRevisions(('2001-03-27 20:08',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdAutoConfAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdAutoConfAgent.setLastUpdated('200103272008Z')
if mibBuilder.loadTexts: usdAutoConfAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdAutoConfAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdAutoConfAgent.setDescription('The agent capabilities definitions for the Auto-Configuration component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdAutoConfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 44, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfAgentV1 = usdAutoConfAgentV1.setProductRelease('Version 1 of the Auto-Configuration component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Auto-Configuration component is\n        supported in the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfAgentV1 = usdAutoConfAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfAgentV1.setDescription('The MIB supported by the SNMP agent for auto-configuration capabilities in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Autoconfigure-CONF", usdAutoConfAgent=usdAutoConfAgent, usdAutoConfAgentV1=usdAutoConfAgentV1, PYSNMP_MODULE_ID=usdAutoConfAgent)
