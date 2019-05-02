#
# PySNMP MIB module Unisphere-Data-ERX-System-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-ERX-System-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, Integer32, ObjectIdentity, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Counter64, IpAddress, MibIdentifier, Counter32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Counter64", "IpAddress", "MibIdentifier", "Counter32", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usdSystemAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usdSystemAgents")
usdERXSysPowerGroup, usdERXSysNotifyGroup2, usdERXSysTimingGroup, usdERXSysFabricGroup, usdERXSysGeneralGroup, usdERXSysTemperatureGroup, usdERXSysTemperatureGroup2, usdERXSysPortGroup, usdERXSysSlotGroup, usdERXSysNvsGroup, usdERXSysGeneralGroup2, usdERXSysNotifyGroup3, usdERXSysGroup, usdERXSysSubsystemGroup, usdERXSysNotifyGroup = mibBuilder.importSymbols("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerGroup", "usdERXSysNotifyGroup2", "usdERXSysTimingGroup", "usdERXSysFabricGroup", "usdERXSysGeneralGroup", "usdERXSysTemperatureGroup", "usdERXSysTemperatureGroup2", "usdERXSysPortGroup", "usdERXSysSlotGroup", "usdERXSysNvsGroup", "usdERXSysGeneralGroup2", "usdERXSysNotifyGroup3", "usdERXSysGroup", "usdERXSysSubsystemGroup", "usdERXSysNotifyGroup")
usdErxSystemAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1))
usdErxSystemAgent.setRevisions(('2002-04-01 22:32', '2001-04-13 13:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdErxSystemAgent.setRevisionsDescriptions(('Added thermal protection support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdErxSystemAgent.setLastUpdated('200204012232Z')
if mibBuilder.loadTexts: usdErxSystemAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdErxSystemAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdErxSystemAgent.setDescription('The agent capabilities definitions for the Edge Routing Switch (ERX) System component of the SNMP agent in the Unisphere ERX family of products.')
usdErxSystemAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV1 = usdErxSystemAgentV1.setProductRelease('Version 1 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 1.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV1 = usdErxSystemAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdErxSystemAgentV1.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in the Unisphere Edge Routing Switch. These capabilities became obsolete when new slot information objects were added.')
usdErxSystemAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV2 = usdErxSystemAgentV2.setProductRelease('Version 2 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV2 = usdErxSystemAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdErxSystemAgentV2.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in the Unisphere Edge Routing Switch. These capabilities became obsolete when the timing group was added.')
usdErxSystemAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV3 = usdErxSystemAgentV3.setProductRelease('Version 3 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 3.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV3 = usdErxSystemAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdErxSystemAgentV3.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in the Unisphere Edge Routing Switch. These capabilities became obsolete when memory management objects and notifications were added.')
usdErxSystemAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV4 = usdErxSystemAgentV4.setProductRelease('Version 4 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component was\n        supported in the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV4 = usdErxSystemAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: usdErxSystemAgentV4.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in the Unisphere Edge Routing Switch. These capabilities became obsolete when thermal protection support was added.')
usdErxSystemAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV5 = usdErxSystemAgentV5.setProductRelease('Version 5 of the ERX System component of the Unisphere Edge Routing\n        Switch SNMP agent.  This version of the ERX System component is\n        supported in the Unisphere RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdErxSystemAgentV5 = usdErxSystemAgentV5.setStatus('current')
if mibBuilder.loadTexts: usdErxSystemAgentV5.setDescription('The MIB supported by the SNMP agent for the ERX (platform-specific) System application in the Unisphere Edge Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-ERX-System-CONF", usdErxSystemAgent=usdErxSystemAgent, usdErxSystemAgentV2=usdErxSystemAgentV2, usdErxSystemAgentV3=usdErxSystemAgentV3, PYSNMP_MODULE_ID=usdErxSystemAgent, usdErxSystemAgentV1=usdErxSystemAgentV1, usdErxSystemAgentV5=usdErxSystemAgentV5, usdErxSystemAgentV4=usdErxSystemAgentV4)
