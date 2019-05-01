#
# PySNMP MIB module NBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, enterprises, NotificationType, Unsigned32, MibIdentifier, Counter64, Counter32, Gauge32, ModuleIdentity, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "enterprises", "NotificationType", "Unsigned32", "MibIdentifier", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 250))
if mibBuilder.loadTexts: nbsMib.setLastUpdated('201309170000Z')
if mibBuilder.loadTexts: nbsMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsMib.setDescription("Textual conventions for NBS mibs. Some informal NBS conventions used include the following: A DESCRIPTION specifying 'Persistent' indicates a user- configured attribute that can be stored in the Agent's non-volatile file system as a configuration file such as 'startup-config'. A DESCRIPTION specifying 'Impulse' indicates a user setting that the Agent will immediately attempt but will not store persistently. An object name containing 'Admin' indicates a setting requested by the user which may be overridden by the system. Admin objects should be updated in the Agent immediately, so a GET request immediately after the SET is accepted will be answered with a GET-RESPONSE indicating the new value. An object name containing 'Oper' indicates an attribute's actual state. An object name containing 'Caps' is a bitmask which refers to the capabilities of an entity to support corresponding entries in a specified feature table.")
nbs = ObjectIdentity((1, 3, 6, 1, 4, 1, 629))
if mibBuilder.loadTexts: nbs.setStatus('current')
if mibBuilder.loadTexts: nbs.setDescription('Root OID of NBS mibs')
class Unsigned16(TextualConvention, Integer32):
    description = 'Used to represent an unsigned two-octet integer'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Unsigned64(TextualConvention, Counter64):
    description = 'Used to represent an unsigned eight-octet integer'
    status = 'current'

class WritableU64(TextualConvention, OctetString):
    description = 'Used to represent an unsigned eight-octet integer which can be SET in SNMPv1'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NbsTcTemperature(TextualConvention, Integer32):
    description = 'Temperature in degrees Celsius. When writable, persistent. Not supported value: 0x80000000 (decimal -2147483648)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 1000)

class NbsTcMilliVolt(TextualConvention, Integer32):
    description = 'Voltage in units of milliVolts. When writable, persistent. Not supported value: -1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1000000)

class NbsTcMilliAmp(TextualConvention, Integer32):
    description = 'Amperage in units of milliAmps. When writable, persistent. Not supported value: -1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1000000)

class NbsTcMicroAmp(TextualConvention, Integer32):
    description = 'Electrical current in units of micro amperes. When writable, persistent. Not supported value: -1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class NbsTcMilliDb(TextualConvention, Integer32):
    description = 'Decibels in thousandths. When writable, persistent. The reserved value -1,000,000 indicates that the signal is blocked from passing through. Blocked value: -1000000 Not supported value: 0x80000000 (decimal -2147483648)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 100000)

class NbsTcMilliWatts(TextualConvention, Integer32):
    description = 'Electrical Power, in milliwatts. Not supported value: -1'
    status = 'current'

class NbsTcMHz(TextualConvention, Unsigned32):
    description = 'Frequency in units of MHz. When writable, persistent. Not supported value: 1'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NbsTcStatusSimple(TextualConvention, Integer32):
    description = 'Basic operating status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 1), ("bad", 2), ("good", 3), ("notInstalled", 4))

class NbsTcStatusLevel(TextualConvention, Integer32):
    description = 'Severity level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notSupported", 1), ("statusLowError", 2), ("statusLowWarning", 3), ("statusGood", 4), ("statusHighWarning", 5), ("statusHighError", 6))

class NbsTcPartIndex(TextualConvention, Unsigned32):
    description = 'Unique ID within scope of an ifIndex'
    status = 'current'

class NbsTcStagingCommit(TextualConvention, Integer32):
    description = 'Staging commit command'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 1), ("supported", 2), ("revertToCommitted", 3), ("apply", 4))

mibBuilder.exportSymbols("NBS-MIB", nbsMib=nbsMib, nbs=nbs, NbsTcMilliAmp=NbsTcMilliAmp, PYSNMP_MODULE_ID=nbsMib, NbsTcMilliVolt=NbsTcMilliVolt, NbsTcMicroAmp=NbsTcMicroAmp, NbsTcPartIndex=NbsTcPartIndex, Unsigned64=Unsigned64, NbsTcStatusSimple=NbsTcStatusSimple, NbsTcStagingCommit=NbsTcStagingCommit, NbsTcTemperature=NbsTcTemperature, NbsTcMilliDb=NbsTcMilliDb, WritableU64=WritableU64, NbsTcMilliWatts=NbsTcMilliWatts, NbsTcMHz=NbsTcMHz, NbsTcStatusLevel=NbsTcStatusLevel, Unsigned16=Unsigned16)
