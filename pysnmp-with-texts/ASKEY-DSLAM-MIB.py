#
# PySNMP MIB module ASKEY-DSLAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASKEY-DSLAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Counter64, IpAddress, NotificationType, Integer32, enterprises, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "IpAddress", "NotificationType", "Integer32", "enterprises", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
askey = ModuleIdentity((1, 3, 6, 1, 4, 1, 3646))
if mibBuilder.loadTexts: askey.setLastUpdated('200311250000Z')
if mibBuilder.loadTexts: askey.setOrganization('ASKEY Inc.')
if mibBuilder.loadTexts: askey.setContactInfo('ASKEY Inc. E-mail: cwfu@askey.com.tw')
if mibBuilder.loadTexts: askey.setDescription('ASKEY DSLAM MIB OID defines and documentation.')
class AskeyVendorTypeEnum(TextualConvention, Integer32):
    description = 'Defines the enumeration of Askey vendor types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 458759, 458762, 458763, 458764, 458765, 458767, 458768, 458769, 458770, 458771, 458772, 458773, 458774))
    namedValues = NamedValues(("noEntity", 1), ("other", 2), ("am0031Chassis", 3), ("am0031BackPlane", 4), ("genericEmptySlot", 5), ("cpuSlot", 6), ("lineCardSlot", 7), ("powerSlot", 8), ("fanSlot", 9), ("am0031CpuModule", 10), ("am0031AdslModule", 11), ("am0031PowerModule", 12), ("am0031FanModule", 13), ("genericAdslPort", 14), ("bcm6430fAdslPort", 15), ("gePort", 16), ("alarmRelayModule", 17), ("alarmRelayPort", 18), ("am0031VdslModule", 19), ("am0031ShdslModule", 20), ("am0031ShdslPort", 21), ("am0021Chassis", 458759), ("am0021CpuModuleX2GE", 458762), ("am0021AdslModule", 458763), ("am0021PowerModule", 458764), ("am0021FanModule", 458765), ("am0021AdslPort", 458767), ("am0021GePort", 458768), ("am0021AlarmRelayModule", 458769), ("am0021AlarmRelayPort", 458770), ("am0021VdslModule", 458771), ("am0021ShdslModule", 458772), ("am0021ShdslPort", 458773), ("am0021CpuModuleX4GE", 458774))

asd300 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300))
swv011 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 1))
swt011 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 2))
swv031 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 3))
swf011 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 4))
swt012 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 5))
am0031 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 6))
am0021 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 7))
ama1011 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 8))
ams1011 = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 9))
unDefinedDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 300, 999))
ipDslam = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2))
mibBuilder.exportSymbols("ASKEY-DSLAM-MIB", ams1011=ams1011, asd300=asd300, ama1011=ama1011, AskeyVendorTypeEnum=AskeyVendorTypeEnum, swt012=swt012, swt011=swt011, swf011=swf011, askey=askey, am0031=am0031, am0021=am0021, swv031=swv031, unDefinedDevice=unDefinedDevice, ipDslam=ipDslam, swv011=swv011, PYSNMP_MODULE_ID=askey)
