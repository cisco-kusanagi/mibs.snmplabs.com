#
# PySNMP MIB module Unisphere-Data-SNMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SNMP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
snmpEngineGroup, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpEngineGroup")
snmpMPDGroup, = mibBuilder.importSymbols("SNMP-MPD-MIB", "snmpMPDGroup")
snmpNotifyFilterType, snmpNotifyFilterStorageType, snmpNotifyGroup, snmpNotifyFilterMask, snmpNotifyFilterProfileStorType, snmpNotifyFilterProfileRowStatus, snmpNotifyRowStatus, snmpNotifyType, snmpNotifyFilterGroup, snmpNotifyTag, snmpNotifyStorageType, snmpNotifyFilterProfileName, snmpNotifyFilterRowStatus = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterType", "snmpNotifyFilterStorageType", "snmpNotifyGroup", "snmpNotifyFilterMask", "snmpNotifyFilterProfileStorType", "snmpNotifyFilterProfileRowStatus", "snmpNotifyRowStatus", "snmpNotifyType", "snmpNotifyFilterGroup", "snmpNotifyTag", "snmpNotifyStorageType", "snmpNotifyFilterProfileName", "snmpNotifyFilterRowStatus")
snmpTargetAddrRetryCount, snmpTargetResponseGroup, snmpTargetParamsSecurityLevel, snmpTargetParamsStorageType, snmpTargetBasicGroup, snmpTargetAddrTDomain, snmpTargetAddrParams, snmpTargetParamsSecurityModel, snmpTargetAddrTagList, snmpTargetParamsSecurityName, snmpTargetAddrTimeout, snmpTargetCommandResponderGroup, snmpTargetAddrStorageType, snmpTargetParamsRowStatus, snmpTargetAddrRowStatus, snmpTargetAddrTAddress, snmpTargetParamsMPModel = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrRetryCount", "snmpTargetResponseGroup", "snmpTargetParamsSecurityLevel", "snmpTargetParamsStorageType", "snmpTargetBasicGroup", "snmpTargetAddrTDomain", "snmpTargetAddrParams", "snmpTargetParamsSecurityModel", "snmpTargetAddrTagList", "snmpTargetParamsSecurityName", "snmpTargetAddrTimeout", "snmpTargetCommandResponderGroup", "snmpTargetAddrStorageType", "snmpTargetParamsRowStatus", "snmpTargetAddrRowStatus", "snmpTargetAddrTAddress", "snmpTargetParamsMPModel")
usmMIBBasicGroup, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmMIBBasicGroup")
vacmBasicGroup, = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmBasicGroup")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
sysORUpTime, snmpGroup, sysORID, snmpBasicNotificationsGroup, sysORLastChange, snmpCommunityGroup, snmpSetGroup, snmpObsoleteGroup, sysORDescr, systemGroup = mibBuilder.importSymbols("SNMPv2-MIB", "sysORUpTime", "snmpGroup", "sysORID", "snmpBasicNotificationsGroup", "sysORLastChange", "snmpCommunityGroup", "snmpSetGroup", "snmpObsoleteGroup", "sysORDescr", "systemGroup")
Gauge32, IpAddress, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSnmpTrapGroup, usdSnmpAccessGroup, usdSnmpGeneralGroup, usdSnmpGeneralGroup2, usdSnmpGroup2, usdSnmpGroup3, usdSnmpAuthFailGroup, usdSnmpGroup = mibBuilder.importSymbols("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGroup", "usdSnmpAccessGroup", "usdSnmpGeneralGroup", "usdSnmpGeneralGroup2", "usdSnmpGroup2", "usdSnmpGroup3", "usdSnmpAuthFailGroup", "usdSnmpGroup")
usdSnmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39))
usdSnmpAgent.setRevisions(('2002-08-14 19:23', '2001-10-16 13:44', '2001-04-13 15:44',))
if mibBuilder.loadTexts: usdSnmpAgent.setLastUpdated('200208141923Z')
if mibBuilder.loadTexts: usdSnmpAgent.setOrganization('Juniper Networks, Inc.')
usdSnmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV1 = usdSnmpAgentV1.setProductRelease('Version 1 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 1.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV1 = usdSnmpAgentV1.setStatus('obsolete')
usdSnmpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV2 = usdSnmpAgentV2.setProductRelease('Version 2 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 2.0 thru 2.2 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV2 = usdSnmpAgentV2.setStatus('obsolete')
usdSnmpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV3 = usdSnmpAgentV3.setProductRelease('Version 3 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 2.3 thru 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV3 = usdSnmpAgentV3.setStatus('obsolete')
usdSnmpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV4 = usdSnmpAgentV4.setProductRelease('Version 4 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV4 = usdSnmpAgentV4.setStatus('obsolete')
usdSnmpAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV5 = usdSnmpAgentV5.setProductRelease('Version 5 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component was supported in\n        the Unisphere RX 3.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV5 = usdSnmpAgentV5.setStatus('obsolete')
usdSnmpAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV6 = usdSnmpAgentV6.setProductRelease('Version 6 of the SNMP entity component of the Unisphere Routing Switch\n        SNMP agent.  This version of the SNMP entity component is supported in\n        the Unisphere RX 3.4 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAgentV6 = usdSnmpAgentV6.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SNMP-CONF", usdSnmpAgentV3=usdSnmpAgentV3, usdSnmpAgentV4=usdSnmpAgentV4, usdSnmpAgentV5=usdSnmpAgentV5, usdSnmpAgent=usdSnmpAgent, usdSnmpAgentV6=usdSnmpAgentV6, usdSnmpAgentV1=usdSnmpAgentV1, usdSnmpAgentV2=usdSnmpAgentV2, PYSNMP_MODULE_ID=usdSnmpAgent)
