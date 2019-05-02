#
# PySNMP MIB module ERICSSON-ALARM-IRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERICSSON-ALARM-IRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Integer32, ModuleIdentity, Counter32, IpAddress, ObjectIdentity, TimeTicks, Bits, Counter64, NotificationType, Gauge32, iso, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ModuleIdentity", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "Bits", "Counter64", "NotificationType", "Gauge32", "iso", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
alarmIrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3881, 2))
alarmIrpMIB.setRevisions(('2004-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alarmIrpMIB.setRevisionsDescriptions(('Specification of alarmId MAX-ACCESS corrected by TSP Node Management.',))
if mibBuilder.loadTexts: alarmIrpMIB.setLastUpdated('200409030000Z')
if mibBuilder.loadTexts: alarmIrpMIB.setOrganization('Telefonaktiebolaget LM Ericsson')
if mibBuilder.loadTexts: alarmIrpMIB.setContactInfo('')
if mibBuilder.loadTexts: alarmIrpMIB.setDescription("This SNMP MIB-module constitutes the Ericsson Alarm Integration Reference Point (IRP) solution set for SNMP, version 1:2. The purpose of this IRP is to define an interface though which a 'system' (typically a network element manager or a network element) can communicate alarm information for its managed objects to one or several 'actors' (typically network management systems). An alarm is a kind of object that represents an abnormal condition for a managed object. An alarm is active as long as the corresponding abnormal condition remains. The system maintains an 'Alarm Table' containing all currently active alarms for its managed objects. When an alarm is cleared, it is removed from the list and no longer accessible. Alarms can be forwarded to the actors either synchronously (requested through get, get-next or get- bulk PDUs) or asynchrously (through inform or trap PDUs) whenever an entry in the Alarm Table is created, modified or cleared.")
alarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3881, 2, 1))
alarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3881, 2, 2))
alarmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3881, 2, 2, 0))
alarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3881, 2, 3))
class DisplayString80(TextualConvention, OctetString):
    description = 'max 80 chars'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

class DisplayString200(TextualConvention, OctetString):
    description = 'max 200 chars'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 200)

class ManagedObjectClass(TextualConvention, OctetString):
    description = 'A name identifying a Managed Object Class'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class ManagedObjectInstance(TextualConvention, OctetString):
    description = 'A distinguished name identifying a Managed Object Instance through a containment hierarchy within the name space of its agent. It is important that this name is consistant with naming used over other interfaces, such as interfaces for configuration and performance management.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 200)

class TypeOfEvent(TextualConvention, Integer32):
    description = 'Event type as specified in ITU recommendations X.733 and X.736.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 10, 11, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("unknown", 0), ("communicationsAlarm", 2), ("environmentalAlarm", 3), ("equipmentAlarm", 4), ("processingErrorAlarm", 10), ("qualityOfServiceAlarm", 11), ("integrityViolation", 15), ("operationalViolation", 16), ("physicalViolation", 17), ("securityServiceViolation", 18), ("timeDomainViolation", 19))

class PerceivedSeverity(TextualConvention, Integer32):
    description = 'Perceived severity as specified in ITU recommendation X.733. The value indeterminate(0) is not recommended to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("cleared", 5))

