#
# PySNMP MIB module SYMMGNSS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMGNSS
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:02 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, iso, ObjectIdentity, Integer32, NotificationType, Counter32, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, ModuleIdentity, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ObjectIdentity", "Integer32", "NotificationType", "Counter32", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "ModuleIdentity", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
GNSSReceiverMode, GNSSPositionMode, symmPhysicalSignal, GNSSHealthStatus, YESVALUETYPE = mibBuilder.importSymbols("SYMM-COMMON-SMI", "GNSSReceiverMode", "GNSSPositionMode", "symmPhysicalSignal", "GNSSHealthStatus", "YESVALUETYPE")
symmGNSS = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1))
if mibBuilder.loadTexts: symmGNSS.setLastUpdated('201808230822Z')
if mibBuilder.loadTexts: symmGNSS.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmGNSS.setContactInfo(' Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com ')
if mibBuilder.loadTexts: symmGNSS.setDescription('This is the Symmetricom common MIB for GNSS/GPS. This MIB has two main nodes: gnssStatus and gnssConfig. The gnssStatus node has a port status table, a satellite table, and a scalar for GNSS current position mode. The gnssConfig node has a configuration table, position setting table, and a present position table.')
class GNSSCURPOSITIONMODE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("surveying", 1), ("positionHold", 2), ("manual", 3))

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

gnssStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1))
gnssPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1), )
if mibBuilder.loadTexts: gnssPortStatusTable.setStatus('current')
if mibBuilder.loadTexts: gnssPortStatusTable.setDescription('GNSS port status table. It contains port name and the current GNSS receiver mode for the specified port.')
gnssPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssPortStatusIndex"))
if mibBuilder.loadTexts: gnssPortStatusEntry.setStatus('current')
if mibBuilder.loadTexts: gnssPortStatusEntry.setDescription('An entry of the GNSS port status table. Table index is ifIndex.')
gnssPortStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: gnssPortStatusIndex.setStatus('current')
if mibBuilder.loadTexts: gnssPortStatusIndex.setDescription('Local index of the GNSS port status table.')
gnssPortStatusPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPortStatusPortName.setStatus('current')
if mibBuilder.loadTexts: gnssPortStatusPortName.setDescription('The name of the specified GNSS port. In TP5000 system there can be one or two GNSS ports. One of them is always called GPS, and the additional one (if present) is either called GPS or GNSS. A port called GNSS indicates that it may be non-GPS or a multi-mode GNSS receiver port.')
gnssPortCurrentGNSS = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 3), YESVALUETYPE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPortCurrentGNSS.setStatus('current')
if mibBuilder.loadTexts: gnssPortCurrentGNSS.setDescription('This value indicates whether the specified GNSS port is used. Its value is Yes (1) or No (2). If it is No, the port is considered absent in the system.')
gnssPortCurrentPosMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 4), GNSSCURPOSITIONMODE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPortCurrentPosMode.setStatus('current')
if mibBuilder.loadTexts: gnssPortCurrentPosMode.setDescription('Current position mode of the GNSS receiver. It can be surveying (1), position hold (2), or manual (3)')
gnssSatTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2), )
if mibBuilder.loadTexts: gnssSatTable.setStatus('current')
if mibBuilder.loadTexts: gnssSatTable.setDescription('GNSS satellite table. This table lists information about the satellites being tracked by the GNSS receiver.')
gnssSatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssSatIndex"))
if mibBuilder.loadTexts: gnssSatEntry.setStatus('current')
if mibBuilder.loadTexts: gnssSatEntry.setDescription('An entry of the GNSS satellite tracking table. Table index is local index gnssSatIndex.')
gnssSatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 125))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatIndex.setStatus('current')
if mibBuilder.loadTexts: gnssSatIndex.setDescription('This is the local index of the table of the GNSS satellites GPS, GLONASS, Galileo being tracked.')
gnssSatNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatNum.setStatus('current')
if mibBuilder.loadTexts: gnssSatNum.setDescription('GNSS satellite number. This is the identification number of the GNSS satellite being tracked. This information is obtained from the GNSS satellite ephemeris or almanac.')
gnssSatSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatSNR.setStatus('current')
if mibBuilder.loadTexts: gnssSatSNR.setDescription('Signal-to-Noise Ratio. This is the GNSS signal to noise ratio measured by the GNSS receiver.')
gnssSatHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 4), GNSSHealthStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatHealth.setStatus('current')
if mibBuilder.loadTexts: gnssSatHealth.setDescription('GNSS satellite health state. It can be healthy (1) or unhealthy (2). This data is obtained from the GNSS receiver.')
gnssSatAzimuth = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 360))).setUnits('degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatAzimuth.setStatus('current')
if mibBuilder.loadTexts: gnssSatAzimuth.setDescription('GNSS satellite azimuthal angle clockwise from true north. Range of the azimuth is 0 to 360 degrees.')
gnssSatElevation = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 360))).setUnits('degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatElevation.setStatus('current')
if mibBuilder.loadTexts: gnssSatElevation.setDescription('GNSS satellite elevation angle relative to the horizon. Range of the elevation angle is 0 to 90 degrees.')
gnssSatPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssSatPortName.setStatus('current')
if mibBuilder.loadTexts: gnssSatPortName.setDescription('The gnss port name. This is defined in gnssConfigTable.')
gnssPresentPosTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3), )
if mibBuilder.loadTexts: gnssPresentPosTable.setStatus('current')
if mibBuilder.loadTexts: gnssPresentPosTable.setDescription('Current position table. This table shows the position of the GNSS receiver antenna. In the automatic mode, the position is calculated by the GNSS receiver. In the manual mode, the position is the manually entered position in gnssPosSettingTable.')
gnssPresentPosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssPresentPosIndex"))
if mibBuilder.loadTexts: gnssPresentPosEntry.setStatus('current')
if mibBuilder.loadTexts: gnssPresentPosEntry.setDescription('An entry of the current position table. Table index is the ifIndex. ')
gnssPresentPosIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: gnssPresentPosIndex.setStatus('current')
if mibBuilder.loadTexts: gnssPresentPosIndex.setDescription('Local index that corresponds to the ifIndex. For TP5K there are up to two GNSS port entries.')
gnssPresentPosLat = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPresentPosLat.setStatus('current')
if mibBuilder.loadTexts: gnssPresentPosLat.setDescription('Latitude of the GNSS receiver antenna position for the specified GNSS port. Its format is Ndd:mm:ss.ss or Sdd:mm:ss.ss. ')
gnssPresentPosLong = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPresentPosLong.setStatus('current')
if mibBuilder.loadTexts: gnssPresentPosLong.setDescription('Longitude of the GNSS receiver antenna position for the specified GNSS port. Its format is Eddd:mm:ss.ss or Wddd:mm:ss.ss. ')
gnssPresentPosHeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssPresentPosHeight.setStatus('current')
if mibBuilder.loadTexts: gnssPresentPosHeight.setDescription('Altitude (height) in meters of the GNSS receiver antenna position for the specified GNSS port. Its format is +/-hhhh.h.')
gnssConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2))
gnssConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1), )
if mibBuilder.loadTexts: gnssConfigurationTable.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationTable.setDescription('The GNSS configuration table.')
gnssConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssConfigurationIndex"))
if mibBuilder.loadTexts: gnssConfigurationEntry.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationEntry.setDescription('An entry of the GNSS configuration table. Table index is ifIndex.')
gnssConfigurationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: gnssConfigurationIndex.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationIndex.setDescription('Local index of the GNSS port configuration table.')
gnssConfigurationPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gnssConfigurationPortName.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationPortName.setDescription('Name of the specified GNSS port. For TP5000 currently there are two names for a GNSS port: GPS or GNSS. Use the name on the equipment front panel.')
gnssConfigurationTrackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 3), GNSSReceiverMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationTrackMode.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationTrackMode.setDescription('GNSS receiver mode. This depends on the GNSS receiver. For the VCOM receiver, there are four modes: beidou (1), gps (2), priorityBeidou (4), which is automatic with GPS priority, and priorityGps (5) which is automatic with Beidou priority. For Ublox receiver, gnssGPS(17),gnssGlonass(18),gnssGPSGlonass(19),gnssGalileo(20), gnssGPSGalileo(21),gnssGlonassGalileo(22),gnssGPSGlonassGalileo(23), gnssBeidou(24), gnssBeidouGPS(25), gnssBeidouGlonass(26), gnssBeidouGlonassGPS(27),gnssBeidouGalileo(28), gnssBeidouGalileoGPS(29), gnssBeidouGalileoGlonass(30), gnssBeidouGalileoGlonassGPS(31) ')
gnssConfigurationPosMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 4), GNSSPositionMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationPosMode.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationPosMode.setDescription('GNSS receiver position survey mode. It can be either automatic (1) or manual (2). When the position survey mode is manual, the user must configure the position. ')
gnssConfigurationElevMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 45))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationElevMask.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationElevMask.setDescription('GNSS elevation mask. The range is 5 to 45 degrees. This value is actually the lower limit of the elevation mask. The upper limit is 90 degrees. If the elevation mask is set to 5 degrees, the elevation coverage is from 5 to 90 degrees. If the elevation mask is set to 30 degrees, the elevation coverage is from 30 to 90 degrees.')
gnssConfigurationCableDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationCableDelay.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationCableDelay.setDescription('GNSS antenna cable delay compensation in nanoseconds. Range is 0 to 999,999 nanoseconds. This value should be as close to the actual antenna cable delay as possible. Residual error will directly affect the time/phase accuracy.')
gnssConfigurationLeapSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssConfigurationLeapSeconds.setStatus('current')
if mibBuilder.loadTexts: gnssConfigurationLeapSeconds.setDescription('Leapseconds used for GLONASS only satellite to set user-provided value. Range 20-255. This leapseconds not applicable for GPS port. Note: zero (0) indicates NotApplicable')
gnssPosSettingTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2), )
if mibBuilder.loadTexts: gnssPosSettingTable.setStatus('current')
if mibBuilder.loadTexts: gnssPosSettingTable.setDescription('This table is used to manually set the GNSS receiver antenna position for the specified GNSS port.')
gnssPosSettingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMGNSS", "gnssPosSettingIndex"))
if mibBuilder.loadTexts: gnssPosSettingEntry.setStatus('current')
if mibBuilder.loadTexts: gnssPosSettingEntry.setDescription('An entry of the GNSS position setting table. Table index is ifIndex.')
gnssPosSettingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: gnssPosSettingIndex.setStatus('current')
if mibBuilder.loadTexts: gnssPosSettingIndex.setDescription('Local index that corresponds to the ifIndex. For TP5K there are up to two GNSS port entries.')
gnssPosSettingLat = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssPosSettingLat.setStatus('current')
if mibBuilder.loadTexts: gnssPosSettingLat.setDescription('Manual setting for the latitude of the GNSS receiver antenna for the specified GNSS port.')
gnssPosSettingLong = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssPosSettingLong.setStatus('current')
if mibBuilder.loadTexts: gnssPosSettingLong.setDescription('Manual setting for the longitude of the GNSS receiver antenna for the specified GNSS port.')
gnssPosSettingHeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gnssPosSettingHeight.setStatus('current')
if mibBuilder.loadTexts: gnssPosSettingHeight.setDescription('Manual setting for the height of the GNSS receiver antenna for the specified GNSS port.')
gnssConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3))
if mibBuilder.loadTexts: gnssConformance.setStatus('current')
if mibBuilder.loadTexts: gnssConformance.setDescription('This subtree contains conformance statements for the SYMMETRICOM-LED-MIB module. ')
gnssCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 1))
gnssBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 1, 1)).setObjects(("SYMMGNSS", "gnssStatusGroup"), ("SYMMGNSS", "gnssConfigGroup"), ("SYMMGNSS", "gnssSVGroup"), ("SYMMGNSS", "gnssConfigPosGroup"), ("SYMMGNSS", "gnssCurrentPosGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssBasicCompliance = gnssBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: gnssBasicCompliance.setDescription('The compliance statement for SNMP entities which have GNSS input.')
gnssUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2))
gnssStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 1)).setObjects(("SYMMGNSS", "gnssPortStatusPortName"), ("SYMMGNSS", "gnssPortCurrentGNSS"), ("SYMMGNSS", "gnssPortCurrentPosMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssStatusGroup = gnssStatusGroup.setStatus('current')
if mibBuilder.loadTexts: gnssStatusGroup.setDescription('A collection of objects providing information applicable to GNSS status group.')
gnssConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 2)).setObjects(("SYMMGNSS", "gnssConfigurationPortName"), ("SYMMGNSS", "gnssConfigurationTrackMode"), ("SYMMGNSS", "gnssConfigurationPosMode"), ("SYMMGNSS", "gnssConfigurationElevMask"), ("SYMMGNSS", "gnssConfigurationCableDelay"), ("SYMMGNSS", "gnssConfigurationLeapSeconds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssConfigGroup = gnssConfigGroup.setStatus('current')
if mibBuilder.loadTexts: gnssConfigGroup.setDescription('A collection of objects providing information applicable to GNSS configuration group.')
gnssSVGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 3)).setObjects(("SYMMGNSS", "gnssSatIndex"), ("SYMMGNSS", "gnssSatNum"), ("SYMMGNSS", "gnssSatSNR"), ("SYMMGNSS", "gnssSatHealth"), ("SYMMGNSS", "gnssSatAzimuth"), ("SYMMGNSS", "gnssSatElevation"), ("SYMMGNSS", "gnssSatPortName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssSVGroup = gnssSVGroup.setStatus('current')
if mibBuilder.loadTexts: gnssSVGroup.setDescription('A collection of objects providing information applicable to GNSS satellite positions group.')
gnssConfigPosGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 4)).setObjects(("SYMMGNSS", "gnssPosSettingLat"), ("SYMMGNSS", "gnssPosSettingLong"), ("SYMMGNSS", "gnssPosSettingHeight"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssConfigPosGroup = gnssConfigPosGroup.setStatus('current')
if mibBuilder.loadTexts: gnssConfigPosGroup.setDescription('A collection of objects providing information applicable to GNSS position configuration group.')
gnssCurrentPosGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 5)).setObjects(("SYMMGNSS", "gnssPresentPosLat"), ("SYMMGNSS", "gnssPresentPosLong"), ("SYMMGNSS", "gnssPresentPosHeight"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gnssCurrentPosGroup = gnssCurrentPosGroup.setStatus('current')
if mibBuilder.loadTexts: gnssCurrentPosGroup.setDescription('A collection of objects providing information applicable to GNSS current position group.')
mibBuilder.exportSymbols("SYMMGNSS", gnssSVGroup=gnssSVGroup, TAntHeight=TAntHeight, gnssPresentPosHeight=gnssPresentPosHeight, gnssConfigurationEntry=gnssConfigurationEntry, gnssSatElevation=gnssSatElevation, gnssPortStatusPortName=gnssPortStatusPortName, GNSSCURPOSITIONMODE=GNSSCURPOSITIONMODE, gnssConformance=gnssConformance, gnssSatSNR=gnssSatSNR, PYSNMP_MODULE_ID=symmGNSS, gnssPortStatusTable=gnssPortStatusTable, gnssPosSettingLat=gnssPosSettingLat, gnssConfigurationTrackMode=gnssConfigurationTrackMode, gnssStatusGroup=gnssStatusGroup, gnssSatEntry=gnssSatEntry, gnssUocGroups=gnssUocGroups, gnssPortStatusEntry=gnssPortStatusEntry, DateAndTime=DateAndTime, gnssSatPortName=gnssSatPortName, gnssConfigurationLeapSeconds=gnssConfigurationLeapSeconds, TLocalTimeOffset=TLocalTimeOffset, gnssPresentPosEntry=gnssPresentPosEntry, gnssPosSettingEntry=gnssPosSettingEntry, gnssPosSettingLong=gnssPosSettingLong, gnssSatAzimuth=gnssSatAzimuth, gnssPresentPosIndex=gnssPresentPosIndex, gnssConfigurationCableDelay=gnssConfigurationCableDelay, gnssConfigPosGroup=gnssConfigPosGroup, gnssSatTable=gnssSatTable, gnssPosSettingHeight=gnssPosSettingHeight, gnssPosSettingIndex=gnssPosSettingIndex, TSsm=TSsm, symmGNSS=symmGNSS, gnssSatIndex=gnssSatIndex, gnssConfigGroup=gnssConfigGroup, gnssConfigurationTable=gnssConfigurationTable, gnssSatNum=gnssSatNum, gnssConfigurationElevMask=gnssConfigurationElevMask, gnssBasicCompliance=gnssBasicCompliance, gnssCurrentPosGroup=gnssCurrentPosGroup, gnssPortStatusIndex=gnssPortStatusIndex, gnssPortCurrentPosMode=gnssPortCurrentPosMode, gnssConfigurationIndex=gnssConfigurationIndex, gnssConfigurationPosMode=gnssConfigurationPosMode, gnssPresentPosTable=gnssPresentPosTable, gnssPresentPosLat=gnssPresentPosLat, gnssConfig=gnssConfig, TLatAndLon=TLatAndLon, gnssSatHealth=gnssSatHealth, gnssStatus=gnssStatus, gnssPosSettingTable=gnssPosSettingTable, gnssConfigurationPortName=gnssConfigurationPortName, gnssCompliances=gnssCompliances, gnssPresentPosLong=gnssPresentPosLong, gnssPortCurrentGNSS=gnssPortCurrentGNSS)
