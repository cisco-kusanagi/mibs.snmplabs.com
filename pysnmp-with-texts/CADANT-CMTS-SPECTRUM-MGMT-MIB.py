#
# PySNMP MIB module CADANT-CMTS-SPECTRUM-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-SPECTRUM-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:45:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
cadIfUpstreamChannelEntry, = mibBuilder.importSymbols("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpstreamChannelEntry")
cadSpectrum, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadSpectrum")
TenthdB, = mibBuilder.importSymbols("DOCS-IF-MIB", "TenthdB")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, ModuleIdentity, iso, Bits, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Counter32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "Gauge32")
TextualConvention, TruthValue, DisplayString, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus", "DateAndTime")
cadSpMgtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4))
cadSpMgtMib.setRevisions(('2013-04-30 00:00', '2012-07-03 00:00', '2012-07-02 00:00', '2006-02-21 00:00', '2006-02-06 00:00', '2005-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadSpMgtMib.setRevisionsDescriptions(('Support cadSpMgtStateFrequency up to 85MHz.', 'Added state change count in history entry.', 'Added cadSpMgtHistorySysUpTime in history entry.', 'Use cadSpMgtHistoryTime for index.', 'Added spectrum group id in history entry.', 'Initial version.',))
if mibBuilder.loadTexts: cadSpMgtMib.setLastUpdated('201304300000Z')
if mibBuilder.loadTexts: cadSpMgtMib.setOrganization('Arris International Inc.')
if mibBuilder.loadTexts: cadSpMgtMib.setContactInfo('Customer Support Address: Arris Group Inc. 2400 E. Ogden Avenue, Suite 180 Lisle, IL 60532 Phone: +1 630 281 3000')
if mibBuilder.loadTexts: cadSpMgtMib.setDescription('The MIB module describes the C4 Upstream Spectrum Management')
cadSpMgtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 1))
cadSpMgtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2))
cadSpMgtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 3))
cadSpMgtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1))
cadSpMgtRequests = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2))
class SpTriggerType(TextualConvention, Integer32):
    description = 'The trigger is used to manage the state transition in C4 Upstream Spectrum Management State Machine. The trigger has the following defined values: TOD - defined with <Time of Day> and reoccurring day within a week Periodic - defined with a period of time degradation - defined with 3 threshold value for the purpose of degradation improvement - defined with 3 threshold value for the purpose of improvement '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tod", 1), ("periodic", 2), ("degradation", 3), ("improvement", 4))

class SpTriggerDay(TextualConvention, Integer32):
    description = 'The trigger day is to specify the reoccurrence of the TOD trigger for a week. The trigger day has the following defined values: 7: every day 0: Sunday 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("everyday", 7))

class SpTimeOfDay(TextualConvention, OctetString):
    description = 'A time-of-day specification in hours:minutes:seconds. field octets contents range ----- ------ -------- ----- 1 1 hour 0..23 2 1 minutes 0..59 3 1 seconds 0..59'
    status = 'current'
    displayHint = '1d:1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class Unsigned16(TextualConvention, Unsigned32):
    description = 'An unsigned 16 bit integer.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cadSpMgtGroupTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1), )
