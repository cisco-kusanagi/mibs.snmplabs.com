#
# PySNMP MIB module CISCO-VIRTUAL-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIRTUAL-SWITCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Gauge32, ModuleIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, TimeTicks, iso, NotificationType, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "TimeTicks", "iso", "NotificationType", "Bits", "Unsigned32")
DisplayString, TextualConvention, RowStatus, DateAndTime, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "DateAndTime", "TimeStamp", "TruthValue")
ciscoVirtualSwitchMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 388))
ciscoVirtualSwitchMIB.setRevisions(('2015-03-04 00:00', '2012-04-10 00:00', '2010-01-21 00:00', '2007-09-25 00:00',))
if mibBuilder.loadTexts: ciscoVirtualSwitchMIB.setLastUpdated('201503040000Z')
if mibBuilder.loadTexts: ciscoVirtualSwitchMIB.setOrganization('Cisco Systems, Inc.')
ciscoVirtualSwitchMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 0))
ciscoVirtualSwitchMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 1))
ciscoVirtualSwitchMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 2))
class VSSwitchID(TextualConvention, Unsigned32):
    status = 'current'

class VSSwitchCapability(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("standalone", 0), ("core", 1))

class VSSwitchMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("standalone", 1), ("multiNode", 2))

class VSSwitchRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standalone", 1), ("active", 2), ("standby", 3))

class VSConnectStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

cvsGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1))
cvsChassisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2))
cvsVSLObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3))
cvsModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4))
cvsDualActiveDetection = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 5))
cvsDomain = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsDomain.setStatus('current')
cvsSwitchID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 2), VSSwitchID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsSwitchID.setStatus('current')
cvsSwitchCapability = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 3), VSSwitchCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsSwitchCapability.setStatus('current')
cvsSwitchMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 4), VSSwitchMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsSwitchMode.setStatus('current')
cvsSwitchConvertingStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsSwitchConvertingStatus.setStatus('current')
cvsVSLChangeNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsVSLChangeNotifEnable.setStatus('current')
cvsCoreSwitchConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1), )
if mibBuilder.loadTexts: cvsCoreSwitchConfigTable.setStatus('current')
cvsCoreSwitchConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchID"))
if mibBuilder.loadTexts: cvsCoreSwitchConfigEntry.setStatus('current')
cvsCoreSwitchID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 1), VSSwitchID())
if mibBuilder.loadTexts: cvsCoreSwitchID.setStatus('current')
cvsCoreSwitchPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsCoreSwitchPriority.setStatus('current')
cvsCoreSwitchPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsCoreSwitchPreempt.setStatus('current')
cvsCoreSwitchLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsCoreSwitchLocation.setStatus('current')
cvsChassisTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2), )
if mibBuilder.loadTexts: cvsChassisTable.setStatus('current')
cvsChassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cvsChassisEntry.setStatus('current')
cvsChassisSwitchID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1, 1), VSSwitchID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsChassisSwitchID.setStatus('current')
cvsChassisRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1, 2), VSSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsChassisRole.setStatus('current')
cvsChassisUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsChassisUpTime.setStatus('current')
cvsVSLConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1), )
if mibBuilder.loadTexts: cvsVSLConnectionTable.setStatus('current')
cvsVSLConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"))
if mibBuilder.loadTexts: cvsVSLConnectionEntry.setStatus('current')
cvsVSLChannelIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cvsVSLChannelIfindex.setStatus('current')
cvsVSLCoreSwitchID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 2), VSSwitchID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvsVSLCoreSwitchID.setStatus('current')
cvsVSLConnectOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 3), VSConnectStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLConnectOperStatus.setStatus('current')
cvsVSLLastConnectionStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLLastConnectionStateChange.setStatus('current')
cvsVSLConfiguredPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLConfiguredPortCount.setStatus('current')
cvsVSLOperationalPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLOperationalPortCount.setStatus('current')
cvsVSLConnectionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvsVSLConnectionRowStatus.setStatus('current')
cvsVSLStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2), )
if mibBuilder.loadTexts: cvsVSLStatsTable.setStatus('current')
cvsVSLStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"))
if mibBuilder.loadTexts: cvsVSLStatsEntry.setStatus('current')
cvsVSLTxTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxTotalPkts.setStatus('current')
cvsVSLTxErrorPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxErrorPkts.setStatus('current')
cvsVSLTxChksumErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxChksumErrPkts.setStatus('current')
cvsVSLRxTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxTotalPkts.setStatus('current')
cvsVSLRxErrorPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxErrorPkts.setStatus('current')
cvsVSLRxChksumErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxChksumErrPkts.setStatus('current')
cvsVSLTxLmpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxLmpPkts.setStatus('current')
cvsVSLTxRrpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxRrpPkts.setStatus('current')
cvsVSLTxPingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxPingPkts.setStatus('current')
cvsVSLTxProtoPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxProtoPkts.setStatus('current')
cvsVSLTxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxDataPkts.setStatus('current')
cvsVSLTxAckPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxAckPkts.setStatus('current')
cvsVSLRxLmpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxLmpPkts.setStatus('current')
cvsVSLRxRrpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxRrpPkts.setStatus('current')
cvsVSLRxPingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxPingPkts.setStatus('current')
cvsVSLRxProtoPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxProtoPkts.setStatus('current')
cvsVSLRxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxDataPkts.setStatus('current')
cvsVSLRxAckPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxAckPkts.setStatus('current')
cvsVSLTxTotalEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxTotalEobcPkts.setStatus('current')
cvsVSLTxLmpEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxLmpEobcPkts.setStatus('current')
cvsVSLTxRrpEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxRrpEobcPkts.setStatus('current')
cvsVSLTxPingEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxPingEobcPkts.setStatus('current')
cvsVSLTxProtoEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxProtoEobcPkts.setStatus('current')
cvsVSLTxDataEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxDataEobcPkts.setStatus('current')
cvsVSLTxAckEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxAckEobcPkts.setStatus('current')
cvsVSLRxTotalEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxTotalEobcPkts.setStatus('current')
cvsVSLRxLmpEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxLmpEobcPkts.setStatus('current')
cvsVSLRxRrpEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxRrpEobcPkts.setStatus('current')
cvsVSLRxPingEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxPingEobcPkts.setStatus('current')
cvsVSLRxProtoEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxProtoEobcPkts.setStatus('current')
cvsVSLRxDataEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxDataEobcPkts.setStatus('current')
cvsVSLRxAckEobcPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxAckEobcPkts.setStatus('current')
cvsVSLTxTotalHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxTotalHCPkts.setStatus('current')
cvsVSLTxErrorHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxErrorHCPkts.setStatus('current')
cvsVSLTxChksumErrHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLTxChksumErrHCPkts.setStatus('current')
cvsVSLRxTotalHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxTotalHCPkts.setStatus('current')
cvsVSLRxErrorHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxErrorHCPkts.setStatus('current')
cvsVSLRxChksumErrHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLRxChksumErrHCPkts.setStatus('current')
cvsVSLPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3), )
if mibBuilder.loadTexts: cvsVSLPortStatsTable.setStatus('current')
cvsVSLPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1), ).setIndexNames((0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"), (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortStatsIfindex"))
if mibBuilder.loadTexts: cvsVSLPortStatsEntry.setStatus('current')
cvsVSLPortStatsIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cvsVSLPortStatsIfindex.setStatus('current')
cvsVSLPortTxOkPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortTxOkPkts.setStatus('current')
cvsVSLPortTxFailPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortTxFailPkts.setStatus('current')
cvsVSLPortRxBidirPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxBidirPkts.setStatus('current')
cvsVSLPortRxUnidirPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxUnidirPkts.setStatus('current')
cvsVSLPortRxFailPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxFailPkts.setStatus('current')
cvsVSLPortRxBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxBadPkts.setStatus('current')
cvsVSLPortRxMyInfoMismatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxMyInfoMismatchPkts.setStatus('current')
cvsVSLPortRxMyInfoAbsentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxMyInfoAbsentPkts.setStatus('current')
cvsVSLPortRxBadMacAddressPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxBadMacAddressPkts.setStatus('current')
cvsVSLPortRxBadSwitchIdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxBadSwitchIdPkts.setStatus('current')
cvsVSLPortRxDomainIdMismatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxDomainIdMismatchPkts.setStatus('current')
cvsVSLPortRxPeerInfoMismatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLPortRxPeerInfoMismatchPkts.setStatus('current')
cvsVSLLinkPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 4), )
if mibBuilder.loadTexts: cvsVSLLinkPortTable.setStatus('current')
cvsVSLLinkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 4, 1), ).setIndexNames((0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"), (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortStatsIfindex"))
if mibBuilder.loadTexts: cvsVSLLinkPortEntry.setStatus('current')
cvsVSLLinkPeerInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 4, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsVSLLinkPeerInterface.setStatus('current')
cvsModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1), )
if mibBuilder.loadTexts: cvsModuleTable.setStatus('current')
cvsModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cvsModuleEntry.setStatus('current')
cvsModuleVSSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsModuleVSSupported.setStatus('current')
cvsModuleVSLCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsModuleVSLCapable.setStatus('current')
cvsModuleSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsModuleSlotNumber.setStatus('current')
cvsModuleRprWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("rprWarm", 2), ("cSSO", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvsModuleRprWarm.setStatus('current')
cvsDualActiveDetectionNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvsDualActiveDetectionNotifEnable.setStatus('current')
cvsDualActiveDetectionInformation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 5, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvsDualActiveDetectionInformation.setStatus('current')
cvsVSLConnectionChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 388, 0, 1)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectOperStatus"))
if mibBuilder.loadTexts: cvsVSLConnectionChangeNotif.setStatus('current')
cvsDualActiveDetectionNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 388, 0, 2)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchID"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionInformation"))
if mibBuilder.loadTexts: cvsDualActiveDetectionNotif.setStatus('current')
cvsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1))
cvsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2))
cvsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 1)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsGlobalGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsConnectionNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsMIBCompliance = cvsMIBCompliance.setStatus('deprecated')
cvsMIBComplianceV02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 2)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsGlobalGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVssModuleStandbyGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsConnectionNotifsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsMIBComplianceV02 = cvsMIBComplianceV02.setStatus('deprecated')
cvsMIBComplianceV03 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 3)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsGlobalGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVssModuleStandbyGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsConnectionNotifsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsExtGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchLocationGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifsControlGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifsInfoGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsMIBComplianceV03 = cvsMIBComplianceV03.setStatus('deprecated')
cvsMIBComplianceV04 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 4)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsGlobalGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVssModuleStandbyGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsConnectionNotifsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLStatisticsExtGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchLocationGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifsControlGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifsInfoGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifsGroup"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLLinkPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsMIBComplianceV04 = cvsMIBComplianceV04.setStatus('current')
cvsGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 1)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsDomain"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchID"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchCapability"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchMode"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchConvertingStatus"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChangeNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsGlobalGroup = cvsGlobalGroup.setStatus('current')
cvsCoreSwitchGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 2)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchPriority"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchPreempt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCoreSwitchGroup = cvsCoreSwitchGroup.setStatus('current')
cvsChassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 3)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisSwitchID"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisRole"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisUpTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsChassisGroup = cvsChassisGroup.setStatus('current')
cvsVSLConnectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 4)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLCoreSwitchID"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectOperStatus"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLLastConnectionStateChange"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConfiguredPortCount"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLOperationalPortCount"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsVSLConnectionGroup = cvsVSLConnectionGroup.setStatus('current')
cvsVSLStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 5)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxTotalPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxErrorPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxChksumErrPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxTotalPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxErrorPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxChksumErrPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortTxOkPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortTxFailPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBidirPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxUnidirPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxFailPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBadPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsVSLStatisticsGroup = cvsVSLStatisticsGroup.setStatus('current')
cvsModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 6)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleVSSupported"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleVSLCapable"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleSlotNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsModuleGroup = cvsModuleGroup.setStatus('current')
cvsConnectionNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 7)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsConnectionNotifsGroup = cvsConnectionNotifsGroup.setStatus('current')
cvsVSLStatisticsExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 8)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxLmpPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxRrpPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxPingPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxProtoPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxDataPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxAckPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxLmpPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxRrpPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxPingPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxProtoPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxDataPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxAckPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxTotalEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxLmpEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxRrpEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxPingEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxProtoEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxDataEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxAckEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxTotalEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxLmpEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxRrpEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxPingEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxProtoEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxDataEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxAckEobcPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxTotalHCPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxErrorHCPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxChksumErrHCPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxTotalHCPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxErrorHCPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxChksumErrHCPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxMyInfoMismatchPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxMyInfoAbsentPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBadMacAddressPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBadSwitchIdPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxDomainIdMismatchPkts"), ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxPeerInfoMismatchPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsVSLStatisticsExtGroup = cvsVSLStatisticsExtGroup.setStatus('current')
cvsVssModuleStandbyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 9)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleRprWarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsVssModuleStandbyGroup = cvsVssModuleStandbyGroup.setStatus('current')
cvsCoreSwitchLocationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 10)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchLocation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCoreSwitchLocationGroup = cvsCoreSwitchLocationGroup.setStatus('current')
cvsDualActiveDetectionNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 11)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsDualActiveDetectionNotifsControlGroup = cvsDualActiveDetectionNotifsControlGroup.setStatus('current')
cvsDualActiveDetectionNotifsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 12)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsDualActiveDetectionNotifsInfoGroup = cvsDualActiveDetectionNotifsInfoGroup.setStatus('current')
cvsDualActiveDetectionNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 13)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsDualActiveDetectionNotifsGroup = cvsDualActiveDetectionNotifsGroup.setStatus('current')
cvsVSLLinkPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 14)).setObjects(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLLinkPeerInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsVSLLinkPortGroup = cvsVSLLinkPortGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIRTUAL-SWITCH-MIB", cvsVSLTxChksumErrPkts=cvsVSLTxChksumErrPkts, cvsVSLTxErrorPkts=cvsVSLTxErrorPkts, cvsCoreSwitchLocationGroup=cvsCoreSwitchLocationGroup, PYSNMP_MODULE_ID=ciscoVirtualSwitchMIB, cvsDualActiveDetection=cvsDualActiveDetection, cvsVSLTxChksumErrHCPkts=cvsVSLTxChksumErrHCPkts, cvsVSLPortRxMyInfoAbsentPkts=cvsVSLPortRxMyInfoAbsentPkts, cvsVSLPortRxDomainIdMismatchPkts=cvsVSLPortRxDomainIdMismatchPkts, cvsVSLTxTotalHCPkts=cvsVSLTxTotalHCPkts, cvsVSLRxRrpEobcPkts=cvsVSLRxRrpEobcPkts, ciscoVirtualSwitchMIBObjects=ciscoVirtualSwitchMIBObjects, VSSwitchMode=VSSwitchMode, cvsVSLTxTotalPkts=cvsVSLTxTotalPkts, cvsVSLObjects=cvsVSLObjects, cvsDualActiveDetectionNotifsGroup=cvsDualActiveDetectionNotifsGroup, cvsCoreSwitchConfigEntry=cvsCoreSwitchConfigEntry, cvsGlobalGroup=cvsGlobalGroup, cvsSwitchConvertingStatus=cvsSwitchConvertingStatus, cvsDualActiveDetectionNotifsInfoGroup=cvsDualActiveDetectionNotifsInfoGroup, cvsVSLTxAckEobcPkts=cvsVSLTxAckEobcPkts, cvsSwitchCapability=cvsSwitchCapability, ciscoVirtualSwitchMIB=ciscoVirtualSwitchMIB, cvsVSLPortTxFailPkts=cvsVSLPortTxFailPkts, cvsDualActiveDetectionNotifsControlGroup=cvsDualActiveDetectionNotifsControlGroup, cvsVSLOperationalPortCount=cvsVSLOperationalPortCount, cvsVSLRxTotalPkts=cvsVSLRxTotalPkts, cvsVSLPortTxOkPkts=cvsVSLPortTxOkPkts, cvsModuleObjects=cvsModuleObjects, cvsVSLRxProtoPkts=cvsVSLRxProtoPkts, cvsCoreSwitchID=cvsCoreSwitchID, cvsMIBComplianceV04=cvsMIBComplianceV04, cvsSwitchMode=cvsSwitchMode, cvsVSLTxProtoPkts=cvsVSLTxProtoPkts, cvsVSLTxDataPkts=cvsVSLTxDataPkts, cvsVSLTxErrorHCPkts=cvsVSLTxErrorHCPkts, VSSwitchID=VSSwitchID, cvsVSLLastConnectionStateChange=cvsVSLLastConnectionStateChange, VSSwitchCapability=VSSwitchCapability, cvsVSLConnectionGroup=cvsVSLConnectionGroup, cvsVSLTxProtoEobcPkts=cvsVSLTxProtoEobcPkts, cvsModuleVSSupported=cvsModuleVSSupported, cvsChassisTable=cvsChassisTable, cvsVSLRxPingPkts=cvsVSLRxPingPkts, cvsVSLRxChksumErrHCPkts=cvsVSLRxChksumErrHCPkts, cvsVssModuleStandbyGroup=cvsVssModuleStandbyGroup, cvsVSLLinkPeerInterface=cvsVSLLinkPeerInterface, cvsVSLTxRrpPkts=cvsVSLTxRrpPkts, cvsVSLLinkPortGroup=cvsVSLLinkPortGroup, cvsDomain=cvsDomain, cvsVSLPortRxUnidirPkts=cvsVSLPortRxUnidirPkts, cvsVSLCoreSwitchID=cvsVSLCoreSwitchID, cvsVSLRxErrorHCPkts=cvsVSLRxErrorHCPkts, cvsCoreSwitchPreempt=cvsCoreSwitchPreempt, cvsDualActiveDetectionNotif=cvsDualActiveDetectionNotif, cvsModuleEntry=cvsModuleEntry, cvsCoreSwitchConfigTable=cvsCoreSwitchConfigTable, cvsVSLStatisticsGroup=cvsVSLStatisticsGroup, cvsVSLTxPingEobcPkts=cvsVSLTxPingEobcPkts, cvsVSLConnectionRowStatus=cvsVSLConnectionRowStatus, cvsVSLChangeNotifEnable=cvsVSLChangeNotifEnable, cvsVSLRxChksumErrPkts=cvsVSLRxChksumErrPkts, cvsVSLConnectOperStatus=cvsVSLConnectOperStatus, cvsVSLRxTotalEobcPkts=cvsVSLRxTotalEobcPkts, cvsChassisRole=cvsChassisRole, cvsChassisSwitchID=cvsChassisSwitchID, cvsVSLRxRrpPkts=cvsVSLRxRrpPkts, cvsVSLConnectionChangeNotif=cvsVSLConnectionChangeNotif, cvsVSLTxTotalEobcPkts=cvsVSLTxTotalEobcPkts, VSConnectStatus=VSConnectStatus, cvsSwitchID=cvsSwitchID, cvsCoreSwitchGroup=cvsCoreSwitchGroup, cvsVSLRxAckEobcPkts=cvsVSLRxAckEobcPkts, cvsVSLRxPingEobcPkts=cvsVSLRxPingEobcPkts, cvsVSLPortRxMyInfoMismatchPkts=cvsVSLPortRxMyInfoMismatchPkts, cvsVSLTxAckPkts=cvsVSLTxAckPkts, cvsModuleSlotNumber=cvsModuleSlotNumber, cvsVSLPortRxBidirPkts=cvsVSLPortRxBidirPkts, cvsCoreSwitchLocation=cvsCoreSwitchLocation, cvsVSLPortRxBadMacAddressPkts=cvsVSLPortRxBadMacAddressPkts, cvsVSLLinkPortTable=cvsVSLLinkPortTable, cvsDualActiveDetectionInformation=cvsDualActiveDetectionInformation, cvsVSLPortRxPeerInfoMismatchPkts=cvsVSLPortRxPeerInfoMismatchPkts, cvsDualActiveDetectionNotifEnable=cvsDualActiveDetectionNotifEnable, cvsVSLRxProtoEobcPkts=cvsVSLRxProtoEobcPkts, cvsVSLPortRxBadSwitchIdPkts=cvsVSLPortRxBadSwitchIdPkts, cvsVSLPortStatsTable=cvsVSLPortStatsTable, cvsVSLConfiguredPortCount=cvsVSLConfiguredPortCount, cvsModuleTable=cvsModuleTable, cvsMIBComplianceV02=cvsMIBComplianceV02, cvsMIBGroups=cvsMIBGroups, cvsVSLStatisticsExtGroup=cvsVSLStatisticsExtGroup, cvsVSLTxLmpPkts=cvsVSLTxLmpPkts, cvsVSLRxTotalHCPkts=cvsVSLRxTotalHCPkts, cvsVSLRxLmpEobcPkts=cvsVSLRxLmpEobcPkts, cvsVSLPortStatsEntry=cvsVSLPortStatsEntry, cvsVSLPortRxFailPkts=cvsVSLPortRxFailPkts, cvsVSLConnectionTable=cvsVSLConnectionTable, cvsVSLRxErrorPkts=cvsVSLRxErrorPkts, cvsConnectionNotifsGroup=cvsConnectionNotifsGroup, cvsModuleGroup=cvsModuleGroup, cvsVSLTxDataEobcPkts=cvsVSLTxDataEobcPkts, VSSwitchRole=VSSwitchRole, cvsVSLRxDataEobcPkts=cvsVSLRxDataEobcPkts, cvsVSLStatsEntry=cvsVSLStatsEntry, cvsVSLRxAckPkts=cvsVSLRxAckPkts, cvsChassisEntry=cvsChassisEntry, cvsVSLTxLmpEobcPkts=cvsVSLTxLmpEobcPkts, ciscoVirtualSwitchMIBConform=ciscoVirtualSwitchMIBConform, cvsChassisUpTime=cvsChassisUpTime, cvsVSLTxPingPkts=cvsVSLTxPingPkts, cvsGlobalObjects=cvsGlobalObjects, cvsVSLStatsTable=cvsVSLStatsTable, cvsVSLRxDataPkts=cvsVSLRxDataPkts, cvsVSLRxLmpPkts=cvsVSLRxLmpPkts, ciscoVirtualSwitchMIBNotifs=ciscoVirtualSwitchMIBNotifs, cvsMIBCompliance=cvsMIBCompliance, cvsVSLChannelIfindex=cvsVSLChannelIfindex, cvsModuleVSLCapable=cvsModuleVSLCapable, cvsMIBCompliances=cvsMIBCompliances, cvsModuleRprWarm=cvsModuleRprWarm, cvsVSLPortStatsIfindex=cvsVSLPortStatsIfindex, cvsVSLLinkPortEntry=cvsVSLLinkPortEntry, cvsChassisObjects=cvsChassisObjects, cvsCoreSwitchPriority=cvsCoreSwitchPriority, cvsMIBComplianceV03=cvsMIBComplianceV03, cvsChassisGroup=cvsChassisGroup, cvsVSLConnectionEntry=cvsVSLConnectionEntry, cvsVSLTxRrpEobcPkts=cvsVSLTxRrpEobcPkts, cvsVSLPortRxBadPkts=cvsVSLPortRxBadPkts)
