#
# PySNMP MIB module Unisphere-Data-SONET-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SONET-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, ModuleIdentity, TimeTicks, Integer32, ObjectIdentity, Counter64, Gauge32, Unsigned32, Counter32, NotificationType, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "Gauge32", "Unsigned32", "Counter32", "NotificationType", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonetLineStuff2, sonetSectionStuff, sonetVTStuff2, sonetMediumTimeElapsed, sonetVTStuff, sonetMediumLineType, sonetMediumValidIntervals, sonetSectionStuff2, sonetPathStuff2, sonetFarEndPathStuff2, sonetFarEndVTStuff2, sonetFarEndLineStuff2, sonetMediumStuff2, sonetMediumStuff, sonetPathStuff, sonetLineStuff, sonetMediumLoopbackConfig, sonetMediumLineCoding = mibBuilder.importSymbols("SONET-MIB", "sonetLineStuff2", "sonetSectionStuff", "sonetVTStuff2", "sonetMediumTimeElapsed", "sonetVTStuff", "sonetMediumLineType", "sonetMediumValidIntervals", "sonetSectionStuff2", "sonetPathStuff2", "sonetFarEndPathStuff2", "sonetFarEndVTStuff2", "sonetFarEndLineStuff2", "sonetMediumStuff2", "sonetMediumStuff", "sonetPathStuff", "sonetLineStuff", "sonetMediumLoopbackConfig", "sonetMediumLineCoding")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSonetGroup, usdSonetVirtualTributaryGroup, usdSonetPathGroup = mibBuilder.importSymbols("Unisphere-Data-SONET-MIB", "usdSonetGroup", "usdSonetVirtualTributaryGroup", "usdSonetPathGroup")
usdSonetAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40))
usdSonetAgent.setRevisions(('2002-02-04 21:35', '2001-04-03 22:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSonetAgent.setRevisionsDescriptions(('Separate out the SONET VT support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdSonetAgent.setLastUpdated('200202042135Z')
if mibBuilder.loadTexts: usdSonetAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdSonetAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSonetAgent.setDescription('The agent capabilities definitions for the SONET component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdSonetAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV1 = usdSonetAgentV1.setProductRelease('Version 1 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV1 = usdSonetAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdSonetAgentV1.setDescription('The MIBs supported by the SNMP agent for the SONET application in the Unisphere Routing Switch. These capabilities became obsolete when support for the standard VT group was added.')
usdSonetAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV2 = usdSonetAgentV2.setProductRelease('Version 2 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV2 = usdSonetAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdSonetAgentV2.setDescription('The MIBs supported by the SNMP agent for the SONET application in the Unisphere Routing Switch. These capabilities became obsolete when support for the proprietary path and VT groups were added.')
usdSonetAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV3 = usdSonetAgentV3.setProductRelease('Version 3 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV3 = usdSonetAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdSonetAgentV3.setDescription('The MIBs supported by the SNMP agent for the SONET application in the Unisphere Routing Switch. These capabilities became obsolete when support for the RFC-2558 version of the SONET-MIB and far-end statistics were added.')
usdSonetAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV4 = usdSonetAgentV4.setProductRelease('Version 4 of the SONET component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SONET component was supported in the\n        Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetAgentV4 = usdSonetAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: usdSonetAgentV4.setDescription('The MIBs supported by the SNMP agent for the SONET application in the Unisphere Routing Switch. These capabilities became obsolete when Virtual Tributary (VT) support was searated out into a separate capabilities statement.')
usdSonetBasicAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5))
usdSonetBasicAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetBasicAgentV1 = usdSonetBasicAgentV1.setProductRelease('Version 1 of the basic SONET component of the Unisphere Routing Switch\n        SNMP agent.  It does not include Virtual Tributary (VT) support.  This\n        version of the basic SONET component is supported in the Unisphere RX\n        3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetBasicAgentV1 = usdSonetBasicAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdSonetBasicAgentV1.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in the Unisphere Routing Switch.')
usdSonetVTAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6))
usdSonetVTAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetVTAgentV1 = usdSonetVTAgentV1.setProductRelease('Version 1 of the SONET VT component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SONET component is supported in the\n        Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetVTAgentV1 = usdSonetVTAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdSonetVTAgentV1.setDescription('The MIB conformance groups supported by the SNMP agent for the SONET application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-SONET-CONF", usdSonetVTAgentV1=usdSonetVTAgentV1, usdSonetAgentV3=usdSonetAgentV3, usdSonetAgentV4=usdSonetAgentV4, usdSonetAgentV1=usdSonetAgentV1, usdSonetVTAgent=usdSonetVTAgent, usdSonetBasicAgent=usdSonetBasicAgent, usdSonetAgentV2=usdSonetAgentV2, usdSonetAgent=usdSonetAgent, PYSNMP_MODULE_ID=usdSonetAgent, usdSonetBasicAgentV1=usdSonetBasicAgentV1)