if mibBuilder.loadTexts: cadSpMgtGroupTable.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupTable.setDescription('Each entry in this table defines a C4 Upstream Spectrum Management group.')
cadSpMgtGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1), ).setIndexNames((0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtGroupIndex"))
if mibBuilder.loadTexts: cadSpMgtGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupEntry.setDescription('A set of C4 Upstream Spectrum Management group information. Entries in the cadSpMgtGroupTable are created and deleted using the cadSpMgtGroupRowStatus object.')
cadSpMgtGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40)))
if mibBuilder.loadTexts: cadSpMgtGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupIndex.setDescription('The index used to identify the Upstream Spectrum Group.')
cadSpMgtGroupSamplePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtGroupSamplePeriod.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupSamplePeriod.setDescription('The time (in seconds) between samples used for the degradation and the improvement triggers.')
cadSpMgtGroupHopPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(1200)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtGroupHopPeriod.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupHopPeriod.setDescription('The minimum period of time (in seconds) that must pass between successive state transitions.')
cadSpMgtGroupCodeword = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 32768)).clone(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtGroupCodeword.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupCodeword.setDescription('The minimum number of codewords that must have been transmitted on the upstream channel before the degradation and improvement triggers are considered to be valid.')
cadSpMgtGroupRetryPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 604800)).clone(86400)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtGroupRetryPeriod.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupRetryPeriod.setDescription('This object specifies the minimum wait time (in seconds) before the retry is attempted. The retry-period timer controls how quickly the state machine is allowed to retry when transition failure occurred.')
cadSpMgtGroupEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtGroupEnabled.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupEnabled.setDescription('This object allows for the optional enabling and disabling of a spectrum group.')
cadSpMgtGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtGroupRowStatus.setDescription('The status of this conceptual row. To create a row in this table, set this object to createAndGo(4). Support of the values includes createAndGo(4) and destroy(6)')
cadSpMgtStateTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2), )
if mibBuilder.loadTexts: cadSpMgtStateTable.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateTable.setDescription('Each entry in this table defines a state used for C4 Upstream Spectrum Management.')
cadSpMgtStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1), ).setIndexNames((0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtGroupIndex"), (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtStateIndex"))
if mibBuilder.loadTexts: cadSpMgtStateEntry.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateEntry.setDescription('A set of Upstream Spectrum Management state information. Entries in the cadSpMgtStateTable are created and deleted using the cadSpMgtStateRowStatus object.')
cadSpMgtStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: cadSpMgtStateIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateIndex.setDescription('The index used to identify the state in C4 Upstream Spectrum Management.')
cadSpMgtStateFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000000, 85000000), ))).setUnits('hertz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtStateFrequency.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateFrequency.setDescription('The center of the frequency band for the upstream channel associated with this state.')
cadSpMgtStateWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6400000))).setUnits('hertz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtStateWidth.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateWidth.setDescription('The bandwidth for the upstream channel associated with this state.')
cadSpMgtStateModulationProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtStateModulationProfile.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateModulationProfile.setDescription('An entry identical to the docsIfModIndex in the docsIfCmtsModulationTable that describes the upstream channel associated with this state.')
cadSpMgtStateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtStateRowStatus.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateRowStatus.setDescription('The status of this conceptual row. To create a row in this table, set this object to createAndGo(4). Support of the values includes createAndGo(4) and destroy(6)')
cadSpMgtTriggerTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3), )
if mibBuilder.loadTexts: cadSpMgtTriggerTable.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerTable.setDescription('Each entry in this table defines a trigger for C4 Upstream Spectrum Management')
cadSpMgtTriggerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1), ).setIndexNames((0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtTriggerIndex"))
if mibBuilder.loadTexts: cadSpMgtTriggerEntry.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerEntry.setDescription('A set of Upstream Spectrum Management trigger information. Entries in the cadSpMgtTriggerTable are created and deleted using the cadSpMgtTriggerRowStatus object.')
cadSpMgtTriggerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: cadSpMgtTriggerIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerIndex.setDescription('The trigger index used to identify the trigger for each state transition.')
cadSpMgtTriggerType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 2), SpTriggerType().clone('degradation')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerType.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerType.setDescription('The trigger type.')
cadSpMgtTriggerDay = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 3), SpTriggerDay()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerDay.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerDay.setDescription('The trigger day is to specify the reoccurrence of the TOD trigger for a week. The trigger day has the following defined values: 0: Sunday 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Everyday ')
cadSpMgtTriggerTOD = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 4), SpTimeOfDay().clone(hexValue="000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerTOD.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerTOD.setDescription('Time of day to transition to next state, in HH:MM:SS format')
cadSpMgtTriggerPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 604800))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerPeriod.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerPeriod.setDescription('The amount of time that should be loaded into a timer, in seconds, once the state machine has transitioned into the associated current state. When the timer expires, the transition to next state defined in the state machine is executed. This value is an integer between 1 and 604,800 (which covers a period of a week). This object is applicable for trigger type of periodic(2)')
cadSpMgtTriggerThres1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('0.001 percentage').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerThres1.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerThres1.setDescription('This object is applicable for trigger type of degradation (3) and improvement (4). For degradation trigger, this is the maximum acceptable percentage of FEC errors (uncorrectable plus correctable). For improvement trigger, this is the minimum acceptable percentage of FEC errors (uncorrectable plus correctable)')
cadSpMgtTriggerThres2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('0.001 percentage').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerThres2.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerThres2.setDescription('This object is applicable for trigger type of degradation (3) and improvement (4). For degradation trigger, this is the maximum acceptable percentage of uncorrectable FEC errors. For improvement trigger, this is the minimum acceptable percentage of uncorrectable FEC errors.')
cadSpMgtTriggerThres3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 8), TenthdB().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(1000)).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerThres3.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerThres3.setDescription('This object is applicable for trigger type of degradation (3) and improvement (4). For degradation trigger, this is the minimum acceptable Signal/Noise ratio (in dB). For improvement trigger, this is the maximum acceptable Signal/Noise ratio (in dB). ')
cadSpMgtTriggerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTriggerRowStatus.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTriggerRowStatus.setDescription('The status of this conceptual row. To create a row in this table, set this object to createAndGo(4). Support of the values includes createAndGo(4) and destroy(6)')
cadSpMgtStateTransTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4), )
if mibBuilder.loadTexts: cadSpMgtStateTransTable.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateTransTable.setDescription('Each entry in this table defines the state machine in C4 Upstream Spectrum Management.')
cadSpMgtStateTransEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4, 1), ).setIndexNames((0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtGroupIndex"), (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtStateIndex"), (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtTriggerIndex"))
if mibBuilder.loadTexts: cadSpMgtStateTransEntry.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateTransEntry.setDescription('')
cadSpMgtTransNextState = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtTransNextState.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtTransNextState.setDescription('The index used to identify the next state to which the state machine may transition to as a result of this trigger.')
cadSpMgtStateTransRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSpMgtStateTransRowStatus.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtStateTransRowStatus.setDescription('The status of this conceptual row. To create a row in this table, set this object to createAndGo(4). Support of the values includes createAndGo(4) and destroy(6)')
cadSpMgtRequestUpChannelIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestUpChannelIfIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestUpChannelIfIndex.setDescription('IfIndex of the upstream channel.')
cadSpMgtRequestTriggerIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestTriggerIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestTriggerIndex.setDescription('The trigger index used to identify the trigger. A value of 0 indicates no trigger is attempted.')
cadSpMgtRequestNextState = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestNextState.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestNextState.setDescription('The index used to identify the next state to which the state machine may transition to.')
cadSpMgtRequestSNR = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 4), TenthdB()).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestSNR.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestSNR.setDescription('This object is the measured Signal/Noise ratio (in dB) for the upstream channel. This object is applicable when the value in cadSpMgtRequestTriggerIndex defines the trigger of type degradation or improvement.')
cadSpMgtRequestUFecError = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('0.001 percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestUFecError.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestUFecError.setDescription('This object is the measured percentage of uncorrectable FEC errors for the upstream channel. This object is applicable when the value in cadSpMgtRequestTriggerIndex defines the trigger of type degradation or improvement.')
cadSpMgtRequestFecError = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('0.001 percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestFecError.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestFecError.setDescription('This object is the measured percentage of FEC errors (uncorrectable plus correctable) for the upstream channel. This object is applicable when the value in cadSpMgtRequestTriggerIndex defines the trigger of type degradation or improvement.')
cadSpMgtRequestCommit = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 2, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSpMgtRequestCommit.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtRequestCommit.setDescription('The command to execute the request when set to true(1). The following are reasons for rejecting an SNMP SET to this object: - An operation is commited for a non-existing upstream channel ID or the corresponding ifOperStatus is down(2). - An operation is committed but cadSpMgtRequestNextState is not an existing state index in cadSpMgtStateEntry. - An operation is committed but the value in cadSpMgtRequestTriggerIndex is non-zero and not an existing trigger index in cadSpMgtTriggerEntry. Reading this object always returns false(2).')
cadSpMgtHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5), )
if mibBuilder.loadTexts: cadSpMgtHistoryTable.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryTable.setDescription('Table of state transition history.')
cadSpMgtHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1), ).setIndexNames((0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtHistoryUpChannelIfIndex"), (0, "CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtHistoryTime"))
if mibBuilder.loadTexts: cadSpMgtHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryEntry.setDescription('Entry of state transition history.')
cadSpMgtHistoryUpChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadSpMgtHistoryUpChannelIfIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryUpChannelIfIndex.setDescription('IfIndex of the upstream channel.')
cadSpMgtHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 2), DateAndTime())
if mibBuilder.loadTexts: cadSpMgtHistoryTime.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryTime.setDescription('The value of this object is the actual clock time when this entry was created.')
cadSpMgtHistoryTriggerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryTriggerIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryTriggerIndex.setDescription('The trigger index used to identify the trigger for state transition. A value of 0 indicates a manual trigger.')
cadSpMgtHistoryFromStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryFromStateIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryFromStateIndex.setDescription('The index used to identify the current state.')
cadSpMgtHistoryNextStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryNextStateIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryNextStateIndex.setDescription('The index used to identify the next state to which the state machine may transition to.')
cadSpMgtHistoryResultStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryResultStateIndex.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryResultStateIndex.setDescription('The index used to identify the result state to which the state machine has transitioned to. For a successful state transition request, the value of this object is the same as cadSpMgtHistoryNextState.')
cadSpMgtHistorySNR = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 7), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistorySNR.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistorySNR.setDescription('This object is the measured Signal/Noise ratio (in dB) for the upstream channel. This object is applicable when the value in cadSpMgtHistoryTriggerIndex defines the trigger of type degradation or improvement.')
cadSpMgtHistoryUFecError = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('0.001 percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryUFecError.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryUFecError.setDescription('This object is the measured percentage of uncorrectable FEC errors for the upstream channel. This object is applicable when the value in cadSpMgtHistoryTriggerIndex defines the trigger of type degradation or improvement.')
cadSpMgtHistoryFecError = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setUnits('0.001 percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryFecError.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryFecError.setDescription('This object is the measured percentage of FEC errors (uncorrectable plus correctable) for the upstream channel. This object is applicable when the value in cadSpMgtHistoryTriggerIndex defines the trigger of type degradation or improvement.')
cadSpMgtHistorySpareCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistorySpareCardId.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistorySpareCardId.setDescription(' The cardId of the spare CAM. The value of 0 indicates the CAM is not spared at the time the request is received.')
cadSpMgtHistoryText = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryText.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryText.setDescription('This object provides a human-readable description of the entry, including all relevant context.')
cadSpMgtHistoryGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryGroupId.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryGroupId.setDescription('The Upstream Spectrum Group index associated with the upstream channel.')
cadSpMgtHistoryStateChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 13), Unsigned16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistoryStateChangeCount.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistoryStateChangeCount.setDescription('Provides the count of state changes in the history entry. This object will always increase. It is 16 bits, once it is at 0xffff, the counter will roll over and start from beginning.')
cadSpMgtHistorySysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 5, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtHistorySysUpTime.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtHistorySysUpTime.setDescription('Provides the system up time in the history entry. This object will always increase.')
cadSpMgtUpChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6), )
if mibBuilder.loadTexts: cadSpMgtUpChannelTable.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtUpChannelTable.setDescription('This table describes Upstream Frequency Agility attributes of attached upstream channels.')
cadSpMgtUpChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6, 1), )
cadIfUpstreamChannelEntry.registerAugmentions(("CADANT-CMTS-SPECTRUM-MGMT-MIB", "cadSpMgtUpChannelEntry"))
cadSpMgtUpChannelEntry.setIndexNames(*cadIfUpstreamChannelEntry.getIndexNames())
if mibBuilder.loadTexts: cadSpMgtUpChannelEntry.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtUpChannelEntry.setDescription('The List of Upstream Frequency Agility attributes associated with an upstream channel.')
cadSpMgtUpChannelCurrState = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtUpChannelCurrState.setReference('C4 CMTS Upstream Frequency Agility')
if mibBuilder.loadTexts: cadSpMgtUpChannelCurrState.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtUpChannelCurrState.setDescription('The current state as a result of the upstream spectrum group state transition. This object is only applicable if upstream spectrum management is enabled for this upstream channel.')
cadSpMgtUpChannelStateTransTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 4, 2, 1, 6, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSpMgtUpChannelStateTransTime.setStatus('current')
if mibBuilder.loadTexts: cadSpMgtUpChannelStateTransTime.setDescription('The value of this object is the actual clock time when the current state information in cadIfUpChannelSpGroupCurrState is most recently updated.')
mibBuilder.exportSymbols("CADANT-CMTS-SPECTRUM-MGMT-MIB", cadSpMgtUpChannelEntry=cadSpMgtUpChannelEntry, cadSpMgtMib=cadSpMgtMib, cadSpMgtGroupHopPeriod=cadSpMgtGroupHopPeriod, cadSpMgtStateRowStatus=cadSpMgtStateRowStatus, cadSpMgtTriggerType=cadSpMgtTriggerType, cadSpMgtHistoryNextStateIndex=cadSpMgtHistoryNextStateIndex, cadSpMgtHistoryGroupId=cadSpMgtHistoryGroupId, cadSpMgtTriggerEntry=cadSpMgtTriggerEntry, cadSpMgtStateModulationProfile=cadSpMgtStateModulationProfile, cadSpMgtStateIndex=cadSpMgtStateIndex, cadSpMgtGroupIndex=cadSpMgtGroupIndex, cadSpMgtRequestFecError=cadSpMgtRequestFecError, cadSpMgtHistoryUpChannelIfIndex=cadSpMgtHistoryUpChannelIfIndex, cadSpMgtHistoryEntry=cadSpMgtHistoryEntry, cadSpMgtConformance=cadSpMgtConformance, cadSpMgtStateTransRowStatus=cadSpMgtStateTransRowStatus, SpTriggerDay=SpTriggerDay, cadSpMgtUpChannelCurrState=cadSpMgtUpChannelCurrState, cadSpMgtHistorySpareCardId=cadSpMgtHistorySpareCardId, cadSpMgtGroupTable=cadSpMgtGroupTable, PYSNMP_MODULE_ID=cadSpMgtMib, cadSpMgtTransNextState=cadSpMgtTransNextState, cadSpMgtHistorySNR=cadSpMgtHistorySNR, SpTimeOfDay=SpTimeOfDay, cadSpMgtStateEntry=cadSpMgtStateEntry, cadSpMgtRequestUFecError=cadSpMgtRequestUFecError, cadSpMgtHistoryFromStateIndex=cadSpMgtHistoryFromStateIndex, cadSpMgtGroup=cadSpMgtGroup, cadSpMgtGroupCodeword=cadSpMgtGroupCodeword, cadSpMgtTriggerIndex=cadSpMgtTriggerIndex, cadSpMgtHistoryUFecError=cadSpMgtHistoryUFecError, cadSpMgtRequestCommit=cadSpMgtRequestCommit, cadSpMgtHistoryStateChangeCount=cadSpMgtHistoryStateChangeCount, cadSpMgtHistorySysUpTime=cadSpMgtHistorySysUpTime, cadSpMgtGroupEnabled=cadSpMgtGroupEnabled, cadSpMgtTriggerRowStatus=cadSpMgtTriggerRowStatus, SpTriggerType=SpTriggerType, cadSpMgtRequestUpChannelIfIndex=cadSpMgtRequestUpChannelIfIndex, cadSpMgtTriggerTOD=cadSpMgtTriggerTOD, cadSpMgtRequests=cadSpMgtRequests, cadSpMgtGroupSamplePeriod=cadSpMgtGroupSamplePeriod, cadSpMgtHistoryTime=cadSpMgtHistoryTime, cadSpMgtUpChannelTable=cadSpMgtUpChannelTable, cadSpMgtTriggerTable=cadSpMgtTriggerTable, cadSpMgtRequestTriggerIndex=cadSpMgtRequestTriggerIndex, cadSpMgtStateFrequency=cadSpMgtStateFrequency, cadSpMgtTriggerDay=cadSpMgtTriggerDay, cadSpMgtHistoryResultStateIndex=cadSpMgtHistoryResultStateIndex, cadSpMgtRequestNextState=cadSpMgtRequestNextState, cadSpMgtGroupEntry=cadSpMgtGroupEntry, cadSpMgtStateTransEntry=cadSpMgtStateTransEntry, Unsigned16=Unsigned16, cadSpMgtGroupRetryPeriod=cadSpMgtGroupRetryPeriod, cadSpMgtStateTable=cadSpMgtStateTable, cadSpMgtHistoryFecError=cadSpMgtHistoryFecError, cadSpMgtHistoryText=cadSpMgtHistoryText, cadSpMgtTriggerPeriod=cadSpMgtTriggerPeriod, cadSpMgtUpChannelStateTransTime=cadSpMgtUpChannelStateTransTime, cadSpMgtObjects=cadSpMgtObjects, cadSpMgtTriggerThres1=cadSpMgtTriggerThres1, cadSpMgtGroupRowStatus=cadSpMgtGroupRowStatus, cadSpMgtHistoryTable=cadSpMgtHistoryTable, cadSpMgtStateWidth=cadSpMgtStateWidth, cadSpMgtStateTransTable=cadSpMgtStateTransTable, cadSpMgtNotifications=cadSpMgtNotifications, cadSpMgtTriggerThres2=cadSpMgtTriggerThres2, cadSpMgtHistoryTriggerIndex=cadSpMgtHistoryTriggerIndex, cadSpMgtTriggerThres3=cadSpMgtTriggerThres3, cadSpMgtRequestSNR=cadSpMgtRequestSNR)
