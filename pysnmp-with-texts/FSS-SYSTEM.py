#
# PySNMP MIB module FSS-SYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSS-SYSTEM
# Produced by pysmi-0.3.4 at Wed May  1 13:16:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fssCommon, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Integer32, Gauge32, Unsigned32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter32, TimeTicks, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter32", "TimeTicks", "IpAddress", "ModuleIdentity")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
fssSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100))
fssSystem.setRevisions(('2016-06-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fssSystem.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: fssSystem.setLastUpdated('201606200000Z')
if mibBuilder.loadTexts: fssSystem.setOrganization('Fujitsu Network Communications, Inc.')
if mibBuilder.loadTexts: fssSystem.setContactInfo('Fujitsu Technical Assistance Center (FTAC), 1-800-USE-FTAC (1-800-873-3822)')
if mibBuilder.loadTexts: fssSystem.setDescription('This module contains definitions for System Management.')
class String(TextualConvention, OctetString):
    description = 'xs:string'
    status = 'current'
    displayHint = '1t'

class ADT_value(TextualConvention, Integer32):
    description = 'Deactivation time for alarms in seconds'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("adt-zero", 0), ("adt-ten", 1))

class RestartLevel(TextualConvention, Integer32):
    description = 'initialization level for restart'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("cold", 0), ("warm", 1))

class AAT_value(TextualConvention, Integer32):
    description = 'Activation time for alarms in seconds'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("aat-zero", 0), ("aat-twoPointFive", 1))

system = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1))
systemVendor = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 1), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemVendor.setStatus('current')
if mibBuilder.loadTexts: systemVendor.setDescription("Vendor Name - 'Fujitsu Limited' ")
systemName = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 2), String().subtype(subtypeSpec=ValueSizeConstraint(7, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemName.setStatus('current')
if mibBuilder.loadTexts: systemName.setDescription('Admin assigned name to this system')
systemLocation = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 3), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemLocation.setStatus('current')
if mibBuilder.loadTexts: systemLocation.setDescription('location information')
systemContact = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 4), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemContact.setStatus('current')
if mibBuilder.loadTexts: systemContact.setDescription('Contact information for this system')
systemNeType = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 5), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemNeType.setStatus('current')
if mibBuilder.loadTexts: systemNeType.setDescription('Network Element type')
systemSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 6), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: systemSoftwareVersion.setDescription('Software version of the system')
systemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTime.setStatus('current')
if mibBuilder.loadTexts: systemUpTime.setDescription('Number of TimeTicks ( in one hudredth of second) since last time System was initilized')
systemAutoP = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAutoP.setStatus('current')
if mibBuilder.loadTexts: systemAutoP.setDescription('Global flag to turn ON/OFF auto provisioning on the system')
systemAAT = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 9), AAT_value()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemAAT.setStatus('current')
if mibBuilder.loadTexts: systemAAT.setDescription('Alarm Activation Time')
systemADT = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 10), ADT_value()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemADT.setStatus('current')
if mibBuilder.loadTexts: systemADT.setDescription('Alarm De-activation Time')
systemClock = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 11))
systemClockTimezone_name = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 11, 1), String()).setLabel("systemClockTimezone-name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemClockTimezone_name.setStatus('current')
if mibBuilder.loadTexts: systemClockTimezone_name.setDescription("The TZ database name to use for the system, such as 'Europe/Stockholm'.")
systemNtp = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtp.setStatus('current')
if mibBuilder.loadTexts: systemNtp.setDescription('Configuration of the NTP client.')
systemNtpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtpEnabled.setStatus('current')
if mibBuilder.loadTexts: systemNtpEnabled.setDescription("Indicates that the system should attempt to synchronize the system clock with an NTP server from the 'ntp/server' list.")
systemNtp_cfg = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 14), TruthValue()).setLabel("systemNtp-cfg").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtp_cfg.setStatus('current')
if mibBuilder.loadTexts: systemNtp_cfg.setDescription('Configuration parameters for NTP.')
systemNtp_cfgNtp_enabled = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 1, 15), TruthValue()).setLabel("systemNtp-cfgNtp-enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemNtp_cfgNtp_enabled.setStatus('current')
if mibBuilder.loadTexts: systemNtp_cfgNtp_enabled.setDescription('Controls whether NTP is enabled or disabled on this device.')
system_state = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2)).setLabel("system-state")
system_stateClock = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2, 1)).setLabel("system-stateClock")
system_stateClockDatetime = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 100, 2, 1, 1), String()).setLabel("system-stateClockDatetime").setMaxAccess("readonly")
if mibBuilder.loadTexts: system_stateClockDatetime.setStatus('current')
if mibBuilder.loadTexts: system_stateClockDatetime.setDescription('The current system date and time.')
mibBuilder.exportSymbols("FSS-SYSTEM", fssSystem=fssSystem, systemNtp=systemNtp, String=String, system=system, PYSNMP_MODULE_ID=fssSystem, systemName=systemName, systemAutoP=systemAutoP, systemSoftwareVersion=systemSoftwareVersion, systemNtpEnabled=systemNtpEnabled, systemClock=systemClock, AAT_value=AAT_value, systemADT=systemADT, systemNeType=systemNeType, systemClockTimezone_name=systemClockTimezone_name, RestartLevel=RestartLevel, systemAAT=systemAAT, systemVendor=systemVendor, systemLocation=systemLocation, systemNtp_cfgNtp_enabled=systemNtp_cfgNtp_enabled, ADT_value=ADT_value, systemUpTime=systemUpTime, system_state=system_state, systemContact=systemContact, system_stateClock=system_stateClock, system_stateClockDatetime=system_stateClockDatetime, systemNtp_cfg=systemNtp_cfg)
