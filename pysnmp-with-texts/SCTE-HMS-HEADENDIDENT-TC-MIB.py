#
# PySNMP MIB module SCTE-HMS-HEADENDIDENT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCTE-HMS-HEADENDIDENT-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, TimeTicks, enterprises, MibIdentifier, Bits, ModuleIdentity, Counter64, IpAddress, ObjectIdentity, NotificationType, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "TimeTicks", "enterprises", "MibIdentifier", "Bits", "ModuleIdentity", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmsTextualConventionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 1))
hmsTextualConventionMIB.setRevisions(('2008-07-23 13:00', '2008-07-12 13:00', '2008-01-16 13:00', '2007-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmsTextualConventionMIB.setRevisionsDescriptions(('Changed enumeration for QAMChannelInterleaveMode.', 'Modifications due to Comment Resolution Phase 2 1. Un-Commented out HeAlarmControl, HeTrapRegenerate to add Alarm Processing back into the HMS-154 mib files. 2. Added support for Alarm Processing. 3. Removed enumerations that were not used under the heDigital tree (heLaserType). 4. Modified QAMChannelModulationFormat. 5. Removed Display String from IMPORTS 6. Removed HeLaserType 7. Added enumeration QAMChannelInterleaveMode', 'Modifications due to Comment Resolution Meeting 1. Commented out HeAlarmControl, HeTrapRegenerate, HeDigitalRedundancyStatus per Comment Resolution meeting for formal release of the Mib File. 2. Added comments to HeDigitalAlarmSeverity and HeDigitalAlarmType that they are not used per Comment Resolution meeting for formal release of the Mib File, and commented out the enumerations so no-one uses them until they are needed in case they will have to change. 3. Added the enumeration other to HeDigitalAlarmType so it would be universal.', 'Modifications due to voting comments 1. Changed syntax errors for capitalized words. 2. Changed mib to have the -MIB extention',))
if mibBuilder.loadTexts: hmsTextualConventionMIB.setLastUpdated('200807231300Z')
if mibBuilder.loadTexts: hmsTextualConventionMIB.setOrganization('SCTE HMS Working Group')
if mibBuilder.loadTexts: hmsTextualConventionMIB.setContactInfo('SCTE HMS Subcommittee, Chairman mail to: standards@scte.org ')
if mibBuilder.loadTexts: hmsTextualConventionMIB.setDescription('The MIB module is for representing general information about HeadEnd Digital equipment present(or indoor) and is supported by an SNMP agent.')
class VideoInputFrameRateType(TextualConvention, Integer32):
    description = ' This value defines the types of MPEG Video Input Frame Rate that is supported by QAM devices.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("autoSelect", 2), ("f24Hz", 3), ("f25Hz", 4), ("f29Hz97", 5), ("f30Hz", 6), ("f29or30Hz", 7), ("f48Hz", 8), ("f50Hz", 9), ("f59Hz94", 10), ("f60Hz", 11), ("f59or60Hz", 12))

class QAMChannelModulationFormat(TextualConvention, Integer32):
    description = ' This value defines the types of QAM Channel Modulation that is supported by QAM devices.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("qam64", 3), ("qam256", 4), ("qam128", 5), ("qam512", 6), ("qam1024", 7))

class QAMChannelInterleaveMode(TextualConvention, Integer32):
    description = ' This value defines the types of QAM Interleave Mode which follows the value of docsIfDownChannelInterleave. This value is supported by HMS QAM devices.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("fecI8J16", 3), ("fecI16J8", 4), ("fecI32J4", 5), ("fecI64J2", 6), ("fecI128J1", 7), ("fecI12J17", 8), ("fecI128J2", 9), ("fecI128J3", 10), ("fecI128J4", 11), ("fecI128J5", 12), ("fecI128J6", 13), ("fecI128J7", 14), ("fecI128J8", 15))

class ProgDataType(TextualConvention, Integer32):
    description = 'This value defines the types of data that can be contained in Programs and program streams.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("video", 1), ("audio", 2), ("data", 3), ("other", 4))

class DeviceEnableDisableValues(TextualConvention, Integer32):
    description = "This data type represents whether the object is disabled(1) or enabled(2), or the object is not supported (3) by the current configuration or this device's hardware."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("notSupported", 3))

class MpegErrorStatus(TextualConvention, Integer32):
    description = "This data type represents whether the object is good(1) or has errors(2), or the object is not supported (3) by the current configuration or this device's hardware."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("good", 1), ("errors", 2), ("notSupported", 3))

