#
# PySNMP MIB module Unisphere-Data-PPP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPP-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, Counter64, iso, NotificationType, Gauge32, Integer32, Bits, Unsigned32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "Counter64", "iso", "NotificationType", "Gauge32", "Integer32", "Bits", "Unsigned32", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdPppProfileGroup2, usdPppProfileGroup3, usdPppProfileGroup4, usdPppProfileGroup = mibBuilder.importSymbols("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileGroup2", "usdPppProfileGroup3", "usdPppProfileGroup4", "usdPppProfileGroup")
usdPppProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3))
usdPppProfileAgent.setRevisions(('2002-01-25 14:10', '2002-01-16 17:58', '2002-01-08 19:43', '2001-10-17 17:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPppProfileAgent.setRevisionsDescriptions(('Added the authenticator virtual router object.', 'Added the IPCP netmask option object.', 'Added support for dynamic multi-link PPP (MLPPP) interfaces.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPppProfileAgent.setLastUpdated('200201251410Z')
if mibBuilder.loadTexts: usdPppProfileAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdPppProfileAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPppProfileAgent.setDescription('The agent capabilities definitions for the PPP Profile component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdPppProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV1 = usdPppProfileAgentV1.setProductRelease('Version 1 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component was supported in\n        the Unisphere RX 3.0 through 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV1 = usdPppProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in the Unisphere Routing Switch. These capabilities became obsolete when the dynamic multilink PPP object was added.')
usdPppProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV2 = usdPppProfileAgentV2.setProductRelease('Version 2 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component was supported in\n        the Unisphere RX 3.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV2 = usdPppProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in the Unisphere Routing Switch. These capabilities became obsolete when the IPCP netmask option object was added.')
usdPppProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV3 = usdPppProfileAgentV3.setProductRelease('Version 3 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component was supported in\n        the Unisphere RX 3.4 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV3 = usdPppProfileAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in the Unisphere Routing Switch. These capabilities became obsolete when the authenticator virtual router object was added.')
usdPppProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV4 = usdPppProfileAgentV4.setProductRelease('Version 4 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV4 = usdPppProfileAgentV4.setStatus('current')
if mibBuilder.loadTexts: usdPppProfileAgentV4.setDescription('The MIB supported by the SNMP agent for the PPP Profile application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-PPP-Profile-CONF", usdPppProfileAgentV4=usdPppProfileAgentV4, usdPppProfileAgentV2=usdPppProfileAgentV2, usdPppProfileAgentV3=usdPppProfileAgentV3, usdPppProfileAgentV1=usdPppProfileAgentV1, PYSNMP_MODULE_ID=usdPppProfileAgent, usdPppProfileAgent=usdPppProfileAgent)
