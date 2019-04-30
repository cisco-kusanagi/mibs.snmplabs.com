#
# PySNMP MIB module Unisphere-Data-ERX-System-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-ERX-System-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Unsigned32, Bits, iso, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Unsigned32", "Bits", "iso", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usdSystemAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdSystemAgents")
usdERXSysNotifyGroup, usdERXSysNvsGroup, usdERXSysFabricGroup, usdERXSysPowerGroup, usdERXSysPortGroup, usdERXSysGroup, usdERXSysTemperatureGroup, usdERXSysGeneralGroup, usdERXSysSlotGroup, usdERXSysNotifyGroup3, usdERXSysTemperatureGroup2, usdERXSysTimingGroup, usdERXSysGeneralGroup2, usdERXSysNotifyGroup2, usdERXSysSubsystemGroup = mibBuilder.importSymbols("Unisphere-Data-ERX-System-MIB", "usdERXSysNotifyGroup", "usdERXSysNvsGroup", "usdERXSysFabricGroup", "usdERXSysPowerGroup", "usdERXSysPortGroup", "usdERXSysGroup", "usdERXSysTemperatureGroup", "usdERXSysGeneralGroup", "usdERXSysSlotGroup", "usdERXSysNotifyGroup3", "usdERXSysTemperatureGroup2", "usdERXSysTimingGroup", "usdERXSysGeneralGroup2", "usdERXSysNotifyGroup2", "usdERXSysSubsystemGroup")
usdErxSystemAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1))
usdErxSystemAgent.setRevisions(('2002-04-01 22:32', '2001-04-13 13:03',))
if mibBuilder.loadTexts: usdErxSystemAgent.setLastUpdated('200204012232Z')
if mibBuilder.loadTexts: usdErxSystemAgent.setOrganization('Unisphere Networks, Inc.')
usdErxSystemAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV1 = usdErxSystemAgentV1.setProductRelease('Version 1 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 1.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV1 = usdErxSystemAgentV1.setStatus('obsolete')
usdErxSystemAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV2 = usdErxSystemAgentV2.setProductRelease('Version 2 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV2 = usdErxSystemAgentV2.setStatus('obsolete')
usdErxSystemAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV3 = usdErxSystemAgentV3.setProductRelease('Version 3 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 3.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV3 = usdErxSystemAgentV3.setStatus('obsolete')
usdErxSystemAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV4 = usdErxSystemAgentV4.setProductRelease('Version 4 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV4 = usdErxSystemAgentV4.setStatus('obsolete')
usdErxSystemAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV5 = usdErxSystemAgentV5.setProductRelease('Version 5 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component is\n        supported in the Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV5 = usdErxSystemAgentV5.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-ERX-System-CONF", PYSNMP_MODULE_ID=usdErxSystemAgent, usdErxSystemAgentV2=usdErxSystemAgentV2, usdErxSystemAgent=usdErxSystemAgent, usdErxSystemAgentV1=usdErxSystemAgentV1, usdErxSystemAgentV4=usdErxSystemAgentV4, usdErxSystemAgentV5=usdErxSystemAgentV5, usdErxSystemAgentV3=usdErxSystemAgentV3)
