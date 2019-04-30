#
# PySNMP MIB module APPACCELERATION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPACCELERATION-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
appAccelerationModules, = mibBuilder.importSymbols("APPACCELERATION-SMI", "appAccelerationModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Gauge32, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, Counter64, iso, Bits, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter64", "iso", "Bits", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
appAccelerationTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3845, 30, 3, 1))
if mibBuilder.loadTexts: appAccelerationTextualConventions.setLastUpdated('200905110000Z')
if mibBuilder.loadTexts: appAccelerationTextualConventions.setOrganization('www.citrix.com')
class AppAccelerationYesNo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class AppAccelerationDescription(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class AppAccelerationAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7))

class AppAccelerationSeqNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

mibBuilder.exportSymbols("APPACCELERATION-TC", appAccelerationTextualConventions=appAccelerationTextualConventions, AppAccelerationAlarmSeverity=AppAccelerationAlarmSeverity, AppAccelerationSeqNum=AppAccelerationSeqNum, AppAccelerationYesNo=AppAccelerationYesNo, PYSNMP_MODULE_ID=appAccelerationTextualConventions, AppAccelerationDescription=AppAccelerationDescription)
