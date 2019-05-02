#
# PySNMP MIB module PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PFC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:40:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, NotificationType, iso, ModuleIdentity, TimeTicks, MibIdentifier, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Counter64", "Counter32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
pfc = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 47))
if mibBuilder.loadTexts: pfc.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: pfc.setOrganization('QCI')
if mibBuilder.loadTexts: pfc.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: strong.chen@quantatw.com')
if mibBuilder.loadTexts: pfc.setDescription('The MIB definitions Priority based Flow Control Feature.')
agentPfcCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1))
agentPfcTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1), )
if mibBuilder.loadTexts: agentPfcTable.setStatus('current')
if mibBuilder.loadTexts: agentPfcTable.setDescription('A table providing configuration of PFC Profile per interface.')
agentPfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1), ).setIndexNames((0, "PFC-MIB", "agentPfcIntfIndex"))
if mibBuilder.loadTexts: agentPfcEntry.setStatus('current')
if mibBuilder.loadTexts: agentPfcEntry.setDescription('PFC Profile configuration for a port.')
agentPfcIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: agentPfcIntfIndex.setStatus('current')
if mibBuilder.loadTexts: agentPfcIntfIndex.setDescription('This is a unique index for an entry in the agentPfcTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable.')
agentPfcIntfAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("auto", 3))).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPfcIntfAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentPfcIntfAdminMode.setDescription('Enables/disables PFC profile on an interface.')
agentPfcIntfPfcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcStatus.setStatus('current')
if mibBuilder.loadTexts: agentPfcIntfPfcStatus.setDescription('Shows the operational-status of PFC on an interface.')
agentPfcTotalIntfPfcFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesRx.setStatus('current')
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesRx.setDescription('Total Received PFC Frames on this interface.')
agentPfcTotalIntfPfcFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesTx.setStatus('current')
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesTx.setDescription('Total Transmitted PFC Frames on this interface.')
agentPfcActionTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2), )
if mibBuilder.loadTexts: agentPfcActionTable.setStatus('current')
if mibBuilder.loadTexts: agentPfcActionTable.setDescription('A table providing priority and action mappings configuration of PFC.')
agentPfcActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2, 1), ).setIndexNames((0, "PFC-MIB", "agentPfcIntfIndex"), (0, "PFC-MIB", "agentPfcPriority"))
if mibBuilder.loadTexts: agentPfcActionEntry.setStatus('current')
if mibBuilder.loadTexts: agentPfcActionEntry.setDescription('PFC Action Profile configuration for a port.')
agentPfcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: agentPfcPriority.setStatus('current')
if mibBuilder.loadTexts: agentPfcPriority.setDescription('This is a unique index for an entry in the agentPfcActionTable. A non-zero value indicates the CosQueue Priority.')
agentPfcAction = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("nodrop", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPfcAction.setStatus('current')
if mibBuilder.loadTexts: agentPfcAction.setDescription('Set Drop/No-Drop action in PFC profile for the corresponding priority.')
agentPfcIntfStatsPerPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 3), )
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityTable.setStatus('current')
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityTable.setDescription('A table providing statistics of PFC per interface per priority.')
agentPfcIntfStatsPerPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 3, 1), ).setIndexNames((0, "PFC-MIB", "agentPfcIntfIndex"), (0, "PFC-MIB", "agentPfcPriority"))
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityEntry.setStatus('current')
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityEntry.setDescription('PFC Stats for a priority and for a port.')
agentPfcIntfPfcPriorityFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcPriorityFramesRx.setStatus('current')
if mibBuilder.loadTexts: agentPfcIntfPfcPriorityFramesRx.setDescription('Received PFC Frames on this interface for a priority.')
mibBuilder.exportSymbols("PFC-MIB", agentPfcIntfPfcPriorityFramesRx=agentPfcIntfPfcPriorityFramesRx, agentPfcIntfIndex=agentPfcIntfIndex, agentPfcIntfAdminMode=agentPfcIntfAdminMode, pfc=pfc, agentPfcAction=agentPfcAction, agentPfcTable=agentPfcTable, agentPfcIntfStatsPerPriorityTable=agentPfcIntfStatsPerPriorityTable, agentPfcEntry=agentPfcEntry, agentPfcTotalIntfPfcFramesTx=agentPfcTotalIntfPfcFramesTx, agentPfcActionEntry=agentPfcActionEntry, agentPfcIntfPfcStatus=agentPfcIntfPfcStatus, agentPfcTotalIntfPfcFramesRx=agentPfcTotalIntfPfcFramesRx, agentPfcPriority=agentPfcPriority, agentPfcIntfStatsPerPriorityEntry=agentPfcIntfStatsPerPriorityEntry, PYSNMP_MODULE_ID=pfc, agentPfcCfgGroup=agentPfcCfgGroup, agentPfcActionTable=agentPfcActionTable)
