#
# PySNMP MIB module CISCO-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-SENSOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, IpAddress, Gauge32, TimeTicks, ModuleIdentity, Unsigned32, iso, Counter64, MibIdentifier, ObjectIdentity, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "IpAddress", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "iso", "Counter64", "MibIdentifier", "ObjectIdentity", "Integer32", "NotificationType")
TextualConvention, DisplayString, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "TimeStamp")
ciscoEntitySensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 91))
ciscoEntitySensorMIB.setRevisions(('2017-01-19 00:00', '2015-01-15 00:00', '2013-09-21 00:00', '2007-11-12 00:00', '2006-01-01 00:00', '2005-09-08 00:00', '2003-01-07 00:00', '2002-10-16 00:00', '2000-06-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorMIB.setRevisionsDescriptions(('Added enumerated value dB(15) to SensorDataType.', 'Corrected the definition of entSensorPrecision.', 'Added entSensorThresholdRecoveryNotification to entitySensorMIBNotifications. Added entSensorThresholdSeverity as a varbind object to entSensorThresholdNotification. Added entitySensorNotificationGroup and deprecated entitySensorThresholdNotificationGroup. Added entSensorThresholdNotification and entSensorThresholdRecoveryNotification to entitySensorNotificationGroup. Added entitySensorMIBComplianceV05 and deprecated entitySensorMIBComplianceV04.', 'Added entitySensorNotifCtrlGlobalGroup.', 'Add new object entSensorMeasuredEntity to entSensorValueTable.', 'Change the module descriptor name from entitySensorMIB to ciscoEntitySensorMIB since ENTITY-SENSOR-MIB also uses the same name and there is a conflict.', '[1] Add dBm(14) in SensorDataType.', '[1] Add critical(30) in CSensorThresholdSeverity. [2] Change to MAX-ACCESS read-write for 3 objects. [3] Add entitySensorMIBComplianceV02.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorMIB.setLastUpdated('201701190000Z')
if mibBuilder.loadTexts: ciscoEntitySensorMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorMIB.setContactInfo('Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 408 526 4000 E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorMIB.setDescription('The CISCO-ENTITY-SENSOR-MIB is used to monitor the values of sensors in the Entity-MIB (RFC 2037) entPhysicalTable.')
entitySensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1))
entitySensorMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2))
entitySensorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3))
class SensorDataType(TextualConvention, Integer32):
    description = 'sensor measurement data types. valid values are: other(1): a measure other than those listed below unknown(2): unknown measurement, or arbitrary, relative numbers voltsAC(3): electric potential voltsDC(4): electric potential amperes(5): electric current watts(6): power hertz(7): frequency celsius(8): temperature percentRH(9): percent relative humidity rpm(10): shaft revolutions per minute cmm(11),: cubic meters per minute (airflow) truthvalue(12): value takes { true(1), false(2) } specialEnum(13): value takes user defined enumerated values dBm(14): dB relative to 1mW of power dB(15): decibel'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12), ("specialEnum", 13), ("dBm", 14), ("dB", 15))

