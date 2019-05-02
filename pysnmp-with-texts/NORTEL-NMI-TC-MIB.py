#
# PySNMP MIB module NORTEL-NMI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-NMI-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nortelNetworkManagementInterfaceMIBs, = mibBuilder.importSymbols("NORTEL-GENERIC-MIB", "nortelNetworkManagementInterfaceMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, IpAddress, Integer32, Gauge32, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "IpAddress", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Unsigned32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
nortelNMItextConvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 3))
nortelNMItextConvMIB.setRevisions(('1999-07-19 00:00', '1999-06-24 00:00', '1999-05-31 00:00', '1999-04-12 00:00', '1999-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nortelNMItextConvMIB.setRevisionsDescriptions((' Change the description of NortelNMIneType. Revision introduced by Jingdong LIU.', ' The fourth version of this MIB module. Module-Identity OID assignment changed. Comments modified.', ' The third version of this MIB module. Contact info updated and Revision history added. Syntaxes changed to - NortelNMIneType - NortelNMIadminState - NortelNMIoperState Revisions introduced by Shobana Sundaram. ', ' The second version of this MIB module. Contact info updated and Revision history added. Comments modified.', ' The first version of this MIB module.',))
if mibBuilder.loadTexts: nortelNMItextConvMIB.setLastUpdated('9907190000Z')
if mibBuilder.loadTexts: nortelNMItextConvMIB.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nortelNMItextConvMIB.setContactInfo(' Jingdong Liu Postal: Nortel Networks P. O. Box 3511, Station C Ottawa, Ontario CANADA K1Y 4H7 Email: jingdong@nortelnetworks.com')
if mibBuilder.loadTexts: nortelNMItextConvMIB.setDescription('This module contains the definitions of some proprietary textual conventions for the Nortel generic NetworkManagementInterface (NMI) mibs. ')
class NortelNMItimeStampDef(TextualConvention, Unsigned32):
    description = ' Represents the time in seconds since the reference epoch, zero hours:zero minutes:zero seconds, Coordinated Universal Time (UTC), January 1, 1970. This timestamp definition would be used to accurately reflect the time of occurrence of various events at the Nortel Network Management Interface (NMI).'
    status = 'current'

class NortelNMIneType(DisplayString):
    description = ' Represents the various possible NE types that are monitored via the Nortel NMI MIBs. The NeType string should be a single word, can only contain alphanumeric characters and underscores. No commas, spaces, slashes, hyphens, or dollar signs is allowed.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class NortelNMIadminState(TextualConvention, Integer32):
    description = ' Represents the various possible administrative states (ITU-T X.731) that are monitored via the Nortel NMI MIBs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("locked", 1), ("shuttingDown", 2), ("unlocked", 3))

class NortelNMIoperState(TextualConvention, Integer32):
    description = ' Represents the possible values of operational states (ITU-T X.731) that are monitored via the Nortel NMI MIBs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class NortelNMIunknownStatusValue(TruthValue):
    description = ' Represents the unknown status value to be true / false (ITU-T X.731). This indicates whether the management system is able to maintain OAM communications with the managed entity or not.'
    status = 'current'

class NortelNMIalarmProblemCategory(TextualConvention, Integer32):
    description = ' Represents the alarm problem category values (ITU-T X.733).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("communications", 1), ("qualityOfService", 2), ("processingError", 3), ("equipment", 4), ("environmental", 5))

class NortelNMInotificationTypes(TextualConvention, Integer32):
    description = " Represents the type of Notification to be traps or Informs. Inform PDUs get acknowledgements / responses while traps don't."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trap", 1), ("inform", 2))

class NortelNMIalarmProbableCause(TextualConvention, Integer32):
    description = ' Represents the probable cause values for the alarms as per (ITU-T X.733, X.736).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118))
    namedValues = NamedValues(("adapterError", 1), ("applicationSubsystemFailure", 2), ("bandwidthReduced", 3), ("callEstablishmentError", 4), ("communicationsProtocolError", 5), ("communicationsSubsystemFailure", 6), ("configurationOrCustomizationError", 7), ("congestion", 8), ("corruptData", 9), ("cpuCyclesLimitExceeded", 10), ("dataSetOrModemError", 11), ("degradedSignal", 12), ("dteDCEInterfaceError", 13), ("enclosureDoorOpen", 14), ("equipmentMalfunction", 15), ("excessiveVibration", 16), ("fileError", 17), ("fireDetected", 18), ("floodDetected", 19), ("framingError", 20), ("heatingOrVentilationOrCoolingSystemProblem", 21), ("humidityUnacceptable", 22), ("inputOutputDeviceError", 23), ("inputDeviceError", 24), ("lANError", 25), ("leakDetected", 26), ("localNodeTransmissionError", 27), ("lossOfFrame", 28), ("lossOfSignal", 29), ("materialSupplyExhausted", 30), ("multiplexerProblem", 31), ("outOfMemory", 32), ("ouputDeviceError", 33), ("performanceDegraded", 34), ("powerProblem", 35), ("pressureUnacceptable", 36), ("processorProblem", 37), ("pumpFailure", 38), ("queueSizeExceeded", 39), ("receiveFailure", 40), ("receiverFailure", 41), ("remoteNodeTransmissionError", 42), ("resourceAtOrNearingCapacity", 43), ("responseTimeExecessive", 44), ("retransmissionRateExcessive", 45), ("softwareError", 46), ("softwareProgramAbnormallyTerminated", 47), ("softwareProgramError", 48), ("storageCapacityProblem", 49), ("temperatureUnacceptable", 50), ("thresholdCrossed", 51), ("timingProblem", 52), ("toxicLeakDetected", 53), ("transmitFailure", 54), ("transmitterFailure", 55), ("underlyingResourceUnavailable", 56), ("versionMismatch", 57), ("authenticationFailure", 101), ("breachOfConfidentiality", 102), ("cableTamper", 103), ("delayedInformation", 104), ("denialOfService", 105), ("duplicateInformation", 106), ("informationMissing", 107), ("informationModificationDetected", 108), ("informationOutOfSequence", 109), ("intrusionDetection", 110), ("keyExpired", 111), ("nonRepudiationFailure", 112), ("outOfHoursActivity", 113), ("outOfService", 114), ("proceduralError", 115), ("unauthorizedAccessAttempt", 116), ("unexpectedInformation", 117), ("unspecifiedReason", 118))

mibBuilder.exportSymbols("NORTEL-NMI-TC-MIB", NortelNMIadminState=NortelNMIadminState, NortelNMIunknownStatusValue=NortelNMIunknownStatusValue, NortelNMIoperState=NortelNMIoperState, NortelNMItimeStampDef=NortelNMItimeStampDef, nortelNMItextConvMIB=nortelNMItextConvMIB, PYSNMP_MODULE_ID=nortelNMItextConvMIB, NortelNMIalarmProblemCategory=NortelNMIalarmProblemCategory, NortelNMIneType=NortelNMIneType, NortelNMInotificationTypes=NortelNMInotificationTypes, NortelNMIalarmProbableCause=NortelNMIalarmProbableCause)
