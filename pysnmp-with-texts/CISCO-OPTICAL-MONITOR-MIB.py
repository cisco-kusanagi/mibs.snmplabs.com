#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OPTICAL-MONITOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:08:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Gauge32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Gauge32", "Integer32", "Counter64")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
ciscoOpticalMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 264))
ciscoOpticalMonitorMIB.setRevisions(('2007-01-02 00:00', '2002-05-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setRevisionsDescriptions(('Add cOpticalMonIfTimeGroup, cOpticalMIBEnableConfigGroup, cOpticalMIBIntervalConfigGroup, cOpticalMonThreshSourceGroup.', 'The initial revision of this MIB.',))
if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ciscoOpticalMonitorMIB.setDescription('This MIB module defines objects to monitor optical characteristics and set corresponding thresholds on the optical interfaces in a network element. ')
class OpticalParameterType(TextualConvention, Integer32):
    description = 'This value indicates the optical parameter that is being monitored. Valid values are - power (1) : Optical Power (AC + DC) in 1/10ths of dBm acPower (2) : Optical AC Power in 1/10ths of dBm ambientTemp (3) : Ambient Temperature in 1/10ths of degrees centigrade laserTemp (4) : Laser Temperature in 1/10ths of degrees centigrade biasCurrent (5) : Laser bias current in 100s of microamperes peltierCurrent (6) : Laser peltier current in milliamperes xcvrVoltage (7) : Transceiver voltage in millivolts '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("power", 1), ("acPower", 2), ("ambientTemp", 3), ("laserTemp", 4), ("biasCurrent", 5), ("peltierCurrent", 6), ("xcvrVoltage", 7))

class OpticalParameterValue(TextualConvention, Integer32):
    description = "The value of the optical parameter that is being monitored. The range of values varies depending on the type of optical parameter being monitored, as identified by a corresponding object with syntax OpticalParameterType. When the optical parameter being monitored is 'power' or 'acPower', the supported range is from -400 to 250, in 1/10ths of dBm. Example: A value of -300 represents a power level of -30.0 dBm. When the optical parameter being monitored is 'laserTemp' or 'ambientTemp', the supported range is from -500 to 850, in 1/10ths of degrees centigrade. Example: A value of 235 represents a temperature reading of 23.5 degrees C. When the optical parameter being monitored is 'biasCurrent', the supported range is from 0 to 10000, in 100s of microamperes. Example: A value of 500 represents a bias current reading of 50,000 microamperes. When the optical parameter being monitored is 'peltierCurrent', the supported range is from -10000 to 10000, in milliamperes. When the optical parameter being monitored is 'xcvrVoltage', the supported range is from 0 to 10000, in millivolts. The distinguished value of '-1000000' indicates that the object has not yet been initialized or does not apply. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000, 1000000)

class OpticalIfDirection(TextualConvention, Integer32):
    description = 'This value indicates the direction being monitored at the optical interface. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("receive", 1), ("transmit", 2), ("notApplicable", 3))

class OpticalIfMonLocation(TextualConvention, Integer32):
    description = "This value applies when there are multiple points at which optical characteristics can be measured, in the given direction, at an interface. It indicates whether the optical characteristics are measured before or after adjustment (e.g. optical amplification or attenuation). The codepoint 'notApplicable' should be used if no amplifier/attenuator exists at an interface. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("beforeAdjustment", 1), ("afterAdjustment", 2), ("notApplicable", 3))

class OpticalAlarmStatus(TextualConvention, OctetString):
    reference = 'Telcordia Technologies Generic Requirements GR-2918-CORE, Issue 4, December 1999, Section 8.11'
    description = 'A bitmap that indicates the current status of thresholds on an interface. The bit is set to 1 if the threshold is currently being exceeded on the interface and will be set to 0 otherwise. (MSB) (LSB) 7 6 5 4 3 2 1 0 +----------------------+ | | +----------------------+ | | | | | | | +-- High alarm threshold | | +----- High warning threshold | +-------- Low alarm threshold +----------- Low warning threshold To minimize the probability of prematurely reacting to momentary signal variations, a soak time may be incorporated into the status indications in the following manner. The indication is set when the threshold violation persists for a period of time that exceeds the set soak interval. The indication is cleared when no threshold violation occurs for a period of time which exceeds the clear soak interval. In GR-2918-CORE, the recommended set soak interval is 2.5 seconds (plus/minus 0.5 seconds), and the recommended clear soak interval is 10 seconds (plus/minus 0.5 seconds). '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class OpticalAlarmSeverity(TextualConvention, Integer32):
    reference = 'Telcordia Technologies Generic Requirements GR-474-CORE, Issue 1, December 1997, Section 2.2'
    description = "The severity of a trouble condition. A smaller enumerated integer value indicates that the condition is more severe. The severities are defined as follows: 'critical' An alarm used to indicate a severe, service-affecting condition has occurred and that immediate corrective action is imperative, regardless of the time of day or day of the week. 'major' An alarm used for hardware or software conditions that indicate a serious disruption of service or malfunctioning or failure of important hardware. These troubles require the immediate attention and response of a technician to restore or maintain system capability. The urgency is less than in critical situations because of a lesser immediate or impending effect on service or system performance. 'minor' An alarm used for troubles that do not have a serious effect on service to customers or for troubles in hardware that are not essential to the operation of the system. 'notAlarmed' An event used for troubles that do not require action, for troubles that are reported as a result of manually initiated diagnostics, or for transient events such as crossing warning thresholds. This event can also be used to raise attention to a condition that could possibly be an impending problem. 'notReported' An event used for troubles similar to those described under 'notAlarmed', and that do not cause notifications to be generated. The information for these events is retrievable from the network element. 'cleared' This value indicates that a previously occuring alarm condition has been cleared, or that no trouble condition is present. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("notAlarmed", 4), ("notReported", 5), ("cleared", 6))

class OpticalAlarmSeverityOrZero(TextualConvention, Integer32):
    description = "A value of either '0' or a valid optical alarm severity."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 6)

