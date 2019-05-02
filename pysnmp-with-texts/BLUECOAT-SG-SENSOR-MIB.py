#
# PySNMP MIB module BLUECOAT-SG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUECOAT-SG-SENSOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, TimeTicks, IpAddress, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, MibIdentifier, Gauge32, Counter64, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "TimeTicks", "IpAddress", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "MibIdentifier", "Gauge32", "Counter64", "Bits", "Unsigned32")
DisplayString, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention")
deviceSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 1))
deviceSensorMIB.setRevisions(('2015-11-26 03:00', '2013-07-11 03:00', '2007-11-05 03:00', '2002-11-06 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deviceSensorMIB.setRevisionsDescriptions(('Add new value (notInstalled) to SensorStatus', 'Access level for deviceSensorTrapEnabled changed.', 'Minor corrections and reformatting.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: deviceSensorMIB.setLastUpdated('201511260300Z')
if mibBuilder.loadTexts: deviceSensorMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceSensorMIB.setContactInfo('support.services@bluecoat.com http://www.bluecoat.com')
if mibBuilder.loadTexts: deviceSensorMIB.setDescription('The sensor MIB is used to monitor the values of sensors')
deviceSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1))
deviceSensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2))
deviceSensorMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0))
class SensorUnits(TextualConvention, Integer32):
    description = 'Sensor measurement unit types. Valid values are: other(1) - a measure other than those listed below. truthvalue(2) - value takes { true(1), false(2) }. specialEnum(3) - value takes user defined enumerated values. volts(4) - electrical potential. celsius(5) - temperature. rpm(6) - revolutions per minute.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("truthvalue", 2), ("specialEnum", 3), ("volts", 4), ("celsius", 5), ("rpm", 6))

class SensorCode(TextualConvention, Integer32):
    description = 'Interpretation of the current sensor value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("notInstalled", 3), ("voltageLowWarning", 4), ("voltageLowCritical", 5), ("noPower", 6), ("voltageHighWarning", 7), ("voltageHighCritical", 8), ("voltageHighSevere", 9), ("temperatureHighWarning", 10), ("temperatureHighCritical", 11), ("temperatureHighSevere", 12), ("fanSlowWarning", 13), ("fanSlowCritical", 14), ("fanStopped", 15))

class ExpBase10(TextualConvention, Integer32):
    description = "Exponent base 10 for the current sensor value. For example '-1' means value*(1/10)."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-24, 24)

class SensorValue(TextualConvention, Integer32):
    description = 'For sensors that measure volts and celsius, this item is a fixed point number. For sensors that measure rpm, this item can take only nonnegative values. For sensors of type truthvalue, this item can take only two values: true(1), false(2). For sensors of type specialEnum, this item can take any value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    description = 'Indicates the operational status of the sensor. ok(1) means the agent can read the sensor value. unavailable(2) means that the agent presently can not report the sensor value. nonoperational(3) means that the sensor is broken. notInstalled(4) means that the sensor or device is not present.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3), ("notInstalled", 4))

deviceSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1))
deviceSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: deviceSensorValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValueTable.setDescription('Table of sensors.')
deviceSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-SENSOR-MIB", "deviceSensorIndex"))
if mibBuilder.loadTexts: deviceSensorValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValueEntry.setDescription('An deviceSensorValueTable entry describes the present reading of a sensor, the measurement units and sensor operational status.')
deviceSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceSensorIndex.setStatus('current')
if mibBuilder.loadTexts: deviceSensorIndex.setDescription('An arbitrary value which uniquely identifies the sensor')
deviceSensorTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTrapEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTrapEnabled.setDescription('This variable controls generation of deviceSensorTrap for this sensor. When this variable is true(1), generation of deviceSensorTrap is enabled. When this variable is false(2), generation of deviceSensorTrap is disabled. The default start-up value is true(1).')
deviceSensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 3), SensorUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorUnits.setStatus('current')
if mibBuilder.loadTexts: deviceSensorUnits.setDescription('This variable indicates the type of data reported by the deviceSensorValue. This variable is set by the agent at start-up and the value does not change during operation.')
deviceSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 4), ExpBase10()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorScale.setStatus('current')
if mibBuilder.loadTexts: deviceSensorScale.setDescription('Power of 10 to apply to the value reported by the deviceSensorValue. This variable is set by the agent at start-up and the value does not change during operation.')
deviceSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 5), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorValue.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValue.setDescription("This variable reports the most recent measurement seen by the sensor. To correctly display or interpret this variable's value, you must also know deviceSensorUnits.")
deviceSensorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 6), SensorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorCode.setStatus('current')
if mibBuilder.loadTexts: deviceSensorCode.setDescription('This variable reports how to interpret deviceSensorValue for the sensor.')
deviceSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 7), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorStatus.setStatus('current')
if mibBuilder.loadTexts: deviceSensorStatus.setDescription('This variable indicates the present operational status of the sensor.')
deviceSensorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 8), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTimeStamp.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTimeStamp.setDescription('This variable indicates the age of the value reported by deviceSensorValue.')
deviceSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorName.setStatus('current')
if mibBuilder.loadTexts: deviceSensorName.setDescription('The textual name of the sensor.')
deviceSensorTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0, 1)).setObjects(("BLUECOAT-SG-SENSOR-MIB", "deviceSensorName"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorValue"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorCode"))
if mibBuilder.loadTexts: deviceSensorTrap.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTrap.setDescription('The sensor value warrants a notification.')
mibBuilder.exportSymbols("BLUECOAT-SG-SENSOR-MIB", deviceSensorValue=deviceSensorValue, deviceSensorMIBNotificationsPrefix=deviceSensorMIBNotificationsPrefix, deviceSensorTrapEnabled=deviceSensorTrapEnabled, PYSNMP_MODULE_ID=deviceSensorMIB, SensorCode=SensorCode, ExpBase10=ExpBase10, SensorUnits=SensorUnits, deviceSensorValueEntry=deviceSensorValueEntry, deviceSensorMIBObjects=deviceSensorMIBObjects, SensorStatus=SensorStatus, deviceSensorMIB=deviceSensorMIB, deviceSensorValues=deviceSensorValues, deviceSensorValueTable=deviceSensorValueTable, SensorValue=SensorValue, deviceSensorUnits=deviceSensorUnits, deviceSensorTrap=deviceSensorTrap, deviceSensorIndex=deviceSensorIndex, deviceSensorMIBNotifications=deviceSensorMIBNotifications, deviceSensorCode=deviceSensorCode, deviceSensorTimeStamp=deviceSensorTimeStamp, deviceSensorScale=deviceSensorScale, deviceSensorName=deviceSensorName, deviceSensorStatus=deviceSensorStatus)
