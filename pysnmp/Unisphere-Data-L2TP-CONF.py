#
# PySNMP MIB module Unisphere-Data-L2TP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-L2TP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, IpAddress, Unsigned32, Counter64, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, ModuleIdentity, TimeTicks, ObjectIdentity, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Unsigned32", "Counter64", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdL2tpConfigGroup, usdL2tpStatusGroup2, usdL2tpMapGroup, usdL2tpConfigGroup2, usdL2tpUdpIpGroup, usdL2tpStatGroup2, usdL2tpConfigGroup3, usdL2tpStatGroup, usdL2tpStatusGroup = mibBuilder.importSymbols("Unisphere-Data-L2TP-MIB", "usdL2tpConfigGroup", "usdL2tpStatusGroup2", "usdL2tpMapGroup", "usdL2tpConfigGroup2", "usdL2tpUdpIpGroup", "usdL2tpStatGroup2", "usdL2tpConfigGroup3", "usdL2tpStatGroup", "usdL2tpStatusGroup")
usdL2tpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24))
usdL2tpAgent.setRevisions(('2001-10-17 16:03', '2001-10-17 14:21',))
if mibBuilder.loadTexts: usdL2tpAgent.setLastUpdated('200110171603Z')
if mibBuilder.loadTexts: usdL2tpAgent.setOrganization('Unisphere Networks, Inc.')
usdL2tpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV1 = usdL2tpAgentV1.setProductRelease('Version 1 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV1 = usdL2tpAgentV1.setStatus('obsolete')
usdL2tpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV2 = usdL2tpAgentV2.setProductRelease('Version 2 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component was supported in the\n        Unisphere RX 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV2 = usdL2tpAgentV2.setStatus('obsolete')
usdL2tpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV3 = usdL2tpAgentV3.setProductRelease('Version 3 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component was supported in the\n        Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV3 = usdL2tpAgentV3.setStatus('obsolete')
usdL2tpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV4 = usdL2tpAgentV4.setProductRelease('Version 4 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component is supported in the Unisphere\n        RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV4 = usdL2tpAgentV4.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-L2TP-CONF", usdL2tpAgentV2=usdL2tpAgentV2, usdL2tpAgentV3=usdL2tpAgentV3, PYSNMP_MODULE_ID=usdL2tpAgent, usdL2tpAgent=usdL2tpAgent, usdL2tpAgentV4=usdL2tpAgentV4, usdL2tpAgentV1=usdL2tpAgentV1)
