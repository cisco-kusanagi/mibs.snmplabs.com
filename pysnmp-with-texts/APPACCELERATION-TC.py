#
# PySNMP MIB module APPACCELERATION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPACCELERATION-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:23:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
appAccelerationModules, = mibBuilder.importSymbols("APPACCELERATION-SMI", "appAccelerationModules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, iso, Bits, Counter32, NotificationType, ObjectIdentity, Unsigned32, IpAddress, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "iso", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
appAccelerationTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3845, 30, 3, 1))
if mibBuilder.loadTexts: appAccelerationTextualConventions.setLastUpdated('200905110000Z')
if mibBuilder.loadTexts: appAccelerationTextualConventions.setOrganization('www.citrix.com')
if mibBuilder.loadTexts: appAccelerationTextualConventions.setContactInfo(' Citrix Systems, Inc. Postal: 851 West Cypress Creek Road Fort Lauderdale, Florida 33309 United States')
if mibBuilder.loadTexts: appAccelerationTextualConventions.setDescription('This module defines the textual conventions used throughout Application Acceleration enterprise mibs.')
class AppAccelerationYesNo(TextualConvention, Integer32):
    description = 'Textual convention for yes/no enum. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class AppAccelerationDescription(DisplayString):
    description = 'Represents a string description used for any MIB object. Currently used for alarms sent out as trap notifications. '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class AppAccelerationAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    description = 'Represents the perceived alarm condition associated with a service affecting condition and/or event. cleared(1) - Indicates a previous alarm condition has been cleared. It is not required (unless specifically stated elsewhere on a case by case basis) that an alarm condition that has been cleared will produce a notification or other event containing an alarm severity with this value. indeterminate(2) - Indicates that the severity level cannot be determined. critical(3) - Indicates that a service or safety affecting condition has occurred and an immediate corrective action is required. major(4) - Indicates that a service affecting condition has occurred and an urgent corrective action is required. minor(5) - Indicates the existence of a non-service affecting condition and that corrective action should be taken in order to prevent a more serious (for example, service or safety affecting) condition. warning(6) - Indicates the detection of a potential or impending service or safety affecting condition, before any significant effects have been felt. info(7) - Indicates an alarm condition that does not meet any other severity definition. This can include important, but non-urgent, notices or informational events. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7))

class AppAccelerationSeqNum(TextualConvention, Integer32):
    description = 'Represents the unique sequence number associated with each generated trap. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

mibBuilder.exportSymbols("APPACCELERATION-TC", PYSNMP_MODULE_ID=appAccelerationTextualConventions, AppAccelerationYesNo=AppAccelerationYesNo, AppAccelerationAlarmSeverity=AppAccelerationAlarmSeverity, appAccelerationTextualConventions=appAccelerationTextualConventions, AppAccelerationSeqNum=AppAccelerationSeqNum, AppAccelerationDescription=AppAccelerationDescription)