class HePIDValue(TextualConvention, Unsigned32):
    description = 'This data type represents a packet identifier (PID) value which ranges from 0 to (2^13 - 1). The value of 65535 indicates that either the PID is invalid or does not exist.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 8191), ValueRangeConstraint(65535, 65535), )
class HeClockSource(TextualConvention, Integer32):
    description = 'An enumerated value that provides the location where the value for the clock on the module is coming from. internal - this value is being derived internally from the local module timing source. external - an source that is external to the module, such as a controller card is providing a signal to calculate the real time clock. ntp - this module is running the ntp protocol and can sync up to a master ntp clock source. other - the real time clock source does not fit into the existing values. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("internal", 3), ("external", 4), ("ntp", 5), ("none", 6))

class HeResetValue(TextualConvention, Integer32):
    description = 'Configured reset value for a specific device. reset - the value of reset is SET at the device and the device will reset. running - the normal value of the device is running when an SNMP GET of the reset value is sent. resetting - The value resetting shall be returned if an SNMP GET of the device is performed after a reset SET command is sent and before the device can actually perform the reset. A second reset SET command should not interrupt the reset sequence. If a second SET is sent, it will be ignored. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reset", 1), ("running", 2), ("resetting", 3))

class HeTenthVolt(TextualConvention, Integer32):
    description = 'This data type represents voltage levels that are normally expressed in volts. Units are in tenths of a volt; for example, -48.1 volts will be represented as -481.'
    status = 'current'
    displayHint = 'd-1'

class HeTenthdBm(TextualConvention, Integer32):
    description = 'This data type represents power levels that are normally expressed in dBm. Units are in tenths of a dBm; for example, -5.1 dBm will be represented as -51.'
    status = 'current'
    displayHint = 'd-1'

class HeTenthdBmV(TextualConvention, Integer32):
    description = 'This data type represents power levels that are normally expressed in dBmV. Units are in tenths of a dBmV; for example, -5.1 dBmV will be represented as -51.'
    status = 'current'
    displayHint = 'd-1'

class HeTenthCentigrade(TextualConvention, Integer32):
    description = 'This data type represents temperature values that are normally expressed in Centigrade. Units are in tenths of a Centigrade; for example, -5.1 Centigrade will be represented as -51.'
    status = 'current'
    displayHint = 'd-1'

class HeHundredthNanoMeter(TextualConvention, Unsigned32):
    description = 'This data type represents wavelength values that are normally expressed in nano meters. Units are in hundredths of a NanoMeter; for example, 1550.56 nm will be represented as 155056.'
    status = 'current'
    displayHint = 'd-2'

class HeTenthdB(TextualConvention, Integer32):
    description = 'This data type represents power levels that are normally expressed in dB. Units are in tenths of a dB; for example, -5.1 dB will be represented as -51.'
    status = 'current'
    displayHint = 'd-1'

class HeOnOffControl(TextualConvention, Integer32):
    description = 'An enumerated value that provides a control of a particular hardware or software parameter that usually represent some sort of switch. A SET request with a value off(1) will cause the switch to be shut off. A SET request with a value on(2) will cause the switch to be turned on. A value meaningless(3) will be implemented by the variables that represent a switch with write-only access. A GET request for the value of the write-only variable shall return a value meaningless(3). A SET request with a value meaningless(3) for the variable with write access shall have no effect and no exception is generated. A value may be used by the variables with both read-write and write-only access. The variables with read-only access shall be defined with the textual convention HeOnOffStatus.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("meaningless", 3))

