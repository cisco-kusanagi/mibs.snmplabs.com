#
# PySNMP MIB module Unisphere-Data-AAA-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-AAA-Server-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, ModuleIdentity, Integer32, Counter32, Gauge32, Bits, NotificationType, TimeTicks, IpAddress, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "Bits", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usdAaaGroup2, usdAaaBrasGroup4, usdAaaAccountingGroup, usdAaaBrasGroup2, usdAaaTunnelGroup, usdAaaBrasGroup, usdAaaCapabilitiesGroup, usdAaaSubscriberGroup3, usdAaaSubscriberGroup, usdAaaGroup, usdAaaAddressGroup, usdAaaBasicGroup, usdAaaBrasGroup3, usdAaaSubscriberGroup2, usdAaaAuthenticationGroup, usdAaaAccountingGroup2 = mibBuilder.importSymbols("Unisphere-Data-AAA-MIB", "usdAaaGroup2", "usdAaaBrasGroup4", "usdAaaAccountingGroup", "usdAaaBrasGroup2", "usdAaaTunnelGroup", "usdAaaBrasGroup", "usdAaaCapabilitiesGroup", "usdAaaSubscriberGroup3", "usdAaaSubscriberGroup", "usdAaaGroup", "usdAaaAddressGroup", "usdAaaBasicGroup", "usdAaaBrasGroup3", "usdAaaSubscriberGroup2", "usdAaaAuthenticationGroup", "usdAaaAccountingGroup2")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdAaaServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1))
usdAaaServerAgent.setRevisions(('2002-05-13 19:32', '2002-01-03 20:30', '2001-09-18 21:13', '2001-04-10 14:02',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdAaaServerAgent.setRevisionsDescriptions(('Added new B-RAS and accounting objects.', 'Added support for subscriber-per-interface-location monitoring.', 'Separated out optional capabilities. Added the subscriber and capabilities groups.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdAaaServerAgent.setLastUpdated('200205131932Z')
if mibBuilder.loadTexts: usdAaaServerAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdAaaServerAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdAaaServerAgent.setDescription('The agent capabilities definitions for the Authentication, Authorization and Accounting (AAA) Server component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdAaaServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV1 = usdAaaServerAgentV1.setProductRelease('Version 1 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 1.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV1 = usdAaaServerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerAgentV1.setDescription('The MIB supported by the SNMP agent for the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added.')
usdAaaServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV2 = usdAaaServerAgentV2.setProductRelease('Version 2 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 2.x system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV2 = usdAaaServerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerAgentV2.setDescription('The MIB supported by the SNMP agent for the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added and new groupings were defined.')
usdAaaServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV3 = usdAaaServerAgentV3.setProductRelease('Version 3 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 3.0 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV3 = usdAaaServerAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerAgentV3.setDescription('The MIB supported by the SNMP agent for the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when the rsAaaAssignDomainStripDomain object was added to the B-RAS group.')
usdAaaServerAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV4 = usdAaaServerAgentV4.setProductRelease('Version 4 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 3.1 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV4 = usdAaaServerAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerAgentV4.setDescription('The MIB supported by the SNMP agent for the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when new assignment delimiter objects were added to the B-RAS group.')
usdAaaServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV5 = usdAaaServerAgentV5.setProductRelease('Version 5 of the AAA Server component of the Unisphere Routing Switch\n        SNMP agent.  This version was supported in the Unisphere RX 3.2 system\n        release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAgentV5 = usdAaaServerAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerAgentV5.setDescription('The MIB supported by the SNMP agent for the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when the groups were separated into multiple statements and the subscriber and capabilties groups were added.')
usdAaaServerBaseAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6))
if mibBuilder.loadTexts: usdAaaServerBaseAgent.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerBaseAgent.setDescription('The registration group of agent capabilities for the basic AAA Server management.')
usdAaaServerBaseAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBaseAgentV1 = usdAaaServerBaseAgentV1.setProductRelease('Version 1 of the basic AAA Server component of the Unisphere Routing\n        Switch SNMP agent.  This version is supported in the Unisphere RX 3.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBaseAgentV1 = usdAaaServerBaseAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerBaseAgentV1.setDescription('The MIB groups supported by the SNMP agent for the basic AAA Server application in the Unisphere Routing Switch.')
usdAaaServerBrasAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7))
if mibBuilder.loadTexts: usdAaaServerBrasAgent.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerBrasAgent.setDescription('The registration group of agent capabilities for AAA Server B-RAS management.')
usdAaaServerBrasAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV1 = usdAaaServerBrasAgentV1.setProductRelease('Version 1 of the B-RAS option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version was supported in the\n        Unisphere RX 3.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV1 = usdAaaServerBrasAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerBrasAgentV1.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for monitoring subscriber information by interface location.')
usdAaaServerBrasAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV2 = usdAaaServerBrasAgentV2.setProductRelease('Version 2 of the B-RAS option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version was supported in the\n        Unisphere RX 3.4 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV2 = usdAaaServerBrasAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerBrasAgentV2.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when new B-RAS objects were added.')
usdAaaServerBrasAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV3 = usdAaaServerBrasAgentV3.setProductRelease('Version 3 of the B-RAS option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerBrasAgentV3 = usdAaaServerBrasAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerBrasAgentV3.setDescription('The MIB groups supported by the SNMP agent for the B-RAS option of the AAA Server application in the Unisphere Routing Switch.')
usdAaaServerTunnelAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8))
if mibBuilder.loadTexts: usdAaaServerTunnelAgent.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerTunnelAgent.setDescription('The registration group of agent capabilities for AAA Server tunneling management.')
usdAaaServerTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerTunnelAgentV1 = usdAaaServerTunnelAgentV1.setProductRelease('Version 1 of the tunneling option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version is supported in the\n        Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerTunnelAgentV1 = usdAaaServerTunnelAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerTunnelAgentV1.setDescription('The MIB group supported by the SNMP agent for the tunneling option of the AAA Server application in the Unisphere Routing Switch.')
usdAaaServerAccountingAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9))
if mibBuilder.loadTexts: usdAaaServerAccountingAgent.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerAccountingAgent.setDescription('The registration group of agent capabilities for AAA Server accounting management.')
usdAaaServerAccountingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV1 = usdAaaServerAccountingAgentV1.setProductRelease('Version 1 of the accounting option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version was supported in the\n        Unisphere RX 3.3 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV1 = usdAaaServerAccountingAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdAaaServerAccountingAgentV1.setDescription('The MIB group supported by the SNMP agent for the accounting option of the AAA Server application in the Unisphere Routing Switch. These capabilities became obsolete when a new accounting object was added.')
usdAaaServerAccountingAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV2 = usdAaaServerAccountingAgentV2.setProductRelease('Version 2 of the accounting option of the AAA Server component of the\n        Unisphere Routing Switch SNMP agent.  This version is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAccountingAgentV2 = usdAaaServerAccountingAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerAccountingAgentV2.setDescription('The MIB group supported by the SNMP agent for the accounting option of the AAA Server application in the Unisphere Routing Switch.')
usdAaaServerAddressAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10))
if mibBuilder.loadTexts: usdAaaServerAddressAgent.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerAddressAgent.setDescription('The registration group of agent capabilities for AAA Server address assignment management.')
usdAaaServerAddressAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAddressAgentV1 = usdAaaServerAddressAgentV1.setProductRelease('Version 1 of the address assignment option of the AAA Server component\n        of the Unisphere Routing Switch SNMP agent.  This version is supported\n        in the Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAaaServerAddressAgentV1 = usdAaaServerAddressAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdAaaServerAddressAgentV1.setDescription('The MIB group supported by the SNMP agent for the address assignment option of the AAA Server application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-AAA-Server-CONF", usdAaaServerBaseAgentV1=usdAaaServerBaseAgentV1, usdAaaServerAddressAgent=usdAaaServerAddressAgent, usdAaaServerBrasAgentV3=usdAaaServerBrasAgentV3, usdAaaServerAgentV3=usdAaaServerAgentV3, usdAaaServerAgentV2=usdAaaServerAgentV2, usdAaaServerBrasAgentV1=usdAaaServerBrasAgentV1, usdAaaServerBrasAgent=usdAaaServerBrasAgent, usdAaaServerAccountingAgentV2=usdAaaServerAccountingAgentV2, usdAaaServerAccountingAgentV1=usdAaaServerAccountingAgentV1, usdAaaServerAgentV5=usdAaaServerAgentV5, usdAaaServerAgent=usdAaaServerAgent, usdAaaServerAgentV1=usdAaaServerAgentV1, usdAaaServerTunnelAgent=usdAaaServerTunnelAgent, usdAaaServerAgentV4=usdAaaServerAgentV4, usdAaaServerAddressAgentV1=usdAaaServerAddressAgentV1, usdAaaServerTunnelAgentV1=usdAaaServerTunnelAgentV1, usdAaaServerAccountingAgent=usdAaaServerAccountingAgent, usdAaaServerBrasAgentV2=usdAaaServerBrasAgentV2, usdAaaServerBaseAgent=usdAaaServerBaseAgent, PYSNMP_MODULE_ID=usdAaaServerAgent)
