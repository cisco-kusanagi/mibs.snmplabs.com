#
# PySNMP MIB module Unisphere-Data-AAA-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-AAA-Server-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, Bits, IpAddress, Integer32, ObjectIdentity, Counter64, Unsigned32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "IpAddress", "Integer32", "ObjectIdentity", "Counter64", "Unsigned32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdAaaGroup, usdAaaBrasGroup4, usdAaaSubscriberGroup3, usdAaaGroup2, usdAaaTunnelGroup, usdAaaAddressGroup, usdAaaSubscriberGroup2, usdAaaSubscriberGroup, usdAaaAccountingGroup2, usdAaaAuthenticationGroup, usdAaaBrasGroup, usdAaaBasicGroup, usdAaaCapabilitiesGroup, usdAaaBrasGroup3, usdAaaBrasGroup2, usdAaaAccountingGroup = mibBuilder.importSymbols("Unisphere-Data-AAA-MIB", "usdAaaGroup", "usdAaaBrasGroup4", "usdAaaSubscriberGroup3", "usdAaaGroup2", "usdAaaTunnelGroup", "usdAaaAddressGroup", "usdAaaSubscriberGroup2", "usdAaaSubscriberGroup", "usdAaaAccountingGroup2", "usdAaaAuthenticationGroup", "usdAaaBrasGroup", "usdAaaBasicGroup", "usdAaaCapabilitiesGroup", "usdAaaBrasGroup3", "usdAaaBrasGroup2", "usdAaaAccountingGroup")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdAaaServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1))
usdAaaServerAgent.setRevisions(('2002-05-13 19:32', '2002-01-03 20:30', '2001-09-18 21:13', '2001-04-10 14:02',))
if mibBuilder.loadTexts: usdAaaServerAgent.setLastUpdated('200205131932Z')
if mibBuilder.loadTexts: usdAaaServerAgent.setOrganization('Unisphere Networks, Inc.')
usdAaaServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV1 = usdAaaServerAgentV1.setProductRelease('Version 1 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV1 = usdAaaServerAgentV1.setStatus('obsolete')
usdAaaServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV2 = usdAaaServerAgentV2.setProductRelease('Version 2 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV2 = usdAaaServerAgentV2.setStatus('obsolete')
usdAaaServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV3 = usdAaaServerAgentV3.setProductRelease('Version 3 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 3.0 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV3 = usdAaaServerAgentV3.setStatus('obsolete')
usdAaaServerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV4 = usdAaaServerAgentV4.setProductRelease('Version 4 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 3.1 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV4 = usdAaaServerAgentV4.setStatus('obsolete')
usdAaaServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV5 = usdAaaServerAgentV5.setProductRelease('Version 5 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 3.2 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV5 = usdAaaServerAgentV5.setStatus('obsolete')
usdAaaServerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6))
if mibBuilder.loadTexts: usdAaaServerBaseAgent.setStatus('current')
usdAaaServerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBaseAgentV1 = usdAaaServerBaseAgentV1.setProductRelease('Version 1 of the basic AAA Server component of the Unisphere Routing\n        Switch SNMP agent.  This version is supported in the Unisphere RX 3.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBaseAgentV1 = usdAaaServerBaseAgentV1.setStatus('current')
usdAaaServerBrasAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7))
if mibBuilder.loadTexts: usdAaaServerBrasAgent.setStatus('current')
usdAaaServerBrasAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV1 = usdAaaServerBrasAgentV1.setProductRelease('Version 1 of the B-RAS option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version was supported in the\n        Unisphere RX 3.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV1 = usdAaaServerBrasAgentV1.setStatus('obsolete')
usdAaaServerBrasAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV2 = usdAaaServerBrasAgentV2.setProductRelease('Version 2 of the B-RAS option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version was supported in the\n        Unisphere RX 3.4 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV2 = usdAaaServerBrasAgentV2.setStatus('obsolete')
usdAaaServerBrasAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV3 = usdAaaServerBrasAgentV3.setProductRelease('Version 3 of the B-RAS option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV3 = usdAaaServerBrasAgentV3.setStatus('current')
usdAaaServerTunnelAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8))
if mibBuilder.loadTexts: usdAaaServerTunnelAgent.setStatus('current')
usdAaaServerTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerTunnelAgentV1 = usdAaaServerTunnelAgentV1.setProductRelease('Version 1 of the tunneling option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version is supported in the\n        Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerTunnelAgentV1 = usdAaaServerTunnelAgentV1.setStatus('current')
usdAaaServerAccountingAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9))
if mibBuilder.loadTexts: usdAaaServerAccountingAgent.setStatus('current')
usdAaaServerAccountingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV1 = usdAaaServerAccountingAgentV1.setProductRelease('Version 1 of the accounting option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version was supported in the\n        Unisphere RX 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV1 = usdAaaServerAccountingAgentV1.setStatus('obsolete')
usdAaaServerAccountingAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV2 = usdAaaServerAccountingAgentV2.setProductRelease('Version 2 of the accounting option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV2 = usdAaaServerAccountingAgentV2.setStatus('current')
usdAaaServerAddressAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10))
if mibBuilder.loadTexts: usdAaaServerAddressAgent.setStatus('current')
usdAaaServerAddressAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAddressAgentV1 = usdAaaServerAddressAgentV1.setProductRelease('Version 1 of the address assignment option of the AAA Server component\n        of the Unisphere Routing Switch SNMP agent.  This version is supported\n        in the Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAddressAgentV1 = usdAaaServerAddressAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-AAA-Server-CONF", PYSNMP_MODULE_ID=usdAaaServerAgent, usdAaaServerAgentV4=usdAaaServerAgentV4, usdAaaServerAddressAgentV1=usdAaaServerAddressAgentV1, usdAaaServerAgentV2=usdAaaServerAgentV2, usdAaaServerAgent=usdAaaServerAgent, usdAaaServerAccountingAgentV1=usdAaaServerAccountingAgentV1, usdAaaServerAddressAgent=usdAaaServerAddressAgent, usdAaaServerBrasAgent=usdAaaServerBrasAgent, usdAaaServerBrasAgentV2=usdAaaServerBrasAgentV2, usdAaaServerBrasAgentV1=usdAaaServerBrasAgentV1, usdAaaServerTunnelAgent=usdAaaServerTunnelAgent, usdAaaServerBaseAgent=usdAaaServerBaseAgent, usdAaaServerAgentV1=usdAaaServerAgentV1, usdAaaServerBaseAgentV1=usdAaaServerBaseAgentV1, usdAaaServerAccountingAgent=usdAaaServerAccountingAgent, usdAaaServerAgentV5=usdAaaServerAgentV5, usdAaaServerTunnelAgentV1=usdAaaServerTunnelAgentV1, usdAaaServerAccountingAgentV2=usdAaaServerAccountingAgentV2, usdAaaServerBrasAgentV3=usdAaaServerBrasAgentV3, usdAaaServerAgentV3=usdAaaServerAgentV3)