class SensorDataScale(TextualConvention, Integer32):
    description = 'International System of Units (SI) prefixes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class SensorPrecision(TextualConvention, Integer32):
    description = "When in the range 1 to 9, SensorPrecision is the number of decimal places in the fractional part of a SensorValue fixed-point number. When in the range -8 to -1, SensorPrecision is the number of accurate digits in a SensorValue fixed-point number. SensorPrecision is 0 for non-fixed-point numbers. Agent implementors must choose a value for SensorPrecision so that the precision and accuracy of a SensorValue is correctly indicated. For example, a temperature sensor that can measure 0o to 100o C in 0.1o increments, +/- 0.05o, would have a SensorPrecision of 1, a SensorDataScale of units(0), and a SensorValue ranging from 0 to 1000. The SensorValue would be interpreted as (degrees C * 10). If that temperature sensor's precision were 0.1o but its accuracy were only +/- 0.5o, then the SensorPrecision would be 0. The SensorValue would be interpreted as degrees C. Another example: a fan rotation speed sensor that measures RPM from 0 to 10,000 in 100 RPM increments, with an accuracy of +50/-37 RPM, would have a SensorPrecision of -2, a SensorDataScale of units(9), and a SensorValue ranging from 0 to 10000. The 10s and 1s digits of SensorValue would always be 0."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class SensorValue(TextualConvention, Integer32):
    description = 'For sensors that measure voltsAC, voltsDC, amperes, watts, hertz, celsius, cmm this item is a fixed point number ranging from -999,999,999 to +999,999,999. Use the value -1000000000 to indicate underflow. Use the value +1000000000 to indicate overflow. Use SensorPrecision to indicate how many fractional digits the SensorValue has. For sensors that measure percentRH, this item is a number ranging from 0 to 100. For sensors that measure rpm, this item can take only nonnegative values, 0..999999999. For sensors of type truthvalue, this item can take only two values: true(1), false(2). For sensors of type specialEnum, this item can take any value in the range (-1000000000..1000000000), but the meaning of each value is specific to the sensor. For sensors of type other and unknown, this item can take any value in the range (-1000000000..1000000000), but the meaning of the values are specific to the sensor. Use Entity-MIB entPhysicalTable.entPhysicalVendorType to learn about the sensor type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    description = 'Indicates the operational status of the sensor. ok(1) means the agent can read the sensor value. unavailable(2) means that the agent presently can not report the sensor value. nonoperational(3) means that the agent believes the sensor is broken. The sensor could have a hard failure (disconnected wire), or a soft failure such as out-of-range, jittery, or wildly fluctuating readings.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

class SensorValueUpdateRate(TextualConvention, Integer32):
    description = "Indicates the interval in seconds between updates to the sensor's value. The value zero indicates: - the sensor value is updated on demand (when polled by the agent for a get-request), - or when the sensor value changes (event-driven), - or the agent does not know the rate"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 999999999)

class SensorThresholdSeverity(TextualConvention, Integer32):
    description = 'sensor threshold severity. Valid values are: other(1) : a severity other than those listed below. minor(10) : Minor Problem threshold. major(20) : Major Problem threshold. critical(30): Critical problem threshold. A system might shut down the sensor associated FRU automatically if the sensor value reach the critical problem threshold.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class SensorThresholdRelation(TextualConvention, Integer32):
    description = 'sensor threshold relational operator types. valid values are: lessThan(1): if the sensor value is less than the threshold value lessOrEqual(2): if the sensor value is less than or equal to the threshold value greaterThan(3): if the sensor value is greater than the threshold value greaterOrEqual(4): if the sensor value is greater than or equal to the threshold value equalTo(5): if the sensor value is equal to the threshold value notEqualTo(6): if the sensor value is not equal to the threshold value'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

entSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1))
entSensorThresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2))
entSensorGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 3))
entSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1), )
if mibBuilder.loadTexts: entSensorValueTable.setStatus('current')
if mibBuilder.loadTexts: entSensorValueTable.setDescription('This table lists the type, scale, and present value of a sensor listed in the Entity-MIB entPhysicalTable.')
entSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entSensorValueEntry.setStatus('current')
if mibBuilder.loadTexts: entSensorValueEntry.setDescription('An entSensorValueTable entry describes the present reading of a sensor, the measurement units and scale, and sensor operational status.')
entSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 1), SensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorType.setStatus('current')
if mibBuilder.loadTexts: entSensorType.setDescription('This variable indicates the type of data reported by the entSensorValue. This variable is set by the agent at start-up and the value does not change during operation.')
entSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 2), SensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorScale.setStatus('current')
if mibBuilder.loadTexts: entSensorScale.setDescription('This variable indicates the exponent to apply to sensor values reported by entSensorValue. This variable is set by the agent at start-up and the value does not change during operation.')
entSensorPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 3), SensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorPrecision.setStatus('current')
if mibBuilder.loadTexts: entSensorPrecision.setDescription("This variable indicates the number of decimal places of precision in fixed-point sensor values reported by entSensorValue. This variable is set to 0 when entSensorType is not a fixed-point type: e.g.'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'. This variable is set by the agent at start-up and the value does not change during operation.")
entSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 4), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValue.setStatus('current')
if mibBuilder.loadTexts: entSensorValue.setDescription("This variable reports the most recent measurement seen by the sensor. To correctly display or interpret this variable's value, you must also know entSensorType, entSensorScale, and entSensorPrecision. However, you can compare entSensorValue with the threshold values given in entSensorThresholdTable without any semantic knowledge.")
entSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 5), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorStatus.setStatus('current')
if mibBuilder.loadTexts: entSensorStatus.setDescription('This variable indicates the present operational status of the sensor.')
entSensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueTimeStamp.setStatus('current')
if mibBuilder.loadTexts: entSensorValueTimeStamp.setDescription('This variable indicates the age of the value reported by entSensorValue')
entSensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 7), SensorValueUpdateRate()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueUpdateRate.setStatus('current')
if mibBuilder.loadTexts: entSensorValueUpdateRate.setDescription('This variable indicates the rate that the agent updates entSensorValue.')
entSensorMeasuredEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 8), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorMeasuredEntity.setStatus('current')
if mibBuilder.loadTexts: entSensorMeasuredEntity.setDescription('This object identifies the physical entity for which the sensor is taking measurements. For example, for a sensor measuring the voltage output of a power-supply, this object would be the entPhysicalIndex of that power-supply; for a sensor measuring the temperature inside one chassis of a multi-chassis system, this object would be the enPhysicalIndex of that chassis. This object has a value of zero when the physical entity for which the sensor is taking measurements can not be represented by any one row in the entPhysicalTable, or that there is no such physical entity.')
entSensorThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1), )
if mibBuilder.loadTexts: entSensorThresholdTable.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdTable.setDescription('This table lists the threshold severity, relation, and comparison value, for a sensor listed in the Entity-MIB entPhysicalTable.')
entSensorThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdIndex"))
if mibBuilder.loadTexts: entSensorThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdEntry.setDescription('An entSensorThresholdTable entry describes the thresholds for a sensor: the threshold severity, the threshold value, the relation, and the evaluation of the threshold. Only entities of type sensor(8) are listed in this table. Only pre-configured thresholds are listed in this table. Users can create sensor-value monitoring instruments in different ways, such as RMON alarms, Expression-MIB, etc. Entries are created by the agent at system startup and FRU insertion. Entries are deleted by the agent at FRU removal.')
entSensorThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99999999)))
if mibBuilder.loadTexts: entSensorThresholdIndex.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdIndex.setDescription('An index that uniquely identifies an entry in the entSensorThresholdTable. This index permits the same sensor to have several different thresholds.')
entSensorThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 2), SensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdSeverity.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdSeverity.setDescription('This variable indicates the severity of this threshold.')
entSensorThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 3), SensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdRelation.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdRelation.setDescription("This variable indicates the relation between sensor value (entSensorValue) and threshold value (entSensorThresholdValue), required to trigger the alarm. when evaluating the relation, entSensorValue is on the left of entSensorThresholdRelation, entSensorThresholdValue is on the right. in pseudo-code, the evaluation-alarm mechanism is: ... if (entSensorStatus == ok) then if (evaluate(entSensorValue, entSensorThresholdRelation, entSensorThresholdValue)) then if (entSensorThresholdNotificationEnable == true)) then raise_alarm(sensor's entPhysicalIndex); endif endif endif ...")
entSensorThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 4), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdValue.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdValue.setDescription("This variable indicates the value of the threshold. To correctly display or interpret this variable's value, you must also know entSensorType, entSensorScale, and entSensorPrecision. However, you can directly compare entSensorValue with the threshold values given in entSensorThresholdTable without any semantic knowledge.")
entSensorThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorThresholdEvaluation.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdEvaluation.setDescription('This variable indicates the result of the most recent evaluation of the threshold. If the threshold condition is true, entSensorThresholdEvaluation is true(1). If the threshold condition is false, entSensorThresholdEvaluation is false(2). Thresholds are evaluated at the rate indicated by entSensorValueUpdateRate.')
entSensorThresholdNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdNotificationEnable.setDescription("This variable controls generation of entSensorThresholdNotification for this threshold. When this variable is 'true', generation of entSensorThresholdNotification is enabled for this threshold. When this variable is 'false', generation of entSensorThresholdNotification is disabled for this threshold.")
entSensorThreshNotifGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThreshNotifGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: entSensorThreshNotifGlobalEnable.setDescription("This variable enables the generation of entSensorThresholdNotification globally on the device. If this object value is 'false', then no entSensorThresholdNotification will be generated on this device. If this object value is 'true', then whether a entSensorThresholdNotification for a threshold will be generated or not depends on the instance value of entSensorThresholdNotificationEnable for that threshold.")
entitySensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0))
entSensorThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"))
if mibBuilder.loadTexts: entSensorThresholdNotification.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdNotification.setDescription('The notification is generated when the sensor value entSensorValue crosses the threshold value entSensorThresholdValue and the value of entSensorThreshNotifGlobalEnable is true. entSensorThresholdSeverity indicates the severity of this threshold. The agent implementation guarantees prompt, timely evaluation of threshold and generation of this notification.')
entSensorThresholdRecoveryNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"))
if mibBuilder.loadTexts: entSensorThresholdRecoveryNotification.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdRecoveryNotification.setDescription('This notification is generated as a recovery notification when the sensor value entSensorValue goes below the threshold value entSensorThresholdValue once it has generated entSensorThresholdNotification. The value of entSensorThreshNotifGlobalEnable needs to be true. entSensorThresholdSeverity indicates the severity of this threshold. The agent implementation guarantees prompt, timely evaluation of threshold and generation of this notification.')
entitySensorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1))
entitySensorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2))
entitySensorMIBComplianceV01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV01 = entitySensorMIBComplianceV01.setStatus('deprecated')
if mibBuilder.loadTexts: entitySensorMIBComplianceV01.setDescription('An Entity-MIB implementation that lists sensors in its entPhysicalTable must implement this group.')
entitySensorMIBComplianceV02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV02 = entitySensorMIBComplianceV02.setStatus('deprecated')
if mibBuilder.loadTexts: entitySensorMIBComplianceV02.setDescription('An Entity-MIB implementation that lists sensors in its entPhysicalTable must implement this group.')
entitySensorMIBComplianceV03 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 3)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV03 = entitySensorMIBComplianceV03.setStatus('deprecated')
if mibBuilder.loadTexts: entitySensorMIBComplianceV03.setDescription('An Entity-MIB implementation that lists sensors in its entPhysicalTable must implement this group.')
entitySensorMIBComplianceV04 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 4)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroupSup1"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorNotifCtrlGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV04 = entitySensorMIBComplianceV04.setStatus('deprecated')
if mibBuilder.loadTexts: entitySensorMIBComplianceV04.setDescription('An Entity-MIB implementation that lists sensors in its entPhysicalTable must implement this group.')
entitySensorMIBComplianceV05 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 5)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroupSup1"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorNotifCtrlGlobalGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV05 = entitySensorMIBComplianceV05.setStatus('current')
if mibBuilder.loadTexts: entitySensorMIBComplianceV05.setDescription('An Entity-MIB implementation that lists sensors in its entPhysicalTable must implement this group.')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorType"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorScale"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorPrecision"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorStatus"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueTimeStamp"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorValueGroup.setDescription('The collection of objects which are used to describe and monitor values of Entity-MIB entPhysicalTable entries of sensors.')
entitySensorThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRelation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdGroup = entitySensorThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorThresholdGroup.setDescription('The collection of objects which are used to describe and monitor thresholds for sensors.')
entitySensorThresholdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdNotificationGroup = entitySensorThresholdNotificationGroup.setStatus('deprecated')
if mibBuilder.loadTexts: entitySensorThresholdNotificationGroup.setDescription('The collection of notifications used for monitoring sensor threshold activity. entitySensorThresholdNotificationGroup object is superseded by entitySensorNotificationGroup.')
entitySensorValueGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 4)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorMeasuredEntity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroupSup1 = entitySensorValueGroupSup1.setStatus('current')
if mibBuilder.loadTexts: entitySensorValueGroupSup1.setDescription('The collection of objects which are used to describe and track the measured entities of ENTITY-MIB entPhysicalTable.')
entitySensorNotifCtrlGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 5)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThreshNotifGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorNotifCtrlGlobalGroup = entitySensorNotifCtrlGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorNotifCtrlGlobalGroup.setDescription('The collection of objects which provide the global notification control on entSensorThresholdNotification.')
entitySensorNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 6)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRecoveryNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorNotificationGroup = entitySensorNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorNotificationGroup.setDescription('The collection of notifications used for monitoring sensor threshold activity.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-MIB", entSensorMeasuredEntity=entSensorMeasuredEntity, entitySensorMIBComplianceV02=entitySensorMIBComplianceV02, entSensorThresholdEvaluation=entSensorThresholdEvaluation, PYSNMP_MODULE_ID=ciscoEntitySensorMIB, entSensorThresholdRelation=entSensorThresholdRelation, SensorDataScale=SensorDataScale, entSensorThresholdNotification=entSensorThresholdNotification, entitySensorThresholdNotificationGroup=entitySensorThresholdNotificationGroup, entitySensorNotificationGroup=entitySensorNotificationGroup, entitySensorMIBCompliances=entitySensorMIBCompliances, entitySensorMIBNotifications=entitySensorMIBNotifications, entitySensorNotifCtrlGlobalGroup=entitySensorNotifCtrlGlobalGroup, entSensorValueTable=entSensorValueTable, entitySensorMIBComplianceV01=entitySensorMIBComplianceV01, SensorDataType=SensorDataType, entSensorThresholds=entSensorThresholds, entitySensorThresholdGroup=entitySensorThresholdGroup, entSensorThresholdValue=entSensorThresholdValue, entitySensorMIBGroups=entitySensorMIBGroups, ciscoEntitySensorMIB=ciscoEntitySensorMIB, entitySensorValueGroup=entitySensorValueGroup, entSensorValueEntry=entSensorValueEntry, SensorPrecision=SensorPrecision, entSensorStatus=entSensorStatus, entSensorThresholdIndex=entSensorThresholdIndex, SensorThresholdSeverity=SensorThresholdSeverity, entitySensorMIBNotificationPrefix=entitySensorMIBNotificationPrefix, entSensorPrecision=entSensorPrecision, entSensorValues=entSensorValues, entitySensorMIBComplianceV05=entitySensorMIBComplianceV05, entSensorThresholdNotificationEnable=entSensorThresholdNotificationEnable, entSensorValueTimeStamp=entSensorValueTimeStamp, entSensorValueUpdateRate=entSensorValueUpdateRate, entitySensorValueGroupSup1=entitySensorValueGroupSup1, SensorStatus=SensorStatus, entSensorGlobalObjects=entSensorGlobalObjects, entSensorValue=entSensorValue, entSensorThresholdTable=entSensorThresholdTable, SensorValue=SensorValue, entSensorThresholdSeverity=entSensorThresholdSeverity, entSensorThresholdEntry=entSensorThresholdEntry, entSensorThreshNotifGlobalEnable=entSensorThreshNotifGlobalEnable, entSensorType=entSensorType, entitySensorMIBConformance=entitySensorMIBConformance, entSensorScale=entSensorScale, SensorThresholdRelation=SensorThresholdRelation, entitySensorMIBComplianceV03=entitySensorMIBComplianceV03, SensorValueUpdateRate=SensorValueUpdateRate, entitySensorMIBComplianceV04=entitySensorMIBComplianceV04, entitySensorMIBObjects=entitySensorMIBObjects, entSensorThresholdRecoveryNotification=entSensorThresholdRecoveryNotification)