class ProbableCause(TextualConvention, Integer32):
    description = 'Probable cause as specified in ITU recommendations M.3100, X.733 and X.736, and in ETSI recommendation GSM 12.11.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 151, 152, 153, 154, 155, 156, 301, 302, 303, 305, 306, 307, 308, 310, 311, 313, 315, 316, 317, 321, 322, 323, 324, 325, 326, 327, 330, 332, 333, 334, 336, 339, 340, 342, 343, 344, 345, 346, 347, 348, 350, 351, 353, 354, 356, 357, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 501, 502, 503, 504, 505, 5056, 507, 508, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 525, 526, 527, 528, 529, 530, 531, 532, 533, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574))
    namedValues = NamedValues(("m3100Indeterminate", 0), ("m3100AlarmIndicationSignal", 1), ("m3100CallSetupFailure", 2), ("m3100DegradedSignal", 3), ("m3100FarEndReceiverFailure", 4), ("m3100FramingError", 5), ("m3100LossOfFrame", 6), ("m3100LossOfPointer", 7), ("m3100LossOfSignal", 8), ("m3100PayloadTypeMismatch", 9), ("m3100TransmissionError", 10), ("m3100RemoteAlarmInterface", 11), ("m3100ExcessiveBitErrorRate", 12), ("m3100PathTraceMismatch", 13), ("m3100Unavailable", 14), ("m3100SignalLabelMismatch", 15), ("m3100LossOfMultiFrame", 16), ("m3100BackPlaneFailure", 51), ("m3100DataSetProblem", 52), ("m3100EquipmentIdentifierDuplication", 53), ("m3100ExternalIfDeviceProblem", 54), ("m3100LineCardProblem", 55), ("m3100MultiplexerProblem", 56), ("m3100NeIdentifierDuplication", 57), ("m3100PowerProblem", 58), ("m3100ProcessorProblem", 59), ("m3100ProtectionPathFailure", 60), ("m3100ReceiverFailure", 61), ("m3100ReplaceableUnitMissing", 62), ("m3100ReplaceableUnitTypeMismatch", 63), ("m3100SynchronisationSourceMismatch", 64), ("m3100TerminalProblem", 65), ("m3100TimingProblem", 66), ("m3100TransmitterFailure", 67), ("m3100TrunkCardProblem", 68), ("m3100ReplaceableUnitProblem", 69), ("m3100AirCompressorFailure", 101), ("m3100AirConditioningFailure", 102), ("m3100AirDryerFailure", 103), ("m3100BatteryDischarging", 104), ("m3100BatteryFailure", 105), ("m3100CommercialPowerFailure", 106), ("m3100CoolingFanFailure", 107), ("m3100EngineFailure", 108), ("m3100FireDetectorFailure", 109), ("m3100FuseFailure", 110), ("m3100GeneratorFailure", 111), ("m3100LowBatteryThreshold", 112), ("m3100PumpFailure", 113), ("m3100RectifierFailure", 114), ("m3100RectifierHighVoltage", 115), ("m3100RectifierLowVoltage", 116), ("m3100VentilationSystemFailure", 117), ("m3100EnclosureDoorOpen", 118), ("m3100ExplosiveGas", 119), ("m3100Fire", 120), ("m3100Flood", 121), ("m3100HighHumidity", 122), ("m3100HighTemperature", 123), ("m3100HighWind", 124), ("m3100IceBuildUp", 125), ("m3100LowFuel", 127), ("m3100LowHumidity", 128), ("m3100LowCablePressure", 129), ("m3100LowTemperature", 130), ("m3100LowWater", 131), ("m3100Smoke", 132), ("m3100ToxicGas", 133), ("m3100StorageCapacityProblem", 151), ("m3100MemoryMismatch", 152), ("m3100CorruptData", 153), ("m3100OutOfCPUCycles", 154), ("m3100SoftwareEnvironmentProblem", 155), ("m3100SoftwareDownloadFailure", 156), ("x733AdapterError", 301), ("x733ApplicationSubsystemFailure", 302), ("x733BandwidthReduced", 303), ("x733CommunicationsProtocolError", 305), ("x733CommunicationsSubsystemFailure", 306), ("x733ConfigurationOrCustomizationError", 307), ("x733Congestion", 308), ("x733CpuCyclesLimitExceeded", 310), ("x733DataSetOrModemError", 311), ("x733DTEDCEInterfaceError", 313), ("x733EquipmentMalfunction", 315), ("x733ExcessiveVibration", 316), ("x733FileError", 317), ("x733HeatingOrVentilationOrCoolingSystemProblem", 321), ("x733HumidityUnacceptable", 322), ("x733InputOutputDeviceError", 323), ("x733InputDeviceError", 324), ("x733LANError", 325), ("x733LeakDetected", 326), ("x733LocalNodeTransmissionError", 327), ("x733MaterialSupplyExhausted", 330), ("x733OutOfMemory", 332), ("x733OuputDeviceError", 333), ("x733PerformanceDegraded", 334), ("x733PressureUnacceptable", 336), ("x733QueueSizeExceeded", 339), ("x733ReceiveFailure", 340), ("x733RemoteNodeTransmissionError", 342), ("x733ResourceAtOrNearingCapacity", 343), ("x733ResponseTimeExcessive", 344), ("x733RetransmissionRateExcessive", 345), ("x733SoftwareError", 346), ("x733SoftwareProgramAbnormallyTerminated", 347), ("x733SoftwareProgramError", 348), ("x733TemperatureUnacceptable", 350), ("x733ThresholdCrossed", 351), ("x733ToxicLeakDetected", 353), ("x733TransmitFailure", 354), ("x733UnderlyingResourceUnavailable", 356), ("x733VersionMismatch", 357), ("x736AuthenticationFailure", 401), ("x736BreachOfConfidentiality", 402), ("x736CableTamper", 403), ("x736DelayedInformation", 404), ("x736DenialOfService", 405), ("x736DuplicateInformation", 406), ("x736InformationMissing", 407), ("x736InformationModificationDetected", 408), ("x736InformationOutOfSequence", 409), ("x736IntrusionDetection", 410), ("x736KeyExpired", 411), ("x736NonRepudiationFailure", 412), ("x736OutOfHoursActivity", 413), ("x736OutOfService", 414), ("x736ProceduralError", 415), ("x736UnauthorizedAccessAttempt", 416), ("x736UnexpectedInformation", 417), ("x736UnspecifiedReason", 418), ("gsm1211AbisToBTSInterfaceFailure", 501), ("gsm1211AbisToTRXInterfaceFailure", 502), ("gsm1211AntennaProblem", 503), ("gsm1211BatteryBreakdown", 504), ("gsm1211BatteryChargingFault", 505), ("gsm1211ClockSynchronisationProblem", 5056), ("gsm1211CombinerProblem", 507), ("gsm1211DiskProblem", 508), ("gsm1211ExcessiveReceiverTemperature", 510), ("gsm1211ExcessiveTransmitterOutputPower", 511), ("gsm1211ExcessiveTransmitterTemperature", 512), ("gsm1211FrequencyHoppingDegraded", 513), ("gsm1211FrequencyHoppingFailure", 514), ("gsm1211FrequencyRedefinitionFailed", 515), ("gsm1211LineInterfaceFailure", 516), ("gsm1211LinkFailure", 517), ("gsm1211LossOfSynchronisation", 518), ("gsm1211LostRedundancy", 519), ("gsm1211MainsBreakdownWithBatteryBackUp", 520), ("gsm1211MainsBreakdownWithoutBatteryBackUp", 521), ("gsm1211PowerSupplyFailure", 522), ("gsm1211ReceiverAntennaFault", 523), ("gsm1211ReceiverMulticouplerFailure", 525), ("gsm1211ReducedTransmitterOutputPower", 526), ("gsm1211SignalQualityEvaluationFault", 527), ("gsm1211TimeslotHardwareFailure", 528), ("gsm1211TransceiverProblem", 529), ("gsm1211TranscoderProblem", 530), ("gsm1211TranscoderOrRateAdapterProblem", 531), ("gsm1211TransmitterAntennaFailure", 532), ("gsm1211TransmitterAntennaNotAdjusted", 533), ("gsm1211TransmitterLowVoltageOrCurrent", 535), ("gsm1211TransmitterOffFrequency", 536), ("gsm1211DatabaseInconsistency", 537), ("gsm1211FileSystemCallUnsuccessful", 538), ("gsm1211InputParameterOutOfRange", 539), ("gsm1211InvalidParameter", 540), ("gsm1211InvalidPointer", 541), ("gsm1211MessageNotExpected", 542), ("gsm1211MessageNotInitialised", 543), ("gsm1211MessageOutOfSequence", 544), ("gsm1211SystemCallUnsuccessful", 545), ("gsm1211TimeoutExpired", 546), ("gsm1211VariableOutOfRange", 547), ("gsm1211WatchDogTimerExpired", 548), ("gsm1211CoolingSystemFailure", 549), ("gsm1211ExternalEquipmentFailure", 550), ("gsm1211ExternalPowerSupplyFailure", 551), ("gsm1211ExternalTransmissionDeviceFailure", 552), ("gsm1211ReducedAlarmReporting", 561), ("gsm1211ReducedEventReporting", 562), ("gsm1211ReducedLoggingCapability", 563), ("gsm1211SystemResourcesOverload", 564), ("gsm1211BroadcastChannelFailure", 565), ("gsm1211ConnectionEstablishmentError", 566), ("gsm1211InvalidMessageReceived", 567), ("gsm1211InvalidMSUReceived", 568), ("gsm1211LAPDLinkProtocolFailure", 569), ("gsm1211LocalAlarmIndication", 570), ("gsm1211RemoteAlarmIndication", 571), ("gsm1211RoutingFailure", 572), ("gsm1211SS7ProtocolFailure", 573), ("gsm1211TransmissionError", 574))

