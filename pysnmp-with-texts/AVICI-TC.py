#
# PySNMP MIB module AVICI-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:32:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
aviciTypes, = mibBuilder.importSymbols("AVICI-SMI", "aviciTypes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, NotificationType, Counter32, iso, TimeTicks, IpAddress, Bits, ObjectIdentity, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "NotificationType", "Counter32", "iso", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aviciTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474, 4, 1))
aviciTextualConventions.setRevisions(('0009-07-14 00:00', '1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aviciTextualConventions.setRevisionsDescriptions(('Added new textual conventions for fabric.', 'Created MIB module.',))
if mibBuilder.loadTexts: aviciTextualConventions.setLastUpdated('000907140000Z')
if mibBuilder.loadTexts: aviciTextualConventions.setOrganization('Avici Systems, Inc.')
if mibBuilder.loadTexts: aviciTextualConventions.setContactInfo(' Avici Systems, Inc. 101 Billerica Avenue North Billerica, MA 01862-1256 (978) 964-2000 (978) 964-2100 (fax) snmp@avici.com')
if mibBuilder.loadTexts: aviciTextualConventions.setDescription('This MIB module specifies the types to be used in Avici MIBs.')
class AviciSystemType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("tsr", 1))

class AviciInventoryType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("server", 1), ("bayController", 2), ("module", 3), ("serverAccessModule", 4))

class AviciHighAvailabilityType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class AviciVoltageType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("bayInput", 2), ("controllerInput", 3), ("voltageRail", 4))

class AviciBayType(TextualConvention, Integer32):
    description = 'The maximum number of bays in an Avici Terabit Switch Router.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 14)

class AviciSlotType(TextualConvention, Integer32):
    description = 'The maximum number of slots in one Avici Bay.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 40)

class AviciSerialNumberType(DisplayString):
    description = 'The serial number of this object.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 13)

class AviciPartNumberType(DisplayString):
    description = 'The part number of this object.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 9)

class AviciProductIdType(DisplayString):
    description = 'The part number of this object.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 26)

class AviciProductRevisionType(DisplayString):
    description = 'The product revision number. The revision number is a string using the form ??? to identify the version.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 3)

class AviciRevisionType(DisplayString):
    description = 'The revision number of this object. The revision number is a string using the form MajorRevision.MinorRevision to identify the version.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 6)

class AviciTrapDescrType(DisplayString):
    description = 'A description of the trap that has occurred.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class AviciUnitType(TextualConvention, Integer32):
    description = 'The type of this object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("fan", 1), ("module", 2), ("breaker", 3), ("bayController", 4), ("voltageRail", 5), ("server", 6), ("multipleFailures", 7))

class AviciLedValue(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("on", 1), ("off", 2), ("red", 3), ("redblink", 4), ("amber", 5), ("amberblink", 6), ("green", 7), ("greenblink", 8))

class AviciPlatformIndexType(TextualConvention, Unsigned32):
    description = 'The index number of the platform described by this object. The high 16 bits represents the platform type as follows 1 Bay Controller 2 Module 3 Server The low 16 bits represents the ID of the platform. For a server, the ID is the server id. For a module, the ID is slot number + (bay number - 1) * 40. For a bay controller, the ID is slot number + (bay number - 1) * 2.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class AviciFabricLinkType(TextualConvention, Integer32):
    description = 'The names of the fabric links.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("plusX", 0), ("minusX", 1), ("plusY", 2), ("minusY", 3), ("plusZ", 4), ("minusZ", 5), ("plusE", 6), ("minusE", 7))

class AviciModuleName(DisplayString):
    description = 'The string name for a module in a given system. Examples: module 1/17 none '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

mibBuilder.exportSymbols("AVICI-TC", AviciPartNumberType=AviciPartNumberType, AviciHighAvailabilityType=AviciHighAvailabilityType, AviciProductRevisionType=AviciProductRevisionType, AviciSerialNumberType=AviciSerialNumberType, aviciTextualConventions=aviciTextualConventions, AviciPlatformIndexType=AviciPlatformIndexType, AviciFabricLinkType=AviciFabricLinkType, AviciSlotType=AviciSlotType, PYSNMP_MODULE_ID=aviciTextualConventions, AviciProductIdType=AviciProductIdType, AviciModuleName=AviciModuleName, AviciLedValue=AviciLedValue, AviciUnitType=AviciUnitType, AviciInventoryType=AviciInventoryType, AviciTrapDescrType=AviciTrapDescrType, AviciBayType=AviciBayType, AviciRevisionType=AviciRevisionType, AviciVoltageType=AviciVoltageType, AviciSystemType=AviciSystemType)
