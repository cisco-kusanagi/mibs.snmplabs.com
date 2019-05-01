#
# PySNMP MIB module SPRING-TIDE-NETWORKS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPRING-TIDE-NETWORKS-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:10:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, TimeTicks, ObjectIdentity, Counter32, Integer32, Gauge32, ModuleIdentity, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "TimeTicks", "ObjectIdentity", "Counter32", "Integer32", "Gauge32", "ModuleIdentity", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnMibModules, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnMibModules")
stnTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 5, 1))
if mibBuilder.loadTexts: stnTextualConventions.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnTextualConventions.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnTextualConventions.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnTextualConventions.setDescription('This MIB module defines textual conventions used throughout the Spring Tide Networks enterprise MIBs.')
class NSAPAddress(TextualConvention, OctetString):
    description = 'Network Service Access Point Address'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class CountryCode(TextualConvention, OctetString):
    description = 'Represents a case-insensitive 2-letter country code taken from ISO-3166. Unrecognized countries are represented as empty string. '
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class StnHardwareModuleType(TextualConvention, Integer32):
    description = 'SpringTide Networks module types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("unknown", 1), ("empty", 2), ("cpm", 3), ("tsm", 4), ("swfm-5G", 5), ("rim", 6), ("fcc", 7), ("fan", 8), ("powersupply", 9), ("midplane", 10), ("e100BT-4", 11), ("e100BT-FX-4", 12), ("e100BT-8", 13), ("e100BT-FX-8", 14), ("atmOC3-SMF-4", 15), ("atmOC3-MMF-4", 16), ("atmOC12-SMF-1", 17), ("atmOC12-MMF-1", 18), ("posOC12-SMF-2", 19), ("atmDS3-12", 20), ("tsm2", 21), ("sfx-5G", 22), ("gigE-1-e100BT-4", 23), ("gigE-1-e100BT-FX-4", 24), ("fan2", 25))

class StnHardwareSubModuleType(TextualConvention, Integer32):
    description = 'SpringTide Networks sub-module types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("empty", 2), ("encryption", 3))

class StnModuleAdminStatus(TextualConvention, Integer32):
    description = 'Administrative status of a module.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("booting", 4), ("testing", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnModuleOperStatus(TextualConvention, Integer32):
    description = 'Operational status of a module.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("booting", 4), ("testing", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnEngineAdminStatus(TextualConvention, Integer32):
    description = 'Administrative status of an engine.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("detected", 4), ("configured", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnEngineOperStatus(TextualConvention, Integer32):
    description = 'Operational status of an engine.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("detected", 4), ("configured", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnLedStatus(TextualConvention, Integer32):
    description = 'Current LED status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("on", 3), ("green", 4), ("yellow", 5), ("red", 6), ("orange", 7), ("blink-green", 8), ("blink-yellow", 9), ("blink-red", 10), ("blink-orange", 11))

class StnPowerStatus(TextualConvention, Integer32):
    description = 'Status of the power supply.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("present", 2), ("not-present", 3))

class StnBatteryStatus(TextualConvention, Integer32):
    description = 'Status of the battery.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("low", 3))

class StnFlashStatus(TextualConvention, Integer32):
    description = 'Status of the flash.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("general-failure", 1), ("ok", 2), ("not-present", 3), ("full", 4), ("cannot-write", 5))

class StnResourceStatus(TextualConvention, Integer32):
    description = 'Status of the system resources.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("low-memory", 3), ("no-semaphores-available", 4), ("no-buffers-available", 5), ("no-sockets-available", 6))

class StnUserFailureType(TextualConvention, Integer32):
    description = 'Types of user failures.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("authentication-failure", 1), ("authorization-failure", 2), ("resource-failure", 3))

class StnConfigFailureType(TextualConvention, Integer32):
    description = 'Types of configuration failures.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("access-failure", 1), ("unexpected-change", 2))

class StnDomainMapType(TextualConvention, Integer32):
    description = 'SpringTide Networks Domain Map types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mapip", 1), ("mapatm", 2))

mibBuilder.exportSymbols("SPRING-TIDE-NETWORKS-TC", StnHardwareModuleType=StnHardwareModuleType, StnPowerStatus=StnPowerStatus, StnDomainMapType=StnDomainMapType, StnResourceStatus=StnResourceStatus, StnModuleOperStatus=StnModuleOperStatus, StnUserFailureType=StnUserFailureType, StnBatteryStatus=StnBatteryStatus, StnLedStatus=StnLedStatus, StnConfigFailureType=StnConfigFailureType, StnFlashStatus=StnFlashStatus, PYSNMP_MODULE_ID=stnTextualConventions, StnModuleAdminStatus=StnModuleAdminStatus, StnHardwareSubModuleType=StnHardwareSubModuleType, StnEngineOperStatus=StnEngineOperStatus, StnEngineAdminStatus=StnEngineAdminStatus, CountryCode=CountryCode, stnTextualConventions=stnTextualConventions, NSAPAddress=NSAPAddress)
