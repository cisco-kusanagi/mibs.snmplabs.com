#
# PySNMP MIB module CNT241-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CNT241-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
cnt2Subagent, = mibBuilder.importSymbols("CNT2-MIB", "cnt2Subagent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, Integer32, Unsigned32, IpAddress, ObjectIdentity, NotificationType, Counter32, ModuleIdentity, MibIdentifier, NotificationType, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "NotificationType", "Counter32", "ModuleIdentity", "MibIdentifier", "NotificationType", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cnt2Sm = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 4, 1))
cnt2SmHw = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1))
cnt2SmSw = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2))
cnt2SmMsg = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3))
cnt2SmMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4))
cnt2SmHwTemperatureF = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwTemperatureF.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwTemperatureF.setDescription('The temperature in Farenheit of the node in the range (0..255). If/when the temperature transitions from below 113 degrees to above 113 degrees, a advisory trap will be sent. If/when the temperature transitions from below 131 degrees to above 131 degrees, a repair trap will be sent.')
cnt2SmHwTapeDriveState = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-present", 1), ("ok", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwTapeDriveState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwTapeDriveState.setDescription('The state of the DAT tape drive.')
cnt2SmHwCdRomDriveState = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-present", 1), ("ok", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwCdRomDriveState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCdRomDriveState.setDescription('The state of the CD drive.')
cnt2SmHwTapeMounted = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-applicable", 1), ("empty", 2), ("mounted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwTapeMounted.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwTapeMounted.setDescription('Indicates whether the DAT tape drive contains a tape.')
cnt2SmHwCdRomMounted = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-applicable", 1), ("empty", 2), ("mounted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwCdRomMounted.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCdRomMounted.setDescription('Indicates whether the CD drive contains a CD.')
cnt2SmHwServiceLed = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwServiceLed.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwServiceLed.setDescription('The state of the service LED.')
cnt2SmHwIplSwitch = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwIplSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwIplSwitch.setDescription('The state of the IPL switch.')
cnt2SmHwAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8), )
if mibBuilder.loadTexts: cnt2SmHwAdapterTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwAdapterTable.setDescription('List of adapters in the node.')
cnt2SmHwAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmHwAdapterIndex"))
if mibBuilder.loadTexts: cnt2SmHwAdapterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwAdapterEntry.setDescription('A adapter entry.')
cnt2SmHwAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwAdapterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwAdapterIndex.setDescription('The relative index of this adapter entry within the node.')
cnt2SmHwAdapterOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("not-ok", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwAdapterOperState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwAdapterOperState.setDescription('The state of the adapter in this slot.')
cnt2SmHwAdapterAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("reset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2SmHwAdapterAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwAdapterAdminState.setDescription('The state of the adapter in this slot.')
cnt2SmHwCardTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9), )
if mibBuilder.loadTexts: cnt2SmHwCardTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCardTable.setDescription('List of adapters in the node.')
cnt2SmHwCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmCardAdapterIndex"), (0, "CNT241-MIB", "cnt2SmHwCardIndex"))
if mibBuilder.loadTexts: cnt2SmHwCardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCardEntry.setDescription('A adapter entry.')
cnt2SmCardAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmCardAdapterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmCardAdapterIndex.setDescription('The relative index of this adapter entry within the node.')
cnt2SmHwCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwCardIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCardIndex.setDescription('The relative index of this adapter entry within the node.')
cnt2SmHwCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("not-ok", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwCardOperState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCardOperState.setDescription('The state of the adapter in this slot.')
cnt2SmHwCardAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("reset", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwCardAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwCardAdminState.setDescription('The state of the adapter in this slot.')
cnt2SmHwPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10), )
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyTable.setDescription('List of power supplies in the node.')
cnt2SmHwPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmHwPowerSupplyIndex"))
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyEntry.setDescription('A power supply entry.')
cnt2SmHwPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyIndex.setDescription('The relative index of this power supply entry within the node.')
cnt2SmHwPowerSupplyACState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("not-ok", 2), ("absent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyACState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyACState.setDescription('The AC state of this power supply.')
cnt2SmHwPowerSupplyDCState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("not-ok", 2), ("absent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyDCState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwPowerSupplyDCState.setDescription('The DC state of this power supply.')
cnt2SmHwFanTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11), )
if mibBuilder.loadTexts: cnt2SmHwFanTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwFanTable.setDescription('List of power supplies in the node.')
cnt2SmHwFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmHwFanIndex"))
if mibBuilder.loadTexts: cnt2SmHwFanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwFanEntry.setDescription('A fan entry.')
cnt2SmHwFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwFanIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwFanIndex.setDescription('The relative index of this fan entry within the node.')
cnt2SmHwFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("not-ok", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmHwFanState.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmHwFanState.setDescription('The state of this fan.')
cnt2SmNumModules = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmNumModules.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmNumModules.setDescription('The number of software modules making up the set referred to as the Service Monitor.')
cnt2SmSwTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2), )
if mibBuilder.loadTexts: cnt2SmSwTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwTable.setDescription('List of entries in the service monitor software module table.')
cnt2SmSwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmSwIndex"))
if mibBuilder.loadTexts: cnt2SmSwEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwEntry.setDescription('A service monitor software module entry.')
cnt2SmSwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwIndex.setDescription('The relative index of this software module entry within the service monitor.')
cnt2SmSwName = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwName.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwName.setDescription('The name of the service monitor module.')
cnt2SmSwFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("loading", 1), ("dumping", 2), ("configuration", 3), ("messages", 4), ("hw-monitoring", 5), ("tracing", 6), ("snmp-master-agent", 7), ("console", 8), ("utilities", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwFunction.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwFunction.setDescription('The primary function performed by this software module.')
cnt2SmSwMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwMajorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwMajorVersion.setDescription('The major version number of this software module.')
cnt2SmSwMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwMinorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwMinorVersion.setDescription('The minor version number of this software module.')
cnt2SmSwSlot = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwSlot.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwSlot.setDescription('The slot number of the active Service Monitor.')
cnt2SmSwAccess = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-write-access", 1), ("read-only-access", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmSwAccess.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmSwAccess.setDescription('The access permissions of the active Service Monitor.')
cnt2SmNumMsgs = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmNumMsgs.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmNumMsgs.setDescription('The number of messages in the system message file that have been entered by all modules within the node.')
cnt2SmMsgTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2), )
if mibBuilder.loadTexts: cnt2SmMsgTable.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgTable.setDescription('List of entries in the service monitor message file. This file contains any messages that has been entered by any software residing in the node.')
cnt2SmMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmMsgIndex"))
if mibBuilder.loadTexts: cnt2SmMsgEntry.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgEntry.setDescription('A message file entry.')
cnt2SmMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgIndex.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgIndex.setDescription('The relative index of this message entry within the message file.')
cnt2SmMsgSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 1), ("alert", 2), ("criticial", 3), ("error", 4), ("warning", 5), ("notice", 6), ("information", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgSeverity.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgSeverity.setDescription('The severity of this message.')
cnt2SmMsgProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgProcessName.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgProcessName.setDescription('The name of the process that sent this message to the message server.')
cnt2SmMsgNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgNumber.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgNumber.setDescription('The number of this message. Each module numbers its message type as another way of describing it. This message can then be cross-referenced in the CNT system messages reference manual.')
cnt2SmMsgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgSlotNumber.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgSlotNumber.setDescription('The slot number of the module that sent this message to the message server.')
cnt2SmMsgDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgDateTime.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgDateTime.setDescription('The date and time that this message was sent to the message server.')
cnt2SmMsgErrorNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgErrorNumber.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgErrorNumber.setDescription('The number of the Error message which caused us to generate this error message. Each module numbers its message errors as another way of describing it.')
cnt2SmMsgContent = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMsgContent.setStatus('deprecated')
if mibBuilder.loadTexts: cnt2SmMsgContent.setDescription('The textual detail of the message sent to the message server.')
cnt2SmMsgTableSize = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2SmMsgTableSize.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmMsgTableSize.setDescription('The number of messages that are available through SNMP access. This message table is limited to the most recent number messages specified by this object.')
cnt2SmMessageTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2), )
if mibBuilder.loadTexts: cnt2SmMessageTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmMessageTable.setDescription('List of entries in the service monitor message file. This file contains any messages that has been entered by any software residing in the node.')
cnt2SmMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2, 1), ).setIndexNames((0, "CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2SmMessageEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmMessageEntry.setDescription('A message file entry.')
cnt2SmMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMessageText.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmMessageText.setDescription('The textual detail of the message sent to the message server.')
cnt2SmMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2SmMessageIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmMessageIndex.setDescription('The textual index of the message sent to the message server.')
cnt2SmMsgToTrapFilter = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 1), ("alert", 2), ("criticial", 3), ("error", 4), ("warning", 5), ("notice", 6), ("information", 7), ("none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2SmMsgToTrapFilter.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2SmMsgToTrapFilter.setDescription('Messages in cnt2SmMessageTable can be sent as traps to selected destinations. However, the messages are filtered by severity before they are forwarded as traps. This object determines which of the messages are filtered. All messages with severity equal and lower in value than the value of this object are forwarded as traps. Severity levels range from 0 (lowest) to 7 (highest). A value of 0 would cause all messages to be forwarded as traps.')
cnt2smEmergencyMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,1)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smEmergencyMsg.setDescription('An emergency level trap (0) signifies that an event has occured which has rendered the system unusable. All modules and interfaces will be affected.')
cnt2smAlertMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,2)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smAlertMsg.setDescription('An Alert level trap (1) signifies that an event has occured which requires that immediate action be taken. The module will be affected.')
cnt2smCriticalMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,3)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smCriticalMsg.setDescription('A Critical level trap (1) signifies that an event has occured for which action should be taken. The module will be affected.')
cnt2smErrorMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,4)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smErrorMsg.setDescription('An Error level trap (3) signifies that an event has occured that has resulted in errors. The module will probably be affected.')
cnt2smWarningMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,5)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smWarningMsg.setDescription('A Warning level trap (4) signifies that an event has occured that may affect the module.')
cnt2smNoticeMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,6)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smNoticeMsg.setDescription('A Notice level trap (1) signifies that an event has occured that is normal but that has significance. The module should be unaffected')
cnt2smInfoMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,7)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smInfoMsg.setDescription('An Informaiton level trap (6) signifies that an event has occured that informational in severity and that the module will not be affected by this error.')
cnt2smDebugMsg = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,8)).setObjects(("CNT241-MIB", "cnt2SmMsgProcessName"), ("CNT241-MIB", "cnt2SmMsgNumber"), ("CNT241-MIB", "cnt2SmMsgSlotNumber"), ("CNT241-MIB", "cnt2SmMsgDateTime"), ("CNT241-MIB", "cnt2SmMsgErrorNumber"), ("CNT241-MIB", "cnt2SmMsgContent"))
if mibBuilder.loadTexts: cnt2smDebugMsg.setDescription('A Debug level trap (7) signifies that an event has occured at a debug level that is informational. The module will not be affected by this error.')
cnt2smEmergencyTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,9)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smEmergencyTrap.setDescription('An emergency level trap signifies that an event has occured which has rendered the system unusable. All modules and interfaces will be affected.')
cnt2smAlertTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,10)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smAlertTrap.setDescription('An Alert level trap signifies that an event has occured which requires that immediate action be taken. The module will be affected.')
cnt2smCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,11)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smCriticalTrap.setDescription('A Critical level trap signifies that an event has occured for which action should be taken. The module will be affected.')
cnt2smErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,12)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smErrorTrap.setDescription('An Error level trap signifies that an event has occured that has resulted in errors. The module will probably be affected.')
cnt2smWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,13)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smWarningTrap.setDescription('A Warning level trap signifies that an event has occured that may affect the module.')
cnt2smNoticeTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,14)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smNoticeTrap.setDescription('A Notice level trap signifies that an event has occured that is normal but that has significance. The module should be unaffected')
cnt2smInfoTrap = NotificationType((1, 3, 6, 1, 4, 1, 333, 2, 4, 1) + (0,15)).setObjects(("CNT241-MIB", "cnt2SmMessageText"))
if mibBuilder.loadTexts: cnt2smInfoTrap.setDescription('An Informaiton level trap signifies that an event has occured that informational in severity and that the module will not be affected by this error.')
mibBuilder.exportSymbols("CNT241-MIB", cnt2SmHwCardOperState=cnt2SmHwCardOperState, cnt2SmHwCardIndex=cnt2SmHwCardIndex, cnt2SmMessageTable=cnt2SmMessageTable, cnt2smWarningTrap=cnt2smWarningTrap, cnt2SmSwMajorVersion=cnt2SmSwMajorVersion, cnt2SmSwSlot=cnt2SmSwSlot, cnt2smAlertMsg=cnt2smAlertMsg, cnt2SmSwMinorVersion=cnt2SmSwMinorVersion, cnt2SmNumModules=cnt2SmNumModules, cnt2SmMessageEntry=cnt2SmMessageEntry, cnt2smNoticeTrap=cnt2smNoticeTrap, cnt2SmMsgErrorNumber=cnt2SmMsgErrorNumber, cnt2SmSwName=cnt2SmSwName, cnt2smEmergencyTrap=cnt2smEmergencyTrap, cnt2smCriticalMsg=cnt2smCriticalMsg, cnt2smInfoTrap=cnt2smInfoTrap, cnt2SmMsgToTrapFilter=cnt2SmMsgToTrapFilter, cnt2SmHwAdapterTable=cnt2SmHwAdapterTable, cnt2SmSwTable=cnt2SmSwTable, cnt2smNoticeMsg=cnt2smNoticeMsg, cnt2SmHwFanState=cnt2SmHwFanState, cnt2smAlertTrap=cnt2smAlertTrap, cnt2SmHwTapeMounted=cnt2SmHwTapeMounted, cnt2SmHwServiceLed=cnt2SmHwServiceLed, cnt2smEmergencyMsg=cnt2smEmergencyMsg, cnt2SmSw=cnt2SmSw, cnt2SmMsgProcessName=cnt2SmMsgProcessName, cnt2SmHwCardTable=cnt2SmHwCardTable, cnt2SmHwAdapterEntry=cnt2SmHwAdapterEntry, cnt2SmHwTapeDriveState=cnt2SmHwTapeDriveState, cnt2SmMsgTable=cnt2SmMsgTable, cnt2SmMsgNumber=cnt2SmMsgNumber, cnt2SmMsgSlotNumber=cnt2SmMsgSlotNumber, cnt2smErrorTrap=cnt2smErrorTrap, cnt2SmHwAdapterIndex=cnt2SmHwAdapterIndex, cnt2SmMsg=cnt2SmMsg, cnt2SmHwFanIndex=cnt2SmHwFanIndex, cnt2SmHwTemperatureF=cnt2SmHwTemperatureF, cnt2SmHwIplSwitch=cnt2SmHwIplSwitch, cnt2smErrorMsg=cnt2smErrorMsg, cnt2SmSwEntry=cnt2SmSwEntry, cnt2SmMessageIndex=cnt2SmMessageIndex, cnt2SmHwPowerSupplyTable=cnt2SmHwPowerSupplyTable, cnt2SmMessageText=cnt2SmMessageText, cnt2smWarningMsg=cnt2smWarningMsg, cnt2SmSwAccess=cnt2SmSwAccess, cnt2SmHwCdRomDriveState=cnt2SmHwCdRomDriveState, cnt2SmHwCardAdminState=cnt2SmHwCardAdminState, cnt2SmMsgDateTime=cnt2SmMsgDateTime, cnt2SmHw=cnt2SmHw, cnt2SmSwIndex=cnt2SmSwIndex, cnt2SmMsgTableSize=cnt2SmMsgTableSize, cnt2smDebugMsg=cnt2smDebugMsg, cnt2Sm=cnt2Sm, cnt2SmHwPowerSupplyDCState=cnt2SmHwPowerSupplyDCState, cnt2SmHwCardEntry=cnt2SmHwCardEntry, cnt2SmHwPowerSupplyACState=cnt2SmHwPowerSupplyACState, cnt2smInfoMsg=cnt2smInfoMsg, cnt2SmHwCdRomMounted=cnt2SmHwCdRomMounted, cnt2SmHwFanEntry=cnt2SmHwFanEntry, cnt2SmMsgEntry=cnt2SmMsgEntry, cnt2smCriticalTrap=cnt2smCriticalTrap, cnt2SmMsgSeverity=cnt2SmMsgSeverity, cnt2SmHwAdapterAdminState=cnt2SmHwAdapterAdminState, cnt2SmCardAdapterIndex=cnt2SmCardAdapterIndex, cnt2SmMessage=cnt2SmMessage, cnt2SmHwPowerSupplyEntry=cnt2SmHwPowerSupplyEntry, cnt2SmHwPowerSupplyIndex=cnt2SmHwPowerSupplyIndex, cnt2SmHwFanTable=cnt2SmHwFanTable, cnt2SmMsgIndex=cnt2SmMsgIndex, cnt2SmHwAdapterOperState=cnt2SmHwAdapterOperState, cnt2SmSwFunction=cnt2SmSwFunction, cnt2SmNumMsgs=cnt2SmNumMsgs, cnt2SmMsgContent=cnt2SmMsgContent)
