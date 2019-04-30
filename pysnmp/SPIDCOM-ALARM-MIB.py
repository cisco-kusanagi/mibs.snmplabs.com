#
# PySNMP MIB module SPIDCOM-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPIDCOM-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
neMibAlarm, = mibBuilder.importSymbols("NE-ALARM-MIB", "neMibAlarm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, iso, Gauge32, NotificationType, Integer32, IpAddress, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "iso", "Gauge32", "NotificationType", "Integer32", "IpAddress", "Counter32", "MibIdentifier")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
neAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 22764, 2, 1))
if mibBuilder.loadTexts: neAlarm.setLastUpdated('200207151330Z')
if mibBuilder.loadTexts: neAlarm.setOrganization('SPiDCOM')
class ItuAlarmProbableCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75))
    namedValues = NamedValues(("other", 1), ("adapterError", 2), ("applicationSubsystemFailure", 3), ("bandwidthReduced", 4), ("callEstablishmentError", 5), ("communicationsProtocolError", 6), ("communicationsSubsystemFailure", 7), ("configurationOrCustomizationError", 8), ("congestion", 9), ("corruptData", 10), ("cpuCyclesLimitExceeded", 11), ("dataSetOrModemError", 12), ("degradedSignal", 13), ("dteDceInterfaceError", 14), ("enclosureDoorOpen", 15), ("equipmentMalfunction", 16), ("excessiveVibration", 17), ("fileError", 18), ("fireDetected", 19), ("floodDetected", 20), ("framingError", 21), ("heatingVentCoolingSystemProblem", 22), ("humidityUnacceptable", 23), ("inputOutputDeviceError", 24), ("inputDeviceError", 25), ("lanError", 26), ("leakDetected", 27), ("localNodeTransmissionError", 28), ("lossOfFrame", 29), ("lossOfSignal", 30), ("materialSupplyExhausted", 31), ("multiplexerProblem", 32), ("outOfMemory", 33), ("ouputDeviceError", 34), ("performanceDegraded", 35), ("powerProblem", 36), ("pressureUnacceptable", 37), ("processorProblem", 38), ("pumpFailure", 39), ("queueSizeExceeded", 40), ("receiveFailure", 41), ("receiverFailure", 42), ("remoteNodeTransmissionError", 43), ("resourceAtOrNearingCapacity", 44), ("responseTimeExecessive", 45), ("retransmissionRateExcessive", 46), ("softwareError", 47), ("softwareProgramAbnormallyTerminated", 48), ("softwareProgramError", 49), ("storageCapacityProblem", 50), ("temperatureUnacceptable", 51), ("thresholdCrossed", 52), ("timingProblem", 53), ("toxicLeakDetected", 54), ("transmitFailure", 55), ("transmitterFailure", 56), ("underlyingResourceUnavailable", 57), ("versionMismatch", 58), ("authenticationFailure", 59), ("breachOfConfidentiality", 60), ("cableTamper", 61), ("delayedInformation", 62), ("denialOfService", 63), ("duplicateInformation", 64), ("informationMissing", 65), ("informationModificationDetected", 66), ("informationOutOfSequence", 67), ("intrusionDetection", 68), ("keyExpired", 69), ("nonRepudiationFailure", 70), ("outOfHoursActivity", 71), ("outOfService", 72), ("proceduralError", 73), ("unauthorizedAccessAttempt", 74), ("unexpectedInformation", 75))

class ItuAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmentalAlarm", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViolation", 10), ("timeDomainViolation", 11))

class NeAlarmPhoto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("takePhoto", 1))

class NeTrapFilter(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("trapFilterOff", 0), ("trapFilterOn", 1))

neAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1), )
if mibBuilder.loadTexts: neAlarmTable.setStatus('current')
neAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1), ).setIndexNames((0, "SPIDCOM-ALARM-MIB", "neAlarmIndex"))
if mibBuilder.loadTexts: neAlarmEntry.setStatus('current')
neAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmIndex.setStatus('current')
neAlarmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmAdditionalText.setStatus('current')
neAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 3), ItuAlarmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmProbableCause.setStatus('current')
neAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmDescription.setStatus('current')
neAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 5), ItuAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmType.setStatus('current')
neAlarmManagedObject = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmManagedObject.setStatus('current')
neAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("terminate", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmStatus.setStatus('current')
neAlarmAlreadyPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmAlreadyPresent.setStatus('current')
neAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmTimeStamp.setStatus('current')
neAlarmActiveLastTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmActiveLastTrapIndex.setStatus('current')
neClearTerminatedAlarms = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neClearTerminatedAlarms.setStatus('current')
neAlarmActivePhoto = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmActivePhoto.setStatus('current')
neAlarmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10))
neAlarmTrapCounter = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmTrapCounter.setStatus('current')
neAlarmTrapFilter = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 3), NeTrapFilter()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmTrapFilter.setStatus('current')
neAlarmTrapDestiIp = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmTrapDestiIp.setStatus('current')
neAlarmTrapDestiPort = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmTrapDestiPort.setStatus('current')
neAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22764, 2, 1, 11)).setObjects(("SPIDCOM-ALARM-MIB", "neAlarmIndex"), ("SPIDCOM-ALARM-MIB", "neAlarmAdditionalText"), ("SPIDCOM-ALARM-MIB", "neAlarmProbableCause"), ("SPIDCOM-ALARM-MIB", "neAlarmDescription"), ("SPIDCOM-ALARM-MIB", "neAlarmType"), ("SPIDCOM-ALARM-MIB", "neAlarmManagedObject"), ("SPIDCOM-ALARM-MIB", "neAlarmAlreadyPresent"), ("SPIDCOM-ALARM-MIB", "neAlarmTimeStamp"), ("SPIDCOM-ALARM-MIB", "neAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    neAlarmGroup = neAlarmGroup.setStatus('current')
neAlarmActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22764, 2, 1, 13)).setObjects(("SPIDCOM-ALARM-MIB", "neAlarmActiveLastTrapIndex"), ("SPIDCOM-ALARM-MIB", "neAlarmActivePhoto"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapFilter"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapDestiIp"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapDestiPort"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapCounter"), ("SPIDCOM-ALARM-MIB", "neClearTerminatedAlarms"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    neAlarmActiveGroup = neAlarmActiveGroup.setStatus('current')
mibBuilder.exportSymbols("SPIDCOM-ALARM-MIB", neAlarmTable=neAlarmTable, NeTrapFilter=NeTrapFilter, neAlarmTrapDestiIp=neAlarmTrapDestiIp, neAlarmTrap=neAlarmTrap, neAlarmDescription=neAlarmDescription, neAlarmEntry=neAlarmEntry, neAlarm=neAlarm, neAlarmTrapDestiPort=neAlarmTrapDestiPort, NeAlarmPhoto=NeAlarmPhoto, neAlarmIndex=neAlarmIndex, neAlarmActiveLastTrapIndex=neAlarmActiveLastTrapIndex, neAlarmActivePhoto=neAlarmActivePhoto, neAlarmTimeStamp=neAlarmTimeStamp, neAlarmTrapCounter=neAlarmTrapCounter, neAlarmAlreadyPresent=neAlarmAlreadyPresent, PYSNMP_MODULE_ID=neAlarm, neAlarmStatus=neAlarmStatus, neAlarmProbableCause=neAlarmProbableCause, neClearTerminatedAlarms=neClearTerminatedAlarms, neAlarmTrapFilter=neAlarmTrapFilter, neAlarmGroup=neAlarmGroup, neAlarmAdditionalText=neAlarmAdditionalText, neAlarmType=neAlarmType, neAlarmActiveGroup=neAlarmActiveGroup, neAlarmManagedObject=neAlarmManagedObject, ItuAlarmType=ItuAlarmType, ItuAlarmProbableCause=ItuAlarmProbableCause)
