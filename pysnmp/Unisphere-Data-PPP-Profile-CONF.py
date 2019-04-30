#
# PySNMP MIB module Unisphere-Data-PPP-Profile-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PPP-Profile-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, Counter64, Unsigned32, iso, NotificationType, Bits, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Unsigned32", "iso", "NotificationType", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdProfileAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdProfileAgents")
usdPppProfileGroup2, usdPppProfileGroup4, usdPppProfileGroup3, usdPppProfileGroup = mibBuilder.importSymbols("Unisphere-Data-PPP-PROFILE-MIB", "usdPppProfileGroup2", "usdPppProfileGroup4", "usdPppProfileGroup3", "usdPppProfileGroup")
usdPppProfileAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3))
usdPppProfileAgent.setRevisions(('2002-01-25 14:10', '2002-01-16 17:58', '2002-01-08 19:43', '2001-10-17 17:10',))
if mibBuilder.loadTexts: usdPppProfileAgent.setLastUpdated('200201251410Z')
if mibBuilder.loadTexts: usdPppProfileAgent.setOrganization('Unisphere Networks, Inc.')
usdPppProfileAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV1 = usdPppProfileAgentV1.setProductRelease('Version 1 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component was supported in\n        the Unisphere RX 3.0 through 3.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV1 = usdPppProfileAgentV1.setStatus('obsolete')
usdPppProfileAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV2 = usdPppProfileAgentV2.setProductRelease('Version 2 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component was supported in\n        the Unisphere RX 3.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV2 = usdPppProfileAgentV2.setStatus('obsolete')
usdPppProfileAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV3 = usdPppProfileAgentV3.setProductRelease('Version 3 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component was supported in\n        the Unisphere RX 3.4 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV3 = usdPppProfileAgentV3.setStatus('obsolete')
usdPppProfileAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV4 = usdPppProfileAgentV4.setProductRelease('Version 4 of the PPP Profile component of the Unisphere Routing Switch\n        SNMP agent.  This version of the PPP Profile component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdPppProfileAgentV4 = usdPppProfileAgentV4.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PPP-Profile-CONF", usdPppProfileAgentV3=usdPppProfileAgentV3, usdPppProfileAgent=usdPppProfileAgent, usdPppProfileAgentV1=usdPppProfileAgentV1, usdPppProfileAgentV4=usdPppProfileAgentV4, usdPppProfileAgentV2=usdPppProfileAgentV2, PYSNMP_MODULE_ID=usdPppProfileAgent)
