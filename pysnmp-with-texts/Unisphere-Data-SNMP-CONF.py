#
# PySNMP MIB module Unisphere-Data-SNMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SNMP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
snmpEngineGroup, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpEngineGroup")
snmpMPDGroup, = mibBuilder.importSymbols("SNMP-MPD-MIB", "snmpMPDGroup")
snmpNotifyFilterMask, snmpNotifyFilterGroup, snmpNotifyFilterProfileRowStatus, snmpNotifyFilterRowStatus, snmpNotifyTag, snmpNotifyStorageType, snmpNotifyFilterProfileStorType, snmpNotifyFilterStorageType, snmpNotifyType, snmpNotifyFilterType, snmpNotifyRowStatus, snmpNotifyGroup, snmpNotifyFilterProfileName = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterMask", "snmpNotifyFilterGroup", "snmpNotifyFilterProfileRowStatus", "snmpNotifyFilterRowStatus", "snmpNotifyTag", "snmpNotifyStorageType", "snmpNotifyFilterProfileStorType", "snmpNotifyFilterStorageType", "snmpNotifyType", "snmpNotifyFilterType", "snmpNotifyRowStatus", "snmpNotifyGroup", "snmpNotifyFilterProfileName")
snmpTargetBasicGroup, snmpTargetParamsSecurityName, snmpTargetAddrRetryCount, snmpTargetAddrTagList, snmpTargetCommandResponderGroup, snmpTargetAddrTAddress, snmpTargetParamsSecurityLevel, snmpTargetParamsMPModel, snmpTargetParamsSecurityModel, snmpTargetAddrRowStatus, snmpTargetResponseGroup, snmpTargetParamsRowStatus, snmpTargetAddrParams, snmpTargetParamsStorageType, snmpTargetAddrStorageType, snmpTargetAddrTimeout, snmpTargetAddrTDomain = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetBasicGroup", "snmpTargetParamsSecurityName", "snmpTargetAddrRetryCount", "snmpTargetAddrTagList", "snmpTargetCommandResponderGroup", "snmpTargetAddrTAddress", "snmpTargetParamsSecurityLevel", "snmpTargetParamsMPModel", "snmpTargetParamsSecurityModel", "snmpTargetAddrRowStatus", "snmpTargetResponseGroup", "snmpTargetParamsRowStatus", "snmpTargetAddrParams", "snmpTargetParamsStorageType", "snmpTargetAddrStorageType", "snmpTargetAddrTimeout", "snmpTargetAddrTDomain")
usmMIBBasicGroup, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmMIBBasicGroup")
vacmBasicGroup, = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmBasicGroup")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
snmpObsoleteGroup, sysORID, sysORUpTime, sysORLastChange, snmpBasicNotificationsGroup, snmpCommunityGroup, snmpGroup, sysORDescr, systemGroup, snmpSetGroup = mibBuilder.importSymbols("SNMPv2-MIB", "snmpObsoleteGroup", "sysORID", "sysORUpTime", "sysORLastChange", "snmpBasicNotificationsGroup", "snmpCommunityGroup", "snmpGroup", "sysORDescr", "systemGroup", "snmpSetGroup")
ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, Counter32, NotificationType, ModuleIdentity, Gauge32, Bits, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "iso", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSnmpAccessGroup, usdSnmpGroup3, usdSnmpGeneralGroup2, usdSnmpGeneralGroup, usdSnmpGroup, usdSnmpTrapGroup, usdSnmpAuthFailGroup, usdSnmpGroup2 = mibBuilder.importSymbols("Unisphere-Data-SNMP-MIB", "usdSnmpAccessGroup", "usdSnmpGroup3", "usdSnmpGeneralGroup2", "usdSnmpGeneralGroup", "usdSnmpGroup", "usdSnmpTrapGroup", "usdSnmpAuthFailGroup", "usdSnmpGroup2")
usdSnmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39))
usdSnmpAgent.setRevisions(('2002-08-14 19:23', '2001-10-16 13:44', '2001-04-13 15:44',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSnmpAgent.setRevisionsDescriptions(('Added support for proxy enable/disable feature.', 'Added support for the snmpSetGroup. Added new objects to the Unisphere-Data-SNMP-MIB supporting interface compress, trap severities and trap severity filtering.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdSnmpAgent.setLastUpdated('200208141923Z')
if mibBuilder.loadTexts: usdSnmpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: usdSnmpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSnmpAgent.setDescription('The agent capabilities definitions for the SNMP entity component of the SNMP agent in the Juniper Routing Switch family of products.')
usdSnmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV1 = usdSnmpAgentV1.setProductRelease('Version 1 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV1 = usdSnmpAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpAgentV1.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in the Unisphere Routing Switch. These capabilities became obsolete when SNMPv3 support, View support, and Named Access List support were added.')
usdSnmpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV2 = usdSnmpAgentV2.setProductRelease('Version 2 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 2.0 thru 2.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV2 = usdSnmpAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpAgentV2.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in the Unisphere Routing Switch. These capabilities became obsolete when the usdSnmpInterfaceMode object was added.')
usdSnmpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV3 = usdSnmpAgentV3.setProductRelease('Version 3 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 2.3 thru 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV3 = usdSnmpAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpAgentV3.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in the Unisphere Routing Switch. These capabilities became obsolete when SNMPv2-MIB.sysORTable support was added.')
usdSnmpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV4 = usdSnmpAgentV4.setProductRelease('Version 4 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV4 = usdSnmpAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpAgentV4.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in the Unisphere Routing Switch. These capabilities became obsolete when SNMPv2-MIB.snmpSetGroup support was added and new Unisphere SNMP MIB objects were added supporting interface compress, trap severities and trap severity filtering.')
usdSnmpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV5 = usdSnmpAgentV5.setProductRelease('Version 5 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV5 = usdSnmpAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpAgentV5.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in the Unisphere Routing Switch. These capabilities became obsolete when support for proxy enable/disable was added.')
usdSnmpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV6 = usdSnmpAgentV6.setProductRelease('Version 6 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component is supported in\n        the Unisphere RX 3.4 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV6 = usdSnmpAgentV6.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAgentV6.setDescription('The MIBs supported by the SNMP agent for the SNMP entity application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-SNMP-CONF", usdSnmpAgentV6=usdSnmpAgentV6, usdSnmpAgentV3=usdSnmpAgentV3, usdSnmpAgentV2=usdSnmpAgentV2, usdSnmpAgent=usdSnmpAgent, PYSNMP_MODULE_ID=usdSnmpAgent, usdSnmpAgentV1=usdSnmpAgentV1, usdSnmpAgentV4=usdSnmpAgentV4, usdSnmpAgentV5=usdSnmpAgentV5)
