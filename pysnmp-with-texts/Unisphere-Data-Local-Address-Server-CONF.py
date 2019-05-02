#
# PySNMP MIB module Unisphere-Data-Local-Address-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Local-Address-Server-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, IpAddress, Counter32, Counter64, ObjectIdentity, TimeTicks, Bits, iso, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter32", "Counter64", "ObjectIdentity", "TimeTicks", "Bits", "iso", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdAddressPoolGroup2, usdAddressPoolGroup3, usdAddressPoolTrapGroup, usdAddressPoolGroup = mibBuilder.importSymbols("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolGroup2", "usdAddressPoolGroup3", "usdAddressPoolTrapGroup", "usdAddressPoolGroup")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdLocalAddressServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25))
usdLocalAddressServerAgent.setRevisions(('2002-05-06 19:20', '2001-05-02 13:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdLocalAddressServerAgent.setRevisionsDescriptions(('Added support for address pools with multiple address ranges.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdLocalAddressServerAgent.setLastUpdated('200205061920Z')
if mibBuilder.loadTexts: usdLocalAddressServerAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdLocalAddressServerAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdLocalAddressServerAgent.setDescription('The agent capabilities definitions for the Local Address Server component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdLocalAddressServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV1 = usdLocalAddressServerAgentV1.setProductRelease('Version 1 of the Local Address Server component of the Unisphere\n        Routing Switch SNMP agent.  This version of the Local Address Server\n        component was supported in the Unisphere RX 1.3 thru RX 3.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV1 = usdLocalAddressServerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdLocalAddressServerAgentV1.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in the Unisphere Data Routing Switch. These capabilities became obsolete when pool exhaustion variables and notifications were added.')
usdLocalAddressServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV2 = usdLocalAddressServerAgentV2.setProductRelease('Version 2 of the Local Address Server component of the Unisphere\n        Routing Switch SNMP agent.  This version of the Local Address Server\n        component was supported in the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV2 = usdLocalAddressServerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdLocalAddressServerAgentV2.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in the Unisphere Data Routing Switch. These capabilities became obsolete when support was added for address pools with multiple address ranges.')
usdLocalAddressServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV3 = usdLocalAddressServerAgentV3.setProductRelease('Version 3 of the Local Address Server component of the Unisphere\n        Routing Switch SNMP agent.  This version of the Local Address Server\n        component is supported in the Unisphere RX 3.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV3 = usdLocalAddressServerAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdLocalAddressServerAgentV3.setDescription('The MIB supported by the SNMP agent for the Local Address Server application in the Unisphere Data Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Local-Address-Server-CONF", usdLocalAddressServerAgentV2=usdLocalAddressServerAgentV2, usdLocalAddressServerAgentV1=usdLocalAddressServerAgentV1, PYSNMP_MODULE_ID=usdLocalAddressServerAgent, usdLocalAddressServerAgent=usdLocalAddressServerAgent, usdLocalAddressServerAgentV3=usdLocalAddressServerAgentV3)
