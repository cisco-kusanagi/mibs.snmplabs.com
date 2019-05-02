#
# PySNMP MIB module EPON-EOC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EPON-EOC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Bits, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Counter64, Gauge32, iso, Integer32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64", "Gauge32", "iso", "Integer32", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eponeoc = ModuleIdentity((1, 3, 6, 1, 4, 1, 34592))
if mibBuilder.loadTexts: eponeoc.setLastUpdated('201005271056Z')
if mibBuilder.loadTexts: eponeoc.setOrganization('epon eoc factory.')
if mibBuilder.loadTexts: eponeoc.setContactInfo('')
if mibBuilder.loadTexts: eponeoc.setDescription('epon eoc common mib module')
class OperSwitch(TextualConvention, Integer32):
    description = 'Device function operation switch type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class DeviceStatus(TextualConvention, Integer32):
    description = 'Device work status type. One device or dummy device may have following five work status: notPresent(1): the device is not present (not installed) offline(2):the device is present,but can not be communicated (or failed to get its info) online(3):the device is present and can be communicated normal(4):the device is online and work well abnormal(5): the device is online but work abnormal for some reason'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notPresent", 1), ("offline", 2), ("online", 3), ("normal", 4), ("abnormal", 5))

class DataDirection(TextualConvention, Integer32):
    description = 'A data channel normally have two direction, up and down'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("upstream", 1), ("downstream", 2))

class DeviceOperation(TextualConvention, Integer32):
    description = 'This type defines an operate action aggregate'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("reset", 2), ("default", 3), ("saveConfig", 4), ("restore", 5), ("delete", 6))

class LedStatus(TextualConvention, Integer32):
    description = 'Led status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("on", 1), ("off", 2), ("blink", 3))

class DeviceType(TextualConvention, Integer32):
    description = 'Device type convention. Define all PBB device type value. ---------------------------------- | family | series | class | type | ---------------------------------- 8b 8b 8b 8b refer to document <pducuct type defines>'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16842752, 16843009, 16843265, 16843521, 16909057, 17105153, 17105409, 17105665, 16974081, 16974082, 16974083, 16974084, 16974085, 16974086, 16974087, 16974088, 16974095, 16974094, 16974089, 16974090, 16974091, 16974092, 16974337, 16974338, 16974593, 16974594, 16974849, 17040129, 16974850, 17039617, 825241960, 825307496, 825307757, 825242728, 825308258, 825308269, 858797160))
    namedValues = NamedValues(("EPON", 16842752), ("CHASSIS", 16843009), ("OLT", 16843265), ("PON", 16843521), ("PON", 16909057), ("EPON-1U", 17105153), ("OLT", 17105409), ("PON", 17105665), ("ONU4D-B", 16974081), ("ONU4D-B", 16974082), ("ONU4D-B", 16974083), ("ONU8D-B", 16974084), ("ONU4D", 16974085), ("ONU1D", 16974086), ("ONU1D-G", 16974087), ("ONU2D-G", 16974088), ("ONU2D-GM", 16974095), ("ONU4D-GM", 16974094), ("ONU4D-P", 16974089), ("ONU3D-M", 16974090), ("ONU4D", 16974091), ("ONU2D-M", 16974092), ("ONU4D2P", 16974337), ("ONU4D2P-P", 16974338), ("ONU4D1R", 16974593), ("ONU4D1R-P", 16974594), ("ONU4D2P1R", 16974849), ("ONU4D2P1R", 17040129), ("ONU4D2P1R-P", 16974850), ("ONU24D", 17039617), ("ONU1FE", 825241960), ("ONU1GE", 825307496), ("ONU2GE", 825307757), ("ONU4FE", 825242728), ("ONU4GE", 825308258), ("ONU4GE", 825308269), ("ONU4FE1RF", 858797160))

ipProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1))
if mibBuilder.loadTexts: ipProduct.setStatus('current')
if mibBuilder.loadTexts: ipProduct.setDescription('Defines the base identifier containing the definition of ip products line. ')
mediaConverter = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 1))
if mibBuilder.loadTexts: mediaConverter.setStatus('current')
if mibBuilder.loadTexts: mediaConverter.setDescription('Defines the base identifier for the subtree supported by media converter line products. ')
switch = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 2))
if mibBuilder.loadTexts: switch.setStatus('current')
if mibBuilder.loadTexts: switch.setDescription('Defines the base identifier for the subtree supported by smartCPE Switch line products. ')
epon = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 3))
if mibBuilder.loadTexts: epon.setStatus('current')
if mibBuilder.loadTexts: epon.setDescription('')
eoc = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 4))
if mibBuilder.loadTexts: eoc.setStatus('current')
if mibBuilder.loadTexts: eoc.setDescription('')
mibBuilder.exportSymbols("EPON-EOC-MIB", LedStatus=LedStatus, DataDirection=DataDirection, epon=epon, PYSNMP_MODULE_ID=eponeoc, DeviceStatus=DeviceStatus, OperSwitch=OperSwitch, eoc=eoc, eponeoc=eponeoc, ipProduct=ipProduct, mediaConverter=mediaConverter, switch=switch, DeviceOperation=DeviceOperation, DeviceType=DeviceType)
