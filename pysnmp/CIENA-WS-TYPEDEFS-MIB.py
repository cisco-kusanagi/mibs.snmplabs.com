#
# PySNMP MIB module CIENA-WS-TYPEDEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-WS-TYPEDEFS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, ObjectIdentity, Bits, Counter32, Gauge32, NotificationType, TimeTicks, Counter64, IpAddress, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "ObjectIdentity", "Bits", "Counter32", "Gauge32", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaWsTypedefsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 13))
cienaWsTypedefsMIB.setRevisions(('2016-12-12 00:00', '2016-03-03 00:00', '2015-02-25 00:00',))
if mibBuilder.loadTexts: cienaWsTypedefsMIB.setLastUpdated('201612120000Z')
if mibBuilder.loadTexts: cienaWsTypedefsMIB.setOrganization('Ciena Corporation')
class ChannelsNumber(TextualConvention, Unsigned32):
    status = 'current'

class ConnectorTypeDescEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("unknownorunspecified", 0), ("sc", 1), ("fibrechannelstyle1copperconnector", 2), ("fibrechannelstyle2copperconnector", 3), ("bnc", 4), ("fibrechannelcoaxheaders", 5), ("fiberjack", 6), ("lc", 7), ("mtrj", 8), ("mu", 9), ("sg", 10), ("opticalpigtail", 11), ("mpo1x12", 12), ("mpo2x16", 13), ("hssdcii", 32), ("copperpigtail", 33), ("rj45", 34), ("noseparableconnector", 35), ("mxc2x16", 36))

class Decimal1Dig(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483640, 2147483640)

class Decimal2Dig(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483600, 2147483600)

class Decimal2DigSmall(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-3000000, 3000000)

class Decimal3Dig(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483000, 2147483000)

class DescriptionString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class EnabledDisabledEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class EnabledDisabledNaEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("na", 2))

class EnhancedOptsEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("yes", 1), ("no", 2))

class LicenseStatusEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notcompliant", 0), ("compliant", 1))

class LineModuleTypeBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("wl3eline", 0))

class LineSysEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("coloured", 0), ("colourless", 1), ("contentionless", 2), ("cscolored", 3), ("cscolorless", 4))

class MacString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class ModemChannel(TextualConvention, Integer32):
    status = 'current'

class ModemFrequency(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483640, 2147483640)

class ModuleTypeBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("integrated", 0), ("fieldreplaceable", 1))

class ModuleTypeEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("integrated", 1), ("fieldreplaceable", 2))

class NameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class OnOffEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class PortId(TextualConvention, Unsigned32):
    status = 'current'

class PortName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class PtpId(TextualConvention, Unsigned32):
    status = 'current'

class RecoverLinkDispersionType(TextualConvention, Integer32):
    status = 'current'

class ServiceDomainIdx(TextualConvention, Unsigned32):
    status = 'current'

class ServiceIdx(TextualConvention, Unsigned32):
    status = 'current'

class StringMaxl128(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class StringMaxl16(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class StringMaxl254(TextualConvention, OctetString):
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class StringMaxl256(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class StringMaxl32(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class StringMaxl50(TextualConvention, OctetString):
    status = 'current'
    displayHint = '50a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 50)

class StringMaxl64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class StringSci(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TxPowerLvl(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483640, 2147483640)

class UpDownEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("down", 0), ("up", 1))

class VendorDateString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '9a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 9)

class VendorRvString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class WlSpacing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("fixed50ghz", 0), ("fixed100ghz", 1), ("fixed200ghz", 2), ("flexgrid", 3))

class XcvrId(TextualConvention, Unsigned32):
    status = 'current'

class XcvrMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("blank", 0), ("mode10gig", 1), ("mode40gig", 2), ("mode100gig", 3), ("mode16qam", 4), ("modeqpsk", 5), ("mode8qam", 6))

class XcvrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notavailable", 0), ("unsupported", 1), ("qsfpplus", 2), ("qsfp28", 3), ("wavelogic3extreme", 4))

class YesNoEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class YesNoNaEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("no", 0), ("yes", 1), ("na", 2))

mibBuilder.exportSymbols("CIENA-WS-TYPEDEFS-MIB", PortName=PortName, StringMaxl64=StringMaxl64, ServiceDomainIdx=ServiceDomainIdx, YesNoEnum=YesNoEnum, RecoverLinkDispersionType=RecoverLinkDispersionType, PYSNMP_MODULE_ID=cienaWsTypedefsMIB, cienaWsTypedefsMIB=cienaWsTypedefsMIB, ModuleTypeEnum=ModuleTypeEnum, LineSysEnum=LineSysEnum, XcvrId=XcvrId, NameString=NameString, EnhancedOptsEnum=EnhancedOptsEnum, DescriptionString=DescriptionString, LicenseStatusEnum=LicenseStatusEnum, ConnectorTypeDescEnum=ConnectorTypeDescEnum, Decimal2Dig=Decimal2Dig, StringSci=StringSci, VendorRvString=VendorRvString, StringMaxl128=StringMaxl128, EnabledDisabledNaEnum=EnabledDisabledNaEnum, Decimal2DigSmall=Decimal2DigSmall, EnabledDisabledEnum=EnabledDisabledEnum, WlSpacing=WlSpacing, XcvrMode=XcvrMode, ModuleTypeBits=ModuleTypeBits, ModemChannel=ModemChannel, ServiceIdx=ServiceIdx, StringMaxl256=StringMaxl256, TxPowerLvl=TxPowerLvl, Decimal3Dig=Decimal3Dig, Decimal1Dig=Decimal1Dig, ModemFrequency=ModemFrequency, XcvrType=XcvrType, PtpId=PtpId, StringMaxl254=StringMaxl254, ChannelsNumber=ChannelsNumber, UpDownEnum=UpDownEnum, StringMaxl50=StringMaxl50, OnOffEnum=OnOffEnum, StringMaxl16=StringMaxl16, PortId=PortId, StringMaxl32=StringMaxl32, MacString=MacString, VendorDateString=VendorDateString, LineModuleTypeBits=LineModuleTypeBits, YesNoNaEnum=YesNoNaEnum)
