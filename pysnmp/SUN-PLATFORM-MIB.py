#
# PySNMP MIB module SUN-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-PLATFORM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalEntry, entLogicalIndex, entPhysicalIndex, entLogicalEntry = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry", "entLogicalIndex", "entPhysicalIndex", "entLogicalEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Integer32, Gauge32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, ObjectIdentity, enterprises, Counter32, Unsigned32, NotificationType, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Gauge32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "enterprises", "Counter32", "Unsigned32", "NotificationType", "Bits", "MibIdentifier")
TAddress, RowPointer, TDomain, DisplayString, RowStatus, VariablePointer, TestAndIncr, TextualConvention, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "RowPointer", "TDomain", "DisplayString", "RowStatus", "VariablePointer", "TestAndIncr", "TextualConvention", "DateAndTime", "TruthValue")
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
sunFire = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70))
sunPlatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 70, 101))
sunPlatMIB.setRevisions(('2002-11-14 00:00',))
if mibBuilder.loadTexts: sunPlatMIB.setLastUpdated('200211140000Z')
if mibBuilder.loadTexts: sunPlatMIB.setOrganization('Sun Microsystems, Inc.')
sunPlatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1))
sunPlatMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2))
sunPlatMIBPhysicalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1))
sunPlatMIBLogicalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2))
sunPlatMIBLogs = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3))
sunPlatMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0))
sunPlatMIBTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1))
sunPlatMIBConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3))
sunPlatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 1))
sunPlatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2))
sunPlatMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1))
sunPlatMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 2))
class SunPlatLogAdministrativeState(TextualConvention, Integer32):
    reference = 'X.735, sec. 8.1.1.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("locked", 1), ("unlocked", 2))

class SunPlatAdministrativeState(TextualConvention, Integer32):
    reference = 'X.731, sec. 8.1.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("locked", 1), ("unlocked", 2), ("shuttingDown", 3))

class SunPlatOperationalState(TextualConvention, Integer32):
    reference = 'X.731, sec. 8.1.1.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class SunPlatAlarmPerceivedSeverity(TextualConvention, Integer32):
    reference = 'X.733, sec. 8.1.2.3.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("cleared", 6))

class SunPlatAlarmStatus(TextualConvention, Integer32):
    reference = 'M.3100, sec. 5.8.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("indeterminate", 4), ("warning", 5), ("pending", 6), ("cleared", 7))

class SunPlatEquipmentHolderType(TextualConvention, Integer32):
    reference = 'M.3100, sec. 5.26.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("bay", 1), ("shelf", 2), ("drawer", 3), ("slot", 4), ("rack", 5))

class SunPlatEquipmentHolderStatus(TextualConvention, Integer32):
    reference = 'M.3100, sec. 5.32.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("holderEmpty", 1), ("inTheAcceptableList", 2), ("notInTheAcceptableList", 3), ("unknownType", 4))

class SunPlatEquipmentHolderPower(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("powerOff", 3), ("powerOn", 4))

class SunPlatCircuitPackAvailabilityStatus(TextualConvention, Bits):
    reference = 'X.731, sec. 8.1.2.3.'
    status = 'current'
    namedValues = NamedValues(("inTest", 0), ("failed", 1), ("powerOff", 2), ("offLine", 3), ("offDuty", 4), ("dependency", 5), ("degraded", 6), ("notInstalled", 7))

class SunPlatProbableCause(TextualConvention, Integer32):
    reference = 'M.3100, sec. 10.2; X.733, sec. 8.1.2.1; X.736, sec. 8.1.2.1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 201, 202, 203, 204, 205, 206, 207, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303))
    namedValues = NamedValues(("aIS", 1), ("callSetUpFailure", 2), ("degradedSignal", 3), ("farEndReceiverFailure", 4), ("framingError", 5), ("lossOfFrame", 6), ("lossOfPointer", 7), ("lossOfSignal", 8), ("payloadTypeMismatch", 9), ("transmissionError", 10), ("remoteAlarmInterface", 11), ("excessiveBER", 12), ("pathTraceMismatch", 13), ("unavailable", 14), ("signalLabelMismatch", 15), ("lossOfMultiFrame", 16), ("receiveFailure", 17), ("transmitFailure", 18), ("modulationFailure", 19), ("demodulationFailure", 20), ("broadcastChannelFailure", 21), ("connectionEstablishmentError", 22), ("invalidMessageReceived", 23), ("localNodeTransmissionError", 24), ("remoteNodeTransmissionError", 25), ("routingFailure", 26), ("backplaneFailure", 51), ("dataSetProblem", 52), ("equipmentIdentifierDuplication", 53), ("externalIFDeviceProblem", 54), ("lineCardProblem", 55), ("multiplexerProblem", 56), ("nEIdentifierDuplication", 57), ("powerProblem", 58), ("processorProblem", 59), ("protectionPathFailure", 60), ("receiverFailure", 61), ("replaceableUnitMissing", 62), ("replaceableUnitTypeMismatch", 63), ("synchronizationSourceMismatch", 64), ("terminalProblem", 65), ("timingProblem", 66), ("transmitterFailure", 67), ("trunkCardProblem", 68), ("replaceableUnitProblem", 69), ("realTimeClockFailure", 70), ("antennaFailure", 71), ("batteryChargingFailure", 72), ("diskFailure", 73), ("frequencyHoppingFailure", 74), ("iODeviceError", 75), ("lossOfSynchronisation", 76), ("lossOfRedundancy", 77), ("powerSupplyFailure", 78), ("signalQualityEvaluationFailure", 79), ("tranceiverFailure", 80), ("protectionMechanismFailure", 81), ("protectingResourceFailure", 82), ("airCompressorFailure", 101), ("airConditioningFailure", 102), ("airDryerFailure", 103), ("batteryDischarging", 104), ("batteryFailure", 105), ("commercialPowerFailure", 106), ("coolingFanFailure", 107), ("engineFailure", 108), ("fireDetectorFailure", 109), ("fuseFailure", 110), ("generatorFailure", 111), ("lowBatteryThreshold", 112), ("pumpFailure", 113), ("rectifierFailure", 114), ("rectifierHighVoltage", 115), ("rectifierLowFVoltage", 116), ("ventilationsSystemFailure", 117), ("enclosureDoorOpen", 118), ("explosiveGas", 119), ("fire", 120), ("flood", 121), ("highHumidity", 122), ("highTemperature", 123), ("highWind", 124), ("iceBuildUp", 125), ("intrusionDetection", 126), ("lowFuel", 127), ("lowHumidity", 128), ("lowCablePressure", 129), ("lowTemperature", 130), ("lowWater", 131), ("smoke", 132), ("toxicGas", 133), ("coolingSystemFailure", 134), ("externalEquipmentFailure", 135), ("externalPointFailure", 136), ("storageCapacityProblem", 151), ("memoryMismatch", 152), ("corruptData", 153), ("outOfCPUCycles", 154), ("sfwrEnvironmentProblem", 155), ("sfwrDownloadFailure", 156), ("lossOfRealTime", 157), ("reinitialized", 158), ("applicationSubsystemFailure", 159), ("configurationOrCustomisationError", 160), ("databaseInconsistency", 161), ("fileError", 162), ("outOfMemory", 163), ("softwareError", 164), ("timeoutExpired", 165), ("underlayingResourceUnavailable", 166), ("versionMismatch", 167), ("bandwidthReduced", 201), ("congestion", 202), ("excessiveErrorRate", 203), ("excessiveResponseTime", 204), ("excessiveRetransmissionRate", 205), ("reducedLoggingCapability", 206), ("systemResourcesOverload", 207), ("other", 255), ("adapterError", 256), ("callEstablishmentError", 257), ("communicationsProtocolError", 258), ("communicationsSubsystemFailure", 259), ("configurationOrCustomizationError", 260), ("cpuCyclesLimitExceeded", 261), ("dataSetOrModemError", 262), ("dteDceInterfaceError", 263), ("equipmentMalfunction", 264), ("excessiveVibration", 265), ("fireDetected", 266), ("floodDetected", 267), ("heatingVentCoolingSystemProblem", 268), ("humidityUnacceptable", 269), ("inputOutputDeviceError", 270), ("inputDeviceError", 271), ("lanError", 272), ("leakDetected", 273), ("materialSupplyExhausted", 274), ("ouputDeviceError", 275), ("performanceDegraded", 276), ("pressureUnacceptable", 277), ("queueSizeExceeded", 278), ("resourceAtOrNearingCapacity", 279), ("responseTimeExecessive", 280), ("retransmissionRateExcessive", 281), ("softwareProgramAbnormallyTerminated", 282), ("softwareProgramError", 283), ("temperatureUnacceptable", 284), ("thresholdCrossed", 285), ("toxicLeakDetected", 286), ("underlyingResourceUnavailable", 287), ("authenticationFailure", 288), ("breachOfConfidentiality", 289), ("cableTamper", 290), ("delayedInformation", 291), ("denialOfService", 292), ("duplicateInformation", 293), ("informationMissing", 294), ("informationModificationDetected", 295), ("informationOutOfSequence", 296), ("keyExpired", 297), ("nonRepudiationFailure", 298), ("outOfHoursActivity", 299), ("outOfService", 300), ("proceduralError", 301), ("unauthorizedAccessAttempt", 302), ("unexpectedInformation", 303))

class SunPlatPhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("alarm", 2), ("watchdog", 3))

class SunPlatSensorClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("binary", 1), ("numeric", 2), ("discrete", 3))

class SunPlatSensorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("temperature", 3), ("voltage", 4), ("current", 5), ("tachometer", 6), ("counter", 7), ("switch", 8), ("lock", 9), ("humidity", 10), ("smokeDetection", 11), ("presence", 12), ("airFlow", 13))

class SunPlatBaseUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("degC", 3), ("degF", 4), ("degK", 5), ("volts", 6), ("amps", 7), ("watts", 8), ("joules", 9), ("coulombs", 10), ("va", 11), ("nits", 12), ("lumens", 13), ("lux", 14), ("candelas", 15), ("kPa", 16), ("psi", 17), ("newtons", 18), ("cfm", 19), ("rpm", 20), ("hertz", 21), ("seconds", 22), ("minutes", 23), ("hours", 24), ("days", 25), ("weeks", 26), ("mils", 27), ("inches", 28), ("feet", 29), ("cubicInches", 30), ("cubicFeet", 31), ("meters", 32), ("cubicCentimeters", 33), ("cubicMeters", 34), ("liters", 35), ("fluidOunces", 36), ("radians", 37), ("steradians", 38), ("revolutions", 39), ("cycles", 40), ("gravities", 41), ("ounces", 42), ("pounds", 43), ("footPounds", 44), ("ounceInches", 45), ("gauss", 46), ("gilberts", 47), ("henries", 48), ("farads", 49), ("ohms", 50), ("siemens", 51), ("moles", 52), ("becquerels", 53), ("ppm", 54), ("decibels", 55), ("dBA", 56), ("dbC", 57), ("grays", 58), ("sieverts", 59), ("colorTemperatureDegK", 60), ("bits", 61), ("bytes", 62), ("words", 63), ("doubleWords", 64), ("quadWords", 65), ("percentage", 66))

class SunPlatRateUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 1), ("perMicroSecond", 2), ("perMilliSecond", 3), ("perSecond", 4), ("perMinute", 5), ("perHour", 6), ("perDay", 7), ("perWeek", 8), ("perMonth", 9), ("perYear", 10))

class SunPlatNumericSensorEnabledThresholds(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lowerThresholdNonCritical", 0), ("upperThresholdNonCritical", 1), ("lowerThresholdCritical", 2), ("upperThresholdCritical", 3), ("lowerThresholdFatal", 4), ("upperThresholdFatal", 5))

class SunPlatNumericSensorThresholdResetAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("reset", 1))

class SunPlatAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("audible", 2), ("visible", 3), ("motion", 4), ("switch", 5))

class SunPlatAlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("steady", 3), ("alternating", 4))

class SunPlatAlarmUrgency(TextualConvention, Integer32):
    reference = 'CIM Schema v2.5, CIM_AlarmDevice.Urgency'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("notSupported", 3), ("informational", 4), ("nonCritical", 5), ("critical", 6), ("unrecoverable", 7))

class SunPlatWatchdogAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("statusOnly", 1), ("systemInterrupt", 2), ("systemReset", 3), ("systemPowerOff", 4), ("systemPowerCycle", 5))

class SunPlatWatchdogMonitoredEntity(TextualConvention, Integer32):
    reference = 'CIM Schema v2.5, CIM_Watchdog.MonitoredEntity'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("operatingSystem", 3), ("operatingSystemBootProcess", 4), ("operatingSystemShutdownProcess", 5), ("firmwareBootProcess", 6), ("biosBootProcess", 7), ("application", 8), ("serviceProcessor", 9))

class SunPlatPowerSupplyClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("powerSupply", 2), ("battery", 3))

class SunPlatFanClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("fan", 2), ("refrigeration", 3), ("heatPipe", 4))

class SunPlatBatteryStatus(TextualConvention, Integer32):
    reference = 'CIM Schema v2.5, CIM_Battery.BatteryStatus'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("fullyCharged", 3), ("low", 4), ("critical", 5), ("charging", 6), ("chargingAndHigh", 7), ("chargingAndLow", 8), ("chargingAndCritical", 9), ("undefined", 10), ("partiallyCharged", 11))

class SunPlatUnitaryComputerSystemPowerState(TextualConvention, Integer32):
    reference = 'CIM Schema v2.5, CIM_UnitaryComputerSystem'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 1), ("fullPower", 2), ("psLowPower", 3), ("psStandby", 4), ("psOther", 5), ("powerCycle", 6), ("powerOff", 7), ("psWarning", 8), ("hibernate", 9), ("softOff", 10), ("reset", 11))

class SunPlatUnitaryComputerSystemApplicableSetting(TextualConvention, Integer32):
    reference = 'CIM Schema v2.5, CIM_UnitaryComputerSystem'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("defaultSetting", 1), ("specifiedSetting", 2))

class SunPlatLogicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("computerSystem", 2), ("adminDomain", 3))

class SunPlatLogicalStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("ok", 1), ("error", 2), ("degraded", 3), ("unknown", 4), ("predFail", 5), ("starting", 6), ("stopping", 7), ("service", 8), ("stressed", 9), ("nonRecover", 10), ("noContact", 11), ("lostComm", 12), ("stopped", 13))

class SunPlatIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SunPlatPercentage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

sunPlatStartTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatStartTime.setStatus('current')
sunPlatEquipmentTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2), )
if mibBuilder.loadTexts: sunPlatEquipmentTable.setStatus('current')
sunPlatEquipmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1), )
entPhysicalEntry.registerAugmentions(("SUN-PLATFORM-MIB", "sunPlatEquipmentEntry"))
sunPlatEquipmentEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: sunPlatEquipmentEntry.setStatus('current')
sunPlatEquipmentAdministrativeState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 1), SunPlatAdministrativeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatEquipmentAdministrativeState.setStatus('current')
sunPlatEquipmentOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 2), SunPlatOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatEquipmentOperationalState.setStatus('current')
sunPlatEquipmentAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 3), SunPlatAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatEquipmentAlarmStatus.setStatus('current')
sunPlatEquipmentUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatEquipmentUnknownStatus.setStatus('current')
sunPlatEquipmentLocationName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatEquipmentLocationName.setStatus('current')
sunPlatEquipmentHolderTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3), )
if mibBuilder.loadTexts: sunPlatEquipmentHolderTable.setStatus('current')
sunPlatEquipmentHolderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatEquipmentHolderEntry.setStatus('current')
sunPlatEquipmentHolderType = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 1), SunPlatEquipmentHolderType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatEquipmentHolderType.setStatus('current')
sunPlatEquipmentHolderAcceptableTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatEquipmentHolderAcceptableTypes.setStatus('current')
sunPlatEquipmentHolderStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 3), SunPlatEquipmentHolderStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatEquipmentHolderStatus.setStatus('current')
sunPlatEquipmentHolderPowered = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 4), SunPlatEquipmentHolderPower()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatEquipmentHolderPowered.setStatus('current')
sunPlatCircuitPackTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4), )
if mibBuilder.loadTexts: sunPlatCircuitPackTable.setStatus('current')
sunPlatCircuitPackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatCircuitPackEntry.setStatus('current')
sunPlatCircuitPackType = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatCircuitPackType.setStatus('current')
sunPlatCircuitPackAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 2), SunPlatCircuitPackAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatCircuitPackAvailabilityStatus.setStatus('current')
sunPlatCircuitPackReplaceable = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatCircuitPackReplaceable.setStatus('current')
sunPlatCircuitPackHotSwappable = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatCircuitPackHotSwappable.setStatus('current')
sunPlatPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 5), )
if mibBuilder.loadTexts: sunPlatPhysicalTable.setStatus('current')
sunPlatPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatPhysicalEntry.setStatus('current')
sunPlatPhysicalClass = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 5, 1, 1), SunPlatPhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatPhysicalClass.setStatus('current')
sunPlatSensorTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6), )
if mibBuilder.loadTexts: sunPlatSensorTable.setStatus('current')
sunPlatSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatSensorEntry.setStatus('current')
sunPlatSensorClass = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1, 1), SunPlatSensorClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatSensorClass.setStatus('current')
sunPlatSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1, 2), SunPlatSensorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatSensorType.setStatus('current')
sunPlatSensorLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1, 3), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatSensorLatency.setStatus('current')
sunPlatBinarySensorTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7), )
if mibBuilder.loadTexts: sunPlatBinarySensorTable.setStatus('current')
sunPlatBinarySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatBinarySensorEntry.setStatus('current')
sunPlatBinarySensorCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatBinarySensorCurrent.setStatus('current')
sunPlatBinarySensorExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatBinarySensorExpected.setStatus('current')
sunPlatBinarySensorInterpretTrue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatBinarySensorInterpretTrue.setStatus('current')
sunPlatBinarySensorInterpretFalse = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatBinarySensorInterpretFalse.setStatus('current')
sunPlatNumericSensorTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8), )
if mibBuilder.loadTexts: sunPlatNumericSensorTable.setStatus('current')
sunPlatNumericSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatNumericSensorEntry.setStatus('current')
sunPlatNumericSensorBaseUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 1), SunPlatBaseUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorBaseUnits.setStatus('current')
sunPlatNumericSensorExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorExponent.setStatus('current')
sunPlatNumericSensorRateUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 3), SunPlatRateUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorRateUnits.setStatus('current')
sunPlatNumericSensorCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorCurrent.setStatus('current')
sunPlatNumericSensorNormalMin = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorNormalMin.setStatus('current')
sunPlatNumericSensorNormalMax = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorNormalMax.setStatus('current')
sunPlatNumericSensorAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 7), SunPlatPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorAccuracy.setStatus('current')
sunPlatNumericSensorLowerThresholdNonCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorLowerThresholdNonCritical.setStatus('current')
sunPlatNumericSensorUpperThresholdNonCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorUpperThresholdNonCritical.setStatus('current')
sunPlatNumericSensorLowerThresholdCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorLowerThresholdCritical.setStatus('current')
sunPlatNumericSensorUpperThresholdCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorUpperThresholdCritical.setStatus('current')
sunPlatNumericSensorLowerThresholdFatal = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorLowerThresholdFatal.setStatus('current')
sunPlatNumericSensorUpperThresholdFatal = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorUpperThresholdFatal.setStatus('current')
sunPlatNumericSensorHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatNumericSensorHysteresis.setStatus('current')
sunPlatNumericSensorEnabledThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 15), SunPlatNumericSensorEnabledThresholds()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorEnabledThresholds.setStatus('current')
sunPlatNumericSensorRestoreDefaultThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 16), SunPlatNumericSensorThresholdResetAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatNumericSensorRestoreDefaultThresholds.setStatus('current')
sunPlatDiscreteSensorTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 9), )
if mibBuilder.loadTexts: sunPlatDiscreteSensorTable.setStatus('current')
sunPlatDiscreteSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 9, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatDiscreteSensorEntry.setStatus('current')
sunPlatDiscreteSensorCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 9, 1, 1), SunPlatIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatDiscreteSensorCurrent.setStatus('current')
sunPlatDiscreteSensorStatesTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10), )
if mibBuilder.loadTexts: sunPlatDiscreteSensorStatesTable.setStatus('current')
sunPlatDiscreteSensorStatesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "SUN-PLATFORM-MIB", "sunPlatDiscreteSensorStatesIndex"))
if mibBuilder.loadTexts: sunPlatDiscreteSensorStatesEntry.setStatus('current')
sunPlatDiscreteSensorStatesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1, 1), SunPlatIndex())
if mibBuilder.loadTexts: sunPlatDiscreteSensorStatesIndex.setStatus('current')
sunPlatDiscreteSensorStatesInterpretation = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatDiscreteSensorStatesInterpretation.setStatus('current')
sunPlatDiscreteSensorStatesAcceptable = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatDiscreteSensorStatesAcceptable.setStatus('current')
sunPlatFanTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 11), )
if mibBuilder.loadTexts: sunPlatFanTable.setStatus('current')
sunPlatFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 11, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatFanEntry.setStatus('current')
sunPlatFanClass = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 11, 1, 1), SunPlatFanClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatFanClass.setStatus('current')
sunPlatAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12), )
if mibBuilder.loadTexts: sunPlatAlarmTable.setStatus('current')
sunPlatAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatAlarmEntry.setStatus('current')
sunPlatAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1, 1), SunPlatAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatAlarmType.setStatus('current')
sunPlatAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1, 2), SunPlatAlarmState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatAlarmState.setStatus('current')
sunPlatAlarmUrgency = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1, 3), SunPlatAlarmUrgency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatAlarmUrgency.setStatus('current')
sunPlatWatchdogTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13), )
if mibBuilder.loadTexts: sunPlatWatchdogTable.setStatus('current')
sunPlatWatchdogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatWatchdogEntry.setStatus('current')
sunPlatWatchdogTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 1), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatWatchdogTimeout.setStatus('current')
sunPlatWatchdogAction = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 2), SunPlatWatchdogAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatWatchdogAction.setStatus('current')
sunPlatWatchdogLastExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatWatchdogLastExpired.setStatus('current')
sunPlatWatchdogMonitoredEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 4), SunPlatWatchdogMonitoredEntity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatWatchdogMonitoredEntity.setStatus('current')
sunPlatPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 14), )
if mibBuilder.loadTexts: sunPlatPowerSupplyTable.setStatus('current')
sunPlatPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 14, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatPowerSupplyEntry.setStatus('current')
sunPlatPowerSupplyClass = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 14, 1, 1), SunPlatPowerSupplyClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatPowerSupplyClass.setStatus('current')
sunPlatBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 15), )
if mibBuilder.loadTexts: sunPlatBatteryTable.setStatus('current')
sunPlatBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 15, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sunPlatBatteryEntry.setStatus('current')
sunPlatBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 15, 1, 1), SunPlatBatteryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatBatteryStatus.setStatus('current')
sunPlatLogicalTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1), )
if mibBuilder.loadTexts: sunPlatLogicalTable.setStatus('current')
sunPlatLogicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1, 1), )
entLogicalEntry.registerAugmentions(("SUN-PLATFORM-MIB", "sunPlatLogicalEntry"))
sunPlatLogicalEntry.setIndexNames(*entLogicalEntry.getIndexNames())
if mibBuilder.loadTexts: sunPlatLogicalEntry.setStatus('current')
sunPlatLogicalClass = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1, 1, 1), SunPlatLogicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogicalClass.setStatus('current')
sunPlatLogicalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1, 1, 2), SunPlatLogicalStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogicalStatus.setStatus('current')
sunPlatUnitaryComputerSystemTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2), )
if mibBuilder.loadTexts: sunPlatUnitaryComputerSystemTable.setStatus('current')
sunPlatUnitaryComputerSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"))
if mibBuilder.loadTexts: sunPlatUnitaryComputerSystemEntry.setStatus('current')
sunPlatUnitaryComputerSystemPowerState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2, 1, 1), SunPlatUnitaryComputerSystemPowerState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatUnitaryComputerSystemPowerState.setStatus('current')
sunPlatUnitaryComputerSystemApplySettings = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2, 1, 2), SunPlatUnitaryComputerSystemApplicableSetting()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatUnitaryComputerSystemApplySettings.setStatus('current')
sunPlatInitialLoadInfoTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3), )
if mibBuilder.loadTexts: sunPlatInitialLoadInfoTable.setStatus('current')
sunPlatInitialLoadInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"), (0, "SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoIndex"))
if mibBuilder.loadTexts: sunPlatInitialLoadInfoEntry.setStatus('current')
sunPlatInitialLoadInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 1), SunPlatIndex())
if mibBuilder.loadTexts: sunPlatInitialLoadInfoIndex.setStatus('current')
sunPlatInitialLoadInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatInitialLoadInfoDescr.setStatus('current')
sunPlatInitialLoadInfoCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatInitialLoadInfoCurrentValue.setStatus('current')
sunPlatInitialLoadInfoDesiredValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 4), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatInitialLoadInfoDesiredValue.setStatus('current')
sunPlatLogTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1), )
if mibBuilder.loadTexts: sunPlatLogTable.setStatus('current')
sunPlatLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1), ).setIndexNames((0, "SUN-PLATFORM-MIB", "sunPlatLogType"))
if mibBuilder.loadTexts: sunPlatLogEntry.setStatus('current')
sunPlatLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: sunPlatLogType.setStatus('current')
sunPlatLogAdministrativeState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 2), SunPlatLogAdministrativeState().clone('unlocked')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sunPlatLogAdministrativeState.setStatus('current')
sunPlatLogOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 3), SunPlatOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogOperationalState.setStatus('current')
sunPlatLogFullStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogFullStatus.setStatus('current')
sunPlatLogCapacityThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 5), SunPlatPercentage()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sunPlatLogCapacityThreshold.setStatus('current')
sunPlatLogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sunPlatLogRowStatus.setStatus('current')
sunPlatLogRecordTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2), )
if mibBuilder.loadTexts: sunPlatLogRecordTable.setStatus('current')
sunPlatLogRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1), ).setIndexNames((0, "SUN-PLATFORM-MIB", "sunPlatLogType"), (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"))
if mibBuilder.loadTexts: sunPlatLogRecordEntry.setStatus('current')
sunPlatLogRecordId = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: sunPlatLogRecordId.setStatus('current')
sunPlatLogRecordLoggingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordLoggingTime.setStatus('current')
sunPlatLogRecordManagedObjectInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 3), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordManagedObjectInstance.setStatus('current')
sunPlatLogRecordRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunPlatLogRecordRowStatus.setStatus('current')
sunPlatLogRecordCorrelatedNotifications = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordCorrelatedNotifications.setStatus('current')
sunPlatLogRecordAdditionalTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3), )
if mibBuilder.loadTexts: sunPlatLogRecordAdditionalTable.setStatus('current')
sunPlatLogRecordAdditionalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3, 1), ).setIndexNames((0, "SUN-PLATFORM-MIB", "sunPlatLogType"), (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"))
if mibBuilder.loadTexts: sunPlatLogRecordAdditionalEntry.setStatus('current')
sunPlatLogRecordAdditionalInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordAdditionalInfo.setStatus('current')
sunPlatLogRecordAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordAdditionalText.setStatus('current')
sunPlatLogRecordAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4), )
if mibBuilder.loadTexts: sunPlatLogRecordAlarmTable.setStatus('current')
sunPlatLogRecordAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1), ).setIndexNames((0, "SUN-PLATFORM-MIB", "sunPlatLogType"), (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"))
if mibBuilder.loadTexts: sunPlatLogRecordAlarmEntry.setStatus('current')
sunPlatLogRecordAlarmPerceivedSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 1), SunPlatAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordAlarmPerceivedSeverity.setStatus('current')
sunPlatLogRecordAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 2), SunPlatProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordAlarmProbableCause.setStatus('current')
sunPlatLogRecordAlarmSpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordAlarmSpecificProblem.setStatus('current')
sunPlatLogRecordAlarmRepairAction = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordAlarmRepairAction.setStatus('current')
sunPlatLogRecordChangeTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5), )
if mibBuilder.loadTexts: sunPlatLogRecordChangeTable.setStatus('current')
sunPlatLogRecordChangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1), ).setIndexNames((0, "SUN-PLATFORM-MIB", "sunPlatLogType"), (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"))
if mibBuilder.loadTexts: sunPlatLogRecordChangeEntry.setStatus('current')
sunPlatLogRecordChangeChangedOID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 1), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeChangedOID.setStatus('current')
sunPlatLogRecordChangeNewInteger = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeNewInteger.setStatus('current')
sunPlatLogRecordChangeOldInteger = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeOldInteger.setStatus('current')
sunPlatLogRecordChangeNewString = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeNewString.setStatus('current')
sunPlatLogRecordChangeOldString = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeOldString.setStatus('current')
sunPlatLogRecordChangeNewOID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeNewOID.setStatus('current')
sunPlatLogRecordChangeOldOID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunPlatLogRecordChangeOldOID.setStatus('current')
sunPlatNotificationEventId = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationEventId.setStatus('current')
sunPlatNotificationTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 2), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationTime.setStatus('current')
sunPlatNotificationObject = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 3), RowPointer()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationObject.setStatus('current')
sunPlatNotificationPerceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 4), SunPlatAlarmPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationPerceivedSeverity.setStatus('current')
sunPlatNotificationProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 5), SunPlatProbableCause()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationProbableCause.setStatus('current')
sunPlatNotificationSpecificProblem = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 6), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationSpecificProblem.setStatus('current')
sunPlatNotificationRepairAction = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 7), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationRepairAction.setStatus('current')
sunPlatNotificationAdditionalInfo = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 8), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationAdditionalInfo.setStatus('current')
sunPlatNotificationAdditionalText = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 9), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationAdditionalText.setStatus('current')
sunPlatNotificationChangedOID = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 10), VariablePointer()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationChangedOID.setStatus('current')
sunPlatNotificationNewInteger = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationNewInteger.setStatus('current')
sunPlatNotificationOldInteger = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 12), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationOldInteger.setStatus('current')
sunPlatNotificationNewString = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 13), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationNewString.setStatus('current')
sunPlatNotificationOldString = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 14), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationOldString.setStatus('current')
sunPlatNotificationNewOID = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 15), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationNewOID.setStatus('current')
sunPlatNotificationOldOID = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 16), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationOldOID.setStatus('current')
sunPlatNotificationCorrelatedNotifications = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 17), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sunPlatNotificationCorrelatedNotifications.setStatus('current')
sunPlatObjectCreation = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 1)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"))
if mibBuilder.loadTexts: sunPlatObjectCreation.setStatus('current')
sunPlatObjectDeletion = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 2)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"))
if mibBuilder.loadTexts: sunPlatObjectDeletion.setStatus('current')
sunPlatCommunicationsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 3)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
if mibBuilder.loadTexts: sunPlatCommunicationsAlarm.setStatus('current')
sunPlatEnvironmentalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 4)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
if mibBuilder.loadTexts: sunPlatEnvironmentalAlarm.setStatus('current')
sunPlatEquipmentAlarm = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 5)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
if mibBuilder.loadTexts: sunPlatEquipmentAlarm.setStatus('current')
sunPlatProcessingErrorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 6)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
if mibBuilder.loadTexts: sunPlatProcessingErrorAlarm.setStatus('current')
sunPlatStateChange = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 7)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldInteger"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewInteger"))
if mibBuilder.loadTexts: sunPlatStateChange.setStatus('current')
sunPlatAttributeChangeInteger = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 8)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldInteger"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewInteger"))
if mibBuilder.loadTexts: sunPlatAttributeChangeInteger.setStatus('current')
sunPlatAttributeChangeString = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 9)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldString"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewString"))
if mibBuilder.loadTexts: sunPlatAttributeChangeString.setStatus('current')
sunPlatAttributeChangeOID = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 10)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewOID"))
if mibBuilder.loadTexts: sunPlatAttributeChangeOID.setStatus('current')
sunPlatQualityOfServiceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 11)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
if mibBuilder.loadTexts: sunPlatQualityOfServiceAlarm.setStatus('current')
sunPlatIndeterminateAlarm = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 12)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
if mibBuilder.loadTexts: sunPlatIndeterminateAlarm.setStatus('current')
sunPlatCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 1, 1)).setObjects(("SUN-PLATFORM-MIB", "sunPlatGeneralGroup"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentGroup"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderGroup"), ("SUN-PLATFORM-MIB", "sunPlatCircuitPackGroup"), ("SUN-PLATFORM-MIB", "sunPlatPhysicalGroup"), ("SUN-PLATFORM-MIB", "sunPlatSensorGroup"), ("SUN-PLATFORM-MIB", "sunPlatBinarySensorGroup"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorGroup"), ("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorGroup"), ("SUN-PLATFORM-MIB", "sunPlatFanGroup"), ("SUN-PLATFORM-MIB", "sunPlatAlarmGroup"), ("SUN-PLATFORM-MIB", "sunPlatWatchdogGroup"), ("SUN-PLATFORM-MIB", "sunPlatPowerSupplyGroup"), ("SUN-PLATFORM-MIB", "sunPlatBatteryGroup"), ("SUN-PLATFORM-MIB", "sunPlatLogicalGroup"), ("SUN-PLATFORM-MIB", "sunPlatUnitaryComputerSystemGroup"), ("SUN-PLATFORM-MIB", "sunPlatLogGroup"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordGroup"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordAdditionalGroup"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmGroup"), ("SUN-PLATFORM-MIB", "sunPlatNotificationsGroup"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatCompliance = sunPlatCompliance.setStatus('current')
sunPlatGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 1)).setObjects(("SUN-PLATFORM-MIB", "sunPlatStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatGeneralGroup = sunPlatGeneralGroup.setStatus('current')
sunPlatEquipmentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 2)).setObjects(("SUN-PLATFORM-MIB", "sunPlatEquipmentOperationalState"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentAdministrativeState"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentAlarmStatus"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentUnknownStatus"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentLocationName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatEquipmentGroup = sunPlatEquipmentGroup.setStatus('current')
sunPlatEquipmentHolderGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 3)).setObjects(("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderType"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderAcceptableTypes"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderStatus"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderPowered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatEquipmentHolderGroup = sunPlatEquipmentHolderGroup.setStatus('current')
sunPlatCircuitPackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 4)).setObjects(("SUN-PLATFORM-MIB", "sunPlatCircuitPackType"), ("SUN-PLATFORM-MIB", "sunPlatCircuitPackAvailabilityStatus"), ("SUN-PLATFORM-MIB", "sunPlatCircuitPackReplaceable"), ("SUN-PLATFORM-MIB", "sunPlatCircuitPackHotSwappable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatCircuitPackGroup = sunPlatCircuitPackGroup.setStatus('current')
sunPlatPhysicalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 5)).setObjects(("SUN-PLATFORM-MIB", "sunPlatPhysicalClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatPhysicalGroup = sunPlatPhysicalGroup.setStatus('current')
sunPlatSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 6)).setObjects(("SUN-PLATFORM-MIB", "sunPlatSensorClass"), ("SUN-PLATFORM-MIB", "sunPlatSensorType"), ("SUN-PLATFORM-MIB", "sunPlatSensorLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatSensorGroup = sunPlatSensorGroup.setStatus('current')
sunPlatBinarySensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 7)).setObjects(("SUN-PLATFORM-MIB", "sunPlatBinarySensorCurrent"), ("SUN-PLATFORM-MIB", "sunPlatBinarySensorExpected"), ("SUN-PLATFORM-MIB", "sunPlatBinarySensorInterpretTrue"), ("SUN-PLATFORM-MIB", "sunPlatBinarySensorInterpretFalse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatBinarySensorGroup = sunPlatBinarySensorGroup.setStatus('current')
sunPlatNumericSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 8)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNumericSensorBaseUnits"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorExponent"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorRateUnits"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorCurrent"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorNormalMin"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorNormalMax"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorAccuracy"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorLowerThresholdNonCritical"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorUpperThresholdNonCritical"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorLowerThresholdCritical"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorUpperThresholdCritical"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorLowerThresholdFatal"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorUpperThresholdFatal"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorHysteresis"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorEnabledThresholds"), ("SUN-PLATFORM-MIB", "sunPlatNumericSensorRestoreDefaultThresholds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatNumericSensorGroup = sunPlatNumericSensorGroup.setStatus('current')
sunPlatDiscreteSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 9)).setObjects(("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorCurrent"), ("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorStatesInterpretation"), ("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorStatesAcceptable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatDiscreteSensorGroup = sunPlatDiscreteSensorGroup.setStatus('current')
sunPlatFanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 10)).setObjects(("SUN-PLATFORM-MIB", "sunPlatFanClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatFanGroup = sunPlatFanGroup.setStatus('current')
sunPlatAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 11)).setObjects(("SUN-PLATFORM-MIB", "sunPlatAlarmType"), ("SUN-PLATFORM-MIB", "sunPlatAlarmState"), ("SUN-PLATFORM-MIB", "sunPlatAlarmUrgency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatAlarmGroup = sunPlatAlarmGroup.setStatus('current')
sunPlatWatchdogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 12)).setObjects(("SUN-PLATFORM-MIB", "sunPlatWatchdogTimeout"), ("SUN-PLATFORM-MIB", "sunPlatWatchdogAction"), ("SUN-PLATFORM-MIB", "sunPlatWatchdogLastExpired"), ("SUN-PLATFORM-MIB", "sunPlatWatchdogMonitoredEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatWatchdogGroup = sunPlatWatchdogGroup.setStatus('current')
sunPlatPowerSupplyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 13)).setObjects(("SUN-PLATFORM-MIB", "sunPlatPowerSupplyClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatPowerSupplyGroup = sunPlatPowerSupplyGroup.setStatus('current')
sunPlatBatteryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 14)).setObjects(("SUN-PLATFORM-MIB", "sunPlatBatteryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatBatteryGroup = sunPlatBatteryGroup.setStatus('current')
sunPlatLogicalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 15)).setObjects(("SUN-PLATFORM-MIB", "sunPlatLogicalClass"), ("SUN-PLATFORM-MIB", "sunPlatLogicalStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatLogicalGroup = sunPlatLogicalGroup.setStatus('current')
sunPlatUnitaryComputerSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 16)).setObjects(("SUN-PLATFORM-MIB", "sunPlatUnitaryComputerSystemPowerState"), ("SUN-PLATFORM-MIB", "sunPlatUnitaryComputerSystemApplySettings"), ("SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoDescr"), ("SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoCurrentValue"), ("SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoDesiredValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatUnitaryComputerSystemGroup = sunPlatUnitaryComputerSystemGroup.setStatus('current')
sunPlatLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 17)).setObjects(("SUN-PLATFORM-MIB", "sunPlatLogAdministrativeState"), ("SUN-PLATFORM-MIB", "sunPlatLogOperationalState"), ("SUN-PLATFORM-MIB", "sunPlatLogFullStatus"), ("SUN-PLATFORM-MIB", "sunPlatLogCapacityThreshold"), ("SUN-PLATFORM-MIB", "sunPlatLogRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatLogGroup = sunPlatLogGroup.setStatus('current')
sunPlatLogRecordGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 18)).setObjects(("SUN-PLATFORM-MIB", "sunPlatLogRecordLoggingTime"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordManagedObjectInstance"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordRowStatus"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordCorrelatedNotifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatLogRecordGroup = sunPlatLogRecordGroup.setStatus('current')
sunPlatLogRecordAdditionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 19)).setObjects(("SUN-PLATFORM-MIB", "sunPlatLogRecordAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordAdditionalText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatLogRecordAdditionalGroup = sunPlatLogRecordAdditionalGroup.setStatus('current')
sunPlatLogRecordAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 20)).setObjects(("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmRepairAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatLogRecordAlarmGroup = sunPlatLogRecordAlarmGroup.setStatus('current')
sunPlatLogRecordChangeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 21)).setObjects(("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeChangedOID"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeNewInteger"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeOldInteger"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeNewString"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeOldString"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeNewOID"), ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeOldOID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatLogRecordChangeGroup = sunPlatLogRecordChangeGroup.setStatus('current')
sunPlatNotificationObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 22)).setObjects(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"), ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"), ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"), ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"), ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"), ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"), ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"), ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"), ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewInteger"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldInteger"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewString"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldString"), ("SUN-PLATFORM-MIB", "sunPlatNotificationNewOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationOldOID"), ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatNotificationObjectGroup = sunPlatNotificationObjectGroup.setStatus('current')
sunPlatNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 2, 1)).setObjects(("SUN-PLATFORM-MIB", "sunPlatObjectCreation"), ("SUN-PLATFORM-MIB", "sunPlatObjectDeletion"), ("SUN-PLATFORM-MIB", "sunPlatCommunicationsAlarm"), ("SUN-PLATFORM-MIB", "sunPlatEnvironmentalAlarm"), ("SUN-PLATFORM-MIB", "sunPlatEquipmentAlarm"), ("SUN-PLATFORM-MIB", "sunPlatProcessingErrorAlarm"), ("SUN-PLATFORM-MIB", "sunPlatStateChange"), ("SUN-PLATFORM-MIB", "sunPlatAttributeChangeInteger"), ("SUN-PLATFORM-MIB", "sunPlatAttributeChangeString"), ("SUN-PLATFORM-MIB", "sunPlatAttributeChangeOID"), ("SUN-PLATFORM-MIB", "sunPlatQualityOfServiceAlarm"), ("SUN-PLATFORM-MIB", "sunPlatIndeterminateAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sunPlatNotificationsGroup = sunPlatNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("SUN-PLATFORM-MIB", sunPlatNotificationRepairAction=sunPlatNotificationRepairAction, sunPlatEquipmentHolderGroup=sunPlatEquipmentHolderGroup, sunPlatMIBGroups=sunPlatMIBGroups, SunPlatPowerSupplyClass=SunPlatPowerSupplyClass, sunPlatBinarySensorEntry=sunPlatBinarySensorEntry, sunPlatLogRowStatus=sunPlatLogRowStatus, sunPlatNotificationAdditionalInfo=sunPlatNotificationAdditionalInfo, sunPlatNumericSensorUpperThresholdNonCritical=sunPlatNumericSensorUpperThresholdNonCritical, sunPlatNumericSensorEnabledThresholds=sunPlatNumericSensorEnabledThresholds, sunPlatAlarmUrgency=sunPlatAlarmUrgency, sunPlatLogRecordAdditionalTable=sunPlatLogRecordAdditionalTable, sunPlatSensorGroup=sunPlatSensorGroup, sunPlatBinarySensorTable=sunPlatBinarySensorTable, SunPlatOperationalState=SunPlatOperationalState, sunPlatSensorEntry=sunPlatSensorEntry, sunPlatDiscreteSensorTable=sunPlatDiscreteSensorTable, sunPlatLogRecordAdditionalInfo=sunPlatLogRecordAdditionalInfo, SunPlatEquipmentHolderType=SunPlatEquipmentHolderType, sunPlatLogEntry=sunPlatLogEntry, sunPlatBatteryTable=sunPlatBatteryTable, SunPlatRateUnits=SunPlatRateUnits, sunPlatDiscreteSensorStatesEntry=sunPlatDiscreteSensorStatesEntry, sunPlatEquipmentTable=sunPlatEquipmentTable, sunPlatPhysicalGroup=sunPlatPhysicalGroup, sunPlatLogRecordManagedObjectInstance=sunPlatLogRecordManagedObjectInstance, sunPlatMIBPhysicalObjects=sunPlatMIBPhysicalObjects, sunPlatLogRecordAlarmRepairAction=sunPlatLogRecordAlarmRepairAction, SunPlatAlarmState=SunPlatAlarmState, SunPlatAdministrativeState=SunPlatAdministrativeState, sunPlatNotificationOldInteger=sunPlatNotificationOldInteger, sunPlatNotificationAdditionalText=sunPlatNotificationAdditionalText, sunPlatLogicalEntry=sunPlatLogicalEntry, sunPlatEquipmentHolderPowered=sunPlatEquipmentHolderPowered, SunPlatCircuitPackAvailabilityStatus=SunPlatCircuitPackAvailabilityStatus, sunPlatBinarySensorExpected=sunPlatBinarySensorExpected, sunPlatUnitaryComputerSystemTable=sunPlatUnitaryComputerSystemTable, SunPlatWatchdogAction=SunPlatWatchdogAction, SunPlatAlarmUrgency=SunPlatAlarmUrgency, sunPlatNotificationCorrelatedNotifications=sunPlatNotificationCorrelatedNotifications, sunPlatStartTime=sunPlatStartTime, sunPlatPhysicalClass=sunPlatPhysicalClass, SunPlatBaseUnits=SunPlatBaseUnits, sunPlatPowerSupplyTable=sunPlatPowerSupplyTable, sunPlatLogRecordRowStatus=sunPlatLogRecordRowStatus, sunPlatNumericSensorGroup=sunPlatNumericSensorGroup, sunPlatMIBConformances=sunPlatMIBConformances, sunPlatWatchdogGroup=sunPlatWatchdogGroup, sunPlatUnitaryComputerSystemPowerState=sunPlatUnitaryComputerSystemPowerState, sunPlatMIBNotifGroups=sunPlatMIBNotifGroups, sunPlatLogRecordAlarmProbableCause=sunPlatLogRecordAlarmProbableCause, sunPlatQualityOfServiceAlarm=sunPlatQualityOfServiceAlarm, sunPlatPhysicalEntry=sunPlatPhysicalEntry, sunPlatCircuitPackAvailabilityStatus=sunPlatCircuitPackAvailabilityStatus, sunPlatCircuitPackHotSwappable=sunPlatCircuitPackHotSwappable, sunPlatAlarmTable=sunPlatAlarmTable, sunPlatEquipmentUnknownStatus=sunPlatEquipmentUnknownStatus, sunPlatNumericSensorUpperThresholdCritical=sunPlatNumericSensorUpperThresholdCritical, sunPlatObjectCreation=sunPlatObjectCreation, sunPlatInitialLoadInfoCurrentValue=sunPlatInitialLoadInfoCurrentValue, sunPlatLogRecordCorrelatedNotifications=sunPlatLogRecordCorrelatedNotifications, sunPlatLogAdministrativeState=sunPlatLogAdministrativeState, sunPlatLogRecordId=sunPlatLogRecordId, sunPlatIndeterminateAlarm=sunPlatIndeterminateAlarm, sunPlatNumericSensorLowerThresholdCritical=sunPlatNumericSensorLowerThresholdCritical, sunPlatNumericSensorUpperThresholdFatal=sunPlatNumericSensorUpperThresholdFatal, SunPlatPhysicalClass=SunPlatPhysicalClass, SunPlatLogicalStatus=SunPlatLogicalStatus, SunPlatBatteryStatus=SunPlatBatteryStatus, sunPlatCommunicationsAlarm=sunPlatCommunicationsAlarm, sunPlatFanGroup=sunPlatFanGroup, sunPlatNumericSensorRestoreDefaultThresholds=sunPlatNumericSensorRestoreDefaultThresholds, sunPlatLogRecordChangeGroup=sunPlatLogRecordChangeGroup, sunPlatBinarySensorCurrent=sunPlatBinarySensorCurrent, sunPlatEquipmentGroup=sunPlatEquipmentGroup, sunPlatUnitaryComputerSystemGroup=sunPlatUnitaryComputerSystemGroup, sunPlatAttributeChangeString=sunPlatAttributeChangeString, sunPlatPowerSupplyGroup=sunPlatPowerSupplyGroup, sunPlatDiscreteSensorStatesInterpretation=sunPlatDiscreteSensorStatesInterpretation, sunPlatLogRecordAdditionalGroup=sunPlatLogRecordAdditionalGroup, sunPlatMIBLogs=sunPlatMIBLogs, sunPlatNotificationObject=sunPlatNotificationObject, sunPlatNotificationEventId=sunPlatNotificationEventId, SunPlatFanClass=SunPlatFanClass, sunPlatBinarySensorGroup=sunPlatBinarySensorGroup, sunPlatEquipmentHolderStatus=sunPlatEquipmentHolderStatus, sunPlatEquipmentAlarm=sunPlatEquipmentAlarm, PYSNMP_MODULE_ID=sunPlatMIB, sunPlatLogRecordChangeNewOID=sunPlatLogRecordChangeNewOID, SunPlatSensorClass=SunPlatSensorClass, sunPlatPowerSupplyEntry=sunPlatPowerSupplyEntry, sunPlatEquipmentHolderType=sunPlatEquipmentHolderType, sunPlatLogRecordAlarmEntry=sunPlatLogRecordAlarmEntry, sunPlatEquipmentHolderEntry=sunPlatEquipmentHolderEntry, sunPlatLogRecordChangeChangedOID=sunPlatLogRecordChangeChangedOID, sunPlatBatteryEntry=sunPlatBatteryEntry, sunPlatLogRecordAlarmPerceivedSeverity=sunPlatLogRecordAlarmPerceivedSeverity, sunPlatAlarmType=sunPlatAlarmType, sunPlatDiscreteSensorStatesTable=sunPlatDiscreteSensorStatesTable, sunPlatNotificationOldOID=sunPlatNotificationOldOID, SunPlatLogicalClass=SunPlatLogicalClass, sunPlatNotificationNewInteger=sunPlatNotificationNewInteger, SunPlatPercentage=SunPlatPercentage, sunPlatSensorType=sunPlatSensorType, SunPlatProbableCause=SunPlatProbableCause, sunPlatEquipmentLocationName=sunPlatEquipmentLocationName, sunPlatNumericSensorRateUnits=sunPlatNumericSensorRateUnits, sunPlatDiscreteSensorCurrent=sunPlatDiscreteSensorCurrent, sunPlatLogRecordChangeTable=sunPlatLogRecordChangeTable, SunPlatAlarmStatus=SunPlatAlarmStatus, sunPlatNumericSensorNormalMax=sunPlatNumericSensorNormalMax, SunPlatSensorType=SunPlatSensorType, sunPlatAttributeChangeOID=sunPlatAttributeChangeOID, sunPlatLogRecordChangeNewInteger=sunPlatLogRecordChangeNewInteger, sunPlatLogRecordChangeOldInteger=sunPlatLogRecordChangeOldInteger, sunPlatFanClass=sunPlatFanClass, sunPlatLogRecordAdditionalText=sunPlatLogRecordAdditionalText, sunPlatUnitaryComputerSystemEntry=sunPlatUnitaryComputerSystemEntry, sunPlatNotificationObjectGroup=sunPlatNotificationObjectGroup, sunPlatMIB=sunPlatMIB, sunPlatNumericSensorExponent=sunPlatNumericSensorExponent, sunPlatLogGroup=sunPlatLogGroup, sunPlatLogicalStatus=sunPlatLogicalStatus, sunPlatDiscreteSensorStatesAcceptable=sunPlatDiscreteSensorStatesAcceptable, sunPlatCompliance=sunPlatCompliance, sunPlatMIBLogicalObjects=sunPlatMIBLogicalObjects, sunPlatMIBObjectGroups=sunPlatMIBObjectGroups, sunPlatEquipmentOperationalState=sunPlatEquipmentOperationalState, sunPlatSensorClass=sunPlatSensorClass, sunPlatDiscreteSensorStatesIndex=sunPlatDiscreteSensorStatesIndex, sunPlatMIBObjects=sunPlatMIBObjects, sunPlatFanEntry=sunPlatFanEntry, sunPlatPhysicalTable=sunPlatPhysicalTable, sunPlatNumericSensorAccuracy=sunPlatNumericSensorAccuracy, SunPlatUnitaryComputerSystemApplicableSetting=SunPlatUnitaryComputerSystemApplicableSetting, sunPlatNotificationProbableCause=sunPlatNotificationProbableCause, sunPlatLogRecordAlarmGroup=sunPlatLogRecordAlarmGroup, sunPlatEquipmentEntry=sunPlatEquipmentEntry, sunPlatMIBCompliances=sunPlatMIBCompliances, SunPlatAlarmPerceivedSeverity=SunPlatAlarmPerceivedSeverity, sunPlatLogTable=sunPlatLogTable, sunPlatLogRecordAdditionalEntry=sunPlatLogRecordAdditionalEntry, sunPlatInitialLoadInfoTable=sunPlatInitialLoadInfoTable, sunPlatInitialLoadInfoIndex=sunPlatInitialLoadInfoIndex, sunPlatAlarmState=sunPlatAlarmState, SunPlatLogAdministrativeState=SunPlatLogAdministrativeState, sunPlatNumericSensorBaseUnits=sunPlatNumericSensorBaseUnits, sunPlatStateChange=sunPlatStateChange, sunPlatMIBTrapPrefix=sunPlatMIBTrapPrefix, sunPlatProcessingErrorAlarm=sunPlatProcessingErrorAlarm, sunPlatNumericSensorNormalMin=sunPlatNumericSensorNormalMin, sunPlatNumericSensorCurrent=sunPlatNumericSensorCurrent, SunPlatAlarmType=SunPlatAlarmType, sunPlatMIBTrapData=sunPlatMIBTrapData, sunPlatEquipmentAdministrativeState=sunPlatEquipmentAdministrativeState, sunPlatWatchdogTable=sunPlatWatchdogTable, sunPlatInitialLoadInfoDescr=sunPlatInitialLoadInfoDescr, SunPlatEquipmentHolderPower=SunPlatEquipmentHolderPower, sunPlatNotificationsGroup=sunPlatNotificationsGroup, sunPlatLogType=sunPlatLogType, sunPlatWatchdogAction=sunPlatWatchdogAction, sunPlatMIBTraps=sunPlatMIBTraps, SunPlatIndex=SunPlatIndex, sunPlatNumericSensorLowerThresholdFatal=sunPlatNumericSensorLowerThresholdFatal, sunPlatCircuitPackReplaceable=sunPlatCircuitPackReplaceable, sunPlatCircuitPackEntry=sunPlatCircuitPackEntry, sunPlatEquipmentHolderTable=sunPlatEquipmentHolderTable, products=products, sunPlatCircuitPackType=sunPlatCircuitPackType, sunPlatLogRecordTable=sunPlatLogRecordTable, sunPlatLogRecordAlarmSpecificProblem=sunPlatLogRecordAlarmSpecificProblem, sunPlatEnvironmentalAlarm=sunPlatEnvironmentalAlarm, SunPlatNumericSensorEnabledThresholds=SunPlatNumericSensorEnabledThresholds, sunPlatLogRecordLoggingTime=sunPlatLogRecordLoggingTime, sunPlatLogRecordChangeOldString=sunPlatLogRecordChangeOldString, SunPlatUnitaryComputerSystemPowerState=SunPlatUnitaryComputerSystemPowerState, sunPlatAlarmGroup=sunPlatAlarmGroup, sunPlatUnitaryComputerSystemApplySettings=sunPlatUnitaryComputerSystemApplySettings, sunPlatLogFullStatus=sunPlatLogFullStatus, sunPlatAttributeChangeInteger=sunPlatAttributeChangeInteger, sunPlatLogicalClass=sunPlatLogicalClass, sunPlatLogRecordChangeEntry=sunPlatLogRecordChangeEntry, sunPlatSensorLatency=sunPlatSensorLatency, sunPlatNumericSensorLowerThresholdNonCritical=sunPlatNumericSensorLowerThresholdNonCritical, sunPlatNotificationOldString=sunPlatNotificationOldString, sun=sun, sunPlatLogCapacityThreshold=sunPlatLogCapacityThreshold, sunPlatEquipmentHolderAcceptableTypes=sunPlatEquipmentHolderAcceptableTypes, sunPlatObjectDeletion=sunPlatObjectDeletion, sunPlatNotificationNewOID=sunPlatNotificationNewOID, sunPlatWatchdogLastExpired=sunPlatWatchdogLastExpired, sunPlatWatchdogEntry=sunPlatWatchdogEntry, sunPlatCircuitPackGroup=sunPlatCircuitPackGroup, sunPlatSensorTable=sunPlatSensorTable, sunPlatInitialLoadInfoDesiredValue=sunPlatInitialLoadInfoDesiredValue, sunPlatBatteryStatus=sunPlatBatteryStatus, sunPlatCircuitPackTable=sunPlatCircuitPackTable, sunPlatDiscreteSensorEntry=sunPlatDiscreteSensorEntry, sunPlatNumericSensorEntry=sunPlatNumericSensorEntry, sunPlatLogOperationalState=sunPlatLogOperationalState, sunPlatNotificationSpecificProblem=sunPlatNotificationSpecificProblem, sunPlatLogRecordGroup=sunPlatLogRecordGroup, SunPlatWatchdogMonitoredEntity=SunPlatWatchdogMonitoredEntity, sunPlatFanTable=sunPlatFanTable, sunPlatInitialLoadInfoEntry=sunPlatInitialLoadInfoEntry, sunPlatLogRecordChangeNewString=sunPlatLogRecordChangeNewString, sunPlatWatchdogTimeout=sunPlatWatchdogTimeout, sunFire=sunFire, sunPlatLogRecordEntry=sunPlatLogRecordEntry, sunPlatPowerSupplyClass=sunPlatPowerSupplyClass, SunPlatEquipmentHolderStatus=SunPlatEquipmentHolderStatus, sunPlatLogRecordAlarmTable=sunPlatLogRecordAlarmTable, sunPlatNotificationNewString=sunPlatNotificationNewString, sunPlatBinarySensorInterpretTrue=sunPlatBinarySensorInterpretTrue, sunPlatNumericSensorTable=sunPlatNumericSensorTable, sunPlatGeneralGroup=sunPlatGeneralGroup, sunPlatWatchdogMonitoredEntity=sunPlatWatchdogMonitoredEntity, sunPlatNotificationChangedOID=sunPlatNotificationChangedOID, sunPlatNumericSensorHysteresis=sunPlatNumericSensorHysteresis, sunPlatLogRecordChangeOldOID=sunPlatLogRecordChangeOldOID, sunPlatDiscreteSensorGroup=sunPlatDiscreteSensorGroup, sunPlatLogicalGroup=sunPlatLogicalGroup, sunPlatNotificationPerceivedSeverity=sunPlatNotificationPerceivedSeverity, sunPlatBatteryGroup=sunPlatBatteryGroup, sunPlatBinarySensorInterpretFalse=sunPlatBinarySensorInterpretFalse, sunPlatAlarmEntry=sunPlatAlarmEntry, sunPlatLogicalTable=sunPlatLogicalTable, sunPlatEquipmentAlarmStatus=sunPlatEquipmentAlarmStatus, SunPlatNumericSensorThresholdResetAction=SunPlatNumericSensorThresholdResetAction, sunPlatNotificationTime=sunPlatNotificationTime)
