#
# PySNMP MIB module Unisphere-Data-PPPoE-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPPoE-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, IpAddress, Counter32, Counter64, ModuleIdentity, Bits, NotificationType, Integer32, MibIdentifier, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "IpAddress", "Counter32", "Counter64", "ModuleIdentity", "Bits", "NotificationType", "Integer32", "MibIdentifier", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdPPPoESubIfGroup2, usdPPPoEGroup4, usdPPPoEGroup2, usdPPPoEGroup3, usdPPPoESummaryGroup = mibBuilder.importSymbols("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfGroup2", "usdPPPoEGroup4", "usdPPPoEGroup2", "usdPPPoEGroup3", "usdPPPoESummaryGroup")
usdPppoeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33))
usdPppoeAgent.setRevisions(('2002-08-19 15:14', '2001-06-19 14:27', '2001-04-02 19:21',))
if mibBuilder.loadTexts: usdPppoeAgent.setLastUpdated('200208191514Z')
if mibBuilder.loadTexts: usdPppoeAgent.setOrganization('Juniper Networks, Inc.')
usdPppoeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV1 = usdPppoeAgentV1.setProductRelease('Version 1 of the PPPoE component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPPoE component was supported in the\n        Unisphere RX 3.0 thru 3.2.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV1 = usdPppoeAgentV1.setStatus('obsolete')
usdPppoeAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV2 = usdPppoeAgentV2.setProductRelease('Version 2 of the PPPoE component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPPoE component was supported in the\n        Unisphere RX 3.2.3 through 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV2 = usdPppoeAgentV2.setStatus('obsolete')
usdPppoeAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV3 = usdPppoeAgentV3.setProductRelease('Version 3 of the PPPoE component of the Unisphere Routing Switch SNMP\n        agent.  This version of the PPPoE component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppoeAgentV3 = usdPppoeAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PPPoE-CONF", PYSNMP_MODULE_ID=usdPppoeAgent, usdPppoeAgentV2=usdPppoeAgentV2, usdPppoeAgentV3=usdPppoeAgentV3, usdPppoeAgent=usdPppoeAgent, usdPppoeAgentV1=usdPppoeAgentV1)
