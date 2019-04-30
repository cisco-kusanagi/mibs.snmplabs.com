#
# PySNMP MIB module SPRING-TIDE-NETWORKS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SPRING-TIDE-NETWORKS-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Counter32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier, Counter64, IpAddress, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "iso", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stnMibModules, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnMibModules")
stnTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 5, 1))
if mibBuilder.loadTexts: stnTextualConventions.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnTextualConventions.setOrganization('Spring Tide Networks, Inc.')
class NSAPAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class CountryCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class StnHardwareModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("unknown", 1), ("empty", 2), ("cpm", 3), ("tsm", 4), ("swfm-5G", 5), ("rim", 6), ("fcc", 7), ("fan", 8), ("powersupply", 9), ("midplane", 10), ("e100BT-4", 11), ("e100BT-FX-4", 12), ("e100BT-8", 13), ("e100BT-FX-8", 14), ("atmOC3-SMF-4", 15), ("atmOC3-MMF-4", 16), ("atmOC12-SMF-1", 17), ("atmOC12-MMF-1", 18), ("posOC12-SMF-2", 19), ("atmDS3-12", 20), ("tsm2", 21), ("sfx-5G", 22), ("gigE-1-e100BT-4", 23), ("gigE-1-e100BT-FX-4", 24), ("fan2", 25))

class StnHardwareSubModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("empty", 2), ("encryption", 3))

class StnModuleAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("booting", 4), ("testing", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnModuleOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("booting", 4), ("testing", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnEngineAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("detected", 4), ("configured", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnEngineOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("not-present", 2), ("down", 3), ("detected", 4), ("configured", 5), ("up-standalone", 6), ("up-standby", 7), ("up-primary", 8))

class StnLedStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("on", 3), ("green", 4), ("yellow", 5), ("red", 6), ("orange", 7), ("blink-green", 8), ("blink-yellow", 9), ("blink-red", 10), ("blink-orange", 11))

class StnPowerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("present", 2), ("not-present", 3))

class StnBatteryStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("low", 3))

class StnFlashStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("general-failure", 1), ("ok", 2), ("not-present", 3), ("full", 4), ("cannot-write", 5))

class StnResourceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("low-memory", 3), ("no-semaphores-available", 4), ("no-buffers-available", 5), ("no-sockets-available", 6))

class StnUserFailureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("authentication-failure", 1), ("authorization-failure", 2), ("resource-failure", 3))

class StnConfigFailureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("access-failure", 1), ("unexpected-change", 2))

class StnDomainMapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mapip", 1), ("mapatm", 2))

mibBuilder.exportSymbols("SPRING-TIDE-NETWORKS-TC", stnTextualConventions=stnTextualConventions, StnPowerStatus=StnPowerStatus, StnFlashStatus=StnFlashStatus, StnResourceStatus=StnResourceStatus, StnConfigFailureType=StnConfigFailureType, StnBatteryStatus=StnBatteryStatus, StnDomainMapType=StnDomainMapType, StnHardwareModuleType=StnHardwareModuleType, PYSNMP_MODULE_ID=stnTextualConventions, StnEngineAdminStatus=StnEngineAdminStatus, StnLedStatus=StnLedStatus, StnModuleAdminStatus=StnModuleAdminStatus, StnHardwareSubModuleType=StnHardwareSubModuleType, StnModuleOperStatus=StnModuleOperStatus, CountryCode=CountryCode, StnEngineOperStatus=StnEngineOperStatus, StnUserFailureType=StnUserFailureType, NSAPAddress=NSAPAddress)
