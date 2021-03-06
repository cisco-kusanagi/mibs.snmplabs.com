#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-PORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:17:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoNetworkAddress, Unsigned64, TimeIntervalSec, CiscoAlarmSeverity, CiscoInetAddressMask = mibBuilder.importSymbols("CISCO-TC", "CiscoNetworkAddress", "Unsigned64", "TimeIntervalSec", "CiscoAlarmSeverity", "CiscoInetAddressMask")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectDn, CucsManagedObjectId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectDn", "CucsManagedObjectId")
CucsPortPIoFsmStageName, CucsPortPIoFsmTaskItem, CucsNetworkTransport, CucsPortSubGroupSlotId, CucsPortTrust, CucsNetworkConnectionType, CucsFsmFlags, CucsFsmCompletion, CucsNetworkLocale, CucsNetworkPortType, CucsFsmFsmStageStatus, CucsPortGroupType, CucsPortSubGroupConfigState, CucsNetworkSwitchId, CucsNetworkPortRole, CucsConditionRemoteInvRslt, CucsLicenseState, CucsPortPIoFsmCurrentFsm = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsPortPIoFsmStageName", "CucsPortPIoFsmTaskItem", "CucsNetworkTransport", "CucsPortSubGroupSlotId", "CucsPortTrust", "CucsNetworkConnectionType", "CucsFsmFlags", "CucsFsmCompletion", "CucsNetworkLocale", "CucsNetworkPortType", "CucsFsmFsmStageStatus", "CucsPortGroupType", "CucsPortSubGroupConfigState", "CucsNetworkSwitchId", "CucsNetworkPortRole", "CucsConditionRemoteInvRslt", "CucsLicenseState", "CucsPortPIoFsmCurrentFsm")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, TimeTicks, MibIdentifier, Bits, Gauge32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, NotificationType, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "NotificationType", "ObjectIdentity", "Unsigned32")
TextualConvention, RowPointer, TimeInterval, DateAndTime, MacAddress, TimeStamp, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "TimeInterval", "DateAndTime", "MacAddress", "TimeStamp", "DisplayString", "TruthValue")
cucsPortObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38))
if mibBuilder.loadTexts: cucsPortObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsPortObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsPortObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsPortObjects.setDescription('MIB representation of the Cisco Unified Computing System PORT management information model package')
cucsPortDomainEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1), )
if mibBuilder.loadTexts: cucsPortDomainEpTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpTable.setDescription('Cisco UCS port:DomainEp managed object table')
cucsPortDomainEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortDomainEpInstanceId"))
if mibBuilder.loadTexts: cucsPortDomainEpEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpEntry.setDescription('Entry for the cucsPortDomainEpTable table.')
cucsPortDomainEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortDomainEpInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortDomainEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpDn.setDescription('Cisco UCS port:DomainEp:dn managed object property')
cucsPortDomainEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpRn.setDescription('Cisco UCS port:DomainEp:rn managed object property')
cucsPortDomainEpEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpEpDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpEpDn.setDescription('Cisco UCS port:DomainEp:epDn managed object property')
cucsPortDomainEpIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 5), CucsNetworkPortRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpIfRole.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpIfRole.setDescription('Cisco UCS port:DomainEp:ifRole managed object property')
cucsPortDomainEpIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 6), CucsNetworkPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpIfType.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpIfType.setDescription('Cisco UCS port:DomainEp:ifType managed object property')
cucsPortDomainEpLocale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 7), CucsNetworkLocale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpLocale.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpLocale.setDescription('Cisco UCS port:DomainEp:locale managed object property')
cucsPortDomainEpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpName.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpName.setDescription('Cisco UCS port:DomainEp:name managed object property')
cucsPortDomainEpPeerDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpPeerDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpPeerDn.setDescription('Cisco UCS port:DomainEp:peerDn managed object property')
cucsPortDomainEpTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 10), CucsNetworkTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpTransport.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpTransport.setDescription('Cisco UCS port:DomainEp:transport managed object property')
cucsPortDomainEpType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 1, 1, 11), CucsNetworkConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortDomainEpType.setStatus('current')
if mibBuilder.loadTexts: cucsPortDomainEpType.setDescription('Cisco UCS port:DomainEp:type managed object property')
cucsPortGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2), )
if mibBuilder.loadTexts: cucsPortGroupTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupTable.setDescription('Cisco UCS port:Group managed object table')
cucsPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortGroupInstanceId"))
if mibBuilder.loadTexts: cucsPortGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupEntry.setDescription('Entry for the cucsPortGroupTable table.')
cucsPortGroupInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortGroupInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortGroupDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortGroupDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupDn.setDescription('Cisco UCS port:Group:dn managed object property')
cucsPortGroupRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortGroupRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupRn.setDescription('Cisco UCS port:Group:rn managed object property')
cucsPortGroupLocale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 4), CucsNetworkLocale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortGroupLocale.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupLocale.setDescription('Cisco UCS port:Group:locale managed object property')
cucsPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortGroupName.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupName.setDescription('Cisco UCS port:Group:name managed object property')
cucsPortGroupTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 6), CucsNetworkTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortGroupTransport.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupTransport.setDescription('Cisco UCS port:Group:transport managed object property')
cucsPortGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 2, 1, 7), CucsPortGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortGroupType.setStatus('current')
if mibBuilder.loadTexts: cucsPortGroupType.setDescription('Cisco UCS port:Group:type managed object property')
cucsPortPIoFsmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5), )
if mibBuilder.loadTexts: cucsPortPIoFsmTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTable.setDescription('Cisco UCS port:PIoFsm managed object table')
cucsPortPIoFsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortPIoFsmInstanceId"))
if mibBuilder.loadTexts: cucsPortPIoFsmEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmEntry.setDescription('Entry for the cucsPortPIoFsmTable table.')
cucsPortPIoFsmInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortPIoFsmInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortPIoFsmDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmDn.setDescription('Cisco UCS port:PIoFsm:dn managed object property')
cucsPortPIoFsmRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmRn.setDescription('Cisco UCS port:PIoFsm:rn managed object property')
cucsPortPIoFsmCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmCompletionTime.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmCompletionTime.setDescription('Cisco UCS port:PIoFsm:completionTime managed object property')
cucsPortPIoFsmCurrentFsm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 5), CucsPortPIoFsmCurrentFsm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmCurrentFsm.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmCurrentFsm.setDescription('Cisco UCS port:PIoFsm:currentFsm managed object property')
cucsPortPIoFsmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmDescr.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmDescr.setDescription('Cisco UCS port:PIoFsm:descr managed object property')
cucsPortPIoFsmFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 7), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmFsmStatus.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmFsmStatus.setDescription('Cisco UCS port:PIoFsm:fsmStatus managed object property')
cucsPortPIoFsmProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmProgress.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmProgress.setDescription('Cisco UCS port:PIoFsm:progress managed object property')
cucsPortPIoFsmRmtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmRmtErrCode.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmRmtErrCode.setDescription('Cisco UCS port:PIoFsm:rmtErrCode managed object property')
cucsPortPIoFsmRmtErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmRmtErrDescr.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmRmtErrDescr.setDescription('Cisco UCS port:PIoFsm:rmtErrDescr managed object property')
cucsPortPIoFsmRmtRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 5, 1, 11), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmRmtRslt.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmRmtRslt.setDescription('Cisco UCS port:PIoFsm:rmtRslt managed object property')
cucsPortPIoFsmStageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6), )
if mibBuilder.loadTexts: cucsPortPIoFsmStageTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageTable.setDescription('Cisco UCS port:PIoFsmStage managed object table')
cucsPortPIoFsmStageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortPIoFsmStageInstanceId"))
if mibBuilder.loadTexts: cucsPortPIoFsmStageEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageEntry.setDescription('Entry for the cucsPortPIoFsmStageTable table.')
cucsPortPIoFsmStageInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortPIoFsmStageInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortPIoFsmStageDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageDn.setDescription('Cisco UCS port:PIoFsmStage:dn managed object property')
cucsPortPIoFsmStageRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageRn.setDescription('Cisco UCS port:PIoFsmStage:rn managed object property')
cucsPortPIoFsmStageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageDescr.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageDescr.setDescription('Cisco UCS port:PIoFsmStage:descr managed object property')
cucsPortPIoFsmStageLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageLastUpdateTime.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageLastUpdateTime.setDescription('Cisco UCS port:PIoFsmStage:lastUpdateTime managed object property')
cucsPortPIoFsmStageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 6), CucsPortPIoFsmStageName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageName.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageName.setDescription('Cisco UCS port:PIoFsmStage:name managed object property')
cucsPortPIoFsmStageOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageOrder.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageOrder.setDescription('Cisco UCS port:PIoFsmStage:order managed object property')
cucsPortPIoFsmStageRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageRetry.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageRetry.setDescription('Cisco UCS port:PIoFsmStage:retry managed object property')
cucsPortPIoFsmStageStageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 6, 1, 9), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmStageStageStatus.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmStageStageStatus.setDescription('Cisco UCS port:PIoFsmStage:stageStatus managed object property')
cucsPortPIoFsmTaskTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4), )
if mibBuilder.loadTexts: cucsPortPIoFsmTaskTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskTable.setDescription('Cisco UCS port:PIoFsmTask managed object table')
cucsPortPIoFsmTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortPIoFsmTaskInstanceId"))
if mibBuilder.loadTexts: cucsPortPIoFsmTaskEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskEntry.setDescription('Entry for the cucsPortPIoFsmTaskTable table.')
cucsPortPIoFsmTaskInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortPIoFsmTaskInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortPIoFsmTaskDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmTaskDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskDn.setDescription('Cisco UCS port:PIoFsmTask:dn managed object property')
cucsPortPIoFsmTaskRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmTaskRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskRn.setDescription('Cisco UCS port:PIoFsmTask:rn managed object property')
cucsPortPIoFsmTaskCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 4), CucsFsmCompletion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmTaskCompletion.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskCompletion.setDescription('Cisco UCS port:PIoFsmTask:completion managed object property')
cucsPortPIoFsmTaskFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 5), CucsFsmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmTaskFlags.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskFlags.setDescription('Cisco UCS port:PIoFsmTask:flags managed object property')
cucsPortPIoFsmTaskItem = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 6), CucsPortPIoFsmTaskItem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmTaskItem.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskItem.setDescription('Cisco UCS port:PIoFsmTask:item managed object property')
cucsPortPIoFsmTaskSeqId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortPIoFsmTaskSeqId.setStatus('current')
if mibBuilder.loadTexts: cucsPortPIoFsmTaskSeqId.setDescription('Cisco UCS port:PIoFsmTask:seqId managed object property')
cucsPortSubGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7), )
if mibBuilder.loadTexts: cucsPortSubGroupTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupTable.setDescription('Cisco UCS port:SubGroup managed object table')
cucsPortSubGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortSubGroupInstanceId"))
if mibBuilder.loadTexts: cucsPortSubGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupEntry.setDescription('Entry for the cucsPortSubGroupTable table.')
cucsPortSubGroupInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortSubGroupInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortSubGroupDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupDn.setDescription('Cisco UCS port:SubGroup:dn managed object property')
cucsPortSubGroupRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupRn.setDescription('Cisco UCS port:SubGroup:rn managed object property')
cucsPortSubGroupAggrPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupAggrPortId.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupAggrPortId.setDescription('Cisco UCS port:SubGroup:aggrPortId managed object property')
cucsPortSubGroupConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 5), CucsPortSubGroupConfigState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupConfigState.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupConfigState.setDescription('Cisco UCS port:SubGroup:configState managed object property')
cucsPortSubGroupLicGP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 6), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupLicGP.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupLicGP.setDescription('Cisco UCS port:SubGroup:licGP managed object property')
cucsPortSubGroupLicState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 7), CucsLicenseState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupLicState.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupLicState.setDescription('Cisco UCS port:SubGroup:licState managed object property')
cucsPortSubGroupLocale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 8), CucsNetworkLocale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupLocale.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupLocale.setDescription('Cisco UCS port:SubGroup:locale managed object property')
cucsPortSubGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupName.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupName.setDescription('Cisco UCS port:SubGroup:name managed object property')
cucsPortSubGroupSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 10), CucsPortSubGroupSlotId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupSlotId.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupSlotId.setDescription('Cisco UCS port:SubGroup:slotId managed object property')
cucsPortSubGroupSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 11), CucsNetworkSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupSwitchId.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupSwitchId.setDescription('Cisco UCS port:SubGroup:switchId managed object property')
cucsPortSubGroupTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 12), CucsNetworkTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupTransport.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupTransport.setDescription('Cisco UCS port:SubGroup:transport managed object property')
cucsPortSubGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 7, 1, 13), CucsNetworkConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortSubGroupType.setStatus('current')
if mibBuilder.loadTexts: cucsPortSubGroupType.setDescription('Cisco UCS port:SubGroup:type managed object property')
cucsPortTrustModeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3), )
if mibBuilder.loadTexts: cucsPortTrustModeTable.setStatus('current')
if mibBuilder.loadTexts: cucsPortTrustModeTable.setDescription('Cisco UCS port:TrustMode managed object table')
cucsPortTrustModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PORT-MIB", "cucsPortTrustModeInstanceId"))
if mibBuilder.loadTexts: cucsPortTrustModeEntry.setStatus('current')
if mibBuilder.loadTexts: cucsPortTrustModeEntry.setDescription('Entry for the cucsPortTrustModeTable table.')
cucsPortTrustModeInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsPortTrustModeInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsPortTrustModeInstanceId.setDescription('Instance identifier of the managed object.')
cucsPortTrustModeDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortTrustModeDn.setStatus('current')
if mibBuilder.loadTexts: cucsPortTrustModeDn.setDescription('Cisco UCS port:TrustMode:dn managed object property')
cucsPortTrustModeRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortTrustModeRn.setStatus('current')
if mibBuilder.loadTexts: cucsPortTrustModeRn.setDescription('Cisco UCS port:TrustMode:rn managed object property')
cucsPortTrustModeState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 38, 3, 1, 4), CucsPortTrust()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsPortTrustModeState.setStatus('current')
if mibBuilder.loadTexts: cucsPortTrustModeState.setDescription('Cisco UCS port:TrustMode:state managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-PORT-MIB", cucsPortTrustModeEntry=cucsPortTrustModeEntry, cucsPortDomainEpInstanceId=cucsPortDomainEpInstanceId, cucsPortDomainEpEpDn=cucsPortDomainEpEpDn, cucsPortSubGroupTable=cucsPortSubGroupTable, cucsPortDomainEpTransport=cucsPortDomainEpTransport, cucsPortPIoFsmStageTable=cucsPortPIoFsmStageTable, cucsPortPIoFsmStageInstanceId=cucsPortPIoFsmStageInstanceId, cucsPortTrustModeRn=cucsPortTrustModeRn, cucsPortPIoFsmTaskRn=cucsPortPIoFsmTaskRn, cucsPortSubGroupName=cucsPortSubGroupName, cucsPortSubGroupTransport=cucsPortSubGroupTransport, cucsPortPIoFsmRmtErrCode=cucsPortPIoFsmRmtErrCode, cucsPortSubGroupLocale=cucsPortSubGroupLocale, cucsPortPIoFsmStageOrder=cucsPortPIoFsmStageOrder, cucsPortPIoFsmStageEntry=cucsPortPIoFsmStageEntry, cucsPortPIoFsmTaskDn=cucsPortPIoFsmTaskDn, cucsPortTrustModeTable=cucsPortTrustModeTable, cucsPortPIoFsmTaskItem=cucsPortPIoFsmTaskItem, cucsPortPIoFsmStageDn=cucsPortPIoFsmStageDn, cucsPortGroupInstanceId=cucsPortGroupInstanceId, cucsPortPIoFsmStageRn=cucsPortPIoFsmStageRn, cucsPortPIoFsmTaskTable=cucsPortPIoFsmTaskTable, cucsPortPIoFsmStageRetry=cucsPortPIoFsmStageRetry, cucsPortPIoFsmCurrentFsm=cucsPortPIoFsmCurrentFsm, cucsPortPIoFsmRmtErrDescr=cucsPortPIoFsmRmtErrDescr, cucsPortDomainEpLocale=cucsPortDomainEpLocale, cucsPortObjects=cucsPortObjects, cucsPortPIoFsmTaskSeqId=cucsPortPIoFsmTaskSeqId, cucsPortPIoFsmDn=cucsPortPIoFsmDn, cucsPortTrustModeState=cucsPortTrustModeState, cucsPortSubGroupRn=cucsPortSubGroupRn, cucsPortDomainEpIfRole=cucsPortDomainEpIfRole, PYSNMP_MODULE_ID=cucsPortObjects, cucsPortGroupEntry=cucsPortGroupEntry, cucsPortPIoFsmStageName=cucsPortPIoFsmStageName, cucsPortGroupTable=cucsPortGroupTable, cucsPortSubGroupType=cucsPortSubGroupType, cucsPortPIoFsmTaskFlags=cucsPortPIoFsmTaskFlags, cucsPortPIoFsmRn=cucsPortPIoFsmRn, cucsPortPIoFsmFsmStatus=cucsPortPIoFsmFsmStatus, cucsPortGroupTransport=cucsPortGroupTransport, cucsPortDomainEpName=cucsPortDomainEpName, cucsPortDomainEpDn=cucsPortDomainEpDn, cucsPortPIoFsmEntry=cucsPortPIoFsmEntry, cucsPortGroupDn=cucsPortGroupDn, cucsPortGroupLocale=cucsPortGroupLocale, cucsPortSubGroupAggrPortId=cucsPortSubGroupAggrPortId, cucsPortPIoFsmRmtRslt=cucsPortPIoFsmRmtRslt, cucsPortPIoFsmStageDescr=cucsPortPIoFsmStageDescr, cucsPortPIoFsmTable=cucsPortPIoFsmTable, cucsPortGroupRn=cucsPortGroupRn, cucsPortSubGroupConfigState=cucsPortSubGroupConfigState, cucsPortGroupName=cucsPortGroupName, cucsPortTrustModeDn=cucsPortTrustModeDn, cucsPortSubGroupSwitchId=cucsPortSubGroupSwitchId, cucsPortPIoFsmTaskInstanceId=cucsPortPIoFsmTaskInstanceId, cucsPortSubGroupDn=cucsPortSubGroupDn, cucsPortPIoFsmProgress=cucsPortPIoFsmProgress, cucsPortDomainEpType=cucsPortDomainEpType, cucsPortSubGroupSlotId=cucsPortSubGroupSlotId, cucsPortDomainEpRn=cucsPortDomainEpRn, cucsPortDomainEpTable=cucsPortDomainEpTable, cucsPortTrustModeInstanceId=cucsPortTrustModeInstanceId, cucsPortSubGroupLicGP=cucsPortSubGroupLicGP, cucsPortDomainEpEntry=cucsPortDomainEpEntry, cucsPortDomainEpPeerDn=cucsPortDomainEpPeerDn, cucsPortPIoFsmInstanceId=cucsPortPIoFsmInstanceId, cucsPortGroupType=cucsPortGroupType, cucsPortSubGroupLicState=cucsPortSubGroupLicState, cucsPortDomainEpIfType=cucsPortDomainEpIfType, cucsPortPIoFsmStageStageStatus=cucsPortPIoFsmStageStageStatus, cucsPortSubGroupInstanceId=cucsPortSubGroupInstanceId, cucsPortPIoFsmCompletionTime=cucsPortPIoFsmCompletionTime, cucsPortPIoFsmStageLastUpdateTime=cucsPortPIoFsmStageLastUpdateTime, cucsPortPIoFsmTaskCompletion=cucsPortPIoFsmTaskCompletion, cucsPortPIoFsmTaskEntry=cucsPortPIoFsmTaskEntry, cucsPortPIoFsmDescr=cucsPortPIoFsmDescr, cucsPortSubGroupEntry=cucsPortSubGroupEntry)