class OpticalPMPeriod(TextualConvention, Integer32):
    description = 'This value indicates the time period over which performance monitoring data has been collected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fifteenMin", 1), ("twentyFourHour", 2))

cOpticalMonitorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 1))
cOpticalMonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1))
cOpticalPMGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2))
cOpticalMonTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1), )
if mibBuilder.loadTexts: cOpticalMonTable.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonTable.setDescription('This table provides objects to monitor optical parameters in a network element. It also provides objects for setting high and low threshold levels, with configurable severities, on these monitored parameters.')
cOpticalMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonDirection"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonLocation"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonParameterType"))
if mibBuilder.loadTexts: cOpticalMonEntry.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonEntry.setDescription('An entry in the cOpticalMonTable provides objects to monitor an optical parameter and set threshold levels on that parameter, at an optical interface. Note that the set of monitored optical parameters may vary based on interface type, direction, and monitoring location. Examples of interfaces that can have an entry in this table include optical transceivers, interfaces before and after optical amplifiers, and interfaces before and after optical attenuators.')
cOpticalMonDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 1), OpticalIfDirection())
if mibBuilder.loadTexts: cOpticalMonDirection.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonDirection.setDescription('This object indicates the direction monitored for the optical interface, in this entry.')
cOpticalMonLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 2), OpticalIfMonLocation())
if mibBuilder.loadTexts: cOpticalMonLocation.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonLocation.setDescription('This object indicates whether the optical characteristics are measured before or after adjustment (e.g. optical amplification or attenuation), at this interface.')
cOpticalMonParameterType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 3), OpticalParameterType())
if mibBuilder.loadTexts: cOpticalMonParameterType.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonParameterType.setDescription('This object specifies the optical parameter that is being monitored in this entry.')
cOpticalParameterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 4), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParameterValue.setStatus('current')
if mibBuilder.loadTexts: cOpticalParameterValue.setDescription('This object gives the value measured for the particular optical parameter specified by the cOpticalMonParameterType object.')
cOpticalParamHighAlarmThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 5), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighAlarmThresh.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamHighAlarmThresh.setDescription("This object is used to set a high alarm threshold on the optical parameter being monitored. An alarm condition will be raised if the value given by cOpticalParameterValue goes from below the value configured in this object to above the value configured in this object, or if the initial value of cOpticalParameterValue exceeds the value configured in this object. For network elements that incorporate a soak time in the status indications, this alarm will be indicated in the cOpticalParamAlarmStatus object only after it persists for a period of time that equals the set soak interval. The severity level of the alarm is specified by the cOpticalParamHighAlarmSev object. When the cOpticalMonParameterType object is set to 'power' for the receive direction at a transceiver, this object specifies the receiver saturation level.")
cOpticalParamHighAlarmSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 6), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighAlarmSev.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamHighAlarmSev.setDescription("This object is used to specify a severity level associated with the high alarm threshold given by the cOpticalParamHighAlarmThresh object. The values 'notAlarmed', 'notReported', and 'cleared' do not apply. The severity level configured in this object must be higher than the level configured in the cOpticalParamHighWarningSev object.")
cOpticalParamHighWarningThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 7), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighWarningThresh.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamHighWarningThresh.setDescription('This object is used to set a high warning threshold on the optical parameter being monitored. A threshold crossing condition will be indicated if the value given by cOpticalParameterValue goes from below the value configured in this object to above the value configured in this object, or if the initial value of cOpticalParameterValue exceeds the value configured in this object. For network elements that incorporate a soak time in the status indications, this threshold violation will be indicated in the cOpticalParamAlarmStatus object only after it persists for a period of time that equals the set soak interval. This threshold crossing may or may not be alarmed or reported, based on the severity level specified by the cOpticalParamHighWarningSev object.')
cOpticalParamHighWarningSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 8), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamHighWarningSev.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamHighWarningSev.setDescription("This object is used to specify a severity level associated with the high warning threshold given by the cOpticalParamHighWarningThresh object. The values 'critical', 'major', and 'cleared' do not apply. The severity level configured in this object must be lower than the level configured in the cOpticalParamHighAlarmSev object. If this object is set to 'notReported', no notifications will be generated when this threshold is exceeded, irrespective of the value configured in the cOpticalNotifyEnable object.")
cOpticalParamLowAlarmThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 9), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowAlarmThresh.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamLowAlarmThresh.setDescription("This object is used to set a low alarm threshold on the optical parameter being monitored. An alarm condition will be raised if the value given by cOpticalParameterValue goes from above the value configured in this object to below the value configured in this object, or if the initial value of cOpticalParameterValue is lower than the value configured in this object. For network elements that incorporate a soak time in the status indications, this alarm will be indicated in the cOpticalParamAlarmStatus object only after it persists for a period of time that equals the set soak interval. The severity level of this alarm is specified by the cOpticalParamLowAlarmSev object. When the cOpticalMonParameterType object is set to 'power' for the receive direction and when the interface supports alarms based on loss of light, this object specifies the optical power threshold for declaring loss of light. Also, when optical amplifiers are present in the network, in the receive direction, this value may need to be configured, since the noise floor may be higher than the minimum sensitivity of the receiver.")
cOpticalParamLowAlarmSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 10), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowAlarmSev.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamLowAlarmSev.setDescription("This object is used to specify a severity level associated with the low alarm threshold given by the cOpticalParamLowAlarmThresh object. The values 'notAlarmed', 'notReported', and 'cleared' do not apply. The severity level configured in this object must be higher than the level configured in the cOpticalParamLowWarningSev object.")
cOpticalParamLowWarningThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 11), OpticalParameterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowWarningThresh.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamLowWarningThresh.setDescription('This object is used to set a low warning threshold on the optical parameter being monitored. A threshold crossing condition will be indicated if the value given by cOpticalParameterValue goes from above the value configured in this object to below the value configured in this object, or if the initial value of cOpticalParameterValue object is lower than the value configured in this object. For network elements that incorporate a soak time in the status indications, this threshold violation will be indicated in the cOpticalParamAlarmStatus object only after it persists for a period of time that equals the set soak interval. This threshold crossing may or may not be alarmed or reported, based on the severity level specified by the cOpticalParamLowWarningSev object.')
cOpticalParamLowWarningSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 12), OpticalAlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamLowWarningSev.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamLowWarningSev.setDescription("This object is used to specify a severity level associated with the low warning threshold given by the cOpticalParamLowWarningThresh object. The values 'critical', 'major', and 'cleared' do not apply. The severity level configured in this object must be lower than the level configured in the cOpticalParamLowAlarmSev object. If this object is set to 'notReported', no notifications will be generated when this threshold is exceeded, irrespective of the value configured in the cOpticalNotifyEnable object.")
cOpticalParamAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 13), OpticalAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamAlarmStatus.setDescription('This object is used to indicate the current status of the thresholds for the monitored optical parameter on the interface. If a threshold is currently being exceeded on the interface, the corresponding bit in this object will be set to 1. Otherwise, the bit will be set to 0.')
cOpticalParamAlarmCurMaxThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 14), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmCurMaxThresh.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamAlarmCurMaxThresh.setDescription("This object indicates the threshold value of the highest severity threshold that is currently being exceeded on the interface, for the optical parameter. If no threshold value is currently being exceeded, then the value '-1000000' is returned.")
cOpticalParamAlarmCurMaxSev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 15), OpticalAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmCurMaxSev.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamAlarmCurMaxSev.setDescription('This object indicates the maximum severity of any thresholds that are currently being exceeded on the interface, for the optical parameter.')
cOpticalParamAlarmLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalParamAlarmLastChange.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamAlarmLastChange.setDescription('This object specifies the value of sysUpTime at the last time a threshold related to a particular optical parameter was exceeded or cleared on the interface.')
cOpticalMon15MinValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalMon15MinValidIntervals.setStatus('current')
if mibBuilder.loadTexts: cOpticalMon15MinValidIntervals.setDescription('This object gives the number of previous 15 minute intervals for which valid performance monitoring data has been stored on the interface. The value of this object will be n (where n is the maximum number of 15 minute intervals supported at this interface), unless the measurement was (re-)started within the last (nx15) minutes, in which case the value will be the number of previous 15 minute intervals for which the agent has some data.')
cOpticalMon24HrValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalMon24HrValidIntervals.setStatus('current')
if mibBuilder.loadTexts: cOpticalMon24HrValidIntervals.setDescription('This object gives the number of previous 24 hour intervals for which valid performance monitoring data has been stored on the interface. The value of this object will be 0 if the measurement was (re-)started within the last 24 hours, or 1 otherwise.')
cOpticalParamThreshSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 1, 1, 19), Bits().clone(namedValues=NamedValues(("highAlarmDefThresh", 0), ("highWarnDefThresh", 1), ("lowAlarmDefThresh", 2), ("lowWarnDefThresh", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalParamThreshSource.setStatus('current')
if mibBuilder.loadTexts: cOpticalParamThreshSource.setDescription("This object indicates if the current value of a particular threshold in this entry is user configured value or it is a system default value. It also allows user to specify the list of thresholds for this entry which should be restored to their system default values. The bit 'highAlarmThresh' corresponds to the object cOpticalParamHighAlarmThresh. The bit 'highWarnThresh' corresponds to the object cOpticalParamHighWarningThresh. The bit 'lowAlarmThresh' corresponds to the object cOpticalParamLowAlarmThresh. The bit 'lowWarnThresh' corresponds to the object cOpticalParamLowWarningThresh. A value of 0 for a bit indicates that corresponding object has system default value of threshold. A value of 1 for a bit indicates that corresponding object has user configured threshold value. A user may only change value of each of the bits to zero. Setting a bit to 0 will reset the corresponding threshold to its default value. System will change a bit from 0 to 1 when its corresponding threshold is changed by user from its default to any other value.")
cOpticalNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 2), OpticalAlarmSeverityOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: cOpticalNotifyEnable.setDescription("This object specifies the minimum severity threshold governing the generation of cOpticalMonParameterStatus notifications. For example, if the value of this object is set to 'major', then the agent generates these notifications if and only if the severity of the alarm being indicated is 'major' or 'critical'. The values of 'notReported', and 'cleared' do not apply. The value of '0' disables the generation of notifications.")
cOpticalMonEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 3), Bits().clone(namedValues=NamedValues(("all", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalMonEnable.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonEnable.setDescription("This object specifies the types of transceivers for which optical monitoring is enabled. A value of 1 for the bit 'all', specifies that optical monitoring functionality is enabled for all the types of transceivers which are supported by system and have optical monitoring capability.")
cOpticalMonPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 4), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cOpticalMonPollInterval.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonPollInterval.setDescription('This object specifies the interval in minutes after which optical transceiver data will be polled by system repeatedly and updated in cOpticalMonTable when one or more bits in cOpticalMonEnable is set.')
cOpticalMonIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5), )
if mibBuilder.loadTexts: cOpticalMonIfTable.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonIfTable.setDescription('This table contains the list of optical interfaces populated in cOpticalMonTable.')
cOpticalMonIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cOpticalMonIfEntry.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonIfEntry.setDescription('An entry containing the information for a particular optical interface.')
cOpticalMonIfTimeInSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 1, 5, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalMonIfTimeInSlot.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonIfTimeInSlot.setDescription('This object indicates when this optical transceiver was detected by the system.')
cOpticalPMCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1), )
if mibBuilder.loadTexts: cOpticalPMCurrentTable.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentTable.setDescription('This table contains performance monitoring data for the various optical parameters, collected over the current 15 minute or the current 24 hour interval.')
cOpticalPMCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentPeriod"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentDirection"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentLocation"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentParamType"))
if mibBuilder.loadTexts: cOpticalPMCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentEntry.setDescription('An entry in the cOpticalPMCurrentTable. It contains performance monitoring data for a monitored optical parameter at an interface, collected over the current 15 minute or the current 24 hour interval. Note that the set of monitored optical parameters may vary based on interface type, direction, and monitoring location. Examples of interfaces that can have an entry in this table include optical transceivers, interfaces before and after optical amplifiers, and interfaces before and after optical attenuators.')
cOpticalPMCurrentPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 1), OpticalPMPeriod())
if mibBuilder.loadTexts: cOpticalPMCurrentPeriod.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentPeriod.setDescription('This object indicates whether the optical parameter values given in this entry are collected over the current 15 minute or the current 24 hour interval.')
cOpticalPMCurrentDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 2), OpticalIfDirection())
if mibBuilder.loadTexts: cOpticalPMCurrentDirection.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentDirection.setDescription('This object indicates the direction monitored for the optical interface, in this entry.')
cOpticalPMCurrentLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 3), OpticalIfMonLocation())
if mibBuilder.loadTexts: cOpticalPMCurrentLocation.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentLocation.setDescription('This object indicates whether the optical characteristics are measured before or after adjustment (e.g. optical amplification or attenuation), at this interface.')
cOpticalPMCurrentParamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 4), OpticalParameterType())
if mibBuilder.loadTexts: cOpticalPMCurrentParamType.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentParamType.setDescription('This object specifies the optical parameter that is being monitored, in this entry.')
cOpticalPMCurrentMaxParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 5), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentMaxParam.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentMaxParam.setDescription('This object gives the maximum value measured for the monitored optical parameter, in the current 15 minute or the current 24 hour interval.')
cOpticalPMCurrentMinParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 6), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentMinParam.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentMinParam.setDescription('This object gives the minimum value measured for the monitored optical parameter, in the current 15 minute or the current 24 hour interval.')
cOpticalPMCurrentMeanParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 7), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentMeanParam.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentMeanParam.setDescription('This object gives the average value of the monitored optical parameter, in the current 15 minute or the current 24 hour interval.')
cOpticalPMCurrentUnavailSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMCurrentUnavailSecs.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMCurrentUnavailSecs.setDescription('This object is used to indicate the number of seconds, in the current 15 minute or the current 24 hour interval, for which the optical performance data is not accounted for. In the receive direction, the performance data could be unavailable during these periods for multiple reasons like the interface being administratively down or if there is a Loss of Light alarm on the interface. In the transmit direction, performance data could be unavailable when the laser is shutdown.')
cOpticalPMIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2), )
if mibBuilder.loadTexts: cOpticalPMIntervalTable.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalTable.setDescription('This table stores performance monitoring data for the various optical parameters, collected over previous intervals. This table can have entries for one complete 24 hour interval and up to 96 complete 15 minute intervals. A system is required to store at least 4 completed 15 minute intervals. The number of valid 15 minute intervals in this table is indicated by the cOpticalMon15MinValidIntervals object and the number of valid 24 hour intervals is indicated by the cOpticalMon24HrValidIntervals object.')
cOpticalPMIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalPeriod"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalNumber"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalDirection"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalLocation"), (0, "CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalParamType"))
if mibBuilder.loadTexts: cOpticalPMIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalEntry.setDescription('An entry in the cOpticalPMIntervalTable. It contains performance monitoring data for an optical parameter, collected over a previous interval. Note that the set of monitored optical parameters may vary based on interface type, direction, and monitoring location. Examples of interfaces that can have an entry in this table include optical transceivers, interfaces before and after optical amplifiers, and interfaces before and after optical attenuators.')
cOpticalPMIntervalPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 1), OpticalPMPeriod())
if mibBuilder.loadTexts: cOpticalPMIntervalPeriod.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalPeriod.setDescription('This object indicates whether the optical parameter values, given in this entry, are collected over a period of 15 minutes or 24 hours.')
cOpticalPMIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: cOpticalPMIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalNumber.setDescription('A number between 1 and 96, which identifies the interval for which the set of optical parameter values is available. The interval identified by 1 is the most recently completed 15 minute or 24 hour interval, and the interval identified by N is the interval immediately preceding the one identified by N-1.')
cOpticalPMIntervalDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 3), OpticalIfDirection())
if mibBuilder.loadTexts: cOpticalPMIntervalDirection.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalDirection.setDescription('This object indicates the direction monitored for the optical interface, in this entry.')
cOpticalPMIntervalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 4), OpticalIfMonLocation())
if mibBuilder.loadTexts: cOpticalPMIntervalLocation.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalLocation.setDescription('This object indicates whether the optical characteristics are measured before or after adjustment (e.g. optical amplification or attenuation), at this interface.')
cOpticalPMIntervalParamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 5), OpticalParameterType())
if mibBuilder.loadTexts: cOpticalPMIntervalParamType.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalParamType.setDescription('This object specifies the optical parameter that is being monitored, in this entry.')
cOpticalPMIntervalMaxParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 6), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalMaxParam.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalMaxParam.setDescription('This object gives the maximum value measured for the optical parameter, in a particular 15 minute or 24 hour interval.')
cOpticalPMIntervalMinParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 7), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalMinParam.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalMinParam.setDescription('This object gives the minimum value measured for the optical parameter, in a particular 15 minute or 24 hour interval.')
cOpticalPMIntervalMeanParam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 8), OpticalParameterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalMeanParam.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalMeanParam.setDescription('This object gives the average value of the measured optical parameter, in a particular 15 minute or 24 hour interval.')
cOpticalPMIntervalUnavailSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 264, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cOpticalPMIntervalUnavailSecs.setStatus('current')
if mibBuilder.loadTexts: cOpticalPMIntervalUnavailSecs.setDescription('This object is used to indicate the number of seconds, in the particular 15 minute or 24 hour interval, for which the optical performance data is not accounted for. In the receive direction, the performance data could be unavailable during these periods for multiple reasons like the interface being administratively down or if there is a Loss of Light alarm on the interface. In the transmit direction, performance data could be unavailable when the laser is shutdown.')
cOpticalMonitorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 2))
cOpticalMonNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 2, 0))
cOpticalMonParameterStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 264, 2, 0, 1)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParameterValue"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmStatus"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmLastChange"))
if mibBuilder.loadTexts: cOpticalMonParameterStatus.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonParameterStatus.setDescription("This notification is sent when any threshold related to an optical parameter is exceeded or cleared on an interface. This notification may be suppressed under the following conditions: - depending on the value of the cOpticalNotifyEnable object, or - if the severity of the threshold as specified by the cOpticalParamHighWarningSev or cOpticalParamLowWarningSev object is 'notReported'. ")
cOpticalMonitorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 3))
cOpticalMonitorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1))
cOpticalMonitorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2))
cOpticalMonitorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1, 1)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBMonGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBThresholdGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBSeverityGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBPMGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifyEnableGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonitorMIBCompliance = cOpticalMonitorMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cOpticalMonitorMIBCompliance.setDescription('The compliance statement for network elements that monitor optical characteristics and set thresholds on the optical interfaces in a network element.')
cOpticalMonitorMIBComplianceRev = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 1, 2)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBMonGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBThresholdGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBSeverityGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBPMGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonIfTimeGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifyEnableGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBNotifGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBEnableConfigGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMIBIntervalConfigGroup"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonThreshSourceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonitorMIBComplianceRev = cOpticalMonitorMIBComplianceRev.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonitorMIBComplianceRev.setDescription('The compliance statement for network elements that monitor optical characteristics and set thresholds on the optical interfaces in a network element.')
cOpticalMIBMonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 1)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParameterValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBMonGroup = cOpticalMIBMonGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBMonGroup.setDescription('A mandatory object that provides monitoring of optical characteristics.')
cOpticalMIBThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 2)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarningThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarningThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmStatus"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxThresh"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBThresholdGroup = cOpticalMIBThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBThresholdGroup.setDescription('A collection of objects that support thresholds on optical parameters and provide status information when the thresholds are exceeded or cleared.')
cOpticalMIBSeverityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 3)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighAlarmSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamHighWarningSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowAlarmSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamLowWarningSev"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamAlarmCurMaxSev"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBSeverityGroup = cOpticalMIBSeverityGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBSeverityGroup.setDescription('A collection of objects that support severities for thresholds on optical parameters.')
cOpticalMIBPMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 4)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMon15MinValidIntervals"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMon24HrValidIntervals"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMaxParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMinParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentMeanParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMCurrentUnavailSecs"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMaxParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMinParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalMeanParam"), ("CISCO-OPTICAL-MONITOR-MIB", "cOpticalPMIntervalUnavailSecs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBPMGroup = cOpticalMIBPMGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBPMGroup.setDescription('A collection of objects that provide optical performance monitoring data for 15 minute and 24 hour intervals.')
cOpticalMIBNotifyEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 5)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBNotifyEnableGroup = cOpticalMIBNotifyEnableGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBNotifyEnableGroup.setDescription('An object to control the generation of notifications.')
cOpticalMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 6)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonParameterStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBNotifGroup = cOpticalMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBNotifGroup.setDescription('A notification generated when a threshold on an optical parameter is exceeded or cleared.')
cOpticalMonIfTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 7)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonIfTimeInSlot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonIfTimeGroup = cOpticalMonIfTimeGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonIfTimeGroup.setDescription('A collection of object(s) that provide time related information for transceivers in the system.')
cOpticalMIBEnableConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 8)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBEnableConfigGroup = cOpticalMIBEnableConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBEnableConfigGroup.setDescription('A collection of object(s) to enable/disable optical monitoring.')
cOpticalMIBIntervalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 9)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalMonPollInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMIBIntervalConfigGroup = cOpticalMIBIntervalConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMIBIntervalConfigGroup.setDescription('A collection of object(s) to specify polling interval for monitoring optical transceivers.')
cOpticalMonThreshSourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 264, 3, 2, 10)).setObjects(("CISCO-OPTICAL-MONITOR-MIB", "cOpticalParamThreshSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cOpticalMonThreshSourceGroup = cOpticalMonThreshSourceGroup.setStatus('current')
if mibBuilder.loadTexts: cOpticalMonThreshSourceGroup.setDescription('A collection of object(s) to restore a given threshold to its default value.')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-MIB", OpticalParameterValue=OpticalParameterValue, cOpticalMonitorMIBComplianceRev=cOpticalMonitorMIBComplianceRev, cOpticalPMCurrentParamType=cOpticalPMCurrentParamType, cOpticalPMIntervalLocation=cOpticalPMIntervalLocation, cOpticalPMCurrentTable=cOpticalPMCurrentTable, OpticalAlarmSeverityOrZero=OpticalAlarmSeverityOrZero, cOpticalPMIntervalUnavailSecs=cOpticalPMIntervalUnavailSecs, cOpticalMonGroup=cOpticalMonGroup, cOpticalParamThreshSource=cOpticalParamThreshSource, cOpticalMonThreshSourceGroup=cOpticalMonThreshSourceGroup, cOpticalPMCurrentMaxParam=cOpticalPMCurrentMaxParam, cOpticalMIBMonGroup=cOpticalMIBMonGroup, cOpticalMon15MinValidIntervals=cOpticalMon15MinValidIntervals, cOpticalParamLowAlarmThresh=cOpticalParamLowAlarmThresh, OpticalIfDirection=OpticalIfDirection, cOpticalMonIfEntry=cOpticalMonIfEntry, cOpticalPMCurrentLocation=cOpticalPMCurrentLocation, cOpticalPMGroup=cOpticalPMGroup, cOpticalParamAlarmStatus=cOpticalParamAlarmStatus, cOpticalPMIntervalParamType=cOpticalPMIntervalParamType, cOpticalMIBEnableConfigGroup=cOpticalMIBEnableConfigGroup, cOpticalMonParameterType=cOpticalMonParameterType, OpticalIfMonLocation=OpticalIfMonLocation, ciscoOpticalMonitorMIB=ciscoOpticalMonitorMIB, cOpticalMIBThresholdGroup=cOpticalMIBThresholdGroup, cOpticalPMCurrentDirection=cOpticalPMCurrentDirection, cOpticalPMCurrentMinParam=cOpticalPMCurrentMinParam, cOpticalMIBNotifGroup=cOpticalMIBNotifGroup, OpticalPMPeriod=OpticalPMPeriod, cOpticalParamHighAlarmThresh=cOpticalParamHighAlarmThresh, cOpticalMonitorMIBObjects=cOpticalMonitorMIBObjects, cOpticalPMIntervalEntry=cOpticalPMIntervalEntry, cOpticalParamLowWarningSev=cOpticalParamLowWarningSev, cOpticalPMCurrentUnavailSecs=cOpticalPMCurrentUnavailSecs, cOpticalMonIfTimeInSlot=cOpticalMonIfTimeInSlot, OpticalParameterType=OpticalParameterType, cOpticalNotifyEnable=cOpticalNotifyEnable, cOpticalParamHighAlarmSev=cOpticalParamHighAlarmSev, cOpticalPMIntervalTable=cOpticalPMIntervalTable, cOpticalMonIfTable=cOpticalMonIfTable, cOpticalPMIntervalMaxParam=cOpticalPMIntervalMaxParam, cOpticalMonitorMIBNotifications=cOpticalMonitorMIBNotifications, cOpticalMonPollInterval=cOpticalMonPollInterval, cOpticalParamAlarmCurMaxThresh=cOpticalParamAlarmCurMaxThresh, cOpticalParamAlarmLastChange=cOpticalParamAlarmLastChange, cOpticalMIBSeverityGroup=cOpticalMIBSeverityGroup, cOpticalMIBIntervalConfigGroup=cOpticalMIBIntervalConfigGroup, cOpticalPMCurrentPeriod=cOpticalPMCurrentPeriod, cOpticalMon24HrValidIntervals=cOpticalMon24HrValidIntervals, cOpticalMonDirection=cOpticalMonDirection, cOpticalPMIntervalPeriod=cOpticalPMIntervalPeriod, cOpticalParamHighWarningSev=cOpticalParamHighWarningSev, cOpticalMonitorMIBCompliance=cOpticalMonitorMIBCompliance, cOpticalMonitorMIBCompliances=cOpticalMonitorMIBCompliances, OpticalAlarmSeverity=OpticalAlarmSeverity, OpticalAlarmStatus=OpticalAlarmStatus, PYSNMP_MODULE_ID=ciscoOpticalMonitorMIB, cOpticalPMIntervalMinParam=cOpticalPMIntervalMinParam, cOpticalMonEntry=cOpticalMonEntry, cOpticalMonNotificationPrefix=cOpticalMonNotificationPrefix, cOpticalParamLowWarningThresh=cOpticalParamLowWarningThresh, cOpticalParamLowAlarmSev=cOpticalParamLowAlarmSev, cOpticalPMCurrentEntry=cOpticalPMCurrentEntry, cOpticalMIBNotifyEnableGroup=cOpticalMIBNotifyEnableGroup, cOpticalMIBPMGroup=cOpticalMIBPMGroup, cOpticalParamAlarmCurMaxSev=cOpticalParamAlarmCurMaxSev, cOpticalMonIfTimeGroup=cOpticalMonIfTimeGroup, cOpticalParameterValue=cOpticalParameterValue, cOpticalMonitorMIBConformance=cOpticalMonitorMIBConformance, cOpticalPMIntervalDirection=cOpticalPMIntervalDirection, cOpticalParamHighWarningThresh=cOpticalParamHighWarningThresh, cOpticalPMIntervalMeanParam=cOpticalPMIntervalMeanParam, cOpticalPMIntervalNumber=cOpticalPMIntervalNumber, cOpticalMonParameterStatus=cOpticalMonParameterStatus, cOpticalMonTable=cOpticalMonTable, cOpticalMonLocation=cOpticalMonLocation, cOpticalMonEnable=cOpticalMonEnable, cOpticalMonitorMIBGroups=cOpticalMonitorMIBGroups, cOpticalPMCurrentMeanParam=cOpticalPMCurrentMeanParam)
