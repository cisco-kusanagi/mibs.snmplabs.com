#
# PySNMP MIB module Unisphere-Data-SONET-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SONET-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter64, IpAddress, Unsigned32, ObjectIdentity, Bits, Gauge32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonetFarEndPathStuff2, sonetMediumValidIntervals, sonetLineStuff2, sonetSectionStuff, sonetPathStuff, sonetLineStuff, sonetMediumStuff2, sonetVTStuff2, sonetFarEndLineStuff2, sonetVTStuff, sonetMediumLineCoding, sonetFarEndVTStuff2, sonetMediumStuff, sonetMediumLoopbackConfig, sonetPathStuff2, sonetSectionStuff2, sonetMediumLineType, sonetMediumTimeElapsed = mibBuilder.importSymbols("SONET-MIB", "sonetFarEndPathStuff2", "sonetMediumValidIntervals", "sonetLineStuff2", "sonetSectionStuff", "sonetPathStuff", "sonetLineStuff", "sonetMediumStuff2", "sonetVTStuff2", "sonetFarEndLineStuff2", "sonetVTStuff", "sonetMediumLineCoding", "sonetFarEndVTStuff2", "sonetMediumStuff", "sonetMediumLoopbackConfig", "sonetPathStuff2", "sonetSectionStuff2", "sonetMediumLineType", "sonetMediumTimeElapsed")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSonetGroup, usdSonetPathGroup, usdSonetVirtualTributaryGroup = mibBuilder.importSymbols("Unisphere-Data-SONET-MIB", "usdSonetGroup", "usdSonetPathGroup", "usdSonetVirtualTributaryGroup")
usdSonetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40))
usdSonetAgent.setRevisions(('2002-02-04 21:35', '2001-04-03 22:35',))
if mibBuilder.loadTexts: usdSonetAgent.setLastUpdated('200202042135Z')
if mibBuilder.loadTexts: usdSonetAgent.setOrganization('Unisphere Networks, Inc.')
usdSonetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV1 = usdSonetAgentV1.setProductRelease('Version 1 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV1 = usdSonetAgentV1.setStatus('obsolete')
usdSonetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV2 = usdSonetAgentV2.setProductRelease('Version 2 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV2 = usdSonetAgentV2.setStatus('obsolete')
usdSonetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV3 = usdSonetAgentV3.setProductRelease('Version 3 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV3 = usdSonetAgentV3.setStatus('obsolete')
usdSonetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV4 = usdSonetAgentV4.setProductRelease('Version 4 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV4 = usdSonetAgentV4.setStatus('obsolete')
usdSonetBasicAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5))
usdSonetBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetBasicAgentV1 = usdSonetBasicAgentV1.setProductRelease('Version 1 of the basic SONET component of the Unisphere Routing Switch\n        SNMP agent.  It does not include Virtual Tributary (VT) support.  This\n        version of the basic SONET component is supported in the Unisphere RX\n        3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetBasicAgentV1 = usdSonetBasicAgentV1.setStatus('current')
usdSonetVTAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6))
usdSonetVTAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetVTAgentV1 = usdSonetVTAgentV1.setProductRelease('Version 1 of the SONET VT component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SONET component is supported in the\n        Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetVTAgentV1 = usdSonetVTAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SONET-CONF", PYSNMP_MODULE_ID=usdSonetAgent, usdSonetAgent=usdSonetAgent, usdSonetAgentV2=usdSonetAgentV2, usdSonetAgentV1=usdSonetAgentV1, usdSonetAgentV4=usdSonetAgentV4, usdSonetBasicAgentV1=usdSonetBasicAgentV1, usdSonetVTAgent=usdSonetVTAgent, usdSonetAgentV3=usdSonetAgentV3, usdSonetVTAgentV1=usdSonetVTAgentV1, usdSonetBasicAgent=usdSonetBasicAgent)
