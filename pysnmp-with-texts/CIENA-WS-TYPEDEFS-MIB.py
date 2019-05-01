#
# PySNMP MIB module CIENA-WS-TYPEDEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-WS-TYPEDEFS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, Counter32, Bits, Unsigned32, Integer32, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "Counter32", "Bits", "Unsigned32", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cienaWsTypedefsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 13))
cienaWsTypedefsMIB.setRevisions(('2016-12-12 00:00', '2016-03-03 00:00', '2015-02-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cienaWsTypedefsMIB.setRevisionsDescriptions(('Waveserver Rel 1.3 revised. Updated enum definition for typedef connector-type-desc-enum to remove the parentheses in some enum names. Added typedef decimal-3-dig. Added typedef decimal-2-dig-small. Added range statement for decimal-1-dig, decimal-2-dig and decimal-3-dig', "Waveserver Rel 1.1 revised. Modified range of typedef 'tx-power-lvl'.", 'Initial version.',))
if mibBuilder.loadTexts: cienaWsTypedefsMIB.setLastUpdated('201612120000Z')
if mibBuilder.loadTexts: cienaWsTypedefsMIB.setOrganization('Ciena Corporation')
if mibBuilder.loadTexts: cienaWsTypedefsMIB.setContactInfo('Web URL: http://www.ciena.com/ Postal: 7035 Ridge Road Hanover, Maryland 21076 U.S.A. Phone: +1 800-921-1144 Fax: +1 410-694-5750')
if mibBuilder.loadTexts: cienaWsTypedefsMIB.setDescription("This YANG module defines Ciena's commonly used typedefs")
class ChannelsNumber(TextualConvention, Unsigned32):
    description = 'Channel number common type, channel range are defined from 0 to 4.'
    status = 'current'

class ConnectorTypeDescEnum(TextualConvention, Integer32):
    description = "Human readable description of Vendor's connector type byte value. Reference SFF-8024, table 4-3"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("unknownorunspecified", 0), ("sc", 1), ("fibrechannelstyle1copperconnector", 2), ("fibrechannelstyle2copperconnector", 3), ("bnc", 4), ("fibrechannelcoaxheaders", 5), ("fiberjack", 6), ("lc", 7), ("mtrj", 8), ("mu", 9), ("sg", 10), ("opticalpigtail", 11), ("mpo1x12", 12), ("mpo2x16", 13), ("hssdcii", 32), ("copperpigtail", 33), ("rj45", 34), ("noseparableconnector", 35), ("mxc2x16", 36))

class Decimal1Dig(TextualConvention, Integer32):
    description = 'Decimal value up to 1 digits.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483640, 2147483640)

class Decimal2Dig(TextualConvention, Integer32):
    description = 'Decimal value up to 2 digits.'
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483600, 2147483600)

class Decimal2DigSmall(TextualConvention, Integer32):
    description = 'Decimal value up to 2 digits.'
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-3000000, 3000000)

class Decimal3Dig(TextualConvention, Integer32):
    description = 'Decimal value up to 3 digits.'
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483000, 2147483000)

class DescriptionString(TextualConvention, OctetString):
    description = 'String type for description used in Ciena defined modules. Max length of 128 characters, plus null. '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class EnabledDisabledEnum(TextualConvention, Integer32):
    description = 'Enabled and Disabled enum toggle used in Ciena defined modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class EnabledDisabledNaEnum(TextualConvention, Integer32):
    description = 'Enabled, Disabled, and not-applicable enum used in Ciena defined modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("na", 2))

class EnhancedOptsEnum(TextualConvention, Integer32):
    description = 'None'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("yes", 1), ("no", 2))

class LicenseStatusEnum(TextualConvention, Integer32):
    description = 'None'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notcompliant", 0), ("compliant", 1))

class LineModuleTypeBits(TextualConvention, Bits):
    description = 'None'
    status = 'current'
    namedValues = NamedValues(("wl3eline", 0))

class LineSysEnum(TextualConvention, Integer32):
    description = 'None'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("coloured", 0), ("colourless", 1), ("contentionless", 2), ("cscolored", 3), ("cscolorless", 4))

class MacString(TextualConvention, OctetString):
    description = 'MAC address string.'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class ModemChannel(TextualConvention, Integer32):
    description = 'Modem channel value.'
    status = 'current'

class ModemFrequency(TextualConvention, Integer32):
    description = 'Modem frequency, in GHz.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483640, 2147483640)

class ModuleTypeBits(TextualConvention, Bits):
    description = 'None'
    status = 'current'
    namedValues = NamedValues(("integrated", 0), ("fieldreplaceable", 1))

class ModuleTypeEnum(TextualConvention, Integer32):
    description = 'None'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("integrated", 1), ("fieldreplaceable", 2))

class NameString(TextualConvention, OctetString):
    description = 'String type for object names used in Ciena defined modules. It must be a non empty string that is at most 32 characters long.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class OnOffEnum(TextualConvention, Integer32):
    description = 'Off and On enum toggle used in Ciena defined modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class PortId(TextualConvention, Unsigned32):
    description = 'Logical port id that uniquely identifies a port.'
    status = 'current'