alarmIrpVersion = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmIrpVersion.setStatus('current')
if mibBuilder.loadTexts: alarmIrpVersion.setDescription("This object represents the version of the Alarm IRP SNMPv2 Solution Set supported by the agent. The format is 'xy', where 'x' is the version of the information model and 'y' the version of the solution set corresponding to this information model.")
alarmIndeterminateNumber = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmIndeterminateNumber.setStatus('current')
if mibBuilder.loadTexts: alarmIndeterminateNumber.setDescription("This object determines the number of currently active alarms with perceived severity 'indeterminate'.")
alarmCriticalNumber = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCriticalNumber.setStatus('current')
if mibBuilder.loadTexts: alarmCriticalNumber.setDescription("This object determines the number of currently active alarms with perceived severity 'critical'.")
alarmMajorNumber = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMajorNumber.setStatus('current')
if mibBuilder.loadTexts: alarmMajorNumber.setDescription("This object determines the number of currently active alarms with perceived severity 'major'.")
alarmMinorNumber = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMinorNumber.setStatus('current')
if mibBuilder.loadTexts: alarmMinorNumber.setDescription("This object determines the number of currently active alarms with perceived severity 'minor'.")
alarmWarningNumber = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmWarningNumber.setStatus('current')
if mibBuilder.loadTexts: alarmWarningNumber.setDescription("This object determines the number of currently active alarms with perceived severity 'warning'.")
alarmNumber = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNumber.setStatus('current')
if mibBuilder.loadTexts: alarmNumber.setDescription('This object determines the total number of currently active alarms, i.e. the total number of entries in the Alarm Table.')
alarmTable = MibTable((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8), )
if mibBuilder.loadTexts: alarmTable.setStatus('current')
if mibBuilder.loadTexts: alarmTable.setDescription('Table with information about the alarms that are currently active in the system.')
alarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1), ).setIndexNames((0, "ERICSSON-ALARM-IRP-MIB", "alarmId"))
if mibBuilder.loadTexts: alarmEntry.setStatus('current')
if mibBuilder.loadTexts: alarmEntry.setDescription('One entry in the table holds one current alarm.')
alarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmId.setStatus('current')
if mibBuilder.loadTexts: alarmId.setDescription("This object uniquely identifies an entry in the Alarm Table. It increases every time a new alarm occurs. Due to cleared alarms the index will not be contiguous. When the maximum is reached of Integer32, the value of this object rolls over to 1. The actor must use 'alarmEventTime' to sort on chronological order. The alarmId object is read-only even though it is used as index in the Alarm Table. The reason is that this facilities a convenient way to extract the corresponding value from a notification where the object is included.")
alarmManagedObjectClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 2), ManagedObjectClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmManagedObjectClass.setStatus('current')
if mibBuilder.loadTexts: alarmManagedObjectClass.setDescription('This object identifies the class of network resources to which the subject alarm is related.')
alarmManagedObjectInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 3), ManagedObjectInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmManagedObjectInstance.setStatus('current')
if mibBuilder.loadTexts: alarmManagedObjectInstance.setDescription('This object identifies the instance (of a class) of network resource to which the subject alarm is related.')
alarmEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEventTime.setStatus('current')
if mibBuilder.loadTexts: alarmEventTime.setDescription("This object represents the time of occurrence of the subject alarm. If the alarm changes 'perceivedSeverity', then this object represents the time of the last severity change, else it represents the time carried in the original alarm emitted by the alarmed network resource. The time indication is in UTC (Co-ordinated Universal Time).")
alarmEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 5), TypeOfEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEventType.setStatus('current')
if mibBuilder.loadTexts: alarmEventType.setDescription('This object represents the type of event according to the ITU recommendations X.733/X.736.')
alarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 6), ProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmProbableCause.setStatus('current')
if mibBuilder.loadTexts: alarmProbableCause.setDescription('This object represents the probable cause identification code (generic classification) for the subject alarm according to the ITU recommendations M.3100/X.733/X.736 and ETSI recommendation GSM 12.11.')
alarmPerceivedSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 7), PerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPerceivedSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmPerceivedSeverity.setDescription("This object represents the perceived severity of the subject alarm according to the ITU recommendation X.733. If the system changes the perceived severity of an existing alarm to a higher value, the corresponding 'alarmAckUser' and 'alarmAckTime' objects are cleared.")
alarmSpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 8), DisplayString80()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSpecificProblem.setStatus('current')
if mibBuilder.loadTexts: alarmSpecificProblem.setDescription("This object represents the specific problem identification code for the subject alarm. This is a more detailed (product specific) identification compared to the (generic) 'alarmprobableCause'.")
alarmAckUser = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 9), DisplayString80()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAckUser.setStatus('current')
if mibBuilder.loadTexts: alarmAckUser.setDescription("This object is used to define the id of a user that acknowledge the subject alarm. An alarm can be unacknowledged by clearing this object. This object shall always be set or cleared in the same set request as the 'alarmAckTime' object defined below. The system will respond with 'inconsistentValue' upon attempts to set this object without setting 'alarmAckTime'.")
alarmAckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 10), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAckTime.setStatus('current')
if mibBuilder.loadTexts: alarmAckTime.setDescription("This object represents the time when the subject alarm was acknowledged. This object shall always be set or cleared in the same set request as the 'alarmAckUser' object defined above. The system will respond with 'inconsistentValue' upon attempts to set this object without setting 'alarmAckTime'. The time indication is in UTC (Co-ordinated Universal Time).")
alarmCommentUser = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 11), DisplayString80()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmCommentUser.setStatus('current')
if mibBuilder.loadTexts: alarmCommentUser.setDescription("This object is used to define the id of a user that enters a comment for the subject alarm. This object shall always be set in the same request as the 'alarmCommentText' object defined below. The system will respond with 'inconsistentValue' upon attempts to set this object without setting 'alarmCommentText'.")
alarmCommentText = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 12), DisplayString200()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmCommentText.setStatus('current')
if mibBuilder.loadTexts: alarmCommentText.setDescription("This object represents a comment added by an actor to the subject alarm. This object shall always be set in the same set request as the 'alarmCommentUser' object defined above. The system will respond with 'inconsistentValue' upon attempts to set this object without setting 'alarmAckUser'.")
alarmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 13), DisplayString200()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmAdditionalText.setStatus('current')
if mibBuilder.loadTexts: alarmAdditionalText.setDescription('This object represents some arbitrary additional text for the subject alarm.')
notificationId = MibScalar((1, 3, 6, 1, 4, 1, 3881, 2, 1, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationId.setStatus('current')
if mibBuilder.loadTexts: notificationId.setDescription('This object uniquely identifies a notification. It increases every time a new notification is sent. When the maximum is reached of Integer32, the value of this object rolls over to 1.')
alarmNew = NotificationType((1, 3, 6, 1, 4, 1, 3881, 2, 2, 0, 1)).setObjects(("ERICSSON-ALARM-IRP-MIB", "notificationId"), ("ERICSSON-ALARM-IRP-MIB", "alarmId"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"), ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"), ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"), ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
if mibBuilder.loadTexts: alarmNew.setStatus('current')
if mibBuilder.loadTexts: alarmNew.setDescription('This notification is sent when a new Alarm is generated and stored in the Alarm Table. Note that the notification does not include all objects for the corresponding entry in the Alarm Table. The reason is that some environments may have problems with large PDUs. Thus, the notification receiver must get the missing objects from the Alarm Table.')
alarmChanged = NotificationType((1, 3, 6, 1, 4, 1, 3881, 2, 2, 0, 2)).setObjects(("ERICSSON-ALARM-IRP-MIB", "notificationId"), ("ERICSSON-ALARM-IRP-MIB", "alarmId"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"), ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"), ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"), ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
if mibBuilder.loadTexts: alarmChanged.setStatus('current')
if mibBuilder.loadTexts: alarmChanged.setDescription('This notification is generated when any of the attributes of an Alarm has changed. Note that the EventTime value in the notification will be different than that in the original notifyNewAlarm if and only if the alarmPerceivedSeverity value is different from that carried in original notifyNewAlarm. Note that the notification does not include all objects for the corresponding entry in the Alarm Table. The reason is that some environments may have problems with large PDUs. Thus, the notification receiver must get the missing objects from the Alarm Table.')
alarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 3881, 2, 2, 0, 3)).setObjects(("ERICSSON-ALARM-IRP-MIB", "notificationId"), ("ERICSSON-ALARM-IRP-MIB", "alarmId"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"), ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"), ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"), ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
if mibBuilder.loadTexts: alarmCleared.setStatus('current')
if mibBuilder.loadTexts: alarmCleared.setDescription('This notification is generated when an alarm is cleared. A cleared alarm is removed from the Alarm Table and is no longer accessible.')
alarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3881, 2, 3, 1))
alarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2))
alarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3881, 2, 3, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterGroup"), ("ERICSSON-ALARM-IRP-MIB", "alarmAdminMandatoryGroup"), ("ERICSSON-ALARM-IRP-MIB", "alarmMandatoryGroup"), ("ERICSSON-ALARM-IRP-MIB", "alarmNotificationMandatoryGroup"), ("ERICSSON-ALARM-IRP-MIB", "alarmNumberGroup"), ("ERICSSON-ALARM-IRP-MIB", "alarmOptionalGroup"), ("ERICSSON-ALARM-IRP-MIB", "alarmNotificationOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmCompliance = alarmCompliance.setStatus('current')
if mibBuilder.loadTexts: alarmCompliance.setDescription('A collection of objects that are required for compliance to the ALARM-IRP.')
alarmAdminMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 1)).setObjects(("ERICSSON-ALARM-IRP-MIB", "alarmIrpVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmAdminMandatoryGroup = alarmAdminMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: alarmAdminMandatoryGroup.setDescription('A collection of mandatory objects holding administrative information.')
alarmNumberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 2)).setObjects(("ERICSSON-ALARM-IRP-MIB", "alarmNumber"), ("ERICSSON-ALARM-IRP-MIB", "alarmIndeterminateNumber"), ("ERICSSON-ALARM-IRP-MIB", "alarmCriticalNumber"), ("ERICSSON-ALARM-IRP-MIB", "alarmMajorNumber"), ("ERICSSON-ALARM-IRP-MIB", "alarmMinorNumber"), ("ERICSSON-ALARM-IRP-MIB", "alarmWarningNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmNumberGroup = alarmNumberGroup.setStatus('current')
if mibBuilder.loadTexts: alarmNumberGroup.setDescription('A collection of optional objects for retrieval of the number of currently active alarms.')
alarmMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 3)).setObjects(("ERICSSON-ALARM-IRP-MIB", "notificationId"), ("ERICSSON-ALARM-IRP-MIB", "alarmId"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"), ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"), ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"), ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"), ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"), ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmMandatoryGroup = alarmMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: alarmMandatoryGroup.setDescription('A collection of objects that represents mandatory alarm attributes.')
alarmOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 4)).setObjects(("ERICSSON-ALARM-IRP-MIB", "alarmAckUser"), ("ERICSSON-ALARM-IRP-MIB", "alarmAckTime"), ("ERICSSON-ALARM-IRP-MIB", "alarmCommentUser"), ("ERICSSON-ALARM-IRP-MIB", "alarmCommentText"), ("ERICSSON-ALARM-IRP-MIB", "alarmAdditionalText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmOptionalGroup = alarmOptionalGroup.setStatus('current')
if mibBuilder.loadTexts: alarmOptionalGroup.setDescription('A collection of objects that represents optional alarm attributes.')
alarmNotificationMandatoryGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 5)).setObjects(("ERICSSON-ALARM-IRP-MIB", "alarmNew"), ("ERICSSON-ALARM-IRP-MIB", "alarmCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmNotificationMandatoryGroup = alarmNotificationMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationMandatoryGroup.setDescription('A collection of mandatory alarm notifications.')
alarmNotificationOptionalGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 6)).setObjects(("ERICSSON-ALARM-IRP-MIB", "alarmChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmNotificationOptionalGroup = alarmNotificationOptionalGroup.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationOptionalGroup.setDescription('A collection of optional alarm notifications.')
mibBuilder.exportSymbols("ERICSSON-ALARM-IRP-MIB", alarmNew=alarmNew, alarmId=alarmId, alarmProbableCause=alarmProbableCause, alarmCommentText=alarmCommentText, alarmEntry=alarmEntry, alarmConformance=alarmConformance, alarmAdditionalText=alarmAdditionalText, alarmNotificationMandatoryGroup=alarmNotificationMandatoryGroup, alarmNumber=alarmNumber, alarmNotifications=alarmNotifications, alarmMajorNumber=alarmMajorNumber, DisplayString80=DisplayString80, alarmSpecificProblem=alarmSpecificProblem, ManagedObjectInstance=ManagedObjectInstance, alarmChanged=alarmChanged, alarmMinorNumber=alarmMinorNumber, alarmOptionalGroup=alarmOptionalGroup, alarmWarningNumber=alarmWarningNumber, alarmManagedObjectClass=alarmManagedObjectClass, alarmIrpMIB=alarmIrpMIB, alarmCriticalNumber=alarmCriticalNumber, alarmAckUser=alarmAckUser, alarmNotificationOptionalGroup=alarmNotificationOptionalGroup, alarmAdminMandatoryGroup=alarmAdminMandatoryGroup, notificationId=notificationId, alarmObjects=alarmObjects, ProbableCause=ProbableCause, alarmEventTime=alarmEventTime, DisplayString200=DisplayString200, alarmCompliance=alarmCompliance, TypeOfEvent=TypeOfEvent, alarmManagedObjectInstance=alarmManagedObjectInstance, alarmAckTime=alarmAckTime, alarmIndeterminateNumber=alarmIndeterminateNumber, alarmTable=alarmTable, alarmIrpVersion=alarmIrpVersion, alarmGroups=alarmGroups, alarmPerceivedSeverity=alarmPerceivedSeverity, PYSNMP_MODULE_ID=alarmIrpMIB, alarmEventType=alarmEventType, alarmNotificationPrefix=alarmNotificationPrefix, alarmCompliances=alarmCompliances, alarmCleared=alarmCleared, PerceivedSeverity=PerceivedSeverity, ManagedObjectClass=ManagedObjectClass, alarmNumberGroup=alarmNumberGroup, alarmMandatoryGroup=alarmMandatoryGroup, alarmCommentUser=alarmCommentUser)
