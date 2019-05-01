#
# PySNMP MIB module Juniper-ATM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ATM-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, Integer32, Unsigned32, Bits, NotificationType, ObjectIdentity, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32", "Unsigned32", "Bits", "NotificationType", "ObjectIdentity", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniAtmAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3))
juniAtmAgent.setRevisions(('2005-08-17 17:26', '2005-02-17 23:15', '2004-01-06 19:53', '2003-11-07 14:57', '2003-05-08 17:57', '2002-09-06 16:54', '2002-08-09 14:15', '2002-01-29 15:18', '2002-01-24 14:16', '2001-12-14 19:51', '2001-05-23 16:12',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniAtmAgent.setRevisionsDescriptions(('Juniper-UNI-ATM-MIB: Removed SVC support. ATM2-MIB: Removed SVC support.', 'Juniper-UNI-ATM-MIB: Added circuit OAM support to the ATM VCC end point agent capabilities.', 'Added support to export the subinterface description to the line cards.', 'ATM2-MIB: Updated from an Internet Draft to a Proposed Standard (RFC 3606). Juniper-UNI-ATM-MIB: Added ATM sub-interface location support.', 'Juniper-UNI-ATM-MIB: Added ATM F4 OAM circuits management and ATM VP description support.', 'Juniper-UNI-ATM-MIB: Replaced Unisphere names with Juniper names.', 'ATM2-MIB: Added support for the atmSigStatTable, the atmAal5VclStatTable and the atmInterfaceExtTable. Juniper-UNI-ATM-MIB: Added receive bandwith support to CAC. Added E164 public addressing support.', 'Juniper-UNI-ATM-MIB: Added ATM switched virtual connection (SVC) support to the VCC end point capabilities.', 'Juniper-UNI-ATM-MIB: Added support for ATM connection admission control (CAC) to the VCC end point capabilities.', 'Juniper-UNI-ATM-MIB: Added ATM traffic shaping capabilities.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniAtmAgent.setLastUpdated('200508171726Z')
if mibBuilder.loadTexts: juniAtmAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniAtmAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniAtmAgent.setDescription('Juniper-UNI-ATM-MIB: The agent capabilities definitions for the ATM component of the SNMP agent in the Juniper E-series family of products.')
juniAtmVccEndPointAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1))
juniAtmVccEndPointAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV1 = juniAtmVccEndPointAgentV1.setProductRelease('Version 1 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV1 = juniAtmVccEndPointAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV1.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilities became obsolete when new objects were added to the juniAtmSubIfGroup and support for the atmfM4IfLoopbackLocationCode object was added.')
juniAtmVccEndPointAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV2 = juniAtmVccEndPointAgentV2.setProductRelease('Version 2 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 3.2 and JUNOSe 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV2 = juniAtmVccEndPointAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV2.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-UNI-ATM-MIB for connection admission control (CAC).')
juniAtmVccEndPointAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV3 = juniAtmVccEndPointAgentV3.setProductRelease('Version 3 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 3.4 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV3 = juniAtmVccEndPointAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV3.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilities became obsolete when support was added to the Juniper-UNI-ATM-MIB for switched virtual connection (SVC).')
juniAtmVccEndPointAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV4 = juniAtmVccEndPointAgentV4.setProductRelease('Version 4 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV4 = juniAtmVccEndPointAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV4.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilitie became obsolete when CAC recieve bandwith and E164 public addressing objects were added.')
juniAtmVccEndPointAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV5 = juniAtmVccEndPointAgentV5.setProductRelease('Version 5 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 4.1 thru 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV5 = juniAtmVccEndPointAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV5.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilitie became obsolete when F4 flow OAM circuits and ATM VP description objects were added to the Juniper-UNI-ATM-MIB.')
juniAtmVccEndPointAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV6 = juniAtmVccEndPointAgentV6.setProductRelease('Version 6 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV6 = juniAtmVccEndPointAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV6.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilitie became obsolete when ATM sub-interface location support was added to the Juniper-UNI-ATM-MIB.')
juniAtmVccEndPointAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV7 = juniAtmVccEndPointAgentV7.setProductRelease('Version 7 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was supported\n        in JUNOSe 5.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV7 = juniAtmVccEndPointAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV7.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilitie became obsolete when support was added to export ATM sub-interface descriptions to the line cards.')
juniAtmVccEndPointAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV8 = juniAtmVccEndPointAgentV8.setProductRelease('Version 8 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was supported\n        in JUNOSe 5.3 and 6.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV8 = juniAtmVccEndPointAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV8.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilities became obsolete when ATM bulk configuration profile override was introduced.')
juniAtmVccEndPointAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV9 = juniAtmVccEndPointAgentV9.setProductRelease('Version 9 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was supported\n        in JUNOSe 6.1 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV9 = juniAtmVccEndPointAgentV9.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV9.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilities became obsolete when ATM bulk configuration profile override was introduced.')
juniAtmVccEndPointAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV10 = juniAtmVccEndPointAgentV10.setProductRelease('Version 10 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent is supported\n        in JUNOSe 7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV10 = juniAtmVccEndPointAgentV10.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV10.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe.These capabilities became obsolete when ATM VP Statistics was introduced.')
juniAtmVccEndPointAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV11 = juniAtmVccEndPointAgentV11.setProductRelease('Version 11 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent is supported\n        in JUNOSe 7.1 and 7.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV11 = juniAtmVccEndPointAgentV11.setStatus('obsolete')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV11.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe. These capabilities became obsolete when SVC support was removed.')
juniAtmVccEndPointAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV12 = juniAtmVccEndPointAgentV12.setProductRelease('Version 12 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent is supported\n        in JUNOSe 7.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV12 = juniAtmVccEndPointAgentV12.setStatus('current')
if mibBuilder.loadTexts: juniAtmVccEndPointAgentV12.setDescription('The MIBs supported by the SNMP agent for the ATM application in JUNOSe.')
juniAtmVpTunnelAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 2))
juniAtmVpTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVpTunnelAgentV1 = juniAtmVpTunnelAgentV1.setProductRelease('Version 1 of the ATM VP tunnel subcomponent of the JUNOSe SNMP agent.\n        This version of the ATM tunnel subcomponent is supported in JUNOSe 3.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVpTunnelAgentV1 = juniAtmVpTunnelAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniAtmVpTunnelAgentV1.setDescription('The MIB supported by the SNMP agent for the ATM application in JUNOSe.')
juniAtmNbmaAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 3))
juniAtmNbmaAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmNbmaAgentV1 = juniAtmNbmaAgentV1.setProductRelease('Version 1 of the ATM NBMA interface subcomponent of the JUNOSe SNMP\n        agent.  This version of the ATM NBMA subcomponent is supported in JUNOSe\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmNbmaAgentV1 = juniAtmNbmaAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniAtmNbmaAgentV1.setDescription('The MIB supported by the SNMP agent for the ATM application in JUNOSe.')
juniAtmSwitchAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4))
juniAtmSwitchAgentV1 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4, 1))
juniAtmSwitchAgentV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4, 2))
juniAtmTrafficShapingAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 5))
juniAtmTrafficShapingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmTrafficShapingAgentV1 = juniAtmTrafficShapingAgentV1.setProductRelease('Version 1 of the ATM traffic shaping subcomponent of the JUNOSe SNMP\n        agent.  This version of the ATM traffic shaping subcomponent is\n        supported in JUNOSe 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmTrafficShapingAgentV1 = juniAtmTrafficShapingAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniAtmTrafficShapingAgentV1.setDescription('The MIB supported by the SNMP agent for the ATM application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-ATM-CONF", juniAtmSwitchAgent=juniAtmSwitchAgent, juniAtmVccEndPointAgentV3=juniAtmVccEndPointAgentV3, juniAtmVccEndPointAgentV4=juniAtmVccEndPointAgentV4, juniAtmVccEndPointAgentV10=juniAtmVccEndPointAgentV10, juniAtmVccEndPointAgentV11=juniAtmVccEndPointAgentV11, juniAtmVccEndPointAgentV6=juniAtmVccEndPointAgentV6, juniAtmVccEndPointAgentV2=juniAtmVccEndPointAgentV2, juniAtmTrafficShapingAgentV1=juniAtmTrafficShapingAgentV1, PYSNMP_MODULE_ID=juniAtmAgent, juniAtmAgent=juniAtmAgent, juniAtmSwitchAgentV1=juniAtmSwitchAgentV1, juniAtmVccEndPointAgentV1=juniAtmVccEndPointAgentV1, juniAtmVccEndPointAgent=juniAtmVccEndPointAgent, juniAtmVccEndPointAgentV5=juniAtmVccEndPointAgentV5, juniAtmVccEndPointAgentV9=juniAtmVccEndPointAgentV9, juniAtmVpTunnelAgent=juniAtmVpTunnelAgent, juniAtmSwitchAgentV2=juniAtmSwitchAgentV2, juniAtmVccEndPointAgentV12=juniAtmVccEndPointAgentV12, juniAtmVpTunnelAgentV1=juniAtmVpTunnelAgentV1, juniAtmVccEndPointAgentV8=juniAtmVccEndPointAgentV8, juniAtmVccEndPointAgentV7=juniAtmVccEndPointAgentV7, juniAtmTrafficShapingAgent=juniAtmTrafficShapingAgent, juniAtmNbmaAgent=juniAtmNbmaAgent, juniAtmNbmaAgentV1=juniAtmNbmaAgentV1)
