#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-TC
# Produced by pysmi-0.3.4 at Wed May  1 13:54:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
regModule, = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "regModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, Unsigned32, NotificationType, IpAddress, TimeTicks, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "Unsigned32", "NotificationType", "IpAddress", "TimeTicks", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
multiFlexServerTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 2))
multiFlexServerTcModule.setRevisions(('2008-05-28 02:00', '2008-05-07 02:40', '2007-08-16 13:30', '2007-08-15 19:00', '2007-07-10 17:00', '2007-06-07 20:30', '2007-06-07 13:30', '2007-05-23 19:00', '2007-05-21 12:00', '2007-03-12 18:30', '2007-02-22 17:00', '2007-01-05 10:50', '2006-12-28 13:10', '2006-11-07 07:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: multiFlexServerTcModule.setRevisionsDescriptions(("Added a few additional enumerations to PresenceLedStates for managers that don't like setting values other than the enumerations already provided.", 'Added reset enumeration to PowerLedStates to provide a mnemonic for a settable action in addition to powering on/off', 'Reordered Revision to reverse chronological as some browsers choke, cleaned up some other simple nit-picky errors', 'Fixed up minor errors causing some managers grief (ommission or addition of commas in lists)', 'Adjusted PowerLedStates, FaultLedStates & PresenceLedStates type definitions to reflect the alert status', 'Added the IdromBinary16 to represent the asset tag, part number, and serial number fields within the IDROM fields.', 'Corrected maximum/nominal IDROM parameters and comments', 'Added new unify INTEGER type with enumerations for exceptions Reworked some of the other enumerations to make consistent, but avoid collisions with other enumerations by the OEMs', 'Added notApplicable (for cases where presence is known of the device to be absent), and identify (for certain device write requests) to LED states', "Created new Textual convention 'Power' for IDROM info on Maximim and Nominal Power data", 'Renamed MIB file and updated internal relevance to formal product name Multi-Flex Server', 'Added timeout enumeration to presence type along with additional documentation', "To support Switches, swiped several types that exist in various MIBs, but appear to be missing from the Net-SNMP distribution. Rather than copy someone else's interpretation of those MIBs (and then have to clean them up to be SMIv2 compliant), only the types were lifted (and documented). Added: JackType - Lifted from the MAU-MIB (RFC 3636) TimeFilter - Lifted from RMON2-MIB (RFC 2021) PortList - Lifted from Q-BRIDGE-MIB (RFC 2674) VlanIndex - Lifted from Q-BRIDGE-MIB (RFC 2674) EnabledStatus - Lifted from P-BRIDGE-MIB (RFC 2674) ", 'Added Presence type',))
if mibBuilder.loadTexts: multiFlexServerTcModule.setLastUpdated('200805280200Z')
if mibBuilder.loadTexts: multiFlexServerTcModule.setOrganization('Intel Corporation')
if mibBuilder.loadTexts: multiFlexServerTcModule.setContactInfo('Brian Kurle Intel Corporation JF5-2-C3 Tel: 503-712-5032 E-Mail: brianx.j.kurle@intel.com')
if mibBuilder.loadTexts: multiFlexServerTcModule.setDescription('Textual Conventions used within INTELCORPORATION-MULTI-FLEX-SERVER-*MIB')
class Index(TextualConvention, Unsigned32):
    description = 'Generial Index definition used in tables.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class INT32withException(TextualConvention, Integer32):
    description = "INTEGER type, but adds enumerations for exceptions when a positive integral value isn't available"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16))

class PowerLedStates(TextualConvention, Integer32):
    description = 'Power LED States type Status enumerations: off, standby, on Settable values: off - soft shutdown on - power up forcedOff - forced power down (unclean) hardReset - reset board '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -4, -1, 0, 1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("identify", -4), ("dataNotAvailable", -1), ("off", 0), ("standby", 1), ("on", 2), ("forcedOff", 3), ("hardReset", 4))

class FaultLedStates(TextualConvention, Integer32):
    description = 'Fault LED States type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -4, -1, 0, 1, 2))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("identify", -4), ("dataNotAvailable", -1), ("normal", 0), ("degraded", 1), ("fault", 2))

class PresenceLedStates(TextualConvention, Integer32):
    description = "The ENUM definition for the state of the presence LED with optional identify request. unknown - any thing that is outside of the following known types off - known to be present, but LED is off on - known to be present, and LED is on alwaysOn - Identification is turn on permanently dataNotAvailable - Device not responding/not available # - ID Notification is on, and the value is the number of seconds before the LED will be turned off. Four additional enumerations are provided for managers that don't like mixing enumerations with integral values, but provide a means of setting it."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -3, -1, 0, 15, 30, 60, 120))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("alwaysOn", -3), ("dataNotAvailable", -1), ("off", 0), ("fifteenSeconds", 15), ("thirtySeconds", 30), ("sixtySeconds", 60), ("twoMinutes", 120))

