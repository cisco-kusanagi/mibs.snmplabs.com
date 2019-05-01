#
# PySNMP MIB module Unisphere-Data-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Profile-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Unsigned32, Gauge32, Bits, Counter64, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Unsigned32", "Gauge32", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdProfileIfGroup, usdProfileGroup = mibBuilder.importSymbols("Unisphere-Data-PROFILE-MIB", "usdProfileIfGroup", "usdProfileGroup")
usdProfileManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1))
usdProfileManagerAgent.setRevisions(('2001-03-29 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdProfileManagerAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdProfileManagerAgent.setLastUpdated('200103291800Z')
if mibBuilder.loadTexts: usdProfileManagerAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdProfileManagerAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdProfileManagerAgent.setDescription('The agent capabilities definitions for the Profile Manager component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdProfileManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV1 = usdProfileManagerAgentV1.setProductRelease('Version 1 of the Profile Manager component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Profile Manager component was\n        supported in the Unisphere RX 1.1 thru 1.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV1 = usdProfileManagerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdProfileManagerAgentV1.setDescription('The MIBs supported by the SNMP agent for the Profile Manager application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for assignment of profiles to interface/ encapsulation pairs.')
usdProfileManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV2 = usdProfileManagerAgentV2.setProductRelease('Version 2 of the Profile Manager component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Profile Manager component is\n        supported in the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV2 = usdProfileManagerAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdProfileManagerAgentV2.setDescription('The MIB supported by the SNMP agent for the Profile Manager application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Profile-CONF", usdProfileManagerAgentV2=usdProfileManagerAgentV2, usdProfileManagerAgent=usdProfileManagerAgent, PYSNMP_MODULE_ID=usdProfileManagerAgent, usdProfileManagerAgentV1=usdProfileManagerAgentV1)
