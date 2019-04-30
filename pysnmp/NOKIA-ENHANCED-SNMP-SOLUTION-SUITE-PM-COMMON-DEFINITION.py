#
# PySNMP MIB module NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
noiOpenInterfaceModule, = mibBuilder.importSymbols("NOKIA-NE3S-REGISTRATION-MIB", "noiOpenInterfaceModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, IpAddress, ModuleIdentity, Counter64, TimeTicks, ObjectIdentity, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "IpAddress", "ModuleIdentity", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
noiSnmpPMIrpCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 3))
noiSnmpPMIrpCommon.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setLastUpdated('200227020000Z')
if mibBuilder.loadTexts: noiSnmpPMIrpCommon.setOrganization('Nokia Networks')
class NoiMeasurementActivationError(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("noError", 1), ("noMeasurementScheduleFileCreatedError", 2), ("syntaxErrorInMeasurementScheduleFileError", 3), ("corruptedFileError", 4), ("unknownMeasurementTypeError", 5), ("startDateError", 6), ("stopDateError", 7), ("intervalError", 8), ("unknowDNError", 9), ("activationError", 10), ("internalError", 11), ("complexityLimitationError", 12), ("invalidHourError", 13), ("invalidMinutesError", 14), ("invalidDurationError", 15))

class NoiMeasurementFileName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 150)

class NoiMeasurementFileDirectory(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 100)

class NoiMeasurementResultIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NoiMeasurementFileTransfer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ftp", 1), ("tftp", 2))

class NoiMeasurementJobStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("idle", 1), ("activating", 2), ("activationFailed", 3), ("active", 4))

class NoiMeasurementResultTransfer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notificationBased", 1), ("pollingBased", 2))

mibBuilder.exportSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION", NoiMeasurementResultTransfer=NoiMeasurementResultTransfer, noiSnmpPMIrpCommon=noiSnmpPMIrpCommon, PYSNMP_MODULE_ID=noiSnmpPMIrpCommon, NoiMeasurementActivationError=NoiMeasurementActivationError, NoiMeasurementFileTransfer=NoiMeasurementFileTransfer, NoiMeasurementResultIdentifier=NoiMeasurementResultIdentifier, NoiMeasurementJobStatus=NoiMeasurementJobStatus, NoiMeasurementFileDirectory=NoiMeasurementFileDirectory, NoiMeasurementFileName=NoiMeasurementFileName)