class FeatureSet(TextualConvention, Integer32):
    description = ' The ENUM definition for feature set support.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, 0, 1))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("unsupported", 0), ("supported", 1))

class Presence(TextualConvention, Integer32):
    description = 'The ENUM definition for presence of an object with optional identify request. unknown - any thing that is outside of the following known types absent - known not to be present (generally reported by the hardware) present - known to be present (ditto) identify - for devices the permit, this value may be written to command the device to identify itself (e.g., blink a LED) timedout - command information sent is timing out, thus not explicitly able to determine if present and not responding or actually absent (for cases where hardware is not present on devices to explicitly inform presence) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-32, -16, -4, -2, 0, 1))
    namedValues = NamedValues(("notApplicable", -32), ("unknown", -16), ("identify", -4), ("timedout", -2), ("absent", 0), ("present", 1))

class Power(TextualConvention, Integer32):
    description = 'Static power generation / consumption (in watts): <0 - Negative numbers indicate device consumes power (in watts) >0 - Positive numbers indicate device generates power (in watts) 0 - Device is passive (does not not consume or generate power) -1 - Power generation/consumption not known or specified'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0))
    namedValues = NamedValues(("unknown", -1), ("passive", 0))

class IdromBinary16(TextualConvention, OctetString):
    description = 'Means of displaying 16 byte binary fields within the IDROM as hexadecimal digits. Used for the Serial Number, Part Number, and Asset Tag fields. All above fields are only 16 bytes as per the IDROM spec.'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class JackType(TextualConvention, Integer32):
    description = 'Common enumeration values for repeater and interface MAU jack types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("other", 1), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14))

class TimeFilter(TextualConvention, TimeTicks):
    description = "To be used for the index to a table. Allows an application to download only those rows changed since a particular time. A row is considered changed if the value of any object in the row changes or if the row is created or deleted. When sysUpTime is equal to zero, this table shall be empty. One entry exists for each past value of sysUpTime, except that the whole table is purged should sysUpTime wrap. As this basic row is updated new conceptual rows are created (which still share the now updated object values with all other instances). The number of instances which are created is determined by the value of sysUpTime at which the basic row was last updated. One instance will exist for each value of sysUpTime at the last update time for the row. A new timeMark instance is created for each new sysUpTime value. Each new conceptual row will be associated with the timeMark instance which was created at the value of sysUpTime with which the conceptual row is to be associated. By definition all conceptual rows were updated at or after time zero and so at least one conceptual row (associated with timeMark.0) must exist for each underlying (basic) row. See the appendix for further discussion of this variable. Consider the following fooTable: fooTable ... INDEX { fooTimeMark, fooIndex } FooEntry { fooTimeMark TimeFilter fooIndex INTEGER, fooCounts Counter } Should there be two basic rows in this table (fooIndex == 1, fooIndex == 2) and row 1 was updated most recently at time 6, while row 2 was updated most recently at time 8, and both rows had been updated on several earlier occasions such that the current values were 5 and 9 respectively then the following fooCounts instances would exist. fooCounts.0.1 5 fooCounts.0.2 9 fooCounts.1.1 5 fooCounts.1.2 9 fooCounts.2.1 5 fooCounts.2.2 9 fooCounts.3.1 5 fooCounts.3.2 9 fooCounts.4.1 5 fooCounts.4.2 9 fooCounts.5.1 5 fooCounts.5.2 9 fooCounts.6.1 5 fooCounts.6.2 9 fooCounts.7.2 9 - note that row 1 doesn't exist for fooCounts.8.2 9 - times 7 and 8"
    status = 'current'

class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'."
    status = 'current'

class VlanIndex(TextualConvention, Unsigned32):
    description = 'A value used to index per-VLAN tables: values of 0 and 4095 are not permitted; if the value is between 1 and 4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged domain (see VlanId textual convention). If the value is greater than 4095 then it represents a VLAN with scope local to the particular agent, i.e. one without a global VLAN-ID assigned to it. Such VLANs are outside the scope of IEEE 802.1Q but it is convenient to be able to manage them in the same way using this MIB.'
    status = 'current'

class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-TC", TimeFilter=TimeFilter, VlanIndex=VlanIndex, multiFlexServerTcModule=multiFlexServerTcModule, INT32withException=INT32withException, PowerLedStates=PowerLedStates, Presence=Presence, PYSNMP_MODULE_ID=multiFlexServerTcModule, Power=Power, PortList=PortList, EnabledStatus=EnabledStatus, FeatureSet=FeatureSet, FaultLedStates=FaultLedStates, Index=Index, IdromBinary16=IdromBinary16, PresenceLedStates=PresenceLedStates, JackType=JackType)
