#
# PySNMP MIB module Unisphere-Data-SSC-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SSC-Client-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, Counter32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, MibIdentifier, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSscClientGroup3, usdSscClientGroup, usdSscClientGroup2 = mibBuilder.importSymbols("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientGroup3", "usdSscClientGroup", "usdSscClientGroup2")
usdSscClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41))
usdSscClientAgent.setRevisions(('2001-09-19 20:29', '2001-03-30 15:18',))
if mibBuilder.loadTexts: usdSscClientAgent.setLastUpdated('200109192029Z')
if mibBuilder.loadTexts: usdSscClientAgent.setOrganization('Unisphere Networks, Inc.')
usdSscClientAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV1 = usdSscClientAgentV1.setProductRelease('Version 1 of the SSC Client component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SSC Client component was supported in\n        the Unisphere RX 2.0 thru 3.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV1 = usdSscClientAgentV1.setStatus('obsolete')
usdSscClientAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV2 = usdSscClientAgentV2.setProductRelease('Version 2 of the SSC Client component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SSC Client component is supported in\n        the Unisphere RX 3.1 thru 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV2 = usdSscClientAgentV2.setStatus('obsolete')
usdSscClientAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV3 = usdSscClientAgentV3.setProductRelease('Version 3 of the SSC Client component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SSC Client component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSscClientAgentV3 = usdSscClientAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SSC-Client-CONF", usdSscClientAgentV2=usdSscClientAgentV2, PYSNMP_MODULE_ID=usdSscClientAgent, usdSscClientAgentV3=usdSscClientAgentV3, usdSscClientAgent=usdSscClientAgent, usdSscClientAgentV1=usdSscClientAgentV1)
