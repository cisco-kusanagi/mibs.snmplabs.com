#
# PySNMP MIB module Unisphere-Data-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, MibIdentifier, ModuleIdentity, Gauge32, Integer32, Unsigned32, iso, Counter64, ObjectIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "Unsigned32", "iso", "Counter64", "ObjectIdentity", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdProfileGroup, usdProfileIfGroup = mibBuilder.importSymbols("Unisphere-Data-PROFILE-MIB", "usdProfileGroup", "usdProfileIfGroup")
usdProfileManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1))
usdProfileManagerAgent.setRevisions(('2001-03-29 18:00',))
if mibBuilder.loadTexts: usdProfileManagerAgent.setLastUpdated('200103291800Z')
if mibBuilder.loadTexts: usdProfileManagerAgent.setOrganization('Unisphere Networks, Inc.')
usdProfileManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV1 = usdProfileManagerAgentV1.setProductRelease('Version 1 of the Profile Manager component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Profile Manager component was\n        supported in the Unisphere RX 1.1 thru 1.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV1 = usdProfileManagerAgentV1.setStatus('obsolete')
usdProfileManagerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV2 = usdProfileManagerAgentV2.setProductRelease('Version 2 of the Profile Manager component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Profile Manager component is\n        supported in the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileManagerAgentV2 = usdProfileManagerAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Profile-CONF", PYSNMP_MODULE_ID=usdProfileManagerAgent, usdProfileManagerAgent=usdProfileManagerAgent, usdProfileManagerAgentV1=usdProfileManagerAgentV1, usdProfileManagerAgentV2=usdProfileManagerAgentV2)
