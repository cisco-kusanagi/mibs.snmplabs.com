#
# PySNMP MIB module CISCO-WIRELESS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WIRELESS-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:21:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, iso, Bits, MibIdentifier, Gauge32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "iso", "Bits", "MibIdentifier", "Gauge32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWirelessTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 137))
ciscoWirelessTextualConventions.setRevisions(('2000-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setRevisionsDescriptions(('Added TEXTUAL-CONVENTIONs for CwrRfType CwrFixedPointScale CwrFixedPointPrecison CwrFixedPointValue P2mpSnapshotAttribute CwrPercentageValue CwrRfFreqRange CwrUpdateTime Modified P2mpRadioSignalAttribute',))
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setLastUpdated('200004030000Z')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: wireless-nms@cisco.com')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setDescription('This module defines textual conventions used in Cisco Wireless MIBs.')
class CwrRFZeroIndex(TextualConvention, Integer32):
    description = 'This represents an index into the cwrRFTable. The valid values are from 1 onwards. The special value of 0 is used to indicate the absence of the associated RF resource.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2)

class CwrCwErrorFreeSecond(TextualConvention, Gauge32):
    description = 'A Codeword Error Free Second (EFS) is defined as 1 second when the radio link was synchronized and no codeword errors detected on the link.'
    status = 'current'

class CwrCwErroredSecond(TextualConvention, Gauge32):
    description = 'A Codeword Errored Second (ES) is defined as 1 second when the radio link was synchronized and 1 or more codeword errors were detected on the link.'
    status = 'current'

class CwrCwSeverelyErroredSecond(TextualConvention, Gauge32):
    description = 'A Codeword Severely Errored Second (SES) is defined as 1 second when the radio link was synchronized and the codeword error rate (CER) was greater than the threshold specified by cwrLinkHighCwErrThresh.'
    status = 'current'

class CwrCwConsecutiveSevErrSecond(TextualConvention, Gauge32):
    description = 'A Codeword Consecutively Severely Errored Seconds (CSES) is defined as the metric that measures the number of times a sequence of Codeword Severely Errored Seconds(SES) crosses the cwrLinkCSESThresh value. It is independent of the length of the SES sequence. In other words this counter is incremented by one and only one for every such occurrence.'
    status = 'current'

class CwrCwDegradedSecond(TextualConvention, Gauge32):
    description = 'A Codeword Degraded Second (DS) is defined as a 1 second interval during which the CER was between cwrLinkLowCwErrThresh and cwrLinkHighCwErrThresh.'
    status = 'current'

class CwrCwDegradedMinute(TextualConvention, Gauge32):
    description = 'A Codeword Degraded Minute (DM) is defined as a 60 Codeword Degraded Seconds.'
    status = 'current'

class CwrCollectionAction(TextualConvention, Integer32):
    description = 'The action to perform on the identified specification. It can be: Stop: Stop the collection specification from continuing. Start: Start the collection specification. Clear: Clear the current collection data. A collection in progress must be stopped before it can be cleared. Restart: Identical to Clear followed by a Start.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("actionStop", 1), ("actionStart", 2), ("actionClear", 3), ("actionRestart", 4))

class CwrCollectionStatus(TextualConvention, Integer32):
    description = 'This indicates the current status of the collection specification. It can be: Idle: No action in progress. In_progress: Collection specification is currently being executed Stopped: The collection specification has been stopped before it completed successfully. Captured: The collection is complete and data is available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("statusIdle", 1), ("statusInProgress", 2), ("statusStopped", 3), ("statusCaptured", 4))

class CwrdBm(TextualConvention, Integer32):
    description = 'This is a unit of power measurement. It is measured in decibels of milliwatts (dBm). dBm = 10 * log(millwatts of power).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-80, 33)

class CwrdB(TextualConvention, Integer32):
    description = 'This is a unit of measurement defined as decibels (dB). dB = 10 * log(measured_value).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16)

class CwrThreshLimitType(TextualConvention, Integer32):
    description = 'This object represents the kind of change that needs to be monitored for a thresholdable attribute . An event is generated when the following condition is met. The kinds of change that may be setup in the radio hardware are: upChange : Monitored value changes by a positive amount. downChange : Monitored value changes by a negative amount. highThresh : Monitored value exceeds specified threshold. lowThresh : Monitored value receeds below a threshold. upLimit : Monitored value crosses the specified threshold when increasing in value. lowLimit : Monitored value crosses the specified threshold when decreasing in value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("upChange", 1), ("downChange", 2), ("highThresh", 3), ("lowThresh", 4), ("upLimit", 5), ("lowLimit", 6))

class CwrRadioSignalAttribute(TextualConvention, Integer32):
    description = 'This represents the set of radio signal attributes that may be monitored by using histograms, timelines, and thresholds. The attributes are: rsaIN(1) - This is the Interference + Noise power levels computed by the hardware on a burst by burst basis. This is available for a dual antenna system only. rsaINR(2) - This is the ratio of the interference+noise power levels captured by first antenna to that captured by the second antenna on a burst by burst basis. The values reported are in log to base 2. rsaConstellationVariance(3) - Constellation variance(CV) is the average energy of the constellation error signal. The constellation error signal is the error between the received (noisy) constellation symbol and the nearest ideal constellation symbol. CV is a measure of the Signal to Interference+noise ratio, (SINR) for that tone. On a Single antenna system it represents (1/SINR). On a Dual antenna system it represents a composite histogram providing (1/SINR). rsaTimingOffset(4) - This represents the histogram of timing delay variations detected in radio link. rsaReceivedPower(5) - This is a measure of the analog signal power received by the radio system on a burst by burst basis. rsaGainSettingsIF(6) - This represents the change in the automatic gain control loop maintained by the hardware. This may be captured for each antenna and at the intermediate frequency (IF) module. Units: Integral values rsaGainSettingsRF(7) - This represents the change in the automatic gain control loop maintained by the hardware. This may be captured for each antenna and at both the intermediate frequency (IF) and radio frequency (RF) modules. Units: Integral values rsaFreqOffset(8) - This represents the frequency offset calculations made to keep the receive frequency on a slave radio in sync with the master radio. Units: Integral values. rsaTotalGain(9) - This represents the change in the automatic gain control loop maintained by the hardware. This may be captured for each antenna. Units: Integral values rsaSyncStatus(10) - This represents the sync status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rsaIN", 1), ("rsaINR", 2), ("rsaConstellationVariance", 3), ("rsaTimingOffset", 4), ("rsaReceivedPower", 5), ("rsaGainSettingsIF", 6), ("rsaGainSettingsRF", 7), ("rsaFreqOffset", 8), ("rsaTotalGain", 9), ("rsaSyncStatus", 10))

class CwrOscState(TextualConvention, Integer32):
    description = 'The current state of the oscillator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oscillatorOk", 1), ("osccillatorBad", 2))

class P2mpRadioSignalAttribute(TextualConvention, Integer32):
    description = 'This represents the set of radio signal attributes that may be monitored in a point to multipoint system by using histograms, timelines, and thresholds. Some of these attributes are common to the head end (HE) and the subscriber unit (SU) whereas some are specific to either the HE or the SU. The attributes are: none(0) - This is a special value reserved to indicate that there is no threshold associated with a timeline. This attribute cannot be used to create a histogram, timeline, or threshold. rsaSinrMainAnt(1) - This is the Interference + Noise power level computed by the hardware at the main antenna on a burst by burst basis rsaSinrDiversityAnt(2) - This is the Interference + Noise power level computed by the hardware at the diversity antenna on a burst by burst basis. rsaSinrRatio(3) - Ratio of (Interference + Noise) in main antenna to diversity antenna rsaTimingOffset(4) - This represents the timing delay variations detected on a radio link. rsaRxPowerMainAnt(5) - This is a measure of the analog signal power received at the main antenna RF head on a burst by burst basis. rsaRxPowerDiversityAnt(6) - This is a measure of the analog signal power received at the diversity antenna RF head on a burst by burst basis. rsaChDelaySpreadMainAnt(7) - Number of samples that the channel response remains within (TBD) db of the manimun TAP in the channel response at the main antenna. rsaChDelaySpreadDiversityAnt(8) - Number of samples that the channel response remains within (TBD) db of the manimun TAP in the channel response at the diversity antenna. rsaHeAmbientNoise(19) - The ambient noise (in dB) is measured when there is no signal being received at the Headend rsaSuRxPowerDeltaMainAnt(10) - Change in received power (dB) at the main antenna of the subscriber unit on a burst by burst basis. rsaSuRxPowerDeltaDiversityAnt(11) - Change in received power (dB) at the diversity antenna of the subscriber unit on a burst by burst basis. rsaSuTotalTxPower(12) - The sum of -20 dBm (reference level out of the DAC) + Tx IF transmit gain - 13 dBm (cable compensation) + Tx RF transmit gain. This parameter does not include antenna gains. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 0), ("rsaSinrMainAnt", 1), ("rsaSinrDiversityAnt", 2), ("rsaSinrRatio", 3), ("rsaTimingOffset", 4), ("rsaRxPowerMainAnt", 5), ("rsaRxPowerDiversityAnt", 6), ("rsaChDelaySpreadMainAnt", 7), ("rsaChDelaySpreadDiversityAnt", 8), ("rsaHeAmbientNoise", 9), ("rsaSuRxPowerDeltaMainAnt", 10), ("rsaSuRxPowerDeltaDiversityAnt", 11), ("rsaSuTotalTxPower", 12))

class CwrRfType(TextualConvention, Integer32):
    description = 'Indicates if the outdoor RF unit is being used as the main RF unit or the diversity RF unit. The main RF unit is used to receive and transmit data whereas the diversity unit is used to receive only.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("main", 0), ("diversity", 1))

class CwrFixedPointScale(TextualConvention, Integer32):
    description = 'International System of Units (SI) prefixes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class CwrFixedPointPrecision(TextualConvention, Integer32):
    description = 'When in the range 1 to 9, CwrFixedPointPrecision is the number of decimal places in the fractional part of a fixed-point number. CwrFixedPointPrecision is 0 for non-fixed-point numbers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 9)

class CwrFixedPointValue(TextualConvention, Integer32):
    description = 'This represents a fixed point number. Use values -2147483648 and +2147483647 to indicate underflow and overflow respectively. Use CwrFixedPointPrecision to indicate how many fractional digits the CwrFixedPointValue has.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class P2mpSnapshotAttribute(TextualConvention, OctetString):
    description = 'This represents the set of radio signal attributes that may be monitored by using a snapshot. The user can capture upto 4 radio signal attributes simultaneously, by picking at most one signal from each of the sets below and setting the bit corresponding to each selected signal. When a snapshot request is issued up to four radio signal attributes may be requested at once, one from each set: =============================================== Type Set1 Set2 =============================================== RX y1n(x1) y2n(x2) H2k(x80) H1k(x40) =============================================== =============================================== Type Set3 Set4 =============================================== RX Y2k(x8) Y1k(x4) h1n(x10) h2n(x20) zhat(x100) - =============================================== The attributes are: rxRawBurstAnt1Y1n(0) - This represents a snapshot of the received signal for the main RF resource. For every sample, the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxRawBurstAnt2Y2n(1) - This represents a snapshot of the received signal for the diversity RF resource. For every sample, the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxSpectrumAnt1Y1k(2) - This represents a snapshot of the spectrum of the received signal for the main RF resource. For every sample, the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxSpectrumAnt2Y2k(3) - This represents a snapshot of the spectrum of the received signal for the diversity RF resource. For every sample the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxTimeDomainChannelAnt1H1n(4) - This represents a snapshot of the time domain channel for the main RF resource. For every sample the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxTimeDomainChannelAnt2H2n(5) - This represents a snapshot of the time domain channel for the diversity RF resource. For every sample, the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxFreqDomainChannelAnt1H1k(6) - This represents a snapshot of the frequency domain channel for the main RF resource. For every sample the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxFreqDomainChannelAnt2H2k(7) - This represents a snapshot of the frequency domain channel for the diversity RF resource. For every sample, the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities. rxConstellationZHatk(8) - This represents a snapshot of the soft decisions. For every sample, the real and imaginary components are captured. Units: (I, q) Value: 32 bit quantities.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class CwrPercentageValue(TextualConvention, Gauge32):
    description = 'This object can be used to represent percentage values for codeword errors, available seconds, etc. The UNITS clause associated with each object will indicate the degree of precison.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000000)

class CwrUpdateTime(TextualConvention, Integer32):
    description = 'This is used to report statistics values measured on the wireless link with a 1 second granularity insted of timeTicks. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CwrRfFreqRange(TextualConvention, Integer32):
    description = 'This represents the entire radio frequency range for a wireless radio product. The lower limit is assumed to be zero.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 60000000)

class WirelessGauge64(TextualConvention, Counter64):
    description = "This is a temporary textual convention that will be deleted from this MIB when all references to this TC have been changed to use 'CounterBasedGauge64' defined in RFC 2856"
    status = 'current'

mibBuilder.exportSymbols("CISCO-WIRELESS-TC-MIB", CwrRfFreqRange=CwrRfFreqRange, ciscoWirelessTextualConventions=ciscoWirelessTextualConventions, CwrCwDegradedMinute=CwrCwDegradedMinute, CwrCwErroredSecond=CwrCwErroredSecond, CwrCwSeverelyErroredSecond=CwrCwSeverelyErroredSecond, CwrCollectionAction=CwrCollectionAction, CwrCwDegradedSecond=CwrCwDegradedSecond, CwrOscState=CwrOscState, PYSNMP_MODULE_ID=ciscoWirelessTextualConventions, CwrdBm=CwrdBm, CwrThreshLimitType=CwrThreshLimitType, CwrCwConsecutiveSevErrSecond=CwrCwConsecutiveSevErrSecond, CwrRFZeroIndex=CwrRFZeroIndex, CwrCollectionStatus=CwrCollectionStatus, P2mpRadioSignalAttribute=P2mpRadioSignalAttribute, CwrRadioSignalAttribute=CwrRadioSignalAttribute, CwrFixedPointPrecision=CwrFixedPointPrecision, CwrRfType=CwrRfType, CwrPercentageValue=CwrPercentageValue, CwrdB=CwrdB, CwrCwErrorFreeSecond=CwrCwErrorFreeSecond, WirelessGauge64=WirelessGauge64, CwrFixedPointScale=CwrFixedPointScale, P2mpSnapshotAttribute=P2mpSnapshotAttribute, CwrUpdateTime=CwrUpdateTime, CwrFixedPointValue=CwrFixedPointValue)
