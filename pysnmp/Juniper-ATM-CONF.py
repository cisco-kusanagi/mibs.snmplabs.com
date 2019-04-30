#
# PySNMP MIB module Juniper-ATM-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ATM-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, IpAddress, NotificationType, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Unsigned32, Gauge32, ObjectIdentity, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "NotificationType", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniAtmAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3))
juniAtmAgent.setRevisions(('2005-08-17 17:26', '2005-02-17 23:15', '2004-01-06 19:53', '2003-11-07 14:57', '2003-05-08 17:57', '2002-09-06 16:54', '2002-08-09 14:15', '2002-01-29 15:18', '2002-01-24 14:16', '2001-12-14 19:51', '2001-05-23 16:12',))
if mibBuilder.loadTexts: juniAtmAgent.setLastUpdated('200508171726Z')
if mibBuilder.loadTexts: juniAtmAgent.setOrganization('Juniper Networks, Inc.')
juniAtmVccEndPointAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1))
juniAtmVccEndPointAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV1 = juniAtmVccEndPointAgentV1.setProductRelease('Version 1 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV1 = juniAtmVccEndPointAgentV1.setStatus('obsolete')
juniAtmVccEndPointAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV2 = juniAtmVccEndPointAgentV2.setProductRelease('Version 2 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 3.2 and JUNOSe 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV2 = juniAtmVccEndPointAgentV2.setStatus('obsolete')
juniAtmVccEndPointAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV3 = juniAtmVccEndPointAgentV3.setProductRelease('Version 3 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 3.4 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV3 = juniAtmVccEndPointAgentV3.setStatus('obsolete')
juniAtmVccEndPointAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV4 = juniAtmVccEndPointAgentV4.setProductRelease('Version 4 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 4.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV4 = juniAtmVccEndPointAgentV4.setStatus('obsolete')
juniAtmVccEndPointAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV5 = juniAtmVccEndPointAgentV5.setProductRelease('Version 5 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 4.1 thru 5.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV5 = juniAtmVccEndPointAgentV5.setStatus('obsolete')
juniAtmVccEndPointAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV6 = juniAtmVccEndPointAgentV6.setProductRelease('Version 6 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was\n        supported in JUNOSe 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV6 = juniAtmVccEndPointAgentV6.setStatus('obsolete')
juniAtmVccEndPointAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV7 = juniAtmVccEndPointAgentV7.setProductRelease('Version 7 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was supported\n        in JUNOSe 5.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV7 = juniAtmVccEndPointAgentV7.setStatus('obsolete')
juniAtmVccEndPointAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV8 = juniAtmVccEndPointAgentV8.setProductRelease('Version 8 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was supported\n        in JUNOSe 5.3 and 6.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV8 = juniAtmVccEndPointAgentV8.setStatus('obsolete')
juniAtmVccEndPointAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV9 = juniAtmVccEndPointAgentV9.setProductRelease('Version 9 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent was supported\n        in JUNOSe 6.1 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV9 = juniAtmVccEndPointAgentV9.setStatus('obsolete')
juniAtmVccEndPointAgentV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV10 = juniAtmVccEndPointAgentV10.setProductRelease('Version 10 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent is supported\n        in JUNOSe 7.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV10 = juniAtmVccEndPointAgentV10.setStatus('obsolete')
juniAtmVccEndPointAgentV11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV11 = juniAtmVccEndPointAgentV11.setProductRelease('Version 11 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent is supported\n        in JUNOSe 7.1 and 7.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV11 = juniAtmVccEndPointAgentV11.setStatus('obsolete')
juniAtmVccEndPointAgentV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV12 = juniAtmVccEndPointAgentV12.setProductRelease('Version 12 of the ATM VCC end point agent subcomponent of the JUNOSe\n        SNMP agent.  This version of the ATM end point subcomponent is supported\n        in JUNOSe 7.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVccEndPointAgentV12 = juniAtmVccEndPointAgentV12.setStatus('current')
juniAtmVpTunnelAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 2))
juniAtmVpTunnelAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVpTunnelAgentV1 = juniAtmVpTunnelAgentV1.setProductRelease('Version 1 of the ATM VP tunnel subcomponent of the JUNOSe SNMP agent.\n        This version of the ATM tunnel subcomponent is supported in JUNOSe 3.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmVpTunnelAgentV1 = juniAtmVpTunnelAgentV1.setStatus('current')
juniAtmNbmaAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 3))
juniAtmNbmaAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmNbmaAgentV1 = juniAtmNbmaAgentV1.setProductRelease('Version 1 of the ATM NBMA interface subcomponent of the JUNOSe SNMP\n        agent.  This version of the ATM NBMA subcomponent is supported in JUNOSe\n        3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmNbmaAgentV1 = juniAtmNbmaAgentV1.setStatus('current')
juniAtmSwitchAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4))
juniAtmSwitchAgentV1 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4, 1))
juniAtmSwitchAgentV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4, 2))
juniAtmTrafficShapingAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 5))
juniAtmTrafficShapingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmTrafficShapingAgentV1 = juniAtmTrafficShapingAgentV1.setProductRelease('Version 1 of the ATM traffic shaping subcomponent of the JUNOSe SNMP\n        agent.  This version of the ATM traffic shaping subcomponent is\n        supported in JUNOSe 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAtmTrafficShapingAgentV1 = juniAtmTrafficShapingAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-ATM-CONF", juniAtmVccEndPointAgentV8=juniAtmVccEndPointAgentV8, juniAtmVccEndPointAgentV9=juniAtmVccEndPointAgentV9, juniAtmVccEndPointAgentV7=juniAtmVccEndPointAgentV7, juniAtmNbmaAgent=juniAtmNbmaAgent, juniAtmVccEndPointAgentV3=juniAtmVccEndPointAgentV3, juniAtmSwitchAgentV1=juniAtmSwitchAgentV1, juniAtmVccEndPointAgentV4=juniAtmVccEndPointAgentV4, juniAtmVccEndPointAgentV12=juniAtmVccEndPointAgentV12, juniAtmVccEndPointAgentV6=juniAtmVccEndPointAgentV6, juniAtmVccEndPointAgentV11=juniAtmVccEndPointAgentV11, juniAtmVccEndPointAgentV1=juniAtmVccEndPointAgentV1, PYSNMP_MODULE_ID=juniAtmAgent, juniAtmAgent=juniAtmAgent, juniAtmTrafficShapingAgent=juniAtmTrafficShapingAgent, juniAtmVccEndPointAgentV10=juniAtmVccEndPointAgentV10, juniAtmSwitchAgentV2=juniAtmSwitchAgentV2, juniAtmNbmaAgentV1=juniAtmNbmaAgentV1, juniAtmVccEndPointAgent=juniAtmVccEndPointAgent, juniAtmVccEndPointAgentV2=juniAtmVccEndPointAgentV2, juniAtmVpTunnelAgentV1=juniAtmVpTunnelAgentV1, juniAtmTrafficShapingAgentV1=juniAtmTrafficShapingAgentV1, juniAtmSwitchAgent=juniAtmSwitchAgent, juniAtmVpTunnelAgent=juniAtmVpTunnelAgent, juniAtmVccEndPointAgentV5=juniAtmVccEndPointAgentV5)
