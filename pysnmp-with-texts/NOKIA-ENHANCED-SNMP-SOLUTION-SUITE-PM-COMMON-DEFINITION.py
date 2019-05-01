#
# PySNMP MIB module NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION
# Produced by pysmi-0.3.4 at Wed May  1 14:23:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
noiOpenInterfaceModule, = mibBuilder.importSymbols("NOKIA-NE3S-REGISTRATION-MIB", "noiOpenInterfaceModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Bits, Unsigned32, iso, Gauge32, NotificationType, ObjectIdentity, ModuleIdentity, Counter32, Integer32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Bits", "Unsigned32", "iso", "Gauge32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter32", "Integer32", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
noiSnmpPMIrpCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 3))
noiSnmpPMIrpCommon.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setRevisionsDescriptions(('Version 1.0.6',))
if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setLastUpdated('200227020000Z')
if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setOrganization('Nokia Networks')
if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setContactInfo('e-mail: NET-OSS-OPEN-SNMP DL (Microsoft Outlook, Nokia internal) DL.NET-OSS-OPEN-SNMP-DL@nokia.com')
if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setDescription('The definition of common parameters used for Nokia SNMP Solution Set of the Performance Management also known as Open SNMP Interface.')
class NoiMeasurementActivationError(TextualConvention, Integer32):
    description = 'Specifies the error code used by the agent to indicate the reason why the activation of a measurement job has failed. The agent will update this object immediately when the activation of a measurement job has failed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("noError", 1), ("noMeasurementScheduleFileCreatedError", 2), ("syntaxErrorInMeasurementScheduleFileError", 3), ("corruptedFileError", 4), ("unknownMeasurementTypeError", 5), ("startDateError", 6), ("stopDateError", 7), ("intervalError", 8), ("unknowDNError", 9), ("activationError", 10), ("internalError", 11), ("complexityLimitationError", 12), ("invalidHourError", 13), ("invalidMinutesError", 14), ("invalidDurationError", 15))

class NoiMeasurementFileName(DisplayString):
    description = 'Contains a file name of a measurement result file or a measurement schdedule file'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 150)

class NoiMeasurementFileDirectory(DisplayString):
    description = 'Contains the name of the directory in the agent where the measurement schedule files are stored.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 100)

class NoiMeasurementResultIdentifier(TextualConvention, Integer32):
    description = ' The measurement result identifier uniquely idenifies an entry in the measurement result table. It represents a consecutive sequence of positive integer numbers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NoiMeasurementFileTransfer(TextualConvention, Integer32):
    description = 'Specifies the supported file transfer mechanism'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ftp", 1), ("tftp", 2))

class NoiMeasurementJobStatus(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("idle", 1), ("activating", 2), ("activationFailed", 3), ("active", 4))

class NoiMeasurementResultTransfer(TextualConvention, Integer32):
    description = 'Specifies the supported mechanism for measurement data transfer'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notificationBased", 1), ("pollingBased", 2))

mibBuilder.exportSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION", NoiMeasurementFileTransfer=NoiMeasurementFileTransfer, NoiMeasurementFileName=NoiMeasurementFileName, NoiMeasurementResultTransfer=NoiMeasurementResultTransfer, noiSnmpPMIrpCommon=noiSnmpPMIrpCommon, NoiMeasurementActivationError=NoiMeasurementActivationError, NoiMeasurementJobStatus=NoiMeasurementJobStatus, NoiMeasurementResultIdentifier=NoiMeasurementResultIdentifier, NoiMeasurementFileDirectory=NoiMeasurementFileDirectory, PYSNMP_MODULE_ID=noiSnmpPMIrpCommon)
