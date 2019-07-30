#
# PySNMP MIB module SYMME1T1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMME1T1
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:59 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, iso, Counter32, MibIdentifier, ModuleIdentity, TimeTicks, IpAddress, Integer32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "iso", "Counter32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "IpAddress", "Integer32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
EnableValue, symmPhysicalSignal, ONVALUETYPE = mibBuilder.importSymbols("SYMM-COMMON-SMI", "EnableValue", "symmPhysicalSignal", "ONVALUETYPE")
symmE1T1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2))
symmE1T1.setRevisions(('2011-03-18 17:06',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmE1T1.setRevisionsDescriptions(('Revision 1.0',))
if mibBuilder.loadTexts: symmE1T1.setLastUpdated('201103181705Z')
if mibBuilder.loadTexts: symmE1T1.setOrganization('Symmetricom.')
if mibBuilder.loadTexts: symmE1T1.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com')
if mibBuilder.loadTexts: symmE1T1.setDescription('This is the Symmetricom Common MIB for the configuration and status monitoring of E1/T1 ports in the system. It is one of the MIBs under the symmPhysicalSignal node. This MIB is organized into two main nodes: input and output. Each node is further has two tables, one for status and one for configuration.')
class TP5000PQLVALUE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

class INPUTE1T1FRAMETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("freq1544khz", 1), ("freq2048khz", 2), ("ccs", 3), ("cas", 4), ("d4", 5), ("esf", 6))

class PORTSTATETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class OUTPUTE1T1FRAMETYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("freq1544khz", 1), ("freq2048khz", 2), ("ccs", 3), ("cas", 4), ("d4", 5), ("esf", 6))

class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

