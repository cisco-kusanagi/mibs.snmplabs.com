#
# PySNMP MIB module RETIX-METROLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RETIX-METROLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:56:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
DisplayString, = mibBuilder.importSymbols("RFC1155-SMI", "DisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, Gauge32, Integer32, mib_2, NotificationType, iso, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Bits, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "Integer32", "mib-2", "NotificationType", "iso", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Bits", "Counter32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
retix = MibIdentifier((1, 3, 6, 1, 4, 1, 72))
metroLanDS3ATM = MibIdentifier((1, 3, 6, 1, 2, 1, 37))
metroLanSS = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20))
atmBandwithGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1))
atmLogicalPort = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 2))
ds3FrameDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 3))
ssUnitProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 1))
ssBaseUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 2))
ssStakBus = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 3))
ssVirtualLan = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 4))
ssSlip = MibIdentifier((1, 3, 6, 1, 4, 1, 72, 20, 5))
atmBWGBandwidth = MibScalar((1, 3, 6, 1, 2, 1, 37, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmBWGBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: atmBWGBandwidth.setDescription('The bandwidth amount (in Kbps) assigned to a specific bandwidth group. Total bandwidth for all eight groups can not exceed the maximum, which is 36880.')
atmBWGConfig = MibScalar((1, 3, 6, 1, 2, 1, 37, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("go", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: atmBWGConfig.setStatus('mandatory')
if mibBuilder.loadTexts: atmBWGConfig.setDescription('this carry out the actual SET of the bandwidth group. a SYSTEM RESET will be executed for the changes in bandwidth group to take effect.')
atmRX_VCI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(35, 1023))).setLabel("atmRX-VCI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRX_VCI.setStatus('mandatory')
if mibBuilder.loadTexts: atmRX_VCI.setDescription('Receive VCI #. can be set as the same as atmTX-VCI')
atmRX_VPI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setLabel("atmRX-VPI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmRX_VPI.setStatus('mandatory')
if mibBuilder.loadTexts: atmRX_VPI.setDescription('Receive VPI #. can be set as the same as atmTX-VPI')
atmTX_VCI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(35, 1023))).setLabel("atmTX-VCI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmTX_VCI.setStatus('mandatory')
if mibBuilder.loadTexts: atmTX_VCI.setDescription('Transmit VCI #. choose a unique number for each ATM logical port.')
atmTX_VPI = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setLabel("atmTX-VPI").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmTX_VPI.setStatus('mandatory')
if mibBuilder.loadTexts: atmTX_VPI.setDescription('Transmit VPI #.')
atmBWG = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmBWG.setStatus('mandatory')
if mibBuilder.loadTexts: atmBWG.setDescription('Bandwidth group number. That paticular bandwidthgroup must be configured with a positive bandwidth')
atmEncaps = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 7))).clone(namedValues=NamedValues(("vcBridged8023", 2), ("llcEncaps", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmEncaps.setStatus('mandatory')
if mibBuilder.loadTexts: atmEncaps.setDescription('Encapsulation')
atmPortConfig = MibScalar((1, 3, 6, 1, 2, 1, 37, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortConfig.setStatus('mandatory')
if mibBuilder.loadTexts: atmPortConfig.setDescription('this carry out the actual SET of the logical port. 0 deletes the existing port, 1 creates a new logical port')
ds3NoSignalCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3NoSignalCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3NoSignalCntr.setDescription('NoSignalCntr stat')
ds3NoDS3FrameCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3NoDS3FrameCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3NoDS3FrameCntr.setDescription('NoDS3FrameCntr stat')
ds3AISDetectCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AISDetectCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3AISDetectCntr.setDescription('AISDetectCntr stat')
ds3YellowAlarmCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3YellowAlarmCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3YellowAlarmCntr.setDescription('YellowAlarmCntr stat')
ds3FErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FErrCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3FErrCntr.setDescription('FErrCntr stat')
ds3PErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3PErrCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3PErrCntr.setDescription('PErrCntr stat')
ds3CPErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CPErrCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3CPErrCntr.setDescription('CPErrCntr stat')
ds3FEBlockErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FEBlockErrCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3FEBlockErrCntr.setDescription('FEBlockErrCntr stat')
ds3BPVErrCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3BPVErrCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3BPVErrCntr.setDescription('BPVErrCntr stat')
ds3ATMOCD = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ATMOCD.setStatus('mandatory')
if mibBuilder.loadTexts: ds3ATMOCD.setDescription('ATMOCD stat')
ds3FIFOOverflow = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FIFOOverflow.setStatus('mandatory')
if mibBuilder.loadTexts: ds3FIFOOverflow.setDescription('FIFOOverflow stat')
ds3RAI = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3RAI.setStatus('mandatory')
if mibBuilder.loadTexts: ds3RAI.setDescription('RAI stat')
ds3RAICntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3RAICntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3RAICntr.setDescription('RAICntr stat')
ds3SignalLoss = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3SignalLoss.setStatus('mandatory')
if mibBuilder.loadTexts: ds3SignalLoss.setDescription('SignalLoss stat')
ds3FrameLoss = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3FrameLoss.setStatus('mandatory')
if mibBuilder.loadTexts: ds3FrameLoss.setDescription('FrameLoss stat')
ds3SyncLoss = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3SyncLoss.setStatus('mandatory')
if mibBuilder.loadTexts: ds3SyncLoss.setDescription('SyncLoss stat')
ds3YellowAlarm = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3YellowAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: ds3YellowAlarm.setDescription('YellowAlarm stat')
ds3AISDetect = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3AISDetect.setStatus('mandatory')
if mibBuilder.loadTexts: ds3AISDetect.setDescription('AISDetect stat')
ds3ClearErrorCntr = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("set", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: ds3ClearErrorCntr.setStatus('mandatory')
if mibBuilder.loadTexts: ds3ClearErrorCntr.setDescription(' SET this object will clear the Error Counters.')
ds3GFCInsertion = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3GFCInsertion.setStatus('mandatory')
if mibBuilder.loadTexts: ds3GFCInsertion.setDescription('Insertion of GFC bits ')
ds3BipolarSerialIO = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3BipolarSerialIO.setStatus('mandatory')
if mibBuilder.loadTexts: ds3BipolarSerialIO.setDescription('Bipolar serial IO')
ds3PayloadScrambling = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PayloadScrambling.setStatus('mandatory')
if mibBuilder.loadTexts: ds3PayloadScrambling.setDescription('Payload scrambling')
ds3PLCPOverheadProc = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3PLCPOverheadProc.setStatus('mandatory')
if mibBuilder.loadTexts: ds3PLCPOverheadProc.setDescription('PLCP overhead processing')
ds3FEBEGeneration = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3FEBEGeneration.setStatus('mandatory')
if mibBuilder.loadTexts: ds3FEBEGeneration.setDescription('FEBE error generation')
ds3LoopBack = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3LoopBack.setStatus('mandatory')
if mibBuilder.loadTexts: ds3LoopBack.setDescription('LoopBack Mode ')
ds3FEACGenNDetect = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 26), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3FEACGenNDetect.setStatus('mandatory')
if mibBuilder.loadTexts: ds3FEACGenNDetect.setDescription('FEAC generation/detection')
ds3RcvEQ = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3RcvEQ.setStatus('mandatory')
if mibBuilder.loadTexts: ds3RcvEQ.setDescription('Use internal receive equalizer')
ds3XmitLevel = MibScalar((1, 3, 6, 1, 2, 1, 37, 3, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds3XmitLevel.setStatus('mandatory')
if mibBuilder.loadTexts: ds3XmitLevel.setDescription(' transmit level: use normal (low) or long (high) cables')
ssBaseModule = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBaseModule.setStatus('mandatory')
if mibBuilder.loadTexts: ssBaseModule.setDescription('Identifies the type of main board card type')
ssIO1Module = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vacant", 1), ("pcnet-6-card-id", 2), ("feast-card-id", 3), ("stakBus-card-id", 4), ("atm-card-id", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIO1Module.setStatus('mandatory')
if mibBuilder.loadTexts: ssIO1Module.setDescription('I/O 1 card type')
ssIO2Module = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vacant", 1), ("pcnet-6-card-id", 2), ("feast-card-id", 3), ("stakBus-card-id", 4), ("atm-card-id", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIO2Module.setStatus('mandatory')
if mibBuilder.loadTexts: ssIO2Module.setDescription('I/O 2 card type')
ssBaseBootFWVer = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBaseBootFWVer.setStatus('mandatory')
if mibBuilder.loadTexts: ssBaseBootFWVer.setDescription('Version number of current boot firmware')
ssBaseSoftVer = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBaseSoftVer.setStatus('mandatory')
if mibBuilder.loadTexts: ssBaseSoftVer.setDescription('Version number of current software')
ssErrorLog = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssErrorLog.setStatus('mandatory')
if mibBuilder.loadTexts: ssErrorLog.setDescription('A stored value indicating that the unit has experienced a fault. Log information is formatted as a four digit hex number. Set to zero to clear the logged fault. Record this value and call Retix technical support.')
ssStkBusIOPort = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on-IO1", 1), ("on-IO2", 2), ("not-installed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusIOPort.setStatus('mandatory')
if mibBuilder.loadTexts: ssStkBusIOPort.setDescription('which I/O port is StakBus installed. (only 1 stakbus per system is allowed)')
ssStkBusSpeed = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: ssStkBusSpeed.setDescription('StakBus speed. 175000000, or 0 if no StakBus card installed')
ssStkBusNodeAddr = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusNodeAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ssStkBusNodeAddr.setDescription('Module ID for StakBus card')
ssStkBusRingOp = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ringOperational", 1), ("ringNotOperational", 2), ("notInstalled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssStkBusRingOp.setStatus('mandatory')
if mibBuilder.loadTexts: ssStkBusRingOp.setDescription('StakBus Ring OperationalStatus')
ssVLANEnDisable = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEnDisable.setStatus('mandatory')
if mibBuilder.loadTexts: ssVLANEnDisable.setDescription('Globally enable/disable VLAN for the system')
portVLANTable = MibTable((1, 3, 6, 1, 4, 1, 72, 20, 4, 2), )
if mibBuilder.loadTexts: portVLANTable.setStatus('mandatory')
if mibBuilder.loadTexts: portVLANTable.setDescription('Table of port based VLAN configurations. Entries (rows) are added to the table by issuing a SET command with the EnableAdd value for the portVLANEntryEdit object. The new row is created using the instantiations.')
portVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1), ).setIndexNames((0, "RETIX-METROLAN-MIB", "ssVLANEntryPortID"), (0, "RETIX-METROLAN-MIB", "ssVLANEntryVLANID"))
if mibBuilder.loadTexts: portVLANEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portVLANEntry.setDescription('a VLAN entry containing portID, VLANID, ...')
ssVLANEntryPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEntryPortID.setStatus('mandatory')
if mibBuilder.loadTexts: ssVLANEntryPortID.setDescription('Port ID')
ssVLANEntryVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEntryVLANID.setStatus('mandatory')
if mibBuilder.loadTexts: ssVLANEntryVLANID.setDescription('Vlan ID')
ssVLANEntryEdit = MibTableColumn((1, 3, 6, 1, 4, 1, 72, 20, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable-add", 1), ("disable", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssVLANEntryEdit.setStatus('mandatory')
if mibBuilder.loadTexts: ssVLANEntryEdit.setDescription('When set to enableAdd(1) the instantiations will be used to create a new table entry (row). Existing entries can be disabled(2) or deleted (3).')
slipEnable = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 5, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slipEnable.setStatus('mandatory')
if mibBuilder.loadTexts: slipEnable.setDescription('enable/disable SLIP')
slipHostIP = MibScalar((1, 3, 6, 1, 4, 1, 72, 20, 5, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slipHostIP.setStatus('mandatory')
if mibBuilder.loadTexts: slipHostIP.setDescription('SLIP Remote IP Addr')
mibBuilder.exportSymbols("RETIX-METROLAN-MIB", portVLANEntry=portVLANEntry, ds3FEACGenNDetect=ds3FEACGenNDetect, ds3SyncLoss=ds3SyncLoss, metroLanDS3ATM=metroLanDS3ATM, ds3RcvEQ=ds3RcvEQ, ssBaseUnit=ssBaseUnit, ds3NoSignalCntr=ds3NoSignalCntr, ds3BipolarSerialIO=ds3BipolarSerialIO, atmRX_VPI=atmRX_VPI, ssErrorLog=ssErrorLog, ds3ATMOCD=ds3ATMOCD, atmPortConfig=atmPortConfig, ssStkBusSpeed=ssStkBusSpeed, ssVLANEnDisable=ssVLANEnDisable, ds3XmitLevel=ds3XmitLevel, ssUnitProfile=ssUnitProfile, ds3RAICntr=ds3RAICntr, atmTX_VCI=atmTX_VCI, ssBaseBootFWVer=ssBaseBootFWVer, ssVLANEntryPortID=ssVLANEntryPortID, ds3FEBEGeneration=ds3FEBEGeneration, atmEncaps=atmEncaps, ds3PayloadScrambling=ds3PayloadScrambling, metroLanSS=metroLanSS, ds3FrameDevice=ds3FrameDevice, ds3PErrCntr=ds3PErrCntr, ssVLANEntryEdit=ssVLANEntryEdit, ssSlip=ssSlip, atmLogicalPort=atmLogicalPort, ds3FEBlockErrCntr=ds3FEBlockErrCntr, atmTX_VPI=atmTX_VPI, slipHostIP=slipHostIP, ds3LoopBack=ds3LoopBack, slipEnable=slipEnable, ds3NoDS3FrameCntr=ds3NoDS3FrameCntr, ssBaseSoftVer=ssBaseSoftVer, ds3FrameLoss=ds3FrameLoss, ssStkBusRingOp=ssStkBusRingOp, ds3GFCInsertion=ds3GFCInsertion, atmBWGConfig=atmBWGConfig, ds3YellowAlarm=ds3YellowAlarm, ssStkBusNodeAddr=ssStkBusNodeAddr, ssVLANEntryVLANID=ssVLANEntryVLANID, ds3RAI=ds3RAI, atmBandwithGroup=atmBandwithGroup, ssStakBus=ssStakBus, ds3CPErrCntr=ds3CPErrCntr, ds3FIFOOverflow=ds3FIFOOverflow, ds3AISDetect=ds3AISDetect, ssVirtualLan=ssVirtualLan, ds3AISDetectCntr=ds3AISDetectCntr, ssStkBusIOPort=ssStkBusIOPort, retix=retix, ssIO1Module=ssIO1Module, ds3PLCPOverheadProc=ds3PLCPOverheadProc, portVLANTable=portVLANTable, ssBaseModule=ssBaseModule, ds3ClearErrorCntr=ds3ClearErrorCntr, atmBWG=atmBWG, atmBWGBandwidth=atmBWGBandwidth, ds3YellowAlarmCntr=ds3YellowAlarmCntr, ssIO2Module=ssIO2Module, ds3SignalLoss=ds3SignalLoss, ds3FErrCntr=ds3FErrCntr, atmRX_VCI=atmRX_VCI, ds3BPVErrCntr=ds3BPVErrCntr)
