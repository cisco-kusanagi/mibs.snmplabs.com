#
# PySNMP MIB module SPIDCOM-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPIDCOM-ALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
neMibAlarm, = mibBuilder.importSymbols("NE-ALARM-MIB", "neMibAlarm")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Integer32, IpAddress, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "IpAddress", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "iso")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
neAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 22764, 2, 1))
if mibBuilder.loadTexts: neAlarm.setLastUpdated('200207151330Z')
if mibBuilder.loadTexts: neAlarm.setOrganization('SPiDCOM')
if mibBuilder.loadTexts: neAlarm.setContactInfo(' TO BE SPECIFIED BY SPiDCOM ')
if mibBuilder.loadTexts: neAlarm.setDescription('Definition of the MIB tree structure to manage the Alarm Monitoring.')
class ItuAlarmProbableCause(TextualConvention, Integer32):
    description = 'ItuAlarmProbableCause is the probable cause according the ITU X.733.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75))
    namedValues = NamedValues(("other", 1), ("adapterError", 2), ("applicationSubsystemFailure", 3), ("bandwidthReduced", 4), ("callEstablishmentError", 5), ("communicationsProtocolError", 6), ("communicationsSubsystemFailure", 7), ("configurationOrCustomizationError", 8), ("congestion", 9), ("corruptData", 10), ("cpuCyclesLimitExceeded", 11), ("dataSetOrModemError", 12), ("degradedSignal", 13), ("dteDceInterfaceError", 14), ("enclosureDoorOpen", 15), ("equipmentMalfunction", 16), ("excessiveVibration", 17), ("fileError", 18), ("fireDetected", 19), ("floodDetected", 20), ("framingError", 21), ("heatingVentCoolingSystemProblem", 22), ("humidityUnacceptable", 23), ("inputOutputDeviceError", 24), ("inputDeviceError", 25), ("lanError", 26), ("leakDetected", 27), ("localNodeTransmissionError", 28), ("lossOfFrame", 29), ("lossOfSignal", 30), ("materialSupplyExhausted", 31), ("multiplexerProblem", 32), ("outOfMemory", 33), ("ouputDeviceError", 34), ("performanceDegraded", 35), ("powerProblem", 36), ("pressureUnacceptable", 37), ("processorProblem", 38), ("pumpFailure", 39), ("queueSizeExceeded", 40), ("receiveFailure", 41), ("receiverFailure", 42), ("remoteNodeTransmissionError", 43), ("resourceAtOrNearingCapacity", 44), ("responseTimeExecessive", 45), ("retransmissionRateExcessive", 46), ("softwareError", 47), ("softwareProgramAbnormallyTerminated", 48), ("softwareProgramError", 49), ("storageCapacityProblem", 50), ("temperatureUnacceptable", 51), ("thresholdCrossed", 52), ("timingProblem", 53), ("toxicLeakDetected", 54), ("transmitFailure", 55), ("transmitterFailure", 56), ("underlyingResourceUnavailable", 57), ("versionMismatch", 58), ("authenticationFailure", 59), ("breachOfConfidentiality", 60), ("cableTamper", 61), ("delayedInformation", 62), ("denialOfService", 63), ("duplicateInformation", 64), ("informationMissing", 65), ("informationModificationDetected", 66), ("informationOutOfSequence", 67), ("intrusionDetection", 68), ("keyExpired", 69), ("nonRepudiationFailure", 70), ("outOfHoursActivity", 71), ("outOfService", 72), ("proceduralError", 73), ("unauthorizedAccessAttempt", 74), ("unexpectedInformation", 75))

class ItuAlarmType(TextualConvention, Integer32):
    description = 'ItuAlarmType is the alarm type according the ITU X.733.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmentalAlarm", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViolation", 10), ("timeDomainViolation", 11))

class NeAlarmPhoto(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("takePhoto", 1))