e1T1input = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1))
inputE1T1Status = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1))
e1T1InputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1), )
if mibBuilder.loadTexts: e1T1InputStatusTable.setStatus('current')
if mibBuilder.loadTexts: e1T1InputStatusTable.setDescription('This table contains status information for each E1/T1 input port.')
e1T1InputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1InputStatusIndex"))
if mibBuilder.loadTexts: e1T1InputStatusEntry.setStatus('current')
if mibBuilder.loadTexts: e1T1InputStatusEntry.setDescription('An entry of the e1T1InputStatusTable. Table index is ifIndex (port/interface index). Each entry has three parameters for the specified E1/T1 input port: 1. Port enable status (enable or disable) 2. Current value of the incoming SSM 3. Port status ')
e1T1InputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1InputStatusIndex.setStatus('current')
if mibBuilder.loadTexts: e1T1InputStatusIndex.setDescription('Local index of the E1/T1 input status table.')
e1T1InputPQLCurValueV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 3), TP5000PQLVALUE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1InputPQLCurValueV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputPQLCurValueV1.setDescription('The current PQL value of the incoming SSM on this input port.')
e1T1InputPortStatusV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1InputPortStatusV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputPortStatusV1.setDescription('The port status of the specified input E1/T1 input port. Possible values are On (1) and Off (2). When the input port state is enabled, port status becomes on. When input port state is disabled, input port status is off.')
e1T1InputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2))
e1T1InputConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: e1T1InputConfigTable.setStatus('current')
if mibBuilder.loadTexts: e1T1InputConfigTable.setDescription('Configuration Table for E1/T1 input ports')
e1T1InputConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1InputConfigIndex"))
if mibBuilder.loadTexts: e1T1InputConfigEntry.setStatus('current')
if mibBuilder.loadTexts: e1T1InputConfigEntry.setDescription('An entry of the E1/T1 input configuration table. Table index is ifIndex (port/interface). Each entry has the following configuration parameters for the selected input port: 1. Frame type 2. CRC enable state 3. SSM enable state 4. SSM bit position 5. Default PQL value that can be used to override the input SSM value 6. Zero suppression state ')
e1T1InputConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1InputConfigIndex.setStatus('current')
if mibBuilder.loadTexts: e1T1InputConfigIndex.setDescription('Local index of the E1/T1 input configuration table.')
e1T1InputFrameTypeV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 2), INPUTE1T1FRAMETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputFrameTypeV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputFrameTypeV1.setDescription('E1 or T1 input frame type. Supported frame types include: 1. Freq1544khz (1) 2. Freq2048khz (2) 3. CCS (3) 4. CAS (4) 5. D4 (5) 6. ESF (6) Default frame type is 2048 kHz ')
e1T1InputCRCStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 3), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputCRCStateV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputCRCStateV1.setDescription('CRC enable state can be Enable (1) or Disable (2). Disabling the CRC means the CRC in the SSM is not used.')
e1T1InputSSMStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputSSMStateV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputSSMStateV1.setDescription("SSM enable state. It can be Enable (1) or Disable (2). Disabling the SSM means the incoming SSM is not used, and the forced (default) PQL value for this input port will be used during the reference selection. SSM is supported for only three frame types: EFS, CAS with CRC4, and CCA with CRC4. SSM should not be enabled for other frame types. If SSM is enabled for an input port, but the frame type does not support SSM or is not sending a valid SSM, then this input will be disqualified and the input PQL will be set to 'invalid.' The system will go into holdover no other qualified reference is available. ")
e1T1InputSSMBitV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputSSMBitV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputSSMBitV1.setDescription('SSM Bit position. The value range is 4 to 8. This parameter is only used for frame types ESF, CCS, or CAS.')
e1T1InputPQLValueV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 6), TP5000PQLVALUE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1InputPQLValueV1.setStatus('current')
if mibBuilder.loadTexts: e1T1InputPQLValueV1.setDescription('The user assigned PQL value for the specified input. This PQL value is used when the SSM state is disabled. The range for the user assigned PQL value is 1 to 9. ')
eT1InputZeroSupprV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 1, 2, 1, 1, 7), ONVALUETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eT1InputZeroSupprV1.setStatus('current')
if mibBuilder.loadTexts: eT1InputZeroSupprV1.setDescription('The number indicates whether zero suppression (ZS) on the input port is enabled or disabled. Valid values are On (1) or Off (2). ')
e1T1Output = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2))
e1T1OutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1))
e1T1OutputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1), )
if mibBuilder.loadTexts: e1T1OutputStatusTable.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputStatusTable.setDescription('This table contains status information for each E1/T1 output port.')
e1T1OutputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1OutputStatusIndex"))
if mibBuilder.loadTexts: e1T1OutputStatusEntry.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputStatusEntry.setDescription('An entry of the e1T1OutputStatusTable. Table index is ifIndex (port/interface index). Each entry has two parameters for the specified E1/T1 input port: 1. Port status 2. Outgoing SSM value ')
e1T1OutputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1OutputStatusIndex.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputStatusIndex.setDescription('Local index of the E1/T1 output status table.')
e1T1OutputPortStatusV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1OutputPortStatusV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputPortStatusV1.setDescription("The port status of the specified E1/T1 output port. Possible values are On (1) and Off (2). 'On' means there is signal on the port. For E1/T1 output port it means the system is in normal tracking mode. 'Off' means there is no signal on the port. For E1/T1 output port it means the output is squelched during some clock states.")
e1T1OutputPQLValueV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 1, 1, 1, 3), TP5000PQLVALUE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1T1OutputPQLValueV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputPQLValueV1.setDescription('The PQL value for the specified E1/T1 output port.')
e1T1OutputConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2))
e1T1OutputConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1), )
if mibBuilder.loadTexts: e1T1OutputConfigTable.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputConfigTable.setDescription('This table contains configuration information for each E1/T1 output port.')
e1T1OutputConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMME1T1", "e1T1OutputConfigIndex"))
if mibBuilder.loadTexts: e1T1OutputConfigEntry.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputConfigEntry.setDescription('An entry of the e1T1OutputConfigTable. Table index is ifIndex (port/interface index). Each entry has the configuration parameters for the specified E1/T1 output port: 1. Port enable state 2. Frame type 3. CRC enable state 4. SSM enable state 5. SSM bit position 6. Zero suppression on/off state 7. Output port cable length ')
e1T1OutputConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: e1T1OutputConfigIndex.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputConfigIndex.setDescription('Local index of the E1/T1 output configuration table.')
e1T1OutputStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 2), PORTSTATETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputStateV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputStateV1.setDescription('E1/T1 output port enable state. Its value can be Enable (1) or Disable (2). Disabling an output port means no output is generated for that port.')
e1T1OutputFrameTypeV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 3), OUTPUTE1T1FRAMETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputFrameTypeV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputFrameTypeV1.setDescription('E1 or T1 output frame type. Supported frame types include: 1. Freq1544khz (1) 2. Freq2048khz (2) 3. CCS (3) 4. CAS (4) 5. D4 (5) 6. ESF (6) Default frame type is 2048 kHz. ')
e1T1OutputCRCStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 4), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputCRCStateV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputCRCStateV1.setDescription('CRC enable state can be Enable (1) or Disable (2). Disabling the CRC means that no CRC is generated for the SSM.')
e1T1OutputSSMStateV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 5), EnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputSSMStateV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputSSMStateV1.setDescription('SSM enable state. It can be Enable (1) or Disable (2). Disabling the output SSM means that no SSM is generated for the specified output port.')
e1T1OutputSSMBitV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputSSMBitV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputSSMBitV1.setDescription('SSM Bit position. The value range is 4 to 8. This parameter is only used for frame types ESF, CCS, or CAS.')
e1T1OutputZeroSupprV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 7), ONVALUETYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputZeroSupprV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputZeroSupprV1.setDescription('The number indicates whether zero suppression (ZS) on the output port is enabled or disabled. Valid values are On (1) or Off (2). ')
e1T1OutputLengthV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1T1OutputLengthV1.setStatus('current')
if mibBuilder.loadTexts: e1T1OutputLengthV1.setDescription('Output cable length. ')
e1T1Conformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3))
if mibBuilder.loadTexts: e1T1Conformance.setStatus('current')
if mibBuilder.loadTexts: e1T1Conformance.setDescription('This node contains conformance statement for the symmE1T1 MIB module. ')
e1T1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 1))
e1T1BasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 1, 1)).setObjects(("SYMME1T1", "e1T1InputStatusGroup"), ("SYMME1T1", "e11T1InputConfigGroup"), ("SYMME1T1", "e11T1OutputStatusGroup"), ("SYMME1T1", "e11T1OutputConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e1T1BasicCompliance = e1T1BasicCompliance.setStatus('current')
if mibBuilder.loadTexts: e1T1BasicCompliance.setDescription('The compliance statement for SNMP entities which have E1/T1 input/output.')
e1T1UocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2))
e1T1InputStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 1)).setObjects(("SYMME1T1", "e1T1InputPortStatusV1"), ("SYMME1T1", "e1T1InputPQLCurValueV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e1T1InputStatusGroup = e1T1InputStatusGroup.setStatus('current')
if mibBuilder.loadTexts: e1T1InputStatusGroup.setDescription('A collection of objects providing information applicable to E1/T1 input status group.')
e11T1InputConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 2)).setObjects(("SYMME1T1", "e1T1InputFrameTypeV1"), ("SYMME1T1", "e1T1InputCRCStateV1"), ("SYMME1T1", "e1T1InputSSMStateV1"), ("SYMME1T1", "e1T1InputSSMBitV1"), ("SYMME1T1", "e1T1InputPQLValueV1"), ("SYMME1T1", "eT1InputZeroSupprV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e11T1InputConfigGroup = e11T1InputConfigGroup.setStatus('current')
if mibBuilder.loadTexts: e11T1InputConfigGroup.setDescription('A collection of objects providing information applicable to E1/T1 input configuration group.')
e11T1OutputStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 3)).setObjects(("SYMME1T1", "e1T1OutputPortStatusV1"), ("SYMME1T1", "e1T1OutputPQLValueV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e11T1OutputStatusGroup = e11T1OutputStatusGroup.setStatus('current')
if mibBuilder.loadTexts: e11T1OutputStatusGroup.setDescription('A collection of objects providing information applicable to E1/T1 output status group.')
e11T1OutputConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 2, 3, 2, 4)).setObjects(("SYMME1T1", "e1T1OutputStateV1"), ("SYMME1T1", "e1T1OutputFrameTypeV1"), ("SYMME1T1", "e1T1OutputCRCStateV1"), ("SYMME1T1", "e1T1OutputSSMStateV1"), ("SYMME1T1", "e1T1OutputSSMBitV1"), ("SYMME1T1", "e1T1OutputLengthV1"), ("SYMME1T1", "e1T1OutputZeroSupprV1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    e11T1OutputConfigGroup = e11T1OutputConfigGroup.setStatus('current')
if mibBuilder.loadTexts: e11T1OutputConfigGroup.setDescription('A collection of objects providing information applicable to E1/T1 output configuration group.')
mibBuilder.exportSymbols("SYMME1T1", TLocalTimeOffset=TLocalTimeOffset, TLatAndLon=TLatAndLon, e1T1InputCRCStateV1=e1T1InputCRCStateV1, e1T1InputFrameTypeV1=e1T1InputFrameTypeV1, e11T1InputConfigGroup=e11T1InputConfigGroup, e1T1InputConfigTable=e1T1InputConfigTable, e11T1OutputConfigGroup=e11T1OutputConfigGroup, e1T1InputStatusGroup=e1T1InputStatusGroup, e1T1OutputStatusEntry=e1T1OutputStatusEntry, OUTPUTE1T1FRAMETYPE=OUTPUTE1T1FRAMETYPE, e1T1OutputLengthV1=e1T1OutputLengthV1, e1T1InputSSMStateV1=e1T1InputSSMStateV1, e1T1BasicCompliance=e1T1BasicCompliance, e1T1OutputStatusIndex=e1T1OutputStatusIndex, e1T1OutputStateV1=e1T1OutputStateV1, e1T1InputPortStatusV1=e1T1InputPortStatusV1, e1T1Output=e1T1Output, e1T1UocGroups=e1T1UocGroups, e1T1InputPQLValueV1=e1T1InputPQLValueV1, TSsm=TSsm, e1T1OutputStatus=e1T1OutputStatus, e11T1OutputStatusGroup=e11T1OutputStatusGroup, e1T1InputStatusIndex=e1T1InputStatusIndex, e1T1OutputFrameTypeV1=e1T1OutputFrameTypeV1, e1T1OutputStatusTable=e1T1OutputStatusTable, PYSNMP_MODULE_ID=symmE1T1, PORTSTATETYPE=PORTSTATETYPE, e1T1OutputSSMStateV1=e1T1OutputSSMStateV1, e1T1OutputPortStatusV1=e1T1OutputPortStatusV1, symmE1T1=symmE1T1, e1T1InputConfigEntry=e1T1InputConfigEntry, e1T1input=e1T1input, e1T1OutputPQLValueV1=e1T1OutputPQLValueV1, e1T1Compliances=e1T1Compliances, TAntHeight=TAntHeight, DateAndTime=DateAndTime, e1T1InputStatusEntry=e1T1InputStatusEntry, INPUTE1T1FRAMETYPE=INPUTE1T1FRAMETYPE, TP5000PQLVALUE=TP5000PQLVALUE, e1T1InputPQLCurValueV1=e1T1InputPQLCurValueV1, e1T1InputStatusTable=e1T1InputStatusTable, e1T1OutputConfigEntry=e1T1OutputConfigEntry, e1T1InputSSMBitV1=e1T1InputSSMBitV1, inputE1T1Status=inputE1T1Status, e1T1InputConfigIndex=e1T1InputConfigIndex, e1T1OutputCRCStateV1=e1T1OutputCRCStateV1, e1T1OutputConfigTable=e1T1OutputConfigTable, e1T1OutputZeroSupprV1=e1T1OutputZeroSupprV1, e1T1OutputConfig=e1T1OutputConfig, e1T1OutputConfigIndex=e1T1OutputConfigIndex, eT1InputZeroSupprV1=eT1InputZeroSupprV1, e1T1OutputSSMBitV1=e1T1OutputSSMBitV1, e1T1InputConfig=e1T1InputConfig, e1T1Conformance=e1T1Conformance)
