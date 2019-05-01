#
# PySNMP MIB module Unisphere-Data-PPPoE-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPPoE-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, NotificationType, Counter64, Gauge32, Counter32, Bits, MibIdentifier, ObjectIdentity, iso, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "NotificationType", "Counter64", "Gauge32", "Counter32", "Bits", "MibIdentifier", "ObjectIdentity", "iso", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdPppoeProfileGroup2, usdPppoeProfileGroup, usdPppoeProfileGroup3 = mibBuilder.importSymbols("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileGroup2", "usdPppoeProfileGroup", "usdPppoeProfileGroup3")
usdPppoeProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4))
usdPppoeProfileAgent.setRevisions(('2002-08-15 20:38', '2002-05-31 18:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPppoeProfileAgent.setRevisionsDescriptions(('Added PADI flag and packet trace support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPppoeProfileAgent.setLastUpdated('200208152038Z')
if mibBuilder.loadTexts: usdPppoeProfileAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdPppoeProfileAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPppoeProfileAgent.setDescription('The agent capabilities definitions for the PPPoE Profile component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdPppoeProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV1 = usdPppoeProfileAgentV1.setProductRelease('Version 1 of the PPPoE Profile component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPPoE Profile component was\n        supported in the Unisphere RX 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV1 = usdPppoeProfileAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppoeProfileAgentV1.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in the Unisphere Routing Switch. These capabilities became obsolete when the duplicate MAC address indicator and AC-NAME were added.')
usdPppoeProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV2 = usdPppoeProfileAgentV2.setProductRelease('Version 2 of the PPPoE Profile component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPPoE Profile component was\n        supported in the Unisphere RX 3.2 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV2 = usdPppoeProfileAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppoeProfileAgentV2.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for PADI flag and packet trace.')
usdPppoeProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV3 = usdPppoeProfileAgentV3.setProductRelease('Version 3 of the PPPoE Profile component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPPoE Profile component is\n        supported in the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV3 = usdPppoeProfileAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdPppoeProfileAgentV3.setDescription('The MIB supported by the SNMP agent for the PPPoE Profile application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-PPPoE-Profile-CONF", usdPppoeProfileAgentV3=usdPppoeProfileAgentV3, usdPppoeProfileAgent=usdPppoeProfileAgent, usdPppoeProfileAgentV2=usdPppoeProfileAgentV2, usdPppoeProfileAgentV1=usdPppoeProfileAgentV1, PYSNMP_MODULE_ID=usdPppoeProfileAgent)
