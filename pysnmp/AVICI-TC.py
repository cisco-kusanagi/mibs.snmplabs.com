#
# PySNMP MIB module AVICI-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
aviciTypes, = mibBuilder.importSymbols("AVICI-SMI", "aviciTypes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, Integer32, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "Integer32", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aviciTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474, 4, 1))
aviciTextualConventions.setRevisions(('0009-07-14 00:00', '1970-01-01 00:00',))
if mibBuilder.loadTexts: aviciTextualConventions.setLastUpdated('000907140000Z')
if mibBuilder.loadTexts: aviciTextualConventions.setOrganization('Avici Systems, Inc.')
class AviciSystemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("tsr", 1))

class AviciInventoryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("server", 1), ("bayController", 2), ("module", 3), ("serverAccessModule", 4))

class AviciHighAvailabilityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class AviciVoltageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("bayInput", 2), ("controllerInput", 3), ("voltageRail", 4))

class AviciBayType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 14)

class AviciSlotType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 40)

class AviciSerialNumberType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 13)

class AviciPartNumberType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 9)

class AviciProductIdType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 26)

class AviciProductRevisionType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 3)

class AviciRevisionType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 6)

class AviciTrapDescrType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class AviciUnitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("fan", 1), ("module", 2), ("breaker", 3), ("bayController", 4), ("voltageRail", 5), ("server", 6), ("multipleFailures", 7))

class AviciLedValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("on", 1), ("off", 2), ("red", 3), ("redblink", 4), ("amber", 5), ("amberblink", 6), ("green", 7), ("greenblink", 8))

class AviciPlatformIndexType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class AviciFabricLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("plusX", 0), ("minusX", 1), ("plusY", 2), ("minusY", 3), ("plusZ", 4), ("minusZ", 5), ("plusE", 6), ("minusE", 7))

class AviciModuleName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

mibBuilder.exportSymbols("AVICI-TC", AviciSystemType=AviciSystemType, AviciFabricLinkType=AviciFabricLinkType, AviciInventoryType=AviciInventoryType, AviciModuleName=AviciModuleName, AviciLedValue=AviciLedValue, AviciVoltageType=AviciVoltageType, PYSNMP_MODULE_ID=aviciTextualConventions, AviciUnitType=AviciUnitType, AviciHighAvailabilityType=AviciHighAvailabilityType, AviciSerialNumberType=AviciSerialNumberType, AviciPartNumberType=AviciPartNumberType, AviciTrapDescrType=AviciTrapDescrType, AviciProductRevisionType=AviciProductRevisionType, AviciProductIdType=AviciProductIdType, AviciPlatformIndexType=AviciPlatformIndexType, aviciTextualConventions=aviciTextualConventions, AviciBayType=AviciBayType, AviciSlotType=AviciSlotType, AviciRevisionType=AviciRevisionType)