class NeTrapFilter(TextualConvention, Integer32):
    description = 'Filtertype used for control of traps by manager. If trapFilterOn, the agent sends non traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("trapFilterOff", 0), ("trapFilterOn", 1))

neAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1), )
if mibBuilder.loadTexts: neAlarmTable.setStatus('current')
if mibBuilder.loadTexts: neAlarmTable.setDescription('neAlarmTable represents all the possible alarms on the NE, stating the probable cause, the alarm type and the perceived severity as per [X.733]. Note that each entry is significant until neAlarmIsApplicable is applicable(1). Entries should never be removed unless the NE they refer to disconnected NEs. To invalidate an entry the Agent sets neAlarmIsApplicable to notApplicable(0). before invalidating the entry, the agent sets the neAlarmPerceivedSeverity to cleared.')
neAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1), ).setIndexNames((0, "SPIDCOM-ALARM-MIB", "neAlarmIndex"))
if mibBuilder.loadTexts: neAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: neAlarmEntry.setDescription('neAlarmMibEntry: an entry in neAlarmMibTable. ')
neAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: neAlarmIndex.setDescription('neAlarmIndex is a unique identifier for an alarm on a given type of NE. The association between the alarmIndex and the alarm for the type of NE is described in the NE MIB. For example for the SRA L it is in the NETVIEWER SRAL 16X2 MIB. ')
neAlarmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmAdditionalText.setStatus('current')
if mibBuilder.loadTexts: neAlarmAdditionalText.setDescription('neAlarmDescription is a brief description of a given alarm. E.g. Tributary 1 Card Fail.')
neAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 3), ItuAlarmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmProbableCause.setStatus('current')
if mibBuilder.loadTexts: neAlarmProbableCause.setDescription('neAlarmProbablecause represents the probable cause values for the alarms as per [X.733]. ')
neAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmDescription.setStatus('current')
if mibBuilder.loadTexts: neAlarmDescription.setDescription('neAlarmDescription represents a description of the Alarm, as per [X.733] ')
neAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 5), ItuAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmType.setStatus('current')
if mibBuilder.loadTexts: neAlarmType.setDescription('neAlarmType represents the event type values for the alarms as per [X.733]. ')
neAlarmManagedObject = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmManagedObject.setStatus('current')
if mibBuilder.loadTexts: neAlarmManagedObject.setDescription('neAlarmManagedObject represents the managed Object values for the alarms. ')
neAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("terminate", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: neAlarmStatus.setDescription('If neAlarmStatus is active(1) the current alarm is active for the NE. If neAlarmStatus is inactive(2), the current alarm is inactive (normality) for the NE. If neAlarmStatus is notAffected(3), the current alarm is not significant for the NE.')
neAlarmAlreadyPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmAlreadyPresent.setStatus('current')
if mibBuilder.loadTexts: neAlarmAlreadyPresent.setDescription('This field could be use to know if alarm already there. ')
neAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmTimeStamp.setStatus('current')
if mibBuilder.loadTexts: neAlarmTimeStamp.setDescription('The alarm timestamp.')
neAlarmActiveLastTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmActiveLastTrapIndex.setStatus('current')
if mibBuilder.loadTexts: neAlarmActiveLastTrapIndex.setDescription('This is the Alarm Index sent for which the last trap was sent ')
neClearTerminatedAlarms = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neClearTerminatedAlarms.setStatus('current')
if mibBuilder.loadTexts: neClearTerminatedAlarms.setDescription('When the manager sets this object, the agent deletes its alarms which status is terminated ')
neAlarmActivePhoto = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmActivePhoto.setStatus('current')
if mibBuilder.loadTexts: neAlarmActivePhoto.setDescription('When the manager sets this object, the agent sends all the active alarms from neAlarmtable to the manager. ')
neAlarmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10))
neAlarmTrapCounter = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmTrapCounter.setStatus('current')
if mibBuilder.loadTexts: neAlarmTrapCounter.setDescription('This object counts only the traps sent under node neAlarmTrap.')
neAlarmTrapFilter = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 3), NeTrapFilter()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmTrapFilter.setStatus('current')
if mibBuilder.loadTexts: neAlarmTrapFilter.setDescription('If trapFilterOn, the agent sends no traps under node neAlarmTrap. ')
neAlarmTrapDestiIp = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmTrapDestiIp.setStatus('current')
if mibBuilder.loadTexts: neAlarmTrapDestiIp.setDescription('The @IP where traps are sent')
neAlarmTrapDestiPort = MibScalar((1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAlarmTrapDestiPort.setStatus('current')
if mibBuilder.loadTexts: neAlarmTrapDestiPort.setDescription('The UDP port where traps are sent')
neAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22764, 2, 1, 11)).setObjects(("SPIDCOM-ALARM-MIB", "neAlarmIndex"), ("SPIDCOM-ALARM-MIB", "neAlarmAdditionalText"), ("SPIDCOM-ALARM-MIB", "neAlarmProbableCause"), ("SPIDCOM-ALARM-MIB", "neAlarmDescription"), ("SPIDCOM-ALARM-MIB", "neAlarmType"), ("SPIDCOM-ALARM-MIB", "neAlarmManagedObject"), ("SPIDCOM-ALARM-MIB", "neAlarmAlreadyPresent"), ("SPIDCOM-ALARM-MIB", "neAlarmTimeStamp"), ("SPIDCOM-ALARM-MIB", "neAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    neAlarmGroup = neAlarmGroup.setStatus('current')
if mibBuilder.loadTexts: neAlarmGroup.setDescription('The objects you can find in this MIB.')
neAlarmActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22764, 2, 1, 13)).setObjects(("SPIDCOM-ALARM-MIB", "neAlarmActiveLastTrapIndex"), ("SPIDCOM-ALARM-MIB", "neAlarmActivePhoto"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapFilter"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapDestiIp"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapDestiPort"), ("SPIDCOM-ALARM-MIB", "neAlarmTrapCounter"), ("SPIDCOM-ALARM-MIB", "neClearTerminatedAlarms"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    neAlarmActiveGroup = neAlarmActiveGroup.setStatus('current')
if mibBuilder.loadTexts: neAlarmActiveGroup.setDescription('The object regarding active alarms')
mibBuilder.exportSymbols("SPIDCOM-ALARM-MIB", neAlarmTrap=neAlarmTrap, neAlarmGroup=neAlarmGroup, NeAlarmPhoto=NeAlarmPhoto, neAlarmTrapDestiPort=neAlarmTrapDestiPort, neAlarmProbableCause=neAlarmProbableCause, neAlarmTrapDestiIp=neAlarmTrapDestiIp, neAlarmManagedObject=neAlarmManagedObject, ItuAlarmType=ItuAlarmType, neClearTerminatedAlarms=neClearTerminatedAlarms, neAlarmActivePhoto=neAlarmActivePhoto, neAlarmStatus=neAlarmStatus, neAlarmDescription=neAlarmDescription, neAlarmActiveGroup=neAlarmActiveGroup, neAlarmType=neAlarmType, neAlarmTable=neAlarmTable, neAlarmTrapFilter=neAlarmTrapFilter, ItuAlarmProbableCause=ItuAlarmProbableCause, neAlarm=neAlarm, neAlarmTimeStamp=neAlarmTimeStamp, neAlarmTrapCounter=neAlarmTrapCounter, NeTrapFilter=NeTrapFilter, PYSNMP_MODULE_ID=neAlarm, neAlarmEntry=neAlarmEntry, neAlarmActiveLastTrapIndex=neAlarmActiveLastTrapIndex, neAlarmAlreadyPresent=neAlarmAlreadyPresent, neAlarmAdditionalText=neAlarmAdditionalText, neAlarmIndex=neAlarmIndex)
