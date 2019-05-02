#
# PySNMP MIB module Unisphere-Data-PPPoE-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPPoE-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, Counter32, TimeTicks, Bits, Gauge32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "Bits", "Gauge32", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPPPoESummaryGroup, usdPPPoEGroup4, usdPPPoESubIfGroup2, usdPPPoEGroup2, usdPPPoEGroup3 = mibBuilder.importSymbols("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryGroup", "usdPPPoEGroup4", "usdPPPoESubIfGroup2", "usdPPPoEGroup2", "usdPPPoEGroup3")
usdPppoeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33))
usdPppoeAgent.setRevisions(('2002-08-19 15:14', '2001-06-19 14:27', '2001-04-02 19:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdPppoeAgent.setRevisionsDescriptions(('Added PADI flag support.', 'Added AC-NAME and duplicate MAC address indicator objects.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdPppoeAgent.setLastUpdated('200208191514Z')
if mibBuilder.loadTexts: usdPppoeAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: usdPppoeAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdPppoeAgent.setDescription('The agent capabilities definitions for the point-to-point protocol over Ethernet (PPPoE) component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdPppoeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV1 = usdPppoeAgentV1.setProductRelease('Version 1 of the PPPoE component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPPoE component was supported in the\n        Unisphere RX 3.0 thru 3.2.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV1 = usdPppoeAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppoeAgentV1.setDescription('The MIB supported by the SNMP agent for the PPPoE application in the Unisphere Routing Switch. These capabilities became obsolete when AC-NAME and duplicate MAC address indicator objects were added.')
usdPppoeAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV2 = usdPppoeAgentV2.setProductRelease('Version 2 of the PPPoE component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPPoE component was supported in the\n        Unisphere RX 3.2.3 through 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV2 = usdPppoeAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdPppoeAgentV2.setDescription('The MIB supported by the SNMP agent for the PPPoE application in the Unisphere Routing Switch. These capabilities became obsolete when PADI flag support was added.')
usdPppoeAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV3 = usdPppoeAgentV3.setProductRelease('Version 3 of the PPPoE component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPPoE component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV3 = usdPppoeAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdPppoeAgentV3.setDescription('The MIB supported by the SNMP agent for the PPPoE application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-PPPoE-CONF", PYSNMP_MODULE_ID=usdPppoeAgent, usdPppoeAgentV3=usdPppoeAgentV3, usdPppoeAgentV2=usdPppoeAgentV2, usdPppoeAgent=usdPppoeAgent, usdPppoeAgentV1=usdPppoeAgentV1)
