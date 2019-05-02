#
# PySNMP MIB module Unisphere-Data-SSC-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SSC-Client-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:33:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter32, Integer32, NotificationType, Gauge32, TimeTicks, Unsigned32, MibIdentifier, Bits, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter32", "Integer32", "NotificationType", "Gauge32", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSscClientGroup3, usdSscClientGroup2, usdSscClientGroup = mibBuilder.importSymbols("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientGroup3", "usdSscClientGroup2", "usdSscClientGroup")
usdSscClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41))
usdSscClientAgent.setRevisions(('2001-09-19 20:29', '2001-03-30 15:18',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSscClientAgent.setRevisionsDescriptions(('Add version number object.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdSscClientAgent.setLastUpdated('200109192029Z')
if mibBuilder.loadTexts: usdSscClientAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdSscClientAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSscClientAgent.setDescription('The agent capabilities definitions for the Service Selection Center (SSC) Client component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdSscClientAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV1 = usdSscClientAgentV1.setProductRelease('Version 1 of the SSC Client component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SSC Client component was supported in\n        the Unisphere RX 2.0 thru 3.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV1 = usdSscClientAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdSscClientAgentV1.setDescription('The MIB supported by the SNMP agent for the SSC Client application in the Unisphere Routing Switch. These capabilities became obsolete when DHCP-LS, Web and SSC support objects were added to the MIB.')
usdSscClientAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV2 = usdSscClientAgentV2.setProductRelease('Version 2 of the SSC Client component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SSC Client component is supported in\n        the Unisphere RX 3.1 thru 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV2 = usdSscClientAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdSscClientAgentV2.setDescription('The MIB supported by the SNMP agent for the SSC Client application in the Unisphere Routing Switch. These capabilities became obsolete when the version number object was added to the MIB.')
usdSscClientAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV3 = usdSscClientAgentV3.setProductRelease('Version 3 of the SSC Client component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SSC Client component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV3 = usdSscClientAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdSscClientAgentV3.setDescription('The MIB supported by the SNMP agent for the SSC Client application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-SSC-Client-CONF", usdSscClientAgentV1=usdSscClientAgentV1, usdSscClientAgent=usdSscClientAgent, usdSscClientAgentV3=usdSscClientAgentV3, usdSscClientAgentV2=usdSscClientAgentV2, PYSNMP_MODULE_ID=usdSscClientAgent)
