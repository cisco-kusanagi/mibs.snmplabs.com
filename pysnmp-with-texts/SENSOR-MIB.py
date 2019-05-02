#
# PySNMP MIB module SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SENSOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ModuleIdentity, IpAddress, Gauge32, Integer32, TimeTicks, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "TimeTicks", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "MibIdentifier")
DisplayString, TruthValue, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "TimeStamp")
deviceSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 1))
if mibBuilder.loadTexts: deviceSensorMIB.setLastUpdated('0211060300Z')
if mibBuilder.loadTexts: deviceSensorMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceSensorMIB.setContactInfo('support@bluecoat.com')
if mibBuilder.loadTexts: deviceSensorMIB.setDescription('The deviceSensorMIB is used to monitor the values of sensors')
deviceSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1))
deviceSensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2))
deviceSensorMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0))
class SensorUnits(TextualConvention, Integer32):
    description = 'Sensor measurement unit types. Valid values are: other : a measure other than those listed below. truthvalue : value takes { true(1), false(2) }. specialEnum : value takes user defined enumerated values. volts : electrical potential. celsius : temperature. rpm : revolutions per minute. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("truthvalue", 2), ("specialEnum", 3), ("volts", 4), ("celsius", 5), ("rpm", 6))

class SensorCode(TextualConvention, Integer32):
    description = 'Interpretation of the current sensor value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("not-installed", 3), ("voltage-low-warning", 4), ("voltage-low-critical", 5), ("no-power", 6), ("voltage-high-warning", 7), ("voltage-high-critical", 8), ("voltage-high-severe", 9), ("temperature-high-warning", 10), ("temperature-high-critical", 11), ("temperature-high-severe", 12), ("fan-slow-warning", 13), ("fan-slow-critical", 14), ("fan-stopped", 15))

class ExpBase10(TextualConvention, Integer32):
    description = "Exponent base 10 for the current sensor value. For example '-1' means value*(1/10). "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-24, 24)

class SensorValue(TextualConvention, Integer32):
    description = 'For sensors that measure volts and celsius, this item is a fixed point number. For sensors that measure rpm, this item can take only nonnegative values. For sensors of type truthvalue, this item can take only two values: true(1), false(2). For sensors of type specialEnum, this item can take any value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    description = 'Indicates the operational status of the sensor. ok(1) means the agent can read the sensor value. unavailable(2) means that the agent presently can not report the sensor value. nonoperational(3) means that the sensor is broken.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

deviceSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1))
deviceSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: deviceSensorValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValueTable.setDescription('Table of sensors.')
deviceSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "SENSOR-MIB", "deviceSensorIndex"))
if mibBuilder.loadTexts: deviceSensorValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValueEntry.setDescription('An deviceSensorValueTable entry describes the present reading of a sensor, the measurement units and sensor operational status.')
deviceSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceSensorIndex.setStatus('current')
if mibBuilder.loadTexts: deviceSensorIndex.setDescription('An arbitrary value which uniquely identifies the sensor')
deviceSensorTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
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
if mibBuilder.loadTexts: deviceSensorValue.setDescription("This variable reports the most recent measurement seen by the sensor. To correctly display or interpret this variable's value, you must also know deviceSensorUnits. ")
deviceSensorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 6), SensorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorCode.setStatus('current')
if mibBuilder.loadTexts: deviceSensorCode.setDescription('This variable reports how to interpret deviceSensorValue by the sensor.')
deviceSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 7), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorStatus.setStatus('current')
if mibBuilder.loadTexts: deviceSensorStatus.setDescription('This variable indicates the present operational status of the sensor.')
deviceSensorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTimeStamp.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTimeStamp.setDescription('This variable indicates the age of the value reported by deviceSensorValue.')
deviceSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorName.setStatus('current')
if mibBuilder.loadTexts: deviceSensorName.setDescription('The textual name of the sensor.')
deviceSensorTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0, 1)).setObjects(("SENSOR-MIB", "deviceSensorName"), ("SENSOR-MIB", "deviceSensorValue"), ("SENSOR-MIB", "deviceSensorCode"))
if mibBuilder.loadTexts: deviceSensorTrap.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTrap.setDescription('The sensor value warrants a notification.')
mibBuilder.exportSymbols("SENSOR-MIB", SensorUnits=SensorUnits, deviceSensorTrapEnabled=deviceSensorTrapEnabled, deviceSensorScale=deviceSensorScale, PYSNMP_MODULE_ID=deviceSensorMIB, deviceSensorValue=deviceSensorValue, deviceSensorMIB=deviceSensorMIB, SensorValue=SensorValue, deviceSensorCode=deviceSensorCode, deviceSensorMIBNotifications=deviceSensorMIBNotifications, deviceSensorIndex=deviceSensorIndex, deviceSensorMIBObjects=deviceSensorMIBObjects, deviceSensorValueEntry=deviceSensorValueEntry, ExpBase10=ExpBase10, deviceSensorTimeStamp=deviceSensorTimeStamp, deviceSensorMIBNotificationsPrefix=deviceSensorMIBNotificationsPrefix, deviceSensorTrap=deviceSensorTrap, deviceSensorName=deviceSensorName, deviceSensorValueTable=deviceSensorValueTable, deviceSensorValues=deviceSensorValues, deviceSensorStatus=deviceSensorStatus, deviceSensorUnits=deviceSensorUnits, SensorCode=SensorCode, SensorStatus=SensorStatus)