class HeOnOffStatus(TextualConvention, Integer32):
    description = 'An enumerated value that provides a status of a particular hardware or software parameter that usually represent some sort of switch. A value off(1) indicates the switch is off. A value on(2) indicates the switch is on.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("on", 2))

class HeAlarmControl(TextualConvention, Integer32):
    description = 'Alarm Control value for a specific device. This object is used to control sending traps related to this headend entity or enabling disabling of raising an alarm condition for a specific entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alarmEnabled", 1), ("alarmDisabled", 2))

class HeTrapRegenerate(TextualConvention, Integer32):
    description = ' This value tells the SNMP Agent to send the Trap Regenerate Trap for all values of Current alarms for this entity. The device can provide for a means to send ALL current alarms, not just one specific entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trapRegenerate", 1), ("trapNormal", 2))

class HeDigitalAlarmSeverity(TextualConvention, Integer32):
    description = ' The alarm severity that is determined by the device and sent over in the trap message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("status", 5), ("clear", 6), ("information", 7))

class HeDigitalAlarmType(TextualConvention, Integer32):
    description = ' The alarm type that describes the Event that caused the alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("communication", 1), ("process", 2), ("session", 3), ("capacity", 4), ("maintenance", 5), ("provisioning", 6), ("programMgmt", 7), ("redundancy", 8), ("other", 9))

class HeFaultStatus(TextualConvention, Integer32):
    description = 'An enumerated value that provides a fault status of a particular hardware or software parameter that usually represent some sort of condition. A value normal(1) indicates the normal condition. A value fault(2) indicates the fault condition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("fault", 2))

class HeMilliAmp(TextualConvention, Unsigned32):
    description = 'This data type represents current levels that are normally expressed in amperes. Units are in milliamperes; for example, 2.1 Amperes would be expressed as 2100.'
    status = 'current'
    displayHint = 'd-3'

class HeHundredthWatts(TextualConvention, Unsigned32):
    description = 'This data type represents power values that are normally expressed in watts. Units are in hundredths of a watt; for example, 420 watts will be represented as 42000.'
    status = 'current'
    displayHint = 'd-2'

mibBuilder.exportSymbols("SCTE-HMS-HEADENDIDENT-TC-MIB", HeHundredthNanoMeter=HeHundredthNanoMeter, HeMilliAmp=HeMilliAmp, ProgDataType=ProgDataType, MpegErrorStatus=MpegErrorStatus, QAMChannelInterleaveMode=QAMChannelInterleaveMode, HeAlarmControl=HeAlarmControl, HeTenthdBmV=HeTenthdBmV, HeTenthdB=HeTenthdB, PYSNMP_MODULE_ID=hmsTextualConventionMIB, DeviceEnableDisableValues=DeviceEnableDisableValues, HeTenthCentigrade=HeTenthCentigrade, HeClockSource=HeClockSource, HeResetValue=HeResetValue, HeTrapRegenerate=HeTrapRegenerate, HeOnOffStatus=HeOnOffStatus, HeTenthVolt=HeTenthVolt, VideoInputFrameRateType=VideoInputFrameRateType, HeHundredthWatts=HeHundredthWatts, QAMChannelModulationFormat=QAMChannelModulationFormat, HeDigitalAlarmType=HeDigitalAlarmType, HeFaultStatus=HeFaultStatus, HeOnOffControl=HeOnOffControl, HePIDValue=HePIDValue, HeTenthdBm=HeTenthdBm, hmsTextualConventionMIB=hmsTextualConventionMIB, HeDigitalAlarmSeverity=HeDigitalAlarmSeverity)
