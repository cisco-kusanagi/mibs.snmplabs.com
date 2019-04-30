#
# PySNMP MIB module NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
noiOpenInterfaceModule, = mibBuilder.importSymbols("NOKIA-NE3S-REGISTRATION-MIB", "noiOpenInterfaceModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Gauge32, IpAddress, Counter32, Integer32, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Gauge32", "IpAddress", "Counter32", "Integer32", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Unsigned32", "Bits")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
noiSnmpAlarmIrpCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 1))
noiSnmpAlarmIrpCommon.setRevisions(('2002-11-01 00:00',))
if mibBuilder.loadTexts: noiSnmpAlarmIrpCommon.setLastUpdated('200211010000Z')
if mibBuilder.loadTexts: noiSnmpAlarmIrpCommon.setOrganization('Nokia Networks')
class NoiAcknowledgementState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("acknowledged", 1), ("unacknowledged", 2), ("indeterminate", 3))

class NoiAcknowledgementTime(DateAndTime):
    status = 'current'

class NoiAcknowledgementUserId(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 10)

class NoiAdditionalText(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class NoiAlarmId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NoiAlarmLogControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("logging", 1), ("flush", 2), ("suspend", 3))

class NoiAlarmLogCount(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NoiAlarmTableCount(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NoiAlarmText(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class NoiEventTime(DateAndTime):
    status = 'current'

class NoiEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("communicationsAlarm", 2), ("environmentalAlarm", 3), ("equipmentAlarm", 4), ("processingErrorAlarm", 10), ("qualityOfServiceAlarm", 11))

class NoiLogFullAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("wrap", 0), ("halt", 1))

class NoiNotificationId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NoiNotificationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noiAlarmNew", 1), ("noiAlarmCleared", 2), ("noiAlarmListRebuild", 3), ("noiAlarmListRebuildInitiated", 4), ("noiAlarmChanged", 5), ("noiAlarmAckStateChanged", 6))

class NoiPerceivedSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 0))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("cleared", 5), ("indeterminate", 0))

class NoiProbableCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 151, 152, 153, 154, 155, 156, 1000001, 1000002, 1000003, 1000005, 1000006, 1000007, 1000008, 1000010, 1000011, 1000013, 1000015, 1000016, 1000017, 1000021, 1000022, 1000023, 1000024, 1000025, 1000026, 1000027, 1000030, 1000032, 1000033, 1000034, 1000036, 1000039, 1000040, 1000042, 1000043, 1000044, 1000045, 1000046, 1000047, 1000048, 1000050, 1000051, 1000053, 1000054, 1000056, 1000057, 2000001, 2000002, 2000003, 2000004, 2000005, 2000006, 2000007, 2000008, 2000009, 2000010, 2000011, 2000012, 2000013, 2000014, 2000015, 2000016, 2000017, 2000018, 3000001, 3000002, 3000003, 3000004, 3000005, 30000056, 3000007, 3000008, 3000010, 3000011, 3000012, 3000013, 3000014, 3000015, 3000016, 3000017, 3000018, 3000019, 3000020, 3000021, 3000022, 3000023, 3000025, 3000026, 3000027, 3000028, 3000029, 3000030, 3000031, 3000032, 3000033, 3000035, 3000036, 3000037, 3000038, 3000039, 3000040, 3000041, 3000042, 3000043, 3000044, 3000045, 3000046, 3000047, 3000048, 3000049, 3000050, 3000051, 3000052, 3000061, 3000062, 3000063, 3000064, 3000065, 3000066, 3000067, 3000068, 3000069, 3000070, 3000071, 3000072, 3000073, 3000074))
    namedValues = NamedValues(("m3100Indeterminate", 0), ("m3100AlarmIndicationSignal", 1), ("m3100CallSetupFailure", 2), ("m3100DegradedSignal", 3), ("m3100FarEndReceiverFailure", 4), ("m3100FramingError", 5), ("m3100LossOfFrame", 6), ("m3100LossOfPointer", 7), ("m3100LossOfSignal", 8), ("m3100PayloadTypeMismatch", 9), ("m3100TransmissionError", 10), ("m3100RemoteAlarmInterface", 11), ("m3100ExcessiveBitErrorRate", 12), ("m3100PathTraceMismatch", 13), ("m3100Unavailable", 14), ("m3100SignalLabelMismatch", 15), ("m3100LossOfMultiFrame", 16), ("m3100BackPlaneFailure", 51), ("m3100DataSetProblem", 52), ("m3100EquipmentIdentifierDuplication", 53), ("m3100ExternalIfDeviceProblem", 54), ("m3100LineCardProblem", 55), ("m3100MultiplexerProblem", 56), ("m3100NeIdentifierDuplication", 57), ("m3100PowerProblem", 58), ("m3100ProcessorProblem", 59), ("m3100ProtectionPathFailure", 60), ("m3100ReceiverFailure", 61), ("m3100ReplaceableUnitMissing", 62), ("m3100ReplaceableUnitTypeMismatch", 63), ("m3100SynchronisationSourceMismatch", 64), ("m3100TerminalProblem", 65), ("m3100TimingProblem", 66), ("m3100TransmitterFailure", 67), ("m3100TrunkCardProblem", 68), ("m3100ReplaceableUnitProblem", 69), ("m3100AirCompressorFailure", 101), ("m3100AirConditioningFailure", 102), ("m3100AirDryerFailure", 103), ("m3100BatteryDischarging", 104), ("m3100BatteryFailure", 105), ("m3100CommercialPowerFailure", 106), ("m3100CoolingFanFailure", 107), ("m3100EngineFailure", 108), ("m3100FireDetectorFailure", 109), ("m3100FuseFailure", 110), ("m3100GeneratorFailure", 111), ("m3100LowBatteryThreshold", 112), ("m3100PumpFailure", 113), ("m3100RectifierFailure", 114), ("m3100RectifierHighVoltage", 115), ("m3100RectifierLowVoltage", 116), ("m3100VentilationSystemFailure", 117), ("m3100EnclosureDoorOpen", 118), ("m3100ExplosiveGas", 119), ("m3100Fire", 120), ("m3100Flood", 121), ("m3100HighHumidity", 122), ("m3100HighTemperature", 123), ("m3100HighWind", 124), ("m3100IceBuildUp", 125), ("m3100LowFuel", 127), ("m3100LowHumidity", 128), ("m3100LowCablePressure", 129), ("m3100LowTemperature", 130), ("m3100LowWater", 131), ("m3100Smoke", 132), ("m3100ToxicGas", 133), ("m3100StorageCapacityProblem", 151), ("m3100MemoryMismatch", 152), ("m3100CorruptData", 153), ("m3100OutOfCPUCycles", 154), ("m3100SoftwareEnvironmentProblem", 155), ("m3100SoftwareDownloadFailure", 156), ("x733AdapterError", 1000001), ("x733ApplicationSubsystemFailure", 1000002), ("x733BandwidthReduced", 1000003), ("x733CommunicationsProtocolError", 1000005), ("x733CommunicationsSubsystemFailure", 1000006), ("x733ConfigurationOrCustomizationError", 1000007), ("x733Congestion", 1000008), ("x733CpuCyclesLimitExceeded", 1000010), ("x733DataSetOrModemError", 1000011), ("x733DTEDCEInterfaceError", 1000013), ("x733EquipmentMalfunction", 1000015), ("x733ExcessiveVibration", 1000016), ("x733FileError", 1000017), ("x733HeatingOrVentilationOrCoolingSystemProblem", 1000021), ("x733HumidityUnacceptable", 1000022), ("x733InputOutputDeviceError", 1000023), ("x733InputDeviceError", 1000024), ("x733LANError", 1000025), ("x733LeakDetected", 1000026), ("x733LocalNodeTransmissionError", 1000027), ("x733MaterialSupplyExhausted", 1000030), ("x733OutOfMemory", 1000032), ("x733OuputDeviceError", 1000033), ("x733PerformanceDegraded", 1000034), ("x733PressureUnacceptable", 1000036), ("x733QueueSizeExceeded", 1000039), ("x733ReceiveFailure", 1000040), ("x733RemoteNodeTransmissionError", 1000042), ("x733ResourceAtOrNearingCapacity", 1000043), ("x733ResponseTimeExcessive", 1000044), ("x733RetransmissionRateExcessive", 1000045), ("x733SoftwareError", 1000046), ("x733SoftwareProgramAbnormallyTerminated", 1000047), ("x733SoftwareProgramError", 1000048), ("x733TemperatureUnacceptable", 1000050), ("x733ThresholdCrossed", 1000051), ("x733ToxicLeakDetected", 1000053), ("x733TransmitFailure", 1000054), ("x733UnderlyingResourceUnavailable", 1000056), ("x733VersionMismatch", 1000057), ("x736AuthenticationFailure", 2000001), ("x736BreachOfConfidentiality", 2000002), ("x736CableTamper", 2000003), ("x736DelayedInformation", 2000004), ("x736DenialOfService", 2000005), ("x736DuplicateInformation", 2000006), ("x736InformationMissing", 2000007), ("x736InformationModificationDetected", 2000008), ("x736InformationOutOfSequence", 2000009), ("x736IntrusionDetection", 2000010), ("x736KeyExpired", 2000011), ("x736NonRepudiationFailure", 2000012), ("x736OutOfHoursActivity", 2000013), ("x736OutOfService", 2000014), ("x736ProceduralError", 2000015), ("x736UnauthorizedAccessAttempt", 2000016), ("x736UnexpectedInformation", 2000017), ("x736UnspecifiedReason", 2000018), ("gsm1211AbisToBTSInterfaceFailure", 3000001), ("gsm1211AbisToTRXInterfaceFailure", 3000002), ("gsm1211AntennaProblem", 3000003), ("gsm1211BatteryBreakdown", 3000004), ("gsm1211BatteryChargingFault", 3000005), ("gsm1211ClockSynchronisationProblem", 30000056), ("gsm1211CombinerProblem", 3000007), ("gsm1211DiskProblem", 3000008), ("gsm1211ExcessiveReceiverTemperature", 3000010), ("gsm1211ExcessiveTransmitterOutputPower", 3000011), ("gsm1211ExcessiveTransmitterTemperature", 3000012), ("gsm1211FrequencyHoppingDegraded", 3000013), ("gsm1211FrequencyHoppingFailure", 3000014), ("gsm1211FrequencyRedefinitionFailed", 3000015), ("gsm1211LineInterfaceFailure", 3000016), ("gsm1211LinkFailure", 3000017), ("gsm1211LossOfSynchronisation", 3000018), ("gsm1211LostRedundancy", 3000019), ("gsm1211MainsBreakdownWithBatteryBackUp", 3000020), ("gsm1211MainsBreakdownWithoutBatteryBackUp", 3000021), ("gsm1211PowerSupplyFailure", 3000022), ("gsm1211ReceiverAntennaFault", 3000023), ("gsm1211ReceiverMulticouplerFailure", 3000025), ("gsm1211ReducedTransmitterOutputPower", 3000026), ("gsm1211SignalQualityEvaluationFault", 3000027), ("gsm1211TimeslotHardwareFailure", 3000028), ("gsm1211TransceiverProblem", 3000029), ("gsm1211TranscoderProblem", 3000030), ("gsm1211TranscoderOrRateAdapterProblem", 3000031), ("gsm1211TransmitterAntennaFailure", 3000032), ("gsm1211TransmitterAntennaNotAdjusted", 3000033), ("gsm1211TransmitterLowVoltageOrCurrent", 3000035), ("gsm1211TransmitterOffFrequency", 3000036), ("gsm1211DatabaseInconsistency", 3000037), ("gsm1211FileSystemCallUnsuccessful", 3000038), ("gsm1211InputParameterOutOfRange", 3000039), ("gsm1211InvalidParameter", 3000040), ("gsm1211InvalidPointer", 3000041), ("gsm1211MessageNotExpected", 3000042), ("gsm1211MessageNotInitialised", 3000043), ("gsm1211MessageOutOfSequence", 3000044), ("gsm1211SystemCallUnsuccessful", 3000045), ("gsm1211TimeoutExpired", 3000046), ("gsm1211VariableOutOfRange", 3000047), ("gsm1211WatchDogTimerExpired", 3000048), ("gsm1211CoolingSystemFailure", 3000049), ("gsm1211ExternalEquipmentFailure", 3000050), ("gsm1211ExternalPowerSupplyFailure", 3000051), ("gsm1211ExternalTransmissionDeviceFailure", 3000052), ("gsm1211ReducedAlarmReporting", 3000061), ("gsm1211ReducedEventReporting", 3000062), ("gsm1211ReducedLoggingCapability", 3000063), ("gsm1211SystemResourcesOverload", 3000064), ("gsm1211BroadcastChannelFailure", 3000065), ("gsm1211ConnectionEstablishmentError", 3000066), ("gsm1211InvalidMessageReceived", 3000067), ("gsm1211InvalidMSUReceived", 3000068), ("gsm1211LAPDLinkProtocolFailure", 3000069), ("gsm1211LocalAlarmIndication", 3000070), ("gsm1211RemoteAlarmIndication", 3000071), ("gsm1211RoutingFailure", 3000072), ("gsm1211SS7ProtocolFailure", 3000073), ("gsm1211TransmissionError", 3000074))

class NoiSpecificProblem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99999)

class NoiSystemDistinguishedName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 160)

mibBuilder.exportSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION", NoiEventTime=NoiEventTime, NoiAlarmLogControl=NoiAlarmLogControl, NoiAlarmText=NoiAlarmText, NoiLogFullAction=NoiLogFullAction, NoiNotificationType=NoiNotificationType, NoiSpecificProblem=NoiSpecificProblem, PYSNMP_MODULE_ID=noiSnmpAlarmIrpCommon, NoiPerceivedSeverity=NoiPerceivedSeverity, NoiEventType=NoiEventType, NoiAlarmLogCount=NoiAlarmLogCount, NoiSystemDistinguishedName=NoiSystemDistinguishedName, NoiNotificationId=NoiNotificationId, NoiAcknowledgementTime=NoiAcknowledgementTime, NoiAdditionalText=NoiAdditionalText, noiSnmpAlarmIrpCommon=noiSnmpAlarmIrpCommon, NoiAcknowledgementUserId=NoiAcknowledgementUserId, NoiAlarmTableCount=NoiAlarmTableCount, NoiProbableCause=NoiProbableCause, NoiAcknowledgementState=NoiAcknowledgementState, NoiAlarmId=NoiAlarmId)