class PortName(TextualConvention, OctetString):
    description = 'None'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class PtpId(TextualConvention, Unsigned32):
    description = 'PTP ID'
    status = 'current'

class RecoverLinkDispersionType(TextualConvention, Integer32):
    description = 'Value for Fast Receiver Recovery Path Link Dispersion. 100000 means Auto.'
    status = 'current'

class ServiceDomainIdx(TextualConvention, Unsigned32):
    description = 'Service Domain Index'
    status = 'current'

class ServiceIdx(TextualConvention, Unsigned32):
    description = 'Service Index'
    status = 'current'

class StringMaxl128(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 128 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class StringMaxl16(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 16 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class StringMaxl254(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 254 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class StringMaxl256(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 256 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class StringMaxl32(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 32 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class StringMaxl50(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 50 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '50a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 50)

class StringMaxl64(TextualConvention, OctetString):
    description = 'Standard string that has a max length of 64 characters. Can be used for various nodes that may require string of this length.'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class StringSci(TextualConvention, OctetString):
    description = 'String in Scientific Notation format with a max length of 32 characters.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TxPowerLvl(TextualConvention, Integer32):
    description = 'Modem Tx Power Level.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483640, 2147483640)

class UpDownEnum(TextualConvention, Integer32):
    description = 'Down and Up enum toggle used in Ciena defined modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("down", 0), ("up", 1))

class VendorDateString(TextualConvention, OctetString):
    description = "Vendor's manufacturing date code string, 8 characters long."
    status = 'current'
    displayHint = '9a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 9)

class VendorRvString(TextualConvention, OctetString):
    description = 'Vendor Revision String. 2 characters.'
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class WlSpacing(TextualConvention, Integer32):
    description = 'Wave length spacing, 50 GHz or 100 GHz. Flexigrid currently not supported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("fixed50ghz", 0), ("fixed100ghz", 1), ("fixed200ghz", 2), ("flexgrid", 3))

class XcvrId(TextualConvention, Unsigned32):
    description = 'XCVR ID'
    status = 'current'

class XcvrMode(TextualConvention, Integer32):
    description = 'None'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("blank", 0), ("mode10gig", 1), ("mode40gig", 2), ("mode100gig", 3), ("mode16qam", 4), ("modeqpsk", 5), ("mode8qam", 6))

class XcvrType(TextualConvention, Integer32):
    description = 'None'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notavailable", 0), ("unsupported", 1), ("qsfpplus", 2), ("qsfp28", 3), ("wavelogic3extreme", 4))

class YesNoEnum(TextualConvention, Integer32):
    description = 'No and Yes enum toggle used in Ciena defined modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class YesNoNaEnum(TextualConvention, Integer32):
    description = 'No and Yes enum toggle used in Ciena defined modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("no", 0), ("yes", 1), ("na", 2))

mibBuilder.exportSymbols("CIENA-WS-TYPEDEFS-MIB", UpDownEnum=UpDownEnum, ModemFrequency=ModemFrequency, Decimal3Dig=Decimal3Dig, XcvrMode=XcvrMode, NameString=NameString, VendorDateString=VendorDateString, LineModuleTypeBits=LineModuleTypeBits, StringMaxl254=StringMaxl254, Decimal2DigSmall=Decimal2DigSmall, StringMaxl256=StringMaxl256, RecoverLinkDispersionType=RecoverLinkDispersionType, DescriptionString=DescriptionString, ServiceIdx=ServiceIdx, YesNoNaEnum=YesNoNaEnum, TxPowerLvl=TxPowerLvl, Decimal2Dig=Decimal2Dig, EnabledDisabledEnum=EnabledDisabledEnum, EnabledDisabledNaEnum=EnabledDisabledNaEnum, ModuleTypeBits=ModuleTypeBits, OnOffEnum=OnOffEnum, StringMaxl32=StringMaxl32, StringMaxl50=StringMaxl50, StringSci=StringSci, PtpId=PtpId, ModemChannel=ModemChannel, PortId=PortId, ServiceDomainIdx=ServiceDomainIdx, VendorRvString=VendorRvString, XcvrId=XcvrId, ConnectorTypeDescEnum=ConnectorTypeDescEnum, cienaWsTypedefsMIB=cienaWsTypedefsMIB, ChannelsNumber=ChannelsNumber, PortName=PortName, ModuleTypeEnum=ModuleTypeEnum, WlSpacing=WlSpacing, StringMaxl16=StringMaxl16, LineSysEnum=LineSysEnum, Decimal1Dig=Decimal1Dig, XcvrType=XcvrType, LicenseStatusEnum=LicenseStatusEnum, EnhancedOptsEnum=EnhancedOptsEnum, PYSNMP_MODULE_ID=cienaWsTypedefsMIB, MacString=MacString, YesNoEnum=YesNoEnum, StringMaxl64=StringMaxl64, StringMaxl128=StringMaxl128)
