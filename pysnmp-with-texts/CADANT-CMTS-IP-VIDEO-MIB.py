#
# PySNMP MIB module CADANT-CMTS-IP-VIDEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-IP-VIDEO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
cadCmtsIpVideo, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadCmtsIpVideo")
CardId, PortId = mibBuilder.importSymbols("CADANT-TC", "CardId", "PortId")
TenthdB, = mibBuilder.importSymbols("DOCS-IF-MIB", "TenthdB")
AttributeMask, = mibBuilder.importSymbols("DOCS-IF3-MIB", "AttributeMask")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
SnmpEngineID, SnmpAdminString = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpEngineID", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter64, IpAddress, Integer32, NotificationType, ModuleIdentity, MibIdentifier, ObjectIdentity, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "IpAddress", "Integer32", "NotificationType", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32")
RowStatus, TextualConvention, DisplayString, MacAddress, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "MacAddress", "TruthValue", "DateAndTime")
cadCmtsIpVideoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1))
cadCmtsIpVideoMib.setRevisions(('2011-08-04 00:00', '2011-07-11 00:00', '2011-04-20 00:00', '2011-04-19 00:00', '2010-12-16 00:00', '2010-07-07 00:00', '2010-04-20 00:00', '2010-04-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadCmtsIpVideoMib.setRevisionsDescriptions(('Change indices of cadIpVideoMonitorDropsEntry to cadIpVideoMonitorCardId, cadIpVideoMonitorPortConnectorId', 'Change indices of cadIpVideoMonitorDropsEntry to cerCardId, cerPortConnectorId', 'Add cadSysIpVideoMulticastAllowedUsage.', 'Add cadSysIpVideoMulticastControlled.', 'Add cadSysIpVideoInterDbcDelayTimer', 'Change description of cadIpVideoMonitorCurTimeIdx and cadIpVideoMonitorDsChlCurTimeIdx.', 'Add cadIPVideoMonitorDropsTable and cadIPVideoMonitorDsChlTable.', 'Initial version.',))
if mibBuilder.loadTexts: cadCmtsIpVideoMib.setLastUpdated('201108040000Z')
if mibBuilder.loadTexts: cadCmtsIpVideoMib.setOrganization('Arris International, Inc.')
if mibBuilder.loadTexts: cadCmtsIpVideoMib.setContactInfo('Arris Technical Support Phone: +1 630 281 3000 E-Mail: support@arrisi.com')
if mibBuilder.loadTexts: cadCmtsIpVideoMib.setDescription('Arris C4 system IP video parameters and constants')
cadSysIpVideoCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1))
cadSysIpVideoAttributeMask = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 1), AttributeMask().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSysIpVideoAttributeMask.setStatus('current')
if mibBuilder.loadTexts: cadSysIpVideoAttributeMask.setDescription('This Attribute Mask provides a mechanism for the MSO to tell the C4 CMTS which attribute bit(s) indicate a type of IP Video for the purposes of monitoring. Only the least significant 16 bits of this mask (the ones numbered 16-31) can be non-zero.')
cadSysIpVideoVodThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSysIpVideoVodThreshold.setStatus('current')
if mibBuilder.loadTexts: cadSysIpVideoVodThreshold.setDescription('This threshold timer parameter sets the watermark against which all IP Video VOD setups will be measured. When a setup exceeds this parameter, then a counter is pegged. For the purpose of this threshold, reception of the request message (Gate-Set in PCMM) begins the setup time and completion of all necessary protocol exchanges at both the CM and network side stops the timer.')
cadSysIpVideoLinearThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSysIpVideoLinearThreshold.setStatus('current')
if mibBuilder.loadTexts: cadSysIpVideoLinearThreshold.setDescription('This threshold timer parameter sets the watermark against which all IP Video Linear setups will be measured. When a setup exceeds this parameter, then a counter is pegged. For the purpose of this threshold, reception of the request message (Gate-Set in PCMM) begins the setup time and completion of all necessary protocol exchanges at both the CM and network side stops the timer.')
cadSysIpVideoInterDbcDelayTimer = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSysIpVideoInterDbcDelayTimer.setStatus('current')
if mibBuilder.loadTexts: cadSysIpVideoInterDbcDelayTimer.setDescription('This object specifies the time the C4 will wait after receiving a DBC-RSP from a single modem before the C4 launches the next DBC-REQ to that same modem.')
cadSysIpVideoMulticastControlled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSysIpVideoMulticastControlled.setStatus('current')
if mibBuilder.loadTexts: cadSysIpVideoMulticastControlled.setDescription('Indicates whether IP Multicast is subject to Admission Control. A value of true(1) indicates that all IP Multicast service flows are subjected to a CAC check.')
cadSysIpVideoMulticastAllowedUsage = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(20)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSysIpVideoMulticastAllowedUsage.setStatus('current')
if mibBuilder.loadTexts: cadSysIpVideoMulticastAllowedUsage.setDescription('Maximum percentage of downstream resources that may be admitted for use by Multicast services. Unlike other similar parameters in the cadPCMibBase section, this parameter is the actual limiting MIB parameter to be used across all downstream channels and is not just the default value for other MIB parameters. This value at all times must be less than or equal to 100% minus all default CAC downstream channel parameters that reserve resources for other applications (including, but not necessarily limited to, emergency and normal voice).')
cadIpVideoMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3))
cadIPVideoMonitorDropsTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1), )
if mibBuilder.loadTexts: cadIPVideoMonitorDropsTable.setStatus('current')
if mibBuilder.loadTexts: cadIPVideoMonitorDropsTable.setDescription('A circular table of historic drop counts for the downstream channels which transport IP Video streams within a DS-SG.')
cadIpVideoMonitorDropsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1), ).setIndexNames((0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorCardId"), (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorPortConnectorId"), (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorCurTimeIdx"))
if mibBuilder.loadTexts: cadIpVideoMonitorDropsEntry.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDropsEntry.setDescription('The drop counts for the downstream IP Video channels associated with a connector. The cadIpVideoMonitorCardId key is for the card that contains the connector. The cadIpVideoMonitorPortConnectorId indicates which downstream port the counts are for. The cadIpVideoMonitorCurTimeIdx is a sequence number.')
cadIpVideoMonitorCurTimeIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cadIpVideoMonitorCurTimeIdx.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorCurTimeIdx.setDescription('A unique index to identify a cadIpVideoMonitorDropsEntry. ')
cadIpVideoMonitorMulticastDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorMulticastDrops.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorMulticastDrops.setDescription('This object represents the total number of multicast packets dropped for DOCSIS IP video channels in the downstream service group over a one hour period.')
cadIpVideoMonitorUnicastDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorUnicastDrops.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorUnicastDrops.setDescription('This object represents the total number of multicast packets dropped for DOCSIS IP video channels in the downstream service group over a one hour period.')
cadIpVideoMonitorDropsSuspectFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorDropsSuspectFlag.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDropsSuspectFlag.setDescription('This object indicates that the rest of the data in this row is suspected to not correctly reflect the counts for the one-hour monitoring period. This condition might have been caused by any scenario which might have resulted in errant statistics (for example, a CAM failover).')
cadIpVideoMonitorCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorCreateTime.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorCreateTime.setDescription('This object indicates the time when the row is created.')
cadIpVideoMonitorCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 6), CardId())
if mibBuilder.loadTexts: cadIpVideoMonitorCardId.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorCardId.setDescription('The unique id of this card within the shelf.')
cadIpVideoMonitorPortConnectorId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 7), PortId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIpVideoMonitorPortConnectorId.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorPortConnectorId.setDescription(' For a DOCSIS or EQAM type port, this is the rear PIC connector.')
cadIpVideoMonitorDsChlTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2), )
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlTable.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlTable.setDescription('A circular table of historic drop counts for the downstream channels which transport IP Video streams within a DS-SG.')
cadIpVideoMonitorDsChlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorCurTimeIdx"))
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlEntry.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlEntry.setDescription('The drop counts for a DS-SG. The ifIndex key is for the downstream channel that carries IP Video service. The cadIpVideoMonitorDsChlCurTimeIdx is a sequence number.')
cadIpVideoMonitorDsChlCurTimeIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlCurTimeIdx.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlCurTimeIdx.setDescription('A unique index to identify a cadIpVideoMonitorDsChlEntry.')
cadIpVideoMonitorMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorMcastPkts.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorMcastPkts.setDescription('This object represents the total number of multicast IP Video packets transmitted for DOCSIS IP video channels in the downstream service group over a one hour period.')
cadIpVideoMonitorMcastFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorMcastFlows.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorMcastFlows.setDescription('This object represents the total number of multicast IP Video flows created over a one hour period.')
cadIpVideoMonitorUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorUcastPkts.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorUcastPkts.setDescription('This object represents the total number of unicast IP Video packets transmitted for DOCSIS IP video channels in the downstream service group over a one hour period.')
cadIpVideoMonitorUcastFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorUcastFlows.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorUcastFlows.setDescription('This object represents the total number of unicast IP Video flows created over a one hour period.')
cadIpVideoMonitorDsChlSuspectFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlSuspectFlag.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlSuspectFlag.setDescription('This object indicates that the rest of the data in this row is suspected to not correctly reflect the counts for the one-hour monitoring period. This condition might have been caused by any scenario which might have resulted in errant statistics (for example, a CAM failover).')
cadIpVideoMonitorDsChlCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlCreateTime.setStatus('current')
if mibBuilder.loadTexts: cadIpVideoMonitorDsChlCreateTime.setDescription('This object incicates when the row is created.')
mibBuilder.exportSymbols("CADANT-CMTS-IP-VIDEO-MIB", cadIpVideoMonitorMulticastDrops=cadIpVideoMonitorMulticastDrops, cadSysIpVideoAttributeMask=cadSysIpVideoAttributeMask, cadIpVideoMonitorDropsEntry=cadIpVideoMonitorDropsEntry, cadIpVideoMonitorMcastPkts=cadIpVideoMonitorMcastPkts, cadIpVideoMonitorDsChlSuspectFlag=cadIpVideoMonitorDsChlSuspectFlag, cadIpVideoMonitorDsChlCreateTime=cadIpVideoMonitorDsChlCreateTime, cadIpVideoMonitorDsChlTable=cadIpVideoMonitorDsChlTable, cadSysIpVideoVodThreshold=cadSysIpVideoVodThreshold, cadIpVideoMonitorMcastFlows=cadIpVideoMonitorMcastFlows, cadIpVideoMonitorCardId=cadIpVideoMonitorCardId, cadIpVideoMonitorUcastFlows=cadIpVideoMonitorUcastFlows, cadIpVideoMonitorUnicastDrops=cadIpVideoMonitorUnicastDrops, cadIpVideoMonitorDsChlCurTimeIdx=cadIpVideoMonitorDsChlCurTimeIdx, PYSNMP_MODULE_ID=cadCmtsIpVideoMib, cadIpVideoMonitorPortConnectorId=cadIpVideoMonitorPortConnectorId, cadIpVideoMonitorDsChlEntry=cadIpVideoMonitorDsChlEntry, cadIpVideoMonitorUcastPkts=cadIpVideoMonitorUcastPkts, cadIpVideoMonitor=cadIpVideoMonitor, cadSysIpVideoLinearThreshold=cadSysIpVideoLinearThreshold, cadSysIpVideoMulticastControlled=cadSysIpVideoMulticastControlled, cadIpVideoMonitorCreateTime=cadIpVideoMonitorCreateTime, cadIpVideoMonitorDropsSuspectFlag=cadIpVideoMonitorDropsSuspectFlag, cadSysIpVideoCfg=cadSysIpVideoCfg, cadIpVideoMonitorCurTimeIdx=cadIpVideoMonitorCurTimeIdx, cadCmtsIpVideoMib=cadCmtsIpVideoMib, cadSysIpVideoInterDbcDelayTimer=cadSysIpVideoInterDbcDelayTimer, cadSysIpVideoMulticastAllowedUsage=cadSysIpVideoMulticastAllowedUsage, cadIPVideoMonitorDropsTable=cadIPVideoMonitorDropsTable)
