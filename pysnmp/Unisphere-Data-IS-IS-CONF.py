#
# PySNMP MIB module Unisphere-Data-IS-IS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IS-IS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, Unsigned32, NotificationType, Counter64, Gauge32, TimeTicks, Counter32, MibIdentifier, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter64", "Gauge32", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIsisSystemMgmtGroup2, usdIsisSystemMgmtGroup, usdIsisCircuitMgmtGroup2, usdIsisCircuitMgmtGroup = mibBuilder.importSymbols("Unisphere-Data-ISIS-MIB", "usdIsisSystemMgmtGroup2", "usdIsisSystemMgmtGroup", "usdIsisCircuitMgmtGroup2", "usdIsisCircuitMgmtGroup")
usdIsisAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23))
usdIsisAgent.setRevisions(('2002-04-04 20:37', '2001-04-24 19:30',))
if mibBuilder.loadTexts: usdIsisAgent.setLastUpdated('200204042037Z')
if mibBuilder.loadTexts: usdIsisAgent.setOrganization('Unisphere Networks, Inc.')
usdIsisAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV1 = usdIsisAgentV1.setProductRelease('Version 1 of the IS-IS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IS-IS component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV1 = usdIsisAgentV1.setStatus('obsolete')
usdIsisAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV2 = usdIsisAgentV2.setProductRelease('Version 2 of the IS-IS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IS-IS component was supported in the\n        Unisphere RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV2 = usdIsisAgentV2.setStatus('current')
usdIsisAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV3 = usdIsisAgentV3.setProductRelease('Version 3 of the IS-IS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IS-IS component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIsisAgentV3 = usdIsisAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IS-IS-CONF", usdIsisAgentV3=usdIsisAgentV3, usdIsisAgentV2=usdIsisAgentV2, usdIsisAgent=usdIsisAgent, PYSNMP_MODULE_ID=usdIsisAgent, usdIsisAgentV1=usdIsisAgentV1)
