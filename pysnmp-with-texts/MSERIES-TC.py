#
# PySNMP MIB module MSERIES-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSERIES-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:15:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Bits, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Unsigned32, Counter64, TimeTicks, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Bits", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "TimeTicks", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smartTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 5))
smartTcMIB.setRevisions(('2014-02-12 13:27', '2013-10-15 13:41', '2011-12-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smartTcMIB.setRevisionsDescriptions(('Added PortStatus and PortMode.', 'Descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: smartTcMIB.setLastUpdated('201402121327Z')
if mibBuilder.loadTexts: smartTcMIB.setOrganization('SmartOptics')
if mibBuilder.loadTexts: smartTcMIB.setContactInfo('http://www.smartoptics.com')
if mibBuilder.loadTexts: smartTcMIB.setDescription('This is the enterprise specific TC MIB for SmartOptics M-Series')
class AlarmPerceivedSeverity(TextualConvention, Integer32):
    description = 'Alarm severity as defined in ITU-T X.733.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class AlarmNotificationType(TextualConvention, Integer32):
    description = 'Type of alarm as defined in ITU-T X.733.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmental", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViloation", 10), ("timeDomainViolation", 11))

class AlarmProbableCause(TextualConvention, Integer32):
    description = 'Alarm probable cause as defined in ITU-T X.733.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57))
    namedValues = NamedValues(("undefined", 0), ("adapterError", 1), ("applicationSubsystemFailure", 2), ("bandwidthReduced", 3), ("callEstablishmentError", 4), ("communicationsProtocolError", 5), ("communicationsSubsystemFailure", 6), ("configurationOrCustomizationError", 7), ("congestion", 8), ("corruptData", 9), ("cpuCyclesLimitExceeded", 10), ("dTEdCEInterfaceError", 11), ("datasetOrModemError", 12), ("degradedSignal", 13), ("enclosureDoorOpen", 14), ("equipmentMalfunction", 15), ("excessiveVibration", 16), ("fileError", 17), ("fireDetected", 18), ("floodDetected", 19), ("framingError", 20), ("heatingOrVentilationOrCoolingSystemProblem", 21), ("humidityUnacceptable", 22), ("inputDeviceError", 23), ("inputOutputDeviceError", 24), ("lANError", 25), ("leakDetected", 26), ("localNodeTransmissionError", 27), ("lossOfFrame", 28), ("lossOfSignal", 29), ("materialSupplyExhausted", 30), ("multiplexerProblem", 31), ("outOfMemory", 32), ("outputDeviceError", 33), ("performanceDegraded", 34), ("powerProblem", 35), ("pressureUnacceptable", 36), ("processorProblem", 37), ("pumpFailure", 38), ("queueSizeExceeded", 39), ("receiveFailure", 40), ("receiverFailure", 41), ("remoteNodeTransmissionError", 42), ("resourceAtOrNearingCapacity", 43), ("responseTimeExcessive", 44), ("retransmissionRateExcessive", 45), ("softwareProgramError", 46), ("softwareError", 47), ("softwareProgramAbnormallyTerminated", 48), ("storageCapacityProblem", 49), ("temperatureUnacceptable", 50), ("thresholdCrossed", 51), ("timingProblem", 52), ("toxicLeakDetected", 53), ("transmitFailure", 54), ("transmitterFailure", 55), ("underlyingResourceUnavailable", 56), ("versionMismatch", 57))

class UnitType(TextualConvention, Integer32):
    description = 'The unit type in the M-Series. nmb - Network Management Board. The controlling board of the M-Series. psu1 - The Power Supply in slot 1 of the M-Series. psu2 - The Power Supply in slot 2 of the M-Series. fan - The Fan of the M-Series. system - The chassis. slaveNmb - Network Management Board of the Cascading system. slavePsu1 - The Power Supply in slot 1 of the Cascading M-Series. slavePsu2 - The Power Supply in slot 2 of the Cascading M-Series. slaveFan - The Fan of the Cascading M-Series.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("nmb", 1), ("psu1", 2), ("psu2", 3), ("fan", 4), ("system", 5), ("slaveNmb", 6), ("slavePsu1", 7), ("slavePsu2", 8), ("slaveFan", 9))

class PortType(TextualConvention, Integer32):
    description = 'Port direction. rx - The port direction is receiving(Rx). tx - The port direction is transmitting(Tx). biDi - The port direction is both transmitting and receiving.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("biDi", 3))

class PortStatus(TextualConvention, Integer32):
    description = 'The operational state for a port. idle - The port is not activated down - The port traffic is lost. up - There is traffic on the port. high - The port got to high power. low - The port got to low power. eyeSafety - The Line Tx port is in Eye Safety Mode. This means that either the connector on the Line Tx port is not inserted or that you have too strong reflection from the line fiber. cd - Channel detected. ncd - No channel detected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("idle", 1), ("down", 2), ("up", 3), ("high", 4), ("low", 5), ("eyeSafety", 6), ("cd", 7), ("ncd", 8))

class PortMode(TextualConvention, Integer32):
    description = 'Port Mode. normal - The port is active. Alarms are not suppressed. service - the port is in Service Mode. Alarms are beeing suppressed. When service is ready the Port Mode should be set back to normal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("service", 2))

mibBuilder.exportSymbols("MSERIES-TC", PYSNMP_MODULE_ID=smartTcMIB, UnitType=UnitType, AlarmProbableCause=AlarmProbableCause, smartTcMIB=smartTcMIB, PortStatus=PortStatus, AlarmPerceivedSeverity=AlarmPerceivedSeverity, PortMode=PortMode, PortType=PortType, AlarmNotificationType=AlarmNotificationType)
