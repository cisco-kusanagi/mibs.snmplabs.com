#
# PySNMP MIB module Unisphere-Data-PPPoE-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPPoE-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, Bits, ModuleIdentity, MibIdentifier, Unsigned32, Counter64, Counter32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "Bits", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter64", "Counter32", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdPppoeProfileGroup2, usdPppoeProfileGroup, usdPppoeProfileGroup3 = mibBuilder.importSymbols("Unisphere-Data-PPPOE-PROFILE-MIB", "usdPppoeProfileGroup2", "usdPppoeProfileGroup", "usdPppoeProfileGroup3")
usdPppoeProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4))
usdPppoeProfileAgent.setRevisions(('2002-08-15 20:38', '2002-05-31 18:21',))
if mibBuilder.loadTexts: usdPppoeProfileAgent.setLastUpdated('200208152038Z')
if mibBuilder.loadTexts: usdPppoeProfileAgent.setOrganization('Unisphere Networks, Inc.')
usdPppoeProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV1 = usdPppoeProfileAgentV1.setProductRelease('Version 1 of the PPPoE Profile component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPPoE Profile component was\n        supported in the Unisphere RX 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV1 = usdPppoeProfileAgentV1.setStatus('obsolete')
usdPppoeProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV2 = usdPppoeProfileAgentV2.setProductRelease('Version 2 of the PPPoE Profile component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPPoE Profile component was\n        supported in the Unisphere RX 3.2 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV2 = usdPppoeProfileAgentV2.setStatus('obsolete')
usdPppoeProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV3 = usdPppoeProfileAgentV3.setProductRelease('Version 3 of the PPPoE Profile component of the Unisphere Routing\n        Switch SNMP agent.  This version of the PPPoE Profile component is\n        supported in the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeProfileAgentV3 = usdPppoeProfileAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PPPoE-Profile-CONF", usdPppoeProfileAgentV1=usdPppoeProfileAgentV1, usdPppoeProfileAgent=usdPppoeProfileAgent, PYSNMP_MODULE_ID=usdPppoeProfileAgent, usdPppoeProfileAgentV3=usdPppoeProfileAgentV3, usdPppoeProfileAgentV2=usdPppoeProfileAgentV2)
